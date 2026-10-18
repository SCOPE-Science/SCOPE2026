"""Reproduce finite algebraic and high-precision asymptotic checks for the
explosion-conditioned Sibuya branching theorem.
Requires Python 3 and mpmath (pip install mpmath).
Numerical checks supplement, and do not replace, the mathematical proof.
"""
import mpmath as mp
mp.mp.dps = 90


def params(alpha, T, u):
    b = 1-alpha
    Q = mp.exp(-b*T)
    C = 1-Q
    q = mp.exp(-b*(T-u))
    w = (-mp.expm1(-b*u))**(1/b)
    return b, Q, C, q, w


def conditional_pgf(alpha,T,u,z):
    b,Q,C,q,w=params(alpha,T,u)
    D=-mp.expm1(mp.log(z))+w*z if z != 0 else mp.mpf(1)
    return z*(D/w)**(-alpha)*(1+q/C*(D**b-w**b))**(alpha/b)


def conditional_laplace(alpha,T,u,s):
    w=params(alpha,T,u)[-1]
    b,Q,C,q,w=params(alpha,T,u)
    z=mp.exp(-s*w)
    D=-mp.expm1(-s*w)+w*z
    return z*(D/w)**(-alpha)*(1+q/C*(D**b-w**b))**(alpha/b)


def coefficients(alpha,T,s):
    b=1-alpha
    Q=mp.exp(-b*T)
    c=Q/(1-Q)
    g=(1+s)**(-alpha)
    h=(1+s)**b-1
    j=-s+alpha*(s+s*s/2)/(1+s)
    A=alpha*c*g*h
    B_nonanalytic=b**(1/b)*g*j
    B_analytic=g*(alpha*b*c*h/2+alpha*(2*alpha-1)*c*c*h*h/2)
    if alpha < mp.mpf('0.5'):
        return g,A,1/b,B_nonanalytic
    if alpha > mp.mpf('0.5'):
        return g,A,mp.mpf(2),B_analytic
    return g,A,mp.mpf(2),B_nonanalytic+B_analytic


def close(a,b,tol=mp.mpf('1e-42')):
    assert abs(a-b) <= tol*(1+abs(a)+abs(b)), (a,b)


def check():
    checks=0
    for a_str in ('0.2','0.3','0.5','0.7','0.9'):
        a=mp.mpf(a_str)
        for T_str in ('0.4','1.6','3.2'):
            T=mp.mpf(T_str)
            for u_str in ('0.001','0.025'):
                u=mp.mpf(u_str)
                b,Q,C,q,w=params(a,T,u)
                close(conditional_pgf(a,T,u,mp.mpf(1)),mp.mpf(1))
                checks+=1
                # Coefficient of z in the conditional generating function,
                # computed independently from the finite-state probability.
                Fprime0=q
                Eprime_u=mp.exp(-b*u)*w**a
                Eprime_T=Q*C**(a/b)
                p1_from_densities=Fprime0*Eprime_u/Eprime_T
                p1_exact=(w/C**(1/b))**a
                close(p1_from_densities,p1_exact)
                close(p1_exact,mp.diff(lambda z: conditional_pgf(a,T,u,z),0))
                checks+=2
                mean_exact=w+a*(1-w)*(1-q)/C
                mean_from_derivative=w*mp.diff(lambda z: conditional_pgf(a,T,u,z),1)
                close(mean_exact,mean_from_derivative)
                checks+=1
                for zstr in ('0.08','0.25','0.8'):
                    z=mp.mpf(zstr)
                    # Semigroup ODE solution / chain-rule pgf comparison.
                    D=-mp.expm1(mp.log(z))+w*z if z != 0 else mp.mpf(1)
                    fprime=q*(1-q+q*D**b)**(a/b)*D**(-a)
                    fprime_at_r=q*C**(a/b)*w**(-a)
                    close(conditional_pgf(a,T,u,z),z*fprime/fprime_at_r)
                    checks+=1
                    if a==mp.mpf('0.5'):
                        lam=(1-q)/C
                        mixture=(1-lam)*z+lam*z*(w/D)**(mp.mpf('0.5'))
                        close(conditional_pgf(a,T,u,z),mixture)
                        checks+=1
            for s_str in ('0.2','1.2','3'):
                s=mp.mpf(s_str)
                g,A,p,B=coefficients(a,T,s)
                # Consistency of both coefficients against smaller scales.
                errors=[]
                for u_str in ('1e-4','1e-6','1e-8'):
                    u=mp.mpf(u_str)
                    L=conditional_laplace(a,T,u,s)
                    ratio=(L-g-A*u)/u**p
                    errors.append(abs(ratio-B))
                    checks+=1
                assert errors[2]<errors[1]<errors[0],(a,T,s,errors)
                checks+=1
                # First correction sign follows analytically from h(s)>0.
                assert A>0 and B!=0
                checks+=1
    print(f'PASS: {checks} finite high-precision checks, 5 shape parameters, 3 explosion times.')
    print('These checks do not establish any infinite-limit statement.')

if __name__ == '__main__':
    check()
