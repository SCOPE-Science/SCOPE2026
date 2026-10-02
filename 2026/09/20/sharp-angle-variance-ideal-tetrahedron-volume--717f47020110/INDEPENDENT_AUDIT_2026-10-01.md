---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For an ideal hyperbolic tetrahedron with squared dihedral-angle deviation \(Q\) from \((\pi/3,\pi/3,\pi/3)\), the exact maximal volume is \(2\Lambda(\pi/6+\sqrt{Q/6})\), attained only by the indicated isosceles branch; consequently \(v_3-V\ge 3v_3Q/(2\pi^2)\), with the constant globally sharp.

## Correctness — PASS

At fixed \(Q\), boundary angle triples have zero volume while the displayed isosceles triple is interior with positive volume. Lagrange multipliers give three roots of one equation whose left side is strictly convex, forcing two angles to agree. The isosceles parametrization reduces the two stationary branches to \(s=\pi/6\pm\sqrt{Q/6}\); the Lobachevsky duplication identity gives volume \(2\Lambda(s)\), and a direct derivative comparison selects the plus branch. The deficit ratio reduces to \([\Lambda(\pi/6)-\Lambda(\pi/6+r)]/r^2\); decreasing curvature proves this ratio decreases to the boundary value, yielding the global best constant and its degenerating sharpness family.

**Checked sources.** Assigned RESULT.md at the frozen source tree; Milnor 1982 standard Lobachevsky volume formula; Thurston's hyperbolic-geometry notes; Haagerup--Munkholm 1981 maximal-volume simplex theorem; Luo 2007 angle-structure variational literature

**Residual risks.** No correctness defect was found.

## Originality — PASS

Classical sources prove the unconstrained maximality of the regular ideal tetrahedron and develop strict concavity/angle-structure volume theory, but the literature and published-result searches performed for this audit did not locate the exact fixed-variance envelope, its unique isosceles equality family, or the globally best quadratic coefficient.

### Equivalent formulations

Equivalent formulations as a fixed Euclidean angle-sphere optimization, a sharp deficit profile, and a quadratic stability inequality were compared.

### Broader coverage

None of the inspected theorem descriptions fixes the squared angle variance and determines the exact constrained profile, so they do not dominate the claim.

### Exact database or table

A finite database/table is inapplicable because the theorem is an analytic continuum optimization.

### Claim versus prior implication

The prior maximum theorem does not mechanically imply the full final claim.

**Checked sources.** Milnor 1982; Haagerup--Munkholm 1981; Luo 2007; published mathematical corpus search

**Residual risks.** Because the proof reduces to a sharp special-function inequality, an older equivalent inequality under unrelated terminology remains a residual risk.

## Value — PASS

The result turns qualitative uniqueness of the regular maximizer into an exact global stability profile with a best constant and equality geometry. That is a natural quantitative invariant of the ideal-tetrahedron moduli simplex.

**Checked sources.** classical regular ideal-tetrahedron maximum; angle-structure variational literature

**Residual risks.** The theorem is three-dimensional and tied to this Euclidean angle-variance coordinate.

## Limitations

- Only nondegenerate ideal tetrahedra in \(\mathbb H^3\) are covered.
- Stability is measured by Euclidean squared deviation of the three dihedral angles.
- No finite, hyperideal, generalized, higher-dimensional, or intrinsic-moduli analogue is claimed.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
