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

The Hamiltonian was independently reduced to its two invariant \(2\times2\) blocks. Their Gibbs exponentials give the two \(X\)-state concurrence candidates used in the proof.

`verify_dm_window.py` checks the closed-form endpoints against those candidates for the source benchmark and a deterministic grid of additional ferromagnetic couplings and temperatures. It verifies zero concurrence throughout the predicted interval on a dense sample, positive concurrence immediately outside whenever the corresponding entangled branch exists, strict placement of \(D_c\) inside the interval, and low-temperature collapse.

The numerical replay is supplementary. The all-parameter claim is proved analytically in `RESULT.md`.

No independent audit has been performed.
