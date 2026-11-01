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

The proof uses the published prime-order Fourier full-minor theorem and an exhaustive integer rank certificate for the additional three-basis obstruction. Running `python3 CHECK.py` from the package directory confirms all 149793 admissible matrices have full column rank after specializing the seventh root of unity to 105 in the prime field with 1009 elements. The program checks exact rank, not a floating-point determinant tolerance. Its seven census totals and explicit equality example are checked by assertions.

An independent implementation in compiled integer arithmetic reproduced the same counts. That cross-check addresses implementation errors but is not an independent mathematical audit. The reduction from nonzero modular minors to nonzero characteristic-zero cyclotomic minors is proved in RESULT.md. No assertion is made for other bases or higher dimensions.
