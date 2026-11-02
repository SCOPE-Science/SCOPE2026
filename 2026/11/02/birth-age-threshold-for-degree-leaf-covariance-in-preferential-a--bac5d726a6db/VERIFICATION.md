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

# Reproducibility and verification

Run `python verify.py` with Python's standard library; no other package or input file is required. The program starts from the two-vertex edge and constructs the exact preferential-attachment distribution over degree sequences through eight vertices by assigning each attachment its conditional rational probability. It independently evaluates the mixed moments of a birth-rank degree and the total leaf count and checks them against the exact closed formula. It also checks rational recurrence/telescoping identities and finite sign profiles up to 31 birth ranks. The executable prints `VERIFICATION_OK` and its assertion count when all checks pass.

The proof in RESULT.md establishes the product identity and the existence of the unique covariance sign transition at *every* eligible birth rank and tree size, as well as the asymptotic threshold. Finite verification is not a proof of unbounded quantifiers or historical novelty. The public literature comparison examines the mathematically related age-independent and degree-stratified results, with unresolved priority risk noted in RESULT.md.
