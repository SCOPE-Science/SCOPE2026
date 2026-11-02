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

# Reproducible scientific checks

Run `python3 verify.py` with Python 3 from the directory holding the script. It requires only the Python standard library and uses a fixed pseudorandom seed for deterministic repeatability.

The observed execution passed these groups: 394 exact finite-horizon tangent identities for arbitrary environmental words; 70 exact-rational positive Markov demographic models in dimensions two and three; 455 strict-positive stationary sensitivity entries; and 2,400 Markov-word enumerations validating the block conditional-moment recursion. The noncommuting two-environment example was reconstructed by exact rational arithmetic, including its stationary law, block moment vector and iid comparison. Two paired finite-difference simulations of length 220,000 produced derivatives approximately 0.1898033 and 0.0598874, compared with exact 0.1904762 and 0.0595238, within the declared test tolerance 0.004.

These are finite, deterministic and stochastic diagnostics; they do not independently establish the theorem for every dimension, Markov matrix or perturbation. The infinite/general claim rests on the normalized positive-matrix contraction and exact stationary-moment proof in RESULT.md. No external independent audit or validation has been performed.
