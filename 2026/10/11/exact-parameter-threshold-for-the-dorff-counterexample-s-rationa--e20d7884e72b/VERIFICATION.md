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

The proof uses exact symbolic identities and exact rational sign certificates.

For the boundary map with \(a=-10/11\), the cleared angular-derivative numerator is
\[
N_b(x)=-440b^2x-463b^2+440bx^2+484bx-21.
\]
For \(b\ge0\) this is convex in \(x\), and
\[
N_b(-1)=-(b+1)(23b+21),
\qquad
N_b(1)=-21(b-1)(43b-1).
\]
This proves strict boundary orientation for \(0\le b<1/43\) and exact degeneration at \(b=1/43\).

The fixed-witness Jacobian was reconstructed from the variable Fourier coefficients and the source's rational summation formula. Its factorization is the one printed in RESULT.md. The included script `verify_dorff_parameter.py` uses only Python's standard library and exact `Fraction` arithmetic. It transforms the relevant polynomials to Bernstein form on \([0,1/43]\); coefficient signs certify
\[
K<0,
\qquad
H'>0,
\qquad
E_1<0<E_2
\]
on the entire interval.

The same script verifies
\[
H(0)<0<H(1/43)
\]
and exact rational signs at
\[
0.02218460173517970
\quad\text{and}\quad
0.02218460173517971,
\]
so the unique root satisfies the displayed bracket.

The checker was executed from the packaged file path after construction and returned `PASS exact rational reconstruction, factorization, and Bernstein/sign certificate`. No floating-point sample is used as proof of an interval sign or root uniqueness.
