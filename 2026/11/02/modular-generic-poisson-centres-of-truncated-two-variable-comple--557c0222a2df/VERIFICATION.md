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

# Reproducibility

Run `python3 verify.py` with Python 3, using only the standard library.

The program directly multiplies basis polynomials in \(k[x,y]/(x^m,y^n)\), implements the bracket from \(\{x,y\}=f\), checks Jacobi on all basis triples for selected parameters, and computes Poisson centres as nullspaces of the two Hamiltonian-coordinate maps by finite-field Gaussian elimination. It performs seven complete small finite-field bracket enumerations and three reproducible larger samples. For \(\mathbb F_4\) it uses the polynomial \(t^2+t+1\) in a binary representation; the other fields are prime fields.

Observed marker: `TRUNCATED_POISSON_CENTRE_OK`.

The finite computations do not prove arbitrary-field claims, completeness of literature searches, or independent validation. The general proof is in RESULT.md.
