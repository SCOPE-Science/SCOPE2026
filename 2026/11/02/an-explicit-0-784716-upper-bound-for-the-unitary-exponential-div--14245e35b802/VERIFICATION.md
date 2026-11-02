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

# Verification and limits

Run `python3 verify_upper.py` in a standard Python 3 installation. The script makes all prime powers, rational ceilings, finite convolution weights, and the three rational numeric comparisons independently using exact integer and fraction operations.

Expected output begins `VERIFY_OK prime_count= 168 states= 153387 cutoff= 51991 offset= -52491`; it reports `finite_probability_bounds: P<784271/1000000, omit<145/1000000, tail<300/1000000` and `density_upper_strict: 0.784716`. Combining the three strict components gives the theorem's \(\delta<0.784716\), not merely \(\delta<0.785\).

The program does not enumerate all integers or independently prove the Erdős–Wintner theorem. The proof of limiting density, continuity at zero, prime-exponent dominance, and the Chernoff bound are supplied in `RESULT.md` and should be scrutinized mathematically. Independent validation has not been performed.
