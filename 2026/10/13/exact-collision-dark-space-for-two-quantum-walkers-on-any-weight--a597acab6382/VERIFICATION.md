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

The recurrence argument in `RESULT.md` is the proof of the all-dimensional statement. Numerical tests are supplementary and make no claim of exhaustive enumeration over any continuous parameter class.

Run `python verification/verify.py` after installing packages in `verification/requirements.txt`. The checker uses the exact listed seed to generate 48 finite weighted-path models, with \(2\le n\le7\), complex hopping, real exchange-symmetric diagonal interactions, unequal positive diagonal loss rates, and 144 randomized initial states. It compares the exact Hermitian dark eigenspace dimension with \(n(n-1)/2\), verifies exchange symmetry, and compares long-time conditional survival with antisymmetric initial weight. It also checks the explicit symmetric zero-energy dark vector on the unweighted four-cycle.

The finite time is \(t=50000\), chosen conservatively for numerical relaxation; finite-time decay is not itself the proof of convergence. The theorem does not give a parameter-uniform decay gap. See `verification/output.txt` for a recorded test run. Independent audit: not performed.
