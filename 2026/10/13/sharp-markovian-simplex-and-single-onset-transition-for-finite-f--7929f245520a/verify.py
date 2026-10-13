"""Finite checks for Weyl-line semigroup mixtures; standard library only.

These tests corroborate, but do not replace, the all-prime-power proof.
"""
import cmath
import math
import random


def field(q):
    assert q in (3, 4, 5, 7)
    if q != 4:
        return ((lambda a,b:(a+b)%q), (lambda a,b:(a*b)%q),
                (lambda a:a%q), q)
    def add(a,b): return a ^ b
    def mul(a,b):
        z=0
        for bit in range(2):
            if (b>>bit)&1: z ^= a<<bit
        for power in (2,):
            if z&(1<<power): z ^= 0b111 << (power-2)
        return z
    def tr(a): return add(a,mul(a,a))
    assert all(tr(a) in (0,1) for a in range(4))
    return add,mul,tr,2


def case(q,x,c,t):
    add,mul,tr,p=field(q)
    y=math.exp(-c*t)
    ell=[]
    for slope in range(q):
        ell.append([(z,mul(slope,z)) for z in range(1,q)])
    ell.append([(0,z) for z in range(1,q)])
    line={v:j for j,lv in enumerate(ell) for v in lv}
    assert len(line)==q*q-1 and len(ell)==q+1
    g=[c*(1-w)*y/(w+(1-w)*y) for w in x]
    direct=[]
    for j,lv in enumerate(ell):
        u=lv[0]
        ff=0j
        for v,iv in line.items():
            ch=tr(add(mul(u[1],v[0]),(-mul(u[0],v[1]))%q)) if q!=4 else tr(add(mul(u[1],v[0]),mul(u[0],v[1])))
            ff+=-g[iv]*cmath.exp(2j*math.pi*ch/p)
        direct.append(ff/(q*q))
    formula=[(sum(g)-q*g[j])/(q*q) for j in range(q+1)]
    for a,b in zip(direct,formula):
        assert abs(a.imag)<1e-12,(q,x,t,a,b)
        assert abs(a.real-b)<1e-12,(q,x,t,a,b)
    # Independent sign decision from normalized end-point inequality.
    if min(x)>0:
        aa=[(1-w)/w for w in x]
        m=max(aa)
        val=sum(aa)-q*m
        jm=aa.index(m)
        if val>=0:
            assert all(v>=-1e-12 for v in formula)
        else:
            # U is increasing with y, crossing exactly once.
            U=lambda z:sum(aa[i]*(1+m*z)/(1+aa[i]*z) for i in range(q+1) if i!=jm)-(q-1)*m
            assert U(0)<0 and U(1)>0
            lo,hi=0.,1.
            for _ in range(70):
                md=(lo+hi)/2
                if U(md)>0:hi=md
                else:lo=md
            root=(lo+hi)/2
            if abs(y-root)>1e-8:
                assert (formula[jm]>0)==(y>root),(q,x,c,t,root,formula)
            assert all(v>=formula[jm]-1e-12 for v in formula)
    else:
        count=sum(w>0 for w in x)
        if count==1: assert all(v>=-1e-12 for v in formula)
        elif t>0:
            assert any(v<-1e-14 for v in formula), (q,x,t,formula)
    return len(line)


def main():
    rr=random.Random(20261009)
    checked=0
    for q in (3,4,5,7):
        for idx in range(240):
            arr=[rr.uniform(.01,4) for _ in range(q+1)]
            if idx%6==0:arr[0]=0.
            if idx%11==0:arr=[float(i==0) for i in range(q+1)]
            if idx%13==0:arr=[1.]* (q+1)
            if idx%17==0:arr=[1., .01]+[.0001]*(q-1)
            s=sum(arr)
            x=[a/s for a in arr]
            for t in (0.,.013,.1,.47,1.,2.7,8.,20.):
                checked+=case(q,x,1.7,t)
    # Exact qutrit delayed-onset root and sharp interior equality point.
    a=[9.,7./3,7./3,7./3]
    m=max(a)
    def F(y):
        return sum(v*(1+m*y)/(1+v*y) for v in a if v!=m)-2*m
    assert F(0.)<0<F(1.) and abs(F(11./21))<1e-12
    r=3*math.sqrt(3)-5
    x=[r]+[(1-r)/3]*3
    aa=[(1-v)/v for v in x]
    assert abs(sum(aa)-3*max(aa))<1e-10
    assert all(v>0 for v in aa)
    for t in (0.,1.,3.,8.):
        case(3,x,1.,t)
    print('VERIFY_OK',checked,'direct finite-field character checks', 'q=3,4,5,7',
          'plus exact example and critical-boundary checks')

if __name__=='__main__':main()
