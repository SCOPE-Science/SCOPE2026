"""Independent full point counts through degree 6 and mod-2 zeta ranks.
Uses only the Python standard library; execute: python check_points.py
"""
REPS=[213034,213150,213334,213658,213756,215182,215210,215310,215482,221388]
MOD={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}
mons=[(a,b,5-a-b) for a in range(5,-1,-1) for b in range(5-a,-1,-1)]
def mul(a,b,poly,n):
 r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
  if a>>n:a^=poly
 return r

def build(q,n):
 poly=MOD[n];m=lambda a,b:mul(a,b,poly,n)
 pw=[[1]*6 for _ in range(q)]
 for a in range(q):
  for k in range(1,6):pw[a][k]=m(pw[a][k-1],a)
 return m,pw

def count(mask,n):
 q=1<<n;m,pw=build(q,n)
 def ev(x,y,z):
  v=0
  for j,(a,b,c) in enumerate(mons):
   if mask>>j&1:v^=m(m(pw[x][a],pw[y][b]),pw[z][c])
  return not v
 return sum(ev(1,y,z) for y in range(q) for z in range(q))+sum(ev(0,1,z) for z in range(q))+int(ev(0,0,1))
def numerator(ns):
 s=[None]+[(1<<k)+1-n for k,n in enumerate(ns,1)]
 c=[1]
 for k in range(1,7):
  r=-sum(c[k-i]*s[i] for i in range(1,k+1))
  assert r%k==0,(r,k)
  c.append(r//k)
 return c
EXPECTED_RANKS=[2,6,6,6,6,5,2,6,2,5]
for mask, expected in zip(REPS,EXPECTED_RANKS):
 ns=[count(mask,n) for n in range(1,7)]
 c=numerator(ns)
 pr=max(i for i,x in enumerate(c) if x&1)
 assert ns[0]==7 and pr==expected
 print(hex(mask),'points',ns,'L0..6',c,'p-rank',pr,flush=True)
print('POINT_COUNT_ZETA_VERIFY_OK')
