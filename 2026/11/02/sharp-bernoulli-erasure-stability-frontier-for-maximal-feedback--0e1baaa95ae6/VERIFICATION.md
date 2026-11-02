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

# Reproduction and limits

The attached `verify.py` defines both exact update matrices, constructs the complete symmetric second-moment matrix directly, and checks its factorized characteristic determinant at one. It independently verifies the two-dimensional Lyapunov identity and its positive determinant. It then compares the transfer matrix with exhaustive erasure-path enumeration over 28 finite rational horizon/parameter cases. Finally, it tests selected spectral radii and the exact step-size root, including the no-compression case. The program executed successfully with Python 3, SymPy and NumPy. Exact finite tests and numerical spectral values do not establish the infinite theorem; the spectral, Lyapunov, positive-map and invariant-subspace proof in `RESULT.md` is essential.

To repeat: install dependencies from `requirements.txt` with a standard Python environment, then run `python verify.py` in the same directory. Results are deterministic; no downloaded datasets, external credentials, remote services, or random seeds are needed.

The main boundaries are strict: \(q\in(0,1]\), \(\gamma>0\), and \(\eta=1\). At \(q=1\), uniform stability means convergence for every initial three-state vector, rather than divergence for every exceptional vector outside the stable region. The result is about mean-square convergence, not almost-sure trajectory growth or performance of nonlinear objectives. Publication-priority verification remains qualified.
