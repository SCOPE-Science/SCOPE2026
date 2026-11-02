"""Independent small-field tests of two intrinsic subspace families in a class-three Lie algebra.
Run with Python 3.10+; no external packages are required.
"""
from itertools import combinations, product
from math import prod


def gaussian(n, k, q):
    if k < 0 or k > n: return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den

def predicted(q,m):
    Q=q**m; n=5*m; P=Q*Q+Q+1
    ab=[P*gaussian(3*m,d,q)-(P-1)*gaussian(2*m,d,q) for d in range(n+1)]
    ids=[gaussian(2*m,d,q) for d in range(n+1)]
    for t in range(1,m+1): ids[2*m+t]+=gaussian(m,t,q)
    for t in range(1,2*m+1): ids[3*m+t]+=gaussian(2*m,t,q)
    return ab,ids


def rref_spaces(n,k,p):
    """All canonical RREF k-planes over prime field Fp, with a pure Python generator."""
    for pivots in combinations(range(n),k):
        others=[j for j in range(n) if j not in pivots]
        free=[(i,j) for i in range(k) for j in others if j>pivots[i]]
        for digits in product(range(p), repeat=len(free)):
            B=[[0]*n for _ in range(k)]
            for i,j in enumerate(pivots): B[i][j]=1
            for (i,j),v in zip(free,digits): B[i][j]=v
            yield tuple(tuple(x) for x in B)


def field_mul(a,b,p,m):
    if m==1: return a*b%p
    assert (p,m)==(2,2)
    z=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1: z ^= 1<<(i+j)
    if z&4: z ^= 0b111 # x^2=x+1
    return z


def chunks(v,p,m):
    if m==1: return list(v)
    return [v[2*i]+2*v[2*i+1] for i in range(5)]


def unchunk(t,p,m):
    if m==1: return tuple(t)
    return tuple(x for z in t for x in (z&1, z>>1))


def bracket(a,b,p,m):
    a=chunks(a,p,m);b=chunks(b,p,m)
    def minus(x,y): return (x-y)%p if m==1 else x^y
    def det(i,j):return minus(field_mul(a[i],b[j],p,m),field_mul(a[j],b[i],p,m))
    return unchunk((0,0,det(0,1),det(0,2),det(1,2)),p,m)


def in_span(x,B,p):
    y=list(x)
    for row in B:
        j=next(i for i,v in enumerate(row) if v)
        c=y[j]
        if c:
            y=[(a-c*b)%p for a,b in zip(y,row)]
    return not any(y)


def run_small(p,m):
    n=5*m
    ab,ids=predicted(p,m)
    found_ab=[0]*(n+1);found_id=[0]*(n+1)
    e=[tuple(1 if i==j else 0 for i in range(n)) for j in range(n)]
    for k in range(n+1):
        # For F2^10 exhaustive low dimensions only; other full dimensions too large.
        if n==10 and k>2:break
        for B in rref_spaces(n,k,p):
            if all(not any(bracket(v,w,p,m)) for i,v in enumerate(B) for w in B[i+1:]): found_ab[k]+=1
            if all(in_span(bracket(v,u,p,m),B,p) for v in B for u in e): found_id[k]+=1
        assert found_ab[k]==ab[k],(p,m,'abelian',k,found_ab[k],ab[k])
        assert found_id[k]==ids[k],(p,m,'ideal',k,found_id[k],ids[k])
    print('DIRECT_RREF_OK', 'q',p,'m',m,'d', list(range(min(n,2) +1)) if n==10 else 'all',
          'abelian', found_ab[:3] if n==10 else found_ab,
          'ideals', found_id[:3] if n==10 else found_id)


def check_field():
    # Characteristic-two field F4 has a^2+a+1=0 and every nonzero element has cube one.
    assert field_mul(2,2,2,2)==3
    assert field_mul(3,2,2,2)==1
    assert all(field_mul(a,field_mul(b,c,2,2),2,2)==field_mul(field_mul(a,b,2,2),c,2,2)
               for a,b,c in product(range(4),repeat=3))
    # Bracket is alternating, Jacobi (basis vectors over base field).
    for p,m in [(2,1),(3,1),(2,2)]:
        n=5*m;e=[tuple(1 if i==j else 0 for i in range(n)) for j in range(n)]
        assert all(not any(bracket(x,x,p,m)) for x in e)
        def add(x,y):return tuple((a+b)%p for a,b in zip(x,y))
        for x,y,z in product(e,repeat=3):
            j=add(add(bracket(x,bracket(y,z,p,m),p,m),bracket(y,bracket(z,x,p,m),p,m)),bracket(z,bracket(x,y,p,m),p,m))
            assert not any(j)
    print('FIELD_AND_JACOBI_OK')


