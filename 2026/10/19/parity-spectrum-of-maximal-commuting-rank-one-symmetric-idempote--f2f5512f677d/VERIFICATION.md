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

Run `python verify.py` using Python 3 without external packages. The script uses exact arithmetic in finite fields defined by irreducible polynomials: \(x+1\), \(x^2+x+1\), and \(x^3+x+1\), for orders \(2,4,8\). It constructs all vectors with coordinate sum one, checks their norm and the literal transpose-symmetric matrix products (for the specified small cases), and enumerates every unordered clique and inclusion-maximal clique recursively.

Configurations: \((q,n)=(2,2),(2,3),(2,4),(2,5),(2,6),(4,2),(4,3),(4,4),(8,2),(8,3)\). Each calculated clique coefficient and each maximal-clique count is compared with the exact order formulas, with assertion failure on any disagreement. The displayed terminal status is `VERIFY_OK_SYMMETRIC_IDEMPOTENT_PARITY_CLIQUES`.

Exhaustion applies **only** to the listed finite cases, not to all characteristic-two fields or arbitrary dimensions; the unrestricted proof is mathematical, using isometry groups and the canonical vector. The numerical verifier assumes the source's basis and graph definitions and is not independent scholarly validation.
