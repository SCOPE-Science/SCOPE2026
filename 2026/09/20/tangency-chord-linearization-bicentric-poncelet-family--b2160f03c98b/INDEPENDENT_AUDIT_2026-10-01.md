# Independent scientific audit — 2026-10-01

**Disposition:** passed

**Final claim:** For every convex Euclidean bicentric quadrilateral, the two squared tangency-chord lengths have the stated radius-only constant sum and fill the stated complete line segment for fixed inradius and circumradius; the resulting formulas recover the circumradius, give a fixed outer/contact area ratio, and factor both Blundon–Eddy semiperimeter defects exactly.

## C — PASS

The classical perpendicular-chord construction was checked against Stastna’s full locus derivation: perpendicular incircle chords and endpoint tangents generate the bicentric family, and the locus computation gives the fixed circumcircle. With \(p=IP\), elementary chord geometry gives \(k^2=4(r^2-p^2\sin^2\alpha)\) and \(l^2=4(r^2-p^2\cos^2\alpha)\); eliminating \(p\) yields the claimed constant sum and full segment. The published bicentric identities \(K=kl\,d_1d_2/(k^2+l^2)\) and \(d_1d_2=2r(\Delta+r)\), followed by \(K=rs\), give the area and semiperimeter formulas; the two defect identities are direct algebra. The inspected symbolic artifact independently checks the algebra, but the proof does not rely on its output.

## O — PASS

The inspected classical and modern sources cover the perpendicular-chord construction, Fuss geometry, the bicentric area formula, and the Blundon–Eddy inequalities, but the searches did not locate the combined radius-only squared-chord segment, radius recovery, fixed contact-area ratio, or the two contact-chord defect factorizations. The 2024 Hung note is a plausible nearby source but its full theorem text was not available; that remains an explicit priority risk rather than evidence of noncoverage.

### Equivalent formulations

**Searches:** Published SCOPE semantic search: bicentric tangency chords fixed radii squared-sum segment Blundon–Eddy defects; Literature search: bicentric quadrilateral tangency chords contact quadrilateral fixed inradius circumradius

**Evidence:** Stastna (2005) proves the perpendicular-chord construction and its circle locus, but does not state the audited squared-chord segment or defect identities. Accessible bicentric/tangential formula sources state perpendicularity and the area formula \(K=klpq/(k^2+l^2)\), not the audited package of formulas.

**Reasoning:** The located prior formulations supply ingredients, not a theorem equivalent to the final claim.
### Broader coverage

**Searches:** Tran Quang Hung, A generalisation of Fuss’ theorem, DOI 10.1017/mag.2024.130; Josefsson 2010/2011 tangency-chord and area formulas; Bencze–Dragan 2021 Blundon–Eddy inequality

**Evidence:** The accessible classical locus result concerns existence/Fuss geometry; Josefsson supplies component formulas; Bencze–Dragan give the semiperimeter bounds with different defect variables.

**Reasoning:** No inspected source implies all of the squared-chord image, recovery, area-ratio, and contact-chord defect statements.
### Exact database or table

**Searches:** Published SCOPE search for tangency-chord linearization aliases; Exact web searches for "k^2+l^2" with bicentric tangency chords and Blundon–Eddy

**Evidence:** No distinct published SCOPE theorem or exact tabulated formula was located that contains the audited statement.

**Reasoning:** This is a symbolic geometric theorem rather than a database lookup; exact-formula searches are relevant but not by themselves novelty proof.
### Claim versus prior implication

**Searches:** Stastna 2005 full PDF locus proof; Josefsson 2011 bicentric area formula; Bencze–Dragan 2021 semiperimeter bounds

**Evidence:** Those results imply some ingredients, but the passage from fixed perpendicular chords to the full squared-length segment and the two exact contact-chord deficit factorizations requires the additional elimination carried out in the record.

**Reasoning:** The audited final theorem is not a stated corollary of any single inspected stronger theorem, although it is built from classical ingredients.

## V — PASS

The result gives a compact exact coordinate model for a classical Poncelet family and turns two sharp inequalities into geometric nonnegative defects with equality cases. The radius recovery and fixed area ratio are natural invariants of a standard geometric object, so this is more than a routine renaming or finite calculation.

## Source inspections

- **Fuss’ Problem of the Chord-Tangent Quadrilateral** — https://math.fce.vutbr.cz/~pribyl/workshop_2005/prispevky/Stastna.pdf. Trigger: Primary exposition of the exact perpendicular-chord construction and locus used in the proof Material read: Complete four-page PDF, including the converse construction and the locus derivation on pp. 2–3. Method: Open full PDF text and page image inspection Assessment: FOUNDATIONAL_PRIOR_ART. Evidence: It proves perpendicularity, the converse tangent construction, and the circle-locus/Fuss relation, but does not state the audited squared-chord line segment or contact-chord defect formulas.
- **The Area of a Bicentric Quadrilateral** — Forum Geometricorum 11 (2011), 155–164. Trigger: Source of the bicentric area identity used in the proof Material read: Accessible formula-level text for the bicentric area identity involving tangency chords and outer diagonals. Method: Public full-text/archive formula inspection Assessment: PARTIAL_COVERAGE. Evidence: It supplies \(K=klpq/(k^2+l^2)\), an ingredient of the audited semiperimeter formula.
- **A generalisation of Fuss’ theorem** — https://doi.org/10.1017/mag.2024.130. Trigger: Recent title directly adjacent to the same classical construction Material read: Abstract/preview and references only; full theorem text was not available in the lawful public route. Method: Publisher preview Assessment: INACCESSIBLE_PLAUSIBLE_SOURCE. Evidence: The title and references make it relevant, but unavailable full text cannot establish either coverage or noncoverage.

## Residual risks

- Hung (2024) and older chord-tangent literature may contain short equivalent consequences under different notation; their unavailable portions were not treated as noncoverage evidence.

## Limitations

- Only convex Euclidean bicentric quadrilaterals are covered.
- The squared-chord segment is an image profile, not an injective parametrization.
- Older chord-tangent literature, especially the unavailable full Hung (2024) note, remains a priority risk.
