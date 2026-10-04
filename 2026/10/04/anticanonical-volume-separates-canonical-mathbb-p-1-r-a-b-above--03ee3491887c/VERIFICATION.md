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
The proof has two logically distinct parts. First, cyclic quotient ages give the exact canonical domain \(0\le b-a\le r\) and \(a\le r+b-a\). Second, equality of
\[
\frac{(r+a+b)^{r+1}}{ab}
\]
for two canonical pairs forces a high power of the reduced ratio of their weight sums to divide a product bounded by \(6r^2\). For \(r\ge8\), the inequality \(2^{r+1}>6r^2\) excludes unequal sums, after which equal sum and product determine the pair.

`verify_volume_collisions.py` performs exact rational checks. It verifies the age-based canonical parametrization for \(2\le r\le40\), confirms exactly the two collisions at \(r=2\), confirms no collisions for \(3\le r\le200\), and checks the numerical cutoff used by the infinite argument. Its successful output is `VERIFY_OK`.

The finite computation is not used as evidence for the infinite range \(r\ge8\); that range is covered by the divisibility proof. Independent audit has not been performed.
