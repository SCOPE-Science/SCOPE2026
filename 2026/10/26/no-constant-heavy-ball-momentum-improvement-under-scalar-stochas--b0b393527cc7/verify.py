"""Finite exact-arithmetic checks for the scalar stochastic heavy-ball theorem.

Requires only Python 3 standard library. These checks are not an infinite proof.
"""
from fractions import Fraction as F
from math import comb


def mat(mu, var, eta, beta):
    a = 1 + beta - eta * mu
    w = eta * eta * var
    return ((a*a + w, -2*beta*a, beta*beta),
            (a, -beta, F(0)), (F(1), F(0), F(0)))


def characteristic(s, mu, var, eta, beta):
    a = 1 + beta - eta * mu
    w = eta * eta * var
    return ((s+beta)*(s*s-beta*beta)
            - s*(s-beta)*a*a - s*(s+beta)*w)


def moments_from_matrix(mu, var, eta, beta, x0, xminus, steps):
    M = mat(mu, var, eta, beta)
    z = (x0*x0, x0*xminus, xminus*xminus)
    for _ in range(steps):
        z = tuple(sum(M[i][j]*z[j] for j in range(3)) for i in range(3))
    return z


def direct_bernoulli_moments(p, m, eta, beta, x0, xminus, steps):
    branches = [(F(comb(m,j))*p**j*(1-p)**(m-j), F(j,m))
                for j in range(m+1)]
    paths = [(F(1),x0,xminus)]
    for _ in range(steps):
        paths = [(pr*pj,(1+beta-eta*h)*x-beta*y,x)
                 for pr,x,y in paths for pj,h in branches]
    return (sum(pr*x*x for pr,x,y in paths),
            sum(pr*x*y for pr,x,y in paths),
            sum(pr*y*y for pr,x,y in paths))


def run():
    moment_cases = 0
    for p in [F(1,5), F(1,2), F(4,5)]:
      for m in range(1,5):
       mu, var = p, p*(1-p)/m
       for beta in [F(0), F(1,6), F(1,2), F(3,4)]:
        for eta in [F(1,4), F(1), F(3)]:
         for steps in range(1,5):
          for x0,xminus in [(F(2),F(1)),(F(1),F(-1))]:
           lhs = moments_from_matrix(mu,var,eta,beta,x0,xminus,steps)
           rhs = direct_bernoulli_moments(p,m,eta,beta,x0,xminus,steps)
           assert lhs == rhs, (p,m,beta,eta,steps,lhs,rhs)
           moment_cases += 1

    polynomial_cases = 0
    for t in [F(1,10),F(1,2),F(1),F(4)]:
     r=t/(1+t)
     for beta in [F(1,100),r/4,r/2,r*F(3,4),r,F(3,4)]:
      for alpha in [F(1,100),F(1,4), F(1,2),F(1),F(3)]:
       value = characteristic(r,F(1),t,alpha,beta)
       if beta>0:
        assert value < 0, (t,beta,alpha,value)
       polynomial_cases += 1
      if beta<r:
       theta=(r-beta)/(r+beta)
       alpha_min=theta*(1+beta)/(theta+t)
       max_value=(r*r-beta*beta)/r-theta*(1+beta-alpha_min)**2-t*alpha_min**2
       formula= -beta*beta*(r-beta)*(1-r)**2/(r*(r-beta+2*r*beta))
       assert max_value==formula, (t,beta,max_value,formula)

    stability_cases=0
    for t in [F(1,10), F(1,2),F(1),F(4)]:
     for beta in [F(0),F(1,8),F(1,2),F(7,8)]:
      upper=2*(1-beta*beta)/((1-beta)+t*(1+beta))
      assert characteristic(F(1),F(1),t,upper,beta)==0
      for alpha in [upper/2,upper,upper*F(3,2)]:
       q=characteristic(F(1),F(1),t,alpha,beta)
       assert (q>0 if alpha<upper else (q==0 if alpha==upper else q<0))
       stability_cases+=1

    for t in [F(1,10),F(1),F(5)]:
     optimum=1/(1+t)
     r=t/(1+t)
     assert (1-optimum)**2+t*optimum**2==r

    print('exact covariance recursions vs full Bernoulli path sums:',moment_cases)
    print('exact strict momentum spectral polynomial tests:',polynomial_cases)
    print('exact stability determinant signs:',stability_cases)
    print('exact zero-momentum optima: 3')
    print('PASS')

if __name__=='__main__':
    run()
