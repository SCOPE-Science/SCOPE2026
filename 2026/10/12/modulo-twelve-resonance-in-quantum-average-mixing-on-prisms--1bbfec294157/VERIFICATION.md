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

# Reproducible verification

The analytical argument in `RESULT.md` is the proof for every integer \(n\ge3\). The packaged `verifier.py` is an independent finite-size corroboration, not an exhaustive computational proof over the infinite family.

Run `python3 verifier.py` with Python 3 and NumPy installed. The program constructs actual adjacency matrices for \(C_n\square K_2\), obtains their spectral projectors from an independent symmetric eigendecomposition, sums entrywise projector squares, evaluates all \(2n\) Fourier eigenvalues, tests stochasticity and positive semidefiniteness, and checks the rank classification for \(3\le n\le24\). It additionally enumerates equal-energy ordered Fourier pairs for \(3\le n\le18\).

The observed output from the packaged source was:

`VERIFY_OK independent_graph_orders=3..24 modes=594 pair_modes=336 matrix_entries=19580 n12_rank=11/24 max_error=1.11e-15`

The numerical projector grouping uses an absolute eigenvalue tolerance of \(10^{-8}\) and equality assertions of \(2\cdot10^{-9}\); those tolerances apply only to the finite numerical tests. The unbounded rank theorem instead uses exact Fourier combinatorics and the algebraic-integer norm argument. Reproducibility is limited by the usual numerical linear algebra environment. No independent audit has yet been performed.
