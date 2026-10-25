"""Independent numerical face/edge/vertex equilibrium checker for right regular bipyramids.

Every tested equilibrium is reconstructed from vertex coordinates and adjacent-face
normals; no preclassified equilibrium orbit is used in the counting algorithm.
"""
import math

def plus(x,y):return tuple(a+b for a,b in zip(x,y))
def minus(x,y):return tuple(a-b for a,b in zip(x,y))
def scale(x,c):return tuple(a*c for a in x)
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def cross(x,y):return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def barycentric(point,v0,v1,v2):
    u=minus(v1,v0);v=minus(v2,v0);w=minus(point,v0)
    uu=dot(u,u);vv=dot(v,v);uv=dot(u,v);uw=dot(u,w);vw=dot(v,w)
    d=uu*vv-uv*uv
    t=(uw*vv-vw*uv)/d;s=(vw*uu-uw*uv)/d
    return 1-t-s,t,s

def make_geometry(n,a,b,r=1.0):
    vertices=[(r*math.cos(2*math.pi*k/n),r*math.sin(2*math.pi*k/n),0.0) for k in range(n)]
    vertices.extend([(0.,0.,a),(0.,0.,-b)])
    t=n; bot=n+1
    faces=[(k,(k+1)%n,t) for k in range(n)]+[((k+1)%n,k,bot) for k in range(n)]
    edges=sorted({tuple(sorted((face[i],face[(i+1)%3]))) for face in faces for i in range(3)})
    centroid=(0.,0.,(a*a-b*b)/(4*(a+b)))
    normals=[]
    for face in faces:
        v0,v1,v2=(vertices[j] for j in face)
        normal=cross(minus(v1,v0),minus(v2,v0))
        normal=scale(normal,1/math.sqrt(dot(normal,normal)))
        if dot(normal,minus(centroid,v0))>0:normal=scale(normal,-1)
        normals.append(normal)
    return vertices,faces,edges,centroid,normals

def brute_counts(n,tau):
    r,b=1.,1.
    a=1+4*tau
    vs,faces,edges,centroid,normals=make_geometry(n,a,b,r)
    eps=1e-8
    stable=[];saddles=[];unstable=[]
    for k, face in enumerate(faces):
        v=vs[face[0]];nor=normals[k]
        foot=plus(centroid,scale(nor,dot(nor,minus(v,centroid))))
        if min(barycentric(foot,*(vs[j] for j in face)))>eps:stable.append(k)
    for edge in edges:
        v,w=(vs[i] for i in edge);d=minus(w,v)
        t=dot(minus(centroid,v),d)/dot(d,d)
        if not eps<t<1-eps:continue
        foot=plus(v,scale(d,t)); radial=minus(foot,centroid)
        adjacent=[k for k,face in enumerate(faces) if all(j in face for j in edge)]
        assert len(adjacent)==2
        u,v=normals[adjacent[0]],normals[adjacent[1]]
        uv=dot(u,v);s1=dot(radial,u);s2=dot(radial,v)
        alpha=(s1-s2*uv)/(1-uv*uv)
        beta=(s2-s1*uv)/(1-uv*uv)
        if alpha>eps and beta>eps:saddles.append(edge)
    for k,v in enumerate(vs):
        neighbors={b if a==k else a for a,b in edges if k in (a,b)}
        radial=minus(v,centroid)
        if all(dot(radial,minus(vs[j],v))< -eps for j in neighbors):unstable.append(k)
    return (len(stable),len(saddles),len(unstable)),(stable,saddles,unstable)

def expected(n,tau):
    c2=math.cos(math.pi/n)**2
    if tau<c2:return (2*n,3*n,n+2)
    if tau<1:return (n,2*n,n+2)
    return (n,n,2)

def main():
    case_count=0
    for n in (3,4,5,6,8,11,20):
        c2=math.cos(math.pi/n)**2
        for t in (0,.13,c2*.75,(c2+1)/2,(c2+1)/2+.01,1.15,1.8,3.5):
            got,_=brute_counts(n,t)
            target=expected(n,t)
            assert got==target,(n,t,got,target)
            assert got[0]-got[1]+got[2]==2
            case_count+=1
        assert c2<1
    print(f'PASS {case_count} independently reconstructed face/edge/vertex cases; all Euler identities hold.')
    for n in (3,4,7):
        c2=math.cos(math.pi/n)**2
        print('n',n,'critical tau',round(c2,9),'samples',*[brute_counts(n,t)[0] for t in (c2/2,(c2+1)/2,1.2)])

if __name__=='__main__': main()
