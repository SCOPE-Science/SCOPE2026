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

# Reproduction checks

Run `python verify.py` using Python 3 standard-library modules. The script carries out 90 exact-rational configurations with \(3\le n\le12\), verifies the analytic endpoint resolvent identity and the minimum-diagonal property, and checks predicted entrywise signs in tested regimes. The explicit \(n=3\), \(z=7/10\) matrix is reconstructed by exact Gaussian elimination; all entries are strictly positive.

The universal all-size conclusion is derived in `RESULT.md` using a Stieltjes inverse, the path Green kernel, sine-diagonalization monotonicity, and a half-line limit. The finite code tests do not constitute an exhaustive certificate or an independent review. The additional oldest relevant cited proceedings paper was not inspected in full; its coverage remains uncertain.
