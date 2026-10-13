from fractions import Fraction

def vertices(n):
    return 2**(n+1)-1

def exact_partial(n):
    return 2**(vertices(n)-1)

def printed_partial(n):
    return 128**(2**(n-1)-1)

assert vertices(2) == 7
assert exact_partial(2) == 64
assert printed_partial(2) == 128
assert exact_partial(3) == 2**14
assert printed_partial(3) == 2**21
assert printed_partial(3) != 2**vertices(3)

for n in range(2, 9):
    exact_exp = vertices(n)-1
    printed_exp = 7*(2**(n-1)-1)
    assert exact_partial(n) == 2**exact_exp
    assert printed_partial(n) == 2**printed_exp
    if n >= 3:
        assert printed_exp > vertices(n)

assert Fraction(7,4) != Fraction(1,1)
print("VERIFY_OK")
print("n2_exact_partial=64 n2_printed=128")
print("n3_exact_partial=2^14 n3_printed=2^21 unrestricted=2^15")
print("free_energy_coefficients exact=1 source=7/4")
