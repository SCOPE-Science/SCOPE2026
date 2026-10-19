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

# Exact rational verification

Run `python3 verify.py` in the same directory as the research documents, using Python 3 standard library only. The checker constructs the combinatorial Laplacian of the eight-vertex path, forms the fourth-order Gauss–Legendre rational map, and uses 15 exact rational evaluations to interpolate a degree-at-most-14 numerator for every entry. Crucially, it independently verifies all 64 identities \(Q(h)P(h)=4D(h)M(h)\) **coefficient-by-coefficient**, so the inferred polynomial identity is valid for every real \(h\), not only the interpolation points.

It verifies \(P_{0,7}=9h^7F\), \(P_{3,4}=-9hG\), the sign-change pattern and root brackets for \(F,G\), and the coefficient-based positivity certificates for each of the other 60 matrix entries. There are 40 all-nonnegative coefficient cases and 20 single-upper-root cases, all strictly positive through \(h=9/2\). It also checks rational sample entries on both negative phases and within the positive interval. The command must terminate with:

`VERIFY_OK exact_polynomial_identities=64 sign_pattern_entries=60 all_positive=40 single_upper_root=20 lower_bracket=(3/10,1/3) upper_bracket=(4,9/2)`

The general all-dimension small-step statement follows analytically from path-walk shortest distances and Padé series coefficients; finitely many numerical evaluations alone would not prove it. Root decimals are not used for sign conclusions. The checker is a reproducible self-review, **not an independent mathematical audit**.
