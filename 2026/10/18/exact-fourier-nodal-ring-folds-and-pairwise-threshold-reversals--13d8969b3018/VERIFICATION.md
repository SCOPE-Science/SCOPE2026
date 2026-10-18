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

The analytic proof in `RESULT.md` reconstructs all objects and hypotheses. For reproducibility run `python verify_circle.py` using Python, NumPy and SciPy. The actual recorded output appears in `verification_output.txt`.

The checker solves the stationary equation \(2arJ_0(r)-J_1(r)=0\) on 45 sampled negative Bessel lobes, checks the sign of \(4a-1-4a^2\rho^2\), compares exact critical heights against the leading asymptotic, computes numerical critical heights for three index pairs on both sides of their crossover, and exhibits two roots below a sampled critical value in each of six lobes. Each root evaluation uses numerical special functions and a scalar bracketing solver; no interval-arithmetic certification is claimed.

The proof of one fold in **every** lobe follows from Bessel's ODE and the strict-negative stationary logarithmic Hessian. The proof of unique pairwise crossings follows from the strict envelope derivative and endpoint ordering. The proof of the sharp fold mass comes from large-argument Bessel expansions. Finite computations do not establish any of these infinite statements; they are independent finite corroboration only.

All characteristic-function parameters are fixed in the formulas: \(\operatorname{Cov}(\gamma_a)=2aI_2\), \(\widehat\mu(\xi)=\int e^{-2\pi i\xi\cdot x}\,d\mu(x)\), and \(r=2\pi|\xi|\). The result excludes \(t=0\) and \(t=1\); limits to those endpoints are asymptotic statements only.
