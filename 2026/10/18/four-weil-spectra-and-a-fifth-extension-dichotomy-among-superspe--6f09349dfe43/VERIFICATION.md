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

# Exact verification and reproducibility

Run the following commands with Python 3 and a C++17 compiler:

```sh
python3 verify_characters.py
python3 verify_counts.py
g++ -O2 -std=c++17 verify_extensions.cpp -o verify_extensions
./verify_extensions
```

The first program enumerates all regular-differential pairs from the valuation inequalities, obtains the five one-form characters and the ten first-cohomology characters, and multiplies ten cyclotomic factors in the exact integer ring \(\mathbf Z[\xi]/(\Phi_{15}(\xi))\). Each coefficient of each of the fifteen degree-ten products is compared to its claimed integer formula.

The second enumerates cubes and affine parameters directly in the quadratic finite fields defined by adjoining a square root of two to \(\mathbf F_{11}\) and \(\mathbf F_{29}\). It verifies all fifteen first-degree point counts, including the two rational ramification points over zero and infinity. The normalized curves have respective counts \(232\), \(122\), \(67\) for the three point-count categories over \(\mathbf F_{121}\), and \(1132\), \(842\), \(697\) over \(\mathbf F_{841}\).

The C++ program independently certifies that \(X^4+X+2\) is irreducible over \(\mathbf F_{11}\), constructs \(\mathbf F_{11^4}\), and counts cube roots of \(-t^2(a+bt^5)\) for all fifteen coefficient cosets from the quadratic subfield. It verifies second-extension counts \(13432\), \(14642\), and \(15247\), according to the corresponding first-degree category. In each computation the number of ramified points is established by the geometric cover description; it is not inferred from the singular plane model.

All three programs completed successfully and reproduced `CHECKS.txt`. The integer polynomial product is exact, but the numerical point computations test only two primes and the first two extension degrees in those examples. The proof in `RESULT.md`, not an experiment or an unrun long extension-field enumeration, supports all-prime classification and fifth-extension consequences. No external independent audit or certification is asserted.
