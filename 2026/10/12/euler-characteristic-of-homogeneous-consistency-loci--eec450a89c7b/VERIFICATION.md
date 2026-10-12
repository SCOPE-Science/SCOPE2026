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
The checker generates actual exponent vectors of homogeneous monomials and exhaustively enumerates selected small systems.

For each tuple it records which selected monomials are pure powers. The tuple is counted as having no common projective zero exactly when these pure-power labels cover every coordinate variable. This criterion is also tested against every nonempty coordinate support.

The brute-force total is compared with
\[
\sum_{t=0}^{n}(-1)^t\binom nt\prod_i(N_i-t).
\]

Separate symbolic checks verify:
\[
m<n\Longrightarrow \chi_c(U)=0,
\]
\[
m=n\Longrightarrow \chi_c(U)=n!,
\]
and, for linear forms,
\[
\chi_c(U)=n!\,{m\brace n}.
\]

These finite checks are regression evidence only. The all-parameter theorem follows from the fixed-point covering argument and inclusion--exclusion in `RESULT.md`.
