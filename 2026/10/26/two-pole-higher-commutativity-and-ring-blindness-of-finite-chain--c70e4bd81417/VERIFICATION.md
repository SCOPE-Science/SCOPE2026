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

The accompanying standalone `verify.py` implements ring multiplication directly for \(\mathbb F_p[t]/(t^m)\) and \(\mathbb Z/p^m\mathbb Z\). It checks all two-element group-product commutation cases at the projected-coordinate level, then enumerates pairwise-commuting ordered tuples without invoking the algebraic counting proof.

Verified configurations: polynomial rings \((p,m,r_{\max})=(2,2,4),(2,3,3),(2,4,2),(3,2,3)\); integer residue rings \((2,2,3),(3,2,3)\). The program computes exact integers and checks them against the claimed full-arity formula after separating the unconstrained central coordinates. Successful execution prints `VERIFY_OK`.

The proof's nonstandard steps (primitive-factorization uniqueness, exact lift count \(q^{2rs}\), parity-sensitive simplification, two-pole inverse reconstruction, derived-subgroup exponent obstruction) are written explicitly in `RESULT.md`. Finite enumeration is not an exhaustive check of all rings, lengths, or arities, and does not establish literature priority. Independent external audit has not been performed.
