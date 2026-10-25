# Review of the antiprism packing–covering theorem

## Correctness — PASS
The sphere sites and both optimization criteria are normalized explicitly. Packing reduces to two chord types whose minima cross uniquely. Covering reduces to the origin-centered inradius of the inscribed convex hull; its polar faces have support height \(h\), while every triangular face has the computed support \(\beta_n(h)\). The ratio \(\beta_n(h)^2/h^2\) has exactly one crossing and the triangular support is decreasing beyond that crossing; hence the global covering optimizer and all three farthest-contact phases follow. The exact difference of optimizer heights and the asymptotic 45-degree covering loss are algebraic consequences. The `verify.py` program passed 2412 finite numerical checks of supporting facets, pairwise packing distances, contact multiplicities and optimality. Those checks are not an infinite proof and are not used as one.

## Originality — PASS, qualified
The closest inspected primary literature is Fowler, Tarnai and Gáspár's 2002 study of antipodally constrained spherical packing/covering. Its ten-site intermediate pentagonal antiprism does not supply the all-\(n\) constrained-configuration covering optimum and contact phase. Brauchart et al. (2015) use the same covering-radius/facet-hole language for random sites, not these symmetric sites. Wimmer (2017) addresses the full global eight-site covering problem, but only its publisher preview was accessible; the finite \(n=4\) priority comparison is incomplete. Searches using antiprism, staggered latitude rings, mesh norm, spherical cap covering and packing-covering transitions did not identify the full theorem; search failure is not a guarantee of priority. The familiar octahedron and equal-edge packing observations are credited, not claimed as independent novelties.

## Mathematical value — PASS
The fixed staggered-ring family is a natural design constraint in spherical covering and packing. Exact, unique optima for each integer \(n\ge3\) answer a complete geometric classification problem. The discontinuous farthest-hole contact count and the asymptotic \(\pi/4\) radius penalty explain a substantive and growing incompatibility of classical packing and covering goals. No global optimality over arbitrary sites or arbitrary twists is asserted.

## Limitations and closest comparisons
The exact result concerns a one-parameter symmetric configuration family and cannot determine unrestricted best spherical coverings. Independent priority assessment remains necessary, particularly for specialist finite-case covering publications unavailable in full. Numerical checks are finite.

Self-review: passed. Independent audit: not yet performed.
