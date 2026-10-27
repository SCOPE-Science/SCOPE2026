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

The standalone Python 3 standard-library checker `verify.py` passed 288 finite-model assertions. For three finite allowed-gap alphabets and six ordered threshold pairs (18 models), it checked the exact rational determinant identity at three scalar arguments, agreement of the expanded finite automaton spectral radius with the proposed scalar entropy root, and 12 direct enumerations of periodic binary words against traces of powers of the expanded finite adjacency matrix. The checker is executable with `python verify.py`.

These are finite-model checks only. The all-infinite-allowed-gap theorem, strict entropy loss and two-tail asymptotic are established by the analytic proof in `RESULT.md`, not by extrapolation of numerical experiments. No independent audit or external validation has been performed.
