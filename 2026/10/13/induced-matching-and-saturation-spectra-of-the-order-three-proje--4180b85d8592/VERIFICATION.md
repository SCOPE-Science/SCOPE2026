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
# Verification and reproducibility

Place `verify_geometry.py`, `verify_independent.cpp` and `orbit_classes.csv` in one directory. Run `python3 verify_geometry.py` and `c++ -O2 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent`.

The first program uses point-subset/private-tangent enumeration over all 8,192 subsets. It asserts the complete seven-coefficient polynomial, unique single-flag extension for each of the 1,404 five-flag matchings, and every inclusion-maximal configuration. It derives the 5,616 projective linear collineations from actual generator permutations, adds incidence polarity, builds all twelve matching orbits and verifies the twelve-row CSV certificate with disjoint exhaustive coverage.

The separate C++ program constructs projective points and 52 flags independently, forms their conflict graph, and performs include/exclude independent-set enumeration; it independently checks the polynomial, 10,700 total systems, 1,989 and 234 maximal counts, and all 1,404 unique five-flag extensions. These checks were executed successfully from the packaged source directory. Both verifiers use exact integer arithmetic throughout.

Finite exhaustive certificates apply only to this 26-vertex Levi graph. The general four-flag maximality structure and other historical propositions are acknowledged as prior literature, not computer-derived originality. The present self-review is not independent validation; independent mathematical audit has not been performed.
