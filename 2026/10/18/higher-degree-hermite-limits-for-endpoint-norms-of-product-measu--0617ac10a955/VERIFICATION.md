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

For fixed k and a fixed compact marginal with at least k+1 support points the orthonormal tensor basis exists, including for atomic laws. In a kernel row the terms other than the degree-k square-free sector have O(d^{k-1}) uniformly bounded, orthogonal coefficients, hence O(d^{(k-1)/2}) error in L1. If a_i=(x_i-m)/sqrt(v), normalize the leading sector by d^{k/2}; the resulting inputs to the elementary symmetric polynomial are a_i Z_i/sqrt(d). On any subsequence with mean a_i^2 tending to q, their first power sum tends in law to sqrt(q)Z (or zero in L2 for q=0), their second tends to q in L2, and each fixed higher power sum vanishes deterministically. Newton's identities give q^{k/2}H_k(Z)/k!; orthogonality gives a uniform second-moment bound (mean a_i^2)^k/k!, justifying absolute expectations. Compact subsequences give the global upper limit, a repeated farthest support point attains it, and strict increase in q yields both directions of rigidity. A sign-of-kernel input realizes each row's absolute integral; continuity and full support identify the max with the essential-supremum operator norm, and symmetry with L1 duality gives exact finite-d endpoint equality. Independent replay `python /workspace/branches/independent_audit_replay.py` confirms the four numerical coefficients by Gaussian integration at Hermite roots, not the infinite-dimensional theorem. The bundled checker, inspected but not executed, counts 1278 pointwise kernel comparisons plus three Hermite moment checks; the text's description of 1281 kernel comparisons conflates these without affecting the theorem.

## originality

PASS

The supported contribution is the fixed higher-degree theorem for general compact marginals with its complete near-maximizer criterion. Its uniform-cube specialization explicitly overlaps another record, and both the degree-two product result and the interaction projection result anticipate key mechanisms. None of those statements gives this full combination of degree, law, operator and evaluation geometry. No novelty is assigned to endpoint duality, Newton identities, or the elementary-symmetric-to-Hermite method.

## value

PASS

The endpoint norm quantifies worst-case amplification under fixed-order polynomial chaos truncation as dimension grows. A sharp constant and a necessary and sufficient maximizing geometry valid across nonsymmetric continuous and discrete laws go beyond a cube constant or an upper bound. The change to centered energy is meaningful for asymmetric laws, where a farthest endpoint may be unique. No finite-d optimizer, rate uniform in the marginal, or growing-degree result follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
