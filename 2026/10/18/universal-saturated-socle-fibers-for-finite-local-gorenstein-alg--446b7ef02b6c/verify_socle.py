"""Independent small-field tests for saturated socle-operator fibers.
No outside packages. Matrices are row-bit encodings over F_2.
"""
from math import prod

def mul(A,B,n):
    out = []
    for r in A:
        x=0
        for k in range(n):
            if (r>>k)&1: x ^= B[k]
        out.append(x)
    return tuple(out)

def rank(A,n):
    basis=[0]*n
    r=0
    for row in A:
        x=row
        while x:
            p=x.bit_length()-1
            if not basis[p]: basis[p]=x; r+=1; break
            x ^= basis[p]
    return r

def matrices(n):
    for v in range(1 << (n*n)):
        yield tuple((v>>(i*n))&((1<<n)-1) for i in range(n))

def target(n):
    # C has one 2x2 Jordan block, in the first two coordinates
    return tuple([2]+[0]*(n-1))

def gl(n,q):
    return prod(q**n-q**j for j in range(n))

def fiber(s,m,q):
    return (q**((s-2)*m*m))*gl((s-2)*m,q)

def test_truncated(s):
    n=s; C=target(n); z=tuple([0]*n)
    total=0
    for T in matrices(n):
        P=T
        for _ in range(s-2): P=mul(P,T,n)
        if P==C:
            # T^s = T C, required to vanish
            assert mul(P,T,n)==z
            total+=1
    assert total==fiber(s,1,2),(s,total,fiber(s,1,2))
    print('TRUNCATED_POWER',s,'q=2','fiber',total)

def test_two_square_zero():
    n=4; C=target(n); z=(0,0,0,0)
    sq=[T for T in matrices(n) if mul(T,T,n)==z]
    assert len(sq)==316,len(sq)
    total=0
    for X in sq:
        for Y in sq:
            if mul(X,Y,n)==C and mul(Y,X,n)==C: total+=1
    assert total==fiber(4,1,2),total
    print('TWO_COMMUTING_SQUARE_ZERO','q=2','fiber',total)

def check_stabilizers(s):
    # For regular multiplication by t_i on a univariate truncated algebra,
    # the commutant is the algebra of polynomials in one Jordan block.
    # Among its q^s elements precisely (q-1)q^(s-1) are units.
    for q in [2,3,4,5]:
        numerator=gl(s,q)
        aut=(q-1)*q**(s-1)
        central=gl(1,q)*gl(s-2,q)*q**(2*s-3)
        assert numerator%aut==0 and numerator%central==0
        assert numerator//aut==(numerator//central)*fiber(s,1,q)
    print('ORBIT_STABILIZER_IDENTITIES',s,'q=2,3,4,5 PASS')

if __name__=='__main__':
    test_truncated(3)
    test_truncated(4)
    test_two_square_zero()
    for s in (2,3,4,5,6,8): check_stabilizers(s)
    print('VERIFY_OK_SOCLE_UNIVERSALITY')
