# Iterated cyclic tournaments have nonzero neighborhood homology in every lower degree

## Finding
Let \(C\) be the directed three-cycle \(0\to1\to2\to0\). Define tournaments recursively by \(T_1=C\) and \(T_{k+1}=C[T_k]\), where the lexicographic substitution puts a copy of \(T_k\) at each vertex of \(C\), directing all arcs between copies according to \(C\). For a digraph \(D\), its **out-neighborhood complex** \(\mathcal N^+(D)\) has as faces the subsets of \(N_D^+(v)\) for some vertex \(v\).

**Theorem.** Every \(T_k\) is a regular tournament on \(3^k\) vertices. For each integer \(k\ge2\), its out-neighborhood complex has integral homotopy type
\[
\mathcal N^+(T_k)\simeq
\left(\bigvee_{j=1}^{k-2}\bigvee^{3^{j-1}}S^j\right)
\vee\bigvee^{7\cdot3^{k-2}}S^{k-1}.
\]
The first wedge is empty for \(k=2\). Thus the reduced integral homology is free and nonzero in *every* degree from \(1\) through \(k-1\) (for \(k\ge3\)); all other reduced groups vanish. In particular,
\[
\mathcal N^+(T_2)\simeq\bigvee^7S^1,\qquad
\mathcal N^+(T_3)\simeq S^1\vee\bigvee^{21}S^2,\qquad
\mathcal N^+(T_4)\simeq S^1\vee\bigvee^3S^2\vee\bigvee^{63}S^3.
\]
The stronger transfer statement proved below is that for **every** finite tournament \(U\) on at least two vertices, with a chosen basepoint in the nonempty complex \(\mathcal N^+(U)\),
\[
\mathcal N^+(C[U])\simeq S^1\vee\bigvee^3\Sigma\mathcal N^+(U),
\]
where \(\Sigma\) is reduced suspension. The transfer statement is the structural ingredient of the single family classification above.

## Assumptions and scope
Tournaments are finite, loop-free, with exactly one directed arc for each unordered pair of distinct vertices. The lexicographic product uses all arcs between consecutive blocks of the outer directed cycle. No homology coefficients are suppressed: the theorem describes ordinary homotopy types, hence the *integral* homology and fundamental group. For the transfer lemma, \(U\) must have at least two vertices so that \(\mathcal N^+(U)\) has a geometric vertex. The nested family starts at the three-cycle, whose neighborhood complex consists of exactly three isolated vertices.

## Proof
**1. An exact three-cone cover.** Let \(U\) have vertex set \(B\), write \(B_i=\{i\}\times B\) for its three copies, and let \(A_i\cong\mathcal N^+(U)\) be the corresponding complex on \(B_i\). Every vertex \((i,u)\) of \(C[U]\) has
\[
N^+_{C[U]}(i,u)=\bigl(\{i\}\times N_U^+(u)\bigr)\sqcup B_{i+1},
\]
with indices modulo \(3\). Consequently the entire neighborhood complex is the union
\[
X=K_0\cup K_1\cup K_2,\qquad K_i=A_i*\Delta(B_{i+1}),
\]
where \(\Delta(B_{i+1})\) is the full simplex on the next block. Each \(K_i\) is contractible, as it is a join with a nonempty simplex. The only nonempty geometric pair intersections are
\[
|K_i|\cap|K_{i+1}|=|A_{i+1}|,
\]
and the triple geometric intersection is empty. The set-theoretic intersection of all three abstract complexes consists solely of the empty face; this is *not* a geometric intersection point.

**2. The graph-of-spaces homotopy equivalence.** All inclusions in this finite simplicial cover are cofibrations. Because there is no nonempty triple intersection, its ordinary union is modeled by the homotopy colimit of the three vertex spaces \(K_i\) and three edge spaces \(A_i\), with the natural two inclusions at each edge. Objectwise replacement of the contractible \(K_i\) by points preserves this homotopy colimit. The resulting CW space consists of three vertices joined cyclically by three cylinders \(|A_i|\times[0,1]\), with each entire end of each cylinder collapsed to its corresponding vertex. Select a point in each \(|A_i|\); its interval gives a distinguished path between the adjacent vertices. These three paths form a circular one-skeleton. Relative to this circular one-skeleton, each cylinder contributes the reduced suspension \(\Sigma|A_i|\), attached at a point: collapse a spanning tree of the three distinguished paths, then apply the usual cylinder/suspension CW quotient. Equivalently, use the homotopy-pushout description with the three nullhomotopic edge-to-vertex maps. Therefore
\[
|X|\simeq S^1\vee\Sigma|A_0|\vee\Sigma|A_1|\vee\Sigma|A_2|.
\]
This argument also applies when \(|A_i|\) is disconnected: the reduced suspension records the additional loops contributed by its extra components. In particular, three discrete points have reduced suspension homotopy equivalent to two circles.

