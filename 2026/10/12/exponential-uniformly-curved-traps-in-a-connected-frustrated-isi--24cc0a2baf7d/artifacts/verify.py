"""Exact-rational finite transcription checks for a weighted frustrated-triangle chain.
This is not a proof for all system sizes; the accompanying mathematics is analytic.
"""
from fractions import Fraction as F
from itertools import product

EPS=F(1,100)
H=(F(1,10),F(1,5),F(3,10))
assert 0<EPS<H[0]<H[1]<H[2]<2-EPS
assert H[1]-H[0]>2*EPS

def hamiltonian(s,m):
    e=F(0)
    for j in range(m):
        a,b,c=s[3*j:3*j+3]
        e+=a*b+b*c+c*a-H[0]*a-H[1]*b-H[2]*c
    for j in range(m-1):
        e+=EPS*s[3*j+2]*s[3*j+3]
    return e

def curvature(s,m):
    diag=[]
    for j in range(m):
        for k in range(3):
            i=3*j+k
            ell=s[3*j+(k+1)%3]+s[3*j+(k+2)%3]-H[k]
            if k==0 and j>0:
                ell+=EPS*s[3*j-1]
            if k==2 and j<m-1:
                ell+=EPS*s[3*j+3]
            diag.append(-s[i]*ell)
    return diag

# Exhaustive finite checkpoints, not a universal proof.
for m in range(1,5):
    low=min(H[0]-EPS,2-H[2]-EPS)
    high=max(H[2]+EPS,2-H[0]+EPS)
    spin_vertices=list(product((-1,1),repeat=3*m))
    strict=[s for s in spin_vertices if min(curvature(s,m))>0]
    assert len(strict)==3**m
    assert all(all(s[3*j:3*j+3].count(-1)==1 for j in range(m)) for s in strict)
    assert all(low<=v<=high for s in strict for v in curvature(s,m))
    preferred=tuple(x for _ in range(m) for x in (-1,1,1))
    emin=min(hamiltonian(s,m) for s in spin_vertices)
    global_vertices=[s for s in spin_vertices if hamiltonian(s,m)==emin]
    assert global_vertices==[preferred]
    gap=2*(H[1]-H[0]-2*EPS)
    assert all(hamiltonian(s,m)-emin>=gap for s in strict if s!=preferred)
    # Each vertex has two unit edges, and each bridge adds one squared
    # edge strength to two incident vertices.
    sum_local_squared=6*m+2*(m-1)*EPS**2
    sum_field_squared=m*sum(h*h for h in H)
    moment_from_sites=(sum_local_squared/F(4)+sum_field_squared/F(2))/(3*m)
    moment_closed=F(1,2)+sum(h*h for h in H)/6+EPS**2*F(m-1,6*m)
    assert moment_from_sites==moment_closed
    assert moment_closed>=F(1,2)
print('VERIFY_OK')
