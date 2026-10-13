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

The analytic argument resolves the total momentum of the two-particle cycle and isolates its exceptional zero-energy sector. It does not require finite-state enumeration. The accompanying `verify.py` constructs an independently diagonalized Hamiltonian for cycle orders \(3\) through \(10\) and compares detector-visible ranks and all ordered position-state probabilities with the theorem; it also tests 328 normalized symmetric distinct-site states and 24 finite-time nonuniform-loss evolutions. Run: `python verify.py`, with versions specified in `requirements.txt`.

Observed output: `VERIFY_OK spectral_dimensions=8 exact_sitewise=380 bosonic_states=328 lossy_evolutions=24`.

The verification does not constitute an exhaustive numerical proof for all cycle orders, does not derive a convergence rate uniform over the loss strengths, and does not independently certify priority relative to all publications.
