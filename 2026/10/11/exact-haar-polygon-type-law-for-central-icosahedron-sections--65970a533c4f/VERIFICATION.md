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

# Verification of the exact central-icosahedron section law

Run `python3 verify_icosahedron.py` from the extracted file set. This requires Python 3.9 or newer and the standard library only.

The script enumerates all 64 possible vertex-axis sign masks and all 30 oriented intersections of pairs of six great circles using exact integer-pair arithmetic for \(\mathbb Z[\sqrt5]\). It verifies that no triple intersections occur, the icosahedron has 30 positive-dot-product edges of degree five, that exactly 20 valid triangular masks have 12 crossed edges, and that exactly 12 valid pentagonal masks have 10 crossed edges. It checks the appropriate interior angles and confirms that the 32 chambers cover the sphere by the spherical excess identity. First output line: `EXACT_CHAMBER_ENUMERATION_OK`.

The probability is established mathematically by uniform spherical separation of each of 30 edges and by the proven two-point distribution support; checking 64 masks is exhaustive after a proof that every chamber corner is a pair-great-circle intersection. The numerical floating-point comparisons of spherical area and expectation in the script are supplementary and are not substitutes for the exact algebraic and analytic proof in RESULT.md.

Non-generic normals lie on a finite union of great circles and have Haar measure zero. The result neither classifies their potentially degenerate sections nor treats offset planes. Overlap with older unindexed formulations remains a literature limitation.
