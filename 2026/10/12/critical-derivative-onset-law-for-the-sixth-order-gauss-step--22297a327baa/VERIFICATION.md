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

# Verification of the derivative-onset law

Run `python verify_gauss3_boundary.py` using Python 3 with SymPy and mpmath installed. The script returns `VERIFY_OK` only after exact symbolic identities hold for the pole-distance cubic, residue comparison, the doubled-angle resultant, irreducibility modulo two, and a negative exact-rational thirteenth derivative coefficient at \(s=3\). It also prints six illustrative higher-precision onset-order observations with \(\delta\) down to \(0.005\).

The actual executed script returned `VERIFY_OK`; its samples are not exhaustive over steps, generators, or derivative orders. The infinite limit is proved by the analytic pole decomposition and nonresonant-rotation argument in RESULT.md. The 2013 absolute-monotonicity radius is cited as a prior theorem, not independently claimed or reintroduced as new. The finite absorbing pure-birth construction is a sufficient witness-size bound and does not prove dimensional minimality.
