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
For a smooth degree-\(d\) hypersurface of dimension \(n\), the checker evaluates
\[
D=d(d-1)^n.
\]

It computes Euler characteristic in two exact ways:
\[
\chi_1
=
\frac{(1-d)^{n+2}-1}{d}+n+2,
\]
and
\[
\chi_2
=
d\sum_{j=0}^{n}\binom{n+2}{j}(-d)^{n-j}.
\]
The identity
\[
\chi_1=\chi_2
\]
is verified throughout the finite test grid.

It then checks the complete comparison:
\[
D=|\chi|
\]
only at \((n,d)=(1,2)\),
\[
D<|\chi|
\]
for \(d=2,n\ge2\), and
\[
D>|\chi|
\]
for every \(d\ge3\).

Finite checks are regression evidence only. The all-parameter proof is the symbolic parity split in the accompanying result.
