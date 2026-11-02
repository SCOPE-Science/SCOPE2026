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

# Verification guide

The file `check.py` is standalone and requires Python 3 with only the standard library. Run `python3 check.py` alongside `check_output.txt` to reproduce exact-rational finite path/transfer identities and seeded numerical spectral comparisons for the rank-one model. The recorded output is given in `check_output.txt`.

The finite calculations do not establish the infinite theorem. Its decisive steps are the finite Gibbs variational identity, entropy-superadditivity bound, Cesàro control of old-memory coefficients, the stationary iid change of measure, and a variance-controlled logarithmic Taylor inequality. No independent audit, external certification, or formal proof verification has been performed.
