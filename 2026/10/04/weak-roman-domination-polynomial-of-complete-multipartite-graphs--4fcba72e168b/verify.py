#!/usr/bin/env python3
from itertools import combinations, product
from collections import Counter
from math import comb

MAX_ORDER = 8

def compositions(n):
    for r in range(2,n+1):
        for cuts in combinations(range(1,n),r-1):
            out=[]; last=0
            for c in cuts+(n,):
                out.append(c-last); last=c
            yield tuple(out)

def build(ns):
    part=[]
    for i,n in enumerate(ns): part.extend([i]*n)
    N=len(part)
    adj=[[part[u]!=part[v] for v in range(N)] for u in range(N)]
    return part,adj

def safe_support(labels,adj):
    N=len(labels)
    for v in range(N):
        if labels[v]==0 and not any(adj[v][u] and labels[u]>0 for u in range(N)):
            return False
    return True

def literal_wrdf(labels,adj):
    N=len(labels)
    for v in range(N):
        if labels[v]!=0: continue
        ok=False
        for u in range(N):
            if adj[u][v] and labels[u]>0:
                g=list(labels); g[u]-=1; g[v]=1
                if safe_support(g,adj):
                    ok=True; break
        if not ok: return False
    return True

def theorem_wrdf(labels,part,ns):
    J={part[v] for v,a in enumerate(labels) if a>0}
    q=len(J)
    if q>=3: return True
    if q==0: return False
    if q==2:
        i,j=sorted(J)
        wi=sum(labels[v] for v in range(len(labels)) if part[v]==i)
        wj=sum(labels[v] for v in range(len(labels)) if part[v]==j)
        zi=sum(1 for v in range(len(labels)) if part[v]==i and labels[v]==0)
        zj=sum(1 for v in range(len(labels)) if part[v]==j and labels[v]==0)
        return (wj>=2 or zi<=1) and (wi>=2 or zj<=1)
    i=next(iter(J))
    if any(part[v]==i and labels[v]==0 for v in range(len(labels))): return False
    if ns[i]>=2: return True
    val=next(labels[v] for v in range(len(labels)) if part[v]==i)
    if val==2: return True
    return all(n==1 for n in ns)

def padd(a,b,scale=1):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=scale*x
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def ppow(a,n):
    r=[1]
    for _ in range(n): r=pmul(r,a)
    return r

def A(n): return padd(ppow([1,1,1],n),[-1])
def F(n): return ppow([0,1,1],n)
def E(n): return [0,n]
def Estar(n): return [0,n] if n>=3 else [0]
def D(n):
    ans=[0]
    for z in range(2,n):
        term=[comb(n,z)*c for c in ppow([0,1,1],n-z)]
        ans=padd(ans,term)
    return ans

def formula(ns):
    N=sum(ns); r=len(ns); As=[A(n) for n in ns]
    q3=padd(ppow([1,1,1],N),[-1])
    for a in As: q3=padd(q3,a,-1)
    for i,j in combinations(range(r),2): q3=padd(q3,pmul(As[i],As[j]),-1)
    q1=[0]
    for n in ns: q1=padd(q1,F(n))
    if not all(n==1 for n in ns): q1=padd(q1,[0,sum(n==1 for n in ns)],-1)
    q2=[0]
    for i,j in combinations(range(r),2):
        v=pmul(As[i],As[j])
        v=padd(v,pmul(D(ns[i]),E(ns[j])),-1)
        v=padd(v,pmul(E(ns[i]),D(ns[j])),-1)
        v=padd(v,pmul(Estar(ns[i]),Estar(ns[j])))
        q2=padd(q2,v)
    return padd(padd(q1,q2),q3)

def main():
    profiles=labelings=coeff_checks=0
    for N in range(2,MAX_ORDER+1):
        for ns in compositions(N):
            profiles+=1
            part,adj=build(ns)
            hist=Counter()
            for lab in product(range(3),repeat=N):
                labelings+=1
                a=literal_wrdf(lab,adj)
                b=theorem_wrdf(lab,part,ns)
                if a!=b: raise AssertionError(('membership',ns,lab,a,b))
                if a: hist[sum(lab)]+=1
            brute=[0]*(2*N+1)
            for k,v in hist.items(): brute[k]=v
            while len(brute)>1 and brute[-1]==0: brute.pop()
            form=formula(ns)
            coeff_checks+=max(len(brute),len(form))
            if brute!=form: raise AssertionError(('coefficients',ns,brute,form))
    print(f'VERIFY_OK graph_profiles={profiles} labelings={labelings} coefficient_checks={coeff_checks} max_order={MAX_ORDER}')

if __name__=='__main__': main()
