"""Reproducibility checks for Jordan derivations of diamond incidence radicals.

Run with Python 3.9+; no dependencies.
"""
from itertools import product


def rank_mod_p(rows, p, width):
    pivots = {}
    for row in rows:
        x = [a % p for a in row]
        for j in range(width):
            if x[j] == 0:
                continue
            if j in pivots:
                factor = x[j]
                y = pivots[j]
                x = [(a - factor * b) % p for a, b in zip(x, y)]
            else:
                inv = pow(x[j], -1, p)
                pivots[j] = [(inv * a) % p for a in x]
                break
    return len(pivots)


def product_basis(r, a, b):
    # x_i*y_i=z; all other basis products vanish.
    return 2*r if a < r and b == r + a else -1


def equation_rows(r, p, jordan):
    n = 2*r+1
    width=n*n
    pairs = [(i, i) for i in range(n)]
    if jordan:
        pairs += [(i, j) for i in range(n) for j in range(i+1,n)]
    else:
        pairs = [(i,j) for i in range(n) for j in range(n)]
    rows=[]
    for a,b in pairs:
        orders=[(a,b)]
        if jordan and a!=b:
            orders.append((b,a))
        for t in range(n):
            row=[0]*width
            for i,j in orders:
                target=product_basis(r,i,j)
                if target>=0:
                    row[target*n+t] += 1
                for v in range(n):
                    if product_basis(r,v,j)==t:
                        row[i*n+v] -= 1
                    if product_basis(r,i,v)==t:
                        row[j*n+v] -= 1
            if any(a%p for a in row):
                rows.append(row)
    return rows


def dimensions(r,p):
    n=2*r+1
    deriv=(n*n-rank_mod_p(equation_rows(r,p,False),p,n*n))
    jordan=(n*n-rank_mod_p(equation_rows(r,p,True),p,n*n))
    return deriv,jordan


def normal_form(r,p,P,Q,R,lamb,f):
    n=2*r+1
    A=[[0]*n for _ in range(n)]
    for i in range(r):
        for j in range(r):
            A[i][j]=P[i][j]%p
            A[i][r+j]=Q[i][j]%p
            A[r+i][j]=R[i][j]%p
            A[r+i][r+j]=(lamb*(i==j)-P[j][i])%p
    for i in range(2*r):
        A[2*r][i]=f[i]%p
    A[2*r][2*r]=lamb%p
    return A


def evaluate(A,r,p,jordan):
    n=2*r+1
    for row in equation_rows(r,p,jordan):
        value=sum(row[i*n+j]*A[j][i] for i in range(n) for j in range(n))%p
        if value:
            return False
    return True


def orthogonal_count(r,p):
    """Brute-force all linear maps in small V and test quadratic similitude."""
    d=2*r
    vectors=list(product(range(p),repeat=d))
    def q(x):
        return sum(x[i]*x[r+i] for i in range(r))%p
    count=0
    for entries in product(range(p),repeat=d*d):
        cols=[entries[j*d:(j+1)*d] for j in range(d)]
        for c in range(1,p):
            if all(q(tuple(sum(cols[j][i]*v[j] for j in range(d))%p for i in range(d))) == c*q(v)%p for v in vectors):
                count += 1
    return count


def gl_order(r,q):
    z=1
    for j in range(r):
        z*=q**r-q**j
    return z


def orthogonal_formula(r,q):
    z=1
    for j in range(1,r+1):
        z*=(q**(j-1)+1)*(q**j-1)*q**(2*j-2)
    return z


def check():
    cases=[]
    for p in (2,3,5,7):
        for r in range(1,5):
            deriv,jordan=dimensions(r,p)
            expected=(r*r+2*r+1,2*r*r+r+1)
            assert (deriv,jordan)==expected,(r,p,deriv,jordan,expected)
            cases.append((r,p,deriv,jordan))
    for p in (2,3,5):
        for r in (1,2,3):
            P=[[((i+2*j+1)*(j+1))%p for j in range(r)] for i in range(r)]
            Q=[[0]*r for _ in range(r)]
            R=[[0]*r for _ in range(r)]
            for i in range(r):
                for j in range(i+1,r):
                    Q[i][j]=1;Q[j][i]=-1
                    R[i][j]=2;R[j][i]=-2
            f=[(j*j+j+1)%p for j in range(2*r)]
            A=normal_form(r,p,P,Q,R,1,f)
            assert evaluate(A,r,p,True)
            if r>=2 and (p!=2 or any(v%p for row in Q+R for v in row)):
                assert not evaluate(A,r,p,False)
            A0=normal_form(r,p,P,[[0]*r for _ in range(r)],[[0]*r for _ in range(r)],1,f)
            assert evaluate(A0,r,p,False)
    assert orthogonal_count(1,2)==orthogonal_formula(1,2)==2
    assert orthogonal_count(1,3)==(3-1)*orthogonal_formula(1,3)==8
    assert orthogonal_count(2,2)==orthogonal_formula(2,2)==72
    for r in range(1,5):
        for q in (2,3,5):
            ratio=orthogonal_formula(r,q)//gl_order(r,q)
            claimed=2*q**(r*(r-1)//2)
            for i in range(1,r):claimed*=q**i+1
            assert ratio==claimed
    print('DIAMOND_JORDAN_OK', 'modular_dimension_cases',len(cases), 'normal_form_tests',9, 'brute_orthogonal_cases',3)
    for x in cases:
        print('r=%s p=%s ordinary=%s Jordan=%s'%(x))

if __name__=='__main__':
    check()
