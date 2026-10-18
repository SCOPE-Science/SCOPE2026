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

# Reproduction
Run `python3 verify_icosa_4cut.py` using Python 3 and SymPy. It reconstructs graph, faces, complete directed Morse Hasse graph, and integral Morse boundary, verifies acyclicity and Smith diagonal, and prints the exact homotopy outcome. Run `python3 independent_face_count.py` using only Python 3 standard library for independent face counts and reduced Euler characteristic. Both programs execute from their own directories and require no other data files. Compare stdout with `verification_output.txt`.

# Boundaries and limitations
Both programs enumerate finite sets for the fixed graph. The Morse acyclicity and integral boundary calculation, together with CW and Hurewicz arguments in RESULT.md, justify the infinite homotopy-type assertion for this *finite* complex. Numeric homology alone would not. No independent external audit is represented here.
