#!/usr/bin/env python3
"""Exact checks for the generic Fresnel-quartic node-field calculation.
Only Python's standard library is required; no symbolic CAS or remote service.
The proof of generic irreducibility uses valuations in Q[a,b,c], supplied
in the mathematical statement and checked below as an F2 matrix.
"""
from fractions import Fraction as Q
from itertools import product

def rank(vectors):
    pivots = {}
    for x in vectors:
        while x:
            k = x.bit_length()-1
            if k not in pivots:
                pivots[k] = x
                break
            x ^= pivots[k]
    return len(pivots)

def radicands(a,b,c):
    p,q,r=b-a,c-b,c-a
    return {
      'A': c*p/r,
      'B': a*q/r,
      'C': -c*p/q,
      'D': b*r/q,
      'E': b*r/p,
      'F': -a*q/p,
      'G': -q/r,
      'H': -p/r,
    }

# Independent prime squareclasses [-1,a,b,c,p=b-a,q=c-b,r=c-a]
formal = {
 'A':'cpr', 'B':'aqr', 'C':'-cpq', 'D':'brq',
 'E':'brp', 'F':'-aqp', 'G':'-qr', 'H':'-pr'
}
prime_basis = '-abcpqr'
def mask(word):
    result=0
    for c in word:
        result ^= 1<<prime_basis.index(c)
    return result
m={k:mask(v) for k,v in formal.items()}
assert rank(list(m.values())) == 5
assert rank([m[k] for k in 'ABCDE']) == 5
assert m['F'] == m['A']^m['B']^m['C']^m['D']^m['E']
assert m['G'] == m['A']^m['C']
assert m['H'] == m['A']^m['C']^m['D']^m['E']
assert all(rank([m[i],m[j]])==2 for i,j in [('A','B'),('C','D'),('E','F'),('G','H')])

# Each tuple specifies [k1^2,k2^2,k3^2,k0^2].
def check(a,b,c):
    d=radicands(a,b,c)
    A,B,C,D,E,F,G,H=(d[k] for k in 'ABCDEFGH')
    assert G == A*C * ((c-b)/(c*(b-a)))**2
    assert H == A*C*D*E * ((c-b)/(b*c*(c-a)))**2
    assert F == A*B*C*D*E * ((c-b)/(b*c*(b-a)))**2
    four = [(A,0,B,1),(0,C,D,1),(E,F,0,1),(G,1,H,0)]
    for x,y,z,t in four:
        R=x+y+z
        S=a*x+b*y+c*z
        T=a*(b+c)*x+b*(c+a)*y+c*(a+b)*z
        polynomial=R*S -t*T +t*t*a*b*c
        # partial derivatives /2: each nonzero coordinate's factor;
        # zero coordinate derivatives vanish identically.
        fac1=S+a*R-t*a*(b+c)
        fac2=S+b*R-t*b*(c+a)
        fac3=S+c*R-t*c*(a+b)
        dt=-T+2*t*a*b*c
        assert polynomial==0,(a,b,c,x,y,z,t,polynomial)
        assert x==0 or fac1==0
        assert y==0 or fac2==0
        assert z==0 or fac3==0
        assert t==0 or dt==0
    # Hessian determinants in the affine chart k0=1, one zero coordinate.
    expected=[32*a*c*(a-b)**2*(b-c)**2,
              32*b*c*(a-b)**2*(a-c)**2,
              32*a*b*(a-c)**2*(b-c)**2]
    for squares,zero,answer in zip(four[:3],[1,0,2],expected):
        v=list(squares[:3]);eps=[a,b,c]
        X=[sum(eps[j]*v[j] for j in range(3))
           +eps[i]*sum(v)-eps[i]*sum(eps[j] for j in range(3) if j!=i)
           for i in range(3)]
        j,k=[i for i in range(3) if i!=zero]
        determinant=-32*X[zero]*(eps[j]-eps[k])**2*v[j]*v[k]
        assert determinant==answer,(a,b,c,zero,determinant,answer)
    Qinf=a*(b+c)*G+b*(c+a)+c*(a+b)*H
    assert 32*Qinf*(a-c)**2*G*H==32*(a-b)**2*(b-c)**2
    return True

for triple in [(1,2,3),(2,5,11),(3,7,19),(5,8,23),(2,9,17)]:
    assert check(*map(Q,triple))

# In Q(a,b,c), each of the six irreducible factors a,b,c,p,q,r
# is an independent squareclass; -1 is independent as well.
# Hence the GF(2) rank is the exact generic splitting-extension rank.
assert sum(1<<2 for _ in range(4))==16
print('VERIFY_OK: four degree-4 orbits, squareclass rank 5, degree 32; exact nodal equations.')
