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

# Reproducible checks

Run from the package root with the Python 3 standard library:

```
python3 -I verification/verify_desargues_integral_module.py
```

The verifier constructs the subset-incidence graph and its entire ordinary independence complex. It enumerates induced matchings exhaustively, constructs five exact integral crosspolytope fundamental cycles, checks their cellular boundaries, and confirms the three mod-101 rank lower bounds. The row/column lists in `verification/CERTIFICATE.json` specify an actual 388-by-388 integer minor of the augmented matrix of degree-six boundaries and five degree-five cycles. Exact unit pivots verify determinant \(-1\) without a modular-to-integral inference. The code also validates every natural \(S_5\times C_2\) signed cycle transformation. Its success token is `VERIFY_OK_DESARGUES_FIVE_MINIMAL_SPHERES_INTEGRAL_S5_C2_MODULE`.

The graph-specific claim is finite, and the computational enumerations are exhaustive for that graph. The separate flag-complex support lemma is proved by induction in `RESULT.md`; its generality does not rely on the computation. Finite-field ranks alone would not establish integral generation: this requires the integer unit minor. The certificate is subject to self-review only; independent audit is not yet performed.
