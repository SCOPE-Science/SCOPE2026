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

# Reproducibility
Run `python verify.py` using Python 3 standard library. The test reconstructs the graph's open-neighborhood simplices directly from definitions, executes the two phase-specific collapse sequences and asserts that every deleted face has a unique codimension-one coface at its removal. It checks the original face vector \((3n,12n,12n,3n)\), the final face vector \((3n,9n,6n)\), connectedness of the triangular core, two incident triangles at every edge, and that every vertex link forms one cycle, for every integer \(n\in[5,40]\). See `verification_output.txt` for the successful execution. These finite tests do not prove every integer case; the independent uniform proof is given in `RESULT.md` by periodic triangulation and covering translations.
