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

The theorem follows from a unique solution of the finite-dimensional Lyapunov equation \(K^\dagger X+XK=-I\), verified entry by entry in the proof. Absorption is certain because no eigenvector of the path hopping matrix can vanish at the lossy endpoint, ruling out neutral modes of the no-jump generator.

Run `python verify_path_absorption.py` (Python 3, SymPy, NumPy, SciPy). At packaging review the program passed 39 exact full-matrix Lyapunov identities for \(2\le n\le14\), with three rational parameter pairs per length, and 33 numerical Lyapunov cross-checks for \(2\le n\le12\), with three real parameter pairs per length. The script additionally checks Hermiticity, all diagonal formulas and strictly negative real parts of the numerical generator eigenvalues. Finite checks are not the proof for unbounded \(n\).

The exact rate optimum is proved by minimizing the positive \(\gamma^{-1}\)-plus-\(\gamma\) formula for each nonabsorber initial site. No independent scientific audit or empirical experiment was performed. The result is specific to a single-particle open path, homogeneous hopping and one endpoint loss channel.
