"""Exact finite verification of the integral Burkhardt node--Jacobi-plane incidence lattice."""
from itertools import combinations, permutations
from collections import Counter

# F_4 = F_2[w]/(w^2+w+1), represented by integers 0,1,2,3.
def times(a,b):
    z = ((a&1)*(b&1)) ^ ((((a&1)*((b>>1)&1)) ^ (((a>>1)&1)*(b&1)))<<1) ^ ((((a>>1)&1)*((b>>1)&1))<<2)
    if z&4: z ^= 7
    return z

def inv(a):
    return (0,1,3,2)[a] if a else None

def canonical(v):
    leading=next(x for x in v if x)
    return tuple(times(inv(leading),x) for x in v)

def rank4(rows):
    a=[list(row) for row in rows]
    n=len(a);r=0
    for j in range(6):
        ii=next((i for i in range(r,n) if a[i][j]),None)
        if ii is None:continue
        a[r],a[ii]=a[ii],a[r]
        u=inv(a[r][j]);a[r]=[times(u,v) for v in a[r]]
        for i in range(n):
            if i!=r and a[i][j]:
                u=a[i][j]
                a[i]=[x^times(u,y) for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r

def sym4(v):
    z=0
    for c in combinations(v,4):
        term=1
        for a in c:term=times(term,a)
        z^=term
    return z

def nodeset():
    points=set()
    for I in combinations(range(6),2):
        v=[int(j in I) for j in range(6)]
        points.add(canonical(v))
    for order in permutations(range(6)):
        a,b,c,d,e,f=order
        if not (a<b and c<d and e<f):continue
        v=[0]*6
        for pair,val in zip(((a,b),(c,d),(e,f)),(1,2,3)):
            for j in pair:v[j]=val
        points.add(canonical(v))
    return sorted(points)

def vanishes_identically_on_plane(basis):
    # Work symbolically in F_4[u,v,w]; test every degree-4 coefficient.
    def prod_poly(p,q):
        o={}
        for a,x in p.items():
            for b,y in q.items():
                m=tuple(a[i]+b[i] for i in range(3))
                o[m]=o.get(m,0)^times(x,y)
        return {m:x for m,x in o.items() if x}
    form={}
    for I in combinations(range(6),4):
        p={(0,0,0):1}
        for coord in I:
            lin={tuple(1 if j==i else 0 for j in range(3)):basis[i][coord] for i in range(3) if basis[i][coord]}
            p=prod_poly(p,lin)
        for monom,coef in p.items():form[monom]=form.get(monom,0)^coef
    return not any(form.values())

def rank_mod2(rows):
    basis={}
    for row in rows:
        b=sum(int(z)<<j for j,z in enumerate(row))
        while b:
            p=b.bit_length()-1
            if p in basis:b ^= basis[p]
            else:
                basis[p]=b
                break
    return len(basis)

def det_bareiss(rows):
    a=[list(map(int,row)) for row in rows]
    n=len(a);prev=1;sgn=1
    for k in range(n-1):
        if a[k][k]==0:
            i=next((i for i in range(k+1,n) if a[i][k]),None)
            if i is None:return 0
            a[k],a[i]=a[i],a[k];sgn=-sgn
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                u=a[i][j]*piv-a[i][k]*a[k][j]
                assert u%prev==0
                a[i][j]=u//prev
        for i in range(k+1,n):a[i][k]=0
        prev=piv
    return sgn*a[-1][-1]

def main():
    points=nodeset()
    assert len(points)==45
    assert all((sum(p)%2==0) and sym4(p)==0 for p in points)
    # A line contains at most three nodes; hence nine-node planes have spanning triples.
    for i,j in combinations(range(45),2):
        line=[points[i],points[j]]
        assert sum(rank4(line+[p])==2 for p in points)<=3
    planes={}
    for tri in combinations(range(45),3):
        b=[points[i] for i in tri]
        if rank4(b)<3:continue
        on=tuple(i for i,p in enumerate(points) if rank4(b+[p])==3)
        if len(on)==9:planes.setdefault(on,tri)
    blocks=sorted(planes)
    assert len(blocks)==40
    assert all(vanishes_identically_on_plane([points[i] for i in planes[block]]) for block in blocks)
    M=[[int(i in block) for block in blocks] for i in range(45)]
    assert all(sum(row)==8 for row in M)
    assert all(sum(M[i][j] for i in range(45))==9 for j in range(40))
    # Gram matrix = 8I+2A, with strongly regular A=(45,32,22,24).
    common=[[sum(M[i][b]*M[j][b] for b in range(40)) for j in range(45)] for i in range(45)]
    assert all(common[i][i]==8 for i in range(45))
    assert all(common[i][j] in (0,2) for i in range(45) for j in range(45) if i!=j)
    adj=[{j for j in range(45) if i!=j and common[i][j]==2} for i in range(45)]
    assert all(len(s)==32 for s in adj)
    assert all(len(adj[i]&adj[j]) == (22 if j in adj[i] else 24) for i in range(45) for j in range(i+1,45))
    assert rank_mod2(M)==15
    # Explicit rank-25 determinant of absolute value 2^10 (zero-based indices).
    R=[18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,21,22,23,24,25,27,28]
    C=[0,1,2,3,4,5,6,8,9,10,11,12,14,15,16,17,18,20,21,22,24,25,28,29,32]
    minor=det_bareiss([[M[i][j] for j in C] for i in R])
    assert abs(minor)==1024, minor
    # Frobenius supplementary checks (not necessary for integral Smith factors).
    f=lambda v:canonical([times(x,x) for x in v])
    pmap=[points.index(f(p)) for p in points]
    assert sum(pmap[i]==i for i in range(45))==15
    bmap=[blocks.index(tuple(sorted(pmap[i] for i in b))) for b in blocks]
    assert not any(bmap[i]==i for i in range(40))
    assert all(bmap[bmap[i]]==i for i in range(40))
    print('NODES=45; JACOBI_PLANES=40; INCIDENCE=45x40')
    print('ROW_SUM=8; COLUMN_SUM=9; GRAM_SRG=(45,32,22,24)')
    print('RATIONAL_RANK=25; MOD_TWO_RANK=15; MAXIMAL_MINOR=',minor)
    print('SMITH_NONZERO_DIAGONAL=1^15,2^10; KERNEL_RANK=15')
    print('COKERNEL=Z^20+(Z/2Z)^10')
    print('FROBENIUS_NODE_ORBITS=15*1+15*2; PLANE_ORBITS=20*2')
    print('VERIFY_OK')
if __name__=='__main__':main()
