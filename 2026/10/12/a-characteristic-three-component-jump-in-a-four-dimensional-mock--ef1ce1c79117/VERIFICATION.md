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
The standalone program `artifacts/verify.py` uses SymPy to reconstruct the complete multiplication and the tensor polynomial
\[
[[r,r]]=r_{12}\bullet r_{13}+r_{13}\bullet r_{23}-r_{12}\bullet r_{23}.
\]
It derives all \(64\) tensor-coordinate polynomials and compares them to the independently reconstructed coadjoint \(\mathcal O\)-operator criterion. It then checks the symbolic component equations, rank-four Pfaffian, and coboundary matrix formulas.

It exhaustively enumerates **every skew tensor** over \(\mathbf F_3\), \(\mathbf F_5\), and \(\mathbf F_7\) and compares the original tensor identities to the closed equations. The respectively observed tuples (total solutions, rank-four solutions, distinct coboundary maps) are
\[
(63,18,21),\quad(145,20,29),\quad(385,42,55).
\]
A further finite-extension check uses an explicit model of \(\mathbf F_9\) and obtains exactly \(2025\) solutions, of which \(648\) are nondegenerate, after eliminating the provably zero coefficient \(b\).

Run `python3 artifacts/verify.py` after installing the dependency specified in `artifacts/requirements.txt`. The output saved in `artifacts/verify_output.txt` ends with `VERIFY_OK`.

These finite checks do not establish the field-uniform result: the exact coefficient calculation, field-by-field algebraic case division, and stated counting arguments supply the proof. No independent external validation has been performed.
