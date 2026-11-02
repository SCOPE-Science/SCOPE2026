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
# Reproduction and verification

Use Python 3 with its standard library only:

```text
python3 verify.py
```

The checker independently constructs the labelled graph for each path-length tuple, tries all vertex subsets, and tests the original \(P_3\)-convexity condition that every omitted vertex sees no more than one selected neighbor. Separately, a four-state word transfer counts locally admissible memberships under the endpoint-capacity filters. For the equal-length-three family a third, symbolic coefficient construction implements the closed binomial formula.

The full polynomial, not only its value at one, was compared on all six equal-length-three networks with \(3\le r\le8\), where the vertex set has \(2r+2\) vertices. Each also passed cardinality-support checks and top-degree coefficient tests. Twelve mixed-length theta graphs with path lengths two through five passed direct-to-transfer coefficient comparison. The expected totals at \(r=3,4,5,6,7,8\) were \(64,137,292,625,1344,2897\). The execution terminates with `VERIFY_OK`.

The exhaustive checks are finite and do not establish the unbounded \(r\) or arbitrary-length theorem. The written binary-neighborhood decomposition, terminal-capacity filtering and exact four-case counting prove those assertions. No independent external mathematical audit has been performed.
