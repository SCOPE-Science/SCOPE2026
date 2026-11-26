---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The tensor projectors for the two complete-graph Laplacians have joint eigenvalues 0,p,q,p+q and give the four entry classes. Exact symbolic replay with python3 /workspace/checks/rk4_algebra.py verified A=h f, A−B, C, both quadratic discriminants, 3ac−b², and the fixed-sum derivative and its discriminant. For h>0, B>A and C>0; the scalar RK4 polynomial is positive on the nonpositive real axis by the exponential Taylor remainder, giving positive diagonals. The positive certificate 3ac−b² forces f′<0, giving a single crossing, A=0 at H and A<0 thereafter, with stochastic row sums where all entries are nonnegative. At fixed N=p+q, the derivative quadratic has positive leading term and negative discriminant bounded away from zero by the endpoint p=N/2 estimates, hence f grows with p at every h>0 and its zero moves strictly right. In the scaled limit N→∞ and p/N→r, dividing the derivative certificate by N⁴ leaves at least the strictly positive term 36(1−r)⁴ in 144(3ac−b²)/N⁴, so the limiting cubic is strictly decreasing and compact-interval convergence brackets the limiting root. The Euler-endpoint polynomial in I−hL verifies the strict improvement. 'Fixed-vertex-count' in the proof heading is a wording slip: the theorem and calculation fix p+q (degree plus two), not pq. The supplied verifier was inspected, not executed.

## originality

PASS

The strongest checked earlier RK4 archive result has complete multipartite, not Cartesian-product, graphs; the checked same-day rook-graph results study different operators. The later balanced strongly regular graph result does not cover unequal rectangles. The exact controlling entry, the strict comparison at fixed sum, and the resulting nontrivial scaled root are not established by these comparisons. This assessment is bounded by the general-theory access risks below.

## value

PASS

Fixing p+q fixes the graph degree and thus the forward-Euler threshold. Along that natural comparison the exact classical RK4 endpoint detects anisotropy that the Euler criterion cannot distinguish. The all-step comparison of transition classes identifies the first failure and rules out reentry; the scaled root gives a quantitative asymptotic version beyond finite examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
