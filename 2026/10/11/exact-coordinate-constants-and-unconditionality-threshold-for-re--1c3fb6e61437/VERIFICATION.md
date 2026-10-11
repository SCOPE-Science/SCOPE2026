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

# Verification record

The complete proof is analytic and uses: (i) exact edge-flow duality on a finite real tree, including the two terminal leaf contributions; (ii) generation of the finite free-space unit ball by normalized molecules; (iii) exact sign-flip and selected-run expressions; (iv) the increasing finite-section passage; and (v) uniform-tail/block-decay equivalence.

The accompanying file `verify_ultrametric.py` may be executed with `python verify_ultrametric.py`. It uses the Python standard library for exact rational tree norms and exhaustive coefficient selectors, plus SciPy's HiGHS-backed `linprog` for an independent dual linear-program check. The recorded successful output was `COMB_ULTRAMETRIC_VERIFIED cases 15 LP 60`: fifteen randomly drawn strictly decreasing rational distance sequences at dimensions one through five were each exhaustively checked for every sign and binary selector; sixty additional arbitrary signed mass patterns were cross-checked by independent dual linear programming.

These are finite checks, not exhaustive over all real distance sequences and not infinite-dimensional certificates. The proof itself, rather than the reported checks, establishes all quantifiers. If the optional SciPy dependency is missing, the numerical LP portion cannot be reproduced without installing a compatible release.
