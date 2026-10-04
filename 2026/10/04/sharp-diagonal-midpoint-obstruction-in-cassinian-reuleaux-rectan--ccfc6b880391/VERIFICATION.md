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

The proof is analytic. The bundled `verify.py` checks only exact algebraic identities and an exact rational witness; it is not a numerical certification of an infinite statement.

For \(r=a/\sqrt{1+a^2}\), the squared ratio between the diagonal-midpoint triple product and the three-corner product is
\[
R(r)^2=\frac{1+r-\sqrt{r^2+4r-1}}{1-r^2}.
\]
On the admissible range \(r\ge1/4\), \(R(r)>1\) is equivalent to
\[
(r+r^2)^2>r^2+4r-1.
\]
The checker expands and factors the exact polynomial difference as
\[
(r-1)\bigl((r+1)^3-2\bigr).
\]
Since \(r<1\), this is positive exactly for \(r<2^{1/3}-1\).

The lower endpoint is checked from
\[
\frac{1/\sqrt{15}}{\sqrt{1+1/15}}=\frac14.
\]
The upper endpoint is obtained by solving \(a/\sqrt{1+a^2}=2^{1/3}-1\).

For the exact example \(a=69/260\), the checker verifies \(s=269/260\), hence \(r=69/269\), together with
\[
276>269
\]
and
\[
338^3=38614472<38930218=2\cdot269^3.
\]
Thus \(1/4<69/269<2^{1/3}-1\), so the strict obstruction follows without floating-point arithmetic.

Limit: the checker does not search for the global maximizing triple and therefore does not establish the exact value of \(d_3(E_a)\) or constant \(3\)-diameter.
