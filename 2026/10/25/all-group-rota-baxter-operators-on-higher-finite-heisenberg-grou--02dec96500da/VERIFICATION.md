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

Run `python verify.py` with a standard Python 3 interpreter. The independent matrix-condition implementation is compared against the defining group Rota–Baxter identity, not merely against a repeated count formula. The small-field enumeration exhausts all two-dimensional linear maps for \(p=3,5,7\), including every scalar \(c\); over \(p=3\), each matrix/scalar pair is also checked on all ordered group-element pairs with zero linear functional. Forty further arbitrary-linear-functional tests check that the chosen functional does not alter the criterion. Dimension-four random linear maps with random functionals are compared against group-identity samples, including constructed valid maps for all three scalar classes. The isotropic-image formula and symplectic-group order are computed in five parameter cases.

Expected terminal line: `VERIFY_OK`.

Expected counts for \(n=2\) are \(45{,}152{,}802\) for \(p=3\), and \(93{,}113{,}281{,}250\) for \(p=5\). These finite computations are not a proof for all primes or dimensions. The symbolic derivation appears in `RESULT.md`, particularly the center-preservation argument, polarization identity, and isotropic-map enumeration.

The scientific work has received a self-review only. Independent audit has not been performed.
