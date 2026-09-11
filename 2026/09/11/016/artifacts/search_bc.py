import itertools, json

B0 = [[0,3,-2],[-3,0,2],[2,-2,0]]

def mut_B(B,k):
    n=len(B)
    Bp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==k or j==k:
                Bp[i][j]=-B[i][j]
            else:
                Bp[i][j]=B[i][j]+max(0,B[i][k])*max(0,B[k][j])-max(0,-B[i][k])*max(0,-B[k][j])
    return Bp

def mut_ext(B,C,k):
    # extended (2n x n): top B, bottom C; mutate at k
    n=len(B)
    # build E rows 2n, cols n
    E=[row[:] for row in B]+[row[:] for row in C]
    Ep=[row[:] for row in E]
    N=2*n
    for i in range(N):
        for j in range(n):
            if i==k or j==k:
                Ep[i][j]=-E[i][j]
            else:
                Ep[i][j]=E[i][j]+max(0,E[i][k])*max(0,E[k][j])-max(0,-E[i][k])*max(0,-E[k][j])
    Bp=[row[:] for row in Ep[:n]]
    Cp=[row[:] for row in Ep[n:]]
    return Bp,Cp

def is_perm_matrix(C):
    n=len(C)
    for row in C:
        for v in row:
            if v not in (0,1): return None
    for i in range(n):
        if sum(C[i])!=1: return None
    for j in range(n):
        if sum(C[i][j] for i in range(n))!=1: return None
    # sigma: col j -> row sigma(j)
    sig=[None]*n
    for j in range(n):
        for i in range(n):
            if C[i][j]==1: sig[j]=i
    return sig

def perm_B(B0,sig):
    n=len(B0)
    return [[B0[sig[i]][sig[j]] for j in range(n)] for i in range(n)]

def mat_eq(A,Bm): return A==Bm

I=[[1 if i==j else 0 for j in range(3)] for i in range(3)]

results=[]
counts={}
# BFS over words, dedupe states? just enumerate all words no-backtrack
def enum(L):
    # generate words as tuples over 0..2, no equal adjacent
    if L==0:
        yield ()
        return
    def rec(prefix):
        if len(prefix)==L:
            yield tuple(prefix); return
        for k in range(3):
            if prefix and prefix[-1]==k: continue
            prefix.append(k)
            yield from rec(prefix)
            prefix.pop()
    yield from rec([])

for L in range(1,11):
    nwords=0; b_hits=0; full_hits=[]
    Bhit_examples=[]
    for w in enum(L):
        nwords+=1
        B=[r[:] for r in B0]; C=[r[:] for r in I]
        for k in w:
            B,C=mut_ext(B,C,k)
        sig=is_perm_matrix(C)
        if sig is not None:
            # check B perm
            if mat_eq(B,perm_B(B0,sig)):
                full_hits.append((w,sig))
        # also B-only up to perm?
        # check B equals some perm of B0
        import itertools as it
        for p in it.permutations(range(3)):
            if mat_eq(B,perm_B(B0,list(p))):
                b_hits+=1
                if len(Bhit_examples)<5:
                    Bhit_examples.append((w,list(p)))
                break
    counts[L]=(nwords,b_hits,len(full_hits))
    print(f"L={L} words={nwords} Bperm-hits={b_hits} full(B+C)perm-hits={len(full_hits)}", flush=True)
    if full_hits:
        for w,s in full_hits[:10]:
            print("  FULL",tuple(x+1 for x in w),s)
    if Bhit_examples:
        for w,p in Bhit_examples:
            print("  Bex",tuple(x+1 for x in w),p)
print(counts)
