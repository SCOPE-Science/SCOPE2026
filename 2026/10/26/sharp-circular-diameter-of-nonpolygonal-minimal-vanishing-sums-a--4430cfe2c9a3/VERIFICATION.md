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

The included `verify.py` is a standalone Python 3 standard-library verifier. Run `python3 verify.py` after extracting the embedded artifact. It enumerates all nonempty proper checkerboards for four pairs of odd primes, checks exact rational tensor-kernel vanishing identities and absence of antipodal pairs, and confirms the predicted maximal gap; selected small extremizers are also checked against all proper subsums. Expected terminal line: `CERTIFICATE_OK configurations= 16992`. This is a finite cross-check, not a proof of the uniform theorem; the mathematical proof is in RESULT.md. No independent audit has been performed.