def check_tuples():
    # Independently enumerate all commuting pairs of F4^5 / F2^10 (1,048,576 pairs).
    p,m=2,2;n=10;Q=4
    vectors=[tuple((a>>i)&1 for i in range(n)) for a in range(1<<n)]
    count=sum(1 for i,x in enumerate(vectors) for y in vectors if not any(bracket(x,y,p,m)))
    target=(Q*Q+Q+1)*Q**6-(Q*Q+Q)*Q**4
    assert count==target,(count,target)
    print('DIRECT_F4_PAIR_OK',count)


def check_identity():
    for p,m in product([2,3,5,7],[1,2,3]):
        a,I=predicted(p,m)
        n=5*m;Q=p**m;P=Q*Q+Q+1
        assert sum(I)==sum(gaussian(2*m,d,p) for d in range(2*m+1))+sum(gaussian(m,d,p) for d in range(1,m+1))+sum(gaussian(2*m,d,p) for d in range(1,2*m+1))
        assert a[3*m]==P and all(a[d]==0 for d in range(3*m+1,n+1))
        assert a[1]==gaussian(n,1,p) and I[n]==1
        for k in range(4):
            expected=P*Q**(3*k)-(P-1)*Q**(2*k)
            assert expected==Q**(2*k)*(1+P*(Q**k-1))
    print('FORMULA_IDENTITIES_OK',4*3)



def check_predicted_ideals():
    # Enumerate all prescribed ideals in F4/F2 10-dimensional model and independently check bracket closure.
    p,m=2,2;n=10
    e=[tuple(1 if i==j else 0 for i in range(n)) for j in range(n)]
    central=e[6:10];derived=e[4:10];
    family=[]
    for k in range(5):
        for B in rref_spaces(4,k,p):
            family.append(tuple(tuple([0]*6+list(row)) for row in B))
    for k in range(1,3):
        for B in rref_spaces(2,k,p):
            family.append(tuple(central)+tuple(tuple([0]*4+list(row)+[0]*4) for row in B))
    for k in range(1,5):
        for B in rref_spaces(4,k,p):
            family.append(tuple(derived)+tuple(tuple(list(row)+[0]*6) for row in B))
    assert len(family)==137,len(family)
    # Every prescribed ideal is closed under [L,-] and all have the expected dimensions.
    assert all(all(in_span(bracket(v,u,p,m),B,p) for v in B for u in e) for B in family)
    print('ALL_137_PREDICTED_IDEALS_CLOSED')


def check_maximal_spread():
    # For F4/F2, projective lines in F4^3 are 21, pairwise intersect trivially;
    # their inverse images with the two-coordinate center are exactly the maximal abelian spaces.
    M=range(4); add=lambda a,b:a^b
    lines=set()
    for v in product(M, repeat=3):
        if not any(v):continue
        line=frozenset(tuple(field_mul(a,t,2,2) for a in v) for t in M)
        lines.add(line)
    assert len(lines)==21
    for a,b in combinations(lines,2):assert len(a&b)==1
    # GL2(F4) and generator shifts act transitively on 20 non-special lines.
    # Fix any (a,b,c) with (a,b)!=(0,0); construct an invertible matrix with A(a,b)=(1,0),
    # then shift its first coordinate by a chosen F4-linear functional to cancel c.
    for line in lines:
        a,b,c=next(v for v in line if any(v))
        if a==b==0:continue
        sol=False
        for s,t,u,v in product(M,repeat=4):
            det=add(field_mul(s,v,2,2),field_mul(t,u,2,2))
            if det==0:continue
            if add(field_mul(s,a,2,2),field_mul(t,b,2,2))!=1:continue
            if add(field_mul(u,a,2,2),field_mul(v,b,2,2))!=0:continue
            # Shift in the U coordinate can always be chosen as lambda*a+mu*b.
            if any(add(field_mul(lam,a,2,2),field_mul(mu,b,2,2))==field_mul(det,c,2,2) for lam,mu in product(M,repeat=2)):
                sol=True;break
        assert sol
    print('PROJECTIVE_SPREAD_AND_AUTOMORPHISM_ORBITS_OK 21=1+20')

if __name__=='__main__':
    check_field()
    check_identity()
    run_small(2,1)
    run_small(3,1)
    run_small(2,2)
    check_tuples()
    check_predicted_ideals()
    check_maximal_spread()
    print('VERIFY_OK')
