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

The source tableau was independently transcribed and eliminated analytically, producing the exact rational–cubic factorization. The standalone `checker.py` directly executes the stages and factorization over 1,000 exact rational inputs; an additional ten parameter probes verify strict negative values between the two distinct positive zeros. Arbitrary precision root brackets give the reported constants. The proof uses sign and monotonicity arguments for all real parameters and step sizes, not finite sampling. The checker is not an external or independent mathematical audit. The statement applies only to scalar decay with a constant implicitness fraction; spatial positivity, multi-mode stability, numerical rounding robustness, and adaptive parameter fields are outside its scope.
