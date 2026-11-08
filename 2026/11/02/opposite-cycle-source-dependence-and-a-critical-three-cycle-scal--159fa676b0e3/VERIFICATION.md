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

Condition on a specific cycle Γ: k forced outgoing arcs hit only cyclic vertices, and t labeled complement targets can only be avoided by t free vertices with probability (n-t)/(n-1) and by remaining n-k-t free vertices with probability (n-t-1)/(n-1). Multiply and count ordered t-tuples to reconstruct E[(Z)_t | Γ]. With E Ck=(n)_k/[k(n-1)^k], E Z=n b^(n-1), b=(n-2)/(n-1), obtain exact Cov=(n)_k/[k(n-1)^k] b^(n-k-1)[n-k−n b^k]. Direct rational g(2)=(n-2)/(n-1)^2>0, g(3)=(3-2n)/(n-1)^3<0 and g(k+1)−g(k)<0 for k≥1 prove all signs. Expansion at fixed k yields the exceptional k3 order n^-2. Independent exact enumeration covered every fixed-point-free mapping n=3..6 including conditional factorial tests for constrained small cycles. Formula at k=n uses b^-1 but n≥3 ensures b>0; no singular boundary.

## originality

PASS

Classical mappings with cycle/tree exponential generating functions and generalized diagonal-bias models contain related statistics, but a specified-cycle conditional source-count factorial-moment law and all-length covariance sign reversal with critical k=3 coefficient were not found in inspected published statements. General marked-EGF methods could yield it after explicit derivation.

## value

PASS

Strongly motivated dependence question: local sources and cycles in fixed-point-free random mappings have a sign reversal that disappears when self-loops are allowed; k=3 has an analytically explained cancellation. Exact finite-support conditional law and asymptotic scales are useful distributional invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
