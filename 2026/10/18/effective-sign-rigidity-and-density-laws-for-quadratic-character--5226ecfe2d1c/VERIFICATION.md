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
# Verification checks and boundaries

The script `verify_signs.py` evaluates the exact integer binomial transform and checks the eventual signs for every odd prime from 3 through 37. For each prime it traverses all indices up to the stated cutoff plus three times the prime. It additionally checks the exact forced zero rule at multiples of the prime and the predicted sign counts in one complete period. The executable check is finite; the infinite theorem follows only from the Fourier/Gauss evaluation and the spectral-gap estimate in `RESULT.md`. No independent audit has been performed.
