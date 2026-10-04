# Review

## Correctness

PASS. The primary AC-group source proves that the commuting graph is a disjoint union of clique components \(K_{m_i}\), where \(m_i=|C_G(g)\setminus Z(G)|\) for distinct noncentral centralizers. Zero forcing is componentwise on a disjoint union. A singleton component contributes polynomial \(x\), while \(K_m\) for \(m\ge2\) contributes \(m x^{m-1}+x^m\). This gives the stated product, minimum-set classification, and count. The minimum-rank calculation is also componentwise: \(K_1\) has real minimum rank \(0\), while every \(K_m\), \(m\ge2\), has real minimum rank \(1\). Therefore \(M=Z\) exactly.

The packaged verifier directly reconstructs \(S_3,D_8,D_{10},D_{12},Q_8\), checks every centralizer and the AC condition, exhaustively enumerates all zero forcing sets, and verifies exact rational ranks of the block witnesses.

## Originality

PASS. The exact-object archive paper uses the centralizer-clique decomposition for genus and does not discuss zero forcing, maximum nullity, or graph minimum rank. The later zero-forcing-polynomial paper explicitly treats generic multiplicativity and uniqueness, so multiplicativity itself is prior coverage. Targeted web and semantic-database searches did not locate the AC-group specialization, the full minimum-zero-forcing-set classification, or the statement that the polynomial is a complete isomorphism invariant on this commuting-graph class.

## Value

PASS. The result identifies a natural class on which the zero forcing polynomial becomes fully graph-recognizing, despite not being a complete invariant in general. It also translates the roots and lowest degree of the polynomial into centralizer data and gives exact inverse-eigenvalue information. This is a complete structural classification for all finite AC-group commuting graphs, not a numerical computation for a single family.

Same-model review: passed. Independent audit: not yet performed.
