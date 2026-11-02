"""Independent exact counting for rank-one two-dimensional evolution algebras."""
from itertools import product
from math import isqrt

def check(p, all_forms):
    sq={k*k%p for k in range(1,p)}
    vectors=[(i,j) for i in range(p) for j in range(p) if (i,j)!=(0,0)]
    forms=[(a,b,c) for a,b,c in product(range(p),repeat=3) if (a*c-b*b)%p]
    if not all_forms:
        # two distinct discriminant classes; every nondegenerate binary form reduces to one.
        forms=[(1,0,1),(1,0,next(c for c in range(1,p) if c not in sq))]
    checked=0
    for a,b,c in forms:
        def val(v,w):
            return (a*v[0]*w[0]+b*(v[0]*w[1]+v[1]*w[0])+c*v[1]*w[1])%p
        lines=[]
        for x,y in vectors:
            if x:
                r=(1,y*pow(x,-1,p)%p)
            else:
                r=(0,1)
            if r not in lines: lines.append(r)
        eps=sum(val(v,v)==0 for v in lines)
        assert eps in (0,2)
        assert (eps==2) == ((-((a*c-b*b)%p))%p in sq)
        basis=[]
        for v in vectors:
            for w in vectors:
                if (v[0]*w[1]-v[1]*w[0])%p and val(v,w)==0:
                    basis.append((v,w))
        assert len(basis)==(p-1)**2*(p+1-eps)
        for u in vectors:
            cnt=[0,0,0]
            for v,w in basis:
                det=(v[0]*w[1]-v[1]*w[0])%p
                x=((u[0]*w[1]-u[1]*w[0])*pow(det,-1,p))%p
                y=((v[0]*u[1]-v[1]*u[0])*pow(det,-1,p))%p
                cnt[bool(x)+bool(y)]+=1
            k1=(2*(p-1)**2 if val(u,u) else 0)
            assert cnt==[0,k1,len(basis)-k1],(p,(a,b,c),u,cnt,k1)
            checked+=1
    print('q=',p,'forms=',len(forms),'nonzero-squares=',p-1,'cases=',checked,'VERIFY_OK')
for q in (3,5,7):check(q,True)
for q in (11,13):check(q,False)
print('VERIFY_OK')
