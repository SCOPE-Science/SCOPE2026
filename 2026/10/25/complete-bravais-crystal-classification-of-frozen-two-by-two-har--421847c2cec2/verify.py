from itertools import product

def crystal(N, u, v):
    return {((a*u[0]+b*v[0])%N,(a*u[1]+b*v[1])%N) for a,b in product(range(N),repeat=2)}

def check(N,u,v,index):
    C=crystal(N,u,v)
    assert len(C)==N*N//index, (N,u,v,len(C))
    for x,y in C:
        for a,b in product((-1,0,1),repeat=2):
            if (a,b)!=(0,0): assert ((x+a)%N,(y+b)%N) not in C
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            X,Y=(x+dx)%N,(y+dy)%N
            assert any(((X+i)%N,(Y+j)%N) in C for i,j in product((-1,0,1),repeat=2) if ((X+i)%N,(Y+j)%N)!=(x,y)), (N,u,v,x,y,dx,dy)
    return len(C)

cases=[((2,0),(0,2),4),((2,1),(0,2),4),((2,0),(1,2),4),((2,1),(-1,2),5),((2,-1),(1,2),5)]
for u,v,k in cases:
    for N in ((4,8,12,20) if k==4 else (5,10,15,20)):
        print('PASS',N,u,v,k,check(N,u,v,k))
