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

# Verification details

Run `python3 verify_cap.py` with Python 3.10 or later; no third-party modules or external data are needed. The checked file was executed from the same directory as the proof text, and returned:

`VERIFY_OK 2220 checks: 2206 rational, 10 quadrature, 4 asymptotic`

The program checks the exact rational forward and inverse formulas at seven cut heights and three sphere radii, all ordered pairs on a 65-point rational grid for the global stability inequality, and the original independent-surface-pair integral via deterministic four-dimensional quadrature for five cases (ten relative-error comparisons). It also tests the small angular-deficit expansion at four positive deficits. The proof's analytic identities, especially the arbitrary-parameter stability bound and equality limits, are reproduced in RESULT.md and do not rest on those finite checks.

The literature comparison includes actual inspection of arXiv:1411.5639v1 (whole-sphere chord law and moment propositions) and arXiv:2007.07297v1 (spherical geodesic distance and cap specialization). The cap-density corollary is forward information and is not treated as an inverse proof. Independent scholarly review has not been performed.
