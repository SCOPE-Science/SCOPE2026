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

Run `python3 verify.py` with Python 3 and only its standard library. The program independently enumerates base-2 and base-4 palindrome predicates by repeated division and digit-array reversal; it does not use the proof's digit-swap recurrence to compute observed values. It checks every integer on the four complete shells from \(16^1\) through \(16^5-1\), including all four individual interval sign censuses. Observed shell count triples \((P_h,N_h,Z_h)\):

- \(h=1\): \((12,94,134)\).
- \(h=2\): \((179,1665,1996)\).
- \(h=3\): \((2853,27235,31352)\).
- \(h=4\): \((45641,438087,499312)\).

The expected terminal line is `ALL_EXACT_CHECKS_PASS`. Exhaustive tests over a finite domain support reproducibility but do not replace the proof for all \(h\ge1\). The infinite formulas are derived in `RESULT.md` using block decomposition and a signed-digit absolute-sum recurrence. Independent audit has not been performed.
