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

# Verification scope

The finite exact checker is `verify.py`, executed with `python3 verify.py`; it passed 1,901,150 exact assertions. It independently enumerates all permutations of sizes two through eight, checks the constant fibre cardinality \(i\), the conditional image set, all footrule tail inequalities, and exact rational means and covariances. The five convex nondecreasing functions checked are \(t\), \(t^2\), \(t^3\), \(\max(0,t-1)\), and \(\max(0,t-3)\). Checks are finite, and do not independently certify the claimed infinite result.

The mathematical proof covers every integer \(n\ge2\) and every \(i\in\{2,\ldots,n\}\) using an explicit counting map, convexity under each inversion-removing adjacent swap, and elementary expectations for maxima of uniform subsets. No external formal certification has been performed. The comparisons to historic literature are a self-review only.
