---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For strictly positive real additive valuations of two agents on a path, the actual proof distinguishes global Pareto dominance by all allocations from dominance restricted to connected allocations. At m<=2 singleton splits yield EF1 and one undominated split; at m=3 eight utility vectors are compared in five exhaustive cases after normalizing a>=c by path reversal. The strict inequalities rule out simultaneous domination of all EF1 candidates. For m=4, v1=(1,1,1,1), v2=(1,2,2,1): each one/three connected split fails EF1, each two/two cut has (2,3) strictly Pareto-dominated by disconnected endpoint/middle allocation (2,4), and all-to-one fails EF1. Chore transfer exchanges bundles and complements each cost, conserving connectivity, EF1 and Pareto dominance. Independent exhaustive positive integer search of 819 profiles for n=1,2,3 with weights 1..3 and exact four-item witness reproduced this; enumeration is not the proof for arbitrary reals.

## originality

PASS

Best-of-knowledge PASS: the earlier Igarashi–Peters five-item binary example is a path obstruction but involves zero values, and their four-item example uses nonadditive valuations. Their general connected Pareto efficiency is not global Pareto efficiency against disconnected allocations. The specific sharp four-positive-additive-item obstruction, including the m<=3 universal lower bound and chores dual, is not implied by the inspected earlier theorems.

## value

PASS

PASS: connected EF1 allocation versus globally Pareto efficient allocation is a natural fairness/efficiency compatibility problem. Sharp four-item minimality for arbitrary strictly positive additive valuations (not merely a witness) and an exact chores duality identify a meaningful first obstruction for two agents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
