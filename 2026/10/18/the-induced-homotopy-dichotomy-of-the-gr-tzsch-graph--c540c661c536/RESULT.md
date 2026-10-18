# The induced-homotopy dichotomy of the Grötzsch graph

## Finding

Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph and \(K=\operatorname{Ind}(G)\) its ordinary independence complex. For **every nonempty subset** \(W\subseteq V(G)\), the inclusion \(K[W]\hookrightarrow K\) is either a homotopy equivalence or a nullhomotopic map. These possibilities are completely characterized by the vertex set.

Write \(o_i\) for the five original cycle vertices, \(t_i\) for their five Mycielskian twins, and \(r\) for the root, with indices modulo five. Put
\[
 C_i=\{o_0,o_1,o_2,o_3,o_4,r,t_i,t_{i+1},t_{i+2}\}\qquad (i\in\mathbb Z/5\mathbb Z).
\]
Then
\[
 K[W]\longrightarrow K\text{ is a homotopy equivalence}
 \quad\Longleftrightarrow\quad C_i\subseteq W\text{ for some }i.
\]
In every other nonempty case the inclusion is nullhomotopic. In particular, there are exactly five inclusion-minimal homotopy-equivalence carriers, each on nine vertices, and precisely eleven equivalence-carrying vertex subsets in total: five with nine vertices, five with ten, and the full vertex set. Each minimal carrier has homotopy type \(S^2\), as does \(K\), and its fundamental class is a primitive generator of \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z\).

The full graph automorphism group is \(D_5\). Its integral action on \(\widetilde H_2(K;\mathbb Z)\) is the dihedral reflection-sign character: all rotations act by \(+1\) and all reflections by \(-1\).

## Assumptions and scope

The graph is simple, finite and undirected. Its vertex set is \(\{o_i,t_i:i\in\mathbb Z/5\mathbb Z\}\cup\{r\}\), with edges exactly
\[
 \{o_i,o_{i+1}\},\quad \{o_i,t_{i+1}\},\quad
 \{o_{i+1},t_i\},\quad \{r,t_i\},\qquad i\in\mathbb Z/5\mathbb Z.
\]
Here \(K[W]\) is the **vertex-induced simplicial subcomplex** of \(K\); the map in the theorem is the actual simplicial inclusion, not an abstract comparison of homotopy types. The empty subset is excluded because its empty realization is not homotopy equivalent to or nullhomotopic into a point in the same standard sense. No other graph, general Mycielskian, or higher degree is covered.

## Proof

**1. A spherical collapse spine.** For the representative \(C_2\), label \(o_i\) by \(i\), \(t_i\) by \(5+i\), and \(r\) by \(10\). The complete complex has nonempty-simplex vector \((11,35,40,15,1)\). The file `certificate.json` records a sequence of 27 elementary simplicial collapses from \(K\) onto the induced subcomplex \(K[C_2]\). Two further elementary collapses take that induced subcomplex onto a 2-dimensional simplicial complex with \(9\) vertices, \(21\) edges, and \(14\) triangles. Every edge belongs to exactly two triangles, every vertex link is a connected cycle, and the surface is connected. Its Euler characteristic is \(9-21+14=2\), so by the classification of closed surfaces it triangulates \(S^2\). These certified elementary collapses show both \(K\simeq S^2\) and \(K[C_2]\simeq S^2\), integrally and with the actual inclusion a homotopy equivalence. Rotating indices establishes the same statement for all five \(C_i\).

**2. All containing subsets are equivalences.** For a fixed representative \(C_2\), any vertex set containing it is one of \(C_2\), \(C_2\cup\{t_0\}\), \(C_2\cup\{t_1\}\), or \(V(G)\). The certificate provides elementary collapses of the intermediate induced subcomplexes onto \(K[C_2]\), using 11 pairs in either ten-vertex case. Together with the 27-pair ambient collapse, the inclusions of these four complexes into \(K\) are homotopy equivalences. Cyclic rotation establishes this for every \(W\) containing some \(C_i\).

