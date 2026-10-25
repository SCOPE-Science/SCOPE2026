# Independent mathematical audit

## correctness

PASS

Actual frozen RESULT.md b30b76... gives tube-simplex-sum support width F(u)=∑_B (max_B u−min_B u). Sorting u and decomposing into centered nested cut indicators gives exact coarea sum and ℓ2 triangle inequality; strictness forces a two-level cut for any minimizer. For any S with s vertices, cyclic-run counting gives C(S)=n(n−1)+1−∑runs T(length), with T(r)=r(r+1)/2, and C(S)≥A_n+s(n−s), equality exactly single cyclic interval. Consequently optimize √n(A_n+z)/√z for z=s(n−s). For n≥5 A_n≥U_n=floor(n²/4), balanced z is optimal; n4 singleton width 4√3 beats balanced 7; n3 singleton. Exact integer cut enumeration built cyclic connected subsets independently through n10 and reproduced squared minima 27/2,48,120,722/3,1701/4,1369/2,5184/5,7442/5; equality cardinalities also verified. The general n proof is the coarea/counting/derivative chain, not sample enumeration.

## originality

PASS

A published Resultary record computes inradius of EXACT SAME W_n but does not determine width; its unique singleton inball tangencies are compatible with the new balanced minimum-width cut when n≥5. Weighted graphical-zonotope inradius uses the analogous coarea mechanism, but for sums of segments, not the connected-subset simplex-sum cyclohedron. Thus the formula and change at n=5 survive comparison, subject to prior geometric-width literature risk.

## value

PASS

Euclidean minimum width is a natural metric invariant of the standard cyclohedron, distinct from its known inradius. Exact minimizing normal classes and abrupt singleton-to-balanced transition are useful for convex-body thickness, directional section/packing estimates and show that different extremal metrics prefer different facets. It is a complete all-n classification with independent significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
