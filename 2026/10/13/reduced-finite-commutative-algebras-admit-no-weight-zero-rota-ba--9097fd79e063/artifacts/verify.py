from itertools import product

def add(x,y,q):
    return tuple((a+b)%q for a,b in zip(x,y))

def scal(c,x,q):
    return tuple(c*a%q for a in x)

def mul_split(x,y,q):
    return tuple(a*b%q for a,b in zip(x,y))

def apply_matrix(M,x,q):
    n=len(M)
    return tuple(sum(M[i][j]*x[j] for j in range(n))%q for i in range(n))

def is_rb(M,q,n,mul):
    elems=list(product(range(q),repeat=n))
    for x in elems:
        Rx=apply_matrix(M,x,q)
        for y in elems:
            Ry=apply_matrix(M,y,q)
            lhs=mul(Rx,Ry,q)
            inside=add(mul(Rx,y,q),mul(x,Ry,q),q)
            rhs=apply_matrix(M,inside,q)
            if lhs!=rhs:
                return False
    return True

def all_matrices(q,n):
    for flat in product(range(q),repeat=n*n):
        yield tuple(tuple(flat[i*n+j] for j in range(n)) for i in range(n))

for q,n in [(2,1),(2,2),(2,3),(3,1),(3,2)]:
    good=[]
    for M in all_matrices(q,n):
        if is_rb(M,q,n,mul_split):
            good.append(M)
    assert len(good)==1
    assert all(all(x==0 for x in row) for row in good[0])
    print({'q':q,'n':n,'split_reduced_rb_count':len(good)})

# Dual numbers: (a,b) represents a+b*eps with eps^2=0.
def mul_dual(x,y,q):
    a,b=x; c,d=y
    return (a*c%q,(a*d+b*c)%q)

for q in (2,3,5):
    # Left multiplication by eps: a+b eps -> a eps.
    M=((0,0),(1,0))
    assert is_rb(M,q,2,mul_dual)
    assert any(M[i][j] for i in range(2) for j in range(2))
    print({'q':q,'dual_number_nonzero_rb':True})

print('VERIFY_OK')
