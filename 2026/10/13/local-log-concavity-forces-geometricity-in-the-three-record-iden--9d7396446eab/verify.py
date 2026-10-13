from fractions import Fraction
import sympy as sp

p1,p2=sp.symbols('p1 p2', positive=True)
Q1=1-p1
Q2=1-p1-p2
p3=sp.factor(p1**2*Q1*Q2/p2)
p4=sp.factor(p1*Q1*Q2)
D2=sp.factor(p2**2-p1*p3)
D3=sp.factor(p3**2-p2*p4)
assert sp.simplify(D3 + (p1*Q1*Q2/p2)*D2)==0
p,q,r=sp.symbols('p q r', positive=True)
expr=sp.expand(q*r**3+p*r-1).subs(q,1-p)
assert sp.expand(expr-(r-1)*((1-p)*r**2+(1-p)*r+1))==0

# Exact finite consistency check for a geometric law p=2/5 through total 18.
pv=Fraction(2,5); qv=1-pv
pm={k:pv*qv**(k-1) for k in range(1,19)}
Q={j:qv**j for j in range(0,19)}
for y in range(6,19):
    lhs=Fraction(0)
    for i in range(1,y):
        for j in range(i+1,y):
            k=y-i-j
            if k>j:
                lhs += pm[i]*pm[j]/Q[i]*pm[k]/Q[j]
    rhs=Fraction(0)
    for x3 in range(1,y):
        for x2 in range(1,y):
            x1=y-2*x2-3*x3
            if x1>=1:
                rhs += pm[x1]*pm[x2]*pm[x3]
    assert lhs==rhs, (y,lhs,rhs)

# Triangularity: at total n+3 the only record triple containing p_n is (1,2,n),
# and no RHS index can equal n, for representative n>=3.
for n in range(3,30):
    triples=[]
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            k=n+3-i-j
            if k>j and k<=n:
                triples.append((i,j,k))
    containing=[t for t in triples if n in t]
    assert containing==[(1,2,n)]
    for x3 in range(1,n+1):
        for x2 in range(1,n+1):
            x1=n+3-2*x2-3*x3
            if x1>=1:
                assert max(x1,x2,x3)<n
print('VERIFY_OK', sp.factor(D2), sp.factor(D3))
