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

Run `python3 checker.py` with Python 3.9 or later and no third-party packages. The expected exact JSON output is `verification_output.json`. The checker constructs and solves an absorbing Markov chain for each finite tested state, tracking whether each neighbor of the designated target has been seen, independently of the theorem's resistance formula. It also tests cyclic inversion and its stability estimate with exact fractions.

The included run passed 801 exact assertions, including 340 independent first-step probability comparisons, at cycle sizes three through six with five positive heterogeneous rational conductance samples per size. It tests constant-resistance symmetry and one inconsistent proposed data vector. It neither constitutes an exhaustive enumeration of all positive real conductances nor replaces the general harmonic proof.

The main analytical steps to inspect are: complement-of-target path equivalence, gambler's-ruin resistance normalization, the two strong-Markov conditional probabilities, the signed cyclic inversion, feasibility sufficiency, and the strict contraction in the stability inequality. The classification excludes zero conductances and assumes known cyclic labels. No independent external mathematical audit has been performed.
