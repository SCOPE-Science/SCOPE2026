"""Standalone numerical checks for random-rotation Reuleaux convexification."""
import math,random
from fractions import Fraction

PI=math.pi

def theory_support(n,w,theta):
    a=PI/(2*n); R=w/(2*math.cos(a))
    period=2*PI/n
    tv=((theta+PI/n)%period)-PI/n
    td=((theta-PI+PI/n)%period)-PI/n
    if abs(tv)<=a+1e-12:
        return R*math.cos(tv)
    if abs(td)<=a+1e-12:
        return w-R*math.cos(td)
    raise AssertionError((tv,td))

def direct_support(n,w,theta):
    R=w/(2*math.cos(PI/(2*n)))
    q=2*PI/n
    ux,uy=math.cos(theta),math.sin(theta)
    verts=[(R*math.cos(q*j),R*math.sin(q*j)) for j in range(n)]
    ans=max(vx*ux+vy*uy for vx,vy in verts)
    a=PI/(2*n)
    for j,(vx,vy) in enumerate(verts):
        ang=q*j+PI
        diff=(theta-ang+PI)%(2*PI)-PI
        t=max(-a,min(a,diff))
        x,y=vx+w*math.cos(ang+t),vy+w*math.sin(ang+t)
        ans=max(ans,x*ux+y*uy)
    return ans

def cdf(n,w,x):
    a=PI/(2*n); R=w/(2*math.cos(a))
    if x<w-R:return 0.
    if x<=w/2:return math.acos(max(-1,min(1,(w-x)/R)))/(2*a)
    if x<R:return 1-math.acos(max(-1,min(1,x/R)))/(2*a)
    return 1.

def simpson(fun,a,b,steps=20000):
    if steps%2:steps+=1
    h=(b-a)/steps
    s=fun(a)+fun(b)
    for i in range(1,steps):s+=(4 if i%2 else 2)*fun(a+i*h)
    return s*h/3

def expected_perimeter(n,m,w=1.):
    a=PI/(2*n);R=w/(2*math.cos(a))
    integral=simpson(lambda t: math.sin(t)*((t/(2*a))**m+(1-t/(2*a))**m),0,a,2000)
    return 2*PI*R*(1-integral)

def main():
    rng=random.Random(7503991)
    count=0
    for n in (3,5,7,11,21):
        for w in (0.3,1.,4.):
            for k in range(600):
                theta=2*PI*((k+0.231)/600)+0.00021
                err=abs(theory_support(n,w,theta)-direct_support(n,w,theta))
                assert err<1e-10,(n,w,theta,err)
                count+=1
        a=PI/(2*n)
        for m in (1,2,3,5,10,20):
            expv=expected_perimeter(n,m)
            if m==1:
                assert abs(expv-PI)<1e-10,(n,m,expv)
            if m==2:
                prediction=PI/2+PI*(1-math.cos(a))/(a*a*math.cos(a))
                assert abs(expv-prediction)<1e-10,(n,m,expv,prediction)
            if m>1:assert expv>PI
            assert expv<=PI/math.cos(a)
            count+=1
        for m in (40,80,160,320):
            deficit=PI/math.cos(a)-expected_perimeter(n,m)
            ratio=(m*m*deficit)/(8*PI*(1/(2*math.cos(a)))*a*a)
            assert abs(ratio-1)<0.11,(n,m,ratio)
            count+=1
    n=7; m=4;w=1.;N=130000
    sample=[]
    for i in range(N):
        val=max(theory_support(n,w,2*PI*rng.random()) for _ in range(m))
        sample.append(val)
    empirical=2*PI*sum(sample)/N
    expected=expected_perimeter(n,m,w)
    assert abs(empirical-expected)<0.008,(empirical,expected)
    count+=1
    a=PI/(2*n);R=w/(2*math.cos(a))
    for s in (0.7,1.2,2.):
        y=2*R*a*a*s*s
        for m in (200,400,800):
            f=cdf(n,w,R-y/(m*m))**m
            assert abs(f-math.exp(-s))<0.004,(m,s,f,math.exp(-s))
            count+=1
    print('VERIFY_OK',count,'support/parameter/numeric checks', 'MonteCarlo',round(empirical,6),'theory',round(expected,6))

if __name__=='__main__':main()

# Check the deterministic exact Hausdorff expression when largest angular gap < half period.
def test_hausdorff():
    rg=random.Random(91931)
    checks=0
    for n in (3,5,9):
        R=1/(2*math.cos(math.pi/(2*n)))
        q=2*math.pi/n
        for m in (10,20,30):
            for _ in range(5):
                angles=sorted(q*rg.random() for k in range(m))
                gaps=[angles[(j+1)%m]-angles[j] if j<m-1 else angles[0]+q-angles[-1] for j in range(m)]
                G=max(gaps)
                assert G<q/2
                # At midpoint of largest gap, nearest vertex distance is G/2.
                j=max(range(m),key=lambda j:gaps[j])
                midpoint=(angles[j]+G/2)%q
                h=max(theory_support(n,1.,midpoint-a) for a in angles)
                assert abs((R-h)-R*(1-math.cos(G/2)))<1e-10,(n,m,R-h,R*(1-math.cos(G/2)))
                checks+=1
    print('HAUSDORFF_OK',checks,'exact mid-gap identities')

if __name__=='__main__':test_hausdorff()

# Independent spacings check: normalized exponentials converge to a Gumbel maximum.
def test_gumbel():
    rg=random.Random(32278)
    m=300
    N=2200
    stats=[]
    for _ in range(N):
        expo=[-math.log1p(-rg.random()) for j in range(m)]
        stats.append(m*max(expo)/sum(expo)-math.log(m))
    for t in (-1.,0.,1.):
        empirical=sum(z<=t for z in stats)/N
        exact=math.exp(-math.exp(-t))
        assert abs(empirical-exact)<0.06,(t,empirical,exact)
    print('GUMBEL_OK',N,'normalized maximal-spacing replicates')

if __name__=='__main__':test_gumbel()
