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

# Reproducibility record

The standalone source `check_square_zero_derivations.py` constructs the exterior-square derivation matrix over three fields using exact finite-field arithmetic, including a polynomial-basis realization of \(\mathbb F_4\). It tests \(A^2=0\), computes \(\rho(A)\) and \(\rho(A)^2\), calculates the rank of \(\rho(A)\), row-reduces the full system \(BA+\rho(A)B=0\), and compares its nullity with the theoretical exponent.

All square-zero quotient matrices \(A\) were enumerated for \((n,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)\). Of these, the control cases \(n=2\) are not part of the novelty assertion. Every possible \(B\) was also directly enumerated for \((n,q)=(2,2),(2,3),(3,2)\), yielding respectively \(10\), \(33\), and \(1184\) square-zero derivations. The complete quotient-matrix enumeration for \((n,q)=(3,3),(3,4),(4,2)\) gives respectively \(44955\), \(584704\), and \(19357696\) after exact fiber counts. The rank-two branch in dimension four contributes \(210\cdot 2^{12}=860160\) over \(\mathbb F_2\), whereas the same rank-two quotient matrix makes the induced central square nonzero over \(\mathbb F_3\).

Execute `python3 check_square_zero_derivations.py` from the directory containing the embedded script; the last line should be `SQUARE_ZERO_FREE_TWO_STEP_DERIVATIONS_OK`. The exact output of the executed script is provided as `checker_output.txt`. No external package is required.

The mathematical theorem is proved by the normal-form, exterior-square rank, fiber and flag arguments in `RESULT.md`; the finite checks alone do not verify arbitrary rank, field or dimension. No statement is made concerning reducedness of the full equation scheme, component intersections, restricted derivations, or a review by a different mathematical reviewer.
