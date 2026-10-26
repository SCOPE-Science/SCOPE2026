import numpy as np,itertools,collections,time
beg=time.monotonic(); N=32768
smooth=np.frombuffer(open('smoothquartic.bin','rb').read(),dtype=np.uint8)
assert len(smooth)==N and smooth[0]==0
exp=sorted([(a,b,4-a-b) for a in range(5) for b in range(5-a)],reverse=True)
# Compute each quartic's 7-bit evaluation incidence, using Boolean monomial supports.
points=list(range(1,8)); monpoint=np.zeros(7,dtype=np.uint16)
for j,p in enumerate(points):
 for i,(a,b,c) in enumerate(exp):
  if all(((p>>k)&1) or d==0 for k,d in enumerate((a,b,c))):monpoint[j]|=1<<i
masks=np.arange(N,dtype=np.uint16)
# xor population-count parity from precomputed 8-bit lookup table
pop8=np.array([int(i).bit_count()%2 for i in range(256)],dtype=np.uint8)
evals=np.zeros(N,dtype=np.uint8)
for j,mon in enumerate(monpoint):
 q=(masks & mon)
 evals|=((pop8[(q&255).astype(np.uint8)] ^ pop8[(q>>8).astype(np.uint8)])<<j)

def fwht(a):
 a=a.astype(np.int64,copy=True)
 for sh in range(15):
  b=a.reshape(-1,2,1<<sh)
  u=b[:,0,:].copy(); v=b[:,1,:].copy()
  b[:,0,:]=u+v; b[:,1,:]=u-v
 return a
contains=np.zeros(128,dtype=np.int64)
for T in range(128):
 A=((evals & T)==0)&(smooth==1)
 w=fwht(A)
 cube_sum=sum(int(u)**3 for u in w) # exact integers
 assert cube_sum%(N*6)==0,(T,cube_sum)
 contains[T]=cube_sum//(N*6)
exact=contains.copy()
for bit in range(7):
 for T in range(128):
  if not (T>>bit)&1: exact[T]-=exact[T|(1<<bit)]
assert all(v>=0 for v in exact)
D=collections.Counter()
for T in range(128):D[T.bit_count()]+=int(exact[T])
print('smooth_forms',int(smooth.sum(dtype=np.int64)),'total_pencils',contains[0], 'distribution',sorted(D.items()),'elapsed',round(time.monotonic()-beg,2))
assert contains[0]==5796728
assert [D[i] for i in range(8)]==[1883160,2388848,1171800,302904,45640,4200,168,8]
