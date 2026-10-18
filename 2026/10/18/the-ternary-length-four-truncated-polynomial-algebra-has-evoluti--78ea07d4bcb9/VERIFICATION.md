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

# Exact reproducibility

`VERIFY.py` (Python 3 standard library) is the complete certificate. Run `python3 VERIFY.py` in the extracted package directory.

The program first reconstructs the quadratic-output subspace over \(\mathbb F_3\), checks the explicit eight-square decomposition by formal coefficients and at all \(81\) field-valued inputs, and validates the eight-square rank. It lists the \(40\) projective rank-one squares, then generates every reduced row-echelon basis of every three-dimensional subspace of the six-dimensional quotient. The resulting \(33880\) cases have intersection-dimension counts \(31905,1830,145,0\) at dimensions \(1,2,3,4\) respectively. The zero count in dimension four proves no seven-square decomposition exists.

Next, it enumerates all \(11011\) two-dimensional normal spaces, representing the four-dimensional quotient support candidates. Exactly \(252\) preimages are square generated: \(243\) contain ten projective squares and nine contain sixteen. It verifies all counts using independent Gaussian-binomial formulas for the numbers of subspaces.

The certificate establishes exact finite calculations; it does not perform any bibliographic originality audit or assert that the \(252\) optimal support spaces are nonisomorphic evolution envelopes. Independent mathematical validation has not been performed.
