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

Run `python3 verify.py` with Python 3.8 or later, using only the standard library. The executable independently evaluates each vertex's neighbors on \(K_{n,n}\setminus M_n\) rather than invoking the proof's case classification. Exhaustive comparisons cover \(4\le n\le8\), \(2\le r\le n-2\), and 407,808 actual action profiles over 15 parameter pairs; the expected families are generated independently and compared as sets. Each parameter pair is also checked after restoring all matching edges, yielding two pure equilibria on \(K_{n,n}\).

A separate weighted enumeration of all four pair-type counts, not constrained to the theorem's families, covers 378 parameter pairs with \(4\le n\le30\). Each feasible type profile contributes its exact multinomial labeling multiplicity. A local execution printed:

```text
VERIFIED
directly_evaluated_profiles=407808
direct_equilibrium_exhaustive_parameter_pairs=15
independent_four_type_weighted_count_parameter_pairs=378
example_n6_r3=43
example_n7_r3=44
```

The finite computations do not certify infinitely many graphs. The universal proof relies on the four type constraints and their exhaustive case split. No external independent audit or formal verification has been performed.
