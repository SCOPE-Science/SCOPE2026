"""Exhaustive finite-field check of a filiform Lie-algebra counting theorem.

Run: python3 verify.py
Standard library only. All computations use RREF over finite fields.
"""
import collections
import itertools

class Field:
    def __init__(self, q):
        self.q=q
        if q not in (2,3,4,5):
            raise ValueError('supported fields: 2,3,4,5')
        if q==4:
            # 0,1,a,a+1 with a^2=a+1; addition is coefficient XOR.
            self.add=lambda a,b:a^b
            def mul(a,b):
                x=((a&1)*(b&1))
                y=((a&1)*((b>>1)&1))^(((a>>1)&1)*(b&1))
                z=((a>>1)&1)*((b>>1)&1)
                return ((x^z)&1)|(((y^z)&1)<<1)
            self.mul=mul
        else:
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
        self.neg=lambda a:next(b for b in range(q) if self.add(a,b)==0)
        self.inv=lambda a:next(b for b in range(1,q) if self.mul(a,b)==1)
    def sub(self,a,b): return self.add(a,self.neg(b))

def all_subspaces(f):
    n=4; q=f.q
    for k in range(5):
        for piv in itertools.combinations(range(n),k):
            free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
            for vals in itertools.product(range(q),repeat=len(free)):
                rows=[[0]*n for _ in range(k)]
                for i,j in enumerate(piv): rows[i][j]=1
                for (i,j),v in zip(free,vals): rows[i][j]=v
                yield tuple(map(tuple,rows))

def echelon(vectors,f):
    a=[list(v) for v in vectors]
    rank=0
    for col in range(4):
        row=next((j for j in range(rank,len(a)) if a[j][col]!=0),None)
        if row is None: continue
        a[rank],a[row]=a[row],a[rank]
        c=f.inv(a[rank][col]);a[rank]=[f.mul(c,v) for v in a[rank]]
        for j in range(len(a)):
            if j==rank:continue
            factor=a[j][col]
            if factor:
                a[j]=[f.sub(x,f.mul(factor,y)) for x,y in zip(a[j],a[rank])]
        rank+=1
        if rank==len(a):break
    return tuple(tuple(row) for row in a[:rank])

def commutator(a,b,f):
    # basis x,y,z,w: [x,y]=z, [x,z]=w, all other basic brackets zero.
    return (0,0,f.sub(f.mul(a[0],b[1]),f.mul(b[0],a[1])),
                 f.sub(f.mul(a[0],b[2]),f.mul(b[0],a[2])))

def contains(u,v,f):
    return len(echelon((*u,v),f))==len(u)

def is_subalgebra(u,f):
    return all(contains(u,commutator(a,b,f),f) for a,b in itertools.combinations(u,2))

def permutes(u,v,f):
    s=echelon((*u,*v),f)
    return all(contains(s,commutator(a,b,f),f) for a in u for b in v)

def check(q):
    f=Field(q)
    # Validate every field operation before the Lie computation.
    assert f.mul(1,1)==1
    for a in range(q):
        assert f.add(a,0)==a and f.mul(a,1)==a
        for b in range(q):
            assert f.add(a,b)==f.add(b,a) and f.mul(a,b)==f.mul(b,a)
            for c in range(q):
                assert f.add(f.add(a,b),c)==f.add(a,f.add(b,c))
                assert f.mul(f.mul(a,b),c)==f.mul(a,f.mul(b,c))
                assert f.mul(a,f.add(b,c))==f.add(f.mul(a,b),f.mul(a,c))
    assert all(f.mul(a,f.inv(a))==1 for a in range(1,q))
    # Enumerate all vector subspaces, with no formula-based filtering.
    subs=[u for u in all_subspaces(f) if is_subalgebra(u,f)]
    assert len(set(subs))==len(subs)
    dim=collections.Counter(map(len,subs))
    expect_dim={0:1,1:q**3+q**2+q+1,2:2*q*q+q+1,3:q+1,4:1}
    assert dict(dim)==expect_dim, (q,dim,expect_dim)
    bad=collections.Counter()
    for a in subs:
        for b in subs:
            if not permutes(a,b,f):
                bad[(len(a),len(b))]+=1
    expected={
        (1,1):q**4*(q+1)**2,
        (1,2):q**4*(2*q+1),
        (2,1):q**4*(2*q+1),
        (2,2):q**3*(q+1),
    }
    assert dict(bad)==expected,(q,bad,expected)
    assert sum(bad.values())==q**3*(q**3+6*q*q+4*q+1)
    assert len(subs)**2-sum(bad.values())==11*q**4+27*q**3+39*q*q+30*q+25
    print('q=',q,'subalgebras=',len(subs),'dimension_counts=',dict(sorted(dim.items())),
          'nonpermuting_pairs=',dict(sorted(bad.items())),
          'permuting_pairs=',len(subs)**2-sum(bad.values()))

if __name__=='__main__':
    for q in (2,3,4,5):check(q)
    print('VERIFY_OK: all subspaces, Lie closures, and ordered permutability pairs checked for q=2,3,4,5')
