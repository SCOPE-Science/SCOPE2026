---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For independent image choices with diagonal probability q and uniform off-diagonal probability r=(1-q)/(n-1), conditioning on the exact loop set S leaves n-f independent nonself choices. A specified subset R of s non-loop vertices is origin-free of incoming edges with probability ((n-s)/(n-1))^s ((n-s-1)/(n-1))^(n-f-s). Multiplying by (n-f)_s and mixing F~Bin(n,q) establishes the entire joint factorial-generating polynomial, including n=2 and q=0,1 via polynomial extension. A direct ordered-pair expectation gives Cov(F,L)=n q(1-q)(1-r)^(n-2)(1-nq)/(n-1), so the interior sign flips at q=1/n. For n>=3 the conditional mean g(n-f) with g(k)=k((n-2)/(n-1))^(k-1) rises f=0->1, ties f=1,2, and then falls. Checked independent exact rational enumeration for all n^n maps with n=2,3,4 against the factorial coefficient and covariance, including q=0 and q=1. Finite checks corroborate, not prove, the all-n counting proof.

## originality

PASS

The independent-choice diagonal-biased model itself is old; the assessed claim is its full loop-origin factorial law, exact covariance phase and conditional regression plateau. Compared the classical origin/cycle generating functions and same-bias model rather than relying on title matching. No inspected theorem implies the full biased one-cycle/origin law, but earlier detailed local-statistics papers remain priority risks.

## value

PASS

The same natural local statistics (one-cycles and indegree-zero vertices) undergo an exact positive-to-negative correlation transition in the classical independent-image model, while being dependent exactly at zero covariance. The full joint law and a nonmonotone conditional expectation make a mathematically useful phase classification not implied by a first-moment or routine covariance identity alone. The theorem is exact at all finite sizes and includes boundary conventions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
