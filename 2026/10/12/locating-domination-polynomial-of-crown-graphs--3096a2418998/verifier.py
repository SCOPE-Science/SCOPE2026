from itertools import combinations
from collections import Counter
from math import factorial

def crown_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                a=i; b=n+j
                adj[a].add(b); adj[b].add(a)
    return adj

def is_ld(n,S):
    adj=crown_adj(n); S=set(S)
    outside=[v for v in range(2*n) if v not in S]
    sig=[]
    for v in outside:
        q=adj[v]&S
        if not q: return False
        sig.append(frozenset(q))
    return len(sig)==len(set(sig))

def classified(n,S):
    S=set(S)
    I={i for i in range(n) if i not in S}
    J={i for i in range(n) if n+i not in S}
    if len(I&J)>1: return False
    if I:
        selB=[j for j in range(n) if j not in J]
        if not selB: return False
        if len(selB)==1 and selB[0] in I: return False
    if J:
        selA=[i for i in range(n) if i not in I]
        if not selA: return False
        if len(selA)==1 and selA[0] in J: return False
    return True

def multinom3(m,c,d,e):
    if min(c,d,e)<0 or c+d+e!=m: return 0
    return factorial(m)//(factorial(c)*factorial(d)*factorial(e))

def predicted_coeff(n,a,b):
    c=a+b-n; d=n-b; e=n-a
    val=multinom3(n,c,d,e)
    m=n-1; c=a+b-m; d=m-b; e=m-a
    val += n*multinom3(m,c,d,e)
    if (a,b)==(n-1,0): val-=n
    if (a,b)==(0,n-1): val-=n
    if (a,b)==(n-1,1): val-=n
    if (a,b)==(1,n-1): val-=n
    if (a,b)==(n-2,1): val-=n*(n-1)
    if (a,b)==(1,n-2): val-=n*(n-1)
    return val

def run():
    subset_checks=classification_checks=coefficient_checks=0
    total_ld=0
    for n in range(5,8):
        cnt=Counter()
        for mask in range(1<<(2*n)):
            S={v for v in range(2*n) if (mask>>v)&1}
            a=sum(i in S for i in range(n)); b=sum(n+i in S for i in range(n))
            ld=is_ld(n,S); cl=classified(n,S)
            subset_checks+=1; classification_checks+=1
            if ld!=cl: raise AssertionError((n,mask,ld,cl))
            if ld: cnt[(a,b)]+=1; total_ld+=1
        for a in range(n+1):
            for b in range(n+1):
                coefficient_checks+=1
                if cnt[(a,b)]!=predicted_coeff(n,a,b):
                    raise AssertionError(('coeff',n,a,b,cnt[(a,b)],predicted_coeff(n,a,b)))
        minsize=min(a+b for (a,b),v in cnt.items() if v)
        mincount=sum(v for (a,b),v in cnt.items() if v and a+b==minsize)
        if minsize!=n-1: raise AssertionError(('min',n,minsize))
        if mincount!=n*(2**(n-1)-2*n): raise AssertionError(('mincount',n,mincount))
        total=sum(cnt.values())
        if total!=(n+3)*3**(n-1)-2*n*(n+1): raise AssertionError(('total',n,total))
    print(f'VERIFY_OK n_range=5..7 subset_checks={subset_checks} classification_checks={classification_checks} coefficient_checks={coefficient_checks} ld_sets={total_ld} max_order=14')
if __name__=='__main__': run()
