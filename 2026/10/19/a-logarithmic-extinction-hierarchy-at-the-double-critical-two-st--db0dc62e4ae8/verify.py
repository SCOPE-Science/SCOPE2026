"""Reproduce exact identities and finite illustrations for a two-strain critical SIR asymptotic."""
from fractions import Fraction as F
from math import log
import numpy as np
from scipy.integrate import solve_ivp


def constants(mu, g1, g2, sig12, sig21):
    b1, b2 = mu+g1, mu+g2
    a1,a2 = b1*b1/mu,b2*b2/mu
    b12=b1*(b2-sig21*g2)/mu
    b21=b2*(b1-sig12*g1)/mu
    return b1,b2,a1,a2,b12,b21,a1-b21


def rhs(mu,g1,g2,sig12,sig21):
    b1,b2,*_=constants(mu,g1,g2,sig12,sig21)
    def f(t,y):
        S,I1,I2,I21,I12,R1,R2,R=y
        J1,J2=I1+I21,I2+I12
        return np.array([
            mu*(1-S)-b1*J1*S-b2*J2*S,
            b1*S*J1-b1*I1,
            b2*S*J2-b2*I2,
            b1*sig21*R2*J1-b1*I21,
            b2*sig12*R1*J2-b2*I12,
            g1*I1-b2*sig12*J2*R1-mu*R1,
            g2*I2-b1*sig21*J1*R2-mu*R2,
            g1*I21+g2*I12-mu*R])
    return f


def finite_checks():
    examples=[(F(1),F(3),F(1),F(1),F(1)),
              (F(1),F(5,3),F(1),F(3,4),F(1,2))]
    init=np.array([.96,.02,.02,0,0,0,0,0],dtype=float)
    for pars in examples:
        mu,g1,g2,sig12,sig21=pars
        b1,b2,a1,a2,b12,b21,k=constants(*pars)
        assert b12==a2 and k>0 and b21>0
        assert b1>b2>mu and 0<sig21<=sig12<=1
        ff=rhs(*map(float,pars))
        times=[100,1000,10000,100000]
        sol=solve_ivp(ff,(0,times[-1]),init,method='LSODA',t_eval=times,rtol=1e-10,atol=1e-17)
        assert sol.success
        A=[];B=[]
        for t,y in zip(times,sol.y.T):
            S,I1,I2,I21,I12,R1,R2,R=y
            J1,J2=I1+I21,I2+I12
            assert abs(sum(y)-1)<1e-8 and min(y)>-1e-9
            assert J1>0 and J2>0
            d=ff(t,y)
            assert abs((d[1]+d[3])+float(b1)*J1*((1-S)-float(sig21)*R2))<1e-11
            assert abs((d[2]+d[4])+float(b2)*J2*((1-S)-float(sig12)*R1))<1e-11
            assert abs(sum(d))<1e-10
            assert float(b1)*J1*(1-S-float(sig21)*R2)>=0
            assert float(b2)*J2*(1-S-float(sig12)*R1)>=0
            A.append(t*log(t)*J1)
            B.append(t*J2)
        assert abs(B[-1]-float(1/a2))<0.03
        assert abs(A[-1]-float(1/k))<0.15
        print('parameters=',list(map(str,pars)),'exact constants',f'a2={a2}',f'k={k}',
              'late indicators',f'tlog(t)J1={A[-1]:.9f}',f'tJ2={B[-1]:.9f}',
              'limits',f'{float(1/k):.9f}',f'{float(1/a2):.9f}')
    print('VERIFY_OK: exact rational boundary and positivity identities, two normalized full eight-compartment trajectories and finite tail checks')

if __name__=='__main__':
    finite_checks()
