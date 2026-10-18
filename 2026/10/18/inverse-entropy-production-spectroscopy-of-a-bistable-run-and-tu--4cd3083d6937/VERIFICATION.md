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

# Verification and scope

The mathematical argument in `RESULT.md` derives the stationary response from the exact Fokker--Planck equations, then applies the spectral theorem for the reversible equilibrium diffusion. The crucial identities are \(Kx=-f\), \(\langle x,Kx\rangle_\pi=T\), \(\|Kx\|_\pi^2=b^2\), and the direct Gibbs integral for \(\operatorname{Var}(X)\). Strict concavity and the inverse two-parameter classification are analytical consequences, not numerical extrapolations.

To run the reproducibility supplement, place `CHECK.py` beside this document and execute `python CHECK.py` with NumPy and SciPy. The program passed 116 assertions on four physical parameter combinations. Checks include reversible-generator matrix positivity consequences, two algebraically independent resolvent formulas, strict numerical derivative signs, exact Gibbs-integral quadratures, and limit-coefficient consistency on a finite spatial grid.

Finite spatial truncation and discretization do not prove the continuum theorem, asymptotic rate limits or injectivity for all parameters. Exact weak-propulsion linearization assumes \(|v|<b\), unique stationary solutions, and the stated order of limits. The origin of the entropy-production normalization is stated explicitly. The relationship to established exact steady-state EPR formulas and residual uniqueness-of-literature risks are disclosed separately in `RESULT.md` and `REVIEW.md`.
