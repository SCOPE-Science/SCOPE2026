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
# Verification and limits

Run `python verify.py` in an environment with SymPy and SciPy. The checker was executed successfully with all symbolic tangency and curvature identities, 24 integrated root-count comparisons at twelve parameter triples, and the critical \(1/n\) numerical consistency test passing. These checks detect algebraic or numerical implementation mistakes; the proof in RESULT.md establishes the infinitely many parameter cases, precise boundaries and global dynamics.

The checker is standalone and does not need any external data files, repositories or network access. The model assumes exact proportional harvest pulses without demographic or environmental noise. Independent scientific verification has not been carried out.
