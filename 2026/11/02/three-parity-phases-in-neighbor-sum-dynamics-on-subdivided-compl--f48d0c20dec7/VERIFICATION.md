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

# Reproducibility and verification

Execute `python check.py` using Python 3 without third-party packages. Its finite-field arithmetic, adjacency construction, exact Gaussian elimination, trajectory enumeration, and expected-count formulas are included in the supplied program; no additional data files are required. The observed output is embedded in `verification_output.txt`.

The completed run reports 81 parameter pairs and 648 exact power-rank comparisons, plus 243 kernel-rank comparisons, over \(\mathbb F_2\). Direct enumeration of 71,240 initial binary configurations covers 13 parameter pairs; enumeration of 83,008 configurations over \(\mathbb F_4\) covers another four parameter pairs. Checks include both cyclic periods and first recurrence-entry times. Test cutoffs are not an infinite proof: the unrestricted statements follow from the incidence-matrix identities and rank/Jordan argument in `RESULT.md`.

The prior-work comparison is a qualified literature assessment, not an exhaustive literature or priority certification. Independent mathematical audit has not been performed.
