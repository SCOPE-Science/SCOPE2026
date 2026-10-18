"""Exact finite-field checks for Peirce incidence of 2-by-2 symmetric Jordan matrices.

All arithmetic is integer arithmetic modulo p (for GF(p)) or polynomial
arithmetic modulo X^2-d (for GF(p^2)), with d a nonsquare in GF(p).
This is illustrative finite checking; the general statement has an algebraic proof.
"""
from collections import Counter
from itertools import product


class Field:
    def __init__(self, p, d=None):
        self.p = p
        self.d = d
        self.q = p if d is None else p*p
        if d is not None:
            assert pow(d, (p-1)//2, p) == p-1
        self.add = [[0]*self.q for _ in range(self.q)]
        self.mul = [[0]*self.q for _ in range(self.q)]
        for a in range(self.q):
            for b in range(self.q):
                if d is None:
                    self.add[a][b] = (a+b)%p
                    self.mul[a][b] = (a*b)%p
                else:
                    aa,ab = a%p,a//p
                    ba,bb = b%p,b//p
                    self.add[a][b] = ((aa+ba)%p) + p*((ab+bb)%p)
                    self.mul[a][b] = ((aa*ba + d*ab*bb)%p) + p*((aa*bb+ab*ba)%p)
        self.zero = 0
        self.one = 1
        self.two = 2
        self.inv2 = next(a for a in range(self.q) if self.mul[a][2]==1)
        self.neg = [next(b for b in range(self.q) if self.add[a][b]==0) for a in range(self.q)]
        self.squares={self.mul[a][a] for a in range(self.q)}
        self.chi_neg_one = 1 if self.neg[1] in self.squares else -1

    def plus(self,*x):
        out=0
        for a in x:out=self.add[out][a]
        return out

    def times(self,*x):
        out=1
        for a in x:out=self.mul[out][a]
        return out


def jordan(f,a,b):
    x,y,z=a;u,v,w=b
    return (f.plus(f.times(x,u),f.times(y,v)),
            f.times(f.inv2,f.plus(f.times(x,v),f.times(y,w),f.times(u,y),f.times(v,z))),
            f.plus(f.times(z,w),f.times(y,v)))


def expected(f):
    q=f.q
    if f.chi_neg_one==-1:
        return {0:q*(q-1)**2//2,
                1:q*q-1,
                2:q*(q*q-1)//2,
                q+1:1}
    return {0:(q**3-2*q*q+7*q-6)//2,
            1:3*(q-1)**2,
            2:(q-1)**2*(q-2)//2,
            q-1:1}


def check(f, exhaustive_word=False):
    q=f.q
    els=list(product(range(q),repeat=3))
    E=[a for a in els if jordan(f,a,a)==a]
    zero=(0,0,0); unit=(1,0,1)
    prim=[a for a in E if a not in (zero,unit)]
    # Calculate rank of L_P by direct enumeration of its image for each P.
    # Exactly one linear constraint describes each rank-two image.
    H=[]
    for p in prim:
        image={jordan(f,p,a) for a in els}
        assert len(image)==q*q,(q,p,len(image))
        H.append(image)
    cnt=Counter(sum(a in img for img in H) for a in els)
    assert dict(cnt)==expected(f),(q,cnt,expected(f))
    assert len(prim)==q-f.chi_neg_one
    assert sum(cnt.values())==q**3
    # Character calculation for arbitrary aI+v predicts exact individual incidence.
    for X in els:
        x,y,z=X
        a=f.times(f.inv2,f.plus(x,z))
        u=f.times(f.inv2,f.plus(x,f.neg[z]))
        vv=y
        Q=f.plus(f.times(u,u),f.times(vv,vv))
        det=f.plus(f.times(x,z),f.neg[f.times(y,y)])
        if X==zero: predicted=len(prim)
        elif u==0 and vv==0:predicted=0
        elif Q!=0:
            ndet=f.neg[det]
            predicted=1 if ndet==0 else 2 if ndet in f.squares else 0
        else:predicted=1 if a!=0 else 0
        assert cnt[predicted]>=0
        # avoid rebuilding potentially many image sets unnecessarily
        actual=sum(X in h for h in H)
        assert actual==predicted,(q,X,actual,predicted)
    reach=None
    if exhaustive_word:
        seen=set(E);front=set(E)
        while front:
            nxt={jordan(f,x,p) for x in front for p in E}-seen
            seen.update(nxt);front=nxt
        reach=len(seen)
        allowed=q**3-cnt[0]+1 # include scalar identity
        assert reach<=allowed
    print('q=%d, chi(-1)=%+d, primitive=%d, incidence=%s, word_reachable=%s' %
          (q,f.chi_neg_one,len(prim),str(dict(sorted(cnt.items()))),str(reach)))


if __name__=='__main__':
    for p in (3,5,7,11,13): check(Field(p),exhaustive_word=(p in (3,5,7)))
    check(Field(3,2),exhaustive_word=True) # GF(9) = GF(3)[X]/(X^2-2)
