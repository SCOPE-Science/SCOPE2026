# Independent mathematical audit

## correctness

PASS

For the stated positive rates, the log reverse/forward edge ratio is 2 z_i F(J sum_{k in N(i)} z_k). The oriented ij-square affinity is 2 z_i z_j[H(R_j)-H(R_i)] for an underlying edge, and zero for a nonedge. Vanishing on squares is sufficient as any two flip paths with the same endpoints are related by interchanging successive distinct flips and cancelling double flips. Differentiating F gives an even F' strictly decreasing with |a| when J>0 and 0<s<1 (the strict decrease of F' uses s); H is then even and strictly decreasing for positive arguments since |x+1|>|x-1|. Thus all square equalities hold exactly when |R_i|=|R_j| for each edge and spin assignment. Assigning all plus spins forces equal degrees across the edge. At common degree d>=3, if the reduced neighborhoods differ, flipping one spin in their symmetric difference gives absolute sums d-3 and d-1, a contradiction. Equal closed neighborhoods propagate through a connected component and make it a clique. Degree two components are cycles; degrees zero and one give cliques, and all these types satisfy the square condition. The cycle Ising weight uses linearity of F on the three possible local fields, and the clique weight has the correct magnetization-layer log increment. On P3 the positive magnitude 2[2F(J)-F(2J)] follows from strict concavity; on K4, 3A+B=F(3J) and A-B=F(J) verify the displayed couplings with B<0. All-positive transition rates give an irreducible finite chain (the empty graph is trivial), and the edge terms (a-b)log(a/b) in stationary entropy production are nonnegative, vanishing simultaneously exactly at detailed balance. At the excluded linear-response endpoints all graphs are reversible. The bundled floating-point checker was inspected, not executed; it is a finite diagnostic, not the proof.

## originality

PASS

The supported distinct claim is the necessary-and-sufficient topology classification for the exact uniform-coupling, zero-field, continuous-time strong-dephasing rates. The rates, the log response, the cycle and clique cases, and nonequilibrium behavior on a square lattice are not claimed as new. Neither the strongest inspected same-model passages nor the nearby indexed findings identify the reversible graphs over all finite simple graphs. This is a bounded best-of-knowledge judgment, not historical priority certification.

## value

PASS

The theorem closes a natural gap left by the known ring, clique and square-lattice cases: the graph alone decides detailed balance throughout the interior parameter range. The open three-vertex path is a sharp small obstruction while the reversible K4 has a four-spin term, separating non-pairwise effective interactions from steady currents. This is a complete graph-structural criterion, not a tabulated parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
