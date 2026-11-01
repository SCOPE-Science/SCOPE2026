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

# Verification evidence and scope

`RESULT.md` gives the self-contained analytic argument: support-function inclusion, a base John frame, explicit positive cap weights, the two John moment identities, affine normalization and the sharp differentiability transition. The proof is valid for all dimensions and real admissible parameters; it does not rely on an exhaustive computer search.

Run `python check_frusta.py` with Python 3. The program uses only standard-library `fractions.Fraction` to check exactly 197 dimension/parameter instances for \(2\le n\le14\), including the dimension-dependent threshold and both endpoints. For each instance it verifies cap inequalities, exact side-support equality, the axial weights and isotropic second-moment equations, and a regular-simplex base contact Gram frame. The program was run against its actual saved source and printed:

```
PASS: 197 dimension/parameter pairs, exact Fraction arithmetic;
both transition regimes and the degenerate top-base endpoint included.
```

The numerical count does not establish the all-parameter theorem. In particular, verification of the non-round and asymmetric base case follows from the general contact-frame construction proved in `RESULT.md`, rather than finite sampling of all possible convex bases. No independent review, formal certification or external certificate is claimed.
