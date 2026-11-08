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

# Reproducible verification

Run `python3 verify.py` from the directory containing the supplied standalone verifier. The program constructs the labelled graph and tests actual two-edge paths without presupposing the factor formula.

The exhaustive cases are \(n\in\{2,3,4\}\), covering \(16,512,65536\) two-colour edge assignments respectively. Each is compared with the closed-form coefficient vector; total counts are \(10,126,4050\) and minimum-blue counts are \(4,9,16\). For each \(n\in\{5,6,7,8\}\), 25,000 reproducible assignments check the direct graph-path predicate against a separately coded local-pair predicate; these tests are sampling, not an exhaustive census. Reciprocal coefficient symmetry, the minimum coefficient and the specialization at one are additionally checked. Expected final line: `VERIFY_OK`.

The infinite theorem depends on the explicit necessary-and-sufficient Boolean path analysis and independent product argument in `RESULT.md`; finite checks do not prove all integers \(n\ge2\). No independent audit has taken place.
