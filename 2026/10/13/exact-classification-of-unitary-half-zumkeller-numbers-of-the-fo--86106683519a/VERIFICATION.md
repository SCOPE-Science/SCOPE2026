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

`verify.py` performs the exact finite proof-stage enumeration after the symbolic reduction. For each \(p\in\{3,5,7\}\), it evaluates all \(64\) triples \((u,v,w)\in\{-5,-3,3,5\}^3\), rejects zero-denominator identities, and checks the resulting candidate table. It separately verifies the five explicit equal-sum partitions.

The script also scans all distinct odd-prime pairs with \(q\le1000\) as regression evidence. That scan is not used to infer the unbounded theorem. The infinite range \(p\ge11\) is excluded algebraically by
\[
q\le\frac{5(p+1)}{p-5}<p,
\]
where the strict inequality follows from \(p^2-10p-5>0\) for \(p\ge11\).

Expected replay output is supplied in `VERIFY_OUTPUT.txt` and starts with `VERIFY_OK`.

Scientific limits: the result addresses only \(4pq\) with distinct odd primes \(p<q\). Independent audit has not been performed.
