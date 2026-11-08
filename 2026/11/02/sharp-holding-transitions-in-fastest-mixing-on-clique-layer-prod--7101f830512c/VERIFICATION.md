---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Convexity of ||P-J||_op for symmetric stochastic matrices and the H-automorphism and fiber-permutation action proves a global optimizer exists in the two-edge-orbit class. In that class P=I-x L_H tensor I-y I tensor L_{K_s}, with x,y>=0 and d x+(s-1)y<=1. Every nonconstant spectral mode lies between 1-alpha*x, 1-s*y and 1-beta*x-s*y, so the exact objective is max{1-alpha*x,1-s*y,beta*x+s*y-1}. The first two constraints force x>=(1-u)/alpha and y>=(1-u)/s; substituting into the third endpoint and row budget gives M=max{beta+2alpha,2d+2alpha(s-1)/s}; x=2/M,y=2alpha/(sM) attains the bound. Active endpoint or budget yields uniqueness within the invariant class, not among all matrices. Johnson spectrum 0,n,2n-2 gives threshold s(n-3)<n including equality. The proof treats all connected vertex-and-edge-transitive H; finite spectral/LP tests are support only.

## originality

PASS

Qualified best-of-knowledge priority based on direct mathematical statement/implication comparison, with explicit named residual risks; none of the inspected prior statements dominates the final claim. Prior convexity and spectral sums make the result derivable, but deriving a sharp two-parameter minimax and locating the holding phase requires solving the independent-orbit constraints; the prior edge-transitive single-edge formula cannot directly be applied when two product factors are inequivalent. This is a qualified incremental, mathematically useful exact specialization rather than a new FMMC method.

## value

PASS

A sharp design and holding-phase classification over arbitrary connected edge-and-vertex-transitive base graphs with clique-layer augmentation, including a concrete Johnson-graph integer frontier. The exact weight allocation and universally active spectral/budget constraints resolve an optimization problem, rather than merely displaying a generic SDP formulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
