"""Finite field check of five-term augmented Rota--Baxter tensor operators.

All finite checks are auxiliary to the symbolic all-field proof in RESULT.md.
"""

def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def e_map(n):
    # For delta-function coordinates, the algebra unit is sum_i delta_i.
    return [[int(j == 0) for j in range(n)] for i in range(n)]


def sum_operator(n, q, weight):
    # (P f)(i) = weight * sum_{j<i} f(j)
    return [[(weight if i > j else 0) % q for j in range(n)] for i in range(n)]


def kron(a, b, q):
    return [[(x * y) % q for x in ar for y in br] for ar in a for br in b]


def five_term(n, q, weight, co):
    p = sum_operator(n, q, weight)
    i, e = ident(n), e_map(n)
    terms = [kron(p, i, q), kron(p, e, q), kron(i, p, q),
             kron(e, p, q), kron(p, p, q)]
    return [[sum(co[t] * terms[t][r][s] for t in range(5)) % q
             for s in range(n*n)] for r in range(n*n)]


def rb_defect(operator, n, q, weight):
    # Coordinate delta basis of the pointwise algebra on n^2 points.
    size = n*n
    for i in range(size):
        for j in range(size):
            lhs = [(operator[k][i] * operator[k][j]) % q
                   for k in range(size)]
            u = [(operator[k][i] * int(k == j)
                  + operator[k][j] * int(k == i)
                  + weight * int(i == j and k == i)) % q
                 for k in range(size)]
            rhs = [sum(operator[k][z] * u[z] for z in range(size)) % q
                   for k in range(size)]
            if lhs != rhs:
                return i, j, [(k, (lhs[k]-rhs[k]) % q)
                              for k in range(size) if lhs[k] != rhs[k]]
    return None


def check_base(n, q, weight):
    p = sum_operator(n,q,weight)
    for i in range(n):
        for j in range(n):
            lhs = [(p[k][i]*p[k][j]) % q for k in range(n)]
            u = [(p[k][i]*int(k==j) + p[k][j]*int(k==i)
                  + weight*int(i==j and k==i)) % q for k in range(n)]
            rhs = [sum(p[k][z]*u[z] for z in range(n)) % q for k in range(n)]
            assert lhs==rhs, (n,q,weight,i,j)
    assert all(p[0][j] == 0 for j in range(n))


for q in (2, 3, 5):
    for weight in (1, q-1):
        for n in (2, 3, 4):
            check_base(n, q, weight)
            for co in ((0,1,1,0,0),(1,0,0,1,0)):
                assert rb_defect(five_term(n,q,weight,co),n,q,weight) is None
        # The symmetric id/id candidate forced by the two-point algebra.
        co=(1,0,1,0,pow(weight,-1,q))
        assert rb_defect(five_term(3,q,weight,co),3,q,weight) is not None
        # The symmetric projection/projection candidate forced by the two-point algebra.
        co=(0,1,0,1,(-pow(weight,-1,q))%q)
        bad=rb_defect(five_term(4,q,weight,co),4,q,weight)
        assert bad is not None
        if q==2:
            assert bad[0:2]==(5,6),bad
            assert dict(bad[2])=={11:1,15:1},bad

# Direct verification that in characteristic 2 the exceptional candidate
# works on the three-point function algebra, but not the four-point algebra.
q=2
assert rb_defect(five_term(3,q,1,(0,1,0,1,1)),3,q,1) is None
assert rb_defect(five_term(4,q,1,(0,1,0,1,1)),4,q,1) is not None
print('VERIFY_OK')
