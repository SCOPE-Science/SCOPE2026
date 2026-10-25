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

# Reproducibility and verification limits

Run `python verify_rosexp.py` in an environment with Python 3, NumPy, and SymPy. This replays exact symbolic identities for the 2-by-2 matrix, its eigenvalues, its asymptotic norm coefficient, and the rational witness, followed by 450 deterministic-seed random symmetric negative-semidefinite matrix tests of the published PartRosExp2 identity. It also checks the reversed-order bound for a specified stiffness sequence. The checked code was executed with all assertions passing.

Universal results for all symmetric dissipative pairs, all dimensions and all positive step sizes are established by the written analytic proof, not by these finite checks. Inputs must satisfy the stated exact matrix assumptions and use the *published* PartRosExp2/PartExpRos2 formulas. No independent mathematical audit, experimental PDE validation or floating-point stability guarantee is asserted.
