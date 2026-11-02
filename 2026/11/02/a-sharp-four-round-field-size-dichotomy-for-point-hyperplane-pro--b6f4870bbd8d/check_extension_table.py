"""Reproduce the three-point incidence-extension table in projective dimension three."""
from itertools import product

def gf(q):
    def mul(a,b):
        if q != 4:
            return a*b%q
        k=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1): k ^= 1 << (i+j)
        return k ^ 7 if (k & 4) else k
    def add(a,b): return a^b if q==4 else (a+b)%q
    def inverse(a): return next(b for b in range(1,q) if mul(a,b)==1)
    return mul,add,inverse

def projective_points(q,m=4):
    mul,add,inv=gf(q)
    out=set()
    for v in product(range(q),repeat=m):
        if not any(v): continue
        w=next(x for x in v if x)
        out.add(tuple(mul(x,inv(w)) for x in v))
    return sorted(out)

def run(q):
    mul,add,_=gf(q)
    v=projective_points(q)
    zero=(0,)*4
    e1=(1,0,0,0); e2=(0,1,0,0); e3=(0,0,1,0)
    col=tuple(x for x in v if x[2:]==(0,0))[:3]
    assert len(col)==3 and e1 in col and e2 in col
    indep=(e1,e2,e3)
    def dot(a,b):
        r=0
        for x,y in zip(a,b):r=add(r,mul(x,y))
        return r
    def patterns(triple):
        return {sum((1<<i) for i,x in enumerate(triple) if dot(h,x)==0) for h in v}
    got_col=patterns(col)
    got_ind=patterns(indep)
    assert got_col==({1,2,4,7} if q==2 else {0,1,2,4,7}), (q,got_col)
    assert got_ind==set(range(8)), (q,got_ind)
    print(f'EXTENSION_TABLE_OK q={q} points={len(v)} dependent={sorted(got_col)} independent={sorted(got_ind)}')

if __name__=='__main__':
    for q in [2,3,4,5]:run(q)
    print('EXTENSION_VERIFY_OK')
