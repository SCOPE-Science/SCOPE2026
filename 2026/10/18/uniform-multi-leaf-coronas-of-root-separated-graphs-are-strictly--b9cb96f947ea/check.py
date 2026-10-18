from fractions import Fraction
from math import comb
import itertools
import sympy as s
z=s.Symbol('z')

def ip_path(n):
    if n==0:return s.Poly(1,z)
    p0,p1=s.Poly(1,z),s.Poly(1+z,z)
    if n==1:return p1
    for j in range(2,n+1):p0,p1=p1,p1+s.Poly(z,z)*p0
    return p1

def ip_cycle(n):
    return ip_path(n-1)+s.Poly(z,z)*ip_path(n-3)


def ip_graph(adj):
    N=len(adj); coeff=[0]*(N+1)
    for mask in range(1<<N):
        if all((mask>>i&1)==0 or all((mask>>j&1)==0 for j in adj[i]) for i in range(N)):
            coeff[mask.bit_count()]+=1
    return s.Poly(sum(v*z**i for i,v in enumerate(coeff)),z)

def graph_corona(core_n,edges,m):
    nn=core_n*(m+1)
    adj=[set() for _ in range(nn)]
    for i,j in edges: adj[i].add(j);adj[j].add(i)
    for i in range(core_n):
        for k in range(m):
            j=core_n+i*m+k
            adj[i].add(j);adj[j].add(i)
    return adj

def hurwitz_poly(poly):
    coeff=list(reversed([s.sympify(v) for v in s.Poly(poly,z).all_coeffs()])) # constant upward
    d=len(coeff)-1
    # H[i,j] = a_(2*j-i+1) in polynomial coeff ascending? conventional polynomial descending c0..cd
    desc=list(reversed(coeff))
    H=s.zeros(d,d)
    for i in range(d):
        for j in range(d):
            k=2*(j+1)-(i+1)
            if 0<=k<=d: H[i,j]=desc[k]
    dets=[H[:k,:k].det(method='domain-ge') for k in range(1,d+1)]
    return all(v>0 for v in dets),dets

# Independent brute-graph subset counts vs corona substitution on 2..5 cores with 1..3 leaves.
case_count=0
for kind in ['path','cycle']:
  for n in range(2,6):
    if kind=='cycle' and n<3:continue
    for m in range(1,4):
      if n*(m+1)>18:continue
      edges=[(i,i+1) for i in range(n-1)]+([(n-1,0)] if kind=='cycle' else [])
      actual=ip_graph(graph_corona(n,edges,m))
      core=ip_path(n) if kind=='path' else ip_cycle(n)
      expected=s.Poly(sum(int(core.nth(k))*z**k*(1+z)**(m*(n-k)) for k in range(core.degree()+1)),z)
      assert actual==expected,(kind,n,m)
      case_count+=1
print('exact subset-to-formula comparisons:',case_count)

# Scalar factor Hurwitz determinants: positive rational a, direct exact determinants.
case_count=0
for m in range(1,11):
    for a in (s.Rational(1,4),s.Rational(1,3),s.Rational(1,2),s.Rational(3,4),s.Integer(1),s.Integer(4)):
        assert hurwitz_poly(s.expand(z+a*(1+z)**m))[0],(m,a)
        case_count+=1
print('exact Hurwitz scalar checks:',case_count)

# Boundary examples around t=19/20 at m=4; scaled f=(1+z)^4+t*z.
for t in [19,20,21]:
    ok,ds=hurwitz_poly(s.expand((1+z)**4+t*z))
    print('K_t leaf corona critical t=',t,'stable:',ok,'dets:',ds)
    assert ok==(t<=19)

# Algebraic bound b7 < 1/4.
assert 16*6**6<7**7
print('proof-side inequality: 16*6^6 < 7^7 verified')
print('ALL_TESTS_PASSED')
