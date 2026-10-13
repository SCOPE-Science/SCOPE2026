from itertools import combinations
from functools import lru_cache


def adj(nA,nB,u,v):
    return (u<nA) != (v<nA)

def is_dominating(nA,nB,S):
    n=nA+nB; S=set(S)
    for v in range(n):
        if v not in S and not any(adj(nA,nB,v,u) for u in S):
            return False
    return True

def is_secure_dominating(nA,nB,S):
    n=nA+nB; S=set(S)
    if not is_dominating(nA,nB,S): return False
    for v in range(n):
        if v in S: continue
        defenders=[u for u in S if adj(nA,nB,u,v)]
        if not any(is_dominating(nA,nB,(S-{u})|{v}) for u in defenders):
            return False
    return True

def occ_secure(s,t,x,y):
    # occupancy characterization
    dom = (x==s or y>0) and (y==t or x>0)
    if not dom: return False
    if x<s and not (x==s-1 or y>=2): return False
    if y<t and not (y==t-1 or x>=2): return False
    return True

def partitions(n):
    # canonical set partitions as tuple of bitmasks
    blocks=[]
    def rec(v):
        if v==n:
            yield tuple(blocks); return
        bit=1<<v
        for i in range(len(blocks)):
            blocks[i]|=bit
            yield from rec(v+1)
            blocks[i]^=bit
        blocks.append(bit)
        yield from rec(v+1)
        blocks.pop()
    yield from rec(0)

def mask_vertices(mask,n):
    return [i for i in range(n) if mask>>i & 1]

def sec_partition(s,t,part):
    n=s+t
    secure={m:is_secure_dominating(s,t,mask_vertices(m,n)) for m in part}
    # In K_st, universal singleton only exists at K_11; generic definition handled.
    for m in part:
        vs=mask_vertices(m,n)
        singleton_universal=(len(vs)==1 and all(adj(s,t,vs[0],w) or w==vs[0] for w in range(n)))
        if secure[m]:
            if not singleton_universal: return False
            continue
        ok=False
        for q in part:
            if q==m or secure[q]: continue
            if is_secure_dominating(s,t,mask_vertices(m|q,n)):
                ok=True; break
        if not ok: return False
    return True

def formula(s,t):
    if s>t: s,t=t,s
    if s==1: return 2 if t==1 else 3
    if s==2: return 4
    return s+t-min(s-2,4)

def exact_SEC(s,t):
    n=s+t
    best=0
    for p in partitions(n):
        k=len(p)
        if k<=best: continue
        if sec_partition(s,t,p): best=k
    return best

# occupancy characterization check all subsets by occupancies through 8x8
occ_checks=0
for s in range(1,9):
  for t in range(s,9):
    n=s+t
    # representative subsets for all occupancies suffice by symmetry, but evaluate direct sets too through n<=10
    for x in range(s+1):
      for y in range(t+1):
        S=list(range(x))+list(range(s,s+y))
        a=is_secure_dominating(s,t,S)
        b=occ_secure(s,t,x,y)
        assert a==b,(s,t,x,y,a,b)
        occ_checks+=1

# exact partition enumeration through order 9
profiles=[]
partition_count=0
for n in range(2,10):
  for s in range(1,n//2+1):
    t=n-s
    val=exact_SEC(s,t)
    exp=formula(s,t)
    assert val==exp,(s,t,val,exp)
    profiles.append((s,t,val))
    # Count Bell number once per profile by generator below is expensive to recount exactly; omit.

# construction checks symbolically for a broad range using occupancy SDS checks
construction_checks=0
for s in range(1,41):
  for t in range(s,41):
    exp=formula(s,t)
    if s==1:
      if t==1:
        # singleton partition: each singleton is universal in K2
        pass
      else:
        # P=(1,t-2), R=(0,1), S=(0,1)
        assert not occ_secure(s,t,1,t-2)
        assert occ_secure(s,t,1,t-1)
    elif s==2:
      if t==2:
        assert occ_secure(s,t,1,1)
      else:
        assert not occ_secure(s,t,1,t-2)
        assert occ_secure(s,t,2,t-2)
        assert occ_secure(s,t,1,t-1)
    elif s<=5:
      # hub U=(s-1,0), all others singleton
      assert not occ_secure(s,t,s-1,0)
      assert occ_secure(s,t,s,0)
      assert occ_secure(s,t,s-1,1)
    else:
      # P=(1,2), Q=(2,1), all remaining singleton
      assert not occ_secure(s,t,1,2)
      assert not occ_secure(s,t,2,1)
      assert occ_secure(s,t,3,3)
      assert occ_secure(s,t,2,2)
    construction_checks+=1

print('ALL CHECKS PASSED')
print(f'occupancy_checks={occ_checks}')
print(f'exact_profiles_order_2_through_9={len(profiles)}')
print('exact_values=' + repr(profiles))
print(f'construction_profiles_1_le_s_le_t_le_40={construction_checks}')
