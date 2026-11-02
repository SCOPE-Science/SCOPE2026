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

# Reproducibility record

The exact checker `verify.py` was executed with Python 3 and SymPy 1.14.0 and completed with `VERIFY_OK`; `verify_output.txt` contains the observed output. It builds projective points over \(\mathbb F_9\), enumerates exactly \(112\) totally isotropic Hermitian generator lines, identifies \(48\) specializations of characteristic-zero Fermat lines and \(64\) complementary lines, and calculates exact incidence, characteristic polynomial and intersection-matrix ranks. The complex-to-characteristic-three geometric-line completeness, K3 Hodge index theorem and supersingularity/Picard rank \(22\) are proved in the cited primary literature rather than inferred from a finite search. No independent scientific audit has been performed.
