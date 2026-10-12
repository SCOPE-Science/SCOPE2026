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

The exact domain is a fixed nonconstant real sample of size \(n\ge2\) and an ordinary equal-weight nonparametric bootstrap resample of the same size.

The critical proof checks are:

1. Conditional on support size \(k\) and a fixed support set, ordered bootstrap labels are uniform surjections.
2. For two specified draw positions, the conditional same-label probability is
   \[
   \frac{\left\{\begin{matrix}n-1\\k\end{matrix}\right\}}
   {\left\{\begin{matrix}n\\k\end{matrix}\right\}}.
   \]
3. For exchangeable draws, expected unbiased sample variance equals one-coordinate variance minus two-coordinate covariance.
4. Averaging the within-support variance over a uniform \(k\)-subset cancels the finite-population factor and leaves exactly the displayed Stirling multiplier.
5. The covariance is independently reconstructed from multinomial multiplicities after centering the fixed data.

`checker.py` enumerates every ordered bootstrap resample for \(2\le n\le6\) for several fixed data profiles, computes the conditional means and covariance directly with exact rational arithmetic, and checks the formulas. It also verifies Stirling recurrences and coefficient identities over a larger finite range.

Finite enumeration is supplementary. The theorem for arbitrary \(n\) and arbitrary fixed real data follows from the symbolic counting and moment argument.

The result does not assert stochastic monotonicity or a full conditional law.
