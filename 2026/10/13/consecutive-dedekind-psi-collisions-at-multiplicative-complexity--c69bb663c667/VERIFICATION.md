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

The proof in `RESULT.md` is complete and unrestricted in size.

The attached checker independently evaluates
\[
\Omega(n)
\]
and
\[
\psi(n)=n\prod_{p\mid n}\left(1+\frac1p\right)
\]
using exact integer factorization for every
\[
1\le n<100000.
\]

It filters to consecutive pairs satisfying
\[
\Omega(n)\le2,\qquad\Omega(n+1)\le2
\]
and asserts that the complete observed collision list is
\[
(4,5),\qquad(14,15).
\]

It separately checks
\[
\psi(4)=\psi(5)=6
\]
and
\[
\psi(14)=\psi(15)=24.
\]

The finite replay is corroborative only. The universal exclusion of all other cases follows from the exhaustive factorization-type argument in `RESULT.md`.
