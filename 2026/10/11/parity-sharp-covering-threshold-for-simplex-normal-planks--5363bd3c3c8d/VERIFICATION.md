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

The exact covering threshold is proved for every integer \(d\ge2\) by a zero-sum tight-frame coordinate transformation, a sharp two-sign-group Cauchy--Schwarz inequality, and a complete case split on the parity of \(d+1\). Equality witnesses are explicitly reconstructed as unit vectors and their antipodal count is elementary combinatorics. Homogeneity proves the claim for the entire unit ball, not just its unit sphere.

Run `python3 verify.py` from the directory containing this file and `RESULT.md`. The script uses only the Python 3 standard library; it checks the rational squared-threshold identities, all possible sign-group sizes and equality patterns in dimensions \(2\) through \(50\), and seeded numerical samples in dimensions \(2\) through \(15\). The expected last line is `SIMPLEX_PLANK_PARITY_CHECKS_OK`. Finite tests cannot certify the infinitely many dimensions; the written proof does.

The literature comparison distinguishes an exact fixed-normal threshold from general necessary sums-of-widths inequalities and the opposite min-max simplex problem. A publicly announced 2026 source was accessible by abstract but not by its complete manuscript, leaving a documented comparison risk. Independent audit has not been performed.
