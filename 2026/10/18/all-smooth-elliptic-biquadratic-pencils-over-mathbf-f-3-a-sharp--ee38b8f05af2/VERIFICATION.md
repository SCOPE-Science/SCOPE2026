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

# Verification
The supplied files provide executable, finite, exact checks for the claimed classification.

1. `groebner_check22.py`: enumerate all 9841 projectivized ternary biquadratic equations and check the full Jacobian ideal on each of the four affine charts of the split quadric. The output contains exactly 5184 smooth form identifiers.
2. `pencil22.cpp`: independently determine smoothness by the squarefree quartic branch discriminant and count all eligible unordered generator pairs; verify 3594672 pairs and six representations per pencil. Print counts 115848, 306432, 153792, 23040 by common rational base-point cardinality.
3. `rref_pencils.cpp`: enumerate every two-dimensional linear subspace of the nine-dimensional section space in reduced-row-echelon form and accept only four-member smooth pencils from the algebraically generated file `groebner_smooth_codes.txt`. It reproduces exactly 599112 pencils and the same distribution with no duplicated subspaces.
4. `witness_check.py`: check geometrical smoothness by four Gröbner charts for each of the four members of the explicit displayed extremal pencil and compute the three common rational points.

Compile with `g++ -std=c++17 -O3 -o pencil22 pencil22.cpp` and `g++ -std=c++17 -O3 -o rref_pencils rref_pencils.cpp`. Run `python groebner_check22.py`, `./pencil22`, `./rref_pencils groebner_smooth_codes.txt`, and `python witness_check.py`. The supplied `.out` files are expected exact outputs; `groebner_smooth_codes.txt` is the expected checker-generated dataset. Each output is independently recomputable, not a substitute for examining the implementation. Characteristic-three algebra and the exact finite list bound the scope. Independent external audit is not performed.
