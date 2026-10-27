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

## Checks performed
The analytic proof in RESULT.md was reconstructed separately from finite computations. Exhaustive enumeration of all labelled simple graphs on 3, 4, 5 and 6 vertices at three exact rational edge probabilities checked the covariance identity for all component sizes 2 through n-1 and for tree-only components: 60 exact rational comparisons passed. The `verify.py` source permits repetition using only Python 3's standard library.

Separately, exact threshold formulas were stress-tested numerically for 123,753 adjacent size pairs over 3 through 500 vertices and against 24 fixed-component-size expansions; those checks are finite supporting evidence, not a substitute for the monotonicity argument or the asymptotic proof.

## Boundaries and unperformed checks
The graph-enumeration verifier only covers n<=6, not all n. The proof applies to arbitrary nonnegative internal component-type weights with positive expectation, not signed weights or weights involving outside edges. A prior 1990 tree-component covariance article could be read only at abstract level; historical priority remains provisional. Independent scientific audit has not been performed.
