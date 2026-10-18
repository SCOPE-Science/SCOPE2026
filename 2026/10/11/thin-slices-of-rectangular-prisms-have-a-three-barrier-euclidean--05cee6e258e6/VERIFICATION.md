---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For n>=3, 0<k<C and positive integer capacities c, affine translation space 1-perp has projected coordinate normal norm sqrt((n-1)/n). Exact lower facet criterion k<C-c_i and upper facet criterion k>c_i were proved from residual-coordinate interior feasibility. If delta=min(k/n,(C-k)/n,c_min/2), each minimal barrier forces enough actual facets for an upper bound: all lowers, all uppers, or both sides of a minimum-width coordinate. Conversely intervals [delta,c_i-delta] are nonempty with total lower <=k and upper >=k, giving a feasible center whose distance to all actual facets is sqrt(n/(n-1))*delta. All incenters are precisely feasible points satisfying shifted actual-facet inequalities. Boundary equalities and strict unique-center regimes were checked; finite rational active-set cases corroborate only listed inputs.

## originality

PASS

Ferroni–McGinnis develops the exact source family for Ehrhart/polymatroid problems and does not give its intrinsic Euclidean Chebyshev radius or full center polytope. Equal-capacity hypersimplex formulas, general Chebyshev linear programming, and non-isometric integer equivalences to fat slices do not directly imply the all-capacity three-barrier classification. Broader affine box-section radius theorem remains a genuine residual literature risk.

## value

PASS

The statistic is the natural Euclidean inradius of Veronese-polymatroid base polytopes, with complete all-capacity answer, exact transitions between mass/co-mass/narrowest facet obstructions and entire incenter family. An elementary LP reduction is not by itself a reason to reject a motivated new exact geometric classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
