# Independent mathematical audit

## correctness

PASS

In a bipartition, the off-diagonal adjacency block B has rank m: a nonzero minor requires a matching, while the submatrix of a maximum matching has exactly one perfect matching (two would produce an alternating cycle). The negative eigenvalue count is rank B by the singular-value decomposition. The forest dominance complex has top reduced integral homology of rank one in degree m−1. For any maximum matching the oriented join of the endpoint differences embeds as a cycle: a closed neighborhood contains its vertex's matched edge or an unmatched vertex. By König's theorem a minimum cover has m vertices, one from each matched edge. It is a facet because each of its vertices has a neighbor outside it, and the outside is independent, so adjoining any outside vertex introduces its full closed neighborhood. Coefficient extraction at the cover facet vanishes on boundaries and has value s_M(C)=±1 on the matching cycle, proving that the cycle is primitive. Comparing the coefficients at C and gC gives the stated sorting-sign formula. Coordinate restriction of E_- to C is injective by negative definiteness (the complementary vertex set is independent), hence an isomorphism by dimension. If a cover replaces a by its matched partner b, the unique restricted basis vector supported at a on the old cover has quadratic form 2x_b<0: other neighbors of a must stay in both covers. The determinant sign therefore acquires the same reversal and row-order correction as s_M. The single-swap graph is connected: after contracting matching edges the unforced implications form a partial order on the matched-edge endpoint choices, since the contracted graph is a forest. One can change coordinates along that order to reach the coordinatewise meet of two admissible assignments, respecting all forced choices. Thus sign(d_C)/s_M(C) is constant. The natural restriction identity d_(gC) det(g|E_-)=s_g(C)d_C combines this with the integral coefficient formula. Isolated vertices are excluded from faces and E_-, disconnected components present no exception, and for m=1 the same proof gives the action on reduced H0.

## originality

PASS

The sphere, its matching-number dimension, and the endpoint-difference generator technique are already established; the full topological sign also has a distinct indexed formulation via orbit-forest matching numbers. The supported distinct contribution here is the explicit identification with the determinant on the negative adjacency eigenspace for every forest, together with the arbitrary maximum-matching/minimum-cover coefficient comparison. The fixed-space record does not assert this spectral identification or the sorting formula; it is not evidence that the topology alone determines the spectral side without proof. No general publication-priority claim is made.

## value

PASS

The orientation sign is the only nontrivial integral homology datum left after the classical sphere theorem, and the identification with a natural spectral subspace gives a structural bridge between two graph constructions for a whole class, including part-flipping actions and permutations of components. The exact minimum-cover recipe computes the same scalar without numerical diagonalization or a specially adapted matching. This is useful beyond either the nonequivariant sphere theorem or tabulating signs on a few trees, even though the orbit-forest formula also computes the topological sign.

The dated certificate retains the supplied scientific assessment, sources and limitations.
