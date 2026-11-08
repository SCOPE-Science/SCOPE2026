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

The exact Cartier calculation uses the basis \(dx,x\,dx,x^2\,dx,x^3\,dx,y\,dx,xy\,dx\) for the one-pole genus-six Artin–Schreier curve. The proof is algebraic and applies to all algebraically closed fields of characteristic \(3\).

`verify_cartier_g6.py` is a standalone standard-library Python checker. It independently expands \(y=y^3-f(x)\), applies Cartier's monomial rule, constructs matrices over \(\mathbb F_3\), and exhaustively checks all \(81\) four-coefficient tuples for the first three ranks. To replay in the same directory, run `python3 verify_cartier_g6.py`. The actual output is in `verification_output.txt` and ends with `ALL_CHECKS_PASSED`.

The enumeration is finite and does not independently verify the theorem over arbitrary fields; the displayed general calculation supplies that proof. No external or independent scientific audit has been performed.