**3. Base case and recurrence.** The out-neighborhoods in \(C\) are the three distinct singleton sets, so \(\mathcal N^+(T_1)\) is a set of three points, homotopy equivalent (as a based space) to \(\bigvee^2S^0\). The transfer equivalence yields
\[
\mathcal N^+(T_2)\simeq S^1\vee\bigvee^{3\cdot2} S^1=\bigvee^7 S^1.
\]
For every \(k\ge2\), the transfer equivalence gives a recurrence on wedge multiplicities: one fresh circle, plus three suspended copies of every sphere at the preceding stage. The formula in the finding follows by induction. Indeed, the top multiplicity starts at \(7\) for \(k=2\) and triples at every subsequent stage, while a fresh circle introduced at stage \(k\) contributes \(3^{j-1}\) spheres in degree \(j\) at stage \(k+j-1\), until it becomes part of the top multiplicity. This proves all homotopy and integral-homology assertions, not merely the Euler characteristics.

**4. Regularity.** If \(U\) is regular of odd order \(m\), every vertex in \(C[U]\) has \(m+(m-1)/2=(3m-1)/2\) outgoing arcs. Starting from the regular three-cycle, induction shows that \(T_k\) has \(3^k\) vertices and degree \((3^k-1)/2\), as required.

## Verification
The accompanying standalone program `verify_neighborhood.py` independently builds tournaments from their directed adjacency sets, enumerates all out-neighborhood faces, and calculates reduced mod-two Betti numbers by explicit boundary elimination. It checks the cases \(C\), \(C[\text{transitive three-vertex tournament}]\), \(C[C]\), and \(C[R_5]\) (where \(R_5\) is the regular cyclic five-vertex tournament). The computed Betti dictionaries are, respectively, \(\{0:2\}\), \(\{1:1\}\), \(\{1:7\}\), and \(\{1:1,2:3\}\). It separately enumerates all \(130306\) faces of \(T_3\) (including the empty face) and confirms reduced Euler characteristic \(20\), agreeing with \(S^1\vee\bigvee^{21}S^2\); no full boundary-rank computation is claimed for that case. The second program `verify_cover.py` directly checks the exact cone-union and pair-intersection identities, including their absence of nonempty triple intersections, for all four substitution examples. Both programs use the standard Python library only. Their finite checks supplement, but do not replace, the proof for arbitrary \(k\).

## Relationship to prior work
Dochtermann and Singh introduced the directed out-neighborhood complex and identified its homotopy type with that of the directed-edge Hom complex; their Section 4 also constructs a directed Mycielskian whose neighborhood complex suspends once, and their Section 5 constructs tournaments with individual prescribed sphere homotopy types [1]. Those results do not give the three-cone lexicographic transfer formula or simultaneous nonzero homology in all the stated degrees within a recursively defined *regular* family. Govc, Levi, and Smith studied tournaplexes and directed flag complexes [2], distinct from out-neighborhood complexes. A publicly available 2026 computation of directed **flag** complexes of three-block cyclic tournament substitutions treats some related graphs, but its simplex criterion is transitive subtournaments rather than common out-neighbors [3]; its classification does not imply the present homotopy formula. For instance, even at the nine-vertex example, the flag complex has homology in degrees \(1,2,3\), whereas the out-neighborhood complex here is a wedge of seven circles.

## Limitations
This is a homotopy classification only for the stated lexicographically iterated tournaments and the general one-step transfer construction. It does not classify their directed flag complexes, equivariant homology representations, persistence modules, or arbitrary regular tournaments. The source comparison cannot rule out an unindexed equivalent homotopy-pushout calculation or a general theorem not retrieved under the searched terminology. No independent mathematical audit has been performed. The computational checks at small sizes do not establish the unlimited-parameter statement; that rests on the exact cover and homotopy-colimit proof.

## References
1. A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948, first submitted 2021-08-24; *European Journal of Combinatorics* 110 (2023), article 103704. In particular, Definitions 4.1 and the results of Sections 4–5.
2. D. Govc, R. Levi, and J. P. Smith, *Complexes of tournaments, directionality filtrations and persistent homology*, arXiv:2003.00324, first submitted 2020-02-29; *Journal of Applied and Computational Topology* 5 (2021), 313–337.
3. *A lexicographic infinite family of regular tournament flag complexes*, public mathematical research note (2026). Its main result concerns the directed flag functor, not the out-neighborhood functor.
