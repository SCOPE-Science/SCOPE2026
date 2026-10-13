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

The analytical proof relies on two exact Hamiltonian moment identities, the equality case of Cauchy–Schwarz in the reversible weighted Hilbert space, coordinate comparison, and an explicit invariant two-state reduction. They establish the theorem for every finite irreducible reversible Markov matrix with at least two states.

Run `python3 verify.py` in the package directory. This standard-library program enumerates connected small symmetric conductance networks, including zero/nonzero edges and loops, using exact `fractions.Fraction` arithmetic. Each marked vertex is checked against the exact second-moment identity, the equivalent constant-entrance criterion, and all coordinates of the invariant-subspace identity when satisfied. It also checks a weighted nonregular-base cone and fixed-topology triangular imbalance/balance examples.

Expected output: `VERIFY_OK exact_markov_moments_checks=41592 condition_true=870 weighted_cone=true triangle_balance=true`.

The finite enumerations are not a proof of all-order correctness, nor is there independent validation. The formulas are exact and their restrictions are stated in the finding.
