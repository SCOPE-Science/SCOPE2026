from itertools import product


def strong_ok(mat, q):
    m=len(mat); n=len(mat[0]); H=(m+n-2)//2
    row=[[0]*q for _ in range(m)]
    col=[[0]*q for _ in range(n)]
    for i in range(m):
        for j in range(n):
            c=mat[i][j]
            row[i][c]+=1; col[j][c]+=1
    for i in range(m):
        for j in range(n):
            own=mat[i][j]
            for c in range(q):
                adj=row[i][c]+col[j][c]-(2 if c==own else 0)
                if adj>H:
                    return False
    return True


def cyclic3(m,n): return [[(i+j)%3 for j in range(n)] for i in range(m)]

def mod4(m,n): return [[(i+j)%4 for j in range(n)] for i in range(m)]

K44=[[0,1,0,0],[2,2,0,1],[0,1,1,2],[2,2,1,0]]
K47=[[2,0,1,2,1,0,2],[0,1,2,0,2,1,1],[1,0,0,1,0,2,2],[2,1,0,2,0,1,1]]

def constructor(m,n):
    if m>n: m,n=n,m
    if m==1:
        if n==1: return [[0]],1
        if n==2: return None,None
        H=(n-1)//2
        q=(n+H-1)//H
        sizes=[0]*q
        mat=[[]]
        for j in range(n):
            c=min(range(q), key=lambda z:sizes[z])
            sizes[c]+=1; mat[0].append(c)
        return mat,q
    if m==2:
        if n%2==0:
            return [[0 if j<n//2 else 1 for j in range(n)] for _ in range(2)],2
        # Three monochromatic column classes, as balanced as possible.
        qs=[j%3 for j in range(n)]
        return [qs[:],qs[:]],3
    if (m,n)==(3,4): return mod4(m,n),4
    if (m,n)==(4,5): return mod4(m,n),4
    if (m,n)==(4,4): return K44,3
    if (m,n)==(4,7): return K47,3
    return cyclic3(m,n),3

# Check all claimed constructive upper bounds on a broad finite range.
constructive=0
for m in range(1,41):
  for n in range(m,61):
    mat,q=constructor(m,n)
    if (m,n)==(1,2):
        assert mat is None
        continue
    assert strong_ok(mat,q),(m,n,q,mat)
    constructive+=1

# Verify the arithmetic claim underlying the cyclic construction.
fail=[]
for m in range(3,41):
  for n in range(m,61):
    H=(m+n-2)//2
    if (m+2)//3 + (n+2)//3 > H:
        fail.append((m,n))
assert fail==[(3,4),(4,4),(4,5),(4,7)], fail

# Exhaustively confirm the published K_{3,4} three-colour obstruction.
def any_q_coloring(m,n,q):
    N=m*n; H=(m+n-2)//2
    for ass in product(range(q), repeat=N):
        row=[[0]*q for _ in range(m)]
        col=[[0]*q for _ in range(n)]
        for k,c in enumerate(ass):
            i,j=divmod(k,n); row[i][c]+=1; col[j][c]+=1
        ok=True
        for k,c0 in enumerate(ass):
            i,j=divmod(k,n)
            for c in range(q):
                if row[i][c]+col[j][c]-(2 if c==c0 else 0)>H:
                    ok=False; break
            if not ok: break
        if ok: return True
    return False
assert not any_q_coloring(3,4,3)
assert strong_ok(mod4(3,4),4)

# Exhaustively maximize one colour class in K_{4,5}; every such class has at most 6 edges.
def class_valid_45(mask):
    m,n=4,5; H=3
    rs=[0]*m; cs=[0]*n
    for k in range(20):
        if mask>>k & 1:
            i,j=divmod(k,n); rs[i]+=1; cs[j]+=1
    for k in range(20):
        i,j=divmod(k,n); x=(mask>>k)&1
        if rs[i]+cs[j]-2*x>H: return False
    return True
mx=0
for mask in range(1<<20):
    s=mask.bit_count()
    if s<=mx: continue
    if class_valid_45(mask): mx=s
assert mx==6,mx
assert 3*mx<20
assert strong_ok(mod4(4,5),4)

# Exhaustively check two-colour feasibility for all bicliques with at most 16 edges.
def any_two(m,n):
    N=m*n
    if N>16: return None
    return any_q_coloring(m,n,2)
small2=0
for m in range(2,5):
  for n in range(m,9):
    if m*n<=16:
      got=any_two(m,n)
      pred=(m==2 and n%2==0)
      assert got==pred,(m,n,got,pred)
      small2+=1

print('ALL CHECKS PASSED; constructive_cases=%d; cyclic_exception_set=%s; K34_three_color_exhaustive=%d; K45_max_single_color=%d; two_color_small_cases=%d; constructive_range=1<=m<=40,m<=n<=60' % (constructive,fail,3**12,mx,small2))
