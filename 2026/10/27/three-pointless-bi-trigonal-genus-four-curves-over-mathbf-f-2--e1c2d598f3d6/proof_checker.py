from sympy import symbols,Poly,groebner
from collections import Counter
from itertools import product
X,Y=symbols('x y')
# S,T and U,V with monomial T^i S^(3-i) V^j U^(3-j)
BASIS=[(i,j) for i in range(4) for j in range(4)]
def ev2(i,point):
 if point==0: return int(i==3)
 elif point==1:return 1
 else: return int(i==0)
# points [1:0], [1:1], [0:1]
mask=[sum(((ev2(i,a)*ev2(j,b))<<k) for k,(i,j) in enumerate(BASIS)) for a in range(3) for b in range(3)]
pointless=[m for m in range(1<<16) if all((m&p).bit_count()%2 for p in mask)]
print('pointless',len(pointless), 'mask rank9', mask)

def charts(m,inf1,inf2):
 # affine coordinate x=T/S when not inf else x=S/T
 p=0
 for k,(i,j) in enumerate(BASIS):
  if m>>k&1:
   a=3-i if inf1 else i
   b=3-j if inf2 else j
   p+=X**a*Y**b
 return Poly(p,X,Y,modulus=2).as_expr()

def good(m):
 for a,b in product(range(2),repeat=2):
  P=charts(m,a,b)
  G=groebner([P,P.diff(X),P.diff(Y)],X,Y, modulus=2, order='lex')
  if not G.contains(__import__("sympy").Integer(1)):return False
 return True
smooth=[]
for i,m in enumerate(pointless):
 if good(m):smooth.append(m)
assert len(smooth)==84
print('smooth pointless',len(smooth),'masks',[hex(m) for m in smooth])
# Action of coordinate changes on each P^1 factor, plus factor interchange
s,t,u,v=symbols('s t u v'); BASE=[s**(3-i)*t**i*u**(3-j)*v**j for i,j in BASIS]
subs=[{s:s+t,t:t},{s:t,t:s},{u:u+v,v:v},{u:v,v:u},{s:u,t:v,u:s,v:t}]
trans=[]
for g in subs:
 rows=[]
 for b in BASE:
  p=Poly(b.subs(g,simultaneous=True).expand(),s,t,u,v,modulus=2)
  rows.append(sum((int(p.coeff_monomial(bb))%2)<<k for k,bb in enumerate(BASE)))
 trans.append(rows)
def act(m,rows):
 result=0
 for i in range(16):
  if m>>i&1:result^=rows[i]
 return result
remaining=set(smooth);orbits=[]
while remaining:
 a=min(remaining);orbit={a};Q=[a]
 while Q:
  b=Q.pop()
  for tr in trans:
   c=act(b,tr)
   assert c in smooth
   if c not in orbit:
    Q.append(c);orbit.add(c)
 remaining-=orbit
 orbits.append((a,len(orbit),72//len(orbit)))
assert [(hex(a),b,c) for a,b,c in orbits] == [('0xb0bd',24,3),('0xb0db',24,3),('0xb1cb',36,2)]
print('orbits',len(orbits),[ (hex(a),b,c) for a,b,c in orbits ])
mods={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}
def gf_mul(a,b,d):
 mod=mods[d];r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
  if a&(1<<d):a^=mod
 return r

def count_points(mask,d):
 q=1<<d
 P=[(1,a) for a in range(q)]+[(0,1)]
 power=[ [1]*4 for a in range(q)]
 for a in range(q):
  for k in range(1,4):power[a][k]=gf_mul(power[a][k-1],a,d)
 n=0
 for s,t in P:
  for u,v in P:
   val=0
   for k,(i,j) in enumerate(BASIS):
    if mask>>k&1:
     h=gf_mul(power[s][3-i],power[t][i],d)
     h=gf_mul(h,gf_mul(power[u][3-j],power[v][j],d),d)
     val ^=h
   n+=val==0
 return n
for a,b,c in orbits:
 print('zeta',hex(a), b,tuple(count_points(a,d) for d in range(1,5)))

assert [(hex(a),tuple(count_points(a,d) for d in range(1,5))) for a,b,c in orbits] == [('0xb0bd',(0,2,18,18)),('0xb0db',(0,0,18,12)),('0xb1cb',(0,2,21,26))]
