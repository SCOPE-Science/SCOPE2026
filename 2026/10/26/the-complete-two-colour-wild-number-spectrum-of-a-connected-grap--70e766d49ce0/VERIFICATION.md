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

Execute `python3 verify_wild_spectrum.py` in the directory containing the accompanying files, using Python \(3.9\) or later and only its standard library. Compare stdout to `verify_wild_spectrum_output.txt`. The script independently enumerates all connected labelled simple graphs on \(n=3,4,5\) vertices and every surjective two-edge-colouring of each graph, computes every set partition for the deficiency bound, and constructs edge blocks by closing under all simple cycles. It verifies the full spectrum, both endpoints, and the count of upper-extremal colourings. The script also tests five six-vertex examples including paths, cycles, graphs with cut vertices and complete graphs.

The expected final marker is `VERIFY_OK`. Assertions fail on any discrepancy. Finite enumeration is corroborative only; it does not establish the universal mathematical statement. The unrestricted proof is given in `RESULT.md` and relies on the standard two-colour wild-number identity and matroid-union theorem. No independent audit has been conducted.
