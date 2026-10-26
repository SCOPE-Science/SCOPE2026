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

# Verification record

The proof is supplied in `RESULT.md`. The independently implemented `artifacts/verify_overlap.py` enumerates one-survey species masks by exact ordered-sample counts, then forms the product law of two independently drawn masks and computes \(\mathbb E[S]\), \(\mathbb E[U]\), and \(\mathbb E[SU]\). It checks the direct covariance against the closed formula for all \(2\le m\le6\), \(1\le n\le5\): 25 exact rational identities.

The separate discrete sign checks cover all \(2\le m\le50\) for every effort from \(n=1\) through ten beyond the first positive covariance length, comparing the formula and equivalent squared-ratio criterion; four small values are asserted exactly. All quantitative comparisons use Python integers and `fractions.Fraction`. The numerical decimal for \(\alpha\) is informational and does not certify its value; its characterization and limiting role are proved analytically.

To reproduce from the package root, run `python3 artifacts/verify_overlap.py`. The observed console output is preserved as `artifacts/VERIFICATION.txt`. Exhaustive checking is limited to the stated finite parameter ranges; the unrestricted monotonicity, irrationality, and asymptotic results follow from the proof.
