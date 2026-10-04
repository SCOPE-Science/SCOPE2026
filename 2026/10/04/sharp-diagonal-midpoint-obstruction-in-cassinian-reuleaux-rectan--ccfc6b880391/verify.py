from fractions import Fraction

# Exact factorization:
# (r+r^2)^2 - (r^2+4r-1)
# = r^4 + 2 r^3 - 4 r + 1
# = (r-1)((r+1)^3-2).
# Coefficients are checked by direct integer polynomial multiplication.
left = [1, -4, 0, 2, 1]  # ascending: 1 - 4r + 0r^2 + 2r^3 + r^4
# (r-1)(r^3+3r^2+3r-1)
a = [-1, 1]
b = [-1, 3, 3, 1]
prod = [0]*(len(a)+len(b)-1)
for i,x in enumerate(a):
    for j,y in enumerate(b):
        prod[i+j] += x*y
assert prod == left

# Exact rational witness a=69/260 has s=269/260 since 69^2+260^2=269^2.
assert 69*69 + 260*260 == 269*269
r = Fraction(69,269)
assert 4*r > 1
# r < 2^(1/3)-1 iff (1+r)^3 < 2.
assert 338**3 == 38614472
assert 2*269**3 == 38930218
assert 338**3 < 2*269**3

# The lower endpoint a=1/sqrt(15) maps to r=1/4 exactly after squaring:
# r^2 = a^2/(1+a^2) = (1/15)/(16/15) = 1/16.
assert Fraction(1,15) / (1 + Fraction(1,15)) == Fraction(1,16)

print('VERIFY_OK')
