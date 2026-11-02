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

# Verification of the exact finite-field rank census

Run `python3 check_nijenhuis.py` with a standard Python 3 interpreter. The bundled `checker_output.txt` records the exact output. The verifier uses no external packages, constructs the matrix algebra product from the four matrix-unit coordinates, enumerates subspaces in reduced row echelon form and tests multiplication closure. It then tests direct-complement dimension and reports the rank histogram in the fields of orders \(2,3,4,5,8\). The two nonprime fields use genuine extension-field polynomial multiplication, not residue arithmetic modulo four or eight.

For the smallest field, the program independently examines all \(65536\) linear endomorphisms of the four-dimensional vector space, filters idempotents by direct composition, and checks the associative Nijenhuis identity on every ordered pair of matrix units. The result is exactly \((1,12,60,12,1)\) across ranks zero through four, agreeing with the independently constructed subalgebra census.

The other verified rank histograms are \(q=3:\ (1,36,168,36,1)\), \(q=4:\ (1,80,360,80,1)\), \(q=5:\ (1,150,660,150,1)\), \(q=8:\ (1,576,2448,576,1)\). The program prints `M2_ASSOCIATIVE_NIJENHUIS_ALL_CHECKS_OK` only if every field case matches the closed formulas. Exhaustion was carried out within these five fields only. The general assertion for every prime power depends on the symbolic subalgebra classification and complement counts in the proof, not extrapolation from these checks.
