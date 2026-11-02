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

# Mathematical and finite checks

`verify_random_routes.py` uses only Python standard library. It constructs the complete bipartite adjacency relation and checks the full set of geodesic intermediates for each fixed terminal pair. It then independently enumerates every assignment of geodesic midpoint choices for 47 bounded parameter triples with 2 <= N <= 4, compares direct vertex coverage with the symbolic inclusion-exclusion expression, and asserts the exact probability 1/9 for N=3,a=b=2 and 1369/4096 for N=4,a=b=3. Command: `python verify_random_routes.py`. The observed result was `VERIFY_OK instances= 47 including asymmetric source counts and original geodesic choices`.

Infinite-parameter guarantees do not rely on finite enumeration: the exact formula is inclusion-exclusion over missing nonterminals; the Poisson window uses all fixed factorial moments, and the zero-one thresholds use first/second moment inequalities. The deterministic comparator uses explicit injection of omitted vertices into same-side terminal pairs. No machine-checkable formal proof or independent external audit is supplied.
