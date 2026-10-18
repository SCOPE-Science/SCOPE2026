# Independent mathematical audit

## correctness

PASS

At the assigned tree read the full RESULT.md and verify.py. For C=[-1,1]^3, its 12 edge midpoints are all permutations/sign choices of (1,1,0) and their convex hull is exactly C intersect {|x|_1<=2}. Diagonal scaling D=diag(a,b,c) sends the midpoint hull to P=D C intersect {sum |x_i|/a_i<=2}. But P°={sum a_i |x_i|<=1}; if P intersect lambda P° equals the midpoint hull, three interior-to-box points with normalized positive coordinates (4,3,3)/5 and permutations belong to the midpoint hull’s triangular facet, forcing lambda values (4a²+3b²+3c²)/5 and permutations. Their equality yields a²=b²=c², hence a=b=c>0. Conversely cubes of half-side s have unique lambda=2s². Independently checked facet-probe values for (1,2,3): 43/5,46/5,51/5; the contradiction is exact, not a sampled optimization.

## originality

PASS

Reid arXiv:1604.00580v1 actually defines rectification as the hull of edge midpoints and explicitly proposes a universal scaled-polar intersection in Conjecture 3. Its surrounding regular-polyhedron formulas do not supply this noncubic rectangular-box obstruction. Resultary and direct alias searches for cuboid/orthotope/midpoint-hull/polar-intersection found no prior rectangular-box iff-cube theorem; the self-hit was excluded. This is a direct counterexample to the motivating published conjecture, not its confirmation.

## value

PASS

A three-parameter family of elementary centrally symmetric polyhedra is a natural first stress test for a purported identity valid for all convex polyhedra. The complete if-and-only-if classification both refutes the universal conjecture via explicit noncubic boxes and identifies the rigid regular boundary. Its importance as a counterexample does not depend on the algebraic proof being long.

The dated certificate retains the supplied scientific assessment, sources and limitations.
