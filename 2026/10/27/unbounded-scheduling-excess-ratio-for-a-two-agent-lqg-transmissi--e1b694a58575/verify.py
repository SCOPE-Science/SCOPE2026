"""Exact arithmetic checks for a two-agent, two-step LQG scheduling instance.
This verification is finite and supplements the analytical inequalities.
"""
from fractions import Fraction as F
from itertools import product

def data(e):
    r=e*e; a=r/(16*(1+r)*(5+4*r)); b=F(1,16)/(1+r); c=e/3; lam=e**3
    return a,b,c,lam

def cost(e, schedule):
    # A transmission resets error; otherwise e(k+1) = (1/2)e(k).
    a,b,c,lam=data(e)
    (s10,s20),(s11,s21)=schedule
    return a*(1-s10)+b*(1-s10)*(1-s11)+c*(1-s20)+lam*(s10+s20+s11+s21)

def test(e):
    a,b,c,lam=data(e)
    possibilities=[]
    for s0 in ((0,0),(1,0),(0,1)):
        for s1 in ((0,0),(1,0),(0,1)):
            sch=(s0,s1)
            possibilities.append((cost(e,sch),sch))
    opt=min(possibilities)
    scores=(a+b-lam,c-lam)
    assert scores[0]>scores[1]>0
    # Auction t0 grants agent one; at t1 all remaining scores are negative.
    auction=((1,0),(0,0))
    assert cost(e,auction)==c+lam
    assert opt==(a+2*lam,((0,1),(1,0))), (e,opt)
    assert c+lam > a+2*lam
    return (e,opt[0],cost(e,auction),cost(e,auction)/opt[0])

for n in (10, 20, 50, 100, 1000, 10000):
    print(test(F(1,n)))

# Independent Riccati recursions at k=0 and k=1.
def riccati(A,B,Q,R,Qterminal):
    P=[None,None,Qterminal]
    Gamma=[None,None]
    for k in (1,0):
        denom=R+B*B*P[k+1]
        L=B*P[k+1]*A/denom
        Gamma[k]=denom*L*L
        P[k]=Q+A*A*P[k+1]-A*A*B*B*P[k+1]*P[k+1]/denom
    return P,Gamma

for n in (10,20,100,1000):
    e=F(1,n); a,b,c,lam=data(e)
    _,g1=riccati(F(1,2),F(1),F(0),e*e,F(1))
    _,g2=riccati(F(1,2),F(1),F(2),F(1),F(0))
    assert g1[0]==a and g1[1]/4==b
    assert e*g2[0]==c and g2[1]==0
    assert (F(1,3)*e+e**3)/(a+2*e**3) > 1
print('All exact checks passed.')
