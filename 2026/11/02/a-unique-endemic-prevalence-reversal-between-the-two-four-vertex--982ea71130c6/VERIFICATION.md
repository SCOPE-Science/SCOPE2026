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

# Reproducibility and verification

Run `python checker.py` in this directory with Python 3 and SymPy installed. The included script reconstructs stationary equations for the two trees, reduces their solutions, verifies the exact difference-factorization and the large-infection-rate coefficient symbolically, and independently iterates the four-dimensional fixed-point equations. It passed 60,415 assertions on its delivered version. Numeric tests do not certify infinitely many parameters; the proof in `RESULT.md` handles all \(\tau>0\).

At zero and positive epidemic thresholds, values and equality cases are established analytically, not inferred by numerical solvers. The classification assumes positive, identical recovery and per-edge infection rates, four vertices, connected undirected three-edge trees, and deterministic NIMFA equilibrium. It does not apply to the absorbing finite Markov SIS stationary distribution.

The closest 2008 and 2011 open-access sources were inspected at their governing and comparative sections; the 2012 NIMFA versus heterogeneous-mean-field paper was not available in full after bounded open-access and institutional-access attempts, so residual originality risk remains. This file records mathematical checks only; there has been no independent audit.
