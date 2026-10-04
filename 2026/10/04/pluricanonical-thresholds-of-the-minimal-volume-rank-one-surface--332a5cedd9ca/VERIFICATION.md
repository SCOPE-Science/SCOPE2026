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

The verifier reconstructs the two Hirzebruch--Jung chains
\[
[2^9,4,2,2],\qquad [2^4,10,2]
\]
from their self-intersection data. It checks determinant and tail-determinant pairs
\[
(73,66),\qquad (87,70),
\]
and therefore local canonical indices \(73\) and \(87\), global index \(6351\), and
\[
6351\cdot\frac1{6351}=1.
\]

For each chain, the script forms the exact intersection matrix \(M\) and solves
\[
M b=(2-e)
\]
over the rational numbers. It checks the discrepancy-coefficient vectors
\[
\frac1{73}(6,12,18,24,30,36,42,48,54,60,40,20)
\]
and
\[
\frac1{87}(16,32,48,64,80,40).
\]

For every \(2\le n\le98\), it computes the fractional part vector \(\{nb\}\), evaluates
\[
\delta_n=\frac12\left(K_Y+\{nB_Y\}\right)\cdot\{nB_Y\},
\]
and then evaluates
\[
P_n=1+\frac{n(n-1)}{2\cdot6351}+\delta_n.
\]
Every result is checked to be a nonnegative integer. The exact set with \(P_n=1\) for \(2\le n\le97\) is checked against the list in `RESULT.md`; all other values in that interval are \(0\), and \(P_{98}=2\).

This proves only the finite threshold claims stated in the result. It does not infer the behavior of the full canonical ring beyond degree \(98\).

The stored output must end in `VERIFY_OK`.
