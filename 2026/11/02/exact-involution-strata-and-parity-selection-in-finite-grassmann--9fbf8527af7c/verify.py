"""Finite exterior-product checks for involution enumerator; ordinary verifier only."""
import itertools
from math import prod

def gaussian(n,k,q):
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den

def strata(n,q):
    h=2**(n-1)
    u=(n+1)*h-n*n-(n%2)
    z=[]
    for b in range(n+1):
        a=n-b
        op=h if b==0 else 0 if b==n else 2**(n-2)
        om=h-op
        f=op-(int(n%2==1 and b%2==0))+a*(op-a)+b*(om-b)
        assert 0<=f<=u
        z.append(gaussian(n,b,q)*q**(b*a+u-f))
    return z

def algebra(q,n):
    def mul(A,B):
        C={}
        for a,x in A.items():
            for b,y in B.items():
                if a&b:continue
                inv=sum((b&((1<<i)-1)).bit_count() for i in range(n) if a>>i&1)
                m=a|b
                C[m]=(C.get(m,0)+x*y*(-1 if inv%2 else 1))%q
        return {a:x for a,x in C.items() if x%q}
    def add(A,B):
        C=dict(A)
        for k,x in B.items():C[k]=(C.get(k,0)+x)%q
        return {k:x for k,x in C.items() if x%q}
    def sc(c,A):return {i:c*v%q for i,v in A.items() if c*v%q}
    def compose(P,Y):
        ans={}
        for m,c in P.items():
            p={0:c}
            for i in range(n):
                if m>>i&1:p=mul(p,Y[i])
            ans=add(ans,p)
        return ans
    return mul,add,sc,compose

def direct_n2(q):
    n=2
    mul,add,sc,compose=algebra(q,n)
    counts=[0]*3
    for a,b,c,d in itertools.product(range(q),repeat=4):
        det=(a*d-b*c)%q
        if not det:continue
        tr=(a+d)%q
        if (a+d)%q or (a*d-b*c)%q!=(-1)%q:
            # Ignore: this is not the test for involution; still enumerate.
            pass
        for z,w in itertools.product(range(q),repeat=2):
            Y=[{1:a,2:b,3:z},{1:c,2:d,3:w}]
            Y=[{k:v for k,v in p.items() if v%q} for p in Y]
            if all(compose(Y[i],Y)=={1<<i:1} for i in range(2)):
                neg=0 if (a,d,b,c)==(1,1,0,0) else 2 if (a,d,b,c)==((q-1),(q-1),0,0) else 1
                counts[neg]+=1
    assert counts==strata(2,q),(counts,strata(2,q))
    return counts

def direct_n3_diagonal(q=3):
    n=3;mul,add,sc,compose=algebra(q,n)
    seen=[]
    for b in range(4):
        diag=[-1 if i>=n-b else 1 for i in range(n)]
        total=0
        for av,cv in itertools.product(itertools.product(range(q),repeat=n),repeat=2):
            A={1<<i:v for i,v in enumerate(av) if v}
            Y=[add(add({1<<i:diag[i]%q},sc(2*diag[i],mul(A,{1<<i:1}))),sc(diag[i]*cv[i],{7:1})) for i in range(n)]
            if all(compose(Y[i],Y)=={1<<i:1} for i in range(n)):
                total+=1
        h=2**(n-1);u=(n+1)*h-n*n-1; a=n-b
        op=h if b==0 else 0 if b==n else 2**(n-2)
        f=op-int(b%2==0)+a*(op-a)+b*(h-op-b)
        expected=q**(u-f)
        assert total==expected,(q,b,total,expected)
        seen.append(total)
    return seen

def symbolic():
    for n in range(2,15):
        h=2**(n-1)
        u=(n+1)*h-n*n-(n%2)
        for b in range(n+1):
            a=n-b
            op=h if b==0 else 0 if b==n else 2**(n-2)
            f=op-int(n%2==1 and b%2==0)+a*(op-a)+b*(h-op-b)
            if b==0:assert u==f
            if b==n:assert u-f==h-(n%2)
            if 0<b<n:
                exponent=b*a+u-f+b*a
                expected=(n+1)*2**(n-2)+int(n%2==1 and b%2==0)-(n%2)
                assert exponent==expected
        assert sum(strata(n,3))>0
    return True

if __name__=='__main__':
    print('N2_EXHAUSTIVE',[(q,direct_n2(q)) for q in (3,5)])
    print('N3_DIAGONAL_LIFTS',direct_n3_diagonal(3))
    print('SYMBOLIC_2_TO_14',symbolic())
    print('VERIFY_OK')
