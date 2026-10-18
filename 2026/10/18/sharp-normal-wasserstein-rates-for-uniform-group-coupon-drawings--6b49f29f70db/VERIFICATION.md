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

# Reproducibility

Execute `python verify.py` with Python 3 and SymPy available. The exact checker enumerates 949 finite rational occupancy laws and verifies all factorial moments after each deterministic packet-size sequence. It additionally checks 88 exact root-isolation certificates that the associated generating polynomials have only nonpositive real roots. These tests verify enumerated finite instances only; they are not used to infer universal real-rootedness or an infinite normal approximation.

The universal finite-horizon representation follows from repeated Gauss–Lucas and the factorization of a real nonpositive-root probability-generating polynomial. The stated limiting order follows from the exact pairwise moments, the standard normal Stein equation for 1-Lipschitz functions, and a lattice-distance lower test. A separate independent scientific audit has not been performed.
