from fractions import Fraction as F
from itertools import product, combinations

D=F(1,13)
a=F(1,4)
centers=[
(F(1),-a,-a),(-F(1),a,a),
(a,F(1),-a),(-a,-F(1),a),
(a,a,F(1)),(-a,-a,-F(1))]

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def interior_K(x):
    return max(abs(t) for t in x)<1 and sum(abs(t) for t in x)<2

def boundary_K(x):
    return max(abs(t) for t in x)<=1 and sum(abs(t) for t in x)<=2 and (max(abs(t) for t in x)==1 or sum(abs(t) for t in x)==2)

# Every half-scaled center touches K; pairwise blockers do not overlap.
assert all(boundary_K(z) for z in centers)
for p,q in combinations(centers,2):
    d=tuple(x-y for x,y in zip(p,q))
    assert not interior_K(d)

# Closed inset K_D: all facet slacks at least D.  Showing boundary(K) is
# covered by z_i+K_D gives strict coverage by z_i+int(K).
ineq=[]
for j in range(3):
    v=[F(0)]*3; v[j]=F(1); ineq.append((tuple(v),F(1)-D))
    v=[F(0)]*3; v[j]=F(-1); ineq.append((tuple(v),F(1)-D))
for s in product([-1,1],repeat=3):
    ineq.append((tuple(F(t) for t in s),F(2)-D))
assert len(ineq)==14

def clip(poly,hp):
    A,B,C=hp
    if not poly: return []
    def val(P): return A*P[0]+B*P[1]-C
    out=[]
    for P,Q in zip(poly,poly[1:]+poly[:1]):
        vp,vq=val(P),val(Q)
        ip,iq=vp<=0,vq<=0
        if ip: out.append(P)
        if ip != iq:
            t=vp/(vp-vq)
            R=(P[0]+t*(Q[0]-P[0]), P[1]+t*(Q[1]-P[1]))
            out.append(R)
    res=[]
    for P in out:
        if not res or P!=res[-1]: res.append(P)
    if len(res)>1 and res[0]==res[-1]: res.pop()
    return res

def failure_halfplanes(z,c,e1,e2):
    # Failure of z+K_D means at least one K_D defining inequality is violated:
    # l.(y-z) >= rhs.  In facet parameters y=c+u e1+v e2 this is a halfplane.
    ans=[]
    for l,rhs in ineq:
        A=-dot(l,e1); B=-dot(l,e2)
        C=-rhs-dot(l,z)+dot(l,c)
        ans.append((A,B,C))
    return ans

def recurse(poly,idx,c,e1,e2,counter):
    if not poly: return False
    if idx==len(centers): return True
    for hp in failure_halfplanes(centers[idx],c,e1,e2):
        q=clip(poly,hp)
        if q:
            counter[idx]+=1
            if recurse(q,idx+1,c,e1,e2,counter): return True
    return False

def facets():
    out=[]
    # Six square facets: coordinate fixed at +/-1, other pair in |u|+|v|<=1.
    for axis in range(3):
        jj=[j for j in range(3) if j!=axis]
        for sg in (-1,1):
            c=[F(0)]*3; c[axis]=F(sg)
            e1=[F(0)]*3; e1[jj[0]]=F(1)
            e2=[F(0)]*3; e2[jj[1]]=F(1)
            P=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))]
            out.append((f'square_{axis}_{sg}',tuple(c),tuple(e1),tuple(e2),P))
    # Eight triangular facets: y_i=s_i p_i, p_i in [0,1], sum p_i=2.
    for s in product((-1,1),repeat=3):
        c=(F(0),F(0),F(2*s[2]))
        e1=(F(s[0]),F(0),F(-s[2]))
        e2=(F(0),F(s[1]),F(-s[2]))
        P=[(F(1),F(1)),(F(1),F(0)),(F(0),F(1))]
        out.append(('triangle_'+''.join('+' if t>0 else '-' for t in s),c,e1,e2,P))
    return out

reports=[]
for name,c,e1,e2,P in facets():
    count=[0]*6
    assert not recurse(P,0,c,e1,e2,count), name
    reports.append((name,tuple(count)))

print('VERIFY_OK')
print('centers', centers)
print('clearance_delta', D)
print('facets_checked', len(reports))
for name,count in reports: print(name, count)
