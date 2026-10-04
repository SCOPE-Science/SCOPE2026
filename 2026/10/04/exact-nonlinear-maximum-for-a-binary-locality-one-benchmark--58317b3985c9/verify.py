from itertools import product, combinations

def hd(x,y):
    return sum(a!=b for a,b in zip(x,y))

# Explicit witness.
C=[]
for a,b,d in product([0,1], repeat=3):
    c=a^b
    C.append((a,a,b,b,c,c,d,d,d))
assert len(C)==8 and len(set(C))==8
assert min(hd(x,y) for x,y in combinations(C,2))==3

# Direct locality check.
for i in range(9):
    ok=False
    for j in range(9):
        if i==j:
            continue
        P=sorted(set((x[i],x[j]) for x in C))
        if len(P)>=2 and min(hd(x,y) for x,y in combinations(P,2))>=2:
            ok=True
            break
    assert ok

def parts(total, lo=2):
    if total==0:
        yield ()
        return
    for a in range(lo,total+1):
        for rest in parts(total-a,a):
            yield (a,)+rest

def wdist(x,y,w):
    return sum(ww for a,b,ww in zip(x,y,w) if a!=b)

best=0
rows=[]
for w in parts(9):
    m=len(w)
    if m==0:
        continue
    V=list(product([0,1], repeat=m))
    local_best=0
    for mask in range(1<<len(V)):
        s=mask.bit_count()
        if s<=local_best:
            continue
        D=[V[t] for t in range(len(V)) if (mask>>t)&1]
        if all(wdist(x,y,w)>=3 for x,y in combinations(D,2)):
            local_best=s
    rows.append((w,local_best))
    best=max(best,local_best)
assert best==8
print("PARTITION_MAXIMA", rows)
print("VERIFY_OK")
