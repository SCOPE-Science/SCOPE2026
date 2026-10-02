# Independent scientific audit — SCOPE-20260918-f4944b61f2db

Audited at: 2026-10-01T08:23:38.851470Z

Disposition: **passed**

## Correctness — PASS

For arbitrary points in a triangle, the two support-line slopes at the perpendicular-bisector chord endpoints are bounded by the chord half-lengths. The smaller unoriented angle between the supporting side lines is at least the minimum triangle angle, so convexity of tangent gives \(C(T)\ge \tan(\alpha/2)\). The minimum-angle vertex and its internal angle-bisector foot attain equality. Splitting by acute versus obtuse largest angle then reduces \(r/R\) at fixed \(C(T)\) to a one-variable monotonicity calculation, yielding both sharp envelopes and equality families.

## Originality — PASS

Full-text inspection of the paper introducing the invariant gives only general roundness/fatness comparisons, disk and square examples, and partition lemmas. It does not evaluate arbitrary triangles or derive the sharp fixed-roundness fatness interval.

### Equivalent formulations

Classical triangle minimum-angle and fatness parameters are related objects, but the exact equality with the new perpendicular-bisector invariant is not a standard renaming.

### Broader coverage

Those inequalities do not determine C(T) exactly or the extremal r/R range at fixed triangle roundness.

### Exact database or table

There is no natural pre-existing database for this newly introduced invariant; noncoverage is established by inspecting the defining primary paper.

### Claim versus prior implication

The audited exact formula and sharp calibration require new triangle geometry beyond the source's general comparisons.

## Value — PASS

Triangles are the canonical finite-dimensional test class for a new planar fatness invariant. Identifying the invariant exactly with the classical minimum-angle quality parameter and determining the full sharp conversion to r/R is a natural complete classification with direct mesh-quality interpretation.

## Sources inspected

- Cutting a convex body into fat parts and approximating Euclidean distance by graph distances — https://arxiv.org/abs/2609.20702. NOT_COVERING: The source gives general comparison bounds and disk/square examples, but no arbitrary-triangle evaluation or sharp triangle-specific fatness window.

## Checked sources

- https://arxiv.org/abs/2609.20702

## Residual risks

- The invariant was introduced immediately before this record, so unindexed parallel calculations remain possible.

## Limitations

- The formulas are specific to nondegenerate Euclidean triangles.
- The containing radius is the smallest-disk radius; it differs from the three-point circumradius for obtuse triangles.
- No general convex-body constant is improved.
