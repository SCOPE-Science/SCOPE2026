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
Run `python3 verify.py`.

For each \(1\le n\le44\), the program generates the required primes by a deterministic sieve and forms
\[
R_n(b)=\prod_{r=0}^{b-1}\frac{P_{n+r}}{P_{n+r}-1}
\]
using exact integer numerators and denominators. It stops at the first \(b\) satisfying
\[
R_n(b)>2.
\]
Because every factor exceeds \(1\), this first crossing is exactly \(a(n)\); the checker also verifies the preceding product is at most \(2\).

Acceptance requires
\[
a(42)=3900,\qquad a(43)=4112,\qquad a(44)=4324,
\]
the terminal primes \(37199,39461,41761\), the published normalization \(f(31)=-5\), the equality \(f(43)=0\), and nonvanishing of every \(f(n)\) for \(2\le n\le42\).

A successful replay prints `VERIFY_OK`. No floating-point arithmetic is used in the threshold comparisons.
