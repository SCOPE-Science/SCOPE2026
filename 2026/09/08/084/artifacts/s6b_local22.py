import json,sys
sys.path.insert(0,'/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts')
D=json.load(open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts/s4_enum22.json'))
def end_basis(rep):
    rows=[]
    for k in range(3):
        A=rep[k]
        A2=[[A[0],A[1]],[A[2],A[3]]]
        for i in range(2):
            for j in range(2):
                r=[0]*8
                for l in range(2):
                    if A2[l][j]: r[i*2+l]^=A2[l][j]
                for m in range(2):
                    if A2[i][m]: r[4+m*2+j]^=A2[i][m]
                rows.append(r)
    M2=[r[:] for r in rows]; piv=0; where=[-1]*8; R=len(rows)
    for c in range(8):
        f=next((i for i in range(piv,R) if M2[i][c]),None)
        if f is None: continue
        M2[piv],M2[f]=M2[f],M2[piv]; where[c]=piv
        for i in range(R):
            if i!=piv and M2[i][c]:
                for j in range(c,8): M2[i][j]^=M2[piv][j]
        piv+=1
    free=[c for c in range(8) if where[c]==-1]
    basis=[]
    for c in free:
        v=[0]*8; v[c]=1
        for c2 in range(8):
            if where[c2]>=0: v[c2]=M2[where[c2]][c]
        basis.append(v)
    def mul(u,v):
        X=[u[4],u[5],u[6],u[7]]; Xu=[v[4],v[5],v[6],v[7]]
        Y=[u[0],u[1],u[2],u[3]]; Yu=[v[0],v[1],v[2],v[3]]
        def mm(A,B): return [A[0]*B[0]^A[1]*B[2],A[0]*B[1]^A[1]*B[3],A[2]*B[0]^A[3]*B[2],A[2]*B[1]^A[3]*B[3]]
        return mm(Y,Yu)+mm(X,Xu)
    def coords(w):
        return [w[c] for c in free]
    d=len(basis)
    T=[[coords(mul(basis[i],basis[j])) for j in range(d)] for i in range(d)]
    return basis,T
def is_field(basis,T):
    # every nonzero element invertible?
    d=len(basis)
    els=[]
    for mask in range(1<<d):
        els.append([ (mask>>j)&1 for j in range(d)])
    def mulc(u,v):
        w=[0]*d
        for i in range(d):
            if u[i]:
                for j in range(d):
                    if v[j]:
                        t=T[i][j]
                        for r in range(d): w[r]^=t[r]
        return w
    def isid(u):
        # identity: mulc(u,v)==v for all v
        for v in els:
            if mulc(u,v)!=v: return False
        return True
    ident=next(u for u in els if isid(u))
    ninv=0
    for u in els:
        if u==[0]*d: continue
        inv=any(mulc(u,v)==ident for v in els)
        if not inv: ninv+=1
    return ninv==0
nloc=0; nfield=0; rows=[]
for k,v in D['reps'].items():
    if not v['indec']: continue
    Mk=[[[v['rep'][kk][i*2+j] for j in range(2)] for i in range(2)] for kk in range(3)]
    B,T=end_basis(v['rep'])
    d=len(B)
    if d==1: rows.append((k,'brick',True)); continue
    assert d==2,(k,d)
    f=is_field(B,T)
    nfield+=f; nloc+=(not f)
    rows.append((k,'F4' if f else 'dual',not f))
nabs=70+nloc
print('dim2-local(abs,dual):',nloc,' dim2-field(F4,nonabs):',nfield,' Kac A22(2)=',nabs)
json.dump({'dual':nloc,'field':nfield,'kac22':nabs,'rows':rows},open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts/s6b_local22.json','w'))
