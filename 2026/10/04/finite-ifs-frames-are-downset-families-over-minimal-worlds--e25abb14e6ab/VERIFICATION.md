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

The structural proof has two exact implications.

If \(xRm\), IFC forces \(m\) to be minimal. Then FC2 says that whenever \(z\leq x\in D_m\), some \(m'\leq m\) satisfies \(zRm'\). Minimality gives \(m'=m\), so \(z\in D_m\).

Conversely, if all targets are minimal and every predecessor fiber \(D_m\) is a downset, IFC is immediate and FC2 is witnessed by taking \(m'=m\).

The modal formulas follow by substituting this normal form into the source definitions:
\[
\Diamond_R U
=
\bigcup_{m\in U\cap M}D_m,
\]
and
\[
\Box_R U
=
X\setminus
\bigcup_{m\in M\setminus U}\uparrow D_m.
\]

The bundled `verify.py` exhaustively enumerates every labelled poset through four points. Through three points it also enumerates every binary relation, checks the iff classification and exact census, and verifies the two modal formulas on every downset. It prints `VERIFY_OK`.

## Limits

The computation is corroborative. The proof applies to arbitrary posets; only the exact finite census uses finiteness. Isomorphism classes are not counted.
