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
# Verification evidence and limits

The executable `verify_biclique_stabilization.py` was run from the package build directory with NumPy. It reported:

```
ALL_BALL_SELECTOR_EXHAUSTIVE_CHECKS_OK 3969
SELECTOR_CLASS_COMPRESSION_CHECKS_OK 5832
EXACT_MODE_WITNESS_DIAGNOSTICS_OK 84
NONNEGATIVE_RANDOM_INPUT_DIAGNOSTICS_OK 2500
TWO_TERM_LARGE_CLASS_ASYMPTOTIC_OK
ALL_EVENTUAL_BICLIQUE_MAXIMAL_CHECKS_OK
```

The first count enumerates every radius selection on several small complete bipartite graphs; the second uses the exact finite selector-class compression; the third tests analytic positive singular vectors against the nonlinear maximum; the fourth checks a reproducible sample of input vectors. All these are finite checks. The proof's globally quantified assertions, including the large explicit threshold, depend on the upper-bound/selector-stabilization inequalities in `RESULT.md`, not on enumeration. No external or independent validation is asserted.
