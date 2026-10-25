# Independent mathematical audit

## correctness

PASS

Use all 65536 masks on sixteen row-major grid vertices; alpha(S)=max(alpha(S\{v}),1+alpha(S\N[v])) gives exact induced independence number and excludes precisely those containing any of the 405 independent 4-sets. Independent re-enumeration gives the complete augmented f vector (1,16,120,560,1415,1788,912), sum 4812. The stated deterministic greedy vertex-toggle matching (v=0,...,15) makes 2364 matched pairs; remaining exactly 84 six-vertex faces. On the FULL augmented Hasse diagram, orient all matched incidences up and all other incidences down and exhaustively topologically sort all 4812 nodes and 22008 directed edges, confirming no directed cycle. Deleting the matched empty-simplex pair leaves an ordinary matching with one critical vertex and eighty-four critical 5-faces, so Forman's theorem gives a CW realization with one 0-cell and 84 5-cells; all attaching maps to a point are constant and the result is wedge 84 S5. Independent regeneration reproduced the face vector, matches, critical faces, Hasse edge count and complete sort; the additional mod2 verifier only corroborates integral homotopy. Precisely one 4x4,k=4 instance; not a proof of all-k rectangular-grid conjectures.

## originality

PASS

Filakovsky's current full text proves k=2 and k=3 all grids and arbitrary k only edge-glued square sequences, a narrower hypothesis than a 4x4 grid (nine faces on 16 vertices require more than edge-only gluing). The concrete 4x4,k=4 wedge84 is not a mechanically implied instance, but a natural next-case test of the conjectured wedge pattern. This is a bounded best-of-knowledge scientific judgment: an unsuccessful search cannot prove absolute priority.

## value

PASS

The 4x4 square grid at robustness 4 is the first natural width-four instance just outside published k=2,3 and edge-only gluing theorems; its explicit sphere wedge supplies a meaningful complete finite test and exact homotopy invariant for an open parameter regime, without claiming the whole conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
