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

# Reproducible mathematical checks

The program `verify_fano_pencils.py` enumerates all \(512\) binary three-by-three matrices and exactly \(256\) distinct corresponding plane-filling quartic forms. A \(66\)-row binary rank computation on the degree-ten homogeneous ideal component finds exactly \(24\) geometrically smooth forms. It checks the equivalence with absence of a binary eigenvector for every matrix representative, lists all \(8\) compatible pencils, and computes the \(168\)-element projective group orbit, order-\(21\) pencil stabilizer and coincident order-\(7\) member stabilizers. The full observed output is `OUTPUT_MAIN.txt`.

The independent C++ program `verify_singer_matrix.cpp` uses a direct irreducible-characteristic-polynomial test, matrix addition modulo binary scalars and projective matrix conjugation to reproduce \(48\) irreducible matrices, \(24\) individual forms, \(8\) compatible pencils and a single eight-element orbit with stabilizer \(21\). The observed output is `OUTPUT_MATRIX.txt`.

To replay, run `python3 verify_fano_pencils.py`; compile the C++ source with `g++ -std=c++17 -O2 verify_singer_matrix.cpp -o verify_singer_matrix` and run `./verify_singer_matrix`. No external libraries beyond Python's standard library and the C++ standard library are required.

The geometric base-locus claim is established algebraically: seven reduced rational intersection points, three Frobenius-conjugate Singer eigenpoints, absence of other seven-element orbits by Bézout, and total multiplicity \(7+3\cdot3=16\). It is not asserted to follow from a bounded finite-extension search.

The two checks are independently written but not independently peer reviewed. Inaccessible historical full papers may conceal equivalent results. No external audit has been performed.
