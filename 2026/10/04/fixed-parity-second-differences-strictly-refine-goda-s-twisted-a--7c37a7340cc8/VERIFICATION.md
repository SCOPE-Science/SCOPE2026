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

The current preprint declares primary MSC \(57K14\), dates version 1 to 2026-09-24, recalls Goda's parity-separated quadratic limit, and states Conjecture 1 as a parity-separated second-difference limit.

For \(b_k=a_{arepsilon+2k}\),
\[
b_{k+1}-2b_k+b_{k-1}
=
rac{2}{\pi}q_{arepsilon+2k}.
\]
Twice summing gives
\[
b_k=b_0+k(b_1-b_0)+rac{2}{\pi}\sum_{j=1}^{k-1}(k-j)q_{arepsilon+2j}.
\]
If \(q_{arepsilon+2j}	o L\), the constant part is \((L/\pi)k(k-1)\) and the weighted error is \(o(k^2)\), hence \(a_n/n^2	o L/(4\pi)\).

For the non-converse, \(b_k=(L/\pi)k^2+(-1)^k k^{3/2}\) has the required quadratic normalized limit while its second differences are unbounded.

The bundled regression script prints:

`VERIFY_OK green_identity_N=160 constant_second_difference=7.25 converse_tail_max=12471.433240`

The finite regression is not used as an infinite proof.

The independent-audit channel has not been performed.
