---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independently verified the factorial-moment reduction. For the quadratic part of the benefit, the factorial second moment of K+1 differs from that of the defector's K by 2(n−1)(i−1)(N−n)/[(N−1)(N−2)]; the linear moment difference is (N−n)/(N−1). With the specified cost and coefficient these give the displayed affine payoff gap and then κ(2i−N) exactly on balance. Reflection swaps birth and death probabilities, including at the boundaries where only exploration remains. The chain is irreducible for the stated μ range, with positive stationary weights; the detailed-balance ratios give reflection symmetry and fixed cooperator mean. On each upper-half interior edge for κ>0 the numerator is nondecreasing and the denominator strictly decreasing with w. At i=N−1 it is the numerator that is strictly increasing while the denominator is fixed. This includes N=3 (only the boundary comparison), even N (the zero-gap center still has a strict denominator), and odd N (the central edge joins identical deviations). The signs reverse when κ<0, and rates are constant in w for κ=0. Since folding only multiplies by intensity-independent multiplicities, successive upper-half ratios give all stated strict likelihood-ratio inequalities. Positivity and normalization make each proper upper tail strict: the weighted average of the increasing likelihood ratio on the upper tail is larger than the overall average one. The variance and heterozygosity identities follow by centering. Independent exact replay: python3 /workspace/branches/independent_replay.py 5, which reproduced all three rational witness laws and their variances. The supplied finite checker was inspected, not used to infer any of the infinite-parameter quantifiers.

## originality

PASS

Credit Hauert–McAvoy for the underlying nonlinear payoff, finite sampling, Fermi and exploration rules, and the numerical balance threshold in a fixation comparison. The supported distinction is the exact strict selection-intensity comparison of the entire folded stationary law, at arbitrary fixed positive exploration below one on that balance surface, not the model, threshold alone, or a qualitative change in modality.

## value

PASS

The balance isolates changes in spread without changes in mean cooperator count. A strict ordering of the entire folded law answers a stronger and operationally different question than fixation bias, modality, or the sign of a weak-selection derivative: every proper polarization tail and every nonconstant increasing polarization statistic move in the same direction for all finite intensity pairs. The standard stationary-ratio argument is short, but it is the modeling constraint and exact finite-population comparison that supply the substantive conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
