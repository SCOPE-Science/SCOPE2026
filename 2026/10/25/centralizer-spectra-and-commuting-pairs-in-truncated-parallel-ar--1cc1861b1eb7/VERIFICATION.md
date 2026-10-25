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
The standalone `verify.py` constructs finite-field linear systems from the pathwise commutator, not from the support-run formula. Gaussian elimination gives the nullity of every such system in the tested ranges. A separate pairwise tensor-product test enumerates commuting arrays when feasible, and a recurrence cross-check evaluates the rational generating function. All assertions in the script are executable under Python 3 with no third-party dependencies. Run `python verify.py`; the expected completion marker is `VERIFY_OK_PARALLEL_ARROW_COMMUTANT_CENSUS`.

The checks use prime fields of orders two, three and five; the proof is field-independent and establishes the formulas for all prime powers. Computation does not establish historical priority, independent validation, or additional cases not entailed by the proof.