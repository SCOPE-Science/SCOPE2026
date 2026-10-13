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

The proof has two literature inputs and one finite verification component.

Yamamoto's arXiv text was checked for the facts that the Fraïssé limit of finite nontrivial Heyting algebras exists, is locally finite, and is ultrahomogeneous. The same text identifies realized quantifier-free types with finite generated subalgebras and uses this explicitly in the automorphism-group analysis.

The one-generated classification was checked against Citkin's statements that every finite one-generated Heyting algebra has one of the cardinalities \(n\ge2\) with a unique isomorphism type \(Z_n\), and against the explicit generator analysis: \(Z_2\), \(Z_4\), and \(Z_5\) have two generators; the two generators are automorphic for \(Z_4\) and \(Z_5\) but not for \(Z_2\); all other finite one-generated algebras have a unique generator.

The script `verify_unary_orbits.py` reconstructs the standard finite \(Z_n\) recursively and checks the resulting Heyting tables, generated-subalgebra sizes, generator counts through \(n=20\), and generator-orbit counts under brute-force automorphism enumeration through \(n=8\). It returns `VERIFY_OK 64 exact assertions`.

The finite computation does not establish the classification for arbitrary \(n\); the all-\(n\) statement rests on the cited algebraic classification.
