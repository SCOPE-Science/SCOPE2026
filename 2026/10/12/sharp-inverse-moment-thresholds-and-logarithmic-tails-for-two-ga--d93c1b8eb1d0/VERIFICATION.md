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

Run `python3 verify.py` using a standard Python 3 interpreter; the program uses only Python's standard library. It reports `VERIFY_OK checks=1513; C2=1/pi; C4=3/pi^2; finite checks do not certify tails`.

Checks cover the exact Kronecker least-squares normal-equation factorization over Gaussian draws, the independent-row tensor and dense Gaussian scalar normal equations, the gamma evaluation \(M_d(2)=1/(d-2)\) for applicable dimensions, exact product-normal polynomial moments giving \(C_2=1/\pi\) and \(C_4=3/\pi^2\), and seven finite Rademacher conditional-moment identities. The sample-based comparisons and finite arithmetic checks are diagnostics only.

The infinity/finite dichotomies for all real positive moment orders, the strict unconditional variance comparison, and the exact tail asymptotics are established by analytical distributional identities and integration in `RESULT.md`; they cannot be certified by finite numerical samples. No independent audit or external validation has been performed.
