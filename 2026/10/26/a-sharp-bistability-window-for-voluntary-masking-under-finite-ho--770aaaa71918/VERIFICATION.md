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

The proof is analytic and applies to every real \(0<q<1\), \(\lambda>0\), \(\ell>0\), \(c>0\) in the stated strict window. The derivative of \(H\) has exactly one zero, and a monotone-branch crossing argument gives an if-and-only-if characterization of two distinct interior symmetric Nash mixtures. The replicator signs on each interval give local asymptotic stability and instability.

Standalone check: `python verify_poisson_mask.py`. The program verifies the rational factorization at \(q=1/2\), \(\lambda=2\), \(\ell=1\), \(c=63/256\), checks endpoint and interior signs, and tests representative parameter windows. The root fractions are obtained by algebra, not by numerical root-finding. Finite samples do not certify the universal theorem; the calculus proof is necessary.

Scientific limitations: symmetric nonatomic population, fixed prevalence, Poisson thinning, risk-neutral loss, no normative benefits, specific replicator dynamics. Literature overlap remains possible, especially in the complete text of the 2025 network-mask study that was not accessed. No independent audit or validation has occurred.
