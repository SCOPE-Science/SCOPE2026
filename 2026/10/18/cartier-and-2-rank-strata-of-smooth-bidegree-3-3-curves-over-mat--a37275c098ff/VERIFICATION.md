---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run in one directory containing all provided files:

```sh
g++ -O3 -std=c++17 enumerate.cpp -o enumerate
./enumerate > enumeration.txt 2> enum_stderr.txt
python3 orbits.py > orbit_output.txt
python3 verify_witnesses.py > verify_output.txt
python3 classify.py > classify_output.txt
```

Dependencies: a C++17 compiler, Python 3, and SymPy for the exact positive Gröbner bases. The C++ tool regenerates binary coefficient-mask lists and exact negative witnesses over \(\mathbf F_{2^m}\) for \(m=1,\dots,6\). Its singular witnesses must all satisfy \(F=F_x=F_y=0\), independently checked by `verify_witnesses.py`. Those negative witnesses classify \(49,515\) equations as geometrically singular; testing bounded extensions *does not* prove smoothness of the remaining \(16,020\). Instead, the 252 independently computed projective orbits of survivors have all four affine chart Jacobian ideals equal to the unit ideal (1,008 exact Gröbner calculations), proving geometric smoothness of all survivors.

The Hasse–Witt matrices are computed by two separately implemented linear-algebra routes: all smooth masks directly in `enumerate.cpp`, and weighted orbit representatives independently in `classify.py`. Both yield the five stated \((2\text{-rank},a\text{-number})\) counts. `statistics.txt` records the class counts and equation counts; `orbit_reps.txt` records all 252 representative masks and their orbit sizes. All required code, singular witnesses and inputs are embedded in the delivered finding. Historical literature and prior data may imply additional unverified coincidences; an external independent audit has not been performed.
