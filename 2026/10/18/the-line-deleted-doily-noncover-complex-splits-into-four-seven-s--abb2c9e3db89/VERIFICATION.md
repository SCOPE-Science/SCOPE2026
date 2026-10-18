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

# Reproducible finite verification

Execute `python3 code/verify.py` using a standard Python 3.9+ interpreter. Compare its standard output byte-for-byte with `code/expected.txt`. The program constructs all fifteen duads and all fifteen synthemes from their definitions, forms the downward closures, and verifies full face-poset gradient acyclicity with a topological sort on every codimension-one incidence. It also enumerates the full \(S_6\) and the 48-element line stabilizer, computes rational homology characters from Euler–Lefschetz fixed-simplex sums, and independently checks all 48 stabilizer traces with signed oriented simplices.

All integer counts, incidence tests and character sums have assertions in the program; it uses no approximate arithmetic. The program proves the finite hypotheses for the matching and homotopy-pushout arguments written in `RESULT.md` but does not itself automate general theorems from discrete Morse theory or homotopy theory. The independent audit status remains not performed.
