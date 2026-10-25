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

# Reproduction

Execute `python check.py` with Python 3.10+ and compatible SymPy (checked with 1.14.0). It generates the twenty-one arcs by the stated modular rule, exhaustively tests all arc subsets, validates the full acyclic matching, computes the exact reduced Morse differential, constructs the cellular rotation quotient with signed boundaries, verifies boundary composition, and recomputes all integer Smith factors.

Observed assertions: face counts \((21,168,630,1113,819,175)\), critical reduced Morse counts \((24,54,17)\), Morse \(\partial_4\) Smith rank eleven with all factors units, quotient Smith nonzero lists \((1,1)\), \((1^{21},7)\), \((1^{68})\), \((1^{88},7,7)\), \((1^{20})\) by increasing boundary degree. Direct full-chain modular boundary ranks in degrees one through five were independently \((20,148,482,618,158)\) over both \(\mathbb F_7\) and \(\mathbb F_{101}\). The integer torsion claim relies on the exact Smith calculation, not on those modular tests.

The computation proves homology and the rational cyclic module at this one tournament. It does not compute an integral group-ring lattice or a full homotopy classification, and it is not an independent external audit.
