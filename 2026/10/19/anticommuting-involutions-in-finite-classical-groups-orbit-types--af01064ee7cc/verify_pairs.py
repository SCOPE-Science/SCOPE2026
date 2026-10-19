"""Independent finite checks of anticommuting classical isometry pairs.

Run with: python verify_pairs.py
Uses only Python's standard library, including an explicit field with nine elements.
The finite tests illustrate, but do not replace, the general orbit proof.
"""
from itertools import product
from math import prod


def mult(A, B, p):
    n = len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n)) % p
                       for j in range(n)) for i in range(n))


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def negate(A, p):
    return tuple(tuple(-v % p for v in row) for row in A)


def transpose(A):
    return tuple(zip(*A))


def det_mod(A, p):
    m = [list(row) for row in A]
    n = len(m)
    ans = 1
    for j in range(n):
        pivot = next((i for i in range(j,n) if m[i][j] % p), None)
        if pivot is None:
            return 0
        if pivot != j:
            m[j], m[pivot] = m[pivot], m[j]
            ans = -ans
        x = m[j][j] % p
        ans = ans*x % p
        inv = pow(x,-1,p)
        for i in range(j+1,n):
            scale = m[i][j]*inv % p
            for k in range(j,n):
                m[i][k] = (m[i][k]-scale*m[j][k]) % p
    return ans%p


def enumerate_prime_group(n,p,B=None):
    I = identity(n)
    result = []
    for values in product(range(p),repeat=n*n):
        A=tuple(tuple(values[i*n:(i+1)*n]) for i in range(n))
        if B is None:
            if det_mod(A,p): result.append(A)
        elif mult(mult(transpose(A),B,p),A,p)==B:
            result.append(A)
    return result


def anti_count(group,p):
    I=identity(len(group[0]))
    sols=[x for x in group if mult(x,x,p)==I]
    pairs=sum(mult(s,t,p)==negate(mult(t,s,p),p)
              for s in sols for t in sols)
    return len(sols),pairs


def gl_order(n,q):
    return prod(q**n-q**j for j in range(n))


