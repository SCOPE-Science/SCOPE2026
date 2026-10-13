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

The universal proof is split into an analytic tail and an exact finite prefix.

For
\[
n\ge1000,
\]
the argument in `RESULT.md` uses the published inequalities
\[
\pi(x+y)-\pi(x)\le\frac{2y}{\log y}
\]
and
\[
\pi(x)>\frac{x}{\log x}\qquad(x\ge17)
\]
to derive
\[
n\log\!\left(1+\frac dA\right)<9<\log A.
\]
This establishes the infinite tail symbolically.

The attached `verify.py` closes the remaining finite interval. It sieves all primes through
\[
10^6
\]
and, for each
\[
3\le n\le999,
\]
forms the exact integers
\[
A=\pi(n^2),
\qquad
B=\pi((n+1)^2)
\]
and verifies
\[
B^n<A^{n+1}.
\]
The comparison uses arbitrary-precision integers and therefore has no rounding ambiguity.

The script also checks the elementary numerical anchors used at the start of the analytic tail. Finite enumeration is not used as evidence for any unbounded range.
