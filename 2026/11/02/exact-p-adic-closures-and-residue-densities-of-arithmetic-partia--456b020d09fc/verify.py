"""Finite independent checks for p-adic orbit-closure formula of arithmetic partial derivatives.

Checks modular orbit via valuation/unit state iteration versus residue unions
predicted by the analytic coset formula. No finite test certifies the general theorem.
"""
from math import gcd

def vp(n, p):
    assert n != 0
    k=0
    while n % p==0:
        n//=p; k+=1
    return k

def val_cycle(a, p):
    seen={}; path=[]
    while a and a not in seen:
        seen[a]=len(path)
        path.append(a)
        a=a-1+vp(a,p)
    if not a: return path, [], len(path)
    i=seen[a]
    return path[:i], path[i:],i

def dynamics(x, p, N):
    mod=p**N
    if x==0: return {0}
    a=vp(abs(x),p)
    unit=(x//(p**a))%mod
    seen=set(); vals=set()
    while (a,unit) not in seen:
        seen.add((a,unit))
        vals.add((unit*pow(p,a,mod))%mod)
        if not a:
            vals.add(0)
            return vals
        k=vp(a,p)
        unit=(unit*(a//(p**k)))%mod
        a=a-1+k
    return vals

def predicted(x,p,N):
    mod=p**N
    if x==0:return {0}
    a=vp(abs(x),p)
    if not a: return {x%mod,0}
    prefix, cyc, t=val_cycle(a,p)
    vals=set(); y=x
    for aa in prefix:
        assert vp(abs(y),p)==aa
        vals.add(y%mod)
        y=(y//p)*aa
    if not cyc:
        vals.add(y%mod)
        vals.add(0)
        return vals
    yjs=[]
    prod=1
    for aa in cyc:
        assert vp(abs(y),p)==aa
        yjs.append(y)
        y=(y//p)*aa
        prod*=aa
    ell=len(cyc)
    assert prod%p**ell==0
    lam=prod//p**ell
    assert lam%p != 0 and y==yjs[0]*lam
    if lam==1: return vals | {z%mod for z in yjs}
    if p==2:
        d=1 if lam%4==1 else 2
    else:
        d=next(j for j in range(1,p) if pow(lam,j,p)==1)
    c=vp(lam**d-1,p)
    assert c>= (2 if p==2 else 1)
    for aa,z in zip(cyc,yjs):
        for r in range(d):
            base=z*lam**r
            M=p**(aa+c)
            if M>=mod:
                vals.add(base%mod)
            else:
                vals.update(range(base%M,mod,M))
    return vals

def test():
    cases=0; count=0; cyclic=0; nontrivial=0
    exemplars={}
    for p,maxN,maxa in [(2,11,52),(3,8,48),(5,6,50),(7,5,50)]:
      for a in range(maxa+1):
        prefix,cycle,t=val_cycle(a,p) if a else ([],[],0)
        if cycle:cyclic+=1
        for u in [1,-1,2,3,-5]:
          if gcd(abs(u),p)>1:continue
          x=u*p**a
          for N in range(1,maxN+1):
            actual=dynamics(x,p,N)
            expected=predicted(x,p,N)
            assert actual==expected, (p,a,u,N,len(actual),len(expected),actual^expected)
            cases+=1
            count+=len(actual)
        if cycle and len(cycle)>1 and p not in exemplars:
            y=p**a
            for aa in prefix:y=(y//p)*aa
            cy=cycle
            lam=1
            for aa in cy:lam*=aa
            lam//=p**len(cy)
            exemplars[p]=(a,cy,lam)
    return {'checked_profiles':cases,'total_attained_residue_instances':count,'nontrivial_cycle_examples':exemplars,'cycles_examined':cyclic,'status':'PASS'}

if __name__=='__main__':
    print(test())
