# Scientific review: maximum-perimeter rectangles in centrally symmetric cyclic polygons

## Correctness — PASS

The centering step follows from the Minkowski average with the reflection in an origin-symmetric convex polygon. For a centered rectangle the half-diagonals have equal Euclidean norm, and its perimeter is twice the sum of the lengths of their sum and difference. This objective is separately convex on the Cartesian square of the polygon. Because all original vertices share circumradius \(R\), maximizing the separately convex objective over vertex pairs produces a genuinely feasible rectangle rather than merely a parallelogram. The positive-definite Hessian away from collinear half-diagonals excludes nonvertex maximizers; the circumdisk's antipodal squared-distance inequality excludes off-center maximizers. Finally, the chord identities give the cosine of the exact perpendicularity defect. The proof covers all nondegenerate centrally symmetric cyclic polygons with at least four vertices, and all nondegenerate contained rectangles.

The included diagnostic checked 300 regular even orders, 104 deterministic nonregular centrally symmetric cyclic polygons, the linear scan against quadratic search, and 26,000 feasible centered sample rectangles. These computations are finite and supplementary. The dimensional normalization and equality counts were rederived directly; there is no reliance on an unverified general computational certificate.

## Originality — PASS, with residual risk

The most relevant earlier general result is Cabello–Cheong–Knauer–Schlipf (arXiv:1405.1223, Theorem 5), which solves the unrestricted maximum-perimeter rectangle problem algorithmically in cubic time. Knauer–Schlipf–Schmidt–Tiwary (2012) concern maximum *area* and separately highlight the perimeter problem. The 2021 Choi–Lee–Ahn contribution develops general-polygon algorithms, not an angular defect principle. The publicly available “Exact maximum-area rectangles in every regular even polygon” establishes a corresponding *area* law and vertex arrangement, but does not prove perimeter optimality or the general cyclic-polygon theorem. In particular, equality patterns for one objective do not imply an inequality for the other objective. The proposed theorem provides a distinct all-cyclic structural characterization and a linear-time angular algorithm, so none of these inspected mathematical statements implies it as written.

The residual risk is that an elementary chord or rotating-calipers argument equivalent to the vertex-pair principle was previously recorded under another name. Targeted searches did not identify one; that is evidence of incomplete coverage, not a proof of priority.

## Value — PASS

Finding a maximum-perimeter rectangle is an explicitly motivated convex-geometric optimization problem, not an arbitrary numerical slice. For the natural family of centrally symmetric cyclic polygons, the theorem collapses a continuous optimization with unrestricted rectangle position and orientation to nearest-perpendicular vertex-diameter selection, classifies every maximizer, and reduces cubic-time general computation to linear time when the vertices are ordered. The exact modulo-four regular-polygon deficit gives a sharp geometric measure of the obstruction to a square optimizer. Both the general structural reduction and the full continuous-family specialization are the substantive point; finite diagnostics and publication searches alone do not establish value.

## Source and scope limitations

The inspected literature includes the 2012 open-direction discussion, the 2014 general exact perimeter algorithm, the subsequent general-polygon algorithmic treatment, and the full public theorem on regular-even-polygon maximum *area*. No claim is made that this problem or its algorithmic general form was previously unsolved. The cyclic and symmetry assumptions are essential to the vertex-pair feasibility argument. No independent audit has occurred.

Same-model review: passed. Independent audit: not yet performed.
