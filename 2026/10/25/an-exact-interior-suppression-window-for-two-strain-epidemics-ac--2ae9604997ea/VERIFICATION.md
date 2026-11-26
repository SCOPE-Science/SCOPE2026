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

Poisson thinning gives the stated type-indexed mean offspring matrix; for Poisson layers the excess-degree means coincide with the respective original means. The larger quadratic eigenvalue is the Perron root, including the reducible diagonal and periodic off-diagonal endpoints. The claimed second derivative is positive when h>0, and the endpoint derivatives are −max(c,d) and q−s. Equality q=s gives a unique endpoint, while h=0 gives the stated affine exception. To fix the sign of the interior minimum, put A=h²+q² and u=t−h²/A. The normalized root is sq²/A−su+sqrt(Au²+h²q²/A). A stationary point requires u>0 and gives u=shq/[A sqrt(q²−cd)]; substituting yields the positive-sign L*, with t* also obtained from characteristic-polynomial tangency. Strict convexity puts L* strictly below both endpoint values, giving precisely the open total-degree range for strict suppression and supercritical pure endpoints. In the example the smaller determinant root is greater than 1/11, so I−M is positive definite between the two roots and has largest M eigenvalue exactly 1 on their boundary. Outside, its determinant is negative. The example's seed can reach the supercritical class in both pure cases; no claim about arbitrary seeds at the reducible endpoint, or about finite-epidemic outbreak size, is required. The strict subcritical interval does not say that critical boundary points survive.

## originality

PASS

The prior two-layer branching model and the qualitative phenomenon of suppression between supercritical pure regimes receive no novelty credit. The distinctive result on the inspected evidence is the sharp fixed-budget suppression classification and concrete interval for the particular Poisson model. The framework is prior; the exact allocation theorem is not a threshold formula stated in different notation.

## value

PASS

A fixed total budget is a natural control constraint for prevention; increasing the number of contacts would be a different question. The iff criterion separates the endpoint regime from strict interior suppression, and the witness identifies a regime in which neither pure allocation suffices. This is a usable decision boundary for the stated early-emergence model, rather than the routine act of diagonalizing a 2×2 matrix or claiming a general effect of layered interventions. The deterministic preserve/switch and Poisson assumptions sharply limit interpretation; no finite-outbreak or agent-specific conclusion is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
