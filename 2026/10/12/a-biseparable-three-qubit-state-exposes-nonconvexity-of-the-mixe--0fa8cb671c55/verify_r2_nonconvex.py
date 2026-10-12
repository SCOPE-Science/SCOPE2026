from fractions import Fraction as F

# Exact arithmetic in Q(sqrt(2)): pair (a,b) means a+b*sqrt(2).
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(q,x): return (q*x[0], q*x[1])
def eq(x,y): return x==y

N=8

def outer(v):
    return [[v[i]*v[j] for j in range(N)] for i in range(N)]

def madd(*ms):
    return [[sum((m[i][j] for m in ms), F(0)) for j in range(N)] for i in range(N)]

def smul(q,m):
    return [[q*x for x in row] for row in m]

def pt(m,party):
    out=[[F(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        bi=[(i>>2)&1,(i>>1)&1,i&1]
        for j in range(N):
            bj=[(j>>2)&1,(j>>1)&1,j&1]
            ii=bi[:]; jj=bj[:]
            ii[party],jj[party]=bj[party],bi[party]
            r=(ii[0]<<2)|(ii[1]<<1)|ii[2]
            c=(jj[0]<<2)|(jj[1]<<1)|jj[2]
            out[r][c]=m[i][j]
    return out

def perm_index(i,p):
    bits=[(i>>2)&1,(i>>1)&1,i&1]
    bb=[bits[p[0]],bits[p[1]],bits[p[2]]]
    return (bb[0]<<2)|(bb[1]<<1)|bb[2]

# Unnormalized integer coefficient vectors; normalization is 1/sqrt(2),
# so projectors are one-half their integer outer products.
vAB=[F(0)]*N; vAB[0]=F(1); vAB[6]=F(1)
vAC=[F(0)]*N; vAC[0]=F(1); vAC[5]=F(1)
vBC=[F(0)]*N; vBC[0]=F(1); vBC[3]=F(1)
PAB=smul(F(1,2),outer(vAB)); PAC=smul(F(1,2),outer(vAC)); PBC=smul(F(1,2),outer(vBC))
rho=smul(F(1,3),madd(PAB,PAC,PBC))

assert sum(rho[i][i] for i in range(N)) == F(1)
assert rho[0][0] == F(1,2)
for k in (3,5,6):
    assert rho[0][k] == rho[k][0] == F(1,6)
    assert rho[k][k] == F(1,6)

# Each state is product across the named singleton cut: the singleton bit is 0
# in both occupied basis vectors.
assert all(((i & 1)==0) for i,x in enumerate(vAB) if x)       # C | AB
assert all((((i>>1)&1)==0) for i,x in enumerate(vAC) if x)   # B | AC
assert all((((i>>2)&1)==0) for i,x in enumerate(vBC) if x)   # A | BC

# Full permutation symmetry of rho.
for p in ((0,2,1),(1,0,2),(2,1,0),(1,2,0),(2,0,1)):
    for i in range(N):
        for j in range(N):
            assert rho[i][j] == rho[perm_index(i,p)][perm_index(j,p)]

# For each partial transpose, verify an exact negative eigenvector.
# The support triples are obtained directly from the transposed matrices.
triples = {
    0:(1,2,4), # PT on A
    1:(1,2,4), # PT on B (same index set, different arrangement but same block)
    2:(1,2,4), # PT on C
}
# Instead of assuming ordering, locate a 3x3 connected zero-diagonal block
# with four off-diagonal entries equal to 1/6, isomorphic to a length-2 star.
for party in range(3):
    M=pt(rho,party)
    found=None
    for center in range(N):
        leaves=[j for j in range(N) if j!=center and M[center][j]==F(1,6) and M[j][center]==F(1,6)]
        if len(leaves)>=2:
            for a in range(len(leaves)):
                for b in range(a+1,len(leaves)):
                    l1,l2=leaves[a],leaves[b]
                    if M[l1][l2]==0 and M[l2][l1]==0 and M[center][center]==M[l1][l1]==M[l2][l2]==0:
                        found=(l1,l2,center); break
                if found: break
        if found: break
    assert found is not None
    l1,l2,c=found
    # v=(1,1,-sqrt(2)) on leaves,center; lambda=-sqrt(2)/6.
    v=[(F(0),F(0)) for _ in range(N)]
    v[l1]=(F(1),F(0)); v[l2]=(F(1),F(0)); v[c]=(F(0),F(-1))
    lam=(F(0),F(-1,6))
    for i in range(N):
        lhs=(F(0),F(0))
        for j in range(N):
            lhs=add(lhs, scale(M[i][j],v[j]))
        rhs=mul(lam,v[i])
        assert eq(lhs,rhs), (party,i,lhs,rhs,found)

print('VERIFY_OK negative_eigenvalue=-sqrt(2)/6 all_three_cuts')
