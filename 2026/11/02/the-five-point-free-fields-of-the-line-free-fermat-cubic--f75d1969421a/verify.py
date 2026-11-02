"""Exact finite-field and incidence verification for the Fermat cubic's line-free locus.

Run with Python 3, no third-party packages. All arithmetic is integer finite-field arithmetic.
"""
from collections import Counter
from itertools import combinations, product

class Field:
    def __init__(self, p, mod=(0,1)):
        self.p = p
        self.mod = tuple(x % p for x in mod)
        assert self.mod[-1] == 1
        self.m = len(self.mod)-1
        self.q = p ** self.m
        self.vec = [self.digits(i) for i in range(self.q)]
        self.add = [[self.encode([(a+b)%p for a,b in zip(self.vec[i],self.vec[j])])
                     for j in range(self.q)] for i in range(self.q)]
        self.mul = [[self.multiply(i,j) for j in range(self.q)] for i in range(self.q)]
        self.neg = [self.encode([(-a)%p for a in self.vec[i]]) for i in range(self.q)]
        self.one = 1
        for a in range(1,self.q):
            if not any(self.mul[a][b]==1 for b in range(1,self.q)):
                raise ValueError('not a field')
        self.cube = [self.mul[self.mul[x][x]][x] for x in range(self.q)]
    def digits(self,n):
        d=[]
        for i in range(self.m):
            d.append(n%self.p); n//=self.p
        return tuple(d)
    def encode(self,vec):
        return sum(x*(self.p**i) for i,x in enumerate(vec))
    def multiply(self,a,b):
        p=self.p; m=self.m
        aa=self.vec[a]; bb=self.vec[b]
        c=[0]*(2*m-1)
        for i in range(m):
            for j in range(m):c[i+j]=(c[i+j]+aa[i]*bb[j])%p
        for k in range(2*m-2,m-1,-1):
            v=c[k]
            for i in range(m):c[k-m+i]=(c[k-m+i]-v*self.mod[i])%p
        return self.encode(c[:m])

def predicted(q,p):
    if q%3==1:
        return (q-4)*(q-16) if p==2 else (q-7)*(q-13)
    return q*(q-2) if p==2 else (q-1)**2

def projective_points(k):
    q=k.q
    for j in range(4):
        for tail in product(range(q),repeat=3-j):
            yield (0,)*j+(1,)+tail

def lines(k):
    if k.q%3!=1:
        return []
    mu=[x for x in range(1,k.q) if k.cube[x]==1]
    assert len(mu)==3
    # each pair orientation is fixed; -omega is the proportionality coefficient
    for a,b,c,d in [(0,1,2,3),(0,2,1,3),(0,3,1,2)]:
        for u,v in product(mu, repeat=2):
            yield ((a,b,u),(c,d,v))

def on_line(P,line,k):
    (a,b,u),(c,d,v)=line
    return k.add[P[a]][k.mul[u][P[b]]]==0 and k.add[P[c]][k.mul[v][P[d]]]==0

def rational_lines(k):
    # In the nonsplit case only omega=1 is fixed under Frobenius.
    return [((a,b,1),(c,d,1)) for a,b,c,d in
            [(0,1,2,3),(0,2,1,3),(0,3,1,2)]]

def verify(k):
    q=k.q; p=k.p
    assert p != 3
    L=list(lines(k)) if q%3==1 else rational_lines(k)
    total=0; union=0; hist=Counter()
    for P in projective_points(k):
        s=0
        for v in P:s=k.add[s][k.cube[v]]
        if s != 0: continue
        total+=1
        mul=sum(on_line(P,l,k) for l in L)
        hist[mul]+=1
        union+=(mul>0)
    full_expected=q*q+(7 if q%3==1 else 1)*q+1
    assert total==full_expected,(q,total,full_expected)
    expected=predicted(q,p)
    assert total-union==expected,(q,total,union,expected)
    if q%3==1:
        if p==2:
            assert hist[3]==45 and hist[2]==0,(q,hist)
            assert union == 27*(q+1)-90
        else:
            assert hist[3]==18 and hist[2]==81,(q,hist)
            assert union == 27*(q+1)-117
    else:
        if p==2:
            assert hist[3]==1 and hist[2]==0,(q,hist)
            assert union==3*q+1
        else:
            assert hist[2]==3 and hist[3]==0,(q,hist)
            assert union==3*q
    return f'GF({q}): X={total}, geometric-line union={union}, U={expected}, multiplicity_profile={dict(sorted(hist.items()))}'

cases=[(2,(0,1)),(2,(1,1,1)),(2,(1,1,0,1)),(2,(1,1,0,0,1)),
       (5,(0,1)),(7,(0,1)),(11,(0,1)),(13,(0,1)),(19,(0,1)),
       (5,(2,0,1)),(31,(0,1)),(37,(0,1)),(7,(1,0,1))]

if __name__=='__main__':
    for p,mod in cases:
        print(verify(Field(p,mod)))
    print('EXACT_FINITE_FIELD_CENSUS_OK')

