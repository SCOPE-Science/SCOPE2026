from pathlib import Path
bad=Path('data/smooth_bitset.bin').read_bytes()
w=Path('data/witness.bin').read_bytes()
assert len(bad)==65536 and len(w)==3*65536
IRR=(0,3,7,11,19,37,67)
def mult(a,b,d):
 z=0;top=1<<d;p=IRR[d]
 while b:
  if b&1:z^=a
  b//=2;a*=2
  if a&top:a^=p
 return z

def check(m,d,u,v):
 q=1<<d;ax=(u==q);ay=(v==q)
 X=[1,0,0,0] if ax else [1,u,0,0]
 Y=[1,0,0,0] if ay else [1,v,0,0]
 for i in (2,3):
  if not ax:X[i]=mult(X[i-1],u,d)
  if not ay:Y[i]=mult(Y[i-1],v,d)
 F=FX=FY=0
 for j in range(4):
  for i in range(4):
   if not((m>>(4*j+i))&1):continue
   a=(3-i) if ax else i;b=(3-j) if ay else j
   F^=mult(X[a],Y[b],d)
   if a&1:FX^=mult(X[a-1],Y[b],d)
   if b&1:FY^=mult(X[a],Y[b-1],d)
 return F==FX==FY==0
n=0
for m in range(1,65536):
 d,u,v=w[3*m:3*m+3]
 if bad[m]:
  assert 1<=d<=6 and check(m,d,u,v),(m,d,u,v)
  n+=1
 else:assert d==u==v==0
assert n==49515
print('independent witness checks:',n,'singular forms confirmed; smooth candidates',65535-n)
