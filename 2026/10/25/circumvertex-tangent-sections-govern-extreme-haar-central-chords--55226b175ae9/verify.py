"""Independent finite endpoint and section-volume checks (Python standard library)."""
import math


def simpson(f, a, b, n=20000):
    assert n % 2 == 0
    h=(b-a)/n
    s=f(a)+f(b)
    for i in range(1,n):
        s+=(4 if i%2 else 2)*f(a+i*h)
    return s*h/3


def octahedron_tail(eps):
    # Region around an octahedron vertex e1 in polar coordinates.
    threshold=1/(1-eps/2)
    def integrand(phi):
        q=math.cos(phi)+math.sin(phi)
        rho=math.atan(q)-math.acos(threshold/math.sqrt(1+q*q))
        return 1-math.cos(rho)
    return (6*4/(4*math.pi))*simpson(integrand,0,math.pi/2)


def rectangle_tail(eps,a,b):
    R=math.hypot(a,b)
    radius=R-eps/2
    assert radius>max(a,b)
    width=math.asin(b/radius)-math.acos(a/radius)
    return 2*width/math.pi


def determinant(A):
    M=[row[:] for row in A]
    n=len(M)
    product=1.
    for j in range(n):
        i=max(range(j,n),key=lambda k:abs(M[k][j]))
        assert abs(M[i][j])>1e-12
        if i!=j:
            M[i],M[j]=M[j],M[i]
            product=-product
        p=M[j][j]
        product*=p
        for i in range(j+1,n):
            z=M[i][j]/p
            for k in range(j+1,n):
                M[i][k]-=z*M[j][k]
            M[i][j]=0
    return product


# These volumes are independent of any previous numerical checking results.
for a in [(1.,1.),(2.,1.),(.75,1.25)]:
    R=math.hypot(*a)
    target=R/(math.pi*a[0]*a[1])
    vals=[rectangle_tail(e,*a)/e for e in [.08,.04,.02,.01,.005]]
    assert vals==sorted(vals,reverse=True), (a, vals)
    assert abs(vals[-1]-target)/target<.008,(a,vals[-1],target)

for d in (2,3,4,5,7):
    a=[1+.3*j for j in range(d)]
    R=math.sqrt(sum(x*x for x in a))
    # The (d-1)-simplex at the positive circumvertex has edge vectors
    # R e_i/a_i-R e_d/a_d; independently compute its Gram determinant.
    m=d-1
    G=[[R*R*((1/a[i]**2 if i==j else 0.)+1/a[-1]**2)
        for j in range(m)] for i in range(m)]
    volume=math.sqrt(determinant(G))/math.factorial(m)
    exact=R**d/(math.factorial(m)*math.prod(a))
    assert abs(volume-exact)/exact<1e-9,(d,volume,exact)

for eps in (.1,.05,.02,.01,.005):
    ratio=octahedron_tail(eps)/eps**2
    target=3/(4*math.pi)
    assert abs(ratio-target)/target<2*eps,(eps,ratio,target)

for n in (4,6,8,12):
    # Independent exact even-polygon quantile gives the endpoint slope.
    b=math.pi/n
    predicted=n/(2*math.pi*math.tan(b))
    eps=.0001
    r=math.cos(b)
    u=math.acos(2*r/(2-eps))/b
    tail=1-u
    assert abs(tail/eps-predicted)/predicted<.005

print('VERIFY_OK: rectangle, octahedron, all-dimensional orthotope Gram, even polygon tests')
