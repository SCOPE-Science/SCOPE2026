"""Exact finite-field checks for the Ciani pencil's rational bitangents.

No external dependencies. For quadratic fields use F_p[t]/(t^2-d), with d a nonsquare.
This is verification over finite examples, not a proof of the all-prime-power theorem.
"""
from collections import Counter


class Field:
    def __init__(self,p,n=1):
        self.p,self.n,self.q=p,n,p**n
        if n==2:
            self.d=next(t for t in range(2,p) if pow(t,(p-1)//2,p)==p-1)
        elif n!=1:
            raise ValueError('only degree one and two needed for checks')
        self.squares={self.mul(x,x) for x in range(1,self.q)}
    def add(self,a,b):
        p=self.p
        if self.n==1:return (a+b)%p
        return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def neg(self,a):
        p=self.p
        if self.n==1:return (-a)%p
        return (-(a%p)%p)+p*((-(a//p))%p)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        p=self.p
        if self.n==1:return a*b%p
        a0,a1=a%p,a//p;b0,b1=b%p,b//p
        return (a0*b0+self.d*a1*b1)%p+p*((a0*b1+a1*b0)%p)
    def scale(self,n,a):return self.mul(n%self.p,a)
    def pow(self,x,n):
        z=1
        while n:
            if n&1:z=self.mul(z,x)
            x=self.mul(x,x);n>>=1
        return z
    def inv(self,a):return self.pow(a,self.q-2)
    def chi(self,a):return 0 if a==0 else (1 if a in self.squares else -1)


def binary_square_coefficients(K,A,B,C,D,E):
    """Whether A u^4+B u^3 v+C u^2 v^2+D u v^3+E v^4 is a geometric square."""
    m,sc=K.mul,K.scale
    if A:
        H=K.sub(sc(4,m(A,C)),m(B,B))
        return sc(8,m(m(A,A),D))==m(B,H) and sc(64,m(m(m(A,A),A),E))==m(H,H)
    if B:return False
    if C:return m(D,D)==sc(4,m(C,E))
    return D==0


def rational_bitangent_count(K,lam):
    m,add,sc=K.mul,K.add,K.scale
    count=0
    # Normalize last nonzero line coefficient to one.
    lines=[(a,b,1) for a in range(K.q) for b in range(K.q)]
    lines += [(a,1,0) for a in range(K.q)] + [(1,0,0)]
    for a,b,c in lines:
        if c:
            ac,bc=K.neg(m(a,K.inv(c))),K.neg(m(b,K.inv(c)))
        elif b:
            ac,bc=K.neg(m(a,K.inv(b))),0
        else:
            ac=bc=0
        A2,B2=m(ac,ac),m(bc,bc)
        A4,B4=m(A2,A2),m(B2,B2)
        cross=m(ac,bc)
        alpha=add(1,add(A4,m(lam,A2)))
        beta=sc(2,m(cross,add(sc(2,A2),lam)))
        gamma=add(sc(6,m(A2,B2)),m(lam,add(1,add(A2,B2))))
        delta=sc(2,m(cross,add(sc(2,B2),lam)))
        epsilon=add(1,add(B4,m(lam,B2)))
        count+=binary_square_coefficients(K,alpha,beta,gamma,delta,epsilon)
    return count


def expected_frequency(K):
    q,p=K.q,K.p
    eps=K.chi(K.neg(1))
    if p==3:
        n28=(q-eps-4)//4
        n16=(q-3)//2-n28
        n4=(q-1)//2
    else:
        e=K.chi(K.neg(3%p))
        n28=(q-eps-4)//4-(1+e)//2
        squareD=(q-4-e)//2
        n16=squareD-n28
        n4=q-3-squareD
    return {4:n4,16:n16,28:n28}


def run():
    cases=[(p,1) for p in [3,5,7,11,13,17,19,23,29,31]]+[(3,2),(5,2),(7,2)]
    total=0
    for p,n in cases:
        K=Field(p,n)
        prohibited={(-2)%p,(-1)%p,2%p}
        observed=Counter()
        for lam in range(K.q):
            if lam in prohibited:continue
            D=K.sub(K.neg(1),lam)
            chiD=K.chi(D)
            chiS=K.chi(K.add(lam,2%p))
            predicted=4 if chiD==-1 else (28 if chiS==1 else 16)
            actual=rational_bitangent_count(K,lam)
            assert actual==predicted,('bitangent count',p,n,lam,actual,predicted)
            observed[actual]+=1
            total+=1
        expected=expected_frequency(K)
        assert dict(observed)=={v:k for v,k in expected.items() if k},(p,n,observed,expected)
        assert sum(expected.values())==K.q-len(prohibited)
        print(f'F_{K.q}: actual frequencies 4={observed[4]}, 16={observed[16]}, 28={observed[28]}; expected={expected}')
    print(f'CIANI_BITANGENT_CLASSIFICATION_PASS total_smooth_parameters={total} finite_fields={len(cases)}')

if __name__=='__main__':run()
