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

Run `python verify.py` in an environment with Python 3 and SymPy. The script checks symbolic polynomial probability normalization for arbitrary parameters, both half-interval branch integrals, and independently evaluates the entropy and derivative-integral identity numerically for three rational parameter pairs. The expected end marker is `VERIFY_OK`.

The finite numeric samples are smoke tests only. The unconditional IID and all-horizon Shannon identities follow from the branchwise change-of-variables formula and conditional entropy chain rule in `RESULT.md`; sharpness follows from strict convexity and explicit limiting families. No mathematical assertion is made about arbitrary initial distributions or ergodicity outside stationarity.
