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

# Reproducibility

The standalone `verify.py` uses SymPy 1.14.0 as specified in `requirements.txt`. From the directory containing the files, execute `python verify.py`.

It reconstructs the exact row-orthogonal factorization and equal normal matrices; the rare-row expanding certificate \(W\), the positive-definite excess \(D\) with determinant \(163/1800000\); the positive-definite decay certificate \(C\), its block determinants \(50703/100\) and \(8191/100\), and the exact Lyapunov identity; and the common first-moment eigenvalue moduli.

The certificate identities are rational or algebraic identities over \(\mathbb Q(\sqrt3)\). Their sign consequences establish the infinite-time claims analytically. They do not rely on enumerating stochastic sample paths. No independent audit has been performed.
