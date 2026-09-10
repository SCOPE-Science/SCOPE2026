# Replay guide (stdlib only; no compiler needed except to rebuild `enum_seq`)

1. Orbit check: `python3 orbit_check.py`
   Both patterns in U, disjoint orbits (4 vs 2), both contain 132 / avoid 231.
2. Filter validation: `python3 thit_test.py` → `done, mismatches: 0`.
3. Witnesses + n=6/n=7 census: `python3 verify_witnesses.py` → `VERIFY: OK`.
4. Brute census to n=8: `python3 brute.py`
   Expect: `n=7: U=1806 C1=1781 C2=1785`, `n=8: U=8558 C1=8224 C2=8308`.
5. Insertion census to n=12: `./enum_seq 12` (prebuilt Linux x86-64 binary;
   source `enum.c`; rebuild with `gcc -O2 -o enum_seq enum.c`)
   Expect U = Schroder (1806, 8558, 41586, 206098, 1037718, 5293446),
   C1 = (1781, 8224, 38311, 179263, 841254, 3958066),
   C2 = (1785, 8308, 39314, 188371, 911785, 4451744).
6. Independent insertion cross-check to n=9 (n=10 slow): `python3 third_engine.py`
