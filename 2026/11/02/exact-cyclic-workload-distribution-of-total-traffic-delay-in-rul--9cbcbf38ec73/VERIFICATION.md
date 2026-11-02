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

# Reproduction and verification

The exact domain is all integers \(k\ge1\), \(h\ge0\), with \(n=2k+h\); indexed circular initial configurations have \(k\) occupied sites. The statistic is the sum, over all time steps, of blocked cars (adjacent clockwise `11` pairs before each update). The all-parameter proof is in `RESULT.md`.

Execute `python3 verify.py` using only Python's standard library. The checker independently implements the parallel site update, enumerates all initial indexed configurations at 32 distinct parameter pairs, computes total stopped updates directly, independently computes prefix-gap delays, and compares both to the workload-vector formula. It checks all histogram marginals and endpoint counts. Expected final line begins `VERIFY_OK: 32 exact (k,h) cases`.

The finite verification reaches \(1\le k\le6\), \(0\le h\le4\), plus \(k=7\), \(h=0,1\). The program is an exhaustive check only within those parameters and is not an infinite proof. The proof's critical steps are the min-plus identity, a nonpositive full-tour increment, uniqueness of a zero-containing cyclic workload, the explicit surplus-gap reconstruction, and rooted-car double counting. No external computation service, independent review or formal proof certification is asserted.
