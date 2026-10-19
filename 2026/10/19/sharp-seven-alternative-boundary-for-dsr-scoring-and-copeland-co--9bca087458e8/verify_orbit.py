"""Independent direct-score and orbit verification using Python stdlib."""
from itertools import permutations

N=7
M=1324
pairs=[(i,j) for i in range(N) for j in range(i+1,N)]
win=[[False]*N for _ in range(N)]
for k,(i,j) in enumerate(pairs):
    a,b=(i,j) if (M>>k)&1 else (j,i)
    win[a][b]=True

def canonical_mask(relabeled):
    result=0
    for k,(i,j) in enumerate(pairs):
        if win[relabeled[i]][relabeled[j]]:
            result |= 1<<k
    return result

def score_direct(win):
    n=len(win)
    s=[0]*n
    for z in range(n):
        u=[x for x in range(n) if win[x][z]]
        d=[y for y in range(n) if win[z][y]]
        if not d:
            for x in u: s[x]+=1
            continue
        divisible=(all(any(win[x][y] for y in d) for x in u)
                   or any(all(win[x][y] for y in d) for x in u))
        if divisible:
            for x in u+[z]:
                s[x]+=int(x!=z)+sum(win[x][y] for y in d)
    return s
cop=[sum(row) for row in win]
s=score_direct(win)
assert cop==[3,3,2,2,2,5,4],cop
assert s==[6,3,2,4,5,14,14],s
orbit={canonical_mask(pi) for pi in permutations(range(N))}
assert len(orbit)==5040,len(orbit)
assert M in orbit
print('witness_copeland:',cop,'witness_dsr:',s)
print('seven_vertex_label_orbit:',len(orbit),'automorphism_order:',5040//len(orbit))
print('VERIFY_OK')

# Independently check the lower orders using a direct Python evaluation.
for n in range(2, 7):
    pairs_n=[(i,j) for i in range(n) for j in range(i+1,n)]
    failures=0
    for mask in range(1 << len(pairs_n)):
        a=[[False]*n for _ in range(n)]
        for k,(i,j) in enumerate(pairs_n):
            src,dst=(i,j) if (mask>>k)&1 else (j,i)
            a[src][dst]=True
        values=score_direct(a)
        cop_values=[sum(row) for row in a]
        best=max(values)
        cbest=max(cop_values)
        failures+=any(values[i]==best and cop_values[i]<cbest for i in range(n))
    assert failures==0,(n,failures)
    print('independent_small_order',n,'checked',1<<len(pairs_n),'failures',failures)
