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

# Finite exact checks and mathematical proof boundary

Run `python3 artifacts/verify.py` with Python 3 and its standard library. The verifier recomputes gcds of all minors of each size for four explicit integer 5-by-5 matrices and checks their \(2\)-adic Smith valuation lists:

- \(M-I:(0,0,0,0,2)\).
- \(M^3-I:(0,0,1,1,2)\).
- \((M^6-I)/2:(0,0,0,0,2)\).
- \((M^{12}-I)/4:(0,0,0,0,2)\).

It independently enumerates and partitions every state for \(k=1,2,3\), recomputes cycle multiplicities and total state mass for several levels, checks the five OEIS totals, and checks the closed formula for \(2\le k\le11\). Expected output begins `VERIFY_OK:` and the script raises an exception on failure.

The enumerations do not prove infinite claims. The argument for every \(j\ge0\) depends on a Hensel decomposition of the degree-five polynomial, the elementary \(2\)-adic lifting valuation and an exact integer-matrix recurrence with invertible correction factors. This deductively propagates the finite Smith bases to arbitrary powers of two. An independent audit has not been conducted.
