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

# Independent reproducibility information

The standalone `verify.py` uses only the Python standard library and may be invoked as `python3 verify.py`. It recomputes all three expected payoffs from 9 ordered co-player pairs, compares them with the closed payoff differences, builds the Jacobian at hypothetical interior payoff equality, and checks the trace/determinant polynomial identities over exact rational parameter and interior-frequency grids. It separately verifies the factorized boundary polynomial and signed edge eigenvalues for the exact rational parameter witness.

The executed check reported: `PASS: 1344 exact rational payoff and Jacobian checks;` followed by `PASS: 101 exact polynomial identity checks; exact three-attractor witness.` The universal sign inequality and equilibrium-count argument are proved in `RESULT.md`; finite arithmetic testing alone is not used to infer them.

No proof of global convergence or absence of periodic orbits is attempted. No independent mathematical audit has been performed.