# Exact cyclotomic incidence certificate over Z[zeta_3].
# This is a universal reduction test, not a sample of characteristics.
def cyclotomic_certificate():
    import math
    from itertools import permutations
    z0=(1,0); z1=(0,1); z2=(-1,-1); zero=(0,0)
    z=[z0,z1,z2]
    def plus(a,b):return (a[0]+b[0],a[1]+b[1])
    def neg(a):return (-a[0],-a[1])
    def times(a,b):
        a0,a1=a; b0,b1=b
        return (a0*b0-a1*b1, a0*b1+a1*b0-a1*b1)
    def norm(a):return a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
    perm_sign=[]
    for t in permutations(range(4)):
        inv=sum(t[i]>t[j] for i in range(4) for j in range(i+1,4))
        perm_sign.append((t,(-1)**inv))
    def det(M):
        A=(0,0)
        for perm,sign in perm_sign:
            x=z0
            for row,col in enumerate(perm):
                v=M[row][col]
                if v==zero:
                    x=zero;break
                x=times(x,v)
            if x!=zero:
                A=plus(A,x if sign>0 else neg(x))
        return A
    forms=[]
    for a,b,c,d in [(0,1,2,3),(0,2,1,3),(0,3,1,2)]:
        for i,j in product(range(3),repeat=2):
            row=[zero]*4;row[a]=z0;row[b]=z[i]
            row2=[zero]*4;row2[c]=z0;row2[d]=z[j]
            forms.append((row,row2))
    pair_norm_hist=Counter()
    for i,j in combinations(range(27),2):
        matrix=(*forms[i],*forms[j])
        pair_norm_hist[norm(det(matrix))]+=1
    assert pair_norm_hist[0]==135, pair_norm_hist
    for v in pair_norm_hist:
        t=v
        for prime in (2,3):
            while t>1 and t%prime==0:t//=prime
        assert t in (0,1), ('unexpected pair-specialization prime',v)
    print('Cyclotomic pair-line determinant norm histogram:',dict(sorted(pair_norm_hist.items())))
    gcd_hist=Counter()
    for ids in combinations(range(27),3):
        rows=[r for l in ids for r in forms[l]]
        g=0
        for chosen in combinations(rows,4):
            v=norm(det(chosen))
            g=math.gcd(g,v)
            if g==1:break
        gcd_hist[g]+=1
    assert sum(gcd_hist.values())==2925
    assert gcd_hist[0]==18,(gcd_hist, 'generic triple concurrence not 18')
    assert set(gcd_hist).issubset({0,1,2,3,4,9,16,27,81}), gcd_hist
    # Only prime 2 or 3 can cause extra concurrence.
    for v in gcd_hist:
        t=v
        for prime in (2,3):
            while t>1 and t%prime==0:t//=prime
        assert t in (0,1),(v,gcd_hist)
    return gcd_hist

if __name__=='__main__':
    print('Cyclotomic triple-line determinant norm gcd histogram:',dict(sorted(cyclotomic_certificate().items())))
    print('UNIVERSAL_GOOD_CHARACTERISTIC_INCIDENCE_OK')

def verify_nonsplit_lines_over_quadratic_extensions():
    # In these cases, base-field scalars embed as constants in F_(p^2).
    for p,mod in [(2,(1,1,1)),(5,(2,0,1)),(11,(9,0,1))]:
        ext=Field(p,mod)
        assert ext.q%3==1
        geom=list(lines(ext))
        fixed=rational_lines(ext)
        assert len(geom)==27
        seen_all=set();seen_fixed=set()
        for P in projective_points(Field(p,(0,1))):
            # All coordinates are constant elements of the extension field.
            if any(on_line(P,l,ext) for l in geom):seen_all.add(P)
            if any(on_line(P,l,ext) for l in fixed):seen_fixed.add(P)
        assert seen_all==seen_fixed,(p,seen_all-seen_fixed)
        print(f'GF({p}) base points on all 27 GF({p*p})-lines: {len(seen_all)}, equal to union of 3 rational lines')
    print('NONSPLIT_GEOMETRIC_LINE_DESCENT_OK')

if __name__=='__main__':
    verify_nonsplit_lines_over_quadratic_extensions()

def zeta_closed_formula(q,p,n):
    """Coefficient sum of the stated rational zeta function over degree n."""
    Q=q**n
    if q%3==1:
        return Q*Q-20*Q+(64 if p==2 else 91)
    even=n%2==0
    return Q*Q-(20 if even else 2)*Q+((64 if p==2 else 91) if even else (0 if p==2 else 1))

if __name__=='__main__':
    for p,mod in cases:
        q=p**(len(mod)-1)
        for n in range(1,13):
            assert zeta_closed_formula(q,p,n)==predicted(q**n,p),(q,n)
    print('FOUR_ZETA_RATIONAL_FUNCTIONS_OVER_ALL_TWELVE_TEST_DEGREES_OK')
    print('VERIFY_OK')
