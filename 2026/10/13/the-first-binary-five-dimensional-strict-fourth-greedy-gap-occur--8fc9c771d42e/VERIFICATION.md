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

The witness generator has the eleven columns
\[
3e_1,\quad2e_2,\quad2e_3,\quad2(e_2+e_3),\quad e_4,\quad e_5.
\]
The script checks binary rank \(5\).

It enumerates all \(155\) projective lines of \(\operatorname{PG}(4,2)\) and verifies
\[
M=3,\qquad L=6,\qquad B=2,
\]
with the unique mass-six line
\[
\{e_2,e_3,e_2+e_3\}.
\]
Therefore the projective formulas give
\[
d_4=8,\qquad g_4=9.
\]

Independently, the verifier enumerates every subspace of the five-dimensional message space and computes support unions. It checks the generalized Hamming hierarchy
\[
(1,2,5,8,11).
\]
It identifies the unique three-dimensional subcode attaining \(d_3=5\), enumerates all four-dimensional supercodes containing it, and verifies directly from the CEZ definition that their minimum support is
\[
9.
\]

The universal lower bound
\[
n\ge11
\]
is proved symbolically in `RESULT.md`; the finite verifier certifies the sharp witness and all numerical premises used for equality.

Successful replay prints `VERIFY_OK`.
