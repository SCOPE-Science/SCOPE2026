"""Independent numerical regression for the analytic antiprism illumination theorem.
The infinite-parameter proof is in RESULT.md; these finite checks are not a proof.
"""
from math import pi, sin, cos


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def normals(n,h,layer,j):
    theta=2*pi/n
    c=cos(theta/2)
    q=sin(theta/2)
    k=(1-c)/(2*h)
    angle=theta*(j+(0.5 if layer==1 else 0))
    r=(cos(angle),sin(angle))
    t=(-sin(angle),cos(angle))
    sg=1 if layer==0 else -1
    return [(0.,0.,float(sg)),(r[0],r[1],-sg*k),
            (c*r[0]+q*t[0],c*r[1]+q*t[1],sg*k),
            (c*r[0]-q*t[0],c*r[1]-q*t[1],sg*k)]


def illuminates(n,h,u,layer,j):
    return all(dot(z,u)<-1.e-10 for z in normals(n,h,layer,j))


def direction(n,h,layer,start,length):
    th=2*pi/n
    c,q=cos(th/2),sin(th/2)
    k=(1-c)/(2*h)
    alpha=(length-1)*th/2
    lo=max(0.,-c*cos(alpha)+q*sin(alpha))
    hi=cos(alpha)
    assert lo<hi-1.e-9, (n,start,length,lo,hi)
    delta=(hi+lo)/2
    az=th*(start+(length-1)/2 + (0.5 if layer==1 else 0))
    return (-cos(az),-sin(az),(-1 if layer==0 else 1)*delta/k)


def run():
    checks=0
    for n in range(3,81):
        m=n//2
        assert 2*((n+m-1)//m)==(4 if n%2==0 else 6)
        for h in (0.1,1.0,3.0):
            # Independent support check at all 2n vertices for all 4n alleged
            # incident facet normals, including equality incidence sizes.
            vertices=[(cos(2*pi*(j+(.5 if layer else 0))/n),
                       sin(2*pi*(j+(.5 if layer else 0))/n),
                       h*(1 if layer==0 else -1))
                      for layer in (0,1) for j in range(n)]
            for layer in (0,1):
                for j in range(n):
                    for t,z in enumerate(normals(n,h,layer,j)):
                        support=dot(z,vertices[layer*n+j]);
                        assert all(dot(z,v)<=support+1.e-9 for v in vertices)
                        eq=sum(abs(dot(z,v)-support)<1.e-9 for v in vertices)
                        assert eq==(n if t==0 else 3), (n,h,layer,j,t,eq)
                        checks+=1
            masks=[]
            for layer in (0,1):
                for start in range(n):
                    u=direction(n,h,layer,start,m)
                    lit=[j for j in range(n) if illuminates(n,h,u,layer,j)]
                    assert len(lit)==m, (n,h,layer,start,lit)
                    assert set(lit)=={(start+t)%n for t in range(m)}
                    assert not any(illuminates(n,h,u,1-layer,j) for j in range(n))
                    checks+=1
                # explicit ordinary cover by contiguous blocks
                for start in range(0,n,m):
                    width=min(m,n-start)
                    u=direction(n,h,layer,start,width)
                    for j in range(start,start+width):
                        assert illuminates(n,h,u,layer,j), (n,h,layer,start,j)
                    checks+=1
                # each vertex belongs to exactly m cyclic full blocks
                assert all(sum(1 for start in range(n) if (j-start)%n<m)==m for j in range(n))
            # sample unrelated directions for general cap and opposite-layer exclusion
            for a in range(48):
                for z in (-6.,-.6,.6,6.):
                    az=(a+0.1234)*2*pi/48
                    u=(cos(az),sin(az),z)
                    counts=[sum(illuminates(n,h,u,layer,j) for j in range(n)) for layer in (0,1)]
                    assert min(counts)==0 and max(counts)<=m, (n,h,a,z,counts)
                    checks+=1
    print('VERIFY_OK antiprism n=3..80, h=0.1,1,3; regression_checks=',checks)

if __name__=='__main__':
    run()
