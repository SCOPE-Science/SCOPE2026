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

The checker verifies all eight rational inequalities used to eliminate impossible prime and exponent patterns. It then verifies the explicit unitary Zumkeller and unitary half-Zumkeller partitions for the infinite family and the three exceptional numbers.

As a separate regression check, it constructs all eight unitary divisors of
\[
2^\alpha p^\beta q^\gamma
\]
for
\[
1\le\alpha,\beta,\gamma\le4
\]
and all prime pairs
\[
3\le p<q\le19.
\]
It directly enumerates every subset, compares unitary Zumkeller membership with the theorem's classification, and checks the proper-unitary half-Zumkeller property for every classified case.

A successful replay prints `VERIFY_OK`.

The finite grid is not evidence for the infinite quantifier. The all-prime, all-exponent classification is established by the symbolic monotone inequalities and explicit partitions in `RESULT.md`.
