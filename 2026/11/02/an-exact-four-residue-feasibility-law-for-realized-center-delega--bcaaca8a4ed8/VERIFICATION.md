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

# Verification of the four-residue feasibility law

Execute `python3 verify.py` in the directory containing the supplied standalone file. The program has no external dependencies.

The program implements the EF1 inequalities directly on every four-agent count vector, using integer numerators and denominators for the positive exceptional value. It compares existence against the stated residue formula over 13,860 rational parameter cases; the smaller cases enumerate every count composition, while the larger cases use the mathematically proved balancing property to restrict the count candidates. In addition, it enumerates every labeled assignment with seven, eight, and nine goods at ratio \(\rho=1/4\), observing respectively 1,260, 0, and 7,560 feasible assignments. It checks an explicit nine-good witness and the twelve-good example's infeasibility.

This is a reproducible finite sanity check, not a machine proof of the universal theorem. The proof of the general parameter law is in `RESULT.md`. No external or independent audit was performed.
