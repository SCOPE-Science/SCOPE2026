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

# Verification details

Run `python verify_trapped_turns.py` with Python, NumPy and SymPy. The program checks the generator recurrence symbolically, separately assembles the real-space stationary Markov equations for four headings at a rational parameter set, and samples exact Poisson intervals for three turning distributions sharing a first angular harmonic. Its current execution passed 21 assertion groups. The infinite-class sharp bounds and endpoint uniqueness come from the analytic recurrence plus Jensen rigidity, not from enumeration. No independent audit or external certification was performed.
