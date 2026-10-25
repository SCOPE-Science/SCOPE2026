#!/usr/bin/env python3
"""Independent numerical incidence checks for rotated regular-polygon prismatoids.
No external packages. Finite checks are not a substitute for the general proof.
"""
import math

TAU=2*math.pi

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def rot(t):return (math.cos(t),math.sin(t))
def unit(n,angle,z):return (math.cos(angle),math.sin(angle),z)

def check(n,ratio,h):
    theta=TAU/n; t=ratio*theta
    delta=math.cos(t-theta/2)-math.cos(theta/2)
    assert delta>0
    c=delta/(2*h)
    verts=[unit(n,j*theta,h) for j in range(n)]+[unit(n,j*theta+t,-h) for j in range(n)]
    planes=[]
    for j in range(n):
        a=(j+.5)*theta
        # Formula in n.x <=b orientation. Validate explicit vertices.
        plus=(math.cos(a),math.sin(a),c)
        minus=(math.cos(a+t),math.sin(a+t),-c)
        topb=math.cos(theta/2)+c*h
        bottomb=math.cos(theta/2)+c*h
        planes.append((plus,topb,{j,(j+1)%n,n+j}))
        planes.append((minus,bottomb,{n+j,n+(j+1)%n,(j+1)%n}))
    # The two horizontal polygonal facets.
    planes.append(((0,0,1),h,set(range(n))))
    planes.append(((0,0,-1),h,set(range(n,2*n))))
    for normal,b,face in planes:
        actual={i for i,p in enumerate(verts) if abs(dot(normal,p)-b)<2e-9}
        assert actual==face, (n,ratio,h,face,actual)
        assert max(dot(normal,p)-b for p in verts)<2e-9
    incident=[[] for _ in range(2*n)]
    for normal,b,face in planes:
        for j in face: incident[j].append(normal)
    m=n//2
    # The independent constructive geometry is tested against *all* active facets.
    def top_dir(a):
        mid=(a+(m-2)/2)*theta+t
        L=(m-1)*theta/2
        C=math.cos(L)
        U=max(0.,-math.cos(L+t),-math.cos(L+theta-t))
        assert C>U+1e-10,(n,ratio,C,U)
        w=(C+U)/2
        return(-math.cos(mid),-math.sin(mid),-w/c)
    def lit(v):
        return {k for k,normals in enumerate(incident) if all(dot(v,normal)<-5e-10 for normal in normals)}
    # A lower-layer direction exists by rotating reflected upper-layer geometry.
    # z-reflection maps bottom angles (j*theta+t) to top angles j*theta after R_{-t};
    # then former top is rotated by -t = theta-t, with index shift -1.
    def lower_dir(a):
        # transformed top labels k correspond to original lower labels k,
        # transformed bottom j has angles j*theta-t ≡ (j-1)*theta+(theta-t).
        sp=theta-t
        mid=(a+(m-2)/2)*theta+sp
        L=(m-1)*theta/2
        C=math.cos(L)
        U=max(0.,-math.cos(L+sp),-math.cos(L+theta-sp))
        w=(C+U)/2
        new=(-math.cos(mid),-math.sin(mid),-w/(delta/(2*h)))
        # inverse transform: rotate x,y by +t, flip z; then original lower label k
        return (new[0]*math.cos(t)-new[1]*math.sin(t),new[0]*math.sin(t)+new[1]*math.cos(t),-new[2])
    top_blocks=[];bot_blocks=[]
    for a in range(n):
        T=lit(top_dir(a));B=lit(lower_dir(a));
        assert T=={(a+j)%n for j in range(m)},(n,ratio,a,'top',T)
        assert B=={n+(a+j)%n for j in range(m)},(n,ratio,a,'bottom',B)
        top_blocks.append(T);bot_blocks.append(B)
    # n cyclic blocks per layer: each vertex appears in exactly m blocks.
    for i in range(2*n):
        assert sum(i in s for s in top_blocks+bot_blocks)==m
    # An ordinary family with 2*ceil(n/m) directions obtained from blocks.
    idx=list(range(0,n,m))
    cover=set()
    for a in idx:cover|=top_blocks[a]|bot_blocks[a]
    assert cover==set(range(2*n))
    # Odd-case opposite chord identity: antiparallel planar vectors.
    if n%2:
        k=(n-1)//2
        x=tuple(sum(rot(-theta/2+t*i)[q] for i in (0,1)) for q in (0,1))
        z=tuple(sum(rot((k+(.5 if i else -.5))*theta + (0 if i else t))[q] for i in (0,1)) for q in (0,1))
        assert abs(x[0]*z[1]-x[1]*z[0])<1e-8
        assert dot(x,z)<-1e-8
    return len(planes),2*n, len(idx)*2

if __name__=='__main__':
    cases=facets=vertices=directions=0
    for n in range(3,33):
        for ratio in (.03,.5,.97):
            for h in (.5,3.):
                f,v,d=check(n,ratio,h)
                cases+=1;facets+=f;vertices+=v;directions+=d
    print('VERIFY_OK cases=%d checked_planes=%d vertices=%d ordinary_directions=%d' %(cases,facets,vertices,directions))
