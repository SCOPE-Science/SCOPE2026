from itertools import product
from fractions import Fraction
from math import comb

def counts_by_paths(par):
    n=len(par)
    cyclic=set(); cycles=[]; seen_global=set()
    for x in range(n):
        if x in seen_global: continue
        path=[]; first={}; v=x
        while v>=0 and v not in first and v not in seen_global:
            first[v]=len(path); path.append(v); v=par[v]
        if v in first:
            cyc=path[first[v]:]; cycles.append(cyc); cyclic.update(cyc)
        seen_global.update(path)
    bad={v for v in range(n) if v in cyclic}
    for v in range(n):
        trail=set(); w=v
        while w>=0 and w not in trail:
            if w in cyclic: bad.add(v); break
            trail.add(w); w=par[w]
    return len(bad),len([x for x in cycles if len(x)%2]),len([x for x in cycles if len(x)%2==0])

def stable_brute(par):
    n=len(par); ans=0
    for mask in range(1<<n):
        if all((((mask>>v)&1)==1) == (par[v]<0 or not (mask>>par[v]&1)) for v in range(n)):
            ans+=1
    return ans

def finite_law(n,p,a,k):
    if k==n:return a**n
    return comb(n,k)*Fraction(a,n)**k * (k**k if k else 1)*p * (p+Fraction(a*(n-k),n))**(n-k-1)

def verify():
    for n in range(1,6):
        p=Fraction(2,5); a=1-p
        hist={k:Fraction(0) for k in range(n+1)}
        total=Fraction(0); z1=Fraction(0); ns=0
        for par in product(range(-1,n),repeat=n):
            ns+=1
            w=p**sum(j<0 for j in par)*Fraction(a,n)**sum(j>=0 for j in par)
            u,odd,even=counts_by_paths(par)
            z=0 if odd else 2**even
            assert stable_brute(par)==z,(n,par,z)
            hist[u]+=w
            z1+=w*(z==1)
            total+=w
        assert total==1
        assert z1==p,(n,z1,p)
        assert all(hist[k]==finite_law(n,p,a,k) for k in hist),(n,hist,{k:finite_law(n,p,a,k) for k in hist})
        print('n=',n,'objects=',ns,'probU0=',hist[0],'probZ1=',z1,'OK')
    print('ALL_CHECKS_OK')
if __name__=='__main__':verify()
