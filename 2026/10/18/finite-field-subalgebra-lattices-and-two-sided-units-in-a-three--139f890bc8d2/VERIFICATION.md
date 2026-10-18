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

## Reproduction
Run `python verify.py` with Python 3 and no external dependencies. The program uses projective representatives for every line and covector for every plane in a three-dimensional finite-field vector space. Every plane is tested for closure by evaluating four basis products; every line is tested by squaring its representative. For two-sided inverses, it forms the six scalar linear equations expressing \(xy=yx=1\) and performs finite-field Gaussian elimination. For generated subalgebras it iteratively enlarges a vector-space basis under multiplication until stable. It also enumerates the square-zero and idempotent loci directly.

Fields checked: \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8,\mathbb F_{11},\mathbb F_{13}\); thirteen nonzero parameter pairs in total. Irreducible binary polynomials encode \(\mathbb F_4\) and \(\mathbb F_8\). The checks include both split and inert quadratic cases, the repeated-root diagonal case in characteristic seven, and characteristic-two inseparability in the axis planes. The proof, not these finite checks, covers all finite fields and nonzero deformation parameters.

## Mathematical limits
No claim is made for \(t=0\), infinite fields as a counting problem, or arbitrary three-dimensional nonassociative algebras. Finite computation does not establish the universal formulas independently of the symbolic proof. Publication priority and independent mathematical validation have not been certified.
