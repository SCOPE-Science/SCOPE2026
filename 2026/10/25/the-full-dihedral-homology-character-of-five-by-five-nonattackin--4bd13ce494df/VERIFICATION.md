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

# Reproducibility

Run `python3 verify_king_d4.py` with standard Python 3. The package does not require an external dataset. It checks all 6427 faces, acyclicity of 3174 pairs, the maximality of 79 critical faces, exact integral chain projection/lifts, eight integer D4 matrices, their group relations and signed simplicial Lefschetz traces. It prints the three class-character rows and irreducible multiplicities and exits only after asserting all stated equalities. These are exhaustive finite checks, not numerical approximations; mathematical identification of homology uses discrete Morse theory. Limits: this does not establish a general-width statement, an integral module classification, or the nonexistence of unindexed prior equivalents.
