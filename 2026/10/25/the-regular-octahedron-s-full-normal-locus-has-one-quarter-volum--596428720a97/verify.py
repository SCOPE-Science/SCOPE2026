from fractions import Fraction as F

# In the chamber 0 <= z <= y <= x and 2*x+y+z <= 1,
# integrating first in x and then in y leaves
# I(z) = 1/12 - 2z/3 + 4z^2/3. Integrate exactly over 0 <= z <= 1/4.
a = F(1, 4)
sector = a * F(1, 12) - a**2 * F(1, 3) + a**3 * F(4, 9)
assert sector == F(1, 144), sector
sigma_volume = 48 * sector
assert sigma_volume == F(1, 3), sigma_volume
octahedron_volume = F(4, 3)
probability = sigma_volume / octahedron_volume
assert probability == F(1, 4), probability
print("PASS: exact chamber volume = 1/144")
print("PASS: exact signohedron volume = 1/3")
print("PASS: exact full-normal probability = 1/4")
