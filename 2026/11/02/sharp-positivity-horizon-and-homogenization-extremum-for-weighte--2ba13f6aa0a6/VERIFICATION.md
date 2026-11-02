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

## Analytical checks

Verified exact Schur complements, diagonal ordering, root uniqueness, sharp Jensen equality, and high-contrast quadratic scaling.

## Computational corroboration

Run `python3 verify_weighted_star_cn.py` with NumPy, SciPy and SymPy to check 525 weighted examples at six timesteps each, and three exact-rational matrix resolvent identities. The random tests do not establish statements for infinitely many graph weights.

## Scope and limitations

Markov-step entrywise nonnegativity only; no convergence/error bound. No independent mathematical audit has been performed.
