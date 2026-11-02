"""Exact exhaustive four-agent complementary-two-type EFX/PO item threshold.
Requires Python 3 and NumPy. No floating point arithmetic.
"""
import itertools
import numpy as np

def compositions(total,parts=4):
    for prefix in itertools.product(range(total+1),repeat=parts-1):
        if sum(prefix)<=total:
            yield prefix+(total-sum(prefix),)

COMPS={i:tuple(compositions(i)) for i in range(9)}
# sample each open interval and each endpoint of the full sign arrangement r>3.
SAMPLES=((13,4),(7,2),(15,4),(4,1),(9,2),(5,1),
         (11,2),(6,1),(13,2),(7,1),(15,2),(8,1),(9,1))

def qualify(a,b,c,p,q):
    """Return (exists EFX+PO, EFX count, PO+EFX count) by exhaustive dominance."""
    P=np.asarray(list(itertools.product(COMPS[a],COMPS[b],COMPS[c])),dtype=np.int16)
    P=P.reshape((-1,3,4)).transpose((0,2,1))
    C=np.asarray(((p,q,p),(p,q,p),(p,p,q),(p,p,q)),dtype=np.int64)
    loads=np.einsum('ait,it->ai',P,C,dtype=np.int64)
    burden=np.einsum('ajt,it->aij',P,C,dtype=np.int64)
    min_item=np.min(np.where(P>0,C[np.newaxis,:,:],2**50),axis=2)
    efx=np.all((loads-min_item)[:,:,None] <= burden,axis=(1,2))
    accepted=0
    for k in np.flatnonzero(efx):
        dom=np.all(loads<=loads[k],axis=1)&np.any(loads<loads[k],axis=1)
        if not np.any(dom): accepted+=1
    return accepted>0,int(np.sum(efx)),accepted

def run():
    samples=0;profile_count=0;all_assignments=0
    for p,q in SAMPLES:
        this_profiles=0; this_allocations=0
        for a in range(9):
            for b in range(9-a):
                for c in range(9-a-b):
                    this_profiles+=1
                    this_allocations+=len(COMPS[a])*len(COMPS[b])*len(COMPS[c])
                    ok,_,_=qualify(a,b,c,p,q)
                    assert ok,(a,b,c,p,q)
        samples+=1
        profile_count=this_profiles
        all_assignments=this_allocations
        print('PASS r=%s/%s profiles=%s allocations=%s'%(p,q,this_profiles,this_allocations),flush=True)
    assert profile_count==165
    # sharp published family: 3 A universally costly, 3 B and 3 C complementary.
    # All EFX allocations are Pareto-dominated at r>3. Check representatives of each cell here.
    for p,q in SAMPLES:
        ok,efx,_=qualify(3,3,3,p,q)
        assert efx>0 and not ok,(p,q,efx)
        print('PASS sharpness at r=%s/%s EFX=%s no EFX+PO'%(p,q,efx),flush=True)
    print('VERIFIED: all 165 profiles at 13 rational cells, exact integer arithmetic; 9-item counterexample.')

if __name__=='__main__':run()
