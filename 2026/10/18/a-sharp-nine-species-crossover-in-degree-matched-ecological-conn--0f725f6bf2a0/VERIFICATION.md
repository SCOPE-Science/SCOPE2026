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
# Reproducibility checks

Execute `python3 check_robustness.py`. Only the Python standard library is required. The complete graph universe is finite: for every \(2\le n\le8\), each split \(a+b=n\) with both guilds nonempty is represented by all nondecreasing \(a\)-tuples of nonzero masks on \(b\) pollinators. This loses only redundant plant relabelings. Connectivity is checked directly; surviving subsets are exhausted, not sampled. For each graph, component sizes from disjoint-set union and graph flood fill agree for every surviving subset.

The checked small-graph totals, ordered by total vertex counts \(n=2,\ldots,8\), are \((1,2,5,18,89,590,5160)\) connected incidence-row profiles, in \((1,2,4,10,27,80,241)\) degree-signature groups. Their distinct coefficient vectors number \((1,2,4,10,27,85,285)\). All 55 comparisons between unequal vectors sharing a signature had a componentwise sign.

The two exhibited nine-vertex graphs are independently connected, degree-matched, and have coefficient vectors \((1,14,40,59,40,9)\) and \((1,14,41,58,38,9)\). Exact binomial expansion gives the difference polynomial \(2q-7q^2+8q^3-3q^4=q(1-q)^2(2-3q)\). A dynamic program checks matching equality for all 32 survival masks. These are finite exact certificates; no general claim for larger orders or stochastic models beyond the defined assumptions is verified. No independent audit has been performed.