def u_order(n,q):
    return q**(n*(n-1)//2)*prod(q**i-(-1)**i for i in range(1,n+1))


def sp_order(even_dim,q):
    assert even_dim%2==0
    k=even_dim//2
    return q**(k*k)*prod(q**(2*i)-1 for i in range(1,k+1))


def o_order(dim,q,kind):
    if dim%2:
        k=dim//2
        return 2*q**(k*k)*prod(q**(2*i)-1 for i in range(1,k+1))
    k=dim//2
    assert k>=1 and kind in (+1,-1)
    return 2*q**(k*(k-1))*(q**k-kind)*prod(q**(2*i)-1 for i in range(1,k))


# F_9=F_3[a] / (a^2+1), encoded x+3*y.
def f9_add(x,y):
    return ((x%3+y%3)%3)+3*((x//3+y//3)%3)


def f9_neg(x):
    return ((-x%3)%3)+3*((-(x//3))%3)


def f9_mul(x,y):
    a,b=x%3,x//3
    c,d=y%3,y//3
    return (a*c+2*b*d)%3+3*((a*d+b*c)%3)


def f9_conj(x):
    return x%3+3*((-(x//3))%3)


def f9_matrix_mul(A,B):
    n=len(A)
    out=[]
    for i in range(n):
        row=[]
        for j in range(n):
            s=0
            for k in range(n):
                s=f9_add(s,f9_mul(A[i][k],B[k][j]))
            row.append(s)
        out.append(tuple(row))
    return tuple(out)


def f9_negmatrix(A):
    return tuple(tuple(f9_neg(x) for x in row) for row in A)


def unitary2_group():
    I=identity(2)
    result=[]
    for a,b,c,d in product(range(9),repeat=4):
        A=((a,b),(c,d))
        Astar=tuple(tuple(f9_conj(A[j][i]) for j in range(2)) for i in range(2))
        if f9_matrix_mul(Astar,A)==I:
            result.append(A)
    return result


def unitary_anti_count(group):
    I=identity(2)
    invol=[A for A in group if f9_matrix_mul(A,A)==I]
    return len(invol),sum(f9_matrix_mul(A,B)==f9_negmatrix(f9_matrix_mul(B,A))
                          for A in invol for B in invol)


def rref_planes4(p):
    result=[]
    for i in range(4):
        for j in range(i+1,4):
            allowed0=[k for k in range(i+1,4) if k!=j]
            allowed1=[k for k in range(j+1,4)]
            for values in product(range(p),repeat=len(allowed0)+len(allowed1)):
                v=[0]*4; w=[0]*4
                v[i]=1; w[j]=1
                for k,x in zip(allowed0,values[:len(allowed0)]):v[k]=x
                for k,x in zip(allowed1,values[len(allowed0):]):w[k]=x
                result.append((tuple(v),tuple(w)))
    return result


def gram_det2(basis,B,p):
    a,b=basis
    def bil(x,y):
        return sum(x[i]*B[i][j]*y[j] for i in range(4) for j in range(4))%p
    return (bil(a,a)*bil(b,b)-bil(a,b)*bil(b,a))%p


def main():
    p=3
    gl2=enumerate_prime_group(2,p)
    assert len(gl2)==gl_order(2,3)==48
    assert anti_count(gl2,p)[1]==gl_order(2,3)//gl_order(1,3)==24
    print('GL2(3): 24 anticommuting pairs; group enumeration passed')
    gl5=enumerate_prime_group(2,5)
    assert len(gl5)==gl_order(2,5)==480
    assert anti_count(gl5,5)[1]==gl_order(2,5)//gl_order(1,5)==120
    print('GL2(5): 120 anticommuting pairs; group enumeration passed')

    O2=enumerate_prime_group(2,p,identity(2))
    assert len(O2)==o_order(2,3,-1)==8
    assert anti_count(O2,p)[1]==8
    print('O(2,I_2,F3): 8 pairs; group enumeration passed')
    for field, expected_kind in ((5,+1),(7,-1)):
        small_group=enumerate_prime_group(2,field,identity(2))
        assert len(small_group)==o_order(2,field,expected_kind)
        assert anti_count(small_group,field)[1]==len(small_group)
        print(f'O(2,I_2,F{field}): {len(small_group)} pairs; group enumeration passed')

    U2=unitary2_group()
    assert len(U2)==u_order(2,3)==96
    assert unitary_anti_count(U2)[1]==u_order(2,3)//u_order(1,3)==24
    print('U2(3): 24 pairs over F9; direct enumeration passed')
    dets={f9_add(f9_mul(A[0][0],A[1][1]),f9_neg(f9_mul(A[0][1],A[1][0]))) for A in U2}
    assert len(dets)==4
    assert len({f9_mul(z,z) for z in dets})==2
    print('U2(3): determinant-image squares of index 2 verified')

    planes=rref_planes4(p)
    assert len(planes)==130
    B_orth=identity(4)
    B_symp=((0,1,0,0),(2,0,0,0),(0,0,0,1),(0,0,2,0))
    counts={+1:0,-1:0}
    symp_good=0
    for plane in planes:
        ds=gram_det2(plane,B_symp,p)
        if ds:symp_good+=1
        d=gram_det2(plane,B_orth,p)
        if d:
            kind=+1 if pow((-d)%3,(3-1)//2,3)==1 else -1
            counts[kind]+=1
    assert symp_good==sp_order(4,3)//sp_order(2,3)**2==90
    assert symp_good*sp_order(2,3)==sp_order(4,3)//sp_order(2,3)==2160
    print('Sp4(3): 90 symplectic eigenplanes, 2160 pairs (independent plane census)')

    assert counts=={+1:72,-1:18},counts
    assert sum(counts[k]*o_order(2,3,k) for k in counts)==432
    assert sum(o_order(4,3,+1)//o_order(2,3,k) for k in (+1,-1))==432
    print('O4+(3): 72 split and 18 nonsplit eigenplanes; 432 pairs')

    # Determinant-character images of diagonal stabilizers.
    assert {det_mod(A,3)**2%3 for A in gl2}=={1}
    assert gl_order(4,3)%gl_order(2,3)==0
    assert u_order(4,3)%u_order(2,3)==0
    assert o_order(4,3,+1)%o_order(2,3,+1)==0
    assert o_order(4,3,+1)%o_order(2,3,-1)==0
    assert gl_order(2,3)//gl_order(1,3)%8==0
    assert u_order(2,3)//u_order(1,3)%8==0
    assert sp_order(4,3)//sp_order(2,3)%8==0
    assert 432%8==0
    print('ALL_EXACT_CHECKS_PASSED')

if __name__=='__main__':
    main()
