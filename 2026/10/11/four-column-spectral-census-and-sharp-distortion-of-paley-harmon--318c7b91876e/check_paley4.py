#!/usr/bin/env python3
"""Reproduce the four-column spectrum and tournament census for a quadratic-residue harmonic frame."""
import itertools
import math
from collections import Counter
import numpy as np
import sympy as sp

PAIRS = tuple(itertools.combinations(range(4),2))
PERMS = tuple(itertools.permutations(range(4)))
TYPES = {
    (-1,-1,-1,-1,-1,-1): 'transitive',
    (-1,-1,-1,-1, 1,-1): 'source_or_sink_cycle',
    (-1,-1, 1,-1,-1,-1): 'strong',
    (-1,-1, 1,-1,-1, 1): 'source_or_sink_cycle',
}

def orientation(bits):
    A = np.zeros((4,4), dtype=int)
    for (i,j),bit in zip(PAIRS,bits):
        A[i,j] = bit
        A[j,i] = -bit
    return A

def canonical(bits):
    A = orientation(bits)
    return min(tuple(int(A[v[i],v[j]]) for i,j in PAIRS) for v in PERMS)

p,z=sp.symbols('p z', real=True); t=sp.Symbol('t')
PT=t**4-6*(p+1)*t**2+8*(p+1)*t+p**2-2*p-3
PS=t**4-6*(p+1)*t**2+8*(1-p)*t+p**2+14*p-3
PD=(3*p-t*t-2*t+3)*(3*p-t*t+2*t-1)
for pattern,label in TYPES.items():
    A=sp.Matrix(orientation(pattern).tolist())
    H=-(sp.ones(4)-sp.eye(4))+z*A
    poly=sp.expand(H.charpoly(t).as_expr()).subs(z**4,p*p).subs(z**2,-p).expand()
    expected=PT if label=='transitive' else PS if label=='strong' else PD
    assert sp.simplify(poly-expected)==0, (pattern, sp.factor(poly-expected))
assert sp.simplify(PS-PT-16*p*(1-t))==0
assert sp.simplify(PT.subs(t,-t)-PS)==-16*(p+t)
r=1+sp.sqrt(3*p+4)
assert sp.simplify(PT.subs(t,-r)+8*p*(p+sp.sqrt(3*p+4)+2))==0

cases=0
for prime in (7,11,19,23):
    assert sp.isprime(prime) and prime%4==3
    residues={a*a % prime for a in range(1,prime)}
    m=(prime-1)//2
    freqs=sorted(residues)
    F=np.exp(2j*np.pi*np.outer(freqs,np.arange(prime))/prime)/np.sqrt(m)
    count=Counter()
    for indices in itertools.combinations(range(prime),4):
        orient=tuple(1 if ((indices[j]-indices[i])%prime) in residues else -1 for i,j in PAIRS)
        label=TYPES[canonical(orient)]
        count[label]+=1
        W=F[:,indices]
        G=W.conj().T@W
        H=(prime-1)*(G-np.eye(4))
        calc=np.poly(H)  # Descending polynomial coefficients.
        expect=PT if label=='transitive' else PS if label=='strong' else PD
        target=np.array([float(c) for c in sp.Poly(expect.subs(p,prime),t).all_coeffs()])
        assert np.max(np.abs(calc-target)) < 3e-7, (prime,indices,calc,target)
        cases+=1
    nt=prime*(prime-1)*(prime-3)*(prime-7)//64
    nd=prime*(prime-1)*(prime-3)*(prime+1)//96
    ns=prime*(prime-1)*(prime-3)*(prime+1)//64
    assert all(count[l]==v for l,v in [('transitive',nt),('source_or_sink_cycle',nd),('strong',ns)]),(prime,count,nt,nd,ns)
print('VERIFY_OK exact_symbolic_characteristic_polynomials_and_comparison_identites=PASS exhaustive_4subsets=',cases,' primes=[7,11,19,23] counts=PASS')
