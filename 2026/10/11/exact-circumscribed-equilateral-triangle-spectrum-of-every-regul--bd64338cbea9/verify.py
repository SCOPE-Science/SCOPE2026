#!/usr/bin/env python3
import math

def u(t):
    return (math.cos(t), math.sin(t))

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]

def det(a,b):
    return a[0]*b[1]-a[1]*b[0]

def regular_vertices(n,R=1.0):
    return [(R*math.cos(2*math.pi*j/n),R*math.sin(2*math.pi*j/n)) for j in range(n)]

def support_direct(vertices,t):
    nn=u(t)
    return max(dot(v,nn) for v in vertices)

def line_intersection(n1,h1,n2,h2):
    D=det(n1,n2)
    assert abs(D)>1e-14
    return ((h1*n2[1]-n1[1]*h2)/D,
            (n1[0]*h2-h1*n2[0])/D)

def triangle_from_support(vertices,theta):
    normals=[u(theta+2*math.pi*k/3) for k in range(3)]
    hs=[max(dot(v,normals[k]) for v in vertices) for k in range(3)]
    pts=[line_intersection(normals[1],hs[1],normals[2],hs[2]),
         line_intersection(normals[2],hs[2],normals[0],hs[0]),
         line_intersection(normals[0],hs[0],normals[1],hs[1])]
    for v in vertices:
        for nn,h in zip(normals,hs):
            assert dot(v,nn)<=h+2e-12
    sides=[]
    for i in range(3):
        a,b=pts[i],pts[(i+1)%3]
        sides.append(math.hypot(a[0]-b[0],a[1]-b[1]))
    assert max(sides)-min(sides)<3e-11
    area=abs(sum(pts[i][0]*pts[(i+1)%3][1]-pts[(i+1)%3][0]*pts[i][1] for i in range(3)))/2
    rho=sum(hs)/3
    predicted=3*math.sqrt(3)*rho*rho
    assert abs(area-predicted)<3e-10
    return rho,area

def h_closed(n,t,R=1.0):
    Delta=2*math.pi/n
    x=(t+Delta/2)%Delta-Delta/2
    return R*math.cos(x)

def rho_closed_direct(n,t,R=1.0):
    return sum(h_closed(n,t+2*math.pi*k/3,R) for k in range(3))/3

def endpoints(n,R=1.0):
    if n%3==0:
        rmax=R
        rmin=R*math.cos(math.pi/n)
    else:
        C=R/3*(1+2*math.cos(2*math.pi/(3*n)))
        rmax=C
        rmin=C*math.cos(math.pi/(3*n))
    return rmin,rmax

worst_area=0.0
for n in range(3,41):
    verts=regular_vertices(n)
    for j in range(29):
        theta=(j+0.371)*2*math.pi/(29*n)
        rho,area=triangle_from_support(verts,theta)
        rho2=rho_closed_direct(n,theta)
        worst_area=max(worst_area,abs(rho-rho2))
        assert abs(rho-rho2)<2e-13

worst_endpoint=0.0
for n in range(3,151):
    rmin,rmax=endpoints(n)
    vals=[]
    # A full period of the support sum is at most 2*pi/n; this dense sweep
    # is only a regression check, with exact candidate extrema added below.
    for k in range(2401):
        t=(2*math.pi/n)*k/2400
        vals.append(rho_closed_direct(n,t))
    if n%3==0:
        vals.extend([rho_closed_direct(n,0),rho_closed_direct(n,math.pi/n)])
    else:
        Delta=2*math.pi/n
        vals.extend([rho_closed_direct(n,0),rho_closed_direct(n,Delta/6),rho_closed_direct(n,-Delta/6)])
    observed_min=min(vals); observed_max=max(vals)
    worst_endpoint=max(worst_endpoint,abs(observed_min-rmin),abs(observed_max-rmax))
    assert observed_min>=rmin-2e-12
    assert observed_max<=rmax+2e-12
    assert abs(observed_min-rmin)<2e-10
    assert abs(observed_max-rmax)<2e-10

# Check factor-nine leading asymptotic using neighboring large residues.
def spread(n):
    mn,mx=endpoints(n)
    return 3*math.sqrt(3)*(mx*mx-mn*mn)
for N in (3000,6000,12000):
    a=spread(N)*N*N
    b=spread(N+1)*(N+1)*(N+1)
    target_a=3*math.sqrt(3)*math.pi**2
    target_b=math.sqrt(3)*math.pi**2/3
    assert abs(a-target_a)/target_a<2e-5
    assert abs(b-target_b)/target_b<2e-5
    assert abs((a/b)-9)<3e-4

print('VERIFY_OK')
print('direct_support_intersections_n = 3..40')
print('spectrum_sweep_n = 3..150')
print('max_support_formula_error = %.3e' % worst_area)
print('max_endpoint_error = %.3e' % worst_endpoint)
print('modulo_three_asymptotic_ratio = passed')
