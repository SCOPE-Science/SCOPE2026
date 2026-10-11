---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The ratio e-value is strictly increasing from zero to \(n+1\), so solving \(1-\lambda+\lambda e(v)<h\) gives exactly the all-positive or finite-interval dichotomy and the displayed endpoint. Differentiation proves strict endpoint decrease on the finite branch. Since the infimum over positive candidate scores of post-batch wealth is \(W(1-\lambda)\), the reserve condition is exactly \(\lambda\le1-R/W\), and choosing the largest feasible fraction minimizes the current set. Fresh independent rational checks reproduced the endpoint classification and reserve inequality over randomized parameter instances.

## originality

PASS

Gauthier--Bach--Jordan's primary paper gives the same ratio e-value and explicitly introduces predictable fractional products \(1-\lambda_s+\lambda_sE_s\), while choosing the all-in process for simplicity and flagging alternatives as worth exploring. The inspected source does not state the finite-score-set phase transition, monotonic endpoint formula, or worst-case one-step reserve frontier. Targeted Resultary search did not locate an equivalent sequential reserve/efficiency theorem.

## value

PASS

The source explicitly identifies fractional betting alternatives as a direction worth exploring. The theorem resolves the natural one-step tradeoff between current-set efficiency and guaranteed future wealth, including an exact boundedness phase transition and sharp reserve frontier. That is a motivated structural analysis of the published procedure rather than an arbitrary algebraic slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
