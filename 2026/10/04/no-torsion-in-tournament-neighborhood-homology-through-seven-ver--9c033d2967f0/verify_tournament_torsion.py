from itertools import combinations, permutations, product
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp, smith_normal_form

EXPECTED={1:1,2:1,3:2,4:4,5:12,6:56,7:456}

def pair_index(n,i,j):
    assert i<j
    return i*(2*n-i-1)//2 + (j-i-1)

def edge(mask,n,i,j):
    if i<j: return (mask>>pair_index(n,i,j))&1
    return 1-((mask>>pair_index(n,j,i))&1)

def degrees(mask,n):
    d=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if edge(mask,n,i,j): d[i]+=1
            else: d[j]+=1
    return d

def canon(mask,n):
    d=degrees(mask,n)
    groups=[[v for v in range(n) if d[v]==q] for q in sorted(set(d),reverse=True)]
    best=None
    for blocks in product(*[list(permutations(g)) for g in groups]):
        order=[v for b in blocks for v in b]
        code=0; k=0
        for a in range(n):
            for b in range(a+1,n):
                if edge(mask,n,order[a],order[b]): code|=1<<k
                k+=1
        if best is None or code<best: best=code
    return best

def extend(mask,n,pat):
    m=n+1; out=0
    for i in range(n):
        for j in range(i+1,n):
            if edge(mask,n,i,j): out |= 1<<pair_index(m,i,j)
    for i in range(n):
        if (pat>>i)&1: out |= 1<<pair_index(m,i,n)
    return out

def reps_upto(N):
    reps={1:{0}}
    for n in range(1,N):
        nxt=set()
        for mask in reps[n]:
            for pat in range(1<<n):
                nxt.add(canon(extend(mask,n,pat),n+1))
        reps[n+1]=nxt
        assert len(nxt)==EXPECTED[n+1], (n+1,len(nxt))
    return reps

def outneighborhoods(mask,n):
    ans=[]
    for i in range(n):
        s=0
        for j in range(n):
            if i!=j and edge(mask,n,i,j): s|=1<<j
        ans.append(s)
    return ans

def faces_by_dim(mask,n):
    outs=outneighborhoods(mask,n)
    faces=[set() for _ in range(n)]
    for F in outs:
        sub=F
        while sub:
            faces[sub.bit_count()-1].add(sub)
            sub=(sub-1)&F
    while faces and not faces[-1]: faces.pop()
    return [sorted(x) for x in faces]

def boundary(faces,k):
    # d_k:C_k -> C_{k-1}
    if k==0: return DomainMatrix.zeros((0,len(faces[0])),ZZ)
    rows={f:i for i,f in enumerate(faces[k-1])}
    m=len(faces[k-1]); c=len(faces[k])
    data=[[ZZ.zero]*c for _ in range(m)]
    for j,F in enumerate(faces[k]):
        vs=[v for v in range(F.bit_length()) if (F>>v)&1]
        for pos,v in enumerate(vs):
            G=F^(1<<v)
            data[rows[G]][j]=ZZ(-1 if pos%2 else 1)
    return DomainMatrix(data,(m,c),ZZ)

def matmul(A,B): return A*B

def inverse_unimodular(T):
    # DomainMatrix.inv_den returns inv numerator, denominator
    inv,den=T.inv_den()
    assert den==ZZ.one
    return inv

def homology_invariants(faces,k):
    # returns free rank, torsion invariant factors for H_k
    nk=len(faces[k]) if k<len(faces) else 0
    if nk==0: return 0,[]
    dk=boundary(faces,k)
    if dk.shape[0]==0:
        r=0; T=DomainMatrix.eye(nk,ZZ)
    else:
        S, U, T = smith_normal_decomp(dk)
        diag=[S[i,i].element for i in range(min(S.shape))]
        r=sum(1 for x in diag if x!=0)
    if k+1>=len(faces) or not faces[k+1]:
        return nk-r,[]
    b=boundary(faces,k+1)
    Tinv=inverse_unimodular(T)
    y=Tinv*b
    # d_k b=0 implies first r rows zero
    for i in range(r):
        assert all(y[i,j].element==0 for j in range(y.shape[1]))
    z=y.extract(range(r,nk), range(y.shape[1]))
    if z.shape[0]==0 or z.shape[1]==0:
        return nk-r,[]
    sz=smith_normal_form(z)
    diag=[abs(int(sz[i,i].element)) for i in range(min(sz.shape)) if sz[i,i].element!=0]
    rank=len(diag)
    tors=[x for x in diag if x>1]
    return (nk-r)-rank,tors

def betti_mod2(faces):
    # cross-check ranks mod2 via bit Gaussian elimination
    def rank2(cols,nrows):
        basis={}; r=0
        for x in cols:
            while x:
                p=x.bit_length()-1
                if p in basis: x^=basis[p]
                else: basis[p]=x; r+=1; break
        return r
    dims=[]; ranks=[]
    for k in range(len(faces)):
        if k==0: ranks.append(0); continue
        row={f:i for i,f in enumerate(faces[k-1])}
        cols=[]
        for F in faces[k]:
            x=0
            for v in range(F.bit_length()):
                if (F>>v)&1: x^=1<<row[F^(1<<v)]
            cols.append(x)
        ranks.append(rank2(cols,len(faces[k-1])))
    bet=[]
    for k in range(len(faces)):
        rk=ranks[k]
        rnext=ranks[k+1] if k+1<len(ranks) else 0
        bet.append(len(faces[k])-rk-rnext)
    if bet: bet[0]-=1
    return bet

def main():
    reps=reps_upto(7)
    print('TOURNAMENT_COUNTS', {n:len(reps[n]) for n in reps})
    total=0; torsion=[]; patterns={}
    for n in range(1,8):
        for mask in sorted(reps[n]):
            faces=faces_by_dim(mask,n)
            inv=[]
            for k in range(1,len(faces)-1):
                a=boundary(faces,k)
                b=boundary(faces,k+1)
                c=a*b
                assert all(c[i,j].element==0 for i in range(c.shape[0]) for j in range(c.shape[1]))
            for k in range(len(faces)):
                fr,tor=homology_invariants(faces,k)
                inv.append((fr,tuple(tor)))
                if tor: torsion.append((n,mask,k,tor))
            b2=betti_mod2(faces)
            # UCT sanity: if no torsion in current/previous degree then mod2 free ranks equal
            # full equality here when all tor lists are empty
            if all(not t for _,t in inv):
                red=[fr for fr,_ in inv]
                if red: red[0]-=1
                assert b2==red, (n,mask,inv,b2)
            patterns[(n,tuple(inv))]=patterns.get((n,tuple(inv)),0)+1
            total+=1
    print('TOTAL_CLASSES',total)
    print('TORSION_WITNESSES',torsion)
    print('SEVEN_CLASSES',len(reps[7]))
    p7=[(inv,count) for (n,inv),count in patterns.items() if n==7]
    print('SEVEN_HOMOLOGY_TYPES',len(p7))
    for inv,count in sorted(p7,key=lambda z:(str(z[0]),z[1])):
        print('H7',count,inv)
    assert not torsion
    print('VERIFY_OK')
if __name__=='__main__': main()
