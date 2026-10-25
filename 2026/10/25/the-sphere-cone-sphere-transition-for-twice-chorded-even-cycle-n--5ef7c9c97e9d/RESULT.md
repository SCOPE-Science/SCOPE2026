# The sphere–cone–sphere transition for twice-chorded even-cycle non-matching complexes

## Finding
For every integer \(t\ge 2\), let the cycle \(C_{2t}\) have vertices \(0,1,\ldots,2t-1\), with indices modulo \(2t\). Put
\[
G_t^{(0)}=C_{2t},\qquad
G_t^{(1)}=C_{2t}+\{0,2\},\qquad
G_t^{(2)}=C_{2t}+\{0,2\}+\{1,3\}.
\]
For any finite graph \(G\), let \(\operatorname{NM}_t(G)\) be the simplicial complex with vertex set \(E(G)\) and faces those edge subsets that contain no matching of size \(t\).

**Theorem (sharp three-stage transition).** For every integer \(t\ge2\), the following are integral homotopy equivalences:
\[
\boxed{
\operatorname{NM}_t(G_t^{(0)})\simeq S^{2t-3},\qquad
\operatorname{NM}_t(G_t^{(1)})\simeq\mathrm{pt},\qquad
\operatorname{NM}_t(G_t^{(2)})\simeq S^{2t-2}.
}
\]
In particular, the map in reduced integral homology induced by the first edge insertion
\[
\widetilde H_{2t-3}(\operatorname{NM}_t(G_t^{(0)});\mathbb Z)
\longrightarrow
\widetilde H_{2t-3}(\operatorname{NM}_t(G_t^{(1)});\mathbb Z)
\]
is the zero map from \(\mathbb Z\) to \(0\). The second chord restores nontrivial reduced homology, but in degree \(2t-2\), not degree \(2t-3\).

## Assumptions and scope
All graphs are finite, simple and undirected. The integer \(t\) ranges over **all** integers at least two; there is no finite upper cutoff. The chords are inserted sequentially as indicated, so the intermediate and final graphs are non-bipartite. The term “non-matching complex” concerns subgraphs **without** a size-\(t\) matching; it must not be confused with the ordinary matching complex or a bounded-degree matching complex. Empty faces are retained in every simplicial join.

For a finite, nonempty set \(F\), write \(\Delta^F\) for the full simplex on \(F\) and \(\partial\Delta^F\) for its boundary. For \(|F|\ge2\), the boundary \(\partial\Delta^F\) is \(S^{|F|-2}\), and the sphere join identity is \(S^a*S^b\cong S^{a+b+1}\). The boundary on a singleton \(\partial\Delta^{\{v\}}\) consists only of the empty face and is the neutral factor for simplicial joins. Cases where this convention matters are treated explicitly below.

## Proof
Label the original cycle edges \(e_i=\{i,i+1\}\), \(0\le i<2t\), with indices modulo \(2t\), and set
\[
A=\{e_0,e_2,\ldots,e_{2t-2}\},\qquad
B=\{e_1,e_3,\ldots,e_{2t-1}\}.
\]
Because the graphs under consideration have exactly \(2t\) vertices, their size-\(t\) matchings are precisely their perfect matchings. In \(C_{2t}\), a perfect matching containing \(e_0\) is forced to contain all even-indexed edges, and one avoiding \(e_0\) is forced to contain all odd-indexed edges. Thus the complete list is \(A,B\), and these use disjoint subsets of the complex vertex set. A face avoids a size-\(t\) matching exactly when it does not contain \(A\) or \(B\), so
\[
\operatorname{NM}_t(G_t^{(0)})
=\partial\Delta^A*\partial\Delta^B
\cong S^{t-2}*S^{t-2}
\cong S^{2t-3}.
\]

Let \(x=\{0,2\}\). The original cycle is bipartite, with even and odd labels as its two parts, each of cardinality \(t\). Any matching using \(x\) covers two even vertices and no odd vertex with that edge, while its other cycle edges each cover one vertex of each parity. It cannot be perfect. Consequently \(G_t^{(1)}\) still has exactly the two perfect matchings \(A,B\). The new edge \(x\) is therefore a cone vertex:
\[
\operatorname{NM}_t(G_t^{(1)})
=\partial\Delta^A*\partial\Delta^B*\Delta^{\{x\}},
\]
which is contractible. This also shows directly that the first inclusion annihilates the fundamental cycle in the old degree.

Now put \(y=\{1,3\}\), and let
\[
T=\{e_4,e_6,\ldots,e_{2t-2}\},\quad
U=\{e_0,e_2\},\quad
W=\{x,y\}.
\]
When \(t=2\), the set \(T\) is empty. The sets \(B,T,U,W\) are mutually disjoint, and \(A=T\cup U\). A perfect matching of \(G_t^{(2)}\) containing exactly one of \(x,y\) is impossible by parity. One containing both must pair the remaining vertices \(4,5,\ldots,2t-1\) using the original cycle edges. Those remaining vertices induce an even path and admit the single perfect matching \(T\). Thus **the complete list** of size-\(t\) matchings of the final graph is
\[
A=T\cup U,\qquad B,\qquad C=T\cup W.
\]
It follows that
\[
\operatorname{NM}_t(G_t^{(2)})
=\partial\Delta^B*L_t,
\]
where \(L_t\) consists of all subsets of \(T\cup U\cup W\) that contain neither \(T\cup U\) nor \(T\cup W\).

