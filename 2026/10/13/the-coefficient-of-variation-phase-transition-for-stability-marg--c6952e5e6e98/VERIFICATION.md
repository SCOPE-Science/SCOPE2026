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

The proof analytically handles every iid positive scalar curvature distribution of finite second moment, every \(0\le\beta<1\), every \(\eta>0\), and all deterministic initial pairs. All strict-boundary cases are included. The determinant identity is a finite algebraic identity, not a sampled probability estimate.

The self-contained `check.py` requires Python 3 and SymPy. Execute `python3 check.py` after extracting it from the same package. The checker symbolically reconstructs \(\det(I-T)\), the Lyapunov matrix determinant and exact conditional drift, the derivative and optimizer identity, and enumerates direct conditional expectations using exact `fractions.Fraction` arithmetic. The execution on the packaged source returned `VERIFY_OK` and 3,528 rational comparisons. These tests supplement but do not replace the analytic infinite-time convergence argument.

This verifies algebraic correctness, not that no earlier literature implies the low-variance optimum. Prior Appendix A Lemma 4 in arXiv:1803.05591 contains the matching necessary cutoff in its restricted high-variance model and is expressly acknowledged. No independent audit or external certification has been performed.
