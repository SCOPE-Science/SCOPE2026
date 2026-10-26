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

Run `python3 verify.py` with Python 3 and its standard library. The verifier computes the two-stage Radau IIA rational endpoint using a direct exact \(2\times2\) matrix inverse and independently reconstructs the stationary-projector update. It compares both matrix constructions, row sums, the exact polynomial sign criterion and strict positivity of two-step matrices for 3,360 exact-rational rate/step choices. It checks the rate-ratio threshold, critical tangency, and the exact witness \((a,b)=(19,1)\), including both endpoint steps and the negative entry at \(h=1\). This run completed with the message `PASS: 3360 direct 2x2 exact matrix reconstructions, mass/positivity, two-step checks; exact witness and critical constants`.

The proofs of the universal assertions use the rank-one Markov projector, the exact quadratic discriminant, and inequalities for the rational amplification factor. Numerical verification is neither exhaustive over a continuum nor a substitute for the proof. The source is reproducible without external datasets. Independent mathematical audit is not performed.
