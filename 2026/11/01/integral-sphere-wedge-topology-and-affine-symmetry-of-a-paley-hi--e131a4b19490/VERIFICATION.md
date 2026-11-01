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

# Reproducibility and verification

Run `python3 verify_paley17_ind2.py` and `python3 verify_morse_elimination.py` from the directory containing both scripts. Only the Python 3 standard library is needed. Their captured outputs are `verification_output.txt` and `morse_elimination_output.txt`.

The first script reconstructs the residue set and all 131071 nonempty subsets; confirms strong-regular parameters, face vector and downward closure; verifies integral boundary-square-zero identities over the full face poset and independent mod-two ranks; constructs the 423 toggle pairs; topologically sorts every directed Hasse incidence to prove acyclicity; computes exact integer critical-cell differential by signed gradient-path recursion; verifies primitive attaching degree; exhaustively computes signed Lefschetz traces of all 136 affine automorphisms and checks the character average.

The second script separately performs signed integer column elimination on the full tetrahedron-to-triangle incidence matrix using the 219 matching pairs in those degrees, finding the same 19 critical tetrahedron attaching-degree histogram. This serves as an independent computational method within the same environment, not an independent audit.

Output marker: `PALEY17_IND2_INTEGRAL_MORSE_AND_AFFINE_CHARACTER_OK`. Checked critical-cell dimensions: one 0-cell, one 2-cell, nineteen 3-cells. The integral boundary row has gcd one, yielding a wedge of eighteen 3-spheres. The character covers exactly the order-136 affine subgroup, not an independently identified full automorphism group. Numerical and homotopy conclusions are confined to the specified 17-vertex graph. No independent audit has been performed.
