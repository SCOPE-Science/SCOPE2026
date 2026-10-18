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

# Reproducibility and verification

Run `python verify.py` using the standard Python library. This enumerates all \(32{,}767\) nonzero mask triples, detects smoothness by two exact gcd tests, computes rational-fiber and branch-support counts, partitions all smooth equations into \(36\)-element group orbits, and compares against `data/joint_table.json` and `data/orbit_representatives.csv`. Expected terminal result:

```
PASS: 32767 nonzero equations, 9216 smooth, 294 embedding orbits.
PASS: full independent coefficient and orbit distributions agree.
PASS: 1083 six-point curves, 37 orbits, p-rank 1/3 split 282/801.
```

Run `python crosscheck.py` with SymPy installed. This checks the Jacobian ideal on all four affine charts by exact Gröbner-basis calculation over \(\mathbf F_2\), for representatives of **every** ambient projective-coordinate orbit, including singular ones. It independently obtains the first three extension-field point counts for each smooth orbit representative and derives the Jacobian \(2\)-rank from the genus-three zeta polynomial modulo two. Expected result:

```
PASS: Groebner smoothness on all projective orbits (smooth and singular).
PASS: independent finite-field zeta p-ranks on every smooth orbit.
```

The orbit reduction is exact because the program explicitly applies all \(36\) group elements, validates that each computed orbit lies inside the remaining coefficient set, and exhausts that set. The field-extension counts verify \(2\)-ranks but do not replace the exact algebraic smoothness test. The data files and both source files are part of the package. No proof about larger fields or about abstract isomorphism-class numbers is asserted.