For \(t=2\), \(T=\varnothing\). The two forbidden sets are simply \(U\) and \(W\), so
\[
L_2=\partial\Delta^U*\partial\Delta^W
\cong S^0*S^0\cong S^1.
\]
For \(t\ge3\), the nonempty set \(T\) allows the exact decomposition
\[
L_t=
\underbrace{\partial\Delta^T*\Delta^{U\cup W}}_{X}
\ \cup\ 
\underbrace{\Delta^T*\partial\Delta^U*\partial\Delta^W}_{Y}.
\]
Indeed, either a face misses at least one element of \(T\) (and then the two forbidden sets are automatically avoided), or it contains all of \(T\) (and must miss at least one element of each of \(U,W\)). Both \(X\) and \(Y\) are contractible: respectively they have the nonempty simplex factors \(\Delta^{U\cup W}\) and \(\Delta^T\). Their intersection is **exactly**
\[
X\cap Y
=\partial\Delta^T*\partial\Delta^U*\partial\Delta^W
\simeq S^{t-2}.
\]
To verify the final equivalence at the lower boundary, if \(t=3\) then \(T\) is a singleton; its boundary contributes only the empty face, and the intersection is \(\partial\Delta^U*\partial\Delta^W\cong S^1\). If \(t\ge4\), the three boundary factors are spheres of dimensions \(t-4,0,0\); their join is \(S^{t-2}\).
As the inclusions of simplicial subcomplexes are cofibrations, their ordinary union is a homotopy pushout. A union of two contractible CW complexes along this nonempty intersection has the homotopy type of its suspension. Therefore
\[
L_t\simeq\Sigma S^{t-2}\simeq S^{t-1}.
\]
This also agrees with the separate case \(t=2\). Finally, since \(|B|=t\),
\[
\operatorname{NM}_t(G_t^{(2)})
\simeq S^{t-2}*S^{t-1}\simeq S^{2t-2}.
\]
Every step is an integral homotopy equivalence. In particular, there is no use of field-dependent homology to infer a sphere. This proves the theorem. \(\square\)

## Verification
The standalone `check_bichord_nonmatching.py` independently enumerates all size-\(t\) matchings of all three graphs for each \(2\le t\le7\) directly from the edge incidences, enumerates the simplicial face sets, and checks that the only minimal nonfaces are exactly the two, two, and three matchings listed in the proof. Across eighteen cases it enumerates 148,638 nonempty faces and checks the reduced Euler characteristics. In the twelve cases with \(2\le t\le5\) it independently computes every reduced mod-two Betti number by explicit boundary-matrix reduction. Each result agrees with the theorem. Its output ends in `REPLAY_OK`. The general theorem is proved by the combinatorial decomposition above, not inferred from these finite checks.

The verifier is self-contained, uses only the Python standard library, and is accompanied by its actual output in `check_bichord_nonmatching.out`. Run `python3 check_bichord_nonmatching.py` in a directory containing the file.

## Relationship to prior work
Shan and Wang [1], public September 2, 2026, proved that **edge additions preserving bipartiteness** induce injection on reduced homology in degree \(2t-3\), and recalled the homotopy-sphere calculation for cycles (their Theorem 2.1 and Lemma 2.2). The present three-stage family demonstrates a sharp obstruction when bipartiteness is abandoned, and additionally computes the integral sphere in a *new degree* after a second odd-cycle-forming chord. The cycle's initial sphere is already known and is included solely as the baseline, not as an original result.

Linusson, Shareshian and Welker [2] calculated nonmatching complexes for complete graphs and complete bipartite graphs. The final graph when \(t=2\) is \(K_4\), so that individual case is not new. For \(t\ge3\), the two-chorded sparse cycle is neither a complete nor a complete bipartite graph. Holmsen and Lee [3] proved general homological vanishing bounds, which neither determine this exact integral homotopy type nor imply the sphere–cone–sphere sequence. The new contribution is the uniform all-\(t\) transition and explicit join/pushout proof for sparse non-bipartite graphs.

## Limitations
The theorem concerns only the stated positions of two consecutive length-two chords of an even cycle. It does not claim any classification for arbitrary chords, arbitrary non-bipartite graphs, or higher matchings than half the vertex count. The one-chord contractibility and two-chord sphere equivalence are proved for **all** \(t\ge2\); the finite verification range is merely supplemental. The oldest complete-graph results already imply the \(t=2\) final case, and the original cycle homotopy type is previously known. A literature comparison did not identify a statement subsuming the whole transition, but absence of such a statement from inspected sources is not a proof of global bibliographic uniqueness.

## References
1. J. Shan and Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley-Reisner ideals*, first public September 2, 2026; arXiv:2609.02621. https://arxiv.org/abs/2609.02621 . Relevant locations: Introduction, Theorem 2.1, Lemma 2.2, Theorem 2.3.
2. S. Linusson, J. Shareshian and V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345, public October 15, 2004. https://arxiv.org/abs/math/0410345 . Relevant locations: Theorems 1.1 and 1.4 and the definition of bounded-matching graph complexes.
3. A. F. Holmsen and S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270, public March 25, 2020. https://arxiv.org/abs/2003.11270 . Relevant locations: Introduction, Theorem 1.1 and the bipartite vanishing bound.
