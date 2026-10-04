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

The checker verifies the formula
\[
\sigma(2pq)-4pq=-pq+3p+3q+3,
\]
the two surviving omitted-divisor pairs
\[
30:\{2,10\},
\qquad
66:\{1,11\},
\]
and the failed small cases.

It also directly enumerates divisors for every pair of odd primes below \(1000\) and confirms that only \(30\) and \(66\) occur in that regression range.

The bounded regression is not an exhaustive proof. The infinite exclusion is symbolic: positivity forces \(p\in\{3,5\}\); the \(p=3\) branch is uniform for every \(q\ge13\), and the \(p=5\) branch leaves only \(q=7\).

A successful replay prints `VERIFY_OK`.
