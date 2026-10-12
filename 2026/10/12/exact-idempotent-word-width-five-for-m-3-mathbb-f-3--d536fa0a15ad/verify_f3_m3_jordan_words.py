#!/usr/bin/env python3
import numpy as np

q=3
N=q**9
weights=(q**np.arange(9,dtype=np.int64))
ids=np.arange(N,dtype=np.int64)
digits=((ids[:,None]//weights[None,:])%q).astype(np.int16)
M=digits.reshape(N,3,3)

# Exhaustive idempotents in M_3(F_3); Jordan idempotence equals ordinary idempotence.
MM=np.matmul(M,M)%q
idem_mask=np.all(MM==M,axis=(1,2))
idem_ids=ids[idem_mask]
E=M[idem_mask]
assert len(idem_ids)==236

# Breadth-first closure under right multiplication by an idempotent in the
# left-nested Jordan word recursion.  Over F_3, 1/2 = 2.
dist=np.full(N,-1,dtype=np.int8)
dist[idem_ids]=1
frontier=idem_ids.copy()
counts=[0,len(frontier)]

def encode(A):
    flat=A.reshape(-1,9).astype(np.int64)
    return flat@weights

depth=1
while len(frontier):
    new_parts=[]
    Xall=M[frontier]
    for s in range(0,len(frontier),128):
        X=Xall[s:s+128]
        # Pairwise products X E and E X for all X in batch and all idempotents E.
        XE=np.einsum('bij,ejk->beik',X,E,optimize=True)
        EX=np.einsum('eij,bjk->beik',E,X,optimize=True)
        J=(2*(XE+EX))%q
        cand=np.unique(encode(J))
        cand=cand[dist[cand]<0]
        if len(cand):
            # Mark immediately so later batches only contribute genuinely new states.
            dist[cand]=depth+1
            new_parts.append(cand)
    if not new_parts:
        break
    frontier=np.unique(np.concatenate(new_parts))
    # All were marked with the same minimal distance.
    counts.append(len(frontier))
    depth+=1

# Exact census.
actual=[int(np.sum(dist==d)) for d in range(1,int(dist.max())+1)]
expected=[236,3068,12953,3308,117]
assert actual==expected,(actual,expected)
assert int(np.sum(dist>=0))==19682
assert int(dist.max())==5

# The unique nonrepresentable point is -I=2I, in agreement with the scalar obstruction.
minusI=np.zeros((3,3),dtype=np.int16); np.fill_diagonal(minusI,2)
minusI_id=int(encode(minusI.reshape(1,3,3))[0])
unseen=np.flatnonzero(dist<0)
assert unseen.tolist()==[minusI_id]

# The length-five stratum is exactly the trace-2 nonscalar involution stratum.
I=np.eye(3,dtype=np.int16)
A2=np.matmul(M,M)%q
trace=(M[:,0,0]+M[:,1,1]+M[:,2,2])%q
scalar=np.zeros(N,dtype=bool)
for a in range(q):
    S=(a*I)%q
    sid=int(encode(S.reshape(1,3,3))[0])
    scalar[sid]=True
invol=np.all(A2==I,axis=(1,2)) & (trace==2) & (~scalar)
extreme=(dist==5)
assert int(np.sum(invol))==117
assert np.array_equal(invol,extreme)

print('VERIFY_OK')
print(f'total={N} idempotents={len(idem_ids)} representable={int(np.sum(dist>=0))} nonrepresentable={unseen.tolist()}')
print('minimal_length_counts=' + ','.join(f'{d}:{c}' for d,c in enumerate(actual,1)))
print(f'width={int(dist.max())} length5={int(np.sum(extreme))} trace2_nonscalar_involutions={int(np.sum(invol))}')
