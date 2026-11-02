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

Run `sh reproduce.sh` in the directory containing this file and the two Python source files. The scripts require Python 3 and only the standard library.

`verify_rank4.py` evaluates full recursive Ehrenfeucht–Fraïssé types in pure equality-and-adjacency logic, including repeated selected vertices, on Latin-square incidence graphs of orders 2, 3, 4 (both nonisotopic group tables), and 5. The check gives one rank-three theory and the three rank-four classes stated in the theorem. This exact finite computation proves the specific rank-four order-three-versus-order-four separation, but not the infinite stabilization.

`verify_geometry.py` independently constructs hidden incidence-diagram classes on up to three selected vertices, compares their fourth-vertex adjacency extension sets for the two nonisotopic order-four squares, and checks the universal integer count inequalities. It finds 2, 10 and 85 structural classes at tuple lengths 1, 2 and 3 in each order-four example. The uniform infinite strategy in RESULT.md rests on the displayed exact formulas and case analysis, not on extrapolating these finite runs.

The archived `verification_output.txt` is the actual output of the reproduction script. The deterministic programs can be rerun separately. Neither an independent mathematical review nor an exhaustive claim of historical priority is implied.
