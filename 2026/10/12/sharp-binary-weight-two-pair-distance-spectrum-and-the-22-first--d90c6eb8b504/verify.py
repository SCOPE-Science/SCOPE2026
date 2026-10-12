"""Exhaustive small-length binary symbol-pair code checks (stdlib only)."""
from itertools import combinations

def pd(n,a,b):
    diff=set(a)^set(b)
    return sum((i in diff) or ((i+1)%n in diff) for i in range(n))

def catalog(n):
    words=list(combinations(range(n),2))
    graph=[sum(1<<j for j,v in enumerate(words) if j>i and pd(n,w,v)>=7) for i,w in enumerate(words)]
    return words,graph

def maximal(n):
    w,g=catalog(n)
    best=0; opts=[]
    def scan(chosen, candidates):
        nonlocal best,opts
        if not candidates:
            if len(chosen)>best: best=len(chosen);opts=[]
            if len(chosen)==best: opts.append(tuple(chosen))
            return
        if len(chosen)+candidates.bit_count()<best: return
        while candidates:
            v=(candidates&-candidates).bit_length()-1
            candidates &= candidates-1
            scan(chosen+[v],candidates & g[v])
            if len(chosen)+candidates.bit_count()<best:return
    scan([], (1<<len(w))-1)
    return best, [tuple(w[i] for i in item) for item in opts]

for n, expected in [(2,1),(3,1),(4,1),(5,1),(6,1),(7,2),(8,2),(9,3),(10,5)]:
    best,opts=maximal(n)
    assert best==expected, (n,best,expected)
    print('length',n,'optimum',best,'number_of_optima',len(opts))
if len(opts)!=22: raise AssertionError(('length-10-optima',len(opts)))

def move(code,rot,flip):
    n=10
    shifted=[]
    for pair in code:
        shifted.append(tuple(sorted(((rot+(-k if flip else k))%n for k in pair))))
    return tuple(sorted(shifted))

remaining=set(tuple(sorted(code)) for code in opts)
orbits=[]; reps=[]
while remaining:
    r=min(remaining)
    o={move(r,t,f) for t in range(10) for f in (0,1)}
    assert o<=remaining
    remaining-=o
    orbits.append(len(o)); reps.append(r)
assert sorted(orbits)==[2,10,10]
for z,r in sorted(zip(orbits,reps)): print('orbit',z,'representative',r)
print('VERIFY_OK direct_45_words_10_length10=22 orbit_sizes='+str(sorted(orbits)))
