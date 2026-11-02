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

# Reproducibility and scientific scope

Run `python verify.py` using Python 3.10+ with SymPy 1.12 or newer. The program checks stationary entry events via a second, independent enumeration of all \(3^{M+1}\) words for \(M=3,4,5,6\) (rather than simply substituting the displayed entry formula), then checks the exact elementary-symmetric identities and derivatives, the uniform Hessian coefficient for lengths three through nineteen, and the algebraic optimizer conditions at six. Recorded stdout is in `verification_output.txt`.

The proof's statements for infinitely many window lengths do not follow from enumeration; they follow from the positive recurrence for \(Q_M\). Strict Schur-concavity is proved by explicit bounds on pair-transfer derivatives. Completeness of the six-draw optimizer list follows from compactness, an interior stationary-point reduction, strict convexity of the critical quartic, and a transverse instability calculation. Numerical root approximations have no role in establishing existence, uniqueness or optimality.

The present analysis does not claim independent mathematical auditing or historical-priority certification.
