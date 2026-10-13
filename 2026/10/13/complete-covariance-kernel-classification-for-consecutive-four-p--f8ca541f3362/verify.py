"""Exact finite certificate for consecutive four-pattern covariance geometry.
Run: python3 verify.py (stdlib only)."""
import itertools, json, math
from pathlib import Path

D=json.loads(Path(__file__).with_name('COVARIANCE_MATRIX.json').read_text())
PAT=[tuple(int(x)-1 for x in v) for v in D['patterns']]
IDX={p:i for i,p in enumerate(PAT)}
L=D['L']; A=D['matrix']; PRIME=1000003
assert len(PAT)==24 and L==20160 and len(A)==24

def pattern(seq):
    ranks={value:i for i,value in enumerate(sorted(seq))}
    return tuple(ranks[x] for x in seq)

def rank_mod(rows):
    B=[[x%PRIME for x in row] for row in rows]
    r=0
    for col in range(len(B[0])):
        pivot=next((i for i in range(r,len(B)) if B[i][col]),None)
        if pivot is None: continue
        B[pivot],B[r]=B[r],B[pivot]
        inv=pow(B[r][col],-1,PRIME)
        B[r]=[(x*inv)%PRIME for x in B[r]]
        for i in range(r+1,len(B)):
            alpha=B[i][col]
            if alpha: B[i]=[(u-alpha*v)%PRIME for u,v in zip(B[i],B[r])]
        r+=1
    return r

def det_mod(rows):
    B=[[x%PRIME for x in row] for row in rows]
    out=1
    for k in range(len(B)):
        pivot=next((i for i in range(k,len(B)) if B[i][k]),None)
        if pivot is None: return 0
        if pivot!=k: B[pivot],B[k]=B[k],B[pivot];out=-out
        v=B[k][k];out=out*v%PRIME
        inv=pow(v,-1,PRIME)
        for i in range(k+1,len(B)):
            factor=B[i][k]*inv%PRIME
            if factor:
                for j in range(k,len(B)):B[i][j]=(B[i][j]-factor*B[k][j])%PRIME
    return out%PRIME

assert A==list(map(list,zip(*A)))
Q=[]
for gap in range(4):
    freq=[[0]*24 for _ in range(24)]
    for perm in itertools.permutations(range(4+gap)):
        i=IDX[pattern(perm[:4])]; j=IDX[pattern(perm[gap:4+gap])]
        freq[i][j]+=1
    f=math.factorial(4+gap)
    Q.append([[freq[i][j]*(L//f)-L//576 for j in range(24)] for i in range(24)])
B=[[Q[0][i][j]+sum(Q[d][i][j]+Q[d][j][i] for d in (1,2,3)) for j in range(24)] for i in range(24)]
assert B==A
BASIS=[[1]*24]
for g in itertools.permutations(range(3)):
    BASIS.append([int(pattern(t[:3])==g)-int(pattern(t[1:])==g) for t in PAT])
assert all(all(sum(x*v for x,v in zip(row,b))==0 for row in A) for b in BASIS)
assert rank_mod(BASIS)==6
assert rank_mod(A)==18
leading=[[A[i][j] for j in range(18)] for i in range(18)]
assert det_mod(leading)==897856

# Independent exact rational sample covariance of all twenty-four counts.
checked=0
for n in range(4,8):
    m=n-3
    n_perm=math.factorial(n)
    sums=[0]*24
    products=[[0]*24 for _ in range(24)]
    for perm in itertools.permutations(range(n)):
        ct=[0]*24
        for i in range(m):ct[IDX[pattern(perm[i:i+4])]]+=1
        for a in range(24):
            sums[a]+=ct[a]
            if ct[a]:
                for b in range(24): products[a][b]+=ct[a]*ct[b]
    assert all(x*24==n_perm*m for x in sums)
    expected=[[m*Q[0][a][b]+sum((m-d)*(Q[d][a][b]+Q[d][b][a]) for d in range(1,min(3,m-1)+1)) for b in range(24)] for a in range(24)]
    for a in range(24):
        for b in range(24):
            empirical=products[a][b]*L//1*n_perm # compare by cross multiplication below
            assert 576*L*products[a][b]-L*n_perm*m*m == 576*n_perm*expected[a][b],(n,a,b)
            checked+=1
print(f'VERIFY_OK: rank18/nullity6; mod det897856; {checked} exact covariance identities across n=4..7')
