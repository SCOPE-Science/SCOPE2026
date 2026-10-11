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

Using Python 3, run `python3 verify.py` from the extracted package folder. The file has no dependencies beyond the standard library and builds the graph independently from its four explicit edge families, then computes integer determinants using fraction-free Bareiss elimination.

The exact grounded-Laplacian determinants equal \(1445\), \(60742656\), \(689041148403125\), and \(3381513651486720000000000\) for \(m=3,4,5,6\), respectively. Each agrees with the claimed product. The complete characteristic-polynomial identities were verified at eleven distinct integers for \(m=3\) and eighteen for \(m=4\), and every constructed vertex has degree \(m\).

For \(m=3,4\), equality of the two degree-\(m^2+1\) characteristic polynomials at \(m^2+2\) distinct integer values is a complete polynomial identity for those respective finite dimensions, not for all dimensions. For \(m=3,4,5,6\), an exact Laplacian cofactor gives the stated tree count. The universal result is independently proved by invariant-subspace decomposition and the matrix-tree theorem in RESULT.md. This package does not represent external, independent, or machine-formal certification.
