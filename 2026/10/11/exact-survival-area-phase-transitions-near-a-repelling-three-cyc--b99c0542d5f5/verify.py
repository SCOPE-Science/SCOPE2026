"""Exact rational certificate for polyhedral 422-itinerary survival laws."""
from fractions import Fraction as Q

def point(x,y):return (Q(x),Q(y))
def mat(A,v):return tuple(sum(A[i][j]*v[j] for j in range(2)) for i in range(2))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def sub(u,v):return (u[0]-v[0],u[1]-v[1])
def poly_area(V):return sum(cross(V[i],V[(i+1)%len(V)]) for i in range(len(V)))/2
M=((Q(2),Q(2)),(Q(-2),Q(2)))
N=((Q(1,4),Q(-1,4)),(Q(1,4),Q(1,4)))
I=((Q(1),Q(0)),(Q(0),Q(1)))
assert mm(M,N)==I
A=I
for i in range(8):A=mm(N,A)
assert A==((Q(1,4096),Q(0)),(Q(0),Q(1,4096)))

def coords(b):return (Q(2)-b)/5, (2*b+1)/5, (4*b-3)/10

def D(b):
 c,d,e=coords(b)
 if b>=1:return [(-c,-2*c),(c+e,e),(-c,e)]
 return [(-c,c-d),((c-d)/2,-d-(c-d)/2),(c+e,e),(-c,e)]

def P2(b):
 c,d,e=coords(b)
 return [(c/4,-3*c/4),(c/4,c/4+e/2),(-c,-c+e/2),(-c,c/2)]

P3constant=[point(Q(1,20),Q(-1,40)),point(Q(-1,5),Q(9,40)),point(Q(-1,5),Q(1,10)),point(Q(-3,40),Q(-1,40))]
def P3(b):return [tuple((2-b)*x for x in p) for p in P3constant]

def halfspaces(b,n):
 c,d,e=coords(b)
 base=[((Q(1),Q(0)),c),((Q(0),Q(-1)),e),((Q(-1),Q(1)),c),((Q(1),Q(1)),d)]
 out=[];A=I
 for k in range(n):
  for (u,v),off in base:
   out.append(((u*A[0][0]+v*A[1][0],u*A[0][1]+v*A[1][1]),off))
  A=mm(A,M)
 return out

def ev(h,p):return sum(h[0][j]*p[j] for j in range(2))+h[1]

def check_interval(lo,hi,n,fn):
    # All constraints and vertex coordinates are affine in b and normals fixed.
    P0,P1=fn(lo),fn(hi)
    H0,H1=halfspaces(lo,n),halfspaces(hi,n)
    assert len(P0)==len(P1) and len(H0)==len(H1)
    assert poly_area(P0)>0
    for P,H in ((P0,H0),(P1,H1)):
        for p in P:
            for h in H: assert ev(h,p)>=0,('feasibility',lo,hi,n,p,h)
            for h in H: assert ev(h,mat(N,p))>=0,('invariance',lo,hi,n,p,h)
    # Each moving polygon edge is on the same fixed supporting halfplane
    # at both endpoints. Degenerate endpoint edges cause no obstacle.
    for i in range(len(P0)):
        j=(i+1)%len(P0)
        assert any(ev(H0[k],P0[i])==ev(H0[k],P0[j])==0 and
                   ev(H1[k],P1[i])==ev(H1[k],P1[j])==0
                   for k in range(len(H0))),(lo,hi,'unsupported',i)
    # Signed areas are positive within each open parameter interval.
    # The first two families have fixed edge directions and the third
    # is a positive homothety of a fixed quadrilateral.
    print('INTERVAL_OK',lo,hi,n,'area0',poly_area(P0),'area1',poly_area(P1))

for x,y,n,fn in [(Q(1),Q(3,2),1,D),(Q(3,2),Q(7,4),2,P2),(Q(7,4),Q(2),3,P3)]:
    check_interval(x,y,n,fn)

for b in (Q(1),Q(5,4),Q(3,2)):
 assert poly_area(D(b))==Q(1,8)
for b in (Q(3,2),Q(8,5),Q(7,4)):
 assert poly_area(P2(b))==(b-1)*(2-b)/16
for b in (Q(7,4),Q(9,5),Q(199,100)):
 assert poly_area(P3(b))==Q(3,128)*(2-b)**2

# The full b range is covered by D(b) with positive interior. Its eight-step
# periodicity follows from N^8=1/4096 I and convexity about the origin.
for b in (Q(751,1000),Q(4,5),Q(99,100),Q(1),Q(11,10),Q(7,4),Q(199,100)):
 assert poly_area(D(b))>0
 for p in D(b):
  assert all(ev(h,(Q(0),Q(0)))>=0 for h in halfspaces(b,1))
print('EXACT_AFFINE_FACET_CERTIFICATE_OK')
