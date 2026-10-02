---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For every convex tangential quadrilateral, Ivanova's inequality admits the sharp stability refinement \(s-4r\ge[3(3\sqrt3-4)/\pi^2]r\sum_i(A_i-\pi/2)^2\), equivalently for \(K-4r^2\); equality for a proper quadrilateral occurs only at the square, and the constant is approached by the stated degenerating angle family.

## Correctness — PASS

Writing \(x_i=(\pi-A_i)/2\) gives \(s/r=\sum_i\tan x_i\), \(\sum x_i=\pi\), and converts the theorem to a sharp four-variable Jensen refinement. Finite boundary points reduce to a three-variable tangent-line inequality, while approach to \(\pi/2\) has infinite cost. At an interior constrained local minimum, strict convexity of the stationarity function leaves only the regular point or a pattern \((a,b,b,b)\). The explicit one-variable rational reduction proves every nonregular interior critical value is positive. The boundary family reaches the claimed constant, so the constant and equality statement are sharp.

**Checked sources.** Assigned RESULT.md at the frozen source tree; Josefsson 2023 square-characterization compilation; Josefsson--Dalcín 2025 square characterizations; Gui--Hu--Li, arXiv:2607.28768, tangential-polygon quantitative Pólya--Szegő theorem

**Residual risks.** No correctness defect was found.

## Originality — PASS

The classical tangential-quadrilateral literature gives \(s\ge4r\) and equality at the square. The recent tangential-polygon Pólya--Szegő theorem includes an angular asymmetry deficit for torsional rigidity, but it is a different functional and does not supply the sharp semiperimeter/area angle-variance constant. Searches did not locate the audited best constant or degenerating equality profile.

### Equivalent formulations

Equivalent semiperimeter, area, and tangent-Jensen formulations were compared.

### Broader coverage

The broader polygon theorem does not dominate the sharp four-angle Jensen constant here.

### Exact database or table

A finite table is inapplicable because the result is a sharp continuum inequality.

### Claim versus prior implication

The qualitative inequality does not mechanically imply the best quadratic coefficient.

**Checked sources.** Josefsson 2023; Josefsson--Dalcín 2025; arXiv:2607.28768; published mathematical corpus search

**Residual risks.** An equivalent sharp refinement of the tangent Jensen inequality could exist in older trigonometric-inequality literature under unrelated terminology.

## Value — PASS

This is a globally sharp quantitative strengthening of a classical geometric inequality, with an explicit optimal constant, equality classification, and a geometrically meaningful degenerating extremal family.

**Checked sources.** Ivanova/Josefsson qualitative inequality; recent quantitative tangential-polygon work

**Residual risks.** The sharp constant is specific to four angles and the chosen Euclidean variance.

## Limitations

- Only Euclidean convex tangential quadrilaterals are covered.
- Stability is measured by squared interior-angle variance.
- The best constant is approached at a degenerate boundary and is not attained by a proper nonsquare quadrilateral.
- No best-constant theorem for general tangential polygons is claimed.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
