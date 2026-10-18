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

# Reproducible verification

Use Python 3 and run `python3 verify.py` alongside `RESULT.md`. No optional packages or network access are required.

The checker reconstructs all 12 directed-edge points over integer polynomials, enumerates exactly 495 distinct index quadruples, expands each normalized 3-by-3 determinant, separates the sign by rational evaluation at a fixed interior point and verifies the exhaustive ten-row polynomial histogram. Its expected totals are 495, ten symbolic volume classes, and 24 vertex-supported maximizers for \(0<t<1/2\).

It also checks \(\frac{M(P_{1/3})}{\operatorname{vol}_3(P_{1/3})}=6/23\), the octahedral endpoint fraction \(1/4\), the exact derivative numerator \(24t^4-32t^3+3t^2+12t-4\), and the unique critical root's rational bisection bracket, reporting its decimal approximation.

Independent universal proof steps appear in `RESULT.md`: affine invariance; the cut-corner volume identity; reduction of an arbitrary contained tetrahedron to vertex points; strict positivity of the eight competitor gap polynomials; an explicit equality witness; and strict increase of the derivative numerator. Finite enumeration is exact for the finite set but is not a proof of continuous optimality without those analytic reductions. No independent external assessment is claimed.
