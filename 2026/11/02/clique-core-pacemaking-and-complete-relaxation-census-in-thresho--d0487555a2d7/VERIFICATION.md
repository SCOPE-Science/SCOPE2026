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

The attached `certificate.json` records complete quotient trajectories for exactly 676 possible six-cohort capacity signatures. Every possible labelled starting state on a complete split graph maps to one of these signatures without loss of trajectory or first-periodic-entry information. `verify.py` recomputes all trajectories, their first repeat and least period, and checks the all-signature histogram and the sharp witness signatures. The same program independently implements literal vertex-neighbor updates, exhaustively comparing 221436 labelled initial states through nine total vertices and verifying six independent labelled-count census instances. The recorded execution in `verification_output.txt` terminated with `SPLIT_GHM_THRESHOLD_TWO_ALL_CHECKS_PASSED`.

Reproduction: place `verify.py`, `certificate.json`, and this file in one directory and execute `python3 verify.py`. Standard Python 3 is the only dependency. The six-cohort reduction is essential to all-size coverage; the finite microscopic checks alone do not establish a theorem for arbitrary sizes. The numerical pacemaker probability bound follows from a union bound and is established analytically, not through sampling. No independent audit has been performed.
