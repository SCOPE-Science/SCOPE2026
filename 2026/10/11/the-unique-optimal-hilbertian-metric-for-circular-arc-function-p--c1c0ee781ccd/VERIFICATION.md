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

# Verification notes
The analytic proof is self-contained. Its critical checks are: an exact coordinate identity; exact supremum and infimum of norm-to-quadratic ratios; monotonicity in the one positive diagonal parameter; and off-diagonal exclusion via explicit lower and upper contact pairs. The limiting coordinate axes are included in the compact projective unit sphere, so infima and suprema are attained.

`verify_arc.py` checks five nondegenerate arcs spanning both regimes, analytically identified equality pairs, and 10,000 deterministic complex random pairs per arc. It runs using only the Python standard library and reports `ARC_HILBERT_FINITE_CHECK_OK`; it is corroborative only. The complete 2026 motivating preprint was not available during the comparison. No external or independent validation is claimed.
