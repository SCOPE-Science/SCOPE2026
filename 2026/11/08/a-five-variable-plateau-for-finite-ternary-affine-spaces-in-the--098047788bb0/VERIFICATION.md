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

Run `python3 verify_direct.py` and `python3 verify_orbit.py` from a directory containing the extracted files, using the Python standard library. Compare stdout against `direct_output.txt` and `orbit_output.txt`. The direct program checks all triples and quadruples in dimensions zero through three. The orbit program constructs every affine dependence kernel for tuple widths two through five, computes all atomic signatures under four-ary `P` and equality, and iterates greatest-bisimulation refinement across dimensions zero through five. Its expected dimension thresholds are 1, 2, 3, and 3 respectively. `ORBIT_BISIMULATION=PASS` and `DIRECT_WITNESSES=PASS` were reproduced. The one-variable case is proved directly because all one-variable atomic formulas are universally true.

The unrestricted-depth theorem relies on explicit permanent pebble strategies in `RESULT.md`, not on finite checks. The bounded computation does not inspect every publication or independently certify novelty. No independent mathematical audit was performed.
