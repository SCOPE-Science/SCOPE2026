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

The standalone arithmetic checker can be executed with `python3 checker.py`. Its complete finite checks are:

- For the canonical four-point affine plane cap, enumerate all \(\binom83=56\) four-character sets containing zero and obtain the five exact characteristic-polynomial multiplicities \(16,4,16,16,4\).
- For the four affinely independent points, enumerate all \(\binom{26}{3}=2600\) four-character sets containing zero, and verify that exactly eight have the equality-case Gram coefficient \(90\) and characteristic polynomial \((t-7)(t-3)^3\).
- Reconstruct three representative Gram characteristic polynomials directly in the integer ring \(\mathbb Z[\omega]\), \(\omega^2+\omega+1=0\), and verify exact optimizer counts in the representative dual spaces.

The checker completed successfully and printed `CHECK_PASS`. It uses no numeric eigenvalue approximations; the analytic trace-square inequality proves the infinite-dimensional family result after affine-span reduction. A finite census alone would not prove a statement about general ambient dimension without that reduction. This verification does not include an independent mathematical audit and does not claim the absence of equivalent earlier publications.
