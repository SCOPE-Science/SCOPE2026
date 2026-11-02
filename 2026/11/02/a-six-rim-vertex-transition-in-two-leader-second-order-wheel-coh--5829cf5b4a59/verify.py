"""Exact rational verification of the finite base cases in the wheel leader theorem.
No external dependencies; execute with Python >=3.8.
"""
from fractions import Fraction as F
from itertools import combinations

def wheel_laplacian(n):
    z = [[F(0) for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for a,b in ((0,i+1),(i+1,1+(i+1)%n)):
            z[a][a] += 1; z[b][b] += 1
            z[a][b] -= 1; z[b][a] -= 1
    return z

def inverse(a):
    n=len(a)
    m=[list(map(F,row))+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        p=next(i for i in range(j,n) if m[i][j])
        m[j],m[p]=m[p],m[j]
        t=m[j][j]; m[j]=[v/t for v in m[j]]
        for i in range(n):
            if i!=j:
                t=m[i][j]
                if t:m[i]=[v-t*w for v,w in zip(m[i],m[j])]
    return [row[n:] for row in m]

def costs(L,leaders):
    f=[i for i in range(len(L)) if i not in leaders]
    g=inverse([[L[i][j] for j in f] for i in f])
    return sum(g[i][i] for i in range(len(g))),sum(g[i][j]**2 for i in range(len(g)) for j in range(len(g)))

def block_cost(n,d):
    # Two paths: rim gaps of lengths d-1 and n-d-1, plus central hub.
    m=n-2
    block=[[F(0) for _ in range(m)] for _ in range(m)]
    lengths=(d-1,n-d-1); shift=0
    for l in lengths:
        for i in range(l):
            block[shift+i][shift+i]=F(3)
            if i+1<l:
                block[shift+i][shift+i+1]=block[shift+i+1][shift+i]=F(-1)
        shift+=l
    g=inverse(block)
    u=[sum(row) for row in g]
    S=F(n)-sum(u)
    s=1/S
    t2=sum(g[i][j]**2 for i in range(m) for j in range(m))
    z=sum(u[i]*g[i][j]*u[j] for i in range(m) for j in range(m))
    norm=sum(v*v for v in u)
    return t2+2*s*z+s*s*(1+norm)**2

def main():
    total=0
    print('n | hub inverse-square | optimal rim inverse-square | all rim-distance costs | optimal leader count')
    for n in range(3,11):
        L=wheel_laplacian(n)
        hub=costs(L,{0,1})
        rim=[costs(L,{1,1+d}) for d in range(1,n//2+1)]
        for d,t in enumerate(rim,1):
            assert t[1]==block_cost(n,d)
        typ='all' if n==3 else ('rim' if n in (4,5) else 'hub')
        best=min([hub[1]]+[x[1] for x in rim])
        expected={3:6,4:2,5:5}.get(n,n)
        winners=0
        for p in combinations(range(n+1),2):
            c=costs(L,set(p))
            if c[1]==best:winners+=1
            if typ=='hub' and (0 in p)!=(c[1]==best):raise AssertionError((n,p))
            if typ=='rim' and (0 not in p and min((p[1]-p[0])%n, n-(p[1]-p[0])%n)==n//2)!=(c[1]==best):
                # p are rim indices, their difference equals cyclic separation.
                raise AssertionError((n,p))
            if typ=='all' and c[1]!=best:raise AssertionError((n,p))
            total+=1
        assert winners==expected,(n,winners,expected)
        if n==6:
            assert hub[1]==F(157,144) and rim[2][1]==F(9,8)
            assert hub[0]==F(25,12) and rim[2][0]==F(2)
        print(n,'|',hub[1],'|',min(t[1] for t in rim),'|',','.join(str(t[1]) for t in rim),'|',winners)
    # Infinite-tail bounds are exact inequalities based on (20)^2 < (9)^2*5.
    assert 400<405
    assert F(27,100)<F(10,36)
    print('BASE_CASES_OK; direct leader-pair inverses=',total)
    print('TAIL_CERTIFICATE_OK: 3/(5sqrt5)<27/100<10/36')

if __name__=='__main__':main()
