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

# Verification

The algebraic proof is self-contained in RESULT.md. The coefficient dictionary is \(b_{ij}=2A_{ij}\), giving \(E=2\|A\|_F^2-\sum_i|A_{ii}|^2\); Takagi factorization and real spectral diagonalization show \(\sup_{\|z\|_2=1}|z^TAz|=\|A\|_{\mathrm{op}}\). Symmetric orthogonal/unitary extreme contractions are sufficient by explicit sign-mixture decompositions. The real Fourier projection example has diagonal \((n+1)/(2n)\), so its reflection has diagonal \(1/n\) and the predicted sharp energy. The complex three-dimensional cofactor relation is checked directly from \(\operatorname{adj}U=(\det U)U^*\); it yields the optimal lower bound \(\delta\ge1/3\). The 5-point Fourier construction is exact because \(1+4\cos\theta=0\), and the reflected eigenvalue sequence makes the unitary symmetric.

As a supplementary finite check, numerical matrix calculations in dimensions one through nine confirmed the expected squared coefficient values, with symmetry/unitarity residuals under \(2\times10^{-14}\); these floating-point observations do not certify the general theorem. The formula is not extended to other polynomial degrees, other domain exponents, or alternate coefficient normalizations. The focal full text was unavailable, so novelty retains the specific literature risk identified in REVIEW.md. No external audit has been performed.
