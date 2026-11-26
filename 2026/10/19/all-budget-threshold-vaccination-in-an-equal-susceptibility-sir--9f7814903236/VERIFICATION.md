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

The nonnegative integrated removals are bounded by initial susceptible plus infectious mass, so bounded beta/mu implies finite integrated force. The stable infectious equation with integrable incidence gives I(t,x) tending to zero. Integrating then yields H=B+T(1-exp(-H)), and the surviving mass is m+(S-m)exp(-H). Convexity, the negative value at zero when B>0 and the positive asymptotic slope give one positive root; at that root T exp(-H)=(H-B)/(exp(H)-1)<1. Thus at fixed m<S minimizing remaining weighted exposure strictly improves the objective and the threshold exchange integral gives all equality cases, with arbitrary allocation on the cut level. Adding a positive feasible increment strictly increases survival, so the budget is saturated, including the endpoints. The rearrangement and implicit differentiation give the frontier and its positive marginal term, regular through T=1. The inherited dynamic-control conclusion is about a supremum, not attainment; at the full endpoint it also follows by taking lower budgets tending to S and using S as an upper bound. Independent bounded bisection reproduced the reported two-group survivor masses 1.853622849292 and 1.574692330951. This is corroboration only; the continuum claim rests on the proof and the dynamic equivalence on the cited theorem. Uploaded code was inspected, not run.

## originality

PASS

Pass for the exact all-budget allocation and finite-seed survivor frontier, including through and beyond the critical-exposure value. The priority ordering, tie handling in the restricted regime and the equality of dynamic and initial suprema are already in Almeida–Ducasse–Paparelli and are not credited as new. The primary theorem and its proof expressly restrict the budget for threshold optimality, with the all-budget extension posed as a possibility. Inspected analogues optimize another objective or operate in an approximation regime. This is a bounded best-of-knowledge decision with the stated access risks.

## value

PASS

The extension resolves a specific open regime in the cited model: finite-seed survivor optimization at budgets that can drive post-vaccination exposure through one. It provides a constructive exact allocation and continuous scalar frontier rather than a simulation, and clarifies why the marginal benefit has no singularity there. The common-hazard, perfect-vaccine objective bounds its practical interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
