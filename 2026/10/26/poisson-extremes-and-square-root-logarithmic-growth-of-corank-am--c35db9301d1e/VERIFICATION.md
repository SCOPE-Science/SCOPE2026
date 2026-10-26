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
# Verification record

Execute `python verify.py` with Python 3 and NumPy. The program evaluates exact transition and rank-distribution identities with `fractions.Fraction`, checks exact harmonic boundary equations for \(q\in\{2,3,4,5\}\), and enumerates small-field residual-border ranks. It computes killed-chain finite-horizon survival probabilities for selected thresholds and compares them against the predicted asymptotic. The output is stored in `verification_output.txt`.

Critical infinite steps were checked analytically: (i) elimination of the appended residual block is valid under invertible changes of basis, preserving conditional uniformity; (ii) the chain has negative drift outside zero and hence a finite mean return; (iii) the scale function gives the precise hitting probability; (iv) Kac's renewal-reward identity gives the cycle mean; (v) deterministic cycle-count sandwich and Bernoulli rare-event asymptotics yield the Poisson probability, including the incomplete-cycle boundary; (vi) dyadic Borel--Cantelli proves the almost-sure maximum asymptotic.

Numeric convergence at moderate thresholds can be slow, since the ratio between the two largest scale-function terms has only exponential—not superexponential—decay. Finite experiments do not certify the asymptotic laws and cannot prove literature novelty. The independent-audit channel is not performed.
