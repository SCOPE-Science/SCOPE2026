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

# Reproducibility and limits

The stand-alone Python 3 script `verify_components.py` uses only the Python standard library. Execute `python3 verify_components.py` alongside this file. It verifies five exact rational tail inequalities, the elementary rational bound associated with the stated prime-ratio theorem, prime-power cutoff factors, all thirty-two candidate intervals, and their exhaustive merging into fourteen strictly separated components. The script uses the rational enclosure \(P_{1000}\le P\le P_{1000}/(1-1/(2\cdot1000^2))\), so no floating-point comparisons are used in correctness assertions; approximate decimal output is only illustrative.

The infinite proof uses the published Nagura prime-gap theorem and the completely stated subsum argument; finite checking does not substitute for them. This verification concerns the closure of the range and does not claim that all interval points occur as individual arithmetic-function values. No independent mathematical audit has been performed.
