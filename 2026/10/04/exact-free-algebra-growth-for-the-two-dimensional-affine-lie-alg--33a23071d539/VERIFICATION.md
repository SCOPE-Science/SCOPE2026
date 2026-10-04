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
The proof was reconstructed directly from the term-function realization. The critical checks are:

1. For \(x_i=a_i e+b_i f\), every bracket is \(f\)-valued and linear in \(b\).
2. The basic coefficient vectors are \(a_i\mathbf e_j-a_j\mathbf e_i\), and further adjoints multiply them by coordinate functions.
3. Polynomial functions exhaust all scalar functions on \(\mathbb F_q^n\), so coefficients can be chosen independently at each point.
4. At each nonzero \(a\), the basic coefficient vectors span \(a^\perp\), of dimension \(n-1\); at zero they all vanish.
5. The generator span has dimension \(n\) and intersects the derived ideal trivially.

The supplied `verify.py` separately closes the coordinate term functions under pointwise brackets for \((q,n)=(2,1),(2,2),(2,3),(3,1),(3,2)\). Its output is stored in `verify_output.txt` and ends with `CHECK_OK`.

The computation does not certify arbitrary prime powers or arbitrary rank. Those cases are covered by the algebraic proof, whose only finite-field-specific step is the standard representation of every function \(\mathbb F_q^n\to\mathbb F_q\) by a polynomial modulo \(a_i^q-a_i\).
