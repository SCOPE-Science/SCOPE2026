"""Exact finite-state and simplicial checks for ladder dominance-complex symmetry.
Run: python3 checker.py   (standard library only).
"""
from collections import defaultdict

def allowed(n,mask):
    for c in range(n):
        for a in (0,1):
            p=2*c+a
            neighborhood=(1<<p)|(1<<(p^1))
            if c: neighborhood|=1<<(p-2)
            if c+1<n: neighborhood|=1<<(p+2)
            if (mask&neighborhood)==neighborhood:
                return False
    return True

def action(n,kind):
    output=[]
    for i in range(n):
        for a in (0,1):
            j=n-1-i if kind in ("r","rs") else i
            b=1-a if kind in ("s","rs") else a
            output.append(2*j+b)
    return output

def orbit_weight(mask,perm):
    return (-1)**sum(bool(mask&(1<<i)) and i<=perm[i] for i in range(len(perm)))

def direct_character(n,kind):
    perm=action(n,kind)
    total=0
    for mask in range(1<<(2*n)):
        if not allowed(n,mask):continue
        moved=sum(1<<perm[i] for i in range(2*n) if mask&(1<<i))
        if moved==mask:total+=orbit_weight(mask,perm)
    return total

def matvec(matrix,v):
    return [sum(x*y for x,y in zip(row,v)) for row in matrix]

def weighted_pair_transfer(states,weight,transition,start,end):
    N=len(states)
    T=[[0]*N for _ in range(N)]
    u=[0]*N;v=[0]*N
    for i,ab in enumerate(states):
        u[i]=weight(ab[0])*weight(ab[1])*start(*ab)
        v[i]=end(*ab)
        for j,bc in enumerate(states):
            if ab[1]==bc[0] and transition(ab[0],ab[1],bc[1]):
                T[i][j]=weight(bc[1])
    return T,u,v

def dot(x,y):return sum(a*b for a,b in zip(x,y))

def layer_matrix():
    states=[(a,b) for a in range(2) for b in range(2)]
    return weighted_pair_transfer(states,lambda a:(-1)**a,
      lambda a,b,c:not(a==b==c==1),
      lambda a,b:not(a==b==1),lambda a,b:not(a==b==1))

def pal_matrix():
    states=[(a,b) for a in range(4) for b in range(4)]
    return weighted_pair_transfer(states,lambda a:(-1)**a.bit_count(),
      lambda a,b,c:b!=3 or (a&c)==0,
      lambda a,b:a!=3 or b==0,
      lambda a,b:b!=3 or a==0)

def rank_gf2(columns):
    pivots={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x;break
            x^=pivots[p]
    return len(pivots)

def reduced_mod2_betti(n):
    groups=defaultdict(list)
    for mask in range(1<<(2*n)):
        if allowed(n,mask):groups[mask.bit_count()-1].append(mask)
    ranks={}
    for degree in sorted(groups):
        if degree<0:continue
        rows={mask:i for i,mask in enumerate(groups[degree-1])}
        columns=[]
        for mask in groups[degree]:
            bitset=0
            k=mask
            while k:
                lsb=k&-k;k-=lsb
                bitset^=1<<rows[mask^lsb]
            columns.append(bitset)
        ranks[degree]=rank_gf2(columns)
    betti={i:len(faces)-ranks.get(i,0)-ranks.get(i+1,0) for i,faces in groups.items()}
    return sum(map(len,groups.values())),{i:v for i,v in betti.items() if v}

def expected(n):
    assert n>=2 and n%2==0
    m=n//4
    if n%4==0:return (n+1,1,2*m+1,2*m+1)
    return (n+1,-1,-(2*m+1),-(2*m+1))

def check():
    L,u,v=layer_matrix()
    P,p,q=pal_matrix()
    vl=v[:]
    for _ in range(4):vl=matvec(L,vl)
    assert vl==v,"4-state identity L^4 v=v"
    p2=matvec(P,matvec(P,q))
    p4=matvec(P,matvec(P,p2))
    assert [a-2*b+c for a,b,c in zip(p4,p2,q)]==[0]*16,"16-state identity (P^2-I)^2 q=0"
    z_layers=[];cv=v[:]
    for n in range(2,33):
        z_layers.append(dot(u,cv));cv=matvec(L,cv)
    z_pal=[-1];cv=q[:]
    for k in range(2,18):
        z_pal.append(dot(p,cv));cv=matvec(P,cv)
    assert z_pal[:4]==[-1,3,-3,5]
    for n in range(2,32,2):
        k=n//2
        e=expected(n)
        assert z_layers[n-2]==e[1]
        assert z_pal[k-1]==e[2]
        assert e[2]==e[3]
        for sign_s,sign_r in ((1,1),(1,-1),(-1,1),(-1,-1)):
            multiplicity=(e[0]+sign_s*e[1]+sign_r*e[2]+sign_s*sign_r*e[3])//4
            assert multiplicity>=0 and (e[0]+sign_s*e[1]+sign_r*e[2]+sign_s*sign_r*e[3])%4==0
    print("TRANSFER_IDENTITIES_OK 4-state_period=4 16-state_polynomial=(T^2-I)^2 checked_exactly")
    direct_checked=0
    for n in (2,4,6,8,10):
        got=tuple(direct_character(n,kind) for kind in ('id','s','r','rs'))
        assert got==expected(n),(n,got,expected(n))
        direct_checked+=1
        print("DIRECT_GROUP_CHARACTER_OK n=%d traces=%s"%(n,got))
    for n in (2,4,6):
        faces,betti=reduced_mod2_betti(n)
        assert betti=={n-1:n+1},(n,betti)
        print("INDEPENDENT_MOD2_HOMOLOGY_OK n=%d augmented_faces=%d betti=%s"%(n,faces,betti))
    print("LADDER_DOMINANCE_KLEIN_FOUR_EXACT_OK direct_cases=%d matrix_parameter_cases=15"%direct_checked)
if __name__=='__main__':check()
