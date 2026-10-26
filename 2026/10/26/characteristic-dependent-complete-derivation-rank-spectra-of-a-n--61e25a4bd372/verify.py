"""Reproduce finite-field derivation rank census for the algebra with e_i^2=z (i=1,2,3)."""
from itertools import product
from collections import Counter
from math import prod


def matrix_rank_mod(a, q):
    a = [row[:] for row in a]
    n, m = len(a), len(a[0])
    r = 0
    for c in range(m):
        pivot = next((i for i in range(r,n) if a[i][c]%q),None)
        if pivot is None: continue
        a[r],a[pivot] = a[pivot],a[r]
        inv = pow(a[r][c]%q,-1,q)
        a[r] = [(v*inv)%q for v in a[r]]
        for i in range(r+1,n):
            factor = a[i][c]%q
            if factor:
                a[i] = [(a[i][j]-factor*a[r][j])%q for j in range(m)]
        r+=1
        if r==n: break
    return r


def derivation_linear_constraints(p):
    """Independent linear-system derivation dimension test."""
    def mult(x,y):
        return [0,0,0,sum(x[i]*y[i] for i in range(3))%p]
    rows=[]
    for i in range(4):
      for j in range(i,4):
        u=[int(k==i) for k in range(4)]
        v=[int(k==j) for k in range(4)]
        cols=[]
        for c in range(4):
          for r in range(4):
            D=[[0]*4 for _ in range(4)]
            D[r][c]=1
            du=[D[k][i] for k in range(4)]
            dv=[D[k][j] for k in range(4)]
            uv=mult(u,v)
            d_uv=[sum(D[k][h]*uv[h] for h in range(4))%p for k in range(4)]
            v2=mult(du,v)
            v3=mult(u,dv)
            cols.append([(d_uv[k]-v2[k]-v3[k])%p for k in range(4)])
        for k in range(4):
            rows.append([cols[a][k] for a in range(16)])
    return 16-matrix_rank_mod(rows,p)


def matrices(q):
    if q%2:
        for t,a,b,c in product(range(q),repeat=4):
            # D|V = tI + S, D(z) = 2tz
            A=[[t,a,b],[-a,t,c],[-b,-c,t]]
            for ell in product(range(q),repeat=3):
                D=[[A[i][j]%q for j in range(3)]+[0] for i in range(3)]
                D.append(list(ell)+[(2*t)%q])
                yield D
    else:
        for a,b,c,d,e,f in product(range(q),repeat=6):
            A=[[a,b,c],[b,d,e],[c,e,f]]
            for ell in product(range(q),repeat=3):
                D=[[A[i][j]%q for j in range(3)]+[0] for i in range(3)]
                D.append(list(ell)+[0])
                yield D


def expected(q):
    if q%2:
        return {0:1,
            1:q**3-1,
            2:q**2*(q**3-1),
            3:(q**3-1)*(q**3-q**2)+(q-1)*q**3*(q**2+q),
            4:(q-1)*q**3*(q**3-q**2-q)}
    return {0:1,
        1:(q+1)*(q**3-1),
        2:(q**3-1)*(q**4+q**3-q),
        3:q**4*(q**2-1)*(q**3-1),
        4:0}


def check_leibniz(D,q):
    # Product e_i e_i = z, with e_i e_j = 0 for i != j.
    for i in range(3):
        if [D[r][3]%q for r in range(4)] != [0,0,0,2*D[i][i]%q]:
            return False
        for j in range(i+1,3):
            if (D[j][i]+D[i][j])%q: return False
    for j in range(3):
        if D[j][3]%q: return False
    return True


def run():
    for q in [2,3,5]:
        cnt=Counter()
        n=0
        for D in matrices(q):
            assert check_leibniz(D,q)
            cnt[matrix_rank_mod(D,q)] += 1
            n+=1
        e=expected(q)
        assert all(cnt.get(k,0)==v for k,v in e.items()),(q,cnt,e)
        assert n== (q**9 if q==2 else q**7),(q,n)
        dim=derivation_linear_constraints(q)
        assert dim == (9 if q==2 else 7),(q,dim)
        print(f'q={q}; dimension={dim}; ranks={[cnt.get(j,0) for j in range(5)]}; checked={n}; PASS')
    print('EVOLUTION_DERIVATION_RANKS_OK')

if __name__=='__main__':run()

# Additional independent tests of the all-dimensional even-characteristic theorem.
def gauss_poly(n, r, q):
    if r<0 or r>n:return 0
    top=prod(q**(n-i)-1 for i in range(r))
    bot=prod(q**(r-i)-1 for i in range(r))
    return top//bot

def beta_recurrence(n,q):
    vals=[1, q-1]
    for r in range(2,n+1):
        vals.append((q-1)*q**(r-1)*vals[-1]+(q**(r-1)-1)*q**(r-1)*vals[-2])
    return vals[:n+1]

def binary_matrix_rank(a):
    a=[list(row) for row in a]
    n=len(a); k=0
    for j in range(n):
        p=next((i for i in range(k,n) if a[i][j]),None)
        if p is None:continue
        a[k],a[p]=a[p],a[k]
        for i in range(k+1,n):
            if a[i][j]: a[i]=[x^y for x,y in zip(a[i],a[k])]
        k+=1
    return k

def gf4_mul(a,b):
    # F_2[w] / (w^2+w+1), represented by binary 0..3.
    p=0
    while b:
        if b&1:p ^= a
        b >>= 1
        a <<= 1
        if a&4:a^=7
    return p

def gf4_rank(a):
    a=[list(row) for row in a];n=len(a);k=0
    inverses={1:1,2:3,3:2}
    for j in range(n):
        p=next((i for i in range(k,n) if a[i][j]),None)
        if p is None:continue
        a[k],a[p]=a[p],a[k]
        inv=inverses[a[k][j]]
        a[k]=[gf4_mul(t,inv) for t in a[k]]
        for i in range(k+1,n):
            if a[i][j]:
                s=a[i][j]
                a[i]=[a[i][z]^gf4_mul(s,a[k][z]) for z in range(n)]
        k+=1
    return k

def test_even_sym(n,q):
    vals=beta_recurrence(n,q)
    expected_N=[gauss_poly(n,r,q)*vals[r] for r in range(n+1)]
    N=Counter()
    rank_func=binary_matrix_rank if q==2 else gf4_rank
    for vec in product(range(q),repeat=n*(n+1)//2):
        A=[[0]*n for _ in range(n)]
        k=0
        for i in range(n):
            for j in range(i,n):A[i][j]=A[j][i]=vec[k];k+=1
        N[rank_func(A)]+=1
    assert [N[r] for r in range(n+1)]==expected_N,(n,q,N,expected_N)
    C=[N[j]*q**j+(N[j-1]*(q**n-q**(j-1)) if j else 0) for j in range(n+1)]
    assert sum(C)==q**(n*(n+3)//2)
    print(f'characteristic=2; q={q}; n={n}; symmetric ranks={expected_N}; derivation ranks={C}; PASS')

if __name__=='__main__':
    test_even_sym(3,4)
    test_even_sym(4,2)
