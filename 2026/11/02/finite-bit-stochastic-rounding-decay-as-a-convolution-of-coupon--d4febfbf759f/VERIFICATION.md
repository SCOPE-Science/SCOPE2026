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

# Reproduction and scope

Run `python verify.py` with Python 3; the script uses standard-library rational arithmetic (`fractions.Fraction`), combinatorics, and no external dependency. The executed result was `PASS 70 rational identities and exact distributions across dyadic grids`.

The independent finite-state Markov recursion was compared coefficientwise with a convolution of coupon-collector probabilities expressed through Stirling numbers of the second kind for all \(1\le r\le p\le4\), up to explicit finite horizons. All exact mean, variance, and absorbing-plateau formulas in these cases were checked, as was exact identity with ideal rounding probabilities for \(1\le p\le6\) and \(r\ge p\) (three tested budgets per precision). The case \((p,r)=(4,2)\) has exact values \(\mathbb E\tau=91/3\) and \(\operatorname{Var}(\tau)=520/9\).

The code does not exhaust every possible precision or prove an infinite distributional limit. The analytic proof is by independent holding times, grouping, classical coupon-collector convergence, and variance concentration. The stochastic update convention is an exact mathematical model of fixed-point probability truncation; hardware behavior is not checked.
