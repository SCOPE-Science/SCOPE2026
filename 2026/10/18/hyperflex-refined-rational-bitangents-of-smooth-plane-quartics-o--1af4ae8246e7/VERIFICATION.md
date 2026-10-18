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

# Verification of enumerated equations and contact strata

The C++17 census generates and checks every normalized equation up to the explicit finite projective group action. Its orbit-size weights partition all 7,174,453 normalized quartic equations and identify 805 smooth orbits. The analytic justification of the algebraic tests is given in `RESULT.md`.

## Executed checks

1. `python make_tables.py` generated `tables.hpp` with coefficient substitutions, thirteen rational-line restrictions, squarefree and double-root quadratic-square patterns and the derivative multiplication matrix.
2. `g++ -std=c++17 -O3 census.cpp -o census` and `./census > results.txt` reproduced the seventeen-bin distribution from `orbits.csv`, with totals 1,557 projective orbits, 805 smooth orbits, and 4,099,680 smooth normalized equations. The unique maximum row is code 78805, orbit size 312, nine proper bitangents and one hyperflex.
3. `python independent_groebner.py` used an independent symbolic check of the partial-derivative common zero in the three affine charts of projective space, passing for **all 1,557** projective orbit representatives.
4. `python verify_independent.py` independently generated the projective point/line system and another choice of each line's basis, constructed all quadratic restrictions symbolically, reproduced each of the 805 smooth-orbit bitangent classifications, and found group order 5,616 through permutation closure.
5. The printed orbit table and the complete 17-bin distribution agree exactly with the expected machine-readable `results.txt` and `orbits.csv`.

## Limits

This finite exhaustive certificate depends on arithmetic code and algebraic lemmas, and an independent external audit has **not** occurred. There is no claim of a formal proof-assistant certificate, generalization beyond this field, or independently verified novelty.
