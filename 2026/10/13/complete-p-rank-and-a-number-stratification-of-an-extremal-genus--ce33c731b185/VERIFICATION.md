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

The reproducible computation in `verify.py` requires only Python 3's standard library and finishes with `VERIFY_OK` if its exact polynomial assertions hold. It checks the original sextic-to-cubic identity in \(\mathbb F_5[t,x]\), both quartic/cubic Hasse-polynomial factorizations, all four entries of the genus-two Cartier–Manin matrix, and pairwise coprimality and separability of the exceptional parameter factors. These are **symbolic identities**, not a bounded collection of samples.

The vanishing of the entire Cartier–Manin matrix at the two common roots proves that these fibers are superspecial, not merely supersingular. The existence of the four singular fibers and smoothness elsewhere is cited from Sun–Xu, arXiv:2610.02760v1, Theorem 1.5 and Section 5. The proof derives both involution quotients directly from the equation and applies the standard genus-two elliptic quotient isogeny, which is separable because the quotient maps have degree two in characteristic five. Neither this script nor these calculations certify novelty against unindexed literature or establish independent audit.
