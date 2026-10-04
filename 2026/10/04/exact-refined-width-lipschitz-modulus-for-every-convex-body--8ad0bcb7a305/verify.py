import math

# Exact support-function checks for three nonsmooth/smooth examples.

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def width_vertices(V,u):
    vals=[dot(x,u) for x in V]
    return max(vals)-min(vals)

def source_p_vertices(V,u,tol=1e-12):
    vals=[dot(x,u) for x in V]
    hi=max(vals); lo=min(vals)
    top=[x for x,z in zip(V,vals) if hi-z <= tol]
    bot=[x for x,z in zip(V,vals) if z-lo <= tol]
    best=None
    for A in top:
        for B in bot:
            d=[A[i]-B[i] for i in range(len(u))]
            r=norm(d)
            if best is None or r>best[0]: best=(r,A,B)
    s,A,B=best
    w=hi-lo
    p=math.sqrt(max(0.0,s*s-w*w))
    return p,A,B,w

def witness_check(V,u):
    p,A,B,w=source_p_vertices(V,u)
    D=[A[i]-B[i] for i in range(len(u))]
    y=[D[i]-w*u[i] for i in range(len(u))]
    assert abs(norm(y)-p) < 1e-10
    if p < 1e-11: return
    xi=[z/p for z in y]
    assert abs(dot(xi,u)) < 1e-10
    for t in (1e-3,3e-4,1e-4,3e-5):
        v=[math.cos(t)*u[i]+math.sin(t)*xi[i] for i in range(len(u))]
        q=(width_vertices(V,v)-width_vertices(V,u))/t
        lower=(w*(math.cos(t)-1)+p*math.sin(t))/t
        assert q + 1e-10 >= lower
        assert abs(lower-p) < 3*t*(w+p+1)

# Cube at a facet normal: the exposed faces are 2-dimensional, so this checks the genuinely nonsmooth case.
V3=[[sx,sy,sz] for sx in (-1.0,1.0) for sy in (-1.0,1.0) for sz in (-1.0,1.0)]
u=[1.0,0.0,0.0]
p,A,B,w=source_p_vertices(V3,u)
assert abs(p-2*math.sqrt(2)) < 1e-12
witness_check(V3,u)

# Square at a vertex-transition direction and at an axis direction.
V2=[[-1.,-1.],[1.,-1.],[1.,1.],[-1.,1.]]
for u in ([1.,0.],): witness_check(V2,list(u))

# Regular octahedron at a nonsmooth direction.
O=[]
for i in range(3):
    for s in (-1.,1.):
        x=[0.,0.,0.]; x[i]=s; O.append(x)
u=[1/math.sqrt(3)]*3
witness_check(O,u)

# Smooth ellipsoid consistency: spherical gradient norm of width equals p_K.
Q=[4.0,2.0,0.5]
for raw in ([1.,2.,3.],[2.,-1.,1.],[1.,1.,0.2]):
    nr=norm(raw); u=[x/nr for x in raw]
    h=math.sqrt(sum(Q[i]*u[i]*u[i] for i in range(3)))
    A=[Q[i]*u[i]/h for i in range(3)]
    D=[2*x for x in A]; w=2*h
    y=[D[i]-w*u[i] for i in range(3)]
    p=norm(y)
    # gradient of w=2*sqrt(u^T Q u), projected tangentially
    g=[2*Q[i]*u[i]/h for i in range(3)]
    gu=dot(g,u)
    gt=[g[i]-gu*u[i] for i in range(3)]
    assert abs(norm(gt)-p) < 1e-11

print('VERIFY_OK exact refined width modulus')
