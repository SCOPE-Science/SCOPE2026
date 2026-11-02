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

# Reproducibility and limits
Run `python verify.py` from the extracted package using SymPy. The script constructs stationary generator equations for \(M_{ij}=\mathbb E[x^iv^j]\) at even total degree and \(L_{ij}=\mathbb E[x^iv^j\sigma]\) at odd degree, through degree four, solves each finite nonsingular symbolic system, and checks both variance and both fourth-cumulant formulas exactly. It also checks large- and small-stiffness standardized limits, exact derivative formulas defining monotone zero counts, and 32 rational parameter evaluations. The local executed source printed `PASS: exact fourth-cumulant identities, limiting ratios, monotone sign polynomials, 32 rational samples`. The mathematical proof of root uniqueness rests on strict analytic inequalities, not sampling.

The exact stationary fourth cumulants of the binary telegraph model are not the same as those for continuously orienting active Brownian particles, even when their covariances agree. The observations here are not assertions about distribution mode counts. Independent audit and exhaustive publication priority verification have not been performed.
