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

The proof's primary certificate is algebraic: for every one of the 16 spin configurations, the backward generator satisfies the four stated moment identities and the heat Poisson corrector equation. The finite-state tilted-generator eigenvalue identity gives the long-time mean and variance rates. No extrapolation from numerical samples is used.

Run `python verify_heat.py` with Python 3 and SymPy from `requirements.txt`. The program independently constructs every allowed spin flip, tests the symbolic identities for generic parameters, and compares the two predicted cumulants against exact rational full 16-state Markov-generator calculations at eight parameter pairs, including equilibrium, unequal temperatures, and an infinite-temperature bath. It solves the stationary equation and the first tilted-eigenvector response anew in each case. All checks passed in the delivered environment.

The script checks the current and second cumulant, not a full counting distribution or the uniqueness of the proposed result in the literature. The analytic proof gives the parameter-wide theorem in the finite irreducible domain; the rational test pairs are additional corroboration. No independent scientific audit has been performed.
