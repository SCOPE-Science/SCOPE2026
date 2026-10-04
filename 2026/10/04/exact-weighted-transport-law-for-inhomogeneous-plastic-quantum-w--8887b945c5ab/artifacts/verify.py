import math


def zeros(n):
    return [[0j for _ in range(n)] for _ in range(n)]


def eye(n):
    A=zeros(n)
    for i in range(n):
        A[i][i]=1.0
    return A


def mm(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    C=zeros(n)
    if m != n:
        C=[[0j for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for t in range(k):
            z=A[i][t]
            if z:
                for j in range(m):
                    C[i][j]+=z*B[t][j]
    return C


def adj(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]


def sub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mv(A,v):
    return [sum(a*z for a,z in zip(row,v)) for row in A]


def norm(v):
    return math.sqrt(sum((z.conjugate()*z).real for z in v))


def opnorm(A):
    B=mm(adj(A),A)
    n=len(B)
    v=[complex(1.0+0.031*i,0.017*(i+1)) for i in range(n)]
    q=norm(v); v=[z/q for z in v]
    for _ in range(500):
        w=mv(B,v); q=norm(w)
        if q==0: return 0.0
        v=[z/q for z in w]
    lam=sum((v[i].conjugate()*mv(B,v)[i]).real for i in range(n))
    return math.sqrt(max(0.0,lam))


def coin(b):
    s=math.sqrt(1.0-b*b)
    return [[-b,s],[s,b]]


def lam(b):
    fp=math.sqrt(1.0-b)+math.sqrt(1.0+b)
    fm=math.sqrt(1.0-b)-math.sqrt(1.0+b)
    return [[-0.5*fm,0.5*fp],[0.5*fp,0.5*fm]]


def setblock(A,x,B):
    A[2*x][2*x]=B[0][0]; A[2*x][2*x+1]=B[0][1]
    A[2*x+1][2*x]=B[1][0]; A[2*x+1][2*x+1]=B[1][1]


def walk(bs):
    L=len(bs); n=2*L
    C=zeros(n); La=zeros(n); S=zeros(n)
    for x,b in enumerate(bs):
        setblock(C,x,coin(b)); setblock(La,x,lam(b))
        S[2*((x+1)%L)][2*x]=1.0
        S[2*((x-1)%L)+1][2*x+1]=1.0
    return mm(mm(mm(mm(mm(adj(La),S),C),S),C),La)


def diag_a(a):
    n=2*len(a); A=zeros(n)
    for x,z in enumerate(a):
        A[2*x][2*x]=z; A[2*x+1][2*x+1]=z
    return A


def check_instance(bs,a,tol=2e-8):
    W=walk(bs); A=diag_a(a)
    comm=sub(mm(W,A),mm(A,W))
    observed=opnorm(comm)
    L=len(bs)
    predicted=max(bs[(x+1)%L]*abs(a[(x+2)%L]-a[x]) for x in range(L))
    if abs(observed-predicted)>tol*max(1.0,predicted):
        raise AssertionError((observed,predicted))


def cycle_distance(bs,eps,start,target):
    L=len(bs); total=0.0; x=start
    while x!=target:
        total+=2.0*eps/bs[(x+1)%L]
        x=(x+2)%L
    cyc=sum(2.0*eps/bs[(x+1)%L] for x in range(start%2,L,2))
    return min(total,cyc-total)


def main():
    instances=[
        ([0.31,0.52,0.73,0.44,0.67,0.28,0.81,0.59],[0.2,-0.4,1.3,0.7,-0.9,0.5,1.1,-0.2]),
        ([0.62,0.35,0.84,0.57,0.48,0.76,0.29,0.68,0.41,0.53],[0.0,0.4,-0.2,1.1,0.6,-0.7,0.3,1.4,-0.5,0.2]),
    ]
    for bs,a in instances: check_instance(bs,a)
    b=0.7; eps=1.0
    if abs((2*eps/b)*3-eps*6/b)>1e-14: raise AssertionError('homogeneous reduction')
    bs=instances[0][0]
    d=cycle_distance(bs,1.0,0,4)
    forward=2/bs[1]+2/bs[3]
    backward=2/bs[5]+2/bs[7]
    if abs(d-min(forward,backward))>1e-14: raise AssertionError('cycle metric')
    print('VERIFY_OK')


if __name__=='__main__':
    main()
