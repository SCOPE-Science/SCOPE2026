---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On a strictly positive two-step orbit, the prey equations give y=λ−x−u/x, v=λ−u−x/u. Hence v−y=(x−u)(1−1/x−1/u), and x+u<2λ−2. For λ≤3 the reciprocal sum exceeds one by AM–GM, so unequal prey states force the opposite ordering of v−y to that required by h(x)h(u)=1 and nondecreasing h. Equal prey states force equal predator states, proving exclusion even at λ=3 without continuity. For each λ>3 one can choose z=2+(λ−3)/6, and x=z+ε,u=z−ε with both recovered predator states near Y=λ−z−1>0. Here v>y, so interpolating the reciprocal positive ratios v/y and y/v gives strictly positive slope. Its limiting intercept is 1−2(z−2)/Y in (0,1), as follows by writing the slope as (1−1/x−1/u)(v+y)/(vy). Sufficiently small positive ε preserves the strict inequalities and yields an exact period-two cycle. At r=1 the special h(x)=γx is still positive on x>0. The rational λ=4 witness was independently checked by exact substitution (both updates close); the supplied script was inspected, not run, and does not prove the universal threshold.

## originality

PASS

Credit the established plankton recurrence, the logistic boundary dynamics and the zero-intercept model. A later indexed paper gives exactly the affine-family frontier and goes further with a parameterization; this is genuine mathematical overlap, not evidence of an earlier covering publication. It states an affine theorem, while the original's exclusion is formulated and proved for arbitrary positive nondecreasing h, including nonsmooth and non-strictly-increasing cases. The strongest inspected earlier primary period-two calculation is on the invariant axis of the λ=2 model. The decision is for the original uniform theorem as a whole, with priority risk in the older overlapping-field literature.

## value

PASS

The growth threshold is for an entire monotone recruitment class, with no need for differentiability, a trapping region or restrictions on the particular positive two-step orbit. Demonstrating attainability on the positive affine subfamily makes the obstruction exact and nonvacuous. This is an existence frontier, not a stability or general global-dynamics claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
