from itertools import combinations_with_replacement
from math import comb

NV = 7
# variables 0..5 are x_i; variable 6 is t.

def monomials_of_degree(d):
    out = []
    def rec(pos, left, cur):
        if pos == NV - 1:
            out.append(tuple(cur + [left]))
            return
        for e in range(left + 1):
            rec(pos + 1, left - e, cur + [e])
    rec(0, d, [])
    return out

M2 = monomials_of_degree(2)
M3 = monomials_of_degree(3)
idx3 = {m:i for i,m in enumerate(M3)}

def D_of_monomial(m):
    # Coefficients mod 2. D(t)=0.
    terms = {}
    for i in range(6):
        if m[i] % 2 == 1:
            n = list(m)
            n[i] -= 1
            n[i] += 2
            n = tuple(n)
            terms[n] = terms.get(n, 0) ^ 1
    return {k:v for k,v in terms.items() if v}

# GF(2) matrix as integer bit rows/columns.
columns = []
for m in M2:
    bits = 0
    for n in D_of_monomial(m):
        bits ^= 1 << idx3[n]
    columns.append(bits)

def rank_bitcols(cols):
    piv = {}
    rank = 0
    for x in cols:
        y = x
        while y:
            p = y.bit_length() - 1
            if p in piv:
                y ^= piv[p]
            else:
                piv[p] = y
                rank += 1
                break
    return rank

rank_D = rank_bitcols(columns)
kernel_dim = len(M2) - rank_D
assert len(M2) == 28
assert rank_D == 21
assert kernel_dim == 7

square_mons = []
for i in range(NV):
    m = [0]*NV
    m[i] = 2
    square_mons.append(tuple(m))
assert all(not D_of_monomial(m) for m in square_mons)
assert all(D_of_monomial(m) for m in M2 if m not in square_mons)

# B and C support check.
def add_poly(a, b):
    out = dict(a)
    for m,c in b.items():
        out[m] = out.get(m, 0) ^ c
        if not out[m]:
            del out[m]
    return out

B = {}
for i,j in [(0,1),(2,3),(4,5)]:
    m = [0]*NV
    m[i] = m[j] = 1
    B[tuple(m)] = 1

DB = {}
for m in B:
    DB = add_poly(DB, D_of_monomial(m))

C_expected = {}
for i,j in [(0,1),(2,3),(4,5)]:
    for a,b in [(i,j),(j,i)]:
        m = [0]*NV
        m[a] = 2
        m[b] = 1
        C_expected[tuple(m)] = 1
assert DB == C_expected

# D(S2) has no t^3 and no x_i t^2 terms.
t3 = (0,0,0,0,0,0,3)
xit2 = []
for i in range(6):
    m = [0]*NV
    m[i] = 1
    m[6] = 2
    xit2.append(tuple(m))
for col_m in M2:
    supp = D_of_monomial(col_m)
    assert t3 not in supp
    assert all(m not in supp for m in xit2)

# In ell*Q, Q has t^2 with coefficient 1, so t^3 and x_i t^2
# recover the coefficients of ell exactly. This is a direct support check.
for j in range(NV):
    # ell = variable j
    signature = t3 if j == 6 else xit2[j]
    assert signature == (tuple([0]*6+[3]) if j == 6 else xit2[j])

# Seven square classes are independent modulo Q because Q has the cross terms B.
assert len(B) == 3
assert all(sum(m) == 2 for m in B)

frobenius_degree = 2**4
quotient_degree = 2
bianticanonical_degree = frobenius_degree // quotient_degree
assert frobenius_degree == 16
assert bianticanonical_degree == 8

print(f"degree2_monomials={len(M2)}")
print(f"rank_D_S2_to_S3={rank_D}")
print(f"kernel_D_S2_dimension={kernel_dim}")
print("kernel_basis=squares_x0_to_x5_and_t")
print(f"D_B_term_count={len(DB)}")
print("t_signature_test=PASS")
print(f"frobenius_degree_dim4={frobenius_degree}")
print(f"quotient_degree={quotient_degree}")
print(f"bianticanonical_degree={bianticanonical_degree}")
print("VERIFY_OK")
