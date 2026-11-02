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

# Reproducibility and limits

Execute `python3 certificate.py` with Python 3.10 or later. Expected terminal marker: `HONEYCOMB_222_DIHEDRAL_EXACT_OK`.

The checker independently enumerates 24 graph vertices, 30 graph edges, 20 perfect matchings, 66,369 nonempty simplices; 33,183 discrete Morse pairs with critical dimensions \((0,3,3)\); and a topological sort of all 420,294 directed cover relations. It tests all 12 graph symmetries and their exact signed action, comparing direct enumeration of fixed simplices with cycle-orbit enumeration. The expected traces on rational third homology are \((2,0,2,0,2,0)\) on rotations and \((0,-2,0,-2,0,-2)\) on reflections.

These are exhaustive finite calculations for the stipulated hexagon. The code alone is not a proof of a claim for arbitrary side length, and no such generalization is made. The main document establishes the discrete-Morse and Lefschetz deductions. There is no independent external validation or audit.
