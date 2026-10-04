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

The claim was checked from the definitions of centroid alignment and maximum translated intersection.

For paired families \(\mathcal A\subset\mathbb R^n\) and \(\mathcal B\subset\mathbb R^d\), the identity
\[
\bigcap_i\bigl((A_i\times B_i)+(x_i,y_i)\bigr)
=
\left(\bigcap_i(A_i+x_i)\right)\times\left(\bigcap_i(B_i+y_i)\right)
\]
is exact. Product Lebesgue measure then factors every overlap volume. The translation variables in the two coordinate blocks are independent, so maximizing the product yields the product of the two maxima. Centroids of Cartesian products factor by Fubini, so the centroid-aligned numerator factors as well.

The passage from concrete families to \(c_{n,m}\) uses epsilon-near-minimizers because the infimum need not be attained. The asymptotic root limit uses Fekete's lemma on the finite numbers \(\log c_{n,m}\); finiteness is guaranteed by the positive published lower bound.

The planar input \(c_{2,m}=4/9\) for \(m\ge2\) and the one-dimensional identity \(c_{1,m}=1\) are taken from the cited 2026 source. Repeated products give the displayed upper bound. No finite numerical experiment, enumeration, or software output is used as evidence for the infinite statement.

The result does not determine the exact constants in dimensions at least three, does not prove sharpness of the product examples, and does not address alignment by rotations or other selectors.
