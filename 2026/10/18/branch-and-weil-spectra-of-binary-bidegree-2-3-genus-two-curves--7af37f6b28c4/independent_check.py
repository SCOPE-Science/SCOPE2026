"""Independent exact coefficient-ring check of genus-two bidegree-(2,3) smoothness over F2.
No finite-extension search or imported smoothness routine is used in this check.
"""
import json

def mul(a,b):
 out=0
 while b:
  if b&1:out^=a
  a<<=1;b>>=1
 return out

def deriv(a):
 return sum(1<<(j-1) for j in range(1,a.bit_length(),2) if a>>j&1)

def mod(a,b):
 n=b.bit_length()-1
 while a and a.bit_length()-1>=n:
  a^=b<<(a.bit_length()-1-n)
 return a

def gcd(a,b):
 while b:a,b=b,mod(a,b)
 return a

def rev4(c):return sum(((c>>j)&1)<<(3-j) for j in range(4))

def Q(a,b,c):
 t=mul(deriv(a),c)^mul(a,deriv(c))
 return mul(t,t)^mul(mul(deriv(b),deriv(b)),mul(a,c))

def smooth_rational_polynomial(m):
 A=m&15;B=m>>4&15;C=m>>8&15
 if not B:return False
 for a,b,c in ((rev4(A),rev4(B),rev4(C)),(A,B,C)):
  if gcd(b,Q(a,b,c))!=1:return False
 return True

def independent_orbit_count(sm):
 # Burnside on coefficient group action; implement substitution independently via evaluation.
 # For each (gx,gy), projectively there are 6x6 transformations over F2.
 G=[(1,0,0,1),(0,1,1,0),(1,1,0,1),(1,0,1,1),(0,1,1,1),(1,1,1,0)]
 assert len(G)==6
 def polypower(a,b,n):
  d=[1]
  for _ in range(n):
   e=[0]*(len(d)+1)
   for k,x in enumerate(d):
    e[k]^=a*x; e[k+1]^=b*x
   d=e
  return d
 def substitute(gx,gy):
  out=[]
  for i in range(3):
   x0=polypower(gx[0],gx[1],2-i);x1=polypower(gx[2],gx[3],i)
   X=[0]*3
   for k,u in enumerate(x0):
    for l,v in enumerate(x1):X[k+l]^=u*v
   for j in range(4):
    y0=polypower(gy[0],gy[1],3-j);y1=polypower(gy[2],gy[3],j)
    Y=[0]*4
    for k,u in enumerate(y0):
     for l,v in enumerate(y1):Y[k+l]^=u*v
    v=0
    for k in range(3):
     for l in range(4):v^=X[k]*Y[l]<<(4*k+l)
    out.append(v)
  return out
 actions=[substitute(gx,gy) for gx in G for gy in G]
 fixed=[]
 for cols in actions:
  n=0
  for m in sm:
   v=0
   for i in range(12):
    if (m>>i)&1:v^=cols[i]
   n+=v==m
  fixed.append(n)
 return sum(fixed)//36,fixed

if __name__=='__main__':
 sm={m for m in range(1,4096) if smooth_rational_polynomial(m)}
 from enumerate import smooth, Nn, enumerate_curves
 sm2={m for m in range(1,4096) if smooth(m)}
 print('independently smooth',len(sm),'matching',sm==sm2,'symmdiff',sm^sm2)
 assert sm==sm2
 orbit_n,fix=independent_orbit_count(sm)
 print('Burnside',orbit_n,'fixed-elements:',fix)
 assert orbit_n==39
 # Verify the third extension by Newton's identities from N1 and N2.
 # Newton relation checked directly against degree-three rational counts:
 data=json.load(open('census.json',encoding='utf-8'))
 assert data==enumerate_curves()
 assert sum(o['size'] for o in data['orbits'])==len(sm)
 for o in data['orbits']:
  a=o['a1'];b=o['a2']
  n3_from_zeta=9+a**3-3*a*b+6*a
  assert Nn(o['rep'],3)==n3_from_zeta
 print('third-extension Newton check verified on',len(data['orbits']),'orbits')


# Unrelated F4 model using z^2+z+1 for the second-extension counts.
def gf4_mul(a,b):
    z=0
    for i in range(2):
        if (b>>i)&1:z^=a<<i
    if z&8:z^=12
    if z&4:z^=7
    return z

def gf4_pow(a,n):
    z=1
    for _ in range(n):z=gf4_mul(z,a)
    return z

def gf4_N2(mask):
    pts=[(1,0)]+[(v,1) for v in range(4)]
    total=0
    for x0,x1 in pts:
        for y0,y1 in pts:
            value=0
            for i in range(3):
                for j in range(4):
                    if (mask>>(4*i+j))&1:
                        xx=gf4_mul(gf4_pow(x0,2-i),gf4_pow(x1,i))
                        yy=gf4_mul(gf4_pow(y0,3-j),gf4_pow(y1,j))
                        value^=gf4_mul(xx,yy)
            total+=(value==0)
    return total

if __name__=='__main__':
    import json
    from enumerate import enumerate_curves
    data=json.load(open('census.json',encoding='utf-8'))
    for row in data['orbits']:
        assert gf4_N2(row['rep'])==row['N2']
    print('Independent GF4 check passed on all orbit representatives')
