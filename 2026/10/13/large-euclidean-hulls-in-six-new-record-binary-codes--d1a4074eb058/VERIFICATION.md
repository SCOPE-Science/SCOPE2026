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
`artifacts/verify.py` uses only the Python standard library.

The verifier reconstructs the six printed quasi-cyclic codes over \(\mathbb F_2\) from their appendix polynomial factors, multiplier polynomials, block lengths, and tail patterns. It checks that the resulting dimensions are correct and then exhaustively enumerates all parent words.

The published parent minimum-distance and shell pairs are reproduced exactly:
\[
(66,2720),\ (68,1156),\ (68,2992),\ (70,3502),\ (72,9826),\ (72,2394).
\]

For every parent generator \(G\), the verifier forms
\[
GG^{\mathsf T}
\]
over \(\mathbb F_2\), computes its exact rank and nullspace, and maps the nullspace back through \(G\) to obtain a hull basis. The exact Gram ranks are
\[
4,18,1,2,0,1,
\]
and exhaustive hull enumeration gives dimensions and minimum distances
\[
(17,68),\ (2,104),\ (20,68),\ (19,72),\ (21,72),\ (21,72).
\]

Successful replay prints `VERIFY_OK`.
