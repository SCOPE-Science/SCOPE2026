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

Run `python3 checks/direct_refinement.py` and `python3 checks/quotient_signatures.py` from the package root. Both use only Python's standard library. Recorded outputs in `checks/direct_output.txt` and `checks/quotient_output.txt` are reproduced by the supplied scripts.

The first program constructs every graph for its parameter range, performs colour refinement with the original vertex neighbourhoods, and compares partitions at every round. The second uses a separately implemented quotient transition on cyclic-distance classes and checks every predicted pair of distance-shell colors. It also tests the antipodal seam witness by a direct modular-arithmetic count.

These checks cover finitely many graphs and do not prove an all-parameter claim. The general proof is in `RESULT.md`. No independent scientific audit or external certification has been performed.
