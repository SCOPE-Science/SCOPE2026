"""Independent exhaustive small-field checks of traceless product-nilpotency counts."""
from collections import Counter
from itertools import product

def field(q):
    if q in (2,3,5,7):
        p=q
        return lambda a,b:(a+b)%p, lambda a,b:(a*b)%p, lambda a: (-a)%p
    if q==4:
        # GF(2)[x]/(x^2+x+1), bitwise coordinates
        def mul(a,b):
            z=0
            if b&1:z^=a
            if b&2:z^=a<<1
            if z&8:z^=0b1110
            if z&4:z^=0b111
            return z
        return lambda a,b:a^b,mul,lambda a:a
    if q==9:
        # GF(3)[x]/(x^2+1), a=a0+3*a1
        def add(a,b):return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
        def neg(a):return (-a%3)+3*(-(a//3)%3)
        def mul(a,b):return ((a%3)*(b%3)-(a//3)*(b//3))%3+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)
        return add,mul,neg
    raise ValueError(q)

def check(q):
    add,mul,neg=field(q)
    matrices=[(a,b,c,neg(a)) for a,b,c in product(range(q),repeat=3)]
    zero=0
    def det(A):return add(mul(A[0],A[3]),neg(mul(A[1],A[2])))
    def trprod(A,B):
        return add(add(mul(A[0],B[0]),mul(A[1],B[2])),add(mul(A[2],B[1]),mul(A[3],B[3])))
    isnil=lambda A: det(A)==0 # traceless 2x2: nilpotent iff determinant zero
    def product_matrix(A,B):
        return (add(mul(A[0],B[0]),mul(A[1],B[2])),
                add(mul(A[0],B[1]),mul(A[1],B[3])),
                add(mul(A[2],B[0]),mul(A[3],B[2])),
                add(mul(A[2],B[1]),mul(A[3],B[3])))
    sq={mul(x,x) for x in range(1,q)}
    counters=Counter()
    total=zeros=0
    n_nil=sum(isnil(A) for A in matrices)
    assert n_nil==q*q,(q,n_nil)
    for A in matrices:
        d=det(A)
        if A==(0,0,0,0): kind='zero'
        elif d==0: kind='nilpotent'
        elif q%2==0:kind='scalar' if A[1]==0 and A[2]==0 else 'nonscalar'
        else:kind='split' if neg(d) in sq else 'nonsplit'
        hits=0
        for B in matrices:
            P=product_matrix(A,B)
            isprod_nil=add(P[0],P[3])==0 and det(P)==0
            predicted=trprod(A,B)==0 and (d==0 or det(B)==0)
            assert isprod_nil==predicted,(q,A,B,P)
            if isprod_nil:
                hits+=1
                total+=1
                if P==(0,0,0,0):zeros+=1
        counters[(kind,hits)]+=1
        expected={'zero':q**3,'nilpotent':q*q,'split':2*q-1,'nonsplit':1,'scalar':q*q,'nonscalar':q}[kind]
        assert hits==expected,(q,A,kind,hits,expected)
    predicted=2*q**4+q**3-3*q*q+q
    predicted_z=3*q**3-q*q-q
    assert total==predicted and zeros==predicted_z,(q,total,predicted,zeros,predicted_z)
    assert total-zeros==2*q*(q-1)*(q*q-1)
    print('q=',q,'total=',total,'zero_products=',zeros,'nonzero_nilpotent_products=',total-zeros,'classes=',sorted(counters.items()))

if __name__=='__main__':
    for q in (2,3,4,5,7,9):check(q)
    print('VERIFY_OK')
