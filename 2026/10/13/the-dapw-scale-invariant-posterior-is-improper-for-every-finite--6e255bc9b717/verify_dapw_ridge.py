"""Standalone numerical checks for the DAPW boundary and likelihood escape.
The proof of posterior impropriety is analytic; finite checks are illustrative.
"""
import math
import sympy as sp

def f_cdf(k, ell, s, c):
    assert k >= -1 and ell > 1 and c > 0
    if k == -1:
        return 0.0
    A = math.exp(ell)
    q = ell + s
    beta = c / ell
    z = math.exp(ell - q * math.exp(beta * math.log(k + 1)))
    return (math.exp(-z) - math.exp(-A)) / (-math.expm1(-A))

def f_pmf(k, ell, s, c):
    return f_cdf(k,ell,s,c) - f_cdf(k-1,ell,s,c)

def lim_cdf(k,s,c):
    if k == -1:
        return 0.0
    return math.exp(-math.exp(-s)*(k+1)**(-c))

def lim_pmf(k,s,c):
    return lim_cdf(k,s,c)-lim_cdf(k-1,s,c)

def t2_lik(data,n,ell,s,c,limit=False):
    pm = (lambda k: lim_pmf(k,s,c)) if limit else (lambda k: f_pmf(k,ell,s,c))
    cv = (lambda k: lim_cdf(k,s,c)) if limit else (lambda k: f_cdf(k,ell,s,c))
    r = len(data)
    assert r <= n and r >= 1 and data == sorted(data)
    return math.factorial(n)//math.factorial(n-r) * math.prod(pm(x) for x in data) * (1-cv(data[-1]))**(n-r)

def upper_lik(data,ell,s,c,limit=False):
    pm = (lambda k: lim_pmf(k,s,c)) if limit else (lambda k: f_pmf(k,ell,s,c))
    cv = (lambda k: lim_cdf(k,s,c)) if limit else (lambda k: f_cdf(k,ell,s,c))
    assert all(data[i] < data[i+1] for i in range(len(data)-1))
    return pm(data[0])*math.prod(pm(data[i])/(1-cv(data[i-1])) for i in range(1,len(data)))

sx,cx=.4,1.2
sy,cy=-.2,1.7
strength=[0,2,5]
stress=[1,3,6]
limit_t=t2_lik(strength,5,10,sx,cx,True)*t2_lik(stress,5,10,sy,cy,True)
limit_u=upper_lik(strength,10,sx,cx,True)*upper_lik(stress,10,sy,cy,True)
assert 0 < limit_t < 1 and 0 < limit_u < 1
for ell in (5,10,20,40,80,160):
    # ell=log(log(alpha)), with log(alpha)=exp(ell)
    sample=[f_cdf(k,ell,sx,cx) for k in (0,1,2,3,7)]
    goal=[lim_cdf(k,sx,cx) for k in (0,1,2,3,7)]
    err=max(abs(x-y) for x,y in zip(sample,goal))
    t=t2_lik(strength,5,ell,sx,cx)*t2_lik(stress,5,ell,sy,cy)
    u=upper_lik(strength,ell,sx,cx)*upper_lik(stress,ell,sy,cy)
    assert t>0 and u>0
    print('ell',ell,'cdf_error',format(err,'.8g'),'typeII_likelihood_ratio',format(t/limit_t,'.8g'),'upper_record_likelihood_ratio',format(u/limit_u,'.8g'))
assert err < .002
assert abs(t/limit_t-1) < .15
assert abs(u/limit_u-1) < .15

# The exact Jacobian for (A,q_1,log(beta_1),q_2,log(beta_2))
# as a function of (A,s_1,c_1,s_2,c_2). The base prior measure
# d(alpha)/alpha d(theta_1)/theta_1 d(beta_1)/beta_1 ...
# is the absolute value of this determinant.
A, s1, c1, s2, c2 = sp.symbols('A s1 c1 s2 c2',positive=True)
ell_sym = sp.log(A)
w=[A, ell_sym+s1, sp.log(c1)-sp.log(ell_sym), ell_sym+s2, sp.log(c2)-sp.log(ell_sym)]
J=sp.Matrix(w).jacobian([A,s1,c1,s2,c2])
assert sp.simplify(J.det()-1/(c1*c2))==0
print('JACOBIAN',str(sp.simplify(J.det())))
print('LIMIT_TYPEII',format(limit_t,'.14g'))
print('LIMIT_UPPER',format(limit_u,'.14g'))
print('VERIFY_OK')
