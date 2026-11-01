"""Independent exhaustive microscopic check for the five-color firefly rule on K_{1,3,4}."""
import numpy as np

SIZES=(1,3,4)
N=sum(SIZES)
TOTAL=5**N
r=np.arange(TOTAL,dtype=np.int64)
original=np.empty((TOTAL,N),dtype=np.uint8)
for j in range(N):
    original[:,j]=(r%5).astype(np.uint8)
    r//=5
state=original.copy()
slices=[]
s=0
for n in SIZES:
    slices.append(slice(s,s+n));s+=n
fixed={}
for t in range(1,19):
    blink=[np.any(state[:,sl]==2,axis=1) for sl in slices]
    nxt=np.empty_like(state)
    for i,sl in enumerate(slices):
        outside=np.logical_or.reduce([blink[j] for j in range(3) if j!=i])
        x=state[:,sl]
        hold=(x>2)&outside[:,None]
        nxt[:,sl]=np.where(hold,x,(x+1)%5)
    state=nxt
    if t in (1,2,3,5,6,9,18):
        fixed[t]=np.all(state==original,axis=1)
        print('fixed',t,int(fixed[t].sum()))
primitive18=fixed[18]&~fixed[9]&~fixed[6]
assert int(primitive18.sum())==864, int(primitive18.sum())
assert not np.any(fixed[1]|fixed[2]|fixed[3])
print('MICRO_PERIOD_18_OK',TOTAL,int(primitive18.sum()),int(primitive18.sum()//18))
