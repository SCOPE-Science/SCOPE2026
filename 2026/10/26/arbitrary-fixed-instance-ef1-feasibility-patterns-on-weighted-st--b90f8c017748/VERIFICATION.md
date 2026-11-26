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

For 2≤k≤m−1 there is exactly one bundle containing the hub and r=m−k+1 leaves; all other bundles are singleton leaves. Only a leaf can be removed from the hub bundle since r≥2. Common nonnegative additivity therefore gives exactly the inequality min(outside) ≥ c + sum(inside) − max(inside), with no additional constraints from singleton comparisons. Every r-subset has an outside leaf among the first r+1 and its r−1 smallest terms sum to at least the first r−1 weights. The r smallest leaves attain both bounds simultaneously, proving the criterion including ties and zeros. At k=m the hub and a least leaf form an edge and the hub can be removed; the other endpoints are automatic. In (3) the first new leaf is at least 9, and consecutive new leaves differ by a_r plus the difference of two signs, at least a_r−2>0; this verifies the strict ordering directly. The intermediate gaps are ±1 and leaf order and positivity persist in a neighbourhood. The witness has thresholds with gaps −1,+1,−1 in order k=2,3,4. For a connected graph with a common additive valuation, k=v−1 is always feasible by pairing a globally least-valued vertex with a neighbour and deleting the neighbour in envy comparisons; Chen–Zwicker verify the stronger arbitrary-monotone guarantee used in the manuscript. Thus for v≤5 at most two consecutive counts are eligible for infeasibility, so the separation phenomenon cannot occur on fewer vertices.

## originality

PASS

The supported distinct claim is the exact weighted fixed-profile criterion and arbitrary strict spectra for outer EF1, including the minimal two-gap witness. Prior universal star spectra and an exact ordinary-EF1 weighted-star catalogue match are material overlap. They do not yield the submitted criterion or establish those spectra under connectivity-preserving deletion.

## value

PASS

The result resolves the sharp fixed-instance question behind the universal star spectrum. It yields both a test for arbitrary common nonnegative weights and a complete robust classification, not just an isolated pathological example. The six-vertex boundary gives a smallest connected graph on which failures in a fixed profile can form separated intervals; the endpoint theorem alone does not furnish such an example. This distinction between fixed and universal spectra prevents a false implication from the graph-wide spectrum conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
