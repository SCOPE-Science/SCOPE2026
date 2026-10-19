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

# Reproducible checks
Run `python3 verify.py` using Python 3.8 or later; only the standard library is required. The code generates the two-strand observations literally and enumerates all unordered pairs of length-n words for n=2..10. It independently calculates the Minkowski sum of all single-strand two-mer count vectors for n=11..17, checks the explicitly characterized feasible profile set, and verifies count formula bounds for n=18..127. The final marker is `THEOREM_BOUNDARY_CHECKS_OK`.

The mathematical proof establishes the theorem for all n>=2. Finite checks alone could not do so; no claim of independent auditing or external certification is made.
