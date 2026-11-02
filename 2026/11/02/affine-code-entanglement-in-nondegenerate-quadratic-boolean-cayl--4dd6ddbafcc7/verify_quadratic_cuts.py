"""Standalone exact checks for affine-flat cuts in quadratic Cayley graph states.

Usage: python verify_quadratic_cuts.py
Requires Python 3.9+ and NumPy for the small direct-state tests.
"""
from itertools import combinations
import random
import numpy as np

def parity(x):
    return x.bit_count() & 1

def rank2(rows):
    pivots={}
    for r in rows:
        v=int(r)
        while v:
            j=v.bit_length()-1
            if j in pivots:
                v^=pivots[j]
            else:
                pivots[j]=v
                break
    return len(pivots)

def standard_quadratic(x,d):
    return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(d//2)) & 1

def random_quadratic(d,rng):
    # Invertible linear substitution gives a nondegenerate polar form.
    rows=[]
    while len(rows)<d:
        r=rng.randrange(1,1<<d)
        if rank2(rows+[r])>len(rows):
            rows.append(r)
    lin=rng.randrange(1<<d)
    def q(x):
        y=sum(parity(x&r)<<i for i,r in enumerate(rows))
        return standard_quadratic(y,d)^parity(lin&x)
    def b(x,y):
        return q(x)^q(y)^q(x^y)
    return q,b

def all_linear_flats(d,k):
    # Unique row-reduced basis for each subspace.
    for piv in combinations(range(d),k):
        nonpiv=[j for j in range(d) if j not in piv]
        positions=[(i,j) for i in range(k) for j in nonpiv if j>piv[i]]
        for mask in range(1<<len(positions)):
            basis=[1<<p for p in piv]
            for t,(i,j) in enumerate(positions):
                if (mask>>t)&1:basis[i]^=1<<j
            U=[0]
            for v in basis:
                U += [x^v for x in U]
            yield tuple(U)

def random_linear_flat(d,k,rng):
    basis=[]
    while len(basis)<k:
        x=rng.randrange(1,1<<d)
        if rank2(basis+[x])>len(basis):basis.append(x)
    U=[0]
    for v in basis:
        U += [x^v for x in U]
    return tuple(U)

def matrix_rank_for_cut(d,q,U,a):
    A=set(a^u for u in U)
    B=[x for x in range(1<<d) if x not in A]
    rows=[sum(q(x^y)<<j for j,y in enumerate(B)) for x in A]
    return rank2(rows)

def theoretical_rank(d,b,U):
    k=(len(U)).bit_length()-1
    if k==d-1:
        return d
    iso=all(b(x,y)==0 for x in U for y in U)
    return k+1+(not iso)

def test_exact_flats():
    rng=random.Random(72623)
    counts={}
    for d in (4,6):
        count=0
        for trial in range(6 if d==4 else 3):
            q,b=random_quadratic(d,rng)
            for k in range(d):
                flats=list(all_linear_flats(d,k)) if d==4 else [random_linear_flat(d,k,rng) for _ in range(35)]
                for U in flats:
                    a_list=list(range(1<<d)) if d==4 else [rng.randrange(1<<d) for _ in range(4)]
                    predicted=theoretical_rank(d,b,U)
                    for a in a_list:
                        observed=matrix_rank_for_cut(d,q,U,a)
                        assert observed==predicted,(d,k,a,predicted,observed)
                        count+=1
        counts[d]=count
    # Independent larger-dimension checks across all permitted dimensions.
    d=8
    count=0
    q,b=random_quadratic(d,rng)
    for k in range(d):
        for _ in range(12):
            U=random_linear_flat(d,k,rng)
            a=rng.randrange(1<<d)
            got=matrix_rank_for_cut(d,q,U,a)
            expect=theoretical_rank(d,b,U)
            assert got==expect,(d,k,a,got,expect)
            count+=1
    counts[d]=count
    return counts

def graph_state_reduced_spectrum(d,q,subset):
    # Explicitly prepare all 2**(2**d) computational-basis amplitudes.
    n=1<<d
    configurations=np.arange(1<<n,dtype=np.uint32)
    phase=np.zeros(1<<n,dtype=np.uint8)
    for u in range(n):
        for v in range(u+1,n):
            if q(u^v):
                phase ^= (((configurations>>u)&1) & ((configurations>>v)&1)).astype(np.uint8)
    state=(1-2*phase.astype(np.int16)).astype(np.float64)/np.sqrt(1<<n)
    complement=[u for u in range(n) if u not in subset]
    order=list(subset)+complement
    # Reshape in increasing-significance-bit convention, then reorder axes.
    tensor=state.reshape((2,)*n)
    matrix=np.transpose(tensor,axes=[n-1-u for u in order]).reshape((1<<len(subset),-1))
    eigenvalues=np.linalg.eigvalsh(matrix@matrix.T)
    eigenvalues=np.where(eigenvalues<1e-11,0,eigenvalues)
    return eigenvalues

def test_direct_quantum():
    d=4
    errors=[]
    count=0
    degrees=[]
    cuts=[(1,(0,1)),(2,(0,1,4,5)),(2,(0,1,2,3)),(3,tuple(range(8)))]
    for lin in (0,3):
        def q(x):return standard_quadratic(x,d)^parity(lin&x)
        def polar(x,y):return q(x)^q(y)^q(x^y)
        degrees.append(sum(q(x) for x in range(1<<d)))
        for k,U in cuts:
            a=(lin*4)&15
            subset=sorted(a^u for u in U)
            r=theoretical_rank(d,polar,U)
            ev=np.sort(graph_state_reduced_spectrum(d,q,subset))
            target=np.array([0.]*(len(ev)-(1<<r))+[2.**(-r)]*(1<<r))
            err=np.max(np.abs(ev-target))
            assert err<1e-11,(lin,k,r,err,ev)
            errors.append(err)
            count+=1
    assert degrees==[6,10],degrees
    return count,max(errors),degrees

if __name__=='__main__':
    print('exact_cut_ranks',test_exact_flats(),flush=True)
    n,e,degrees=test_direct_quantum()
    print('direct_graph_state_spectra',n,'max_abs_error',format(e,'.5g'),'graph_degrees',degrees,flush=True)
    print('PASS',flush=True)
