#!/usr/bin/env python3
"""Independent finite check of kernel classes and automorphism orbits."""
from itertools import product
from math import prod

def qbinom2(k,p):
    return ((p**k-1)*(p**k-p)//((p*p-1)*(p*p-p))) if k>=2 else 0

def expected(p,k):
    s=(p**k-1)//(p-1)
    g=qbinom2(k,p)
    t= p**(k-2)*s*((p**(k-1)-1)//(p-1)) if k>=2 else 0
    typ=1+(1+p**(k-1))*s+g+t
    orb=typ+s+p*g
    return typ,orb

def test(p,k):
    mod=p*p
    elements=list(product(range(mod),range(p)))
    matrices=[(a,b,c,d) for a in range(mod) if a%p for b in range(p) for c in range(p) for d in range(1,p)]
    def act(M,t):
        a,b,c,d=M;x,y=t
        return ((a*x+p*b*y)%mod,(c*x+d*y)%p)
    alltuples=list(product(elements,repeat=k))
    kerclass={}
    for tup in alltuples:
        kernel=bytes( int(all((sum(z[i]*tup[i][0] for i in range(k))%mod==0,
                              sum(z[i]*tup[i][1] for i in range(k))%p==0)))
                       for z in product(range(mod),repeat=k))
        kerclass.setdefault(kernel,set()).add(tup)
    seen=set(); classes={}
    for tup in alltuples:
        if tup in seen: continue
        orb={tuple(act(M,x) for x in tup) for M in matrices}
        assert tup in orb
        seen.update(orb)
        key=bytes(int(all((sum(z[i]*tup[i][0] for i in range(k))%mod==0,
                           sum(z[i]*tup[i][1] for i in range(k))%p==0)))
                  for z in product(range(mod),repeat=k))
        classes[key]=classes.get(key,0)+1
    assert len(seen)==len(alltuples)
    th,oh=expected(p,k)
    assert len(kerclass)==th, (p,k,len(kerclass),th)
    assert sum(classes.values())==oh,(p,k,sum(classes.values()),oh)
    assert set(classes)==set(kerclass)
    print(f'CASE p={p} k={k} tuples={len(alltuples)} kernels={th} automorphism_orbits={oh} gap={oh-th} PASS')
    return len(alltuples)

def main():
    num=0
    for p,k in [(2,1),(2,2),(2,3),(3,1),(3,2)]:
        num+=test(p,k)
    print(f'VERIFY_OK independent_tuples={num} cases=5 full_kernel_equations=PASS full_automorphism_orbits=PASS')

if __name__=='__main__': main()
