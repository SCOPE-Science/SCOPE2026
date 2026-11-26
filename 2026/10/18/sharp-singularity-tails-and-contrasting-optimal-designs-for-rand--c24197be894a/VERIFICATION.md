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

Cauchy–Binet gives the sum of squared pair sines. Write theta=t·1+z with sum z=0; then the sum of squared pair differences is m||z||². On the folded interval, |sin u|≥2|u|/π, and the larger Gram eigenvalue is at most m, so the small-eigenvalue event is globally confined to ||z||≤πε/2. Near that diagonal the determinant is m||z||²+O(||z||⁴) and the larger eigenvalue is m+O(||z||²), giving the claimed transverse unit ball. The Jacobian is sqrt(m); after rescaling, dominated convergence applies for every interior t even if f vanishes, and endpoints have zero longitudinal measure. In the uniform m=2 case λ=1−cos|θ1−θ2|, and triangular integration gives leading coefficient 2sqrt(2)/L, an exact normalization check. Strict Jensen gives the unique continuous minimizer. Integrating the positive tail coefficient gives the strict inverse-moment cutoff for s>0, including divergence at equality; conditional OLS risk is σ² times the sum of the two inverse eigenvalues, so it is finite exactly for m≥4. The iid pair expectation follows from the double-angle cosine; zero mean of e^(2it) forces support on the endpoints by its positive interior imaginary part, and then equal masses. The singular probability is the probability all endpoint draws agree.

## originality

PASS

The supported distinction is the exact folded-angle coefficient for arbitrary continuous densities and the associated finite-sample conditioning and design conclusions. The nearest circular-sketch result uses the same transverse mechanism, and the expected-determinant optimum itself is ordinary two-regressor D-optimality; neither is credited as a new general principle.

## value

PASS

The smallest eigenvalue controls noise amplification in this minimal support-reconstruction model. Its exact design-dependent tail distinguishes rank almost surely from finite mean-square error and singles out a continuous optimum. The contrast with the D-optimal design, which creates a positive singular mass, is substantive and interpretable even though the expected-determinant calculation alone is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
