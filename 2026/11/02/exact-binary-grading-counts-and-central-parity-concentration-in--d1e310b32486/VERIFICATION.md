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

The attached `verify.py` uses only Python's standard library. Execute `python3 verify.py` from the directory containing this file and the script.

The program implements the exact symbolic formulas and separately enumerates all ordered complementary pairs of reduced-row-echelon subspaces in six finite, small cases. Each candidate is tested directly for closure of homogeneous Lie brackets, with no reliance on the symplectic normal form. It checks \((q,n,r)=(2,1,0),(2,1,1),(2,1,2),(2,2,0),(3,1,0),(3,1,1)\), with respective \((E,O)\) values \((5,12),(33,72),(385,816),(97,480),(10,36),(136,432)\). As a separate parameterization check, it exhaustively searches all \(q^9\) linear maps in the three-dimensional case for \(q=2,3\), retaining exactly those idempotent projections that satisfy the grading identities. Both searches return the same counts. Actual run result:

```
PASS q 2 n 1 r 0 even 5 odd 12
PASS q 2 n 1 r 1 even 33 odd 72
PASS q 2 n 1 r 2 even 385 odd 816
PASS q 2 n 2 r 0 even 97 odd 480
PASS q 3 n 1 r 0 even 10 odd 36
PASS q 3 n 1 r 1 even 136 odd 432
PASS_PROJECTOR 2 (5, 12)
PASS_PROJECTOR 3 (10, 36)
VERIFY_OK: six exhaustive decomposition cases, two exhaustive projector cases
```

The \(n,r,q\) theorem is not inferred from these finite checks: the symplectic and center-splitting proof establishes the unrestricted result. Extension fields and large dimensions are covered by that proof and the field-order formulas, but are not directly enumerated by the attached prime-field checker. The asymptotic follows by dominated convergence and the explicit parity-switching involution, not numerical tests. No external independent audit has been performed.
