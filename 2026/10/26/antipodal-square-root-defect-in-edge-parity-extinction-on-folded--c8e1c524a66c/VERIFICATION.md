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

# Finite reproducibility

Run `python3 check_folded_cube.py` with Python 3.8 or later. The file uses standard library only and constructs adjacency directly from graph edges, without the group-algebra proof implementation. It checks three powers over binary row bitsets for dimensions 3–7 and exhaustively iterates all 65,536 states in dimension 3. The recorded run output appears in `folded_line_verification.txt` with terminal marker `FOLDED_LINE_VERIFY_OK`.

# Limits

The tests are finite examples and do not certify the infinite statement, which rests on the incidence and quadratic normal-form proof. No external independent audit has been carried out.
