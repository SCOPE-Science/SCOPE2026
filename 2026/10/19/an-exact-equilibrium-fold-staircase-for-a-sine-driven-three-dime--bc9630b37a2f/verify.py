"""Reproducible numerical checks for the sine-driven flow's equilibrium-fold theorem.

Run: python3 verify.py
No nonstandard packages needed. All infinite or uniqueness claims rely on
analytical inequalities in RESULT.md, not on this finite computation.
"""
import math

PI=math.pi

def bisect(fun,lo,hi,n=90):
    flo=fun(lo); fhi=fun(hi)
    assert flo*fhi < 0, (lo,hi,flo,fhi)
    for _ in range(n):
        mid=(lo+hi)/2.0; fmid=fun(mid)
        if flo*fmid<=0: hi=mid
        else:lo=mid;flo=fmid
    return (lo+hi)/2.0

def branches(x,a,c,d,g,k):
    s=math.sqrt(d*d + 4*c*a*g*x*x/k)
    return (d-s)/(2*c), (d+s)/(2*c),s

def B(x,m,a,c,d,g,k):
    zm,zp,s=branches(x,a,c,d,g,k)
    return x * (-zm if m%2==0 else zp) / abs(math.sin(x))

def E(x,m,a,c,d,g,k):
    _,_,s=branches(x,a,c,d,g,k)
    return 2+d/s if m%2==0 else 2-d/s

def min_in_lobe(m,a,c,d,g,k):
    assert m>=1
    f=lambda x: x/math.tan(x)-E(x,m,a,c,d,g,k)
    eps=1e-5
    x=bisect(f,m*PI+eps,(m+0.5)*PI)
    return x,B(x,m,a,c,d,g,k)

def equilibria_for_b(b,a,c,d,g,k,nlobes=40):
    assert b>0
    # The unique positive root in (0,pi) is mandatory.
    points=[bisect(lambda x:B(x,0,a,c,d,g,k)-b,1e-10,PI-1e-5)]
    for m in range(1,nlobes+1):
        xm,threshold=min_in_lobe(m,a,c,d,g,k)
        if threshold < b-1e-7:
            q=lambda x:B(x,m,a,c,d,g,k)-b
            points.extend((bisect(q,m*PI+1e-5,xm),bisect(q,xm,(m+1)*PI-1e-5)))
    return points

def field(x,y,z,a,b,c,d,g,k):
    return (a*x-k*y*z,b*math.sin(x)+x*z,g*x*y-c*z+d)

def check():
    count=0
    for a,c,d,g,k in [(1.5,4,2,4,2),(.9,1.3,.5,2.2,3.3),(2.5,1.1,1.7,.8,.6)]:
        for m in range(1,16):
            xm,t=min_in_lobe(m,a,c,d,g,k)
            assert m*PI < xm < (m+.5)*PI
            for frac in (.03,.2,.7,.95):
                x=m*PI+frac*PI
                assert B(x,m,a,c,d,g,k)>=t*(1-1e-12)
                count+=1
            A=math.sqrt(a*g/(c*k));D=d/(2*c);L=(m+.5)*PI
            # The signed linear term is essential for the sharp asymptotic.
            approx=A*L*L+(-D if m%2==0 else D)*L
            assert abs((t-approx)/(A*L*L))<.12
            count+=1
    # Source's published parameter vector.
    a,b,c,d,g,k=1.5,10.,4.,2.,4.,2.
    positive=equilibria_for_b(b,a,c,d,g,k,nlobes=20)
    assert len(positive)==1,positive
    assert 2.59333<positive[0]<2.59334
    for x in positive:
        z=-b*math.sin(x)/x
        y=a*x/(k*z)
        for sign in (-1,1):
            r=field(sign*x,sign*y,z,a,b,c,d,g,k)
            assert max(abs(u) for u in r)<1e-9,r
            count+=3
    assert field(0,0,d/c,a,b,c,d,g,k)==(0.,0.,0.)
    count+=1
    # A larger sine amplitude creates further pairs on later half-waves.
    for b in (20.,60.,160.,400.):
        positive=equilibria_for_b(b,a,c,d,g,k,nlobes=25)
        expected=1+2*sum(1 for m in range(1,26) if min_in_lobe(m,a,c,d,g,k)[1]<b)
        assert len(positive)==expected,(b,len(positive),expected)
        for x in positive:
            z=-b*math.sin(x)/x;y=a*x/(k*z)
            assert max(abs(u) for u in field(x,y,z,a,b,c,d,g,k))<1e-7
            count+=1
    print('PASS:',count,'finite consistency checks. Baseline positive equilibrium x =',
          format(equilibria_for_b(10.,a,c,d,g,k,20)[0],'.14f'))

if __name__=='__main__':check()
