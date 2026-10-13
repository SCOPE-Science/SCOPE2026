#!/usr/bin/env python3
"""Exact checks for two-edge complementary versus independent relaxed projection sampling."""
import sympy as S


def check(q, r):
    assert S.simplify(q - r) == 0


def gram_data(U, V):
    pair = (U*V**2*U + V*U**2*V)/2
    independent = (U**4+V**4+U*V**2*U+V*U**2*V)/4
    return pair, independent


def main():
    w, c = S.symbols('w c', real=True)
    u = S.Matrix([1, 0]); v = S.Matrix([c, S.sqrt(1-c*c)])
    U = S.eye(2) - w*u*u.T
    V = S.eye(2) - w*v*v.T
    pair, iid = gram_data(U, V)
    diff = iid - pair
    prefactor = w*w*(2-w)*(1-c*c)/4
    expected = w*w*(2-w)/4 * ((2-w*(1-c*c))*(u*u.T + v*v.T) - 2*c*(u*v.T+v*u.T))
    for i in range(2):
        for j in range(2):
            check(diff[i,j], expected[i,j])
    for sign in (+1,-1):
        direction = u+sign*v
        quotient = ((direction.T*diff*direction)[0]/(direction.T*direction)[0])
        check(quotient, prefactor*(2-w*(1+sign*c)))
    checks=6
    for a,b in [(3,4),(5,12),(8,15),(7,24)]:
        uu=S.Matrix([S.Integer(1),0])
        hyp=S.integer_nthroot(a*a+b*b,2)
        if not hyp[1]: continue
        den=hyp[0]; vv=S.Matrix([S.Rational(a,den),S.Rational(b,den)])
        cp=S.Rational(a,den)
        for om in [S.Rational(1,3),S.Rational(5,4),S.Rational(3,2),S.Rational(7,4)]:
            UA=S.eye(2)-om*uu*uu.T
            VB=S.eye(2)-om*vv*vv.T
            pp,ii=gram_data(UA,VB)
            dd=ii-pp
            plus=uu+vv;minus=uu-vv
            f=om*om*(2-om)*(1-cp*cp)/4
            check((plus.T*dd*plus)[0],(plus.T*plus)[0]*f*(2-om*(1+cp)))
            check((minus.T*dd*minus)[0],(minus.T*minus)[0]*f*(2-om*(1-cp)))
            checks+=2
    # The physical three-vertex path: updates exchange only along incident edges.
    e12=S.Matrix([1,-1,0]); e23=S.Matrix([0,-1,1]);
    P=e12*e12.T/2; Q=e23*e23.T/2
    omega=S.Rational(3,2)
    A=S.eye(3)-omega*P; B=S.eye(3)-omega*Q
    RR,IID=gram_data(A,B)
    ep=S.Matrix([1,-2,1])/S.sqrt(6)
    em=S.Matrix([1,0,-1])/S.sqrt(2)
    check((ep.T*IID*ep)[0], S.Rational(179,512))
    check((ep.T*RR*ep)[0], S.Rational(103,256))
    check((em.T*IID*em)[0], S.Rational(257,512))
    check((em.T*RR*em)[0], S.Rational(61,256))
    check((S.ones(1,3)*(IID-RR)*S.ones(3,1))[0], 0)
    assert (ep.T*(IID-RR)*ep)[0] < 0
    assert (em.T*(IID-RR)*em)[0] > 0
    checks+=7
    print(f'PASS: {checks} exact matrix, directional and graph identities; universal assertions are proved analytically.')


if __name__=='__main__':main()
