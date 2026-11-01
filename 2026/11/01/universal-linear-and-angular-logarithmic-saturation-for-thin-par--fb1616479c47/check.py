"""Reproducible numerical checks for the thin-parallelogram distance-gap law.

Requires mpmath 1.3. All integrations use independently normalized
edge-pair and interior-pair decompositions. The proof is analytic.
Run: python check.py
"""
import mpmath as mp
import math
import random
mp.mp.dps=45


def phi(x,b):
    return (x*mp.sqrt(x*x+b*b)+b*b*mp.asinh(x/b))/2

def psi(x,b):
    return (x*x+b*b)**mp.mpf('1.5')/3

def F(a,b):
    return ((1-a)*(phi(a,b)-phi(a-1,b)) + psi(a,b)-psi(a-1,b)
            +(1+a)*(phi(a+1,b)-phi(a,b)) - psi(a+1,b)+psi(a,b))

def mean_pair(eps,theta):
    c=mp.cos(theta); h=mp.sin(theta)
    mean_in=mp.quad(lambda z: 2*(1-z)*F(eps*c*z,eps*h*z) if z else mp.mpf(2)/3,[0,1])
    HH=mp.mpf(1)/6+F(eps*c,eps*h)/2
    def hvr(r):
        if not r:return mp.mpf('1')/2
        a=eps*c*r;b=eps*h*r
        return (phi(1+a,b)-phi(a,b)+phi(1-a,b)-phi(-a,b))/2
    HV=mp.quad(hvr,[0,1])
    VV=eps/6+mp.quad(lambda z:(1-z)*(mp.sqrt((1+eps*c*z)**2+(eps*h*z)**2)
                    +mp.sqrt((1-eps*c*z)**2+(eps*h*z)**2)),[0,1])/2
    # VV above: opposite-edge probability 1/2, and E over signed triangular z
    # E opposite-edge distance = int_0^1 (1-z)*(f(+z)+f(-z)) dz.
    # Thus VV = eps/6 + 0.5 * that integral.
    bd=(HH+2*eps*HV+eps**2*VV)/(1+eps)**2
    return mean_in,bd

def law(eps,theta):
    c=mp.cos(theta);h=mp.sin(theta)
    L=mp.log(2/(eps*h))
    return eps/3+eps**2*(h*h*(L/3-mp.mpf(55)/72)-c*c/6)


def test():
    # Compare the primitive with direct weighted distance integration.
    for a,b in [(mp.mpf('.1'),mp.mpf('.2')),
                (mp.mpf('-.23'),mp.mpf('.07')),
                (mp.mpf('.014'),mp.mpf('.008'))]:
        direct=mp.quad(lambda z:(1+z)*mp.sqrt((z+a)**2+b*b),[-1,0]) + \
               mp.quad(lambda z:(1-z)*mp.sqrt((z+a)**2+b*b),[0,1])
        assert abs(direct-F(a,b))<mp.mpf('1e-35')
        assert abs(F(a,b)-F(-a,b))<mp.mpf('1e-35')
    angles=[mp.pi/2,mp.pi/3,mp.pi/6,mp.mpf('2.2')]
    for a in angles:
        print('angle',mp.nstr(a,12))
        for eps in [mp.mpf('.04'),mp.mpf('.02'),mp.mpf('.01'),mp.mpf('.005')]:
            inside,boundary=mean_pair(eps,a)
            gap=boundary-inside
            approximate=law(eps,a)
            residual=(gap-approximate)/(eps**3*mp.log(1/eps))
            assert gap>0
            assert abs(residual)<mp.mpf(5)
            print('  width',mp.nstr(eps,5),'gap',mp.nstr(gap,15),
                  'scaled remainder',mp.nstr(residual,8))
        eps=mp.mpf('.006')
        g1=mean_pair(eps,a)[1]-mean_pair(eps,a)[0]
        g2=mean_pair(eps,mp.pi-a)[1]-mean_pair(eps,mp.pi-a)[0]
        assert abs(g1-g2)<mp.mpf('1e-28')
    # The independently known square line-picking constant checks the
    # interior normalization (unit-square limit eps=1).
    interior,surface=mean_pair(mp.mpf(1),mp.pi/2)
    known=(2+mp.sqrt(2)+5*mp.asinh(1))/15
    assert abs(interior-known)<mp.mpf('1e-28')
    print('square interior',mp.nstr(interior,20),'boundary',mp.nstr(surface,20))
    # A separate direct sampler of area and arclength measures.
    rng=random.Random(12341)
    N=180000
    width=.3; angle=math.pi/3; c=math.cos(angle);h=math.sin(angle)
    sumi=sumb=0.0
    def interior_point():
        x=rng.random();y=rng.random()
        return x+width*c*y,width*h*y
    def boundary_point():
        # Each of two unit edges and two width edges has its true length mass.
        edge=rng.random()*2*(1+width)
        t=rng.random()
        if edge<1:return t,0.0
        if edge<2:return t+width*c,width*h
        if edge<2+width:return width*c*t,width*h*t
        return 1+width*c*t,width*h*t
    for _ in range(N):
        u,v=interior_point(),interior_point()
        sumi+=math.hypot(u[0]-v[0],u[1]-v[1])
        u,v=boundary_point(),boundary_point()
        sumb+=math.hypot(u[0]-v[0],u[1]-v[1])
    ai,ab=mean_pair(mp.mpf('0.3'),mp.pi/3)
    assert abs(sumi/N-float(ai))<.004
    assert abs(sumb/N-float(ab))<.004
    print('direct pair samples',N,'absolute errors',abs(sumi/N-float(ai)),abs(sumb/N-float(ab)))
    print('ALL CHECKS PASSED')

if __name__=='__main__':test()
