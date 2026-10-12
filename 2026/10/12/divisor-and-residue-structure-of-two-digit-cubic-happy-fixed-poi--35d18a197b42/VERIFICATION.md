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

For a two-digit numeral
\[
N=(a,c)_b,
\]
the fixed-point equation is checked in the equivalent form
\[
a(b-a^2)=c(c-1)(c+1).
\]

The attached checker performs three independent finite stress tests.

For every base
\[
2\le b\le500,
\]
it directly enumerates all digit pairs and compares the observed fixed points with the base formula.

For every
\[
2\le c\le250,
\]
it enumerates every positive divisor of
\[
c^3-c,
\]
constructs the predicted base, checks the digit inequalities, and verifies that the number of constructions is exactly
\[
\tau(c^3-c).
\]

For every
\[
2\le a\le500,
\]
it directly counts residue classes modulo \(a\) satisfying
\[
a\mid c(c-1)(c+1)
\]
and compares the result with
\[
r(\nu_2(a))3^{\omega(a/2^{\nu_2(a)})}.
\]

The checker also verifies the two boundary rays \(c=0,1\) for a large finite range. These finite checks are corroborative. The universal theorem follows from the exact factorization and the prime-power/Chinese-remainder proof in `RESULT.md`.
