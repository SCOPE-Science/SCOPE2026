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
The checker reconstructs the classical root systems \(A_\ell,B_\ell,C_\ell,D_\ell\) through rank \(12\), and explicit root sets for \(F_4\) and \(G_2\).

For every tested root system it:
1. verifies the long-root and short-root counts;
2. checks the resulting one-value or two-value Euler formulas;
3. finds an integral cocharacter whose pairing with every root is nonzero and pairwise distinct.

For \(E_6,E_7,E_8\), it checks the standard identity
\[
|\Phi|=\dim\mathfrak g-\operatorname{rank}\mathfrak g
\]
against the standard dimensions and ranks.

Finite checks are regression evidence only. The theorem for arbitrary rank follows from the root-space fixed-point argument and the standard minimal-orbit theorem in `RESULT.md`.
