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

Forced adjacent numeric successions make each labeled position block an increasing interval of consecutive values. Every ordering of the blocks on the value axis assigns disjoint intervals uniquely, including permutations with extra unforced successions. Thus the event has probability b!/n!, block ranks are uniform and each reversed pair contributes weight w_ij=ℓ_iℓ_j, giving the full conditional histogram and mean. For independent uniform ranks in continuous representation, subtract (U_i−U_j) from the centered indicator on pair i<j. The residual has variance 1/12 and zero conditional mean given either argument; distinct residuals sharing one argument are orthogonal by conditional independence. Summing the linear coefficients ℓ_i(Σ_{j>i}ℓ_j−Σ_{j<i}ℓ_j) and residual squares gives the general variance. Independently, for a single run at an endpoint the count is an independent sum of the inversion count of h singletons and L times a uniform integer on {0,…,h}. The endpoint variance is h(h−1)(2h+5)/72+L²h(h+2)/12. For i<j<k the three shared-index comparisons have covariances +1/12, −1/12, +1/12 in order (ij,ik),(ij,jk),(ik,jk). Moving the long block between two of the singletons changes the triple contribution by (2L−2L²)/6, leaving all other variances and triple contributions unchanged. Hence placement a reduces the endpoint variance by L(L−1)a(h−a)/3, yielding exactly the stated formula and gap, including h=0,1. The independent endpoint decomposition gives the centered uniform n²-scale limit, as the singleton count has O(n³) variance. At a nearest center the h-scaled polynomial part has a positive cubic coefficient when L/n→λ∈(0,1), and the position term is only O(n²); variance is Θ(n³) and the centered n²-scaled variable vanishes in L². A separate enumeration through n=6 checked all forced sets, conditional histograms, moments and single-run extrema (266 finite checks; no saved script). It can be reconstructed by tabulating permutations satisfying each set and enumerating orders of the labeled blocks for comparison. The supplied script and its reported 505 assertions were inspected, not executed.

## originality

PASS

The distinct contribution is the inversion refinement and, in particular, the exact placement-dependent variance and differing endpoint and central fluctuation regimes. Prescribed-succession block ordering is known, and the weighted count itself follows directly by recording inversions in that bijection; the review does not credit contraction or the event count as novel. The closest sources inspected do not supply the weighted covariance sum, the quantitative placement law, or the endpoint/center comparison for this conditioning.

## value

PASS

The conditioning event is a standard permutation statistic and total inversions are a natural test of its global effect. A constant conditional mean across positions conceals a sharp and quantifiable dependence in variance: with the same asymptotic forced fraction, only a change of position separates n⁴ variance with a nondegenerate uniform limit from n³ variance and no n²-scale fluctuation. The formula measures that effect exactly and gives a usable benchmark for structured permutation models; proving a full lower-scale central law is not necessary for this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
