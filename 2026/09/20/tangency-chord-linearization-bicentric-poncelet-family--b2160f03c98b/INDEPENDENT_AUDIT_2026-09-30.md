# Independent Audit — 2026/09/20/tangency-chord-linearization-bicentric-poncelet-family--b2160f03c98b

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `653d4b6bf1630f714ebc0efdaddbeeaaeffaf8f6`
- Disposition: **PASSED**

## Correctness

**PASS** — The chord-coordinate derivation is consistent. The classical chord-tangent locus equation R^2=r^4(2r^2-p^2)/(r^2-p^2)^2 with p=IP rearranges to p^2=r^2(Delta-3r)/(Delta-r). For perpendicular incircle chords through P, choosing angle alpha gives k^2=4(r^2-p^2 sin^2 alpha) and l^2=4(r^2-p^2 cos^2 alpha), hence their squared lengths traverse exactly the stated line segment and have constant sum 4r^2(Delta+r)/(Delta-r). Solving this sum for Delta gives the radius-recovery formula. Combining the established bicentric area identity K=kl d_1 d_2/(k^2+l^2) with d_1d_2=2r(Delta+r) gives the submitted semiperimeter, area, and contact-area formulas. The two Blundon-Eddy defect factorizations then follow by elementary algebra from the constant-sum relation, including the right-kite and isosceles-tangential-trapezoid equality cases. The square boundary R=sqrt(2)r collapses correctly to k=l=2r.

## Originality

**PASS** — Perpendicular tangency chords, the chord-tangent construction, Fuss' relation, and several area/tangency-chord formulas are classical. Josefsson and later bicentric-quadrilateral papers cover those ingredients, while Tran Quang Hung's 2024/2025-published note was retrieved in full and checked: it generalizes Fuss through opposite-angle bisectors and distance identities but does not contain the squared-chord line segment, radius-recovery formula, fixed contact-area ratio, or the submitted exact defect factorizations. Targeted searches likewise did not locate those formulas. Because they are short consequences once the classical construction is put in the right coordinates, older chord-tangent literature remains a meaningful residual priority risk.

## Scientific value

**PASS** — The result gives a simple linear coordinate model for the entire fixed-circle bicentric Poncelet family and packages several classical inequalities into exact nonnegative defect formulas. Radius recovery and the fixed area ratio are concrete geometric invariants. The advance is structural rather than foundational, but it materially simplifies a classical one-parameter family.

## Sources

- **The Area of a Bicentric Quadrilateral** — Martin Josefsson. https://forumgeom.fau.edu/FG2011volume11/FG201119.pdf — Prior bicentric area and tangency-chord formulas used as acknowledged input.
- **Calculations concerning the tangent lengths and tangency chords of a tangential quadrilateral** — Martin Josefsson. https://forumgeom.fau.edu/FG2010volume10/FG201014.pdf — Classical tangency-chord formulas and characterizations; no checked statement gives the submitted fixed-circle line-segment profile.
- **A new proof of the Blundon-Eddy inequality and some applications** — M. Bencze; M. Dragan. https://amj-math.com/wp-content/uploads/2022/01/AMJ2021-vol8iss2.pdf — Prior Blundon-Eddy bounds and side-based deficit factorizations.
- **A generalisation of Fuss' theorem** — Tran Quang Hung. https://doi.org/10.1017/mag.2024.130 — Authorized full text checked after open-access attempts; its generalized Fuss identity does not state the audited tangency-chord profile or defect formulas.

## Limitations

- Only convex Euclidean bicentric quadrilaterals are treated.
- The squared-chord segment is an image of the Poncelet family, not asserted to be a one-to-one parametrization of labeled quadrilaterals.
- No analogous result is claimed for ex-bicentric quadrilaterals or higher Poncelet polygons.
- Older chord-tangent sources may contain equivalent short consequences under different notation.

## Independent checks

```json
{
  "fuss_locus_rearrangement_checked": true,
  "chord_length_line_segment_checked": true,
  "radius_recovery_algebra_checked": true,
  "area_and_semiperimeter_formulas_checked": true,
  "blundon_eddy_defect_factorizations_checked": true,
  "square_boundary_case_checked": true,
  "open_access_first": true,
  "oxford_used": true,
  "oxford_job_id": "7a32615185b5712bf7d0642948d31785",
  "oxford_status": "complete",
  "oxford_pages_checked": "1-6 of 6"
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access/preprint sources were checked before institutional retrieval. Any inaccessible comparison is explicitly identified and is not claimed read.
