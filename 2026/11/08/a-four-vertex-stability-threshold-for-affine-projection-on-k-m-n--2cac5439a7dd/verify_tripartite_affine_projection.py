"""Exact symbolic and rational checks for affine spline projections on K_{m,n,1}.

Run: python verify_tripartite_affine_projection.py (requires SymPy).
All universal inequalities are certified by polynomial identities whose
coefficient lists are checked symbolically, not by finite sampling.
"""
import sympy as sp

m,n = sp.symbols('m n', integer=True, positive=True)
h,k = sp.symbols('h k', integer=True, nonnegative=True)
D = (m+n+1)*(m*n+m+n)
Q = sp.Matrix([[(n+1)/3, n/sp.Integer(6), sp.Rational(1,6)],
               [m/sp.Integer(6),(m+1)/3,sp.Rational(1,6)],
               [m/sp.Integer(6),n/sp.Integer(6),(m+n)/3]])
R = Q.inv().applyfunc(sp.factor)
print('EQ_INV_OK',flush=True)
assert (Q*R-sp.eye(3)).applyfunc(sp.cancel)==sp.zeros(3)
print('Q_MATRIX_OK',flush=True)

# Inverse nodal mass-matrix entries for a distinguished vertex in each part.
a1 = sp.factor((R[0,0]-3/(n+1))/m)
a0 = sp.factor(a1+3/(n+1))
ab = sp.factor(R[0,1]/n)
ac = sp.factor(R[0,2])
b1 = sp.factor((R[1,1]-3/(m+1))/n)
b0 = sp.factor(b1+3/(m+1))
ba = sp.factor(R[1,0]/m)
bc = sp.factor(R[1,2])
ca,cb,cc = sp.factor(R[2,0]/m),sp.factor(R[2,1]/n),R[2,2]
assert sp.simplify(ab-ba) == 0
assert sp.simplify(ac-ca) == 0 and sp.simplify(bc-cb) == 0

# For opposite-sign endpoints a>0>b, integral |a(1-t)+bt|dt.
opp = lambda a,b: sp.cancel((a*a+b*b)/(2*(a-b)))
same = lambda a,b: (a+b)/2
# In the domain 1<=m<=n: a0,a1,b0,b1,cc>0, ab,bc<0.
# The sign of ac is negative when n<=2m+2, positive when n>=2m+2.
EB = sp.cancel(m*opp(b0,ba)+m*(n-1)*opp(b1,ba)
               +opp(b0,bc)+(n-1)*opp(b1,bc)-m*same(ba,bc))
u = (m*m+m*n-m+n+1)/((m+1)*D)
v = u+3/(m+1)
x=(2*m+2*n-1)/D
y=(2*n+2-m)/D
F = lambda a,b: (a*a+b*b)/(2*(a+b))
formula = m*F(v,x)+m*(n-1)*F(u,x)+F(v,y)+(n-1)*F(u,y)+m*(x+y)/2
assert sp.factor(b1-u)==0 and sp.factor(b0-v)==0
assert sp.factor(-ba-x)==0 and sp.factor(-bc-y)==0
print('THREE_CLASS_GRAM_INVERSE_AND_EXPLICIT_NORM_FORMULA_OK',flush=True)

# Exact alternative endpoint norms in the two sign regions.
EAlo = sp.cancel(n*opp(a0,ab)+(m-1)*n*opp(a1,ab)
                 +opp(a0,ac)+(m-1)*opp(a1,ac)-n*same(ab,ac))
EClo = sp.cancel(-m*n*same(ca,cb)+m*opp(cc,ca)+n*opp(cc,cb))
EAhi = sp.cancel(n*opp(a0,ab)+(m-1)*n*opp(a1,ab)
                 +same(a0,ac)+(m-1)*same(a1,ac)+n*opp(ac,ab))
EChi = sp.cancel(m*n*opp(ca,cb)+m*same(ca,cc)+n*opp(cc,cb))

