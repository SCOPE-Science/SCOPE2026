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

# Verification details

Execute `python verify.py` with Python 3, NumPy, and SciPy. The script constructs the finite reversible walk directly from its microscopic transition rule, checks transition probabilities as rational numbers, forms the symmetrized full-chain and odd-sector tridiagonal matrices, and compares their first positive eigenvalues. It computes the Airy boundary root, the weighted Rayleigh integral, the virial endpoint identity, and the first finite-size coefficient by direct numerical quadrature. The stored run produced 2,953 passing assertions; a reproduction should report the same count and approximately \(\mu=3.47661900799224\), \(c=14.91835623997505\).

Numerical diagonalization at a finite list of lengths is not a proof that the asymptotic statement holds for every large length. The proof is the reversible Rayleigh reduction plus the uniform quadrature/FEM perturbation argument in RESULT.md. No formal proof assistant, independent audit, or exhaustive priority certification was performed.
