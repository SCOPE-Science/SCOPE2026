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

# Exact reproducibility checks

The standalone `verify_c7_product.py` requires only Python 3 standard-library modules. Execute `python3 verify_c7_product.py` from the directory containing the file. On success, it prints `C7K3_COMPLETE_INTEGER_MORSE_AND_84_EQUIVARIANT_CHARACTERS_OK`.

Checks made in the executable: all 21 graph vertices and all 5,281 nonempty independent simplices; the face vector; 2,638 matched pairs with exact global Hasse acyclicity; five critical simplices with dimensions 0,3,4,4,4; zero integral Morse boundary; signed integer cycles with 16,90,96,154 terms; each of the 84 dihedral-color permutations; integral action matrices; expected irreducible characters; and equality with exact signed Lefschetz fixed-face counts.

The algorithm is finite and exhaustive for the named graph. It does not certify claims about other products or the integral topology of the quotient. No independent external audit was performed.
