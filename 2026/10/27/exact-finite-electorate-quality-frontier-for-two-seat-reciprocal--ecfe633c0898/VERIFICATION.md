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

Run `python verify.py` using standard Python 3 from the package directory. The program directly enumerates voter groups under the defined reciprocal-JR and reciprocal-EJR affordability conditions and computes the highest-quality two-seat satisfying committee, separately for both axioms. It tests finite rational-quality and finite support-pattern instances, random larger ones with a fixed seed, and the exact sharpness profiles. Execution on the packaged program gave `CHECKS_OK 24407`.

The infinite-domain result is verified by the complete symbolic proof in `RESULT.md`, not by the finite checks. In particular the bound applies to every positive real quality and any finite approval pattern. The nonnegativity identity, equality cases, support assumption, and exact supremum/infimum quantifiers are stated there. This package performs no independent audit and makes no claim about axioms not included in the finding.
