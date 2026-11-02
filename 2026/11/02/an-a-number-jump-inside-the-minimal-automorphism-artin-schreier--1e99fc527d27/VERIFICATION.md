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

# Mathematical verification

The characteristic-three computations can be reproduced using the accompanying standalone standard-library script:

```text
python3 verify.py
VERIFY_OK: genus basis, universal coefficients, Cartier rank, F3 automorphisms
```

The script checks the nine distinct pole orders \(3i+10j\le16\) for the basis forms \(x^iy^jdx\), computes the formal Cartier action, and verifies that its ranks are four at \(a=0\) and five for nonzero parameters in \(\mathbb F_3\). It also enumerates all affine base-map lifts over \(\mathbb F_3\) to test the rigidity calculation. The full proof, not the enumeration, establishes the results over algebraically closed fields and excludes automorphisms defined only after field extension.

The standard geometric inputs are the ramification formula for an Artin–Schreier cover, Deuring–Shafarevich, Castelnuovo–Severi, and the Cartier operator's semilinearity. The nonstandard steps specific to this family are the coefficient comparison in equation (1) of RESULT.md and the nine-by-nine Cartier calculation; both are written explicitly there and checked in the script.

An independent mathematical audit has not been performed. No computer experiment is treated as an infinite-field proof.
