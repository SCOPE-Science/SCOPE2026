# Same-model review

## Correctness

PASS. Every nondegenerate centrally symmetric convex hexagon is the sum of three centered segments, with area \(4(X+Y+Z)\). The circumscribed-parallelogram area is \(4h_P(u)h_P(v)/|\det(u,v)|\). Since polygonal support functions are linear on normal-fan cones, minimizing one normal at a time reduces the unrestricted global minimum to a pair of existing edge normals. The three resulting tight enclosures have areas \(4(T+XYZ/X^2)\) and its cyclic counterparts. Thus the smallest is \(4(T+XYZ/M^2)\), with no unexamined orientation case. The upper extremum, its affine-regular equality, and the sharp determinant-ratio stability follow by exact positive-variable algebra. A rational one-parameter family attains the stability bound for every admissible determinant ratio.

## Originality

PASS. The classical Petty theorem already gives the universal bound \(4/3\) and equality precisely for affine-regular hexagons; these components are not claimed new. The inspected recent primary preprint gives that historical bound but no exact per-hexagon area expression. The inspected Section 4 of Pełczyński--Szarek establishes the same universal extremal theorem but does not present the three-determinant profile or the sharp stability estimate. The inspected affine hexagon shape-evolution paper concerns different extremal-rectangle dynamics. Targeted direct-source, algebraic and equivalent geometric searches did not uncover stronger covering statements.

Residual originality risk: an older optimization/computational-geometry source may give an equivalent pointwise formula under different parameterization, especially since the normal-fan reduction itself is elementary.

## Value

PASS. Enclosing quadrilaterals are a canonical convex approximation objective. This claim replaces a universal worst-case upper bound for all centrally symmetric hexagons by an explicit affine-invariant exact optimizer, a three-candidate algorithm, and a sharp family-wide stability law. It distinguishes how much each non-regular affine hexagon improves on the classical extremal value, with exact equality families for every condition-number parameter. No unrelated downstream conjecture is needed to motivate the invariant.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The primary motivating paper is Fodor--Grundbacher, arXiv:2506.05185v1. The closest earlier complete mathematical coverage is Pełczyński--Szarek, DOI:10.1017/S0305004100069619, Section 4, which proves the universal upper ratio and affine-regular equality but no profile. Related affine hexagon geometry appears in Domokos--Lángi--Mezei, arXiv:1604.07630v2.

The original 1955 Petty text was not directly accessible. The result covers only genuine six-sided centrally symmetric polygons; the quantitative stability is in determinant anisotropy, not a geometric metric.
