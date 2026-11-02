"""Independent finite-field checks for commuting involutions in four-by-four unitriangular groups.
Run: python ut4_involution_checker.py (standard Python, no dependencies).
"""
from itertools import product


def mul(x,y,q):
    if q==2:
        return x&y
    if q==4:
        if not x or not y: return 0
        v=0
        for j in range(2):
            if (y>>j)&1: v ^= x<<j
        if v&8: v ^= 0b1100
        if v&4: v ^= 0b111
        return v
    raise ValueError(q)


def predicted(q,m):
    t=q**m
    return t*(1+(q+1)**2*(t-1)+2*(q+1)*(t-1)*(t-q)+(t-1)*t*t)


def involution(x,q):
    a,b,c,d,e,f=x
    return mul(a,b,q)==0 and mul(b,c,q)==0 and mul(a,e,q)^mul(d,c,q)==0


def commute(x,y,q):
    a,b,c,d,e,_=x
    A,B,C,D,E,_=y
    return (mul(a,B,q)==mul(A,b,q) and
            mul(b,C,q)==mul(B,c,q) and
            (mul(a,E,q)^mul(d,C,q))==(mul(A,e,q)^mul(D,c,q)))


def test(q):
    el=list(product(range(q),repeat=6))
    I=[x for x in el if involution(x,q)]
    assert len(I)==predicted(q,1),(q,len(I),predicted(q,1))
    # Enumerate quadratic-form maximal totally singular 2-spaces without
    # assuming the Segre/ruling formula. Each is represented by its full set.
    vec=list(product(range(q),repeat=4))
    def add(u,v):return tuple(i^j for i,j in zip(u,v))
    def scale(s,u):return tuple(mul(s,z,q) for z in u)
    def sing(u):return (mul(u[0],u[3],q)^mul(u[2],u[1],q))==0
    planes=set()
    zero=(0,0,0,0)
    for u in vec:
        if u==zero or not sing(u):continue
        Lu={scale(a,u) for a in range(q)}
        for v in vec:
            if v in Lu or not sing(v):continue
            P=frozenset(add(scale(a,u),scale(b,v)) for a in range(q) for b in range(q))
            if all(sing(w) for w in P):planes.add(P)
    assert len(planes)==2*(q+1),(q,len(planes))
    rowcounts=[]
    for x in I:
        rowcounts.append(sum(commute(x,y,q) for y in I))
    n2=sum(rowcounts)
    assert n2==predicted(q,2),(q,n2,predicted(q,2))
    if q==2:
        n3=0
        for i,x in enumerate(I):
            for j,y in enumerate(I):
                if commute(x,y,q):
                    n3+=sum(commute(x,z,q) and commute(y,z,q) for z in I)
        assert n3==predicted(q,3),(q,n3,predicted(q,3))
        # Maximal elementary abelian subgroups equal maximal cliques in
        # the graph of involutions including the identity.
        # Bron-Kerbosch exact graph clique enumeration, no dependencies.
        N=len(I)
        neighbor=[{j for j,y in enumerate(I) if i!=j and commute(x,y,q)} for i,x in enumerate(I)]
        maximal=[]
        def bk(R,P,X):
            if not P and not X:
                maximal.append(len(R));return
            pivot=max(P|X,key=lambda u:len(P & neighbor[u])) if P or X else None
            for v in list(P-neighbor[pivot] if pivot is not None else P):
                bk(R|{v},P&neighbor[v],X&neighbor[v]);P.remove(v);X.add(v)
        bk(set(),set(range(N)),set())
        assert sorted(maximal)==[8]*5+[16],sorted(maximal)
        return (len(el),len(I),n2,n3,len(planes),sorted(maximal))
    return (len(el),len(I),n2,len(planes))


if __name__=='__main__':
    for q in (2,4):
        print('GF',q,'group involutions pair_count and other:',test(q))
    print('UT4_INVOLUTION_POLAR_CENSUS_OK')
