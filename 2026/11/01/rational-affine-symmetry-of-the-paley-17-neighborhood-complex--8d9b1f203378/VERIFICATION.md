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

# Verification of the rational affine character

Run `python3 verify_character.py` from the extracted folder. No dependencies other than Python 3 standard library are used. The program reconstructs all faces from the 17 quadratic-residue neighborhoods, determines every mod-two simplicial boundary rank, and calculates each signed simplicial Lefschetz trace for the entire affine group of order 136. It also compares the resulting character against the explicit sum of two point-augmentation modules, one multiplier-sign line, and a two-dimensional quarter-turn module. `VERIFY_OUTPUT.txt` is the recorded output of a successful real execution ending in `VERIFY_OK`.

The exhaustive binary boundary calculation proves upper bounds on rational Betti numbers, not integral Smith invariants. Euler characteristic supplies the exact remaining rational Betti number. The character comparison and standard semisimplicity give an isomorphism over \(\mathbb Q\), not a preferred explicit basis. The finite checker has a fixed 17-vertex scope; it proves no statement for other graphs. No independent audit is represented by these checks.
