import numpy as np,json,time,collections
start=time.monotonic()
N=32768;s=np.frombuffer(open('smoothquartic.bin','rb').read(),dtype=np.uint8)
rep=json.load(open('smoothquartic_orbits.json'))['smooth_orbits']
ind=np.arange(N,dtype=np.int32)

def hadamard(z):
 a=z.astype(np.int64,copy=True)
 for k in range(15):
  b=a.reshape(-1,2,1<<k)
  u=b[:,0,:].copy();v=b[:,1,:].copy()
  b[:,0,:]=u+v;b[:,1,:]=u-v
 return a

ordtriple=0
byclass=[]
for a,size in rep:
 B=(s==1)&(s[ind^a]==1)
 w=hadamard(B)
 corr=hadamard(w*w)
 assert np.all(corr%N==0)
 corr=corr//N
 bmask=(s==1)&(s[ind^a]==1)
 n=int(corr[bmask].sum(dtype=np.int64))
 assert n%4==0
 byclass.append((a,size,n))
 ordtriple+=size*n
print('smooth_orbits',len(rep),'ordered_triples',ordtriple,'div168',ordtriple%168,'NETS',ordtriple//168,'sec',time.monotonic()-start)
print('sample_counts',byclass[:8])
import json
json.dump({'nets':ordtriple//168,'ordered_triples':ordtriple,'orbit_contributions':byclass},open('quartic_nets_walsh_out.json','w'))
