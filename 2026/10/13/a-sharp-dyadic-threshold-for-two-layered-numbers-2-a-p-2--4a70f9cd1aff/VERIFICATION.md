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

The checker directly applies the subset-sum criterion to every pair consisting of an odd prime \(p\le300\) and an integer \(1\le a\le9\). For each pair it constructs every proper divisor of \(2^a p^2\) relevant to the target
\[
\frac{\sigma(2^a p^2)-1}{2}-2^a p^2,
\]
then performs an exact bitset subset-sum decision and compares it with the claimed condition
\[
p<2^a.
\]

The replay checks \(549\) parameter pairs. It is finite regression evidence only; it is not used to justify the unbounded theorem. The proof for all \(a\) and \(p\) is in `RESULT.md`.

A successful replay starts with `VERIFY_OK` and reports `violations=0`.
