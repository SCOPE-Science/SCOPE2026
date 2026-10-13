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
The geometric input is
\[
\sigma_k(C_d)^\vee
=
\Delta_{\{1^{d-2k},2^k\}},
\]
obtained from the published duality statement and biduality.

Hilbert's formula then gives
\[
A_{d,k}
=
2^k\binom{d-k}{k}.
\]

For adjacent terms,
\[
\frac{A_{d,k+1}}{A_{d,k}}
=
\frac{2(d-2k)(d-2k-1)}
{(k+1)(d-k)}.
\]
The numerator-minus-denominator polynomial is
\[
F_d(k)=2d^2-9dk-3d+9k^2+5k,
\]
with
\[
F_d(k+1)-F_d(k)=18k+14-9d<0
\]
on the comparison range.

Writing
\[
m=\left\lfloor\frac{d+1}{3}\right\rfloor,
\]
the three residue classes modulo three give strict positive values at \(m-1\) and strict negative values at \(m\). This is a complete symbolic certificate of strict unimodality.

The bundled checker reconstructs the degrees independently from the partition multiplicities for every
\[
2\le d\le1000.
\]
No finite enumeration is used as proof of the infinite theorem.
