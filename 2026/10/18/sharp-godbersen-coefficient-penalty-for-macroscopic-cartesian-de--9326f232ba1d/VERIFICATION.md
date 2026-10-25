---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: for compact full-dimensional K_i in R^{d_i}, m>=2, 1<=j<=n-1, the Minkowski polynomial of the Cartesian product factors exactly into factor volume polynomials. The established sharp Godbersen inequality bounds each factor coefficient q_{i,h} by binomial(d_i,h)^2; positivity gives the exact B_{d,j} bound. Simplices attain simultaneously. If any d_i>=2 factor is nonsimplex, the published interior strict equality theorem and h_i=max(1,j-(n-d_i)) produce a feasible strictly smaller coefficient summand, so equality forces all simplex factors. Dividing the convolution by binomial(n,j)^2 is exactly the self-collision probability of multivariate hypergeometric block counts; no missing normalization. For fixed m, d_i/n->alpha_i>0, j/n->beta in (0,1), uniform Stirling on n^{1/2+1/10} windows, exponential hypergeometric tails and the Gaussian determinant 1/prod(alpha_i) give n^{-(m-1)/2}[4*pi*beta*(1-beta)]^{-(m-1)/2}/sqrt(prod alpha_i). Independently checked 23 small coefficient polynomial/collision integer identities and limiting numerical direction. Critical published Godbersen inequality/equality is an explicit external premise, not reproved; finite checks do not prove the asymptotic or all-body inequality.

## originality

PASS

PASS best-of-knowledge: the 2026 Godbersen solution supplies the factor bound and simplex equality, and Alon–Elboim–Pach–Tardos supply related collision-exponent mechanics. The distinctive claim combines an exact sharp arbitrary-convex-factor product extremum and explicit all-proportion/all-interior-index leading constant. Source comparisons found no dominating implication; priority is qualified, not certified.

## value

PASS

PASS: Cartesian product is a natural stable convex-geometric construction after the recent universal Godbersen bound. The exact worst-case product coefficient, equality class and macroscopic n^{-(m-1)/2} cost quantify how factor count changes extremal reflected mixed volumes (two factors n^{-1/2} vs three n^{-1}), independently useful even though local-limit methods and probability exponents are established. Not a renamed universal theorem or an arbitrary dimension slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
