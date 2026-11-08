---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For independent Bernoulli p_i in [0,p], 0<p<=1/2, derive P(S=2)/P(S=0)=e_2(p_i/(1−p_i)). At fixed pair sum s=x+y and product v=xy, e_2=H+[Us+(1−2U)v]/(1−s+v); its derivative in v is [1−s−(2−s)U]/(1−s+v)^2. If e_2>=1, the contrary nonnegative derivative would force e_2<1 using H<=U²/2 and s<1, a contradiction. Thus reducing v at fixed s strictly increases e_2 and saturates one interior probability per step, reaching m full-cap parameters and one residual q. The saturated e_2 crosses 1 at minimal m with binom(m+1,2)(p/(1−p))²>=1; q=(1−binom(m,2)t²)/(mt+1−binom(m,2)t²), threshold T=mp+q. Strict compression establishes boundary uniqueness, perturbation gives sharp strict-event infimum; p=1/2 and p→0 limits verified. Independent exact-rational grid tested 6552 instances over six caps and lengths ≤6, including threshold and equality families. Testing is finite only.

## originality

PASS

PASS qualified for the capped sharp staircase and equality rigidity, explicitly excluding the known unrestricted reversal threshold and classical elementary symmetric sum identity. Full Kleiner 2026 text was inspected: general fixed-mean multi-affine reductions and unrestricted k=0,r=2 do not state this cap-saturated extremizer; a more general older cap-constrained theorem remains a residual possibility.

## value

PASS

This is a natural sharp cap-dependent refinement of an established Poisson-binomial point-mass reversal question: operational constraints on individual success probabilities shift the minimum mean from 1 to a nontrivial arithmetic staircase with a rigid extremal law. The threshold and distribution shape may be needed in bounded-risk Bernoulli comparisons, rather than a random isolated table value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
