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

# Verification and scope

Execute `python check.py` with Python 3, NumPy and SymPy. The script is standalone and requires no external files. At package preparation, it printed `PASS 54319 assertion checks`. It checks polynomial pencil identities over exact rationals, the radical optimum over hundreds of parameter triples, spectral roots, nonnegative and positive price-tie boundaries, and thousands of sampled feasible designs. Floating-point comparison tolerances account for the square-root sensitivity of exactly repeated eigenvalues.

The proof in `RESULT.md` supplies the all-positive-rate and all-positive-price quantifiers. The experiments are reproducibility checks, not exhaustive real-parameter enumeration. Defective roots may cause polynomial transient factors; only the exponential asymptotic exponent is optimized. The nonnegative boundary point for two tied cheapest prices is not an irreducible chain. No external independent validation has been performed.
