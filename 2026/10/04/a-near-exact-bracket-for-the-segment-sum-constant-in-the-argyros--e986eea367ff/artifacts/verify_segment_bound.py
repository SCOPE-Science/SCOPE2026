from decimal import Decimal, getcontext

# Heap labelling V(n,i)=2^n+i: parent(k)=k//2 for k>1.
def is_ancestor(a, b):
    while b > 1:
        b //= 2
        if b == a:
            return True
    return False

def incomparable(a, b):
    return a != b and not is_ancestor(a, b) and not is_ancestor(b, a)

triple = [3, 4, 5]
level_six = list(range(64, 97))
assert all(incomparable(triple[i], triple[j]) for i in range(3) for j in range(i+1, 3))
assert all((n.bit_length() - 1) == 6 for n in level_six)
assert len(level_six) == 33
assert 3 > 2**1
assert 33 > 2**5
assert [1, 2, 4, 8, 16, 32, 64] == [2**k for k in range(7)]

getcontext().prec = 80
lower_sq = Decimal(1) + Decimal(1)/9 + Decimal(1)/1089
tail = (Decimal(4) ** Decimal(-37)) / Decimal(3)
lower = lower_sq.sqrt()
upper = (lower_sq + tail).sqrt()
assert upper - lower < Decimal('8.368e-24')
print('lower =', lower)
print('upper =', upper)
print('width =', upper-lower)
print('finite witness checks = OK')
