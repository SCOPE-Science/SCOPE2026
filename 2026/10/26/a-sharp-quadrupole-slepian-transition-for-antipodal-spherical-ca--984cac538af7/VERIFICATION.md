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

# Reproduction and scope

The proof needs no machine computations. Its central ingredients are the conditional beta distribution of one squared spherical coordinate, the exact second and fourth moments, and two displayed derivatives integrated between the cap cutoff and one. Those steps are explicitly shown in `RESULT.md` and apply to all integers of dimension at least three, not merely enumerated cases.

For independent numerical sanity checks, execute `python check_quadrupole.py` with Python 3 and SciPy. This checks each eigenvalue integral and both closed-form spectral gaps at multiple cutoffs. Finite numerical checks do not establish identities on infinite parameter ranges, and no code-based or third-party certification is claimed. The equality case follows analytically from the gap factors, not an empirical tolerance.
