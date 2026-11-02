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

# Finite reproducibility checks

Execute `python3 verification/check.py` from the package root, using Python 3.10 or later and its standard library only. The expected summary is recorded in `verification/output.txt`.

The checker uses exact rational arithmetic to compare short-horizon killed-walk probabilities and the full Bellman recursion, then checks the explicit error certificate numerically over horizons \(32\le n<6000\) and selected other parameters. For a smaller collection of horizons it computes the genuinely optimal stopping and continuation values and tests domination by the certificate. It asserts only finite quantities; neither its bounded iteration nor numerical floating-point output establishes any infinite-range theorem.

The universal result is proved independently in `RESULT.md` using the stopping-time split, a likelihood ratio at first passage, Hoeffding's bounded-sum inequality, and the elementary finite-horizon envelope. No independent audit or external formal verification was performed.
