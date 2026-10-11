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

# Reproducibility

Run `python verify.py` with SymPy and mpmath available. The checker verifies the exact profile identity and polynomial derivative factorization, the critical-interval endpoint algebra, five two-atom moments reconstructed at 75-digit precision, and 16,800 randomized finite-dimensional Birkhoff-orthogonal ratios. The first output line is:

`VERIFY_OK symbolic_identities=3 root_bracket=1 two_atom_moments=5 random_pair_ratios=16800`

The analytical proof of universal sharpness uses Cauchy–Schwarz equality and a two-point construction in any pair of disjoint finite-measure sets. Symbolic identities and finite numerical checks cannot replace the strict-concavity argument, root uniqueness, or classification of equality in arbitrary real \(L_4\). The 1970 defining reference was unavailable in full text, leaving an originality comparison risk. No independent audit has been performed.
