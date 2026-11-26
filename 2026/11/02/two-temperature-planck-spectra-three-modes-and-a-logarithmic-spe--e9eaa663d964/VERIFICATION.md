---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The frequency-law normalization is correct: R^-2 x^3/(exp(x/R)-1) = R f(x/R), so the hot term contributes f'(x/R) to the derivative. The single-Planck sign change follows from strict concavity of 3(1-exp(-x))-x; f'' is negative near a, positive near zero, and positive on [5,infinity) by the explicit second-derivative formula. For fixed small delta and eta, these signs give strict decrease of F_R' on [a,a+delta], strict increase on [5,eta R], and strict decrease on [(a-delta)R,aR], with opposite endpoint signs in each case. On the intervening intervals signs are uniform by compactness or exponential decay, and outside (a,aR) there is no zero. This proves the quantified root count and nondegeneracy, not by numerical sampling. Uniform slope at the cold root first gives x1-a=O(1/R), justifying its Taylor remainder; on the hot interval the slope is bounded above by -c/R, so the shift from aR is O(R^4 exp(-aR)). For the notch, F_R' is eventually negative at any fixed X>=5 and positive at any fixed small t times R, so x2 diverges with x2/R tending to zero. The derivative balance gives x2-2 log x2 = log R-log 2+o(1); first x2/log R tends to one, then substitution gives the subleading terms. The hot Rayleigh–Jeans contribution x2^2/R dominates the cold term 2 x2/R at the notch. Taylor estimates at both maxima also give the stated heights.

## originality

PASS

The supported distinction is exact large-contrast critical-point multiplicity together with the notch's logarithmic location (including the second logarithm and constant) and algebraic height for the specified frequency-domain scaling. The examined primary and catalogue statements do not cover that combination or imply it by a specialization. Neither mixtures themselves nor the single-temperature Wien law are new here.

## value

PASS

The exact sum is a motivated two-temperature radiative model: the weight keeps the hot low-frequency derivative small around the cold peak while allowing a dominant hot peak. Resolving the entire axis distinguishes true bimodality from simply locating two approximate peak scales. The notch location and height quantify how the exponential cold tail and algebraic hot tail meet; neither the Wien displacement relation nor a peak-sampling diagnostic yields this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
