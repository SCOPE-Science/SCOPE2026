import itertools, collections
pts=[(a,b) for a in range(4) for b in range(4)]; idx={p:i for i,p in enumerate(pts)}; N=16
sub=[[idx[((pts[i][0]-pts[j][0])%4,(pts[i][1]-pts[j][1])%4)] for j in range(N)] for i in range(N)]
phase=[[ (pts[x][0]*pts[b][0]+pts[x][1]*pts[b][1])%4 for x in range(N)] for b in range(N)]
vals=[(1,0),(0,1),(-1,0),(0,-1)]
def bits(m):
    while m:
        l=m&-m; yield l.bit_length()-1; m-=l
def zmask(A):
    xs=list(bits(A)); z=0
    for b in range(N):
        re=im=0
        for x in xs:
            r,i=vals[phase[b][x]]; re+=r; im+=i
        if re==im==0:z|=1<<b
    return z
def dmask(A):
    xs=list(bits(A)); d=0
    for x in xs:
      for y in xs:d|=1<<sub[x][y]
    return d
comb0={}
for k in (1,2,4,8,16):
  arr=[]
  for c in itertools.combinations(range(1,16),k-1):
    m=1
    for i in c:m|=1<<i
    arr.append(m)
  comb0[k]=arr
def spectral(A,zc={}):
  k=A.bit_count()
  if k not in comb0:return False
  z=zmask(A); key=(z,k)
  if key in zc:return zc[key]
  for B in comb0[k]:
    xs=list(bits(B)); ok=True
    for x in xs:
      for y in xs:
        if x!=y and not (z>>sub[x][y])&1:ok=False;break
      if not ok:break
    if ok:zc[key]=True;return True
  zc[key]=False;return False
def tile(A,tc={}):
  k=A.bit_count()
  if 16%k:return False
  d=dmask(A); kt=16//k; key=(d,kt)
  if key in tc:return tc[key]
  for T in comb0[kt]:
    if dmask(T)&d==1:tc[key]=True;return True
  tc[key]=False;return False
counts=collections.Counter(); good={k:set() for k in (1,2,4,8,16)}
for A in range(1,1<<16):
  s=spectral(A); t=tile(A)
  assert s==t
  if s: counts[A.bit_count()]+=1;good[A.bit_count()].add(A)
assert dict(counts)=={1:16,2:120,4:1244,8:774,16:1}
# affine orbit classification
mats=[]
for a,b,c,d in itertools.product(range(4),repeat=4):
  if ((a*d-b*c)%4)%2:mats.append((a,b,c,d))
assert len(mats)==96
perms=[]
for a,b,c,d in mats:
  for t0,t1 in pts:
    perms.append([idx[((a*x+b*y+t0)%4,(c*x+d*y+t1)%4)] for x,y in pts])
def tr(A,p):
  out=0
  for i in bits(A):out|=1<<p[i]
  return out
orbit_counts={}
for k,S in good.items():
  rem=set(S); n=0
  while rem:
    A=min(rem); orb={tr(A,p) for p in perms}; inter=orb&S
    assert inter and orb<=S
    rem-=inter;n+=1
  orbit_counts[k]=n
assert orbit_counts=={1:1,2:2,4:8,8:7,16:1}
print('VERIFY_OK total=2155 size_counts=16,120,1244,774,1 affine_orbits=1,2,8,7,1 GL2Z4=96')
