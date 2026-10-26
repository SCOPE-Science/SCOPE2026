#!/usr/bin/env python3
"""Check the Euler-characteristic obstruction from the published face vector."""

face_vector = (21, 120, 420, 480, 192)
euler_characteristic = sum((-1) ** dimension * count for dimension, count in enumerate(face_vector))
expected_for_cp2 = 3
assert euler_characteristic == 33
assert euler_characteristic != expected_for_cp2
print(f"face_vector={face_vector}")
print(f"euler_characteristic={euler_characteristic}")
print(f"chi_CP2={expected_for_cp2}")
