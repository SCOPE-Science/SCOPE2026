import math

def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(c,a): return (c*a[0],c*a[1])
def norm(a): return math.sqrt(dot(a,a))

def intersections(vertices, center, r):
    pts=[]; n=len(vertices)
    for j in range(n):
        A=sub(vertices[j],center); e=sub(vertices[(j+1)%n],vertices[j])
        aa=dot(e,e); bb=2*dot(A,e); cc=dot(A,A)-r*r
        disc=bb*bb-4*aa*cc
        if disc < -1e-10: continue
        disc=max(0.0,disc)
        for s in ((-bb-math.sqrt(disc))/(2*aa),(-bb+math.sqrt(disc))/(2*aa)):
            if -1e-9 <= s <= 1+1e-9:
                p=add(vertices[j],mul(s,e))
                if all(norm(sub(p,q))>1e-7 for q in pts): pts.append(p)
    return len(pts)

for n in range(3,32,2):
    k=(n-1)//2; alpha=2*math.pi/n
    V=[(math.cos(j*alpha),math.sin(j*alpha)) for j in range(n)]; v0=V[0]
    for j in range(k):
        e=sub(V[j+1],V[j]); deriv0=2*dot(sub(V[j],v0),e)
        if j==0: assert abs(deriv0)<1e-10
        else: assert deriv0>0
    e=sub(V[k+1],V[k]); M=mul(0.5,add(V[k],V[k+1]))
    assert 2*dot(sub(V[k],v0),e)<0
    assert abs(2*dot(sub(M,v0),e))<1e-10
    dM=norm(sub(M,v0)); dK=norm(sub(V[k],v0)); assert dM<dK
    for t in (0.2,0.5,0.8): assert intersections(V,v0,dM+t*(dK-dM))==4
print('sanity checks passed')
