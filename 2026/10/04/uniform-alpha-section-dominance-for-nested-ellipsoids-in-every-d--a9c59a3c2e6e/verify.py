from fractions import Fraction

for c_num in range(0, 9):
    for s_num in range(1, 13):
        c = Fraction(c_num, 4)
        s = Fraction(s_num, 4)
        if c + s < 1:
            continue
        for t_num in range(0, 13):
            t = Fraction(t_num, 12)
            lhs = c + t*s - t
            rhs = t*(c+s-1) + (1-t)*c
            assert lhs == rhs
            assert lhs >= 0
            assert (t-c)/s <= t
print("VERIFY_OK")
