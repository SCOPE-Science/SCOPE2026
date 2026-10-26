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

Run `python3 verify.py` in a directory containing `verify.py` and `checks.txt`. The program uses only the Python standard library. Exhaustive enumeration directly constructs all labeled uniform recursive trees for \(2\le n\le10\), and independently compares the two joint count tables. A separate integer-coefficient recursion derived from root forests and the maximum-label branch checks \(2\le n\le22\). Exact fractional moments check both covariance identities. The provided `checks.txt` is the actual output of `verify.py`.

These are finite diagnostics and are not offered as a proof for all sizes. The analytic proof follows the formal-series recurrences in `RESULT.md` and includes the \(n=1\) exception and the weighted-root \(n=3\) boundary. Independent validation is not claimed.
