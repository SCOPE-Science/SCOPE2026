"""Exact algebraic checks for a three-row sampling Kaczmarz-Motzkin model.

Run with Python 3 and SymPy. This checks finite symbolic identities and
Sturm root counts; the accompanying mathematical proof supplies the
infinite-horizon implications.
"""
from itertools import combinations
from sympy import (Matrix, Rational, Symbol, factor, simplify, resultant,
                   Poly, sturm, sqrt, N)

x, t, z = Symbol('x'), Symbol('t'), Symbol('z')
y = (2*x-1)**2
P5 = 64*x**5 - 128*x**4 + 192*x**3 - 40*x**2 + 11*x - 1
P9 = (8192*x**9 - 32768*x**8 + 53632*x**7 - 45056*x**6
      + 18401*x**5 - 607*x**4 - 2887*x**3 + 1313*x**2 -253*x+19)
assert factor(resultant(3*t*t-y*t-2*x*x,t**3-x*x,t)) == -x*x*(x-1)*P5
assert factor(resultant(3*t*t-2*y*t-x*x,t**3-y*y,t) +(x-1)*P9) == 0
assert Poly(P5,x).count_roots(0,Rational(1,4)) == 1
assert Poly(P5,x).count_roots(Rational(1,12),Rational(1,8)) == 1
assert Poly(P9,x).count_roots(Rational(1,4),1) == 1
assert Poly(P9,x).count_roots(Rational(1,4),Rational(1,3)) == 1
assert [len(sturm(p,x)) for p in (P5,P9)] == [6,10]

def sign_variations(p, endpoint):
    values = [simplify(f.subs(x,endpoint)) for f in sturm(p,x)]
    signs = [1 if v > 0 else -1 for v in values if v]
    return sum(a != b for a,b in zip(signs,signs[1:]))
assert [sign_variations(P5,v) for v in (0,Rational(1,12),Rational(1,8),Rational(1,4))] == [3,3,2,2]
assert [sign_variations(P9,v) for v in (Rational(1,4),Rational(1,3),1)] == [5,4,4]

C = Matrix([[1,x,x],[x,1,y],[x,y,1]])
M1 = C/3
assert factor(M1.charpoly(z).as_expr()) == factor((z-(1-y)/3)*(z*z-(2+y)*z/3+(1+y-2*x*x)/9))
for a in (Rational(1,3),Rational(1,2),Rational(2,3)):
    M2 = Matrix([[0,x/2,x/2],[a*x,0,(1-a)*y],[a*x,(1-a)*y,0]])
    assert factor(M2.charpoly(z).as_expr()) == factor((z+(1-a)*y)*(z*z-(1-a)*y*z-a*x*x))
M3_left = Matrix([[0,x/2,x/2],[x,0,0],[x,0,0]])
M3_right = Matrix([[0,x/2,x/2],[0,0,y],[0,y,0]])
assert factor(M3_left.charpoly(z).as_expr() - z*(z*z-x*x)) == 0
assert factor(M3_right.charpoly(z).as_expr() - z*(z*z-y*y)) == 0

# A lower bound for the one-sample rate, then a Rayleigh bound in the
# large-x region. These exact factorizations are used in the proof.
assert factor(8*x*x+2*y-1) == (4*x-1)**2
rayleigh = (3+4*x+2*y)/9
assert factor(rayleigh**3-y) == (4*(x-1)**2*(128*x**4+64*x**3+336*x*x+352*x-151)/729)
assert simplify((128*x**4+64*x**3+336*x*x+352*x-151).subs(x,Rational(1,3))) > 0
assert factor(3-8*y-16*x*x + 48*(x-Rational(1,4))*(x-Rational(5,12))) == 0
assert factor(3-4*y-32*x*x + 48*(x-Rational(1,12))*(x-Rational(1,4))) == 0

# Directly enumerate the uniform without-replacement subsets and ties
# using a rational geometric instance. Check its finite Markov recurrence
# against the actual planar projection updates, not only against C.
rows = [Matrix([1,0]), Matrix([Rational(3,5),Rational(4,5)]),
        Matrix([Rational(3,5),-Rational(4,5)])]
e0 = Matrix([2,3]); xx=Rational(9,25); yy=(2*xx-1)**2

def select(e,beta):
    out=[]
    subs=list(combinations(range(3),beta))
    for S in subs:
        vals=[abs((rows[j].dot(e))) for j in S]
        best=max(vals)
        winners=[j for j,v in zip(S,vals) if v==best]
        for j in winners: out.append((j,Rational(1,len(subs)*len(winners))))
    return out

def next_dist(dist,beta):
    result={}
    for e,p in dist.items():
        for j,prob in select(Matrix(e),beta):
            a=rows[j]
            en=Matrix(e)-a*a.dot(Matrix(e))
            key=tuple(en)
            result[key]=result.get(key,0)+p*prob
    return result

def kernel(beta):
    if beta==1:return M1.subs(x,xx)
    if beta==3:return M3_right.subs({x:xx,y:yy})
    return Matrix([[0,xx/2,xx/2],[xx/3,0,2*yy/3],
                   [xx/3,2*yy/3,0]])

for beta in (1,2,3):
    dist={tuple(e0):Rational(1)}
    dist=next_dist(dist,beta)
    v=Matrix([[0,0,0]])
    for e,p in dist.items():
        # Post-first-step selected row can be inferred uniquely unless
        # the update has already reached zero; this instance has no such case.
        zeros=[j for j,a in enumerate(rows) if a.dot(Matrix(e))==0]
        assert len(zeros)==1, (beta,e,zeros)
        j=zeros[0];v[0,j]+=p*Matrix(e).dot(Matrix(e))
    for k in range(1,6):
        actual=sum(p*Matrix(e).dot(Matrix(e)) for e,p in dist.items())
        predicted=(v*(kernel(beta)**(k-1))*Matrix([1,1,1]))[0]
        assert simplify(actual-predicted)==0, (beta,k,actual,predicted)
        dist=next_dist(dist,beta)

# Assert interval order for explicit rational geometry values (diagnostics,
# not the proof of the continuum classification).
for q,expected in [(Rational(1,16),3),(Rational(1,5),2),
                   (Rational(3,10),2),(Rational(1,2),3),
                   (Rational(9,10),3)]:
    yyq=(2*q-1)**2
    lam1=((2+yyq)+sqrt(yyq**2+8*q*q))/6
    if q<Rational(1,4):
        lam2=(yyq+sqrt(yyq**2+24*q*q))/6
    else:
        lam2=(yyq+sqrt(yyq**2+3*q*q))/3
    lam3=min(q,yyq)
    work=[float(N(lam1,40)),float(N(sqrt(lam2),40)),
          float(N(lam3**Rational(1,3),40))]
    assert 1+min(range(3),key=lambda i:work[i]) == expected,(q,work)

# Printed approximate locations are informative only.
print('PASS: two resultants; 7 Sturm intervals; symbolic characteristic factors;')
print('PASS: 3 cost inequalities; 15 exact-rational finite step checks;')
print('PASS: 5 rational interval diagnostics. No finite test used as an infinite proof.')
