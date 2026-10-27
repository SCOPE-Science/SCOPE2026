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

# Reproducibility

Run `python3 verify.py` with Python 3.10 or later, using only the standard library. The included `verification_output.txt` contains the recorded successful output. The script must be run against the file actually contained in this package; no prior-run data or external certificate is required.

The code builds each signed ordered-pair transition matrix directly; computes traces of the first \(k(k-1)\) powers; reconstructs all six exact characteristic polynomials by Newton identities and checks them against the stated factorizations; evaluates the even four-rim-color and odd five-rim-color root-sum formulas for 51 instances against an independently written parity dynamic program; computes the exceptional 14-rim six-color count both by an all-sign trace and by a direct parity dynamic program; directly enumerates canonical rim partitions for wheel orders 3 through 11 and tests the original neighborhood strong odd condition; checks all seven construction seeds and forty insertion extensions.

All arithmetic is integer exact. Characteristic-polynomial checks involve finite matrices of dimensions 12 and 20. The exceptional trace uses a dimension-30 matrix. Computed cases do not prove the all-order enumeration or asymptotics; those follow from the trace-word bijection, the finite characteristic-polynomial identities, parity projection and the spectral argument in `RESULT.md`.
