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

The checker uses exact rational arithmetic for the harmonious equation
\[
\frac{2^a}{\sigma(2^a)}+\frac{2^bq}{\sigma(2^bq)}=1.
\]
It verifies the first Mersenne-prime instances and exhaustively tests \(1\le a,b\le12\) with odd primes \(q<5000\), confirming that every computational solution has \(a=b\) and \(q=2^a-1\).

This finite replay is not the proof of the infinite statement. The proof is the exact divisibility argument in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
