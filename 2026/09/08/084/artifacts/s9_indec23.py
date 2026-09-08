import json
D=json.load(open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts/s8_end23.json'))
# generic indec test for dim (2,3): End idempotent split test over GF2
def end_basis(A,B,C):
    # X 2x2 (4 vars idx 4..7), Y 3x3 (9 vars idx 0..8): YM = MX. rows: 3 eqs per arrow *3 rows? Y(3x3)M(3x2): 3*2=6 eqs per arrow
    rows=[]
    for M in (A,B,C):
        for i in range(3):
            for j in range(2):
                r=[0]*13
                for l in range(3):
                    if M[l][j]: r[i*3+l]^=M[l][j]
                for m in range(2):
                    if M[i][m]: r[9+m*2+j]^=M[i][m]
                rows.append(r)
    M2=[r[:] for r in rows]; piv=0; where=[-1]*13; R=len(rows)
    for c in range(13):
        f=next((i for i in range(piv,R) if M2[i][c]),None)
        if f is None: continue
        M2[piv],M2[f]=M2[f],M2[piv]; where[c]=piv
        for i in range(R):
            if i!=piv and M2[i][c]:
                for j in range(c,13): M2[i][j]^=M2[piv][j]
        piv+=1
    free=[c for c in range(13) if where[c]==-1]
    basis=[]
    for c in free:
        v=[0]*13; v[c]=1
        for c2 in range(13):
            if where[c2]>=0: v[c2]=M2[where[c2]][c]
        basis.append(v)
    return basis
def mm(A,n):
    def M(X,Y):
        return [[sum(X[r][k]*Y[k][c] for k in range(n))%2 for c in range(n)] for r in range(n)]
    return M(A[0],A[1])
def split_end(basis):
    # enumerate endos, test idempotent nontrivial
    d=len(basis)
    for mask in range(1,(1<<d)-1):
        v=[0]*13
        for j in range(d):
            if mask>>j &1:
                for c in range(13): v[c]^=basis[j][c]
        Y=[v[0:3],v[3:6],v[6:9]]; X=[v[9:11],v[11:13]]
        def sq(M):
            n=len(M); return [[sum(M[r][k]*M[k][c] for k in range(n))%2 for c in range(n)] for r in range(n)]
        if sq(Y)==Y and sq(X)==X:
            if all(a==0 for a in v): continue
            if Y==[[1,0,0],[0,1,0],[0,0,1]] and X==[[1,0],[0,1]]: continue
            return False
    return True
def bits6(x): return [[(x>>(2*i+j))&1 for j in range(2)] for i in range(3)]
nind=0; rows=[]
for x,s,d in D['rows']:
    k0=x&63; k1=(x>>6)&63; k2=(x>>12)&63
    B=end_basis(bits6(k0),bits6(k1),bits6(k2))
    assert len(B)==d,(x,d,len(B))
    ind=split_end(B)
    nind+=ind
    rows.append([x,s,d,ind])
print('indec classes:',nind,'of 402')
import collections
print('by enddim:',collections.Counter((d,ind) for _,_,d,ind in rows))
json.dump({'nind':nind,'rows':rows},open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts/s9_indec23.json','w'))
