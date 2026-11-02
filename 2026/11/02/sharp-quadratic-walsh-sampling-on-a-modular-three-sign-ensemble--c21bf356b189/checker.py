"""Exact moment and numerical Gram checks for modular-three Walsh sampling."""
from itertools import product, combinations
from fractions import Fraction
from math import comb, sqrt
import numpy as np

def spectrum(n):
    eps=(-1)**n; D=2**n+2*eps
    a=Fraction(-6*eps,D); b=Fraction(18*eps,D)
    M=comb(n,2)
    edge_standard=1+(n-4)*a-(n-3)*b
    edge_second=1-2*a+b
    odd_standard=1-a
    odd_trivial=1+(n-1)*a
    e0=1+2*(n-2)*a+comb(n-2,2)*b
    mat=np.array([[1.0, float(a)*sqrt(M)],[float(a)*sqrt(M),float(e0)]])
    e0plus,e0minus=np.linalg.eigvalsh(mat)[::-1]
    return {'odd_standard':(float(odd_standard),n-1),'odd_trivial':(float(odd_trivial),1),
            'edge_standard':(float(edge_standard),n-1),'edge_second':(float(edge_second),n*(n-3)//2),
            'scalar_plus':(e0plus,1),'scalar_minus':(e0minus,1)},a,b

def run():
    checks=0; eigenchecks=0
    for n in range(3,12):
        pts=[x for x in product((-1,1),repeat=n) if sum(x)%3==0]
        D=2**n+2*((-1)**n)
        assert len(pts)*3==D,(n,len(pts),D)
        # exact moments for all subsets of sizes 1..4, where meaningful
        for s in range(1,min(4,n)+1):
            for ind in combinations(range(n),s):
                obs=Fraction(sum(__import__('math').prod(x[i] for i in ind) for x in pts),len(pts))
                expected=Fraction(0) if s%2 else Fraction(2*(-1)**n*(-3)**(s//2),D)
                assert obs==expected,(n,ind,obs,expected)
                checks+=1
        if n>=4:
            ids=[()] + [(i,) for i in range(n)] + list(combinations(range(n),2))
            F=np.array([[np.prod([x[i] for i in ind]) for ind in ids] for x in pts], dtype=float)
            G=(F.T@F)/len(pts)
            ev=np.linalg.eigvalsh(G)
            vals,_,_=spectrum(n)
            expected=sorted(e for name,(v,m) in vals.items() for e in [v]*m)
            assert len(ev)==len(expected)
            assert np.max(np.abs(ev-expected))<5e-12,(n,ev,expected)
            eigenchecks+=len(ev)
            if n>=8: assert ev[0]>0
        print(f'n={n}, rows={len(pts)}, exact_moment_checks_cumulative={checks}, all_eigenvalues_checked={(n>=4)}')
    print(f'PASS exact moment identities={checks}, independently assembled Gram eigenvalues={eigenchecks}')

if __name__=='__main__':run()
