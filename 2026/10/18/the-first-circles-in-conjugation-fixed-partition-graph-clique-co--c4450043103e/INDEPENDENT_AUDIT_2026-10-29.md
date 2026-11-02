# Independent mathematical audit

## correctness

PASS

All-size PL fixed-point orbit model follows from uniqueness of barycentric coordinates of a simplicial involution: on each support simplex, tau-invariance is equality of weights along 1- and 2-element conjugation orbits, and a set of orbit barycenters spans a simplex precisely when each orbit is internally a clique and all cross-pairs are adjacent; this is exactly Cl(H_n). If two conjugate distinct Ferrers diagrams differ by one transfer, their n−1 common cells form a self-conjugate diagram and the added cells are transposed off-diagonal addable corners; converse is immediate. For all 22 sizes, the actual certificate.json blob SHA c03b41d... was independently parsed and checked: partition sets up to p(22)=1002; adjacency independently characterized by Ferrers-intersection cardinality n−1; all admissible orbits/compatibility cliques rebuilt; all 414 faces, all 160 ordered actual free-face pairs uniquely certified at the exact deletion step; residual graph vertices/edges, components, cycle ranks and separate mod-2 boundary ranks matched all 22 rows. At n=18 and 20 the core is one isolated point plus an 8-vertex graph with beta1=1; at n=22 it is one point plus a 15-vertex beta1=2 graph; all other n≤22 have only contractible components. Actual elementary collapses preserve integral homotopy, not just mod-two ranks. Published K_n≃wedge S² ensures reduced rational homology concentrated in degree 2; simplicial Lefschetz identifies 1+tr(tau|H2) with chi(F_n). Thus chi(F_22)=0 gives trace −1; smaller n give chi=1 or 2 and nonnegative traces. The all-size orbit model is proved but no finite certificate extrapolates to n>22.

## originality

PASS

Best-of-knowledge PASS after statement-level comparison of same-object primary sources, Resultary semantic searches, published repository code searches and database/table searches. The barycentric fixed-orbit construction itself is standard; the novel candidate is its Ferrers-specific paired-corner instantiation together with the exhaustively certified sharp integral fixed-space homotopy through n=22 and negative rational conjugation character at n=22. A general nonequivariant sphere wedge theorem or ordinary clique-count table does not imply the involution character.

## value

PASS

Conjugation is the canonical internal involution of the integer-partition transfer graph, so its geometric fixed realization and rational action on H2 are motivated invariants. Earlier graph-level axis results omit fixed barycenters, while the ambient nonequivariant 2-sphere wedge misses the fixed one-dimensional topology entirely. The exact all-size orbit model and full 1≤n≤22 integral-collapse classification determine sharp qualitative first transitions: an S1 component at n=18 and a negative homology-character trace at n=22. These are meaningful exact finite cutoff results and a natural partial answer to a prior published equivariant-modeling direction; they do not claim an unproved general recurrence or a stronger all-size classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
