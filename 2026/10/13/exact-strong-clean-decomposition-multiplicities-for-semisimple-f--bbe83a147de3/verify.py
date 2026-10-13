from itertools import product


def matmul(A,B,q):
    n=len(A); m=len(B[0]); t=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(t))%q for j in range(m)] for i in range(n)]

def matsub(A,B,q):
    return [[(a-b)%q for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]

def eye(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def rank(A,q):
    M=[row[:] for row in A]
    nr=len(M); nc=len(M[0]) if nr else 0
    r=0
    for c in range(nc):
        piv=next((i for i in range(r,nr) if M[i][c]%q),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        inv=pow(M[r][c],-1,q)
        M[r]=[(x*inv)%q for x in M[r]]
        for i in range(nr):
            if i!=r and M[i][c]%q:
                f=M[i][c]%q
                M[i]=[(x-f*y)%q for x,y in zip(M[i],M[r])]
        r+=1
        if r==nr: break
    return r

def all_mats(n,q):
    for vals in product(range(q), repeat=n*n):
        yield [list(vals[i*n:(i+1)*n]) for i in range(n)]

def strong_count(A,q):
    n=len(A); I=eye(n); z=0
    for E in all_mats(n,q):
        if matmul(E,E,q)!=E: continue
        if matmul(E,A,q)!=matmul(A,E,q): continue
        if rank(matsub(A,E,q),q)==n:
            z+=1
    return z

def block_diag(*blocks):
    n=sum(len(B) for B in blocks)
    A=[[0]*n for _ in range(n)]
    off=0
    for B in blocks:
        for i,row in enumerate(B):
            for j,x in enumerate(row): A[off+i][off+j]=x
        off+=len(B)
    return A

def gaussian(m,k,Q):
    if k<0 or k>m: return 0
    num=den=1
    for i in range(k):
        num*=Q**(m-i)-1
        den*=Q**(k-i)-1
    return num//den

def H(Q,m):
    return sum(gaussian(m,k,Q)*Q**(k*(m-k)) for k in range(m+1))

assert H(3,2)==14
assert H(5,2)==32
assert H(4,2)==22
assert strong_count([[2,0],[0,2]],3)==14
assert strong_count([[2,0],[0,2]],5)==32
assert strong_count([[0,0],[0,2]],3)==2
assert strong_count([[0,0],[0,1]],3)==1
C=[[0,1],[1,1]]
assert strong_count(C,2)==2
A4=block_diag(C,C)
assert strong_count(A4,2)==22
A_mix=block_diag([[0]],[[1]],C)
assert strong_count(A_mix,2)==2

# Independent idempotent count in M_2(F_4), with F_4=F_2[a]/(a^2+a+1).
def f4_add(x,y): return x^y
def f4_mul(x,y):
    # bits encode c0+c1*a; a^2=a+1
    a0=x&1; a1=(x>>1)&1; b0=y&1; b1=(y>>1)&1
    c0=(a0*b0)^(a1*b1)
    c1=(a0*b1)^(a1*b0)^(a1*b1)
    return c0 | (c1<<1)
def mm2_f4(A,B):
    return [[f4_add(f4_mul(A[i][0],B[0][j]),f4_mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
count=0
for vals in product(range(4), repeat=4):
    E=[list(vals[:2]),list(vals[2:])]
    if mm2_f4(E,E)==E: count+=1
assert count==22
print('VERIFY_OK')
print('H_3(2)=14 H_5(2)=32 H_4(2)=22')
print('semisimple representative strong-clean counts verified')
