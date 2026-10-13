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

# Reproduction and limits

Execute `python3 artifacts/verify.py` using Python 3 and the standard library. The script independently computes residues using a forced/optional-parts dynamic program and a separate implementation of the published generating-function coefficients, comparing them modulo 128 at all indices from 0 through 300. It then checks the explicit modulo-eight formula and the sharpness witness at 36. The file `artifacts/verify_output.txt` contains the captured successful output. These arithmetic tests are finite; the theorem for every positive integer is proved by formal coefficient identities in `RESULT.md`. No external checking, independent audit or automated proof certification is claimed.
