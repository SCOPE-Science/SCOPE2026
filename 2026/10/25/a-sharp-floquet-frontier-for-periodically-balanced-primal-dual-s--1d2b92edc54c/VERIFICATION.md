---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Independently reconstructed the elimination x_k=(y_k-y_{k-1})/sigma_{k-1}, reached arbitrary (y_1,y_0) from (x_0,y_0), and derived companion M_r(q)=[[1+q-2r,r-q],[1,0]]. Direct exact matrix multiplication recovers trace 2(1+2r^2-r(1+S)) and determinant 1+r^2-rS of M(1/t)M(t). Schur quadratic margins are r(S+2-3r)>0, 4+5r^2-2r-3rS, and r(S-r)>0, so strict stability is equivalent to the claimed frontier for all r in (0,1), S>=2. At equality -1 is a nonzero neutral eigenmode and beyond it one eigenvalue<-1, with no unreachable eigenvector loophole. SVD decouples square invertible matrix modes; convex minimization of S_c(r)=4/(3r)+5r/3-2/3 gives r=2/sqrt5. Independently reproduced the rational strongly convex two-step matrix and characteristic polynomial with negative value at -1 and nonzero excitation minor; proves divergence of an explicit initial state. Finite direct-iterate checks only confirm identities, not asymptotic necessity.

## originality

PASS

Best-knowledge PASS for the exact period-two dual-extrapolated Schur frontier, its sharp all-spectrum minimum and strictly convex witness. Existing work already observes variable-step PDHG divergence under subcritical products, so qualitative divergence is NOT novel. Chambolle et al convergence requires additional quasi-increase hypotheses violated by the permanent alternating schedule. Goldstein et al use related but differently extrapolated methods; Resultary fixed-product PDHG optimization uses constant step pairs; generic two-periodic recurrence energy-norm estimates are not this spectral stability frontier.

## value

PASS

A necessary-and-sufficient stability boundary for a standard primal–dual update under two-periodic step contrast, with a sharp dimension-free safety cutoff and an admissible interior worst singular mode, is structural, nontrivial parameter information. Its explicit strongly convex divergence witness rules out a tempting but unsupported stabilization heuristic. It has algorithm-design relevance distinct from the already known observation that variable steps can sometimes fail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