**3. All other inclusions factor through contractible induced complexes.** The certificate also verifies collapses to a single vertex for: \(K-o_0\) (41 pairs); \(K-r\) (45 pairs); and \(K[D_0]\) (25 pairs), where
\[
 D_i=\{o_0,o_1,o_2,o_3,o_4,r,t_i,t_{i+1},t_{i+3}\}.
\]
Rotation yields the corresponding contractible complexes for every \(K-o_i\) and every \(K[D_i]\). If \(W\) omits an original vertex or \(r\), it lies in one of the first six contractible induced complexes. Otherwise it retains all six such vertices; let \(T\) be its subset of twins. If \(T\) contains three cyclically consecutive twins, then \(W\) contains a \(C_i\). If not, \(T\) is contained in one of the five nonconsecutive three-element sets \(\{i,i+1,i+3\}\): every four-element set contains a consecutive triple, the five other three-element sets have the displayed form, and each pair lies in one of them. Hence \(W\subseteq D_i\) for some \(i\). The inclusion \(K[W]\hookrightarrow K\) therefore factors through a contractible simplicial complex and is nullhomotopic.

The eleven listed contractible supersets are the inclusion-maximal sets not containing a \(C_i\); the five cores are the inclusion-minimal sets containing one. This proves the exhaustive dichotomy, including its cardinalities. Since each good inclusion is a homotopy equivalence onto a sphere, its degree on integral top homology is \(\pm1\), not merely nonzero over a field.

**4. Symmetry.** The root is the unique degree-five graph vertex, the original vertices have degree four, and the twins have degree three. Thus every automorphism preserves these three layers. Its restriction to the original pentagon is dihedral and determines the twin permutation; conversely every such dihedral permutation preserves the graph. Hence \(\operatorname{Aut}(G)\cong D_5\). The verifier computes the signed simplicial Lefschetz number on all ten automorphisms, using
\[
 \operatorname{tr}(g\mid \widetilde H_2(K;\mathbb Q))=
 -1+\sum_{\substack{\varnothing\ne\sigma\in K\\g\sigma=\sigma}}
 (-1)^{|\sigma|-1}\operatorname{sgn}(g|_{\sigma}).
\]
All five rotations have trace \(+1\) and all five reflections trace \(-1\). The reduced integral homology is concentrated in degree two and is \(\mathbb Z\), so the same signs describe the integral action.

## Verification

Run `python3 verify.py` next to `certificate.json` using only the Python standard library. The verifier reconstructs the graph's twenty edges and all \(102\) nonempty independent faces. It checks all seven independent collapse sequences pair by pair, including unique-coface freeness, equality of the final complexes, and the closed connected sphere's local manifold conditions. It then exhaustively checks the covering dichotomy for all \(2^{11}=2048\) vertex subsets and the signed Lefschetz traces for all ten graph automorphisms. The verified output ends with `ALL_2048_INDUCED_SETS CLASSIFIED GOOD_SIZES_9_5_10_5_11_1` and `FULL_D5_CHARACTER ROTATIONS_POSITIVE REFLECTIONS_NEGATIVE`. All homotopy and integral conclusions follow from the elementary collapses and manifold certificate, not from numerical Betti numbers.

## Relationship to prior work

Barmak (2010) proved general suspension and star-cluster results for independence complexes of triangle-free graphs; these do not classify the inclusion maps of this specific graph. Goyal, Shukla and Singh (arXiv:1905.06926, Theorem 4.1) showed \(\operatorname{Ind}(\mu(G))\simeq\Sigma\operatorname{Ind}(G)\), which already yields the **ambient** sphere for \(G=C_5\). Carnero Bravo (arXiv:2601.13432, Theorem 5 and Corollary 9) likewise covers the nonequivariant homotopy type of generalized Mycielskians of cycles. Neither inspected statement gives the exact eleven equivalence-carrying vertex subsets, the five minimal nine-vertex cores, the eleven maximal null-carrier supersets, or the induced-inclusion homotopy dichotomy. The ambient sphere is acknowledged as previously known.

## Limitations

The theorem concerns the inclusion maps into the full independence complex, **not** the intrinsic homotopy types of every bad induced subcomplex. A bad subcomplex may itself have nontrivial topology despite its inclusion being nullhomotopic. The dihedral character is a supplementary invariant of this finite graph, not a claim about arbitrary Mycielskians. An equivalent induced-support calculation in unindexed literature remains possible; publication priority and independent validation are not claimed.

## References

1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first public 2010-07-02. https://arxiv.org/abs/1007.0418
2. S. Goyal, S. Shukla, A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, 2019, Theorem 4.1. https://arxiv.org/abs/1905.06926
3. A. Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432, 2026, Theorem 5 and Corollary 9. https://arxiv.org/abs/2601.13432
