from functools import lru_cache
from collections import Counter
from itertools import product


def partitions(n, mx=None):
    if n == 0:
        yield (); return
    if mx is None or mx > n: mx=n
    for a in range(mx,0,-1):
        for r in partitions(n-a,a): yield (a,)+r


def profile(part,q):
    return tuple(min(sum(s>=k for s in part),q-k+1) for k in range(1,q+1)) + tuple(min(sum(s==k for s in part),q-k) for k in range(1,q))


def criterion(part,q):
    cnt=Counter(part); d=sorted(cnt); m=[cnt[x] for x in d]; t=len(d)
    if q<d[-1]+1: return False
    R=[sum(m[i:]) for i in range(t)]
    A=[]; prev=0
    for i in range(t): A.append(R[i]+prev+1); prev=d[i]
    A.append(0); B=[d[i]+m[i]+1 for i in range(t)]
    up=[a<=q for a in A]
    changed=True
    while changed:
        changed=False
        for i,b in enumerate(B):
            if b<=q:
                if up[i] and not up[i+1]: up[i+1]=True; changed=True
                if up[i+1] and not up[i]: up[i]=True; changed=True
            elif b==q+1 and up[i] and not up[i+1]: up[i+1]=True; changed=True
    low=[a<=q+1 for a in A]
    changed=True
    while changed:
        changed=False
        for i,b in enumerate(B):
            if b<=q:
                if low[i] and not low[i+1]: low[i+1]=True; changed=True
                if low[i+1] and not low[i]: low[i]=True; changed=True
            elif b==q+1 and low[i+1] and not low[i]: low[i]=True; changed=True
    return all(up) and all(low)


def depth(part):
    q=1
    while not criterion(part,q): q+=1
    return q


def struct(part):
    out=[]
    for i,s in enumerate(part): out += [i]*s
    return tuple(out)


def ef_equiv(pa,pb,q):
    A=struct(pa); B=struct(pb); na=len(A); nb=len(B)
    @lru_cache(None)
    def rec(at,bt,r):
        for i in range(len(at)):
            for j in range(len(at)):
                if (at[i]==at[j])!=(bt[i]==bt[j]): return False
                if (A[at[i]]==A[at[j]])!=(B[bt[i]]==B[bt[j]]): return False
        if r==0: return True
        for a in range(na):
            if not any(rec(at+(a,),bt+(b,),r-1) for b in range(nb)): return False
        for b in range(nb):
            if not any(rec(at+(a,),bt+(b,),r-1) for a in range(na)): return False
        return True
    return rec((),(),q)

# Direct EF versus profile, all partitions of order <=6, q<=3.
plist=[]
for n in range(1,7): plist.extend(partitions(n))
ef_cases=0
for i,a in enumerate(plist):
    for b in plist[i:]:
        for q in range(1,4):
            assert ef_equiv(a,b,q)==(profile(a,q)==profile(b,q)), (a,b,q)
            ef_cases+=1

# Criterion versus exhaustive uniqueness among all partitions of order <=12 where target max part <=4.
allp=[]
for n in range(1,13): allp.extend(partitions(n))
crit_cases=0
for a in allp:
    if max(a)>4: continue
    for q in range(max(a)+1,7):
        same=[b for b in allp if b!=a and profile(a,q)==profile(b,q)]
        # If criterion says unique, a larger competitor would have to alter only truncated counts;
        # separately test canonical count vectors below.
        if not same:
            # bounded canonical representatives for each exact-size count 0..q
            L=max(a); found=False
            for cb in product(range(q+2),repeat=L):
                if not any(cb): continue
                b=tuple(sorted([j+1 for j,c in enumerate(cb) for _ in range(c)],reverse=True))
                if b!=a and profile(a,q)==profile(b,q): found=True; break
            unique=not found
        else: unique=False
        assert criterion(a,q)==unique,(a,q,criterion(a,q),unique,same[:1])
        crit_cases+=1

for s in range(1,7):
    for r in range(1,7): assert depth((s,)*r)==max(s,r)+1
for a in range(1,6):
    for b in range(a,7): assert depth(tuple(sorted((a,b),reverse=True)))==(3 if a==b==1 else b+1)
print(f"VERIFY_OK ef_cases={ef_cases} criterion_cases={crit_cases} uniform=36 biclique=20")
