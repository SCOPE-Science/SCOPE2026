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
Use Python 3 with the standard library. Execute `python3 verify_maxdegree2_k6.py` in this directory. The code explicitly enumerates all possible subsets of the 15 simple graph edges, verifies face admissibility by two methods, checks all 7,440 oriented Hasse incidences for gradient acyclicity, and reduces the oriented integral Morse complex through unit pivots. It computes the determinant of the listed 14-by-14 Morse boundary minor in integers and checks the mod-two and mod-three simplicial boundary ranks independently.

For the symmetry claim, two separately formulated character calculations are compared: signed traces of individual invariant simplices and alternating orbit-subcollection counts. Each computes the character on representatives of all 11 conjugacy classes. Inner products with Specht characters derived from Jacobi–Trudi give five multiplicity-one constituents and no others. `verification_output.txt` is the recorded stdout, ending with `VERIFY_OK`.

This is a bounded, finite proof of the single six-label case. The verifier does not establish originality relative to every publication, infer an infinite family from finite tests, or constitute independent external validation.
