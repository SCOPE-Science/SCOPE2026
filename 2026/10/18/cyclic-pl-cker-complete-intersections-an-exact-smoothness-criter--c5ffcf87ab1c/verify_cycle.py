"""Independent finite-field checks for cyclic Pluecker sections.
No third-party library needed; this checks Jacobian ranks, proposed pointwise smoothness,
and component coverage for small finite fields. It does not prove all-size assertions.
"""
from itertools import combinations, product
from math import comb

def rank(M,p):
    a=[list(map(lambda x:x%p, row)) for row in M]
    if not a:return 0
    r=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        s=pow(a[r][c],-1,p)
        a[r]=[(x*s)%p for x in a[r]]
        for j in range(len(a)):
            if j!=r and a[j][c]:
                t=a[j][c]
                a[j]=[(u-t*v)%p for u,v in zip(a[j],a[r])]
        r+=1
        if r==len(a):break
    return r

def planes(q,n):
    for p,s in combinations(range(n),2):
        positions=[(0,j) for j in range(p+1,n) if j!=s]+[(1,j) for j in range(s+1,n)]
        for vals in product(range(q),repeat=len(positions)):
            m=[[0]*n for _ in range(2)]
            m[0][p]=1;m[1][s]=1
            for (i,j),v in zip(positions,vals):m[i][j]=v
            yield m

def det(v,w,q):return (v[0]*w[1]-v[1]*w[0])%q

def components(n):
    return [T for k in range(2,n//2+1) for T in combinations(range(n),k)
            if all(((j+1)%n not in T) for j in T)]

def on_component(vs,T,q):
    if any(vs[t]!=(0,0) for t in T):return False
    n=len(vs)
    for start in T:
        j=(start+1)%n
        if j in T: return False
        while (j+1)%n not in T:
            nxt=(j+1)%n
            if det(vs[j],vs[nxt],q):return False
            j=nxt
    return True

def point_check(m,q,Ts):
    n=len(m[0]);vs=[(m[0][i],m[1][i]) for i in range(n)]
    if any(det(vs[i],vs[(i+1)%n],q) for i in range(n)):return None
    J=[]
    for i in range(n):
        j=(i+1)%n
        row=[0]*(2*n)
        a,b=vs[i];c,d=vs[j]
        row[i]=d;row[n+i]=-c;row[j]=-b;row[n+j]=a
        J.append(row)
    actual=rank(J,q)==n
    Z={i for i,v in enumerate(vs) if v==(0,0)}
    expected=(all((z+1)%n not in Z for z in Z) and
              all(det(vs[(z-1)%n],vs[(z+1)%n],q)!=0 for z in Z))
    assert actual==expected,(n,q,m,actual,expected)
    assert any(on_component(vs,T,q) for T in Ts),(n,q,m,Z)
    return actual

def main():
    for q,n in [(2,4),(2,5),(2,6),(2,7),(3,4),(3,5),(3,6)]:
        Ts=components(n)
        total=smooth=0
        for m in planes(q,n):
            ans=point_check(m,q,Ts)
            if ans is None:continue
            total+=1;smooth+=int(ans)
        print(f'GF({q}) n={n}: |X|={total}, smooth={smooth}, components={len(Ts)}')
        assert len(Ts)==sum(n*comb(n-j-1,j-1)//j for j in range(2,n//2+1))
    print('VERIFY_OK')
if __name__=='__main__':main()
