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

# Reproducibility and scope

Run `python3 verify.py` from the directory containing this file and the supplied standalone Python verifier. It uses only the Python standard library, constructs each rook graph directly, and checks each induced matching by whether different selected rook edges have any adjacent endpoints. It determines inclusion-maximality by testing every possible additional edge, not by using the counting formula.

The recorded execution was:

```
VERIFY_OK exhaustive_boards=16 dimensions=2..5 total_induced_matchings=6201 formula_support_checks=289
R_3_3_all={0: 1, 1: 18, 2: 9} R_3_3_maximal={2: 9}
R_6_6_all={0: 1, 1: 180, 2: 6300, 3: 36000, 4: 8100} R_6_6_maximal={3: 3600, 4: 8100}
```

The finite checks verify every graph in the tested range but do not establish the theorem for unbounded orders. That follows from the bijection, factorial count, and maximality criterion given in the proof. Independent mathematical audit has not been performed.
