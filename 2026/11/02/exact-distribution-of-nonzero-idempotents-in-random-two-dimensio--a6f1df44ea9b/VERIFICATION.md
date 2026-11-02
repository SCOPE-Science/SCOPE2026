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

Run `python3 verify.py` using only Python 3's standard library. The script independently enumerates every invertible \(2\times2\) matrix over the prime fields of orders \(2,3,5,7\) and extension fields of orders \(4,8,9\), constructs the projective fixed-line count, and compares all four frequency classes against the closed formulas using exact rational arithmetic. It also validates multiplication in each finite-field implementation. Its successful marker is `VERIFY_OK`.

Run `python3 verify_direct.py` as a separately implemented check: it loops through all nonzero coordinate vectors over \(\mathbb F_q\), for \(q\in\{2,3,5,7\}\), tests the raw idempotency equations, and reproduces all four frequencies without using projective reduction. Its successful marker is `DIRECT_VERIFY_OK`.

The recorded outputs `verification_output.txt` and `verification_direct_output.txt` were produced by these exact files. All-dimensional and all-prime-power assertions rely on the proof of projective fiber counts and sharp three-transitivity, not on finite-case extrapolation. The historical-novelty assessment is limited by the scope and accessibility of the checked literature; no independent audit has been performed.
