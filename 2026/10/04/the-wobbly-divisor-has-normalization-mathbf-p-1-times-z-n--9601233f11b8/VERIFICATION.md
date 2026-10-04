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

The proof has two logically distinct parts. The uniform statement for every \(n\ge3\) is proved symbolically: multiple roots bound the \(\mathbf P^1\)-coordinate of a fiber; the remaining coordinates give finite fibers; Lagrange interpolation produces a nonempty unique-double-root open set and hence generic degree one; and a cubic interpolation contradiction produces a nontrivial sign-flip fiber at every distinguished branch value.

The bundled `verify.py` does not replace that proof. It performs exact rational checks in the smallest case \(n=3\): for six distinct sample parameters it computes the kernel of the four Vandermonde moment rows, confirms for every coordinate \(m\) that some kernel vector has nonzero \(m\)-th coordinate, and rechecks the complete-intersection degree and genus. The saved output must end in `VERIFY_OK`.

Unproved limits: the conductor, number and geometry of irreducible components of the singular locus, and overlap with the inaccessible full text of the 2026 thesis are not determined here.
