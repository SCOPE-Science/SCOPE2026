"""Reproduce the stationary potential–kinetic covariance phase boundary.

Dependencies: sympy and mpmath. Run: python CHECK.py.
"""
from itertools import combinations, product
import sympy as sp
import mpmath as mp


def polynomial(g, u):
    return (48*u**4 + 192*g*u**3 + (288*g**2+104)*u**2
            + (138*g**3+136*g)*u + (6*g**2-1)*(3*g**2+9))


def formula(g,u):
    B = 1+2*g*u+4*u*u
    C = 9+6*g*u+4*u*u
    E = 1+2*g*g+6*g*u+4*u*u
    return -4*u*polynomial(g,u)/(g*(3*g*g+4)*B*B*C*E)


def exact_hierarchy():
    g,u=sp.symbols('g u',positive=True)
    moments={(0,0,0):sp.Integer(1),(0,0,1):sp.Integer(0)}
    for degree in range(1,5):
        keys=[(i,degree-i,t) for i in range(degree+1) for t in (0,1)]
        unknown=sp.symbols(f'c{degree}_0:{len(keys)}')
        symbols=dict(zip(keys,unknown))
        equations=[]
        for i,j,t in keys:
            rhs=i*symbols[(i-1,j+1,t)] if i else 0
            if j:
                rhs+=-j*symbols[(i+1,j-1,t)]-j*g*symbols[(i,j,t)]
                rhs+=j*moments[(i,j-1,1-t)]
            if t:
                rhs+=-2*u*symbols[(i,j,t)]
            equations.append(rhs)
        matrix,vector=sp.linear_eq_to_matrix(equations,unknown)
        solution=matrix.inv()*vector
        for key,value in zip(keys,solution):
            moments[key]=sp.factor(value)
    B=1+2*g*u+4*u*u
    assert sp.simplify(moments[(2,0,0)]-(g+2*u)/(g*B))==0
    assert sp.simplify(moments[(0,2,0)]-2*u/(g*B))==0
    assert moments[(1,1,0)]==0
    cov=sp.factor(moments[(2,2,0)]-moments[(2,0,0)]*moments[(0,2,0)])
    assert sp.factor(cov-formula(g,u))==0
    P=polynomial(g,u)
    assert sp.factor(P.subs(g,0)-(12*u*u-1)*(4*u*u+9))==0
    assert sp.factor(P.subs(u,0)-(6*g*g-1)*(3*g*g+9))==0
    for symbol in (g,u):
        poly=sp.Poly(sp.diff(P,symbol),g,u)
        assert all(coefficient>0 for _,coefficient in poly.terms())
    return 7


def independent_telegraph_integral(g_value,u_value):
    """Four-time telegraph integral using ordered gaps, not moment recursions."""
    mp.mp.dps=40
    g=mp.mpf(str(g_value));u=mp.mpf(str(u_value))
    discriminant=mp.sqrt(g*g-4)
    z=[(-g+discriminant)/2,(-g-discriminant)/2]
    coeff={'x':[1/discriminant,-1/discriminant],
           'v':[z[0]/discriminant,-z[1]/discriminant]}
    def second(kind):
        ans=0
        for i,j in product(range(2),repeat=2):
            aa,bb=z[i],z[j]
            ans+=2*coeff[kind][i]*coeff[kind][j]/(-(aa+bb))/(2*u-bb)
        return mp.re(ans)
    x2,v2=second('x'),second('v')
    mixed=0
    for x_positions in combinations(range(4),2):
        kinds=['x' if i in x_positions else 'v' for i in range(4)]
        for indices in product(range(2),repeat=4):
            aa=[z[k] for k in indices]
            coefficient=mp.fprod(coeff[kind][k] for kind,k in zip(kinds,indices))
            denominator=(-(aa[0]+aa[1]+aa[2]+aa[3]))
            denominator*=2*u-(aa[1]+aa[2]+aa[3])
            denominator*=-(aa[2]+aa[3])
            denominator*=2*u-aa[3]
            mixed+=4*coefficient/denominator
    return x2,v2,mp.re(mixed)


def run():
    count=exact_hierarchy()
    for g,u in ((0.2,0.1),(0.2,0.3),(1.0,0.1),(3.0,0.02)):
        x2,v2,mixed=independent_telegraph_integral(g,u)
        B=1+2*g*u+4*u*u
        assert abs(x2-(g+2*u)/(g*B))<1e-10
        assert abs(v2-2*u/(g*B))<1e-10
        assert abs(mixed-x2*v2-formula(g,u))<1e-10
        count+=3
    gcrit=1/mp.sqrt(6)
    ucrit=1/(2*mp.sqrt(3))
    assert polynomial(0,ucrit)==mp.mpf(0) or abs(polynomial(0,ucrit))<1e-25
    assert abs(polynomial(gcrit,0))<1e-25
    count+=2
    for g,u,sign in ((.2,.1,1),(.2,.3,-1),(1,.1,-1),(3,.02,-1)):
        assert formula(g,u)*sign>0
        count+=1
    print(f'PASS: {count} symbolic, factorization, and independent-integral assertions')


if __name__=='__main__':
    run()
