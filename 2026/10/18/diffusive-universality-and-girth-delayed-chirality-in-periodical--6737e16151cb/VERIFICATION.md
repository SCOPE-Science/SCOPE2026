---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification

The proof in `RESULT.md` establishes the one-step winding-tail estimate, telescopes it for the full transition law, and proves the scaling limit via Fourier inversion with summable domination. These analytic arguments, not any finite run, prove the uniform comparison and the heat profile.

The original `verify.py` uses NumPy and SciPy (see `requirements.txt`). From the extracted source package its replay command is `python verify.py`. It constructs the finite Hamiltonian and matrix exponential directly, checks stochasticity and translation invariance, and compares the Bessel estimates and selected diffusive-time distances against numerical circle heat-kernel integrals. Its recorded output `VERIFY_OK 702 finite identities and mixing comparisons` is for the original checker as a whole, including ancillary parity tests not part of the present theorem. It is not a fresh rerun or a count of narrowed-claim-only checks.

The numerical comparisons are finite floating-point checks and do not certify the limit, all fluxes or all sizes. No experimental or formal certification is claimed.
