---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The unnormalized Laplacian has four orthogonal invariant components with eigenvalues 0, b on A-zero-sum, a on B-zero-sum and a+b on part contrast. The signed heat-distribution difference for an A vertex x and B vertex y has positive mass at x and other B vertices and negative at y and other A vertices for t>0. Transport on graph metric has cheap cross-part cost1, costly same-part cost2; the excess imbalance forces cost2 |s_x-d_y|, giving W1=E+2 max{(a-1)(U-E)/a,(b-1)(V-E)/b}; for a>=b its first branch wins. The explicit fixed potential f(x)=2, f(other A)=0, f(all B)=1 is 1-Lipschitz and realizes this cost for all t, establishing exact dual and operator norm. Differentiating gives derivative sign [-2m(M-1)+(M-2)(M+m)e^{-Mt}]/M, with initial threshold M-m-2, a unique root only if M-m>2, and explicit t*, peak; K1,1 direct case exp(-2t). Independent original heat eigensystem plus Kantorovich dual LP for 75 graph/time combinations agrees to 3.8e-15. Tests finite, all-time result analytic.

## originality

PASS

Best-of-knowledge comparison after fresh Resultary searches, focused primary-source proof inspection and explicit implication checks. A related method, family or parameter alone does not establish identity/coverage; historical risk remains noted.

## value

PASS

The graph heat semigroup is supremum-contractive yet can transiently increase spatial Lipschitz slopes. The exact all-time phase diagram, nontrivial threshold in part imbalance, universal fixed norming potential, and sharp peak tending 2 give meaningful stability information missing from infinitesimal graph curvature alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
