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

# Verification and limits

The derivation uses normalized barycentric coordinates and exact Euclidean orthogonal projection. The decisive infinite-dimensional-range argument is a common strictly contracting return itinerary: for every integer dimension at least three, the linear tangential parts of the projections onto all different facets have operator norm strictly less than one when multiplied, since equality would require a nonzero vector tangent to all facet hyperplanes. This is a mathematical argument and does not rely on finite enumeration.

The included `verify.py` runs with `python3 verify.py` and requires no third-party dependencies. Exact rational checks enumerate all periodic phases for dimensions three through six (respectively 24, 120, 720 and 5040 labeled phases), test rank cycles and selected off-orbit points and tie-to-fixed cases, and reconstruct the tetrahedral four-step return matrix with exact trace and determinant. The program prints `CHECK_OK` upon success.

An invariant-probability classification additionally invokes the standard Poincaré recurrence theorem for invariant Borel probabilities; no unproved classification or simulation replaces this theorem. Nothing here certifies priority against literature that was not inspected or provides an independent scientific audit.
