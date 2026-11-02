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

# Verification

Run `python verify.py` with NumPy and SciPy installed. The program constructs all graph vertices and weighted stochastic matrices directly, checks exact rational budget and hold identities, compares full eigenspectra with tensor subset predictions, and independently solves finite-size linear minimax programs. It also tests feasible non-orbit-constant perturbations. Replayed locally: `PASS 362 assertion groups on 19 product instances; full spectra, exact row budgets, LPs and perturbed feasible chains`.

The proof in `RESULT.md`, not this finite run, establishes optimality and uniqueness for every allowed product dimension and alphabet profile. These tests cannot exclude unseen prior work, establish independent audit, or verify arbitrary infinite graph instances.
