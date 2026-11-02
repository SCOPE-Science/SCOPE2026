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

# Verification of the Gaussian GEPP edge coefficient

Run the standalone standard-library Python script `python verify.py`. It compares the explicit pivoted Schur complement with an independent expression in ordered magnitudes and signs on 35,000 reproducible Gaussian matrices; checks the deterministic upper bound; evaluates the exact Gaussian integral; checks representative inequalities for the two edge regions; and runs 750,000 seeded sampling trials. During preparation, the script reported `PASS: 74,001 deterministic checks; 750,000 seeded Gaussian trials`, with coefficient `0.050660591821`.

The proof, not the random trials, establishes the infinite-limit claim. The essential checks are the factor \(1/2\) from signs, the ordered-density factor \(2\), both leading triangular regions, the smaller third region, and the integral \(\int_0^\infty\int_0^t ptf(t)^2f(p)^2\,dp\,dt=1/(2\pi^2)\). The leading asymptotic at a finite noninfinitesimal threshold need not equal its exact probability.

No independent mathematical audit or external certification is claimed. Full-text review of all possible historical sources remains incomplete.
