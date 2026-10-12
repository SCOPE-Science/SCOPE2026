"""Exact rational reproduction of finite checks for the SEIRV equilibrium theorem.

The analytic uniform asymptotic theorem is in RESULT.md, not inferred from examples.
"""
from fractions import Fraction as Q


def pol_add(a, b):
    n=max(len(a),len(b))
    return [ (a[j] if j<len(a) else Q(0))+(b[j] if j<len(b) else Q(0)) for j in range(n)]


def pol_mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): out[i+j]+=v*w
    return out


def pol_scale(a,v): return [v*t for t in a]


def pol_eval(a,x): return sum((z*x**j for j,z in enumerate(a)),Q(0))


def check():
    alpha,mu,sigma,Lambda,gamma,delta,theta=(Q(2),Q(1),Q(1,2),Q(5),Q(3),Q(2),Q(1))
    A=alpha+mu; M=mu+alpha*sigma
    K=(gamma+mu)*(delta+mu+theta)/gamma
    H=K-delta; c=Lambda*M/(A*mu)
    b_inf=H/c; b_star=K/c
    L=Lambda*b_inf**2*(mu*M+A*alpha*sigma**2)/(A*A*mu*mu)
    assert (A,M,K,H,c,b_inf,b_star,L)==(3,2,Q(16,3),Q(10,3),Q(10,3),1,Q(8,5),Q(35,18))
    assert 4*delta*mu*L/(c*c)==Q(7,5)  # z0^2 = 35/25
    assert delta*mu/L==Q(36,35)          # y0^2 = 36/35
    beta=Q(6,5);B=Q(100)

    def P(I):
        return Lambda*beta*(M+beta*sigma*I)/((A+beta*I)*(mu+beta*sigma*I))

    def F(I): return P(I)+delta*B*I/(mu+B*I)-K

    assert F(Q(0))==-Q(4,3)
    assert F(Q(1,10))==Q(5051,22737)
    assert F(Q(1,2))==-Q(281,663)
    for I in (Q(1,10),Q(1,2),Q(1,3)):
        S=Lambda/(A+beta*I)
        E=(delta+mu+theta)*I/gamma
        R=delta*I/(mu+B*I)
        V=alpha*S/(mu+beta*sigma*I)
        assert Lambda-beta*S*I-A*S==0
        assert gamma*E-(delta+mu+theta)*I==0
        assert delta*I-B*R*I-mu*R==0
        assert alpha*S-beta*sigma*V*I-mu*V==0
        assert (beta*S*I+beta*sigma*V*I+B*R*I-(gamma+mu)*E)/I==F(I)

    numer=pol_add(
      pol_add(pol_mul(pol_scale([M,beta*sigma],Lambda*beta),[mu,B]),
              pol_scale(pol_mul([Q(0),B],pol_mul([A,beta],[mu,beta*sigma])),delta)),
      pol_scale(pol_mul(pol_mul([A,beta],[mu,beta*sigma]),[mu,B]),-K)
    )
    assert len(numer)==4
    assert numer[0]==A*mu**2*(c*beta-K)<0
    assert numer[3]==-H*B*beta**2*sigma<0
    for I in (Q(0),Q(1,10),Q(1,2)):
        denom=(A+beta*I)*(mu+beta*sigma*I)*(mu+B*I)
        assert numer[0]+numer[1]*I+numer[2]*I**2+numer[3]*I**3==F(I)*denom

    assert mu*(K-c*beta)/(c*beta-H)==Q(2)
    assert Q(1)-delta/K==Q(5,8)
    print('VERIFY_OK')

if __name__=='__main__': check()
