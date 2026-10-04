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
The proof begins with the published exponential generating function
\[
\sum_{d\ge0}H_d\frac{x^d}{d!}
=
e^{-2x}(1-x)^{-2},
\]
which yields
\[
H_d
=
d!\sum_{j=0}^{d}(d-j+1)\frac{(-2)^j}{j!}.
\]

Legendre's identity gives
\[
\nu_2(j!)=j-s_2(j).
\]
Thus the normalized summand has the exact dyadic contribution
\[
\nu_2\!\left(\frac{2^j}{j!}\right)=s_2(j).
\]

For even \(d\), the normalized degree is odd. For odd \(d\), every term with \(j\ge2\) is divisible by \(4\) in the \(2\)-adic integers, so the normalized degree is congruent to
\[
1-d
\pmod4.
\]
This establishes the three cases.

The bundled checker derives the integer sequence from the equivalent recurrence, checks the exact coefficient formula with rational arithmetic on an initial range, and verifies the valuation statements on a larger range. These finite tests are regression evidence only.

Limits: the theorem does not determine the full excess valuation when \(d\equiv1\pmod4\).
