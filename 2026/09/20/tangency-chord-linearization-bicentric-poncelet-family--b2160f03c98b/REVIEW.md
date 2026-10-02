# Independent audit review — 2026-10-01

## Final claim

For every convex Euclidean bicentric quadrilateral, the two squared tangency-chord lengths have the stated radius-only constant sum and fill the stated complete line segment for fixed inradius and circumradius; the resulting formulas recover the circumradius, give a fixed outer/contact area ratio, and factor both Blundon–Eddy semiperimeter defects exactly.

## Correctness — PASS

The classical perpendicular-chord construction was checked against Stastna’s full locus derivation: perpendicular incircle chords and endpoint tangents generate the bicentric family, and the locus computation gives the fixed circumcircle. With \(p=IP\), elementary chord geometry gives \(k^2=4(r^2-p^2\sin^2\alpha)\) and \(l^2=4(r^2-p^2\cos^2\alpha)\); eliminating \(p\) yields the claimed constant sum and full segment. The published bicentric identities \(K=kl\,d_1d_2/(k^2+l^2)\) and \(d_1d_2=2r(\Delta+r)\), followed by \(K=rs\), give the area and semiperimeter formulas; the two defect identities are direct algebra. The inspected symbolic artifact independently checks the algebra, but the proof does not rely on its output.

## Originality — PASS

The inspected classical and modern sources cover the perpendicular-chord construction, Fuss geometry, the bicentric area formula, and the Blundon–Eddy inequalities, but the searches did not locate the combined radius-only squared-chord segment, radius recovery, fixed contact-area ratio, or the two contact-chord defect factorizations. The 2024 Hung note is a plausible nearby source but its full theorem text was not available; that remains an explicit priority risk rather than evidence of noncoverage.

## Value — PASS

The result gives a compact exact coordinate model for a classical Poncelet family and turns two sharp inequalities into geometric nonnegative defects with equality cases. The radius recovery and fixed area ratio are natural invariants of a standard geometric object, so this is more than a routine renaming or finite calculation.

## Source inspections

- **Fuss’ Problem of the Chord-Tangent Quadrilateral** (https://math.fce.vutbr.cz/~pribyl/workshop_2005/prispevky/Stastna.pdf): FOUNDATIONAL_PRIOR_ART. It proves perpendicularity, the converse tangent construction, and the circle-locus/Fuss relation, but does not state the audited squared-chord line segment or contact-chord defect formulas.
- **The Area of a Bicentric Quadrilateral** (Forum Geometricorum 11 (2011), 155–164): PARTIAL_COVERAGE. It supplies \(K=klpq/(k^2+l^2)\), an ingredient of the audited semiperimeter formula.
- **A generalisation of Fuss’ theorem** (https://doi.org/10.1017/mag.2024.130): INACCESSIBLE_PLAUSIBLE_SOURCE. The title and references make it relevant, but unavailable full text cannot establish either coverage or noncoverage.

## Residual risks

- Hung (2024) and older chord-tangent literature may contain short equivalent consequences under different notation; their unavailable portions were not treated as noncoverage evidence.
