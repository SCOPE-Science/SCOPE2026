#!/usr/bin/env python3
import math
from statistics import NormalDist

N = NormalDist()

def Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def phi(x):
    return math.exp(-0.5*x*x) / math.sqrt(2.0*math.pi)

def mean(xs):
    return sum(xs)/len(xs)

def sample_sd(xs):
    m=mean(xs)
    return math.sqrt(sum((x-m)**2 for x in xs)/(len(xs)-1))

def source_cross(a,b):
    m=len(a)
    ma,mb=mean(a),mean(b)
    da=math.sqrt(sum((x-ma)**2 for x in a)/m)
    db=math.sqrt(sum((x-mb)**2 for x in b)/m)
    return math.sqrt(m)*ma*mb/(abs(mb)*da) + math.sqrt(m)*mb*ma/(abs(ma)*db)

def reduced_cross(a,b):
    m=len(a)
    ta=math.sqrt(m)*mean(a)/sample_sd(a)
    tb=math.sqrt(m)*mean(b)/sample_sd(b)
    s=lambda x: 1.0 if x>0 else -1.0
    return math.sqrt(m/(m-1))*(s(tb)*ta+s(ta)*tb)

def adaptive_simpson(f,a,b,eps=1e-11,maxdepth=25):
    def simp(a,b,fa,fb,fm):
        return (b-a)*(fa+4*fm+fb)/6
    fa,fb=f(a),f(b); m=(a+b)/2; fm=f(m); whole=simp(a,b,fa,fb,fm)
    def rec(a,b,fa,fb,fm,whole,eps,depth):
        m=(a+b)/2; l=(a+m)/2; r=(m+b)/2
        fl,fr=f(l),f(r)
        left=simp(a,m,fa,fm,fl); right=simp(m,b,fm,fb,fr)
        if depth<=0 or abs(left+right-whole) <= 15*eps:
            return left+right+(left+right-whole)/15
        return rec(a,m,fa,fm,fl,left,eps/2,depth-1)+rec(m,b,fm,fb,fr,right,eps/2,depth-1)
    return rec(a,b,fa,fb,fm,whole,eps,maxdepth)

def cross_power(h, alpha):
    p=(1-math.sqrt(1-2*alpha))/2
    u=N.inv_cdf(1-p)
    delta=math.sqrt(2)*h
    f=lambda x: phi(x-delta)*(2*Phi(abs(x))-1)
    return adaptive_simpson(f,-10,-u)+adaptive_simpson(f,u,10)

def single_power(h, alpha):
    z=N.inv_cdf(1-alpha)
    return Phi(h)*Phi(h-z)+Phi(-h)*Phi(-h-z)

def main():
    a=[-0.8,0.3,1.7,2.1,0.2]
    b=[-1.2,-0.4,0.5,0.9,1.4]
    x=source_cross(a,b); y=reduced_cross(a,b)
    assert abs(x-y) < 1e-12, (x,y)

    alpha=0.05
    p=(1-math.sqrt(1-2*alpha))/2
    u=N.inv_cdf(1-p)
    c=math.sqrt(2)*u
    size=0.5*(1-(2*Phi(u)-1)**2)
    assert abs(size-alpha) < 2e-15
    assert abs(u-1.9488218625070588) < 2e-12
    assert abs(c-2.7560503086066777) < 2e-12

    z=N.inv_cdf(1-alpha)
    a0=z/math.sqrt(2)
    def gs(r):
        if r<=a0: return 0.0
        return Phi(r)-Phi(math.sqrt(2)*z-r)
    def gc(r):
        if r<=u: return 0.0
        return 2*Phi(r)-1
    for k in range(1,20000):
        r=5*k/20000
        d=gc(r)-gs(r)
        if a0 < r <= u:
            assert d < 1e-14
        if r > u:
            assert d > 0

    vals=[]
    for h in (0.25,0.5,0.75,1.0,1.5,2.0,3.0):
        pc=cross_power(h,alpha); ps=single_power(h,alpha)
        assert pc > ps
        vals.append((h,pc,ps))
    h,pc,ps=vals[3]
    assert abs(pc-0.2915585669881667) < 5e-10
    assert abs(ps-0.2189865506507057) < 5e-12
    print('VERIFY_OK')
    print(f'u_alpha={u:.15f} c_alpha={c:.15f} null_size={size:.15f}')
    print(f'h=1 cross_power={pc:.15f} single_power={ps:.15f}')

if __name__=='__main__':
    main()
