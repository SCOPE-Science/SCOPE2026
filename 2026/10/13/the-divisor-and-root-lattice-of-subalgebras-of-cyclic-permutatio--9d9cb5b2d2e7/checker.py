"""Direct small-field census of linear subalgebras of cyclic evolution algebras.

Run: python checker.py
No third-party packages required.
"""
from itertools import combinations, product
from collections import Counter
from math import gcd


def field(q):
    if q in (2, 3, 5):
        mul = [[(a*b)%q for b in range(q)] for a in range(q)]
        add = [[(a+b)%q for b in range(q)] for a in range(q)]
    elif q in (4, 8):
        deg = {4:2,8:3}[q]
        modulus = {4:0b111,8:0b1011}[q]
        add = [[a^b for b in range(q)] for a in range(q)]
        mul = [[0]*q for _ in range(q)]
        for a in range(q):
            for b in range(q):
                z = 0
                for k in range(deg):
                    if (b>>k)&1:
                        z ^= a<<k
                for k in range(2*deg-2,deg-1,-1):
                    if (z>>k)&1:
                        z ^= modulus<<(k-deg)
                mul[a][b] = z
    else:
        raise ValueError(q)
    neg = [next(i for i in range(q) if add[a][i] == 0) for a in range(q)]
    inv = [0]+[next(i for i in range(1,q) if mul[a][i]==1) for a in range(1,q)]
    return add,mul,neg,inv


def rref_bases(n,k,q):
    for piv in combinations(range(n),k):
        free = [(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
        for vals in product(range(q), repeat=len(free)):
            rows = [[0]*n for _ in range(k)]
            for i,j in enumerate(piv): rows[i][j] = 1
            for (i,j),v in zip(free, vals): rows[i][j] = v
            yield rows,piv


def in_span(vec,rows,piv,add,mul,neg):
    v = list(vec)
    n = len(v)
    for row,p in zip(rows,piv):
        a = v[p]
        if a:
            for j in range(p,n):
                v[j] = add[v[j]][neg[mul[a][row[j]]]]
    return all(x==0 for x in v)


def counts(n,q):
    add,mul,neg,inv = field(q)
    c = Counter()
    for k in range(n+1):
        for rows,piv in rref_bases(n,k,q):
            good = True
            for i in range(k):
                if not good:break
                for j in range(i,k):
                    v = [0]*n
                    for t in range(n):
                        v[(t+1)%n] = mul[rows[i][t]][rows[j][t]]
                    if not in_span(v,rows,piv,add,mul,neg):
                        good = False;break
            if good: c[k]+=1
    return dict(sorted(c.items()))


def expected(n,q):
    ans = {0:1}
    for d in range(1,n+1):
        if n%d==0:
            ans[d] = gcd((2**n-1)//(2**d-1), q-1)
    return ans



def power(a,e,mul):
    z = 1
    while e:
        if e&1:z=mul[z][a]
        a=mul[a][a]
        e//=2
    return z


def canonical_rows(n,d,c,mul):
    rows = [[0]*n for _ in range(d)]
    for i in range(n):
        j=i%d
        exponent=(2**i-2**j)//(2**d-1)
        rows[j][i] = power(c,exponent,mul)
    return rows


def check_lattice(n,q):
    add,mul,neg,inv = field(q)
    nodes=[]
    for d in range(1,n+1):
        if n%d:continue
        s=(2**n-1)//(2**d-1)
        for c in range(1,q):
            if power(c,s,mul)==1:
                rows=canonical_rows(n,d,c,mul)
                for a in range(d):
                    for b in range(d):
                        prodv=[0]*n
                        for i in range(n):
                            prodv[(i+1)%n]=mul[rows[a][i]][rows[b][i]]
                        # Full-coordinate RREF reduction using rank by Gaussian elimination.
                        assert matrix_rank(rows+[prodv],add,mul,neg,inv)==d
                nodes.append((d,c,rows))
    assert len(nodes) == sum(expected(n,q).values())-1
    for d,c,rows in nodes:
        for e,h,other in nodes:
            via_rows=all(matrix_rank(other+[v],add,mul,neg,inv)==e for v in rows)
            via_formula=(e%d==0 and h==power(c,(2**e-1)//(2**d-1),mul))
            assert via_rows == via_formula, (n,q,d,c,e,h,via_rows,via_formula)
    print(f'lattice n={n} q={q} nodes={len(nodes)} OK')


def matrix_rank(rows,add,mul,neg,inv):
    if not rows:return 0
    a=[list(r) for r in rows]
    n=len(a[0]); r=0
    for j in range(n):
        piv=next((i for i in range(r,len(a)) if a[i][j]!=0),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        scale=inv[a[r][j]]
        a[r]=[mul[scale][v] for v in a[r]]
        for i in range(len(a)):
            if i==r:continue
            coef=a[i][j]
            if coef:
                a[i]=[add[a[i][k]][neg[mul[coef][a[r][k]]]] for k in range(n)]
        r+=1
        if r==len(a):break
    return r


def main():
    cases = [(2,2),(2,3),(2,4),(3,2),(3,4),(3,8),(4,2),(4,3),(4,4),(4,5),(5,2),(6,2)]
    for n,q in cases:
        obs = counts(n,q)
        exp = expected(n,q)
        assert obs == exp, (n,q,obs,exp)
        print(f'n={n} q={q} rank_counts={obs}')
    for n,q in [(4,4),(6,2),(6,8),(12,4),(12,8)]:check_lattice(n,q)
    print('VERIFY_OK')

if __name__=='__main__':main()
