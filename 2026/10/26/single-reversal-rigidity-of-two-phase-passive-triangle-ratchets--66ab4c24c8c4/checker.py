"""Exact checks for the two-phase triangle ratchet classification.

Requires Python 3 and SymPy. The degree bound in the theorem is algebraic;
finite parameter checks below corroborate, rather than replace, its proof.
"""
import sympy as S

r = S.symbols('r', nonnegative=True)
U = S.Matrix([[1, 0], [-1, 1], [0, -1]])
R = S.Matrix([[1, 0, 0], [0, 0, -1]])
assert R*U == S.eye(2)

def generator(weights, conductances):
    G = S.zeros(3)
    for i in range(3):
        j=(i+1)%3
        c=S.Rational(conductances[i])
        f=c/S.Rational(weights[i]); b=c/S.Rational(weights[j])
        G[j,i]+=f;G[i,i]-=f
        G[i,j]+=b;G[j,j]-=b
    return G

def exact_current(P,C):
    L=[generator(P[s],C[s]) for s in range(2)]
    Q=S.zeros(6)
    for s in range(2):
        Q[s*3:s*3+3,s*3:s*3+3]=L[s]-r*S.eye(3)
        for i in range(3):Q[(1-s)*3+i,s*3+i]=r
    T=Q.copy();T[5,:]=S.ones(1,6)
    right=S.zeros(6,1);right[5]=1
    z=T.inv()*right
    J=S.factor(sum(S.Rational(C[s][0])*(z[3*s]/S.Rational(P[s][0])-z[3*s+1]/S.Rational(P[s][1])) for s in range(2)))
    B=[-R*L[s]*U for s in range(2)]
    f=[R*L[s]*S.ones(3,1)/6 for s in range(2)]
    H=(B[0]+r*S.eye(2)).row_join(-r*S.eye(2)).col_join((-r*S.eye(2)).row_join(B[1]+r*S.eye(2)))
    d=S.factor(H.det())
    assert S.simplify(d-S.det(B[0]*B[1]+r*(B[0]+B[1])))==0
    assert S.degree(d,r)==2
    W=H.inv()*f[0].col_join(f[1])
    ZZ=[S.ones(3,1)/6+U*W[2*s:2*s+2,0] for s in range(2)]
    jshort=S.factor(sum(S.Rational(C[s][0])*(ZZ[s][0]/S.Rational(P[s][0])-ZZ[s][1]/S.Rational(P[s][1])) for s in range(2)))
    assert S.simplify(J-jshort)==0
    numer=S.cancel(J*d)
    assert S.Poly(numer,r).degree()<=2 and numer.subs(r,0)==0
    return J,d,z

pairs=[
    ([[1,1,1],[1,2,3]],[[1,1,1],[4,1,2]]),
    ([[1,2,3],[4,3,1]],[[2,4,5],[5,2,3]]),
    ([[2,5,1],[3,1,4]],[[1,7,2],[2,3,4]]),
]
for P,C in pairs:
    j,d,z=exact_current(P,C)
    print('weights',P,'bonds',C,'J=',j,'d=',d)
    assert all(d.subs(r,t)>0 for t in (0,1,2,7))
J,d,z=exact_current(*pairs[0])
assert S.simplify(J-r*(r-2)/(2*(103*r*r+339*r+252)))==0
assert list(z.subs(r,2)) == [S.Rational(17,122),S.Rational(21,122),S.Rational(23,122),S.Rational(6,61),S.Rational(11,61),S.Rational(27,122)]
assert S.simplify(J.subs(r,2))==0
print('EXACT CHECKS PASSED; switching rate r=2 yields zero coarse current and nonzero microscopic currents')
