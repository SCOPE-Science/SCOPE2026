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

# Exact checks and limitations

Run `python3 check.py` with Python 3.10 or later. The script uses only the Python standard library. It reconstructs \(D(n)\) and \(\varphi(n)\) by trial-factorization identities independently of the algebraic classification formula and tests all \(2\le a,b\le55\). It checks the positive-index initial terms of OEIS A260961 through 2048, excluding its conventional value \(n=1\), where ordinary \(\varphi(0)\) is undefined. It compares the two integer compositions exactly (never as floating-point approximations). A successful run prints two PASS messages and several witness lines.

The script is finite, so its checks do not prove the all-index theorem or its asymptotic. The former is established by the Euler-product deficit and prime-factor argument in RESULT.md; the latter follows from the prime number theorem after the exact prime-counting identity. No independent audit has been performed.
