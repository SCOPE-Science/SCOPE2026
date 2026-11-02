"""Exhaustive ordered-pair one-point extension check for scalar affine quasigroups.
Only the Python standard library is required. The source mathematical statement
is in RESULT.md; this program checks finite test instances, not the universal proof.
"""
from itertools import product, permutations

class Field:
    def __init__(self, p, poly=None):
        self.p=p; self.poly=poly or [0,1]; self.e=len(self.poly)-1; self.q=p**self.e
        assert self.poly[-1] == 1
    def digits(self,x):
        return [(x//(self.p**i))%self.p for i in range(self.e)]
    def encode(self,ds):
        return sum((a%self.p)*self.p**i for i,a in enumerate(ds))
    def add(self,a,b):
        return self.encode([(x+y)%self.p for x,y in zip(self.digits(a),self.digits(b))])
    def neg(self,a): return self.encode([-x for x in self.digits(a)])
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        da=self.digits(a);db=self.digits(b);out=[0]*(2*self.e-1)
        for i,x in enumerate(da):
            for j,y in enumerate(db): out[i+j]=(out[i+j]+x*y)%self.p
        for i in range(2*self.e-2,self.e-1,-1):
            c=out[i]
            for j in range(self.e):out[i-self.e+j]=(out[i-self.e+j]-c*self.poly[j])%self.p
        return self.encode(out[:self.e])
    def pow(self,a,n):
        ret=1
        while n:
            if n&1:ret=self.mul(ret,a)
            a=self.mul(a,a);n//=2
        return ret
    def inv(self,a):
        assert a!=0
        z=self.pow(a,self.q-2)
        assert self.mul(z,a)==1
        return z

def model(q,t,d=1):
    specs={4:(2,[1,1,1]),8:(2,[1,1,0,1]),9:(3,[1,0,1]),16:(2,[1,1,0,0,1]),25:(5,[2,0,1])}
    f=Field(*specs[q]) if q in specs else Field(q)
    assert 0<t<q and t!=1 and d>=1
    xs=list(product(range(q),repeat=d))
    def op(x,y):
        return tuple(f.add(f.mul(f.sub(1,t),xi),f.mul(t,yi)) for xi,yi in zip(x,y))
    def R(x,y,z):return op(x,y)==z
    perms=list(permutations(range(3)))
    def mask(x,y,z):
        w=[x,y,z]
        return sum((1<<i) for i,perm in enumerate(perms) if R(w[perm[0]],w[perm[1]],w[perm[2]]))
    profiles=set()
    full=0
    for x in xs:
        for y in xs:
            if x==y:continue
            counts={}
            for z in xs:
                if z in (x,y):continue
                m=mask(x,y,z)
                counts[m]=counts.get(m,0)+1
            profile=frozenset(counts)
            profiles.add(profile);full+=1
    assert len(profiles)==1, (q,t,d,len(profiles))
    assert len(next(iter(profiles)))>=1
    masks=next(iter(profiles))
    # Unique positive masks and their multiplicities for the canonical pair.
    x,y=xs[0],xs[1]
    positive={mask(x,y,z):0 for z in xs if z not in (x,y) and mask(x,y,z)}
    for z in xs:
        if z not in (x,y) and mask(x,y,z):positive[mask(x,y,z)]+=1
    assert all(v==1 for v in positive.values()),(q,t,d,positive)
    absent=any(mask(x,y,z)==0 for z in xs if z not in (x,y))
    return (tuple(sorted(positive)), absent),full

cases=[
 ('triple3-small',3,2,1),('triple3-large',3,2,2),
 ('half-small',5,3,1),('half-large',7,4,1),
 ('twice-small',5,2,1),('twice-large',7,2,1),
 ('minus-small',5,4,1),('minus-large',7,6,1),
 ('equianharmonic-small',4,2,1),('equianharmonic-large',7,3,1),
 ('generic-small',8,2,1),('generic-large',9,3,1),
 ('generic-prime11',11,4,1),('generic-prime13',13,3,1),
 ('equianharmonic-second',7,5,1),('harmonic-dimension2',5,3,2),
 ('generic-9-alternative',9,4,1),('equianharmonic-16',16,6,1)
]
if __name__=='__main__':
    out={};pairs=0
    for name,q,t,d in cases:
        sig,n=model(q,t,d);pairs+=n
        print(f'{name:<27} q={q:<2} t={t:<2} d={d} n={q**d:<3} signature={sig}')
        out[name]=sig
    assert len({out[name] for name,*_ in cases[:12]})==12
    assert out['generic-small'][0]==out['generic-large'][0] and out['generic-small'][1]!=out['generic-large'][1]
    assert out['equianharmonic-large']==out['equianharmonic-second']
    assert out['half-large']==out['harmonic-dimension2']
    assert out['generic-large']==out['generic-prime11']==out['generic-prime13']==out['generic-9-alternative']
    print(f'PASS: 12 distinct classes, {pairs} ordered-pair extension profiles checked')
