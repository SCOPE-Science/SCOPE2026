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

# Reproducibility and scientific verification

Run `python3 check.py` using the Python 3 standard library; no third-party package is required. The checker reconstructs the fourteen candidate vertices from the explicit coordinate model, verifies the twelve four-vertex facet sets, deduces all twenty-four genuine edges by two-facet incidence, and checks their exact squared lengths. It then verifies by rational arithmetic that all ninety-one pairwise vertex-height differences keep a fixed sign on each of seven triangular normal subchambers. Sweeping thirteen height gaps on each chamber confirms exactly the three rows of piecewise-linear offset-length coefficients in RESULT.md.

The checker evaluates oriented spherical triangle first moments from cross products and geodesic edge lengths, comparing the resulting seven integrals with their closed forms to within `2e-14` absolute tolerance; this floating-point comparison is a numerical confirmation of the separately stated analytic moment formulas. It verifies positivity, total mass and mean side count. A separately sampled, width-weighted collection of 120000 affine planes compares the numerical frequencies to all seven exact probabilities. The stochastic experiment is corroborative, not a proof of the formula in infinitely many directions.

The actual delivered-checker run produced:

```
RATIONAL_CHAMBERS_OK vertices=14 facets=12 edges=24 triangles=7
EXACT_FORMULAS_OK classes=3..9 expectation=6
p3=0.040224879850928
p4=0.133974596215561
p5=0.161886425232915
p6=0.298680246894837
p7=0.191034375739269
p8=0.163122546721916
p9=0.011076929344573
WEIGHTED_RANDOM_PLANES_OK samples=120000
```

The proof uses exact rational subdivision and analytic spherical identities; finite checks do not imply any claim about all directions on their own. Equality and boundary planes have zero invariant measure and are not classified. No independent mathematical audit or definitive historical-priority adjudication is claimed.
