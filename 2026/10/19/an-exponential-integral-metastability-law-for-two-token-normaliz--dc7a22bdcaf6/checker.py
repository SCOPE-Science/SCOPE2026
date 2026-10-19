"""Supplementary numerical consistency checks for the two-token sphere map.

All asymptotic conclusions in the accompanying proof are analytical;
these experiments only test the finite-step identities and trends.
"""
import math
import random


def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def unit(a):
    r=norm(a)
    return tuple(x/r for x in a)

def direct_step(u,v,beta,eta):
    c=dot(u,v)
    t=1/(1+math.exp(beta*(1-c)))
    a=tuple((1+eta*(1-t))*x+eta*t*y for x,y in zip(u,v))
    b=tuple((1+eta*(1-t))*y+eta*t*x for x,y in zip(u,v))
    return unit(a),unit(b)

def scalar_step(c,beta,eta):
    alpha=2*eta/(1+eta)
    t=1/(1+math.exp(beta*(1-c)))
    r=1-alpha*t
    delta=(1-c*c)*(1-r*r)/(1+c+(1-c)*r*r)
    return c+delta

def e1(z):
    # Simpson quadrature for \int_z^40 e^{-t}/t dt; tail < e^{-40}/40.
    N=40000
    a=z;b=40.0;h=(b-a)/N
    sm=math.exp(-a)/a+math.exp(-b)/b
    for j in range(1,N):
        x=a+h*j
        sm+=(4 if j%2 else 2)*math.exp(-x)/x
    return sm*h/3

def hitting(beta,c0,ctarget,eta,max_steps=3000000):
    c=c0
    for n in range(max_steps+1):
        if c>=ctarget: return n
        c=scalar_step(c,beta,eta)
    raise RuntimeError('Increase max_steps for this diagnostic')

def main():
    rng=random.Random(72633)
    total=0
    for d in (2,3,5,9):
      for beta in (0.1,0.8,2.0,5.0):
       for eta in (0.2,1.0,3.0):
        for k in range(30):
            u=unit([rng.uniform(-1,1) for _ in range(d)])
            v=unit([rng.uniform(-1,1) for _ in range(d)])
            c=dot(u,v)
            up,vp=direct_step(u,v,beta,eta)
            cp=scalar_step(c,beta,eta)
            assert abs(dot(up,vp)-cp)<2e-12, (d,beta,eta,c)
            a=unit([x+y for x,y in zip(u,v)])
            ap=unit([x+y for x,y in zip(up,vp)])
            assert norm([x-y for x,y in zip(a,ap)])<2e-12
            total+=1
    print('Direct vector and scalar identity cases:',total)
    for beta in (6,8,10,11):
        t=hitting(beta,0.0,0.5,1.0)
        ratio=t*beta*math.exp(-beta)
        print('Fixed-correlation beta, exit time, scaled value:',beta,t,ratio)
        assert abs(ratio-1)<0.06
    zz=1.0; target=e1(zz)/2
    values=[]
    for beta in (4,5,6,7,8):
        t=hitting(beta,-1+zz/beta,0.0,1.0)
        value=t*math.exp(-2*beta)
        values.append(value)
        print('Antipodal-layer beta, exit time, scaled value:',beta,t,value)
    assert all(values[j+1] < values[j] for j in range(len(values)-1))
    assert abs(values[-1]-target)<0.02
    print('Independent quadrature of asymptotic constant:', target)
    print('All finite checks passed.')

if __name__=='__main__': main()
