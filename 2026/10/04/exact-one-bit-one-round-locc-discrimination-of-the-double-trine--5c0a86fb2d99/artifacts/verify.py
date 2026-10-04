import math

SQ3=math.sqrt(3.0)
ns=((0.0,1.0),(SQ3/2.0,-0.5),(-SQ3/2.0,-0.5))
CLAIM=(4.0+SQ3+math.sqrt(15.0+6.0*SQ3))/12.0

def norm(v):
    return math.hypot(v[0],v[1])

def pair_candidate(q,i,j):
    k=3-i-j
    p=(q[i]*ns[i][0],q[i]*ns[i][1])
    z=(q[j]*ns[j][0],q[j]*ns[j][1])
    dx,dy=z[0]-p[0],z[1]-p[1]
    d=math.hypot(dx,dy)
    R=(q[i]+q[j]+d)/2.0
    t=(d+q[j]-q[i])/(2.0*d)
    g=(p[0]+t*dx,p[1]+t*dy)
    feasible=(R-q[k] >= norm((g[0]-q[k]*ns[k][0],g[1]-q[k]*ns[k][1]))-2e-11)
    return R,g,feasible

def triple_candidate(q):
    e2=q[0]*q[1]+q[1]*q[2]+q[2]*q[0]
    e3=q[0]*q[1]*q[2]
    den=4.0*e3-e2*e2
    if min(q)<=0.0 or den<=0.0:
        return None
    R=2.0*e2*e3/den
    S1=sum(1.0/x for x in q)
    K=6.0*R/S1
    dots=[R-K/(2.0*x) for x in q]
    gx=(2.0/3.0)*sum(dots[i]*ns[i][0] for i in range(3))
    gy=(2.0/3.0)*sum(dots[i]*ns[i][1] for i in range(3))
    g=(gx,gy)
    ok=True
    for i in range(3):
        lhs=R-q[i]
        rhs=norm((g[0]-q[i]*ns[i][0],g[1]-q[i]*ns[i][1]))
        if lhs < -2e-10 or abs(lhs-rhs)>2e-8:
            ok=False
    return (R,g,ok)

def S(q):
    vals=[]
    for i,j in ((0,1),(0,2),(1,2)):
        R,g,ok=pair_candidate(q,i,j)
        if ok: vals.append(R)
    t=triple_candidate(q)
    if t and t[2]: vals.append(t[0])
    if not vals:
        raise RuntimeError(('no dual candidate',q))
    return min(vals)

def total(phi):
    m=(math.cos(phi),math.sin(phi))
    dots=[m[0]*n[0]+m[1]*n[1] for n in ns]
    qp=[(1+x)/3.0 for x in dots]
    qm=[(1-x)/3.0 for x in dots]
    return 0.5*(S(qp)+S(qm))

q=[1/3,(2+SQ3)/6,(2-SQ3)/6]
assert max(abs(q[0]-1/3),abs(q[1]-(2+SQ3)/6),abs(q[2]-(2-SQ3)/6))<1e-15
assert abs(total(0.0)-CLAIM)<2e-12
mx=-1.0; arg=None
N=20000
for k in range(N+1):
    ph=(math.pi/6)*k/N
    v=total(ph)
    if v>mx:
        mx,arg=v,ph
assert mx <= CLAIM+3e-11, (mx,CLAIM,arg)
assert abs(arg)<1e-12
print('VERIFY_OK')
print('claimed_probability=%.15f'%CLAIM)
print('grid_max=%.15f angle=%.15g'%(mx,arg))
