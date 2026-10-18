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

# Verification and reproducibility

Run the standalone standard-library program `python3 verify.py`. It uses exact `fractions.Fraction` arithmetic throughout; no network access, hidden data, scientific package, or particular operating system is required.

The program independently constructs the projectors of the complete bipartite Laplacian, groups equal-eigenvalue projectors, checks their exact idempotence, mutual orthogonality and identity resolution, constructs the spectral entrywise-square matrix, and evaluates the exact \(\ell^1\) residual. Its exact reference expression is the proved two-case formula. The program covers 64 positive size pairs with \(m,n\le8\) and six further stress cases, including balanced and singleton parts. Observed successful execution:

`VERIFY_OK 70 exact projector/rational-residual cases; limiting optimum 24/125`

Separately, direct double-precision symmetric eigendecomposition was used for all 361 pairs with \(1\le m,n\le19\), checking agreement to better than \(10^{-10}\). This independent matrix route does not replace the exact-arithmetic checks or the proof.

The continuum all-size assertion, the \(m=3\) sign threshold, and the macroscopic optimum are proved symbolically in `RESULT.md`. Finite checks cannot certify all \(m,n\), the time limit, or priority against unpublished research. The analysis treats \(t\to\infty\) before changing graph size, assumes \(\gamma>0\), and makes no uniform relaxation-time or experimentally noisy-measurement claim.
