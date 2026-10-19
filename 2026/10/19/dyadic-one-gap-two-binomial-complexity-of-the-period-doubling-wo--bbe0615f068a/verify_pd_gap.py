"""Independent finite checks of dyadic gapped two-binomial factor-profile counts."""
from collections import Counter

def val(j):
    assert j>=1
    return ((j & -j).bit_length()-1)&1

def cycles(m):
    n=1<<m
    prefix=tuple(val(i) for i in range(1,n))
    return [(prefix+(b,)) for b in (0,1)]

def profile_direct(w):
    c=[w.count(0),w.count(1)]+[0]*4
    for i in range(len(w)):
        for j in range(i+2,len(w)):
            c[2+2*w[i]+w[j]]+=1
    return tuple(c)

def profile_fast(w):
    n=len(w); z=0;k=sum(w);t01=0
    for b in w:
        if b:t01+=z
        else:z+=1
    a01=sum(a==0 and b==1 for a,b in zip(w,w[1:]))
    a10=sum(a==1 and b==0 for a,b in zip(w,w[1:]))
    a00=sum(a==0 and b==0 for a,b in zip(w,w[1:]))
    a11=sum(a==1 and b==1 for a,b in zip(w,w[1:]))
    return (n-k,k,(n-k)*(n-k-1)//2-a00,t01-a01,k*(n-k)-t01-a10,k*(k-1)//2-a11)

def all_factors(m):
    ans=set()
    for word in cycles(m):
        for j in range(len(word)):
            ans.add(word[j:]+word[:j])
    return ans

def formula(m):
    n=1<<m
    return (3*n//2) if not m%2 else ((17*n-4)//12)

def count_pattern(c,p=(1,0,1,0,1)):
    n=len(c)
    return sum(all(c[(i+j)%n]==a for j,a in enumerate(p)) for i in range(n))

for m in range(2,10):
    n=1<<m
    facs=all_factors(m)
    by_profile={}
    for w in facs:
        p=profile_fast(w)
        by_profile.setdefault(p,[]).append(w)
    expected=formula(m)
    sizes=Counter(map(len,by_profile.values()))
    per=next(c for c in cycles(m) if c[:n//2]==c[n//2:])
    prim=next(c for c in cycles(m) if c[:n//2]!=c[n//2:])
    motif=count_pattern(prim)
    assert len(facs)==3*n//2,(m,len(facs))
    assert len(by_profile)==expected,(m,len(by_profile),expected)
    assert sizes[1]+sizes[2]==len(by_profile)
    assert not any(size>2 for size in sizes)
    assert sizes[2]==(n+4)//12 if m%2 else sizes[2]==0
    assert sizes[2]==motif if m%2 else sizes[2]==0
    if m<=6:
        for w in facs:assert profile_direct(w)==profile_fast(w)
    print('m',m,'n',n,'factors',len(facs),'profiles',len(by_profile),'classes',dict(sizes),'motif',motif)

# Independent infinite-prefix sampling via substitution and direct gapped-pair counts
p=(0,)
for j in range(13):
    p=tuple(x for a in p for x in ((0,1) if a==0 else (0,0)))
for m in range(2,8):
    n=1<<m
    observed={tuple(p[i:i+n]) for i in range(len(p)-n+1)}
    assert observed==all_factors(m),(m,len(observed))
    print('infinite-prefix factors verified',m,len(observed))
