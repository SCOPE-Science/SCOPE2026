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
# Verification

The identity \(F_t=2(s-ts^{(4)})\) is checked symbolically and independently by direct numerical integration. The partial-fraction relation is tested with truncations of lengths 1000, 5000 and 20000, allowing an explicit \(O(1/N)\) truncation bound rather than treating a finite sum as an identity. Root residual and localization checks cover representative parameter regimes but cannot prove the complete classification; the proof in `RESULT.md` handles all parameters and infinitely many zeros.

Run `python check.py` after installing the exact dependencies stated in `requirements.txt`, and compare with `check_output.txt`. There is no external or independent mathematical verification certificate.
