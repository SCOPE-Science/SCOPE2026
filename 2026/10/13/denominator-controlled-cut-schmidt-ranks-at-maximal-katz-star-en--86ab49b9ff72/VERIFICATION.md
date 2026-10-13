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

The algebraic proof derives the exact Gram matrix from bipartite coefficients in Dicke bases and determines rank using Vandermonde nodes and modular residue cardinality. The exact purity follows from a binomial convolution. These steps cover all allowed \(m\), \(a\), and \(\beta\).

Execute `python3 verify_rank.py` with `numpy>=1.24` from `requirements.txt`. The verifier constructs the original Ising-evolved statevector independently for \(m\le8\), compares its nonzero reduced eigenvalues to the compressed formula, and checks purity, trace, positive semidefiniteness and predicted Schmidt rank across 510 cases. It independently exhausts 8,550 exact rational residue-class instances. The separate representative rank checks include a rational-versus-irrational difference at fixed subsystem size and a dimension-80 rational resonance. Expected output ends with `VERIFY_OK`.

Finite computations are supporting checks only; they are not an infinite proof or an independent audit. Numerical diagonalization becomes ill-conditioned when predicted nonzero eigenvalues are extremely small, so the all-dimensional Schmidt rank rests on the symbolic Vandermonde argument, not eigenvalue thresholding. No independent review or validation has been performed.
