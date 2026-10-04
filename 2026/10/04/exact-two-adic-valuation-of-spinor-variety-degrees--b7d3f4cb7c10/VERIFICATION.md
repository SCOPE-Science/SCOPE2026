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
The geometric coefficient is checked in two independent finite ways. The factorial product
\[
\deg S_n=\frac{M!\prod_{a=2}^{n-1}a!}{\prod_{a=2}^{n}(2a-1)!}
\]
is evaluated exactly with arbitrary-precision integers. Separately, for small \(n\), the checker recursively removes admissible corners from strict partitions and counts every saturated chain from the staircase to the empty partition. The two values agree.

For the arithmetic theorem, the checker computes the exact two-adic valuation of the integer degree and compares it with
\[
n-s_2(n(n+1)/2)
\]
through \(n=200\). It also verifies the claimed odd and modulo-four exceptional sets.

The infinite proof does not rely on these finite ranges. It follows from the one-box Pieri rule, the shifted hook-length product, Legendre's identity \(\nu_2(m!)=m-s_2(m)\), and the elementary digit-sum relation \(s_2(2a-1)=s_2(a-1)+1\).

Limits: the polarization is the minimal half-spin embedding, the ground field is \(\mathbb C\), and only the two-adic valuation is classified.
