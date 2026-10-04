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

The packaged script `verify_nested_ccsmcs.py` uses only Python's standard library and exact rational arithmetic. It checks the following finite identities and examples:

- the suffix-maximum lower closure and prefix-minimum upper closure;
- the necessary-and-sufficient compatibility criterion for an interval box intersected with a nonincreasing order cone;
- equivalence between the original lower-endpoint possible-feasibility rule and the order-aware rule under nonincreasing tolerances;
- the strengthened certified-feasibility condition based on prefix minima of shifted upper endpoints;
- the strict two-method example in which the rectangular projection contains two methods while the order-aware exact projection is a singleton.

The checker exhausts a finite family of rational two- and three-level boxes and compares the formulas with direct enumeration on a rational grid whenever the grid contains feasible points. It also verifies the displayed strict example exactly.

Finite enumeration is not used as proof of the infinite statement. The analytic proof in `RESULT.md` establishes the coordinate extrema and the constrained-argmin implication for arbitrary finite \(R\), while the sequential coverage claim is inherited from the original simultaneous confidence event together with deterministic nesting.
