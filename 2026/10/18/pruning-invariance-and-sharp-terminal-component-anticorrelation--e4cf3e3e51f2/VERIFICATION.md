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

# Verification record

Run `python verify.py` with Python 3 standard library from the same directory. The embedded code exhaustively enumerates all functions on \(n=1,2,3,4,5,6\) vertices, including 46,656 at \(n=6\). It compares complete conditional factorial-component distributions, individual cycle-length covariances, total-component covariance, and cyclic-point tail probabilities using `fractions.Fraction`. It checks exact monotonicity of the component mean through \(n=500\) and a floating numerical consistency estimate at \(n=10000\).

Observed successful output ended with `CHECKS_OK 644`, and the numerical covariance estimate was `-0.18317329873045785`, compared with the analytical target `-0.18393972058572117`. These tests do not constitute a proof for arbitrary \(n\) or of the asymptotic limit. The proof in `RESULT.md` supplies the universal pruning argument, stochastic coupling, finite moment comparisons, and asymptotic domination estimates. No independent audit has been performed.
