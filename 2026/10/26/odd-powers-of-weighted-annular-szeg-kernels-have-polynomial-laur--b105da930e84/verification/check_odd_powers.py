"""Deterministic high-precision checks of polynomial odd Szego kernel powers.

Requires mpmath. Numerical tests corroborate, but do not establish,
the all-parameter analytic identity.
"""
from math import comb
import mpmath as mp
mp.mp.dps = 80


def regular_coeffs(q, r, L, N=360):
    out = []
    for h in range(L-1):
        out.append(mp.fsum(
            (q**(2*k+2)/(r+q**(2*k+2)))*comb(k+h,h)
            -(r*q**(2*k)/(1+r*q**(2*k)))*((-1)**h)*(comb(k,h) if k>=h else 0)
            for k in range(N)
        ))
    return out


def mul_poly(a,b,k):
    z=[mp.mpf(0)]*(k+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j<=k:
                z[i+j]+=x*y
    return z


def coefficients(q,r,L):
    assert L>=1 and L%2==1 and 0<q<1 and r>0
    B=[mp.mpf(0)]*L
    B[0]=1
    for h,x in enumerate(regular_coeffs(q,r,L)):
        B[h+1]=x
    E=[mp.mpf(0)]*L
    E[0]=1
    for _ in range(L):
        E=mul_poly(E,B,L-1)
    principal={k:E[L-k] for k in range(1,L+1)}
    basis=[]
    A={1:1}
    for j in range(L):
        basis.append(A)
        nxt={}
        for k,x in A.items():
            nxt[k+1]=nxt.get(k+1,0)+k*x
            nxt[k]=nxt.get(k,0)-k*x
        A=nxt
    a=[mp.mpf(0)]*L
    for j in reversed(range(L)):
        a[j]=principal[j+1]/basis[j][j+1]
        for k,x in basis[j].items():
            principal[k]-=a[j]*x
    assert all(abs(x)<mp.mpf('1e-60') for x in principal.values())
    return a


def polynomial(n,a):
    return mp.fsum(a[j]*mp.mpf(n)**j for j in range(len(a)))


def kernel(q,r,t,N=400):
    return mp.fsum(t**n/(1+r*q**(2*n)) for n in range(-N,N+1))


def main():
    identity_cases=0
    for qstr, rstr in [('0.12','0.12'),('0.33','0.33'),('0.61','0.61'),
                       ('0.33','0.73'),('0.61','1.3'),('0.24','2.2')]:
        q=mp.mpf(qstr); r=mp.mpf(rstr)
        for L in [1,3,5,7]:
            a=coefficients(q,r,L)
            assert abs(a[-1]-1/mp.factorial(L-1))<mp.mpf('1e-55')
            for n in range(-12,13):
                assert polynomial(n,a)>0, (q,r,L,n)
            for theta in [mp.mpf(0),mp.mpf('0.65')]:
                t=q*mp.e**(1j*theta)
                lhs=kernel(q,r,t)**L
                rhs=mp.fsum(t**n*polynomial(n,a)/(1+(r**L)*q**(2*n))
                            for n in range(-400,401))
                err=abs(lhs-rhs)/(1+abs(lhs))
                assert err < mp.mpf('1e-34'), (q,r,L,theta,err)
                identity_cases+=1
            if L==3 and r==q:
                E=mp.fsum((2*k+1)*q**(2*k+1)/(1+q**(2*k+1)) for k in range(400))
                for n in range(-12,13):
                    expected=mp.mpf((n+1)*(n+2))/2+3*E
                    assert abs(polynomial(n,a)-expected)<mp.mpf('1e-56')
                    identity_cases+=1
    print('PASS:', identity_cases, 'identity/cubic comparisons; positivity and leading-term checks also passed.')
    for hstr in ['0.25','0.1','0.05']:
        h=mp.mpf(hstr); q=mp.exp(-h)
        E=mp.fsum((2*k+1)*q**(2*k+1)/(1+q**(2*k+1)) for k in range(4000))
        print('h=',hstr,' normalized E=',mp.nstr(E/(mp.pi**2/(24*h*h)),18))

if __name__=='__main__':
    main()
