# Independent mathematical audit

## correctness

PASS

Using Ferroni--Riccardi's interval-poset representation Q, rank-one elements are [vertex,1] and [0,facet], giving a1=v+f. Rank two consists of [edge,1], [0,edge] and vertex--facet incidences; the latter count is 2e, so a2=4e. For rank-three lower intervals, the local toric g linear coefficient is atoms-3. Summing over [facet,1] and [0,vertex] gives 4e-3(v+f), while the [edge,facet] and [vertex,edge] types contribute zero. In the toric h recursion this yields [x^3]h=v+f-4 and [x^2]h=6+8e-6(v+f). Euler's relation e=v+f-2 reduces the latter to 2(v+f)-10; toric h symmetry supplies the remaining coefficients. The factorization is direct. Since every three-polytope has v,f>=4, v+f-8>=0 and the quadratic factor has discriminant (v+f-8)(v+f-4)>=0 with positive coefficients, so its roots are negative. The finite verifier checks representative Platonic examples only as consistency tests.

## originality

PASS

Ferroni--Riccardi prove the general structural identity identifying the Eulerian-kernel Z-polynomial with the toric h-polynomial of the interval poset and explicitly ask about gamma positivity for Gorenstein* lattices. Their inspected primary text does not state the dimension-three coefficient collapse, gamma vector, or real-rooted factorization. The submitted rank-by-rank evaluation closes the full three-dimensional polytopal subclass and strengthens gamma positivity there to real-rootedness.

## value

PASS

The result gives a complete dimension-three answer to a stated gamma-positivity question for the natural polytopal subclass and strengthens it to real-rootedness with an explicit universal formula. The calculation is structural and all-dimensional within the three-polytope class, not an extrapolation from examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
