from fractions import Fraction as F

# B = [[1,-1/2],[1,1/2]], so B^{-1} = [[1/2,1/2],[-1,1]].
B = ((F(1), F(-1,2)), (F(1), F(1,2)))
Bi = ((F(1,2), F(1,2)), (F(-1), F(1)))
I00 = Bi[0][0]*B[0][0] + Bi[0][1]*B[1][0]
I01 = Bi[0][0]*B[0][1] + Bi[0][1]*B[1][1]
I10 = Bi[1][0]*B[0][0] + Bi[1][1]*B[1][0]
I11 = Bi[1][0]*B[0][1] + Bi[1][1]*B[1][1]
assert (I00,I01,I10,I11) == (1,0,0,1)

def mu(lam):
    assert F(0) <= lam <= F(1)
    a = (F(2)-lam)/4
    b = (F(1)+lam)/2
    one_row = max(F(1,1)/(2*a), F(1,1)/(2*b))
    two_rows = max(F(1,1)/(4*a), F(1,1)/b)
    # On [0,1], these simplify exactly as in the proof.
    assert one_row == F(2,1)/(F(2)-lam)
    assert two_rows == F(2,1)/(F(1)+lam)
    return min(one_row, two_rows)

for q in range(1,33):
    for p in range(q+1):
        l = F(p,q)
        expected = F(2,1)/(F(2)-l) if l <= F(1,2) else F(2,1)/(F(1)+l)
        assert mu(l) == expected
        inv = 1/mu(l)
        assert inv == F(1) - min(l, F(1)-l)/2
        assert mu(l) == mu(F(1)-l)

assert mu(F(0)) == 1
assert mu(F(1)) == 1
assert mu(F(1,2)) == F(4,3)
assert 1/mu(F(1,2)) == F(3,4)
print('VERIFY_OK')
