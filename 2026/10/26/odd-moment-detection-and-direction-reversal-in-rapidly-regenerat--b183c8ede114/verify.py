"""Exact finite-path checks for the odd-moment velocity criterion."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import prod

def annealed_mean(n, atoms, weights):
    @lru_cache(None)
    def site(r, l):
        return sum(p * w**r * (1-w)**l for w,p in zip(atoms,weights))
    result=F(0)
    for steps in product((-1,1),repeat=n):
        counts={}; x=0
        for d in steps:
            counts.setdefault(x,[0,0])[int(d==1)] += 1
            x+=d
        result+=x*prod(site(c[1],c[0]) for c in counts.values())
    return result

def check(atoms,weights,r):
    assert sum(weights)==1
    assert sum(w*p for w,p in zip(atoms,weights))==F(1,2)
    moments={k:sum(p*(w-F(1,2))**k for w,p in zip(atoms,weights)) for k in range(2*r+2)}
    assert all(moments[k]==0 for k in range(1,2*r,2))
    assert moments[2*r+1]!=0
    delta=sum(p*q*(x-y)**(2*r) for x,p in zip(atoms,weights) for y,q in zip(atoms,weights))
    expected=2*delta*moments[2*r+1]
    for n in range(1,4*r+1):
        assert annealed_mean(n,atoms,weights)==0, (r,n)
    assert annealed_mean(4*r+1,atoms,weights)==expected
    print(f'r={r}: zero means through {4*r}; coefficient={expected}; exact check PASS')

check([F(1,20),F(2,5),F(4,5)],[F(2,25),F(3,5),F(8,25)],1)
check([F(1,10),F(3,10),F(3,5),F(9,10)],[F(22,125),F(6,25),F(48,125),F(1,5)],2)
assert annealed_mean(7,[F(1,4),F(3,4)],[F(1,2)]*2)==0
print('reflection-symmetric seven-step check PASS')
