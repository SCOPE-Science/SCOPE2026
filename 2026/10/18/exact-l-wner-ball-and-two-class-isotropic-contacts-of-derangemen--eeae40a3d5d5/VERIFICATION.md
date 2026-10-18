---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

The theorem's proof gives all-dimensional arguments. A separately executable scientific checker is bundled as `verify_derangement_ellipsoids.py`. It requires Python 3 and NumPy and can be run with `python verify_derangement_ellipsoids.py` in its extracted directory.

The checker constructs the bipartite row/column incidence matrix, the orthogonal projector onto the zero-margin tangent space, and its constant diagonal. For each \(n\in\{3,4,5,6,7\}\), it enumerates relevant conjugacy classes, builds their exact rational design weights and numerical covariance matrices, and checks the isotropy equation, vertex norms, and the squared outer radius. All five tested orders passed, with residual less than \(2\times10^{-14}\). The \(n=3\) test covers the one-dimensional boundary case, which is not part of the principal statement.

Finite matrix calculations do **not** prove the theorem for arbitrary \(n\). The proof of global Löwner optimality requires the pair-module irreducibility and analytic conjugacy-class mixture. The literature comparison relies on inspected source passages and the precise nonimplication arguments documented in the accompanying review.
