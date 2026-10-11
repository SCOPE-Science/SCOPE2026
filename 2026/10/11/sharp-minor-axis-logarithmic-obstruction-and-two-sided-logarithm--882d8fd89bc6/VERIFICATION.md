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

# Reproduction and logical checks

Run `python3 verify_ellipse.py` with Python 3's standard library only. The script constructs the geometric translation families for five axis ratios and two displacement parameters, checks normalized disk inclusion and physical-length constraints, and prints `VERIFY_OK: 38000 randomized finite checks` on success.

The analytic proof checks: (i) the exact minor-axis interval calculation and sign separation; (ii) uniform logarithmic width of interval ratios above the scale cutoff; (iii) overlap of the geometric progression and its last-index bound; (iv) both central-square subcases and the quadratic factor inequality in the remaining case; (v) the compactness lemma via interior endpoints; and (vi) the infinite-coverage obstruction at the circumradius. The finite verifier alone establishes none of the asymptotic quantifiers. Its tolerance accounts only for ordinary floating-point roundoff. No formal verification or independent audit has been performed.
