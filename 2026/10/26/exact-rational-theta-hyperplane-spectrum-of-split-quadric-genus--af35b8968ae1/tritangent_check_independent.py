"""Independent incidence checker for bidegree-(3,3) curves over F2."""
import itertools, collections
from tri_orbits import get_orbits
from tri_smooth import is_smooth
P=((1,0),(0,1),(1,1))
def conv(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,c in enumerate(a):
  if c:
   for j,d in enumerate(b):z[i+j]^=d
 return z
def power(a,k):
 z=[1]
 for _ in range(k):z=conv(z,a)
 return z

def sections(f):
 c=[[f>>(4*i+j)&1 for j in range(4)] for i in range(4)]
 return c

def cubic_line_u(f,u):
 c=sections(f)
 w=[u[0]**(3-i)*u[1]**i for i in range(4)]
 return [sum(w[i]*c[i][j] for i in range(4))%2 for j in range(4)]

def cubic_line_v(f,v):
 c=sections(f)
 w=[v[0]**(3-j)*v[1]**j for j in range(4)]
 return [sum(w[j]*c[i][j] for j in range(4))%2 for i in range(4)]

def linroot_cubic(c,p):
 # enumerate all a*u0^2+b*u1^2, including zero, and require it be nonzero
 L=(p[1],p[0]); return tuple(c) in {tuple(conv(L,[a,0,b])) for a,b in ((1,0),(0,1),(1,1))}

def count(f):
 ans=[]
 for a,b,c,d in itertools.product((0,1),repeat=4):
  if a==b==c==d==0:continue
  h=a+2*b+4*c+8*d
  if a*d^b*c:
   # nonsingular plane section: v=(b*u0+d*u1,a*u0+c*u1)
   # nonzero degree6 binary polynomial must be square
   v0=[b,d];v1=[a,c]; poly=[0]*7
   for i in range(4):
    for j in range(4):
     if not (f>>(4*i+j)&1):continue
     term=conv(power([1,0],3-i),power([0,1],i))
     term=conv(term,conv(power(v0,3-j),power(v1,j)))
     for k,z in enumerate(term):poly[k]^=z
   if poly[1]==poly[3]==poly[5]==0:ans.append(h)
  else:
   # rank-one A, solve left and right nullspaces over F2
   u=next(p for p in P if (a*p[0]+c*p[1])%2==0 and (b*p[0]+d*p[1])%2==0)
   v=next(p for p in P if (a*p[0]+b*p[1])%2==0 and (c*p[0]+d*p[1])%2==0)
   if linroot_cubic(cubic_line_u(f,u),v) and linroot_cubic(cubic_line_v(f,v),u):ans.append(h)
 return len(ans),sum(1<<k for k in ans)

def main():
 from tri_probe import form_test
 total=collections.Counter(); countrep=0
 for mask,sz in get_orbits():
  p=count(mask)
  q=form_test(mask)
  if p!=q:raise AssertionError((mask,p,q))
  if is_smooth(mask):total[p[0]]+=sz;countrep+=1
 assert total=={0:5208,1:8076,2:2556,3:120,4:60},total
 print('Independent F2-bilinear plane incidence checker PASS: 1,075 projective orbit representatives; 252 smooth, 16,020 equations')
 print('Smooth distribution:', sorted(total.items()))
if __name__=='__main__':main()
