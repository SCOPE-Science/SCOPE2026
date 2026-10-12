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
For corank
\[
c=n-r,
\]
the projective degree is checked in two exact forms:
\[
D_{n,n-c}
=
\prod_{j=0}^{c-1}
\frac{(n+j)!\,j!}{(n-c+j)!\,(c+j)!}
\]
and
\[
D_{n,n-c}
=
\det\!\left[\binom{n}{c-i+j}\right]_{1\le i,j\le c}.
\]

The proof of the prime-power branch reduces the determinant modulo \(p\) and applies Lucas's theorem. The proof of the converse chooses
\[
c=p^{\nu_p(n)}
\]
and applies Lucas's theorem to each binomial ratio in the product inside the localization at \(p\).

The bundled checker compares the two exact degree formulas for every proper rank with
\[
2\le n\le32,
\]
then verifies the common-prime classification through
\[
n=120.
\]
It also verifies every explicit prime-avoiding witness in that range.

Finite computation is not used as an infinite proof. The exact exponent of the common prime when \(n\) is a nontrivial prime power is not asserted.
