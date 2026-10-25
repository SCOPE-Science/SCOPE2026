---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The agent-level rate-one voter first-moment equation is ẋq=−D^(-1)Lq with root fixed, where L is positive definite grounded combinatorial Laplacian and D is the nonroot full-degree matrix. Integration from all-negative initial state gives La=d, hence cumulative dissent 1^T L^(-1)d, equal to the sum of fixed-root mean hitting times. A nonroot edge adds bb^T to L and e_u+e_v to d; substituting Sherman–Morrison yields the stated rank-one response with denominator 1+b^TPb>1. Independent Fraction Gaussian elimination across ALL connected labeled graphs and roots n=2,3,4 checked respectively 0,3,168 missing-nonroot-edge insertions, all 171 nonvacuous deltas strictly positive (minimum 2). For the five-vertex tree 01,04,12,23, hitting-time vectors before (5,8,9,1), after adding 24 (4,6,7,4), sums 23 and 21. Root-attached leaves each contribute exactly one independent unit of expected dissent in both graphs, extending the witness to all n>=5. The 16-state voter-chain certificate independently corroborates n=5.

## originality

PASS

Best-of-knowledge: the underlying voter/walk correspondence and inverse update are known techniques, but inspected related zealot control and Kemeny constants do not supply the exact fixed-target integrated dissent insertion sign or the sharp five-agent threshold. Kemeny averages a random stationary target rather than one immutable root. Resultary semantic search returned no directly covering mathematical statement.

## value

PASS

Cumulative negative-opinion person-time is a natural, explicitly normalized transient cost under an immutable source. The result identifies the smallest network size where adding an ordinary peer link can SPEED conversion, despite universal worsening in all smaller networks, with an all-graph rank-one response to test interventions. The first failure at five and extension to arbitrary orders are mathematically motivated structural features, not merely an inverse-matrix exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
