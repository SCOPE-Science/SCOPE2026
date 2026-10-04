from fractions import Fraction
import math

# At r=1/3, write A''=(3/2)*sqrt(3) and B'=-(7/30)*sqrt(3).
shape_offset = -Fraction(-7, 30) / Fraction(3, 2)
assert shape_offset == Fraction(7, 45)

leading = 2.0 / math.sqrt(6.0 * math.pi)
cubic = -71.0 * math.sqrt(3.0) / (270.0 * math.sqrt(2.0 * math.pi))

delta = 0.01
shape_prediction = 1.0 / (3.0 * delta) + float(shape_offset)
minimum_prediction = 0.5 + leading * math.sqrt(delta) + cubic * delta ** 1.5

source_shape = 33.4871
source_minimum = 0.545885
assert abs(shape_prediction - source_shape) < 0.01
assert abs(minimum_prediction - source_minimum) < 2e-6

print(f"shape_offset={shape_offset}")
print(f"leading_constant={leading:.15f}")
print(f"cubic_constant={cubic:.15f}")
print(f"delta={delta:.2f} shape_prediction={shape_prediction:.12f} source={source_shape:.4f}")
print(f"delta={delta:.2f} minimum_prediction={minimum_prediction:.12f} source={source_minimum:.6f}")
print("VERIFY_OK")
