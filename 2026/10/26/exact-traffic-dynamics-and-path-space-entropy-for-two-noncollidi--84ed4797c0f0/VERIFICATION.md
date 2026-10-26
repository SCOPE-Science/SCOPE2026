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

The executable `verify.py` reconstructs the two-state killed matrix and checks its explicit positive eigenpair for integer graph sizes \(2\le m\le30\). For \(2\le m\le6\), it independently constructs the full labelled collision-free state-space generator, transformed generator and invariant weights and checks lumped transition rates. The recorded execution in `verification_output.txt` passed 601 assertions. Reproduce with `python verify.py` using Python 3, NumPy and the standard library. No random sampling is used. An analytic two-state generator reduction proves the claim for every integer \(m\ge2\); the finite computation is supplementary. Independent audit was not performed.
