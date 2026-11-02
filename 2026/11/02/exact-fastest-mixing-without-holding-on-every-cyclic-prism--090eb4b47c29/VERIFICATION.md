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

# Verification and scientific limits

The proof uses symmetry averaging of the spectral norm and an explicit two-branch Fourier diagonalization, followed by an exact minimax balance. Its critical inequalities reduce to \(\varepsilon_n\le\delta_n,\Lambda_n\le4\), valid for all odd \(n\ge3\). Every even prism has a bipartition sign eigenvector with eigenvalue \(-1\), independently of edge probabilities.

Run `python3 verify_loopless.py` using only the Python 3 standard library. It recomputes the eigenvalues from independent trigonometric formulas over finite samples and checks that the proposed weights attain the analytic bounds. Finite computations do not prove the infinite statements. No independent audit has been performed.
