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

# Reproducibility checks and limits

Execute `python3 checks.py` with a standard CPython installation; no third-party packages are required.

The script checks 180 distinct exact-rational cancellations of the three environmental log-odds derivatives and the harmonic resonance relation; 250 random environmental triples for both logistic envelopes and their equality-attaining configurations; a 30-time-unit fourth-order Runge--Kutta integration of all five equations for admissible payoff matrices and mismatched feedback, obtaining a maximum absolute affine-drift residual of approximately \(3.05\times10^{-11}\); and a fully asymmetric resonance example with zero residual in all five equations. The original source's illustrative parameters \((3,5,8)\) give the exact identities \(\Delta=-7/36\) and \(\lvert\Delta\rvert/W=7/23\).

The unrestricted theorem is proved algebraically from the environmental differential equations; finite rational and numerical checks do not verify behavior for all times or all initial states. The optimality claim is pointwise conditional on \(H\), not a claim that a particular trajectory realizes equality at arbitrarily late times. No global convergence to an individually chosen boundary face is asserted.
