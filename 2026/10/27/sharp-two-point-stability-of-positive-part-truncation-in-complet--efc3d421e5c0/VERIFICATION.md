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
Reproduce the analytical quotient for a mask \(S\) of size \(k\) using the positive-definite Gram matrix \(A=(1+n\gamma)I-\gamma\mathbf1\mathbf1^\top\). Minimization over inactive coordinates gives \(b=\gamma\sum_{i\in S}z_i/(1+\gamma k)\), and the active constant/zero-sum decomposition yields the two mask quotient eigenvalues \(1\) and \(1+\gamma^2k(n-k)/(1+n\gamma)\). A same-orthant finite perturbation realizes the larger quotient, proving sharpness. No approximation or numerical computation enters the quantified proof.

Run `python CHECK.py` with Python 3 and NumPy. The checker compares complete masks against direct symmetric generalized eigenvalues for dimensions 2 through 8 and several couplings, checks explicit norming directions, and verifies rational identities through dimension 17. The observed output was `PASS 2552 mask eigenvalue, witness, and exact rational identities`. This is only finite computational corroboration.

No general-graph extension, independent proof review, external certification, or machine formalization is claimed. The graph norm includes a strictly positive vertex mass, making the finite-dimensional quadratic form positive definite.
