"""Exact finite checks for dyadic Perrin zero-surjectivity."""
from itertools import product

A=((0,1,0),(0,0,1),(1,1,0))
I=((1,0,0),(0,1,0),(0,0,1))

def mul(x,y):
    return tuple(tuple(sum(x[i][h]*y[h][j] for h in range(3)) for j in range(3)) for i in range(3))

def power(x,n):
    out=I
    while n:
        if n & 1: out=mul(out,x)
        x=mul(x,x);n//=2
    return out

def mat_sub_div(x,k):
    return tuple(tuple((x[i][j]-I[i][j])//k for j in range(3)) for i in range(3))

def mv(x,v,m):
    return tuple(sum(x[i][j]*v[j] for j in range(3))%m for i in range(3))

def det3(c):
    x=c
    return (x[0][0]*(x[1][1]*x[2][2]-x[1][2]*x[2][1])-x[0][1]*(x[1][0]*x[2][2]-x[1][2]*x[2][0])+x[0][2]*(x[1][0]*x[2][1]-x[1][1]*x[2][0]))

P7=power(A,7);B=mat_sub_div(P7,2);C=mat_sub_div(power(A,14),4)
assert P7==((1,2,2),(2,3,2),(2,4,3))
assert B==((0,1,1),(1,1,1),(1,2,1))
assert C==((2,4,3),(3,5,4),(4,7,5))
assert det3(B)%2==det3(C)%2==1
assert power(A,7)==P7
assert all((power(A,t)[0][0]%2,power(A,t)[0][1]%2,power(A,t)[0][2]%2)!=(0,0,0) for t in range(7))
assert len({tuple(c%2 for c in power(A,t)[0]) for t in range(7)})==7
for v in product(range(2),repeat=3):
    if not any(v): continue
    rows=[]
    for r in range(7):
        ar=power(A,r)
        rows.append((mv(ar,v,2)[0],mv(ar,mv(B,v,2),2)[0],mv(ar,mv(C,v,2),2)[0]))
    assert rows.count((0,1,1))==1,(v,rows)
    col=((v[0],mv(B,v,2)[0],mv(C,v,2)[0]),(v[1],mv(B,v,2)[1],mv(C,v,2)[1]),(v[2],mv(B,v,2)[2],mv(C,v,2)[2]))
    assert det3(col)%2==1

for j in range(1,10):
    x=power(A,7*(1<<j))
    assert all((x[i][h]-I[i][h])%(2**(j+1))==0 for i in range(3) for h in range(3))
    assert all(((x[i][h]-I[i][h])//(2**(j+1)))%2==C[i][h]%2 for i in range(3) for h in range(3))

counts=[]
for k in range(1,6):
    m=1<<k
    states=(v for v in product(range(m),repeat=3) if any(z&1 for z in v))
    if k==5:
        states=(v for v in product(range(m),repeat=3) if any(z&1 for z in v) and (v[0]*17+v[1]*7+v[2]*3)%293==0)
    n=0
    for v in states:
        t0=(v[0]%2,v[1]%2,v[2]%2)
        idx=[r for r in range(7) if (mv(power(A,r),t0,2)[0],mv(power(A,r),mv(B,t0,2),2)[0],mv(power(A,r),mv(C,t0,2),2)[0])==(0,1,1)]
        assert len(idx)==1
        r=idx[0]
        w=mv(power(A,r),v,m)
        seen=[]
        for t in range(m//2):
            seen.append(w[0]);w=mv(P7,w,m)
        assert sorted(seen)==list(range(0,m,2)),(k,v,r,seen)
        n+=1
    counts.append((k,n))
print('VERIFY_OK: exact A^7 and A^14 matrices; seven mod-two classes; ten 2-adic matrix lift levels; even-residue bijection for',counts)
