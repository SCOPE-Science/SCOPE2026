# Independent mathematical audit

## correctness

PASS

For each radius r the induction identifies all coordinate-swap orbits inside the Chebyshev square Q_r and separates their old colors globally. Every new front orbit (i,r+1) has an old-orbit neighbor cut I_i={a in [0,r]: |a-i|<=1}, distinct for r>=2; base r=0,1 separate by vertex degree. Swap invariance prevents splitting any orbit. For the lower bound, (0,n-1) and (n-1,n-1) have isomorphic unmarked neighborhoods to radius n-2 and are at distance n-1 from the unique marked root, but become different at round n-1. The underlying proof, not finite cases, gives every n>=3. Independent implementation checks n=3..10 round counts and final classes; source verification script independently inspected.

## originality

PASS

The exact submitted statement was compared against equivalent terminology, general bounds, named exact prior tables and their logical implications. Inspected relevant sources support a distinct increment; missing full texts and hidden equivalent special cases remain documented best-of-knowledge risks.

## value

PASS

The king graph is a natural diagonal-adjacency lattice used for symmetric-neighborhood refinement; a single individualized corner leaves one nontrivial stabilizer. Exact coincidence of 1-WL and that orbit partition, and the sharp number of synchronous fronts needed, are motivated structural facts for this infinite grid family; this is not an assertion about arbitrary strong products or a generic extremal n^2-vertex stabilization result. The result is modest in scope but not a mere parameter substitution from Cartesian grids.

The dated certificate retains the supplied scientific assessment, sources and limitations.
