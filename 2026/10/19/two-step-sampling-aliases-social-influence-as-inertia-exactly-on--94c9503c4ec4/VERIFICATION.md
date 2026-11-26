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

Fix any initial configuration. Independence and finite fields give a full-support product law for the intermediate spins. Conditional covariance of distinct outputs reduces to covariance of their intermediate-state mean functions. When they share a neighbor, both mean functions are strictly increasing in its spin, and nondecreasing in every other spin. Conditioning on the shared spin, the first covariance term is nonnegative by induction on the remaining independent coordinates; the second is strictly positive since both conditional means strictly increase and the shared spin is nondegenerate. If there is no such pair, every vertex has degree one under the graph hypotheses. Its partner map is bijective, so the output coordinates use distinct independent intermediate spins and separate second-step noise. Each binary channel has mean tanh(beta/2) times its input; the composition has mean tanh(beta/2)^2 times the initial spin, giving the asserted parameter. Equality of the two-step kernels extends to the even-time path laws, with the same starting law. The path witness reduces to the shared-spin variance, including the stated rational values.

## originality

PASS

The supported distinction is the exact all-initial-state two-step product-kernel boundary and inertia alias for the given model. Closest inspected results concern one-step model specification, stationary sublattice factorization, or stationary one-site time series, not the stated conditional transition-kernel equivalence.

## value

PASS

Exact even-time aliasing limits mechanistic inference even with the complete transition kernel. The graph classification and strict covariance witness identify when the alias breaks, beyond merely giving an example of indistinguishability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
