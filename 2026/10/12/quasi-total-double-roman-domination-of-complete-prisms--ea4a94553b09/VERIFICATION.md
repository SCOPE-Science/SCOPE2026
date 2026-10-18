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

Directly checked the definition: a zero needs adjacent 3 or two adjacent 2s; a 1 needs adjacent >=2; an isolated positive may only be 2. For a total weight <=6 and n>=4, any layer weight <=2 forces too much weight in matched opposite-layer vertices, hence layer weights >=3. At equality each layer weight 3 cannot be 2+1 (remaining zeros demand >=2 in opposite layer) nor 1+1+1 (zeros or unsupported 1s); each layer has a unique 3. Nonisolated-positive condition forces matched indices. Independently exhausted all 4^8=65,536 labelings for n=4 and all 4^10=1,048,576 for n=5: respective optima 6 with exactly 4 and 5 matching minima. Analytic lower bound covers all n>=4.

## originality

PASS

Source determines paths, cycles, complete multipartite and small general value ranges; these do not supply the complete prism minimum-function classification. A published Roman-{3} complete-prism result is about a distinct labeling rule and cannot imply this value/count.

## value

PASS

Natural Cartesian-product family exhibits a constant sharp weight and a rigid complete optimizer classification with n labeled solutions. This extends the graph-domination invariant beyond cycles/multipartite examples, not merely a small isolated value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
