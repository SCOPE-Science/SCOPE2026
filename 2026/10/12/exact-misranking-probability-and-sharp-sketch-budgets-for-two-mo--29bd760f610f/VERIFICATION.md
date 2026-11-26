---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof of the starting-error deterioration law uses an exact conditional Cauchy probability. The scaled conditional probability has a Gaussian absolute-value limit in distribution. On the event that the diagonal gap is at least half its mean, a uniform second-moment bound upgrades this to convergence of expectations; the complementary event contributes at most a constant times \(\ell^{-1/2}\) after scaling. The midpoint comparison uses the top eigenprojector's diagonal difference and the classical beta ratio. For instance, \(\kappa=2,\ell=4\) gives the midpoint probability \(I_{1/5}(2,2)=13/125\). No finite numerical checks are needed to establish either limiting rate.
