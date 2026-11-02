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

# Reproducible mathematical verification

The included `verify.py` is a standalone Python 3 script depending only on the standard library. From its own Bell-number binomial recurrence, it constructs exact integers through \(B_{803}\) and evaluates the covariance numerator at every \(4\le n\le799\). The reported computation completed with **849 exact assertion groups/instances**, confirming negative signs at all 232 sizes \(4\le n\le235\), positive signs at all 564 sizes \(236\le n\le799\), and the strict integer inequality \(5B_{801}<801B_{800}\).

An independent Stirling-number recurrence reproduces the first crossing moments and covariance at \(4\le n\le15\). A separate restricted-growth-word generator enumerates all set partitions for \(4\le n\le8\), constructs successor arcs directly, and compares exact covariances with the closed Bell expression. Rational inequalities enclose the covariance at the two adjacent boundary sizes. All comparisons relevant to certification use arbitrary-precision integers or exact fractions, not floating-point tolerances. The approximate printed boundary values are for display only.

To reproduce, run `python verify.py` in a directory containing the extracted file. The proof for **all** \(n\ge800\) is analytic: real-rootedness of the Touchard polynomial and the cited normalized-Bell log-concavity theorem supply the necessary inequalities. The finite script's successful termination is not presented as a substitute for that proof. No external or independent audit has been performed.
