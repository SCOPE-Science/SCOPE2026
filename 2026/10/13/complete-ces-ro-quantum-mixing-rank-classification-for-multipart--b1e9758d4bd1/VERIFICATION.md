---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The distinct-eigenvalue Cesàro expansion is a sum of positive semidefinite Schur squares, so the kernel is their common kernel. On normalized part indicators the adjacency quotient is ww^T-diag(n_i), with w_i=sqrt(n_i); it has no zero vector in its kernel (a zero-mode equation in part values gives S=rS). Thus the zero projector is exactly the direct sum of within-part zero-sum projectors, using the zero operator if the zero eigenspace is absent. On a part of size m its Schur square is (1-2/m)I+J/m^2, so for m>=2 it leaves only the m=2 contrast in the kernel. The -1 quotient equation is (n_i-1)a_i=S: with a singleton it forces S=0 and leaves exactly singleton contrasts, and without singletons division would require 1=sum_i n_i/(n_i-1)>1. The corresponding singleton block excludes all singleton directions for s>=3, leaves a single contrast for s=2, and is absent for s=1, where the positive Perron projector detects the lone singleton direction. Orthogonality makes every other projector have equal columns at the vertices of each proposed contrast, so squaring entrywise does not remove those null vectors. This proves exactly the claimed kernel and rank, including K2, all-singleton graphs, and repeated non-singleton sizes. The supplied numerical and rational checks were inspected, not executed; the unrestricted result follows from the checked algebra, not finite examples.

## originality

PASS

Credit the existing equal-fibre blow-up formula and the published complete-graph calculation. The finding passes only as the unified result for arbitrary part sizes and the interaction of the size-two and singleton exceptions, not as novelty of those subfamilies or of the spectral-projector machinery. Bounded comparison did not substantiate coverage of this general claim.

## value

PASS

The complete multipartite family is a standard uneven blow-up family in which symmetry alone leaves several possible null directions. The uniform kernel tells exactly which initial-vertex distinctions are lost by averaging, exhibits two different twin mechanisms, and gives a sharp positive-definiteness criterion even with mixed part sizes. This is useful beyond the balanced and complete cases and is not just a recomputation of those ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
