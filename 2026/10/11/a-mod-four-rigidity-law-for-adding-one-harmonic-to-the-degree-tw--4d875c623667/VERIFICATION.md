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

The universal verification is the analytic proof in `RESULT.md`.

The critical identities are:
\[
Q(\theta)=1+\sqrt2\cos\theta+\frac12\cos(2\theta)
=\left(\cos\theta+\frac1{\sqrt2}\right)^2,
\]
with zero set modulo \(2\pi\)
\[
\left\{\frac{3\pi}{4},\frac{5\pi}{4}\right\},
\]
and
\[
\cos\left(\frac{3\pi n}{4}\right)=0
\quad\Longleftrightarrow\quad
n\equiv2\pmod4.
\]

For the strict classes, the perturbation
\[
P_n(\theta)=\cos\theta+
2\operatorname{sgn}\!\left(\cos(3\pi n/4)\right)\cos(n\theta)
\]
is positive at both zeros of \(Q\). Compactness supplies the global small-\(\varepsilon\) argument.

`verify.py` checks these identities over a finite range and performs dense-grid stress tests. Its successful output in the packaging run was:

`VERIFY_OK parity_n=3..64 strict_cases=29 grid=120000 worst_sample=4.649e-08`

The numerical test is only a consistency check. It does not establish the theorem for infinitely many \(n\), and the proof does not depend on it.

The exact values and extremizers for the strict classes are not established here.
