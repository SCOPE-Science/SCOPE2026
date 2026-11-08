# Independent mathematical audit

## correctness

PASS

Fix full-dimensional compact convex (d−1)-polytope P, q interior, h>0, d>=2. The Gaussian vertex tangent cone at apex gives a(h)=∫_0^∞φ(s)Pr[Z∈(s/h)(P−q)]ds, strictly decreasing by strict nested homothetic bodies and positive Gaussian measure, with endpoints 1/2 and 0. At each base vertex v, C_v=cone(P−v) is full-dimensional pointed and w_v=q−v lies in its interior. The tangent-cone section is C_v+(s/h)w_v; these translations strictly increase in Gaussian measure as h increases, since a supporting functional exhibits an open difference set. Dominated convergence yields b_v(h) from 0 to 0.5 γ_(d−1)(C_v). Because finitely many b_v are strictly increasing, b(h)=min_v b_v(h) is strictly increasing and continuous. Thus a(h)−b(h) changes sign exactly once and min(a,b) increases before the balancing height h* and decreases after it; joint continuity in q yields continuous h*(P,q). For regular (d−1)-simplex circumradius R, matching edge lengths gives unique h*=R sqrt((d+1)/(d−1)), the regular d-simplex. Inspected exact Gaussian cone geometry; packaged checks/verify.py samples triangular, rectangular and hexagonal 3D pyramids and triangulated trihedral angles. Those finite samples are corroboration, not all-dimensional proof. Boundary projections excluded.

## originality

PASS

PASS by best-of-knowledge: Licht 2026 minimum vertex solid-angle/fullness inequalities do not state the constrained one-parameter height max-min balancing theorem; Akopyan–Karasev 2015 treats global upper bounds for minimum polytope vertex angles (3D theorem and higher-dimensional conjecture), not fixed arbitrary polytopal base and interior apex projection. O’Hara cone isoperimetric center optimizes a different functional; indexed pyramid shadow and width optimization are different invariants. Licht full text not accessible; relevant open risk is recorded.

## value

PASS

The least normalized solid angle of every vertex is a natural simplex/pyramid quality invariant. Opposing strict monotonicity at apex and every base vertex solves a nonlinear, constrained max-min problem for all dimensions, every fixed polytopal base and interior apex projection. The unique balancing height and continuous dependence provide an exact structural classification beyond regular tetrahedra or isolated numerical examples; it does not claim unrestricted simplex optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
