from itertools import product
from math import gcd,lcm
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form

def count_cyclic(n,a,q):
    assert gcd(a,n)==gcd(a-1,n)==gcd(q,n)==1
    L=1
    while pow(q,L,n)!=1:L+=1
    Q=q**L-1
    unseen=set(range(n)); groups=[]
    while unseen:
        S={min(unseen)}
        while True:
            T=S|{(j*a)%n for j in S}|{(j*(1-a))%n for j in S}|{(j*q)%n for j in S}
            if S==T:break
            S=T
        unseen-=S;groups.append(sorted(S))
    total=1;results=[]
    for U in groups:
        pos={v:i for i,v in enumerate(U)}
        M=[]
        for j in U:
            row=[0]*len(U)
            row[pos[j]]+=1;row[pos[j*a%n]]-=1;row[pos[j*(1-a)%n]]-=1
            M.append(row)
            row=[0]*len(U)
            row[pos[j*q%n]]+=1;row[pos[j]]-=q
            M.append(row)
        D=smith_normal_form(Matrix(M),domain=ZZ)
        diagonal=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
        kernel=Q**(len(U)-len(diagonal))
        for d in diagonal:kernel*=gcd(d,Q)
        total*=1+kernel;results.append(dict(U=U,diag=diagonal,Q=Q,nonzero=kernel))
    return total,results

def brute(n,a,q):
    # prime q
    cnt=0
    prod_idx=[[(a*i+(1-a)*j)%n for j in range(n)] for i in range(n)]
    for v in product(range(q),repeat=n):
        u=[0]*n
        for i,x in enumerate(v):
            if not x:continue
            for j,y in enumerate(v):
                if y:u[prod_idx[i][j]]=(u[prod_idx[i][j]]+x*y)%q
        if tuple(u)==v:cnt+=1
    return cnt

if __name__=='__main__':
    cases=[(3,2,2),(3,2,5),(5,2,2),(5,2,3),(5,2,7),(5,3,2),(5,3,3),(7,2,2),(7,2,3),(7,3,2),(7,3,3),(7,4,2),(9,2,2),(9,5,2)]
    for n,a,q in cases:
        if gcd(q,n)>1:continue
        cnt,info=count_cyclic(n,a,q); got=brute(n,a,q)
        print(n,a,q,cnt,got,'OK' if cnt==got else 'BAD',info)
        assert cnt==got

def matrix_g3x3(q):
    n=3; pts=list(product(range(n),repeat=2))
    A=((0,2),(1,1));B=((1,1),(2,0))
    def primal(A,v):return tuple(sum(A[i][j]*v[j] for j in range(2))%3 for i in range(2))
    def dual(A,v):return tuple(sum(A[j][i]*v[j] for j in range(2))%3 for i in range(2))
    def F(v):return tuple(q*z%3 for z in v)
    unseen=set(pts);cnt=1
    L=1
    while pow(q,L,3)!=1:L+=1
    Q=q**L-1
    while unseen:
        W={min(unseen)}
        while 1:
            Z=W|{dual(A,x) for x in W}|{dual(B,x) for x in W}|{F(x) for x in W}
            if W==Z:break
            W=Z
        unseen-=W;U=sorted(W);ix={z:i for i,z in enumerate(U)};rows=[]
        for t in U:
            row=[0]*len(U);row[ix[t]]+=1;row[ix[dual(A,t)]]-=1;row[ix[dual(B,t)]]-=1;rows.append(row)
            row=[0]*len(U);row[ix[F(t)]]+=1;row[ix[t]]-=q;rows.append(row)
        D=smith_normal_form(Matrix(rows),domain=ZZ)
        dia=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
        c=Q**(len(U)-len(dia))
        for d in dia:c*=gcd(Q,d)
        print('2d orbit',U,'smith',dia,'count',c)
        cnt*=1+c
    brute_cnt=0
    for v in product(range(q),repeat=len(pts)):
        d=dict(zip(pts,v));out=dict.fromkeys(pts,0)
        for x in pts:
            for y in pts:
                z=tuple((a+b)%3 for a,b in zip(primal(A,x),primal(B,y)))
                out[z]=(out[z]+d[x]*d[y])%q
        brute_cnt+=(list(out.values())==list(v))
    print('non-scalar C3xC3',q,cnt,brute_cnt)
    assert cnt==brute_cnt
matrix_g3x3(2)

# Independent midpoint regression, including binary extension fields.
def midpoint_exact_count(moduli,q):
    assert all(m%2 for m in moduli) and gcd(q,__import__('math').prod(moduli))==1
    H=list(product(*(range(m) for m in moduli)))
    def perm(x,k):return tuple((k*a)%m for a,m in zip(x,moduli))
    S=set(H); orbits=[]; oid={}
    while S:
        a=min(S); cyc=[]; z=a
        while z not in cyc:
            cyc.append(z);z=perm(z,2)
        assert z==a
        i=len(orbits)
        for v in cyc:oid[v]=i;S.remove(v)
        orbits.append(cyc)
    rem=set(range(len(orbits)));ans=1;data=[]
    while rem:
        i=min(rem);cyc=orbits[i]; base=cyc[0]; f=base; seq=[]
        while oid[f] not in seq:
            j=oid[f];seq.append(j);rem.remove(j)
            f=perm(f,q)
        assert oid[f]==i
        r=len(cyc);s=len(seq);h=cyc.index(f)
        g=gcd(2**r-1, q**s-2**h)
        ans*=1+g;data.append((r,s,h,g,seq))
    return ans, data

def brute_cyclic(n,q,deg=1,poly=0):
    # represent GF(2^deg) as bit polynomials if deg>1
    p=q if deg==1 else 2
    def mul(a,b):
        if deg==1:return a*b%p
        c=0
        while b:
            if b&1:c^=a
            b>>=1;a<<=1
            if a & (1<<deg):a^=poly
        return c
    inv2=pow(2,-1,n)
    table=[[(inv2*(i+j))%n for j in range(n)] for i in range(n)]
    cnt=0
    for v in product(range(q),repeat=n):
        out=[0]*n
        for i,a in enumerate(v):
            if not a:continue
            for j,b in enumerate(v):
                if not b:continue
                k=table[i][j]
                if deg>1:out[k]^=mul(a,b)
                else:out[k]=(out[k]+a*b)%p
        cnt+= (tuple(out)==v)
    return cnt


for n,q,d,poly in [(5,4,2,0b111),(5,8,3,0b1011)]:
    expect,_=midpoint_exact_count((n,),q)
    got=brute_cyclic(n,q,d,poly)
    assert expect==got, (n,q,expect,got)
    print("midpoint extension",n,q,expect,got)
print("VERIFIED_ALL")
