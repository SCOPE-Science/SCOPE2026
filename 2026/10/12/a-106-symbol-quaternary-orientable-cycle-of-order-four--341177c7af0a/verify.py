"""Directly verify a quaternary order-four orientable cyclic word."""
from itertools import product
from pathlib import Path

p = Path(__file__).with_name("witness.txt")
w = p.read_text(encoding="ascii").strip()
assert len(w) == 106
assert set(w) <= set("0123")

factors = ["".join(w[(i + j) % len(w)] for j in range(4)) for i in range(len(w))]
assert all(t != t[::-1] for t in factors)
canon = [min(t, t[::-1]) for t in factors]
assert len(canon) == len(set(canon)) == 106

allclasses = {min("".join(z), "".join(z)[::-1]) for z in product("0123", repeat=4)
              if z != z[::-1]}
unused = sorted(allclasses - set(canon))
assert len(allclasses) == 120
assert len(unused) == 14
assert unused == ["0003", "0011", "0022", "0032", "0033", "0111", "0322", "0333",
                  "1033", "1103", "1122", "1133", "2223", "2233"]
print("VERIFY_OK period=106 windows=106 reversal_orbits=106 unused_orbits=14")
