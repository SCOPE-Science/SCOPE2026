# A lexicographic infinite family of regular tournament flag complexes
## Finding
For every odd integer \(n=2m+1\ge 3\), let \(R_n\) be the cyclic tournament on \(\mathbb Z/n\mathbb Z\) with \(i\to j\) exactly when \(1\le (j-i)\bmod n\le m\). Let \(T_n=\overrightarrow C_3[R_n]\) be the tournament obtained from three disjoint copies \(A,B,C\) of \(R_n\), with every edge directed from \(A\) to \(B\), from \(B\) to \(C\), and from \(C\) to \(A\). Then
\[
\operatorname{dFl}(T_n)\simeq S^1\vee\bigvee^3 S^2\vee\bigvee^3 S^3.
\]
In particular, this gives an infinite family of regular tournaments of orders \(3n\) whose directed flag complexes have the same mixed-dimensional sphere-wedge type.

## Assumptions and scope
The directed flag complex \(\operatorname{dFl}(T)\) has one simplex for each transitive subtournament of the tournament \(T\). The lexicographic product used here replaces each vertex of the directed 3-cycle by a copy of \(R_n\), with all edges between two blocks oriented according to the corresponding outer edge. The claim is for every odd \(n\ge3\); no assertion is made for even block sizes or for other outer tournaments.

Each vertex of \(T_n\) has \(m\) out-neighbors in its own block and all \(n\) vertices in the next block, hence out-degree \(m+n=(3n-1)/2\), so \(T_n\) is regular. It is not doubly regular: two consecutive vertices in one block have \(n+m-1\) common out-neighbors, while a vertex in \(A\) and a vertex in \(B\) have only \(m\) common out-neighbors.

## Proof
Write \(X=\operatorname{dFl}(R_n)\), and let \(X_A,X_B,X_C\) be its three disjoint block copies. A transitive subtournament of \(T_n\) cannot meet all three blocks, because choosing one vertex from each block already gives the outer directed 3-cycle. Conversely, a vertex set meeting at most two blocks is transitive exactly when its intersections with the occupied blocks are transitive: all cross-block edges point uniformly in one direction. Therefore, as an abstract simplicial complex,
\[
K:=\operatorname{dFl}(T_n)=(X_A*X_B)\cup(X_B*X_C)\cup(X_C*X_A).
\]
The pairwise intersections are respectively \(X_B,X_C,X_A\), and the triple geometric intersection is empty.

The cyclic tournament complex \(X=\operatorname{dFl}(R_n)\) is the standard cyclic nerve complex \(\mathcal N(n,(n-1)/2)\): every transitive set has a source, hence lies in one of the cyclic intervals of \(m+1\) consecutive vertices, while every subset of such an interval is transitive. The cyclic complex collapses to a circle, so \(X\simeq S^1\). This identification and circle collapse are also the cyclic regular-tournament case recorded in Govc's directed-flag classification.

It remains to compute the union above. Put \(U=X_A*X_B\) and \(V=X_B*X_C\). Their intersection is \(X_B\). The two inclusions \(X_B\hookrightarrow U\) and \(X_B\hookrightarrow V\) are null-homotopic because an end of a nonempty join contracts inside that join. Since these are simplicial cofibrations, the ordinary union is a homotopy pushout, hence
\[
U\cup V\simeq U\vee V\vee\Sigma X_B.
\]
Now put \(W=X_C*X_A\). Its intersection with \(U\cup V\) is the disjoint union \(X_A\sqcup X_C\). Each component inclusion is null-homotopic both in \(W\) and in \(U\cup V\), and both target spaces are connected, so the full maps from \(X_A\sqcup X_C\) are homotopic to constant maps. A second homotopy-pushout calculation gives
\[
K\simeq U\vee V\vee W\vee\Sigma X_A\vee\Sigma X_B\vee\Sigma X_C\vee S^1.
\]
Here the last \(S^1\) is the extra suspension summand caused by the two connected components of \(X_A\sqcup X_C\). Since \(X\simeq S^1\), each join \(X*X\simeq S^3\) and each suspension \(\Sigma X\simeq S^2\). Substitution yields exactly
\[
K\simeq S^1\vee\bigvee^3S^2\vee\bigvee^3S^3.
\]

## Verification
The standalone verifier reconstructs \(R_n\) and \(T_n\) for the first nontrivial values \(n=3,5\), enumerates every transitive subtournament, verifies the exact three-join decomposition, checks regularity and failure of double regularity, and computes homology over \(\mathbb F_2\) and \(\mathbb F_3\). For \(n=5\), the 15-vertex complex has face vector \((15,105,315,450,300,75)\) and Betti vector \((1,1,3,3,0,0)\) over both fields, agreeing with the theorem. These finite calculations are checks of the symbolic proof, not substitutes for its universal quantifier.

## Relationship to prior work
Govc's 2020 classification has primary MSC \(55\)-08 and classifies regular tournaments only through 13 vertices; it separately classifies doubly regular tournaments through 27 vertices. The present family is regular but not doubly regular and has order \(3n\). Thus only the \(n=3\) member, of order 9, lies inside the published regular census; the infinite tail \(n\ge5\) starts at order 15 and is not implied by the doubly regular table. Govc's order-9 census does contain the same wedge type, so the theorem also gives a structural explanation for that low-order occurrence rather than claiming it as new.

Searches for directed flag complexes under the aliases directed clique complex, transitive-subtournament complex, tournament composition, tournament substitution, and lexicographic product did not locate a published formula for this three-block family. Searches of the indexed result database likewise returned directed Hom complexes and tournament neighborhood complexes as the closest entries, which are different constructions.

## Limitations
The novelty comparison cannot rule out unindexed or differently phrased literature on tournament substitution. The proof uses only ordinary homotopy type; it does not classify simple-homotopy types, equivariant structure, persistence, or maps induced by embeddings between different \(n\). The computational verifier checks representative finite cases only; the all-\(n\) statement rests on the block-decomposition and homotopy-pushout proof above.

## References
1. D. Govc, “Computing Homotopy Types of Directed Flag Complexes,” arXiv:2006.05333, first submitted 2020-06-09. The arXiv record gives primary MSC \(55\)-08; Section 3.1 treats regular tournaments through 13 vertices and records the cyclic circle case.
2. D. Govc, R. Levi, J. P. Smith, “Complexes of tournaments, directionality filtrations and persistent homology,” Journal of Applied and Computational Topology 5 (2021), 313–337, DOI 10.1007/s41468-021-00068-0.
