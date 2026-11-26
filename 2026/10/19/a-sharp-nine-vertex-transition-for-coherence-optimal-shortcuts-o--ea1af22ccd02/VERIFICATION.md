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

Replayed the trace gain directly by series/parallel effective resistances: the drop for a vertex pair is its squared clipped-ramp separation divided by d+1/w. Summing gives the centered variance and parity penalty. The all-span affine difference is positive at zero weight and, at W_n, its factorization is strictly positive except at tail sum t=2 (the t=1 parity case is separately positive). The slope for t=2 is negative beyond W_n; n<=8 has nonnegative slopes. Thus the only critical tie is the endpoint and {1,n-2}, with W_9=7/4. Sequential convergence of normalized gain, including d/n going to zero, and the unique maximum of x/4-x²/6 give the span and both normalized trace limits at every fixed w>0.

## originality

PASS

The strongest located exact placement result is for the unit shortcut, and already gives the same asymptotic locations and trace at w=1, plus a stronger finite-n placement law on that slice. The weighted-cycle result is not a path augmentation result. Neither those statements nor the generic Laplacian update settles the prescribed arbitrary-w first transition and exactly two critical optimizers. This pass is for the distinct weighted path comparison, not the generic identity or a novelty claim for the w=1 subcase in isolation.

## value

PASS

This is a natural test of whether joining the largest-resistance pair optimizes a standard network objective: nine is the first possible counterexample size, with an exact conductance scale and the complete critical tie. The limiting geometry quantifies an appreciable one-eighth improvement in leading coherence cost versus the endpoint design. Both are usable design facts; no claim that optimizing spectral gap or multiple chords has been solved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