# After substitutions the polynomial denominators have strictly positive
# coefficients, as do numerators after removing their exact equality factors.
certs=[]
for region, ea, ec, substitutions in [
    ('low',EAlo,EClo,{m:h+1,n:h+1+k}),
    ('high',EAhi,EChi,{m:h+1,n:2*h+4+k})]:
    for label,expr in [('BminusA',EB-ea),('BminusC',EB-ec)]:
        t=sp.factor(expr.subs(substitutions, simultaneous=True))
        num,den=sp.fraction(t)
        num=sp.Poly(sp.expand(num),h,k).as_expr()
        den=sp.Poly(sp.expand(den),h,k).as_expr()
        eq= (k if label=='BminusA' else h+k) if region=='low' else sp.Integer(1)
        q,r=sp.div(num,eq,h,k)
        assert r==0, (region,label,'equality factor')
        pnum=sp.Poly(q,h,k)
        pden=sp.Poly(den,h,k)
        assert all(c>0 for c in pnum.coeffs()), (region,label,'positive numerator')
        assert all(c>0 for c in pden.coeffs()), (region,label,'positive denominator')
        certs.append((region,label,len(pnum.terms()),len(pden.terms())))
print('UNIVERSAL_VERTEX_DOMINANCE_POSITIVE_COEFFICIENT_CERTIFICATES_OK',certs)

# Threshold ||P||>2 iff the larger independent part has >=4 vertices.
for label,sub in [('m>=4',{m:4+h,n:4+h+k}),
                  ('m=1',{m:1,n:4+k}),('m=2',{m:2,n:4+k}),
                  ('m=3',{m:3,n:4+k})]:
    expr=sp.factor((EB-2).subs(sub,simultaneous=True))
    num,den=sp.fraction(expr)
    cn=sp.Poly(sp.expand(num),h,k).coeffs()
    cd=sp.Poly(sp.expand(den),h,k).coeffs()
    assert all(c>0 for c in cn) and all(c>0 for c in cd),label
for N in (1,2,3):
    for M in range(1,N+1):
        assert EB.subs({m:M,n:N})<2
assert sp.simplify(sp.limit(EB,n,sp.oo)-sp.Rational(7,3)) == 0
print('EXACT_TWO_THRESHOLD_AND_LIMIT_CERTIFICATES_OK')

# Independent dense Gram inversions plus direct absolute kernel integration.
# Uses exact rational arithmetic and is independent of the three-class inverse.
def J(a,b):
    if a*b>=0:return (abs(a)+abs(b))/2
    return (a*a+b*b)/(2*(abs(a)+abs(b)))
checks=0
for M in range(1,8):
 for N in range(M,8):
    nv=M+N+1
    edges=[(i,M+j) for i in range(M) for j in range(N)]
    edges += [(i,nv-1) for i in range(M+N)]
    MM=sp.zeros(nv)
    for i,j in edges:
        MM[i,i]+=sp.Rational(1,3);MM[j,j]+=sp.Rational(1,3)
        MM[i,j]+=sp.Rational(1,6);MM[j,i]+=sp.Rational(1,6)
    I=MM.inv()
    rows=[sum((J(I[i,a],I[i,b]) for a,b in edges),sp.Rational(0)) for i in range(nv)]
    target=formula.subs({m:M,n:N})
    assert all(v==target for v in rows[M:M+N]),(M,N,'largest part')
    assert max(rows)==target,(M,N,rows,target)
    assert all(v<target for v in rows[:M]) if N>M else all(v==target for v in rows[:M])
    assert all(v<target for v in rows[-1:]) if N+M>2 else all(v==target for v in rows[-1:])
    checks+=1
print('INDEPENDENT_DENSE_EXACT_GRAM_KERNEL_INTEGRATIONS_OK',checks)
print('ALL_TRIPARTITE_AFFINE_PROJECTION_CHECKS_OK')
