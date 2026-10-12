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

The proof is analytic. Two identities were checked independently in the attached standard-library script.

First, for several heterogeneous tuples satisfying \(\sum_i\theta_i=\pi/2\), the script constructs the parity probe coefficient-by-coefficient and evaluates every rotated-basis outcome amplitude directly. It compares the result with
\[
2^{-(w-1)/2}\cos\!\left(\sum_i\theta_i-\frac{|y|\pi}{2}\right),
\]
and verifies that all even-parity rotated outcomes vanish while all odd-parity rotated outcomes have the predicted magnitude.

Second, for every proper nonempty subset in those examples, the script enumerates all eigenphases \(\sum_{i\in S}\varepsilon_i\theta_i\) with \(\varepsilon_i\in\{-1,1\}\) and verifies that every cosine is strictly positive. This checks the positive-definite Hermitian-part obstruction used in the proof.

The finite replay is corroborative only. The infinite statement follows from the displayed generating-function identity and the strict subset-sum bound \(0<\sum_{i\in S}\theta_i<\pi/2\), not from enumeration.
