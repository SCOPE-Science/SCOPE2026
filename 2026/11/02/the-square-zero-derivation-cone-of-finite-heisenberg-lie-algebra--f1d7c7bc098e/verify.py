"""Direct finite-field checks of square-zero derivations of Heisenberg Lie algebras.

Run: python3 verify.py. Uses only Python's standard library. Counts direct
matrices satisfying Leibniz and D^2=0, independently from the formula.
"""
from itertools import product


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return a * b % q
    if not a or not b:
        return 0
    z = 0
    for i in range(2):
        for j in range(2):
            if ((a >> i) & 1) and ((b >> j) & 1):
                z ^= 1 << (i+j)
    if z & 8:
        z ^= 0b1100  # x^3 = x^2+x
    if z & 4:
        z ^= 0b111   # x^2 = x+1
    return z


def neg(a, q):
    return a if q in (2,4) else (-a) % q


def matsquare(M, q):
    n = len(M)
    return [[sum_products(((M[i][k], M[k][j]) for k in range(n)), q)
             for j in range(n)] for i in range(n)]


def sum_products(pairs, q):
    a = 0
    for x, y in pairs:
        a = add(a, mul(x, y, q), q)
    return a


def rank(M, q):
    A = [row[:] for row in M]
    n, m = len(A), len(A[0]); z = 0
    for col in range(m):
        pivot = next((i for i in range(z, n) if A[i][col]), None)
        if pivot is None:
            continue
        A[z], A[pivot] = A[pivot], A[z]
        lead = A[z][col]
        inv = next(v for v in range(1,q) if mul(lead,v,q)==1)
        A[z] = [mul(inv,t,q) for t in A[z]]
        for i in range(n):
            if i!=z and A[i][col]:
                t=A[i][col]
                A[i]=[add(x,neg(mul(t,y,q),q),q) for x,y in zip(A[i],A[z])]
        z += 1
        if z == n: break
    return z


def symplectic(v,w,r,q):
    return sum_products([(v[i],w[r+i]) for i in range(r)] +
                        [(neg(v[r+i],q),w[i]) for i in range(r)],q)


def bracket(v,w,r,q):
    return [0]*(2*r)+[symplectic(v,w,r,q)]


def column(M,j):
    return [row[j] for row in M]


def matvec(M,x,q):
    return [sum_products(zip(row,x),q) for row in M]


def is_derivation(M,r,q):
    n=2*r+1
    basis=[[int(i==j) for i in range(n)] for j in range(n)]
    columns=[column(M,j) for j in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            lhs=matvec(M,bracket(basis[i],basis[j],r,q),q)
            x=bracket(columns[i],basis[j],r,q)
            y=bracket(basis[i],columns[j],r,q)
            if lhs != [add(a,b,q) for a,b in zip(x,y)]:
                return False
    return True


def all_matrices(n,q):
    for vals in product(range(q),repeat=n*n):
        yield [list(vals[i*n:(i+1)*n]) for i in range(n)]


def nonsing_sym(j,q):
    if j==0:return 1
    S0,S1=1,q-1
    if j==1:return S1
    for n in range(2,j+1):
        S0,S1=S1,(q-1)*q**(n-1)*S1 + (q**(n-1)-1)*q**(n-1)*S0
    return S1


def isotropic_planes(r,j,q):
    num=den=1
    for i in range(j):
        num *= q**(2*r-2*i)-1
        den *= q**(j-i)-1
    assert num%den==0
    return num//den


def predicted_spectrum(r,q):
    out=[0]*(r+1)
    for j in range(r+1):
        nj=isotropic_planes(r,j,q)*nonsing_sym(j,q)
        out[j] += nj * q**j
        if j<r:
            out[j+1] += nj * (q**(2*r-j)-q**j)
    return out


def direct_small(r,q):
    n=2*r+1;count=[0]*(r+1)
    for M in all_matrices(n,q):
        if is_derivation(M,r,q) and not any(any(row) for row in matsquare(M,q)):
            count[rank(M,q)]+=1
    return count


def direct_r2_binary():
    # Enumerate every possible quotient map A and central scalar lambda;
    # these form a necessary parametrization since the center is preserved.
    r=2;q=2;n=5
    cnt=[0]*(r+1); numA=0
    for A in all_matrices(4,2):
        vals=[column(A,j) for j in range(4)]
        for lam in range(2):
            correct=True
            for i in range(4):
                for j in range(i+1,4):
                    e_i=[int(t==i) for t in range(4)]
                    e_j=[int(t==j) for t in range(4)]
                    expected=lam*symplectic(e_i,e_j,2,2)
                    calc=symplectic(vals[i],e_j,2,2)^symplectic(e_i,vals[j],2,2)
                    if expected!=calc:correct=False;break
                if not correct:break
            if not correct: continue
            numA+=1
            for f in product(range(2),repeat=4):
                D=[[A[i][j] for j in range(4)]+[0] for i in range(4)]
                D.append(list(f)+[lam])
                assert is_derivation(D,2,2)
                if not any(any(row) for row in matsquare(D,2)):
                    cnt[rank(D,2)]+=1
    return cnt,numA


def main():
    for q in (2,3,4):
        actual=direct_small(1,q)
        expected=predicted_spectrum(1,q)
        assert actual==expected,(q,actual,expected)
        print(f'Heisenberg dimension 3 over GF({q}): direct {actual} = formula {expected}')
    actual,numA=direct_r2_binary()
    expected=predicted_spectrum(2,2)
    assert actual==expected,(actual,expected)
    print(f'Heisenberg dimension 5 over GF(2): direct {actual} = formula {expected}; quotient-derivation possibilities {numA}')
    for q in (2,3,4):
        for j in (1,2,3):
            # Independently enumerate small symmetric matrices.
            c=0
            positions=[(i,k) for i in range(j) for k in range(i,j)]
            for values in product(range(q),repeat=len(positions)):
                M=[[0]*j for _ in range(j)]
                for (i,k),v in zip(positions,values): M[i][k]=M[k][i]=v
                if rank(M,q)==j:c+=1
            assert c==nonsing_sym(j,q),(q,j,c,nonsing_sym(j,q))
    print('HEISENBERG_SQZERO_DERIVATION_RANK_OK: 4 direct derivation spectra and 9 symmetric-matrix comparisons')

if __name__=='__main__':main()
