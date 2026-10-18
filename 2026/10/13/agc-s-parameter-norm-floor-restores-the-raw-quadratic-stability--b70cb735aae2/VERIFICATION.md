---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

From source AGC ratio |h x|/max(|x|,epsilon)>lambda, the small-norm threshold is |x|>lambda*epsilon/h and all three stated branches follow (continuous at a and epsilon). For 0<eta*h<2, each nonzero branch decreases |x| strictly; a nonzero positive asymptotic magnitude is excluded by continuity and strict decrease. For eta in [2/h,2/lambda], both proposed phases lie in the closed [a,epsilon] interpolation where gradient equals lambda*epsilon*sign(x), so x->x-s->x; endpoint a and epsilon agree with adjacent formulas. For eta>2/lambda the outer factor |1-eta*lambda|>1 is invariant for sufficiently large |x| and diverges. Independently used exact fractions h=5,lambda=1,epsilon=1/10,eta=1/2: a=1/50, s=1/20, x=1/40 gives x->-1/40->x. The infinity statement is universal convergence, not convergence of all intermediate trajectories to cycles.

## originality

PASS

Specific positive AGC parameter-norm floor changes scalar asymptotic stability ceiling from clipped curvature to raw curvature and exactly locates a cycle continuum; this source-specific conjunction was not identified in checked primary sources or relevant published records. Generic gradient clipping and elementary scalar sign-flip dynamics remain antecedents, not claimed new in themselves.

## value

PASS

The positive AGC parameter norm floor is an implemented safeguard for zero/near-zero weights; the sharp h rather than lambda stability ceiling and exact cycle band reveal a mathematical limitation of the very safeguard. This is a motivated source-specific discrete dynamical boundary rather than renaming a textbook scalar GD threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
