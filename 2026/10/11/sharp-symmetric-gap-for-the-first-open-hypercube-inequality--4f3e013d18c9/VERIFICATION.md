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

The checker uses only exact integer arithmetic.

It enumerates every one of the
\[
\binom{16}{5}=4368
\]
five-vertex subsets of \(\{0,1\}^4\), computes the normalized simplex volume as the absolute determinant of the augmented \(5\times5\) vertex matrix, and groups each contribution by the multiplicities of the three symmetry classes
\[
|v|\in\{0,4\},\qquad |v|\in\{1,3\},\qquad |v|=2.
\]
The resulting polynomial is exactly
\[
\begin{aligned}
P={}&32a^2b^3+96a^2b^2c+96a^2bc^2+16a^2c^3\\
&+132ab^4+480ab^3c+624ab^2c^2+336abc^3+48ac^4\\
&+64b^5+396b^4c+576b^3c^2+368b^2c^3+96bc^4.
\end{aligned}
\]

The same checker represents multivariate polynomials as exact coefficient dictionaries and verifies
\[
6\left(105(a+4b+3c)^5-1024P\right)
=
(a-b)^2A+(b-c)^2B+(a-c)^2C
\]
with the cubics \(A,B,C\) displayed in the proof.

Every coefficient in those cubics is a positive integer. Hence the certificate proves the inequality for all real \(a,b,c\ge0\), rather than only for enumerated or sampled parameter values.

The checker also verifies directly from the \(4\)-cube incidence structure that every facet sum is \(a+4b+3c\), that the total weight is twice this quantity, and that the uniform weighting \(a=b=c=1\) gives the exact ratio
\[
\frac{105}{128}.
\]

The finite determinant census computes only the finite coefficient polynomial. The infinite parameter statement follows analytically from the exact nonnegative certificate.
