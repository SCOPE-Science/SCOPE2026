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
# Verification and scope

The theorem is proved by invariant-subspace and stationary-support analysis in `RESULT.md`, not by exhaustive finite enumeration. The recorded program builds the complex Lindbladian directly from the stated Hamiltonian, positive site dephasers and local absorber, and compares the predicted fixed-space projector against the numerically computed superoperator spectrum. It samples all dephasing subsets for small bipartite sizes and four long-time propagations.

Replay: install `requirements.txt` with pip, then run `python verify.py`. Recorded outcome: `VERIFY_OK rank_one_bipartite_lindblad_cases=168 stationary_kernel=168 long_time_states=4`.

The numerical tests are finite corroboration only; no spectral-gap bounds uniform in system size or rates are proved. The exact absorbing projection, all-subset rank formula, and minimum placement budget are proved in the accompanying analytic text for every stated parameter choice.
