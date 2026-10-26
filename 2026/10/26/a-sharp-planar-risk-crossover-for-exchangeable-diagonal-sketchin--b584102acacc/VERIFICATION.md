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
# Reproducibility and checks

Execute `python3 verify_xdiag.py` using Python 3 and the standard library. The checker uses `fractions.Fraction` to independently reconstruct the leave-one-out projector and each diagonal estimate for all \(16\) pairs of two-dimensional Rademacher vectors. It compares the enumerated squared error with the closed rational risk and checks the four-probe BKS risk by sign enumeration on 60 positive-definite rational inputs. It also checks the cubic risk-difference identity, representative strict inequalities, derivative signs on rational points, and a five-dimensional diagonal-matrix witness. The recorded result was `PASS: 1208 exact-rational assertion families; all pairwise sign cases included`.

The proof of the universal one-crossing theorem is the derivative and endpoint argument in `RESULT.md`; the checker does not exhaustively verify real parameters. The high-dimensional arbitrary-ratio theorem follows analytically from a finite-sign-set continuity argument, not from extrapolating experiments. This verification does not assess finite-precision QR implementations or all alternative estimators. No independent scientific audit has been performed.
