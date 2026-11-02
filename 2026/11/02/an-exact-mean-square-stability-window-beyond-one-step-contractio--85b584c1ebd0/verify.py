"""Reproducible finite identities for two-row averaged Gaussian-free Kaczmarz.
Only standard Python is needed. Analytical infinite-time claims are proved separately.
"""
from fractions import Fraction as F
from math import comb, sqrt

def mm(B,v):
    return (B[0][0]*v[0]+B[0][1]*v[1], B[1][0]*v[0]+B[1][1]*v[1])

def check():
    exact=0
    numerical=0
    for a,d,r in [(F(4,5),F(1,5),F(2,5)),(F(9,10),F(1,10),F(3,10)),(F(25,26),F(1,26),F(5,26))]:
      assert r*r==a*d and a+d==1
      rho=a-d
      for eta in (1,2,3,4):
        choices=[(F(comb(eta,j),2**eta), F(2*j-eta,eta)) for j in range(eta+1)]
        assert sum(p for p,t in choices)==1
        assert sum(p*t for p,t in choices)==0
        assert sum(p*t*t for p,t in choices)==F(1,eta)
        exact+=3
        for alpha in (F(1,2),F(1),F(3,2),F(2),F(9,4)):
          B=(( (1-alpha*a)**2,alpha**2*a*d/eta),
             (alpha**2*a*d/eta,(1-alpha*d)**2))
          for X0,Y0 in ((F(1),F(0)),(F(0),F(1)),(F(1),F(2))):
            dist={(X0,Y0):F(1)}
            expected=(X0*X0,Y0*Y0)
            for step in range(1,4):
              nxt={}
              for (x,y),p in dist.items():
                for prob,t in choices:
                  xp=(1-alpha*a)*x-alpha*r*t*y
                  yp=(1-alpha*d)*y-alpha*r*t*x
                  nxt[xp,yp]=nxt.get((xp,yp),F(0))+p*prob
              dist=nxt
              expected=mm(B,expected)
              direct=(sum(p*x*x for (x,y),p in dist.items()),
                      sum(p*y*y for (x,y),p in dist.items()))
              assert expected==direct,(a,eta,alpha,step,expected,direct)
              exact+=2
          R=float(rho)
          A=float(alpha)
          eta_f=float(eta)
          xx=1-A+A*A*(1+R*R)/4
          rad=(R*(A-2))**2+(A*(1-R*R)/(2*eta_f))**2
          pf=xx+A*sqrt(rad)/2
          Bf=((float(B[0][0]),float(B[0][1])),(float(B[1][0]),float(B[1][1])))
          trace=Bf[0][0]+Bf[1][1]
          pf_direct=(trace+sqrt((Bf[0][0]-Bf[1][1])**2+4*Bf[0][1]**2))/2
          assert abs(pf-pf_direct)<1e-12
          numerical+=1
        bound=4/(1+sqrt(float(rho*rho+(1-rho*rho)/eta**2)))
        def rate(A):
          return 1-A+A*A*(1+float(rho*rho))/4+(A/2)*sqrt(float(rho*rho)*(A-2)**2+A*A*float((1-rho*rho)**2)/(4*eta*eta))
        assert abs(rate(bound)-1)<1e-12
        assert rate(.99*bound)<1 and rate(1.01*bound)>1
        numerical+=3
        if eta>1:
          stepbound=4/(1+float(rho)+float(1-rho)/eta)
          assert stepbound<bound
          assert rate((stepbound+bound)/2)<1
          numerical+=2
    print('VERIFY_OK exact='+str(exact)+' numerical='+str(numerical))

if __name__=='__main__':
    check()
