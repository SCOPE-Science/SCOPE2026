"""Independent finite checks for the three-absorber hypercube theorem.

Usage: python verify_three_hypercube_traps.py
Requires only the Python 3 standard library. The checks are finite,
not a substitute for the published-in-package proof for all dimensions.
"""
from itertools import combinations
from math import comb

P=1000003

def modular_rank(a, prime=P):
    if not a: return 0
    a=[[x % prime for x in row] for row in a]
    nrows,ncols=len(a),len(a[0]);r=0
    for c in range(ncols):
        pivot=next((i for i in range(r,nrows) if a[i][c]), None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        z=pow(a[r][c],-1,prime)
        for k in range(c,ncols):a[r][k]=a[r][k]*z%prime
        for i in range(r+1,nrows):
            v=a[i][c]
            if v:
                for k in range(c,ncols):a[i][k]=(a[i][k]-v*a[r][k])%prime
        r+=1
        if r==nrows: break
    return r

def expected_rank(d, traps):
    anti=(1<<d)-1
    has_antipodal=any((x^y)==anti for x,y in combinations(traps,2))
    return 2*d if has_antipodal else 3*d-1

def fourier_rank(d,traps):
    total=0
    for weight in range(d+1):
        rows=[]
        for subset in range(1<<d):
            if subset.bit_count()==weight:
                rows.append([(-1)**((subset&vertex).bit_count()) for vertex in traps])
        total+=modular_rank(rows)
    return total

def krylov_rank(d,traps):
    n=1<<d
    vectors=[]
    for vertex in traps:
        v=[int(s==vertex) for s in range(n)]
        for _ in range(d+1):
            vectors.append(v)
            v=[sum(v[s^(1<<bit)] for bit in range(d)) for s in range(n)]
    return modular_rank([[vector[s] for vector in vectors] for s in range(n)])

def run():
    tests=0
    for d in range(2,7):
        n=1<<d
        anchored=list(combinations(range(1,n),2))
        if d>=6:
            # Deterministic broad sweep, exact at every tested instance.
            anchored=anchored[::13]+anchored[-15:]
        types=set()
        for a,b in anchored:
            traps=(0,a,b)
            target=expected_rank(d,traps)
            fr=fourier_rank(d,traps)
            assert fr==target,(d,traps,'Fourier',fr,target)
            tests+=1
            types.add(target)
            if d<=5 or a%5==0:
                cr=krylov_rank(d,traps)
                assert cr==target,(d,traps,'Krylov',cr,target)
                tests+=1
        print(f'dimension={d}, tested_triples={len(anchored)}, expected_ranks={sorted(types)}')
    # Explicit nontrivial examples at d=3 (full-absorption configuration
    # versus a configuration containing antipodal absorbers).
    assert fourier_rank(3,(0,1,2))==8
    assert fourier_rank(3,(0,7,1))==6
    tests+=2
    print(f'PASS {tests} exact finite rank checks (two independent formulations)')

if __name__=='__main__':run()
