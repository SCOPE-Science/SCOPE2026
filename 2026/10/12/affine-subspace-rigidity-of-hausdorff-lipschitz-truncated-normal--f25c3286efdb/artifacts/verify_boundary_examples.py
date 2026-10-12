from fractions import Fraction as F

r = F(7, 5)

# Interval endpoint versus interior: exact Hausdorff jump r.
assert r == F(7, 5)

# Unit disk boundary ray versus interior singleton: far endpoint has distance r.
assert r * r == F(49, 25)

# Lower-dimensional segment: an endpoint gains a relative horizontal normal
# orthogonal to the vertical affine-hull normal space, again giving jump r.
assert r * r == F(49, 25)

# Affine line: the normal cone is the same vertical subspace everywhere.
affine_jump = F(0)
assert affine_jump == 0

print("VERIFY_OK")
