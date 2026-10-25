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

# Computation verification

Run `python3 verify_closed_neighborhood.py` in a standard Python 3 environment. The script has two independent face representations (ordered tuples and bit masks) and two separate exact elimination implementations (symmetric-difference sets and XOR integer bitsets). It exhaustively produces all simplices, not an estimate, random search, heuristic, or truncated enumeration. Assertions compare all face counts and ranks with the reported table for each integer parameter from 2 through 6. The Euler identity is checked. No third-party dependency, external file or network access is needed.

The finite calculations certify only reduced homology with coefficients in the field of two elements. They do not certify fundamental groups, integral torsion, wedge decompositions or any input beyond this range. An external independent audit has not been performed.
