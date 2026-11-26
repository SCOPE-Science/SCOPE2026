# Independent mathematical audit

## correctness

PASS

With real potentials, the adjacency commutator is real skew-symmetric and has the same norm on the complex vertex space. Pair-fixing automorphism averaging preserves the target difference and cannot increase the norm. For the hubs the resulting three-dimensional skew block has squared norm (2m+4)s²+2mu² at hub difference 2s, minimized at u=0. For two leaves, projection onto the symmetric hub vector bounds the difference by the operator norm, and opposite unit leaf potentials attain equality. In the hub–leaf case only the two hubs, target leaf and unit aggregate of other leaves remain; the skew block has half squared Hilbert–Schmidt norm S_m and Pfaffian tx(1−v). The radicands are squares of the sum and difference of the two singular speeds, and column bounds give compact sublevels when m≥2. Compression to a smaller induced book proves monotonicity; the triangle gives the lower bound on r_m and the x=2b/t, v=b/t derivative at zero makes r_m<√2 strict. At a minimizer the aggregate column gives |x|≤2/t, so the target-leaf column gives √2−√2/t+O(t^−2) as a lower bound for large t. The explicit b=1−t^−1/4 trial gives radicands 2[(1±b−b/t)²+3b²/t²]; the smaller positive linear term is of order t^−1/4. The square-root corrections are O(t^−7/4), and replacing b by one incurs O(t^−5/4). Reciprocation yields the stated error and coefficient in m−1. The supplied check_book.py was inspected, not executed; sampled matrix checks and finite numerical optimizations do not certify global optima or the asymptotic.

## originality

PASS

The bounded comparison supports the exact orbit distances on the spine-edge book K2 ∨ independent m-set, in particular the attained hub–leaf prescription, and the fact that its hub–leaf asymptotic retains the first correction despite the spine edge. The analogous complete bipartite family already has the same leaf–leaf distance and the same first hub–leaf coefficient; these facts are not novel on their own. A previously known diamond-graph leaf pair is an exact special-case overlap.

## value

PASS

Books are a natural one-edge change to a standard complete bipartite family. The operator metric responds differently on its three orbits, and the exact result separates the changed hub–hub law from the persistence of the leading hub–leaf behavior. The finite attained reduction makes the remaining distance evaluable for each m without optimizing over all vertex potentials. This is a useful exact invariant and edge-edit comparison, not a claim of a new asymptotic coefficient independent of the graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
