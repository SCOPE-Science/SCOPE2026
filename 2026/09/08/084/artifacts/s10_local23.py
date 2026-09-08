import json
D=json.load(open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts/s9_indec23.json'))
def bits6(x): return [[(x>>(2*i+j))&1 for j in range(2)] for i in range(3)]
def end_basis(A,B,C):
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
    return basis,free
def mulc_func(basis,free):
    def mul(u,v):
        Y=[u[0:3],u[3:6],u[6:9]]; Yu=[v[0:3],v[3:6],v[6:9]]
        X=[u[9:11],u[11:13]]; Xu=[v[9:11],v[11:13]]
        def mm(A,B):
            n=len(A); return [[sum(A[r][k]*B[k][c] for k in range(n))%2 for c in range(n)] for r in range(n)]
        R1=mm(Y,Yu); R2=mm(X,Xu)
        return R1[0]+R1[1]+R1[2]+R2[0]+R2[1]
    def coords(w): return [w[c] for c in free]
    d=len(basis)
    T=[[coords(mul(basis[i],basis[j])) for j in range(d)] for i in range(d)]
    return T
def is_field(T):
    d=len(T)
    els=[[ (mask>>j)&1 for j in range(d)] for mask in range(1<<d)]
    def mc(u,v):
        w=[0]*d
        for i in range(d):
            if u[i]:
                for j in range(d):
                    if v[j]:
                        t=T[i][j]
                        for r in range(d): w[r]^=t[r]
        return w
    ident=next(u for u in els if all(mc(u,v)==v for v in els))
    bad=[u for u in els if u!=[0]*d and not any(mc(u,v)==ident for v in els)]
    return len(bad)==0
nloc=0; nfield=0; det=[]
for x,s,d,ind in D['rows']:
    if not ind or d==1: continue
    k0=x&63; k1=(x>>6)&63; k2=(x>>12)&63
    B,free=end_basis(bits6(k0),bits6(k1),bits6(k2))
    T=mulc_func(B,free)
    f=is_field(T)
    det.append([x,d,'F4' if f else 'local'])
    if f: nfield+=1
    else: nloc+=1
print('indec nonbrick:',det,'local:',nloc,'field:',nfield,'Kac=',183+nloc)
json.dump({'det':det,'local':nloc,'field':nfield,'kac23':183+nloc},open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts/s10_local23.json','w'))
