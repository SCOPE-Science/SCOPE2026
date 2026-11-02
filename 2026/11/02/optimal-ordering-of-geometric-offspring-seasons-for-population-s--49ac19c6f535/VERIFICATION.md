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

# Computational and analytical verification

The all-parameter proof is in `RESULT.md`; it establishes the exact composition and adjacent-interchange identity and does not rely on experiments for an infinite claim.

Run `python3 CHECK.py` with Python 3 and the standard library. The deterministic test program, with exact `fractions.Fraction` arithmetic, completed 152,229 assertions without failures. It checks 150 randomly sampled admissible rational season multisets across sizes two to six, their complete distinct permutation sets, PGF substitution, commutator equality/sign, terminal survival, stop-loss ordering and periodic survival. It also checks explicit examples, including one in which the mean-ranked order is strictly suboptimal.

The computational suite does not enumerate all real-valued parameters or prove historical novelty; those issues are addressed by the analytical proof and the provisional literature comparison respectively. External independent verification has not been performed.
