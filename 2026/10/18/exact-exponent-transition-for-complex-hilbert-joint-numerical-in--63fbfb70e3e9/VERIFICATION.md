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

The unrestricted theorem is proved in `RESULT.md` by deterministic inequalities. To reproduce finite stress tests run `python3 verify.py` with Python 3; no third-party packages are required.

Successful local check: `VERIFY_OK assertions=3283 exact_sign_and_polarization=True universal_proof_in_RESULT_required=True`.

The script checks sign-second-moment identities exactly on Gaussian-integer test vectors, the four-phase polarization identity for non-Hermitian complex matrices, rational exponent cancellations, the exact rank-one maximizing configurations across tuple lengths and exponents, and additional sampled unit vectors. The second-moment and polarization steps are separately proved for all finite tuples in `RESULT.md`; the tests cannot establish their universal scope. The script does not test the entire space of bounded operators, finite-dimensional or otherwise. No independent validation has been performed.
