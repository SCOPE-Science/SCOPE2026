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

# Verifiable mathematical checks

The companion `verify.py` can be run using Python 3.10 or later and only the Python standard library. It independently enumerates finite-tree admissible labelings with exact rational weights (checking root ratios against the transfer recurrence), checks exact rational identities for the cubic normal-form coefficient, and compares finite critical-window boundary differences against the asymptotic formula.

Observed local execution: `VERIFY_OK: 42 exact independent finite-tree partition comparisons; 10 exact cubic coefficient identities; 48 finite-depth crossover checks; worst_relative=0.00122794`.

Finite enumerations and numerical depths are not proofs of an infinite limit. The analytic verification in `RESULT.md` establishes the normalized inverse-square recursion, proves uniform \(\Theta(n)\) control of its transformed trajectories in the critical window, and identifies the limiting coefficient. The recursion for finite trees and the known uniqueness threshold are cited to earlier primary literature. The review does not certify historical uniqueness or provide independent auditing.
