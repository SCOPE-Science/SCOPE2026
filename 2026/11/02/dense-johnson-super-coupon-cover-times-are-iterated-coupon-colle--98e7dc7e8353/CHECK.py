from itertools import product,combinations

def epoch_done(slots,k,s):
    count=0; seen=set()
    for i,a in enumerate(slots,1):
        seen.add(a)
        if len(seen)==k:
            count+=1; seen=set()
            if count==s: return True
    return False

def path(k, slots, new=None):
    A=list(range(k))
    seq=[tuple(A)]
    for t,a in enumerate(slots,1):
        A[a] = k+t-1 if new is None else new[t-1]
        assert len(set(A))==k
        seq.append(tuple(A))
    return seq

def complete(seq,k,s):
    universe=set().union(*(set(A) for A in seq))
    # if s labels hit every omitted set, s-subsets aren't all covered
    for j in range(1,min(s,len(universe))+1):
        for chosen in combinations(universe,j):
            if all(set(chosen).intersection(A) for A in seq): return False
    return True

count=0
for k in range(1,4):
 for s in range(1,4):
  for t in range(0,9 if k<3 else 8):
   for word in product(range(k),repeat=t):
    target=epoch_done(word,k,s)
    actual=complete(path(k,word),k,s)
    assert actual==target,(k,s,word,target,actual)
    count+=1
print('FRESH_EQUIVALENCE_OK',count)

# finite n and collisions: any finite-label history covering all s-subsets
# must have completed s slot epochs; enumerate exactly for a small sample.
import random
R=random.Random(1829)
checks=0
for k in (1,2,3):
 for s in (1,2,3):
  n=max(2*k+4,k+s+3)
  for _ in range(1000):
   A=list(range(k)); seq=[tuple(A)]; word=[]
   for t in range(16):
    j=R.randrange(k); word.append(j)
    new=R.choice([x for x in range(n) if x not in A]);A[j]=new
    seq.append(tuple(A))
    if complete(seq,k,s):
     assert epoch_done(word,k,s),(k,s,word,seq)
    checks+=1
print('FINITE_MONOTONE_OK',checks)
