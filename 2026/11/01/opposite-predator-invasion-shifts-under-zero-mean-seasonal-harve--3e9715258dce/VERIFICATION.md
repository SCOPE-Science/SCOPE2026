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

# Reproducible checks and limits

The full proof is in `RESULT.md`. A separate finite check is in `checks/verify.py`, with dependencies pinned in `checks/requirements.txt`. After installation, run `python checks/verify.py`.

Successful execution checked exact rational trapping margins, closed-form response values and derivatives, positivity and curvature on the stated interval, numerical convergence of the period map, and three distinct zero-mean periodic harvests. The computed prey mean–variance identity agreed within \(2\times10^{-9}\). All six signed invasion-shift inequalities were strict in the expected directions. For the three forcing profiles, numerical variance was approximately \(0.00036008618\), \(0.00017178472\), and \(0.00000840084\), respectively. These computations are not exhaustive over waveforms, parameters, periods, initial states, or nonlinear predator–prey dynamics; universal statements depend on the supplied exact proof.

At a zero transverse exponent, or outside the trapping and curvature assumptions, the findings make no stability prediction. This self-review is not independent scientific validation.
