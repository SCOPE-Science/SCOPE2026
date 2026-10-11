import math

N=16
V=[(math.cos(k*math.pi/8),math.sin(k*math.pi/8)) for k in range(N)]
d0=(V[1][0]-V[0][0],V[1][1]-V[0][1])
q=2-math.sqrt(2)-1.5*math.sqrt(2-math.sqrt(2))+0.5*math.sqrt(2+math.sqrt(2))
T=1-math.sqrt(2)+2*math.sqrt(4-2*math.sqrt(2))
k1=-2-2*math.sqrt(2-math.sqrt(2))+2*math.sqrt(2+math.sqrt(2))
k2=-math.sqrt(2+math.sqrt(2))-math.sqrt(2-math.sqrt(2))+2*math.sqrt(2)
assert 0<q<0.5 and k1>0 and k2>0
assert abs(k1*q-k2*(1-2*q))<2e-14

def det(a,b,c,d): return a*d-b*c

def st_affine(j,k):
    dy=(V[(j+1)%N][0]-V[j][0],V[(j+1)%N][1]-V[j][1])
    dz=(V[(k+1)%N][0]-V[k][0],V[(k+1)%N][1]-V[k][1])
    D=det(dy[0],dz[0],dy[1],dz[1])
    if abs(D)<1e-13: return None
    # rhs(a)=V0-Vj-Vk+a*d0
    r0=(V[0][0]-V[j][0]-V[k][0],V[0][1]-V[j][1]-V[k][1])
    def solve(rhs):
        return ((rhs[0]*dz[1]-rhs[1]*dz[0])/D,
                (dy[0]*rhs[1]-dy[1]*rhs[0])/D)
    s0,t0=solve(r0); s1,t1=solve((r0[0]+d0[0],r0[1]+d0[1]))
    return (s0,s1-s0,t0,t1-t0)

def feasible_interval(coeff):
    s0,sa,t0,ta=coeff
    lo,hi=0.0,1.0
    for c,m in ((s0,sa),(t0,ta)):
        if abs(m)<1e-14:
            if c < -1e-12 or c > 1+1e-12: return None
        else:
            u=(0-c)/m; v=(1-c)/m
            lo=max(lo,min(u,v)); hi=min(hi,max(u,v))
    if hi-lo<1e-10: return None
    return (lo,hi)

found={}
for j in range(N):
    for k in range(N):
        c=st_affine(j,k)
        if c is None: continue
        iv=feasible_interval(c)
        if iv is not None: found[(j,k)]=iv
expected={(2,13),(3,13),(3,14),(13,2),(13,3),(14,3)}
assert set(found)==expected, (set(found),expected)
for pair in ((2,13),(13,2)):
    lo,hi=found[pair]; assert abs(lo)<2e-12 and abs(hi-q)<2e-12
for pair in ((3,13),(13,3)):
    lo,hi=found[pair]; assert abs(lo-q)<2e-12 and abs(hi-(1-q))<2e-12
for pair in ((3,14),(14,3)):
    lo,hi=found[pair]; assert abs(lo-(1-q))<2e-12 and abs(hi-1)<2e-12

normals=[(math.cos((2*j+1)*math.pi/16),math.sin((2*j+1)*math.pi/16)) for j in range(8)]
den=math.cos(math.pi/16)
def norm(p): return max(abs(nx*p[0]+ny*p[1])/den for nx,ny in normals)
def point_edge(j,u):
    return (V[j][0]+u*(V[(j+1)%N][0]-V[j][0]),V[j][1]+u*(V[(j+1)%N][1]-V[j][1]))
def add(p,r): return (p[0]+r[0],p[1]+r[1])

def solve_yz(j,k,A):
    c=st_affine(j,k); s0,sa,t0,ta=c
    return point_edge(j,s0+sa*A),point_edge(k,t0+ta*A)

def X(A): return (V[0][0]+A*d0[0],V[0][1]+A*d0[1])
# Dense replay of the exact branch table; the proof of affine identities is in RESULT.md.
checks=0
for m in range(1001):
    A=q*m/1000
    y,z=solve_yz(2,13,A); xx=X(A)
    assert abs(norm(add(xx,y))-T)<2e-11
    assert abs(norm(add(xx,z))-(T-k1*A))<2e-11; checks+=1
for m in range(1001):
    A=q+(1-2*q)*m/1000
    y,z=solve_yz(3,13,A); xx=X(A)
    assert abs(norm(add(xx,y))-(T-k2*(A-q)))<2e-11
    assert abs(norm(add(xx,z))-(T-k2*(1-q-A)))<2e-11; checks+=1
for m in range(1001):
    A=1-q+q*m/1000
    y,z=solve_yz(3,14,A); xx=X(A)
    assert abs(norm(add(xx,y))-(T-k1*(1-A)))<2e-11
    assert abs(norm(add(xx,z))-T)<2e-11; checks+=1
# Equality witness.
h=(math.cos(math.pi/16)-0.5*math.sin(3*math.pi/16))/math.cos(3*math.pi/16)
x=(1.0,0.0); y=(0.5,h); z=(0.5,-h)
assert abs(norm(x)-1)<2e-14 and abs(norm(y)-1)<2e-14 and abs(norm(z)-1)<2e-14
assert abs(norm(add(x,y))-T)<2e-13 and abs(norm(add(x,z))-T)<2e-13
print(f"VERIFY_OK branches={len(found)} branch_checks={checks} q={q:.15f} T16={T:.15f} equality=simultaneous")
