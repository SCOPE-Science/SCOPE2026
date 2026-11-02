"""Exact rational regression tests of state-resolved run/rest stationary laws.
Uses only Python 3 standard library; finite tests do not replace proof.
"""
from fractions import Fraction as F
from math import factorial


def poch(z,n):
    p=F(1)
    for j in range(n):p*=z+j
    return p


def full_moment(a,t,k):
    return F(factorial(2*k),4**k*factorial(k))*poch(t/2,k)/(
        poch((a+t)/2,k)*poch((a+1)/2,k))


def prediction(a,t,m,state):
    if m%2:
        if state==0:return F(0)
        return F(state,2)*full_moment(a,t,(m+1)//2)
    k=m//2
    M=full_moment(a,t,k)
    Mp=full_moment(a,t,k+1)
    if state==0:return M-(1+a/F(2*k+1))*Mp
    return (1+a/F(2*k+1))*Mp/2


def linear_solve3(A,b):
    w=[list(row)+[b[j]] for j,row in enumerate(A)]
    for j in range(3):
        pivot=next(k for k in range(j,3) if w[k][j])
        w[j],w[pivot]=w[pivot],w[j]
        scale=w[j][j]
        w[j]=[z/scale for z in w[j]]
        for k in range(3):
            if k!=j:
                s=w[k][j]
                w[k]=[z-s*v for z,v in zip(w[k],w[j])]
    return [z[-1] for z in w]


def independent_moments(a,t,degree):
    vec=[t/(2*(a+t)),a/(a+t),t/(2*(a+t))]
    ms=[vec]
    for m in range(1,degree+1):
        M=[[m+a,-t/2,F(0)],[-a,m+t,-a],[F(0),-t/2,m+a]]
        vec=linear_solve3(M,[-m*vec[0],F(0),m*vec[2]])
        ms.append(vec)
    return ms


def binomial_stationarity(a,m,state):
    # On t=a+1 the exact beta law gives E[x^(2k)] = (1/2)_k/(a+1/2)_k.
    def B(k):
        return F(0) if k%2 else poch(F(1,2),k//2)/poch(a+F(1,2),k//2)
    def em(k,s):
        if s==0: return (B(k)-B(k+2))/2
        return (B(k)+2*s*B(k+1)+B(k+2))/4
    t=a+1
    if state==0:return -m*em(m,0)+a*(em(m,-1)+em(m,1))-t*em(m,0)
    return m*(state*em(m-1,state)-em(m,state))*(m>0)-a*em(m,state)+t*em(m,0)/2


def run():
    checks=0
    aa=[F(1,4),F(1,2),F(3,4),F(1),F(3,2),F(2),F(3),F(11,2)]
    tt=[F(1,3),F(1),F(3,2),F(2),F(9,4)]
    for a in aa:
        for t in tt+[a+1,a+3]:
            mm=independent_moments(a,t,20)
            for degree in range(21):
                for s in [-1,0,1]:
                    assert mm[degree][s+1] == prediction(a,t,degree,s),(a,t,degree,s)
                    checks+=1
        for degree in range(27):
            for s in [-1,0,1]:
                assert binomial_stationarity(a,degree,s)==0,(a,degree,s)
                checks+=1
        assert prediction(a,a+1,0,0)==a/(2*a+1)
        assert prediction(a,a+1,0,1)==(a+1)/(2*(2*a+1))
        assert full_moment(a,a+1,1)==1/(2*a+1)
        checks+=3
    print(f'PASS: {checks} exact rational generator, reconstruction, binomial-state and normalization checks')

if __name__=='__main__':run()
