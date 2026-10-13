from itertools import product
from collections import Counter

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def powpoly(a,k):
    r=[1]
    for _ in range(k):
        r=conv(r,a)
    return r

def add_shift(out,p,s):
    if len(out)<len(p)+s:
        out += [0]*(len(p)+s-len(out))
    for i,v in enumerate(p):
        out[i+s]+=v

def formula(k):
    T=[1,2,3,2,1]
    A=[0,2,3,2,1]
    B=[0,0,3,2,1]
    out=[]
    add_shift(out,powpoly(B,k),0)
    add_shift(out,powpoly(A,k),1)
    add_shift(out,powpoly(T,k),2)
    return out

def brute(k):
    n=1+2*k
    adj=[set() for _ in range(n)]
    for i in range(k):
        u=1+2*i; v=u+1
        for w in (u,v):
            adj[0].add(w); adj[w].add(0)
        adj[u].add(v); adj[v].add(u)
    c=Counter()
    for lab in product(range(3), repeat=n):
        if all(x!=0 or sum(lab[u] for u in adj[v])>=2 for v,x in enumerate(lab)):
            c[sum(lab)]+=1
    out=[0]*(2*n+1)
    for w,z in c.items(): out[w]=z
    return out

def main():
    total_labelings=0
    for k in range(1,6):
        b=brute(k)
        f=formula(k)+[0]*max(0,len(b)-len(formula(k)))
        assert b==f
        assert sum(b)==6**k+8**k+9**k
        gamma=next(i for i,v in enumerate(b) if v)
        assert gamma==2
        if k>=2:
            assert b[2]==1
        total_labelings += 3**(2*k+1)
        print(f"k={k}; gamma={gamma}; min_count={b[2]}; total_idfs={sum(b)}")
    print(f"ALL CHECKS PASSED; k_range=1..5; labelings_checked={total_labelings}")

if __name__=='__main__':
    main()
