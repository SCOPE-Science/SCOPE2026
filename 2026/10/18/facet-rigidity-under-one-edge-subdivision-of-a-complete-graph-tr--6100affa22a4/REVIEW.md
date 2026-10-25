# Independent mathematical audit

## correctness

PASS

Fix m=n-2 untouched clique vertices U. The active-incidence rank criterion forces polar-extreme potentials to have a connected tight-edge graph and hence integral heights. On the clique U, heights are either constant or 0/1 (after translation). For each nonempty proper lower level subset, a,b adjacent to all of U can each lie at 0 or 1 and the two-edge subdividing vertex z has two admissible tight placements, giving exactly eight polar vertices. For constant U, tight connectivity forces a,b in {-1,+1}, with exactly six allowed z configurations. Counting 8(2^m-2)+6 gives 2^(n+1)-10. Degree identifies z, so Aut G=S_m x C2; complement/sign and endpoint swapping partition nonconstant configurations into 6 or 3 orbit-types per height class, totaling 3m. Tight oriented edges are vertices on the face; counts rk+2r+2, rk+2k+2 or rk+m+1, and the quadratic maximum yields floor(n^2/4)+2; the special m=3 tie adds six constant-class maximizers. Independently exhaustive integer potentials with slack edges and tight-spanning connectivity n=5,6,7 returned (facets, signed orbits, max vertices) (54,9,8),(118,12,11),(246,15,14). All-n assertion rests on classification and quadratic proof, not the finite test.

## originality

PASS

The general tight incidence criterion and K_n baseline are prior. This theorem counts a one-edge topological graph subdivision (not regular triangulations or contractions of a polytope); the total facet count plus sharp face-incidence spectrum and signed orbit sizes were not found in checked prior general results or tables.

## value

PASS

Subdividing one edge is a canonical perturbation of an equilateral finite metric and produces exponentially many facet normals but only linearly many symmetry classes. The exact maximum facial incidence, with sharp extremizer multiplicities, quantifies a genuine geometric consequence, beyond a routine fixed-size table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
