"""Reproducible finite-prime-field checks for power-zero endomorphism loci.
The field tests corroborate, but do not prove, the all-primes/all-fields theorem.
"""
import itertools


def check(p, q):
    assert all(q % d for d in range(2,int(q**.5)+1))
    mon=list(itertools.product(range(p),repeat=2))
    idx={v:i for i,v in enumerate(mon)}
    basis=[i for i,v in enumerate(mon) if v!=(0,0)]
    bx=idx[(1,0)]; by=idx[(0,1)]
    mul=[(i,j,idx[(a[0]+b[0],a[1]+b[1])])
         for i,a in enumerate(mon) for j,b in enumerate(mon)
         if a[0]+b[0]<p and a[1]+b[1]<p]
    z=(0,)*len(mon)
    one=tuple(int(i==idx[(0,0)]) for i in range(len(mon)))
    def times(a,b):
        out=[0]*len(mon)
        for i,j,h in mul:out[h]=(out[h]+a[i]*b[j])%q
        return tuple(out)
    def power(a,e):
        out=one
        for _ in range(e):out=times(out,a)
        return out
    def radical_square(a):return a[bx]==a[by]==0
    def in_xA(a):return all(a[i]==0 for i,(x,y) in enumerate(mon) if x==0)
    def in_yA(a):return all(a[i]==0 for i,(x,y) in enumerate(mon) if y==0)
    def matrix_rank(cols):
        arr=[[v[i] for v in cols] for i in basis]
        r=0
        for c in range(len(cols)):
            pivot=next((j for j in range(r,len(basis)) if arr[j][c]),None)
            if pivot is None:continue
            arr[r],arr[pivot]=arr[pivot],arr[r]
            inv=pow(arr[r][c],-1,q)
            arr[r]=[(v*inv)%q for v in arr[r]]
            for j in range(len(basis)):
                if j!=r:
                    t=arr[j][c]
                    arr[j]=[(v-t*w)%q for v,w in zip(arr[j],arr[r])]
            r+=1
        return r
    actual=0
    for coeff in itertools.product(range(q),repeat=len(basis)):
        a=list(z)
        for i,c in zip(basis,coeff):a[i]=c
        a=tuple(a)
        is_zero=(power(a,p)==z)
        expected_membership=(q==p or in_xA(a) or in_yA(a) or radical_square(a))
        assert is_zero==expected_membership,(p,q,a,is_zero,expected_membership)
        actual+=is_zero
    if q==p:
        expected=q**(p*p-1)
    else:
        expected=2*q**(p*(p-1))+q**(p*p-3)-2*q**(p*(p-1)-1)
    assert actual==expected,(p,q,actual,expected)
    if q!=p:
        # The tangent map is v -> p*u^(p-1)*v.
        for u,rank in [((1,0),p-1),((0,1),p-1),((2,0),0)]:
            if u[0]>=p or u[1]>=p:continue
            v=[0]*len(mon);v[idx[u]]=1
            u_pow=power(tuple(v),p-1)
            cols=[]
            for b in basis:
                e=[0]*len(mon);e[b]=1
                w=times(u_pow,tuple(e))
                cols.append(tuple((p*w[i])%q for i in range(len(mon))))
            got=matrix_rank(cols)
            assert got==rank,(p,q,u,got,rank)
    return {'p':p,'q':q,'power_zero_elements':actual,'augmented_endomorphisms':actual**2}


if __name__=='__main__':
    for p,q in [(2,2),(2,3),(3,2),(3,3)]:
        print('CASE',check(p,q))
    print('VERIFY_OK')
