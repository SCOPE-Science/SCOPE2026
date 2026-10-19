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

# Verification of the three-state time-reversal resonance law

Run `python3 verify.py` from a directory containing this file and the standalone checker. The program uses Python's standard-library exact rational arithmetic extended to \(\mathbb Q(\sqrt3)\).

The run completed successfully with 345 exact assertions: row and column stochasticity, nonnegativity, \(P^2=\Pi\) for the sharp and rational matrices, centered nilpotency, the stated singular-value squares, all matrix powers through fifteen for six rational mixture weights, the corresponding even-lag correlations, and strict branch expansion for every nonempty branch.

The proof supplies the complete universal argument, including the sine-phase positivity obstruction and the minimal two-versus-three-state argument. Finite exact assertions corroborate algebraic identities and witnesses; they do not prove the infinite quantifiers or literature priority. The expanding interval realization verifies only correlations of observables constant on the three common Markov cells. All independent scientific audit channels remain unperformed.
