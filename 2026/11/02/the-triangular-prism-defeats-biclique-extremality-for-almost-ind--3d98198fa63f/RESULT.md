# The triangular prism defeats biclique extremality for almost-independent sets

## Finding
Let \(G\) be a finite simple graph, let \(e_G(S)\) be the number of edges induced by a vertex set \(S\subseteq V(G)\), and put
\[
F_G(z)=\sum_{S\subseteq V(G)}z^{e_G(S)},\qquad N_G(t)=\#\{S\subseteq V(G):e_G(S)\le t\}.
\]
Let \(B=K_{3,3}\) and let \(P=K_3\mathbin{\square}K_2\) be the triangular prism. Their induced-edge generating polynomials satisfy the **exact identity**
\[
F_P(z)-F_B(z)=-2(1-z)^3.
\]
Consequently
\[
N_P(1)=28>24=N_B(1).
\]
For \(d=3,n=6,\gamma=1/18\), the convention \(e_G(S)\le\gamma dn\) becomes \(e_G(S)\le1\). Therefore the prism is a counterexample to the universal biclique-extremality proposal for the number of almost-independent subsets in Carenini's Question 1.3. This is the **smallest admissible order** for a counterexample when \(d\ge2\) and \(2d\mid n\).

Moreover, these are the only two isomorphism classes of simple cubic graphs on six vertices. The sharp comparison of their counts at every integer threshold is
\[
N_P(t)-N_B(t)=\begin{cases}
-2,&t=0,\\
4,&t=1,\\
-2,&t=2,\\
0,&t\ge3,
\end{cases}\qquad (t\in\mathbb Z_{\ge0}).
\]
Thus the prism uniquely maximizes \(N_G(1)\) up to isomorphism among all six-vertex cubic graphs, while the biclique uniquely maximizes for thresholds zero and two. For thresholds at least three their counts tie.

## Assumptions and scope
Graphs are simple and undirected; vertex subsets may be empty. The degree is \(d=3\), the order is \(n=6\), and the two candidate graphs are considered on unlabelled isomorphism types (the enumerator counts vertex subsets, not graph labellings). The main counterexample concerns **cumulative** counts by number of induced edges, not the independent-set count alone, and not a size-conditioned count. All threshold statements use integer \(t\ge0\); for a real threshold \(\gamma\ge0\), put \(t=\lfloor18\gamma\rfloor\). Since each six-vertex cubic graph has nine edges, no larger thresholds need separate consideration.

## Proof
**The two polynomials.** For the bipartite graph \(B\), if \(a\) of the three left-side vertices and \(b\) of the three right-side vertices are chosen, the subset induces exactly \(ab\) edges. Consequently,
\[
F_B(z)=\sum_{a,b=0}^{3}\binom3a\binom3b z^{ab}
=15+9z+18z^2+6z^3+9z^4+6z^6+z^9.
\]
For the prism, denote its two triangular layers by copies of \([3]\), with the three corresponding vertices joined by matching edges. Each vertex subset is uniquely determined by \(A,B\subseteq[3]\), one subset in each layer. It induces exactly
\[
\binom{|A|}{2}+\binom{|B|}{2}+|A\cap B|
\]
edges, since its internal edges are precisely those within the two triangles plus matching edges with both endpoints chosen. Therefore,
\[
F_P(z)=\sum_{A,B\subseteq[3]}z^{\binom{|A|}{2}+\binom{|B|}{2}+|A\cap B|}
=13+15z+12z^2+8z^3+9z^4+6z^6+z^9.
\]
The finite sums are explicit and can be evaluated by partitioning according to \(|A|,|B|,|A\cap B|\). Subtraction proves \(F_P-F_B=-2+6z-6z^2+2z^3=-2(1-z)^3\). Summing coefficients up to a threshold proves the displayed phase diagram and the strict \(28>24\) inequality.

For an additional count independent of the full expansion, the biclique has \(15\) independent vertex subsets (all subsets of either bipartition class, with the empty set counted once) and \(9\) subsets spanning exactly one edge (choose one vertex from each class). The prism has \(13\) independent subsets (the empty set, six singletons, and six nonadjacent pairs) and \(15\) subsets spanning exactly one edge. Of the latter, nine are two-vertex edge endpoints; six are three-vertex subsets consisting of a within-triangle edge together with the unique nonmatching vertex in the opposite triangle. Hence the same comparison is \(13+15=28\) versus \(15+9=24\).

**Completeness on six vertices.** A simple graph on six vertices is 3-regular exactly when its complement is 2-regular. A simple 2-regular graph is a disjoint union of cycles of length at least three. The only partitions of six into integers at least three are \(6\) and \(3+3\). Thus the complement is either \(C_6\) or \(C_3\sqcup C_3\). The respective original graphs are isomorphic to the triangular prism and to \(K_{3,3}\). In particular, the above phase diagram is the global comparison for the full six-vertex cubic class, not merely for two selected examples.

**Minimal order.** For \(d\ge2\), if \(2d\mid n\) and \(n<6\), then the only admissible nonempty parameter pair is \((d,n)=(2,4)\). Every simple 2-regular graph on four vertices is \(C_4\cong K_{2,2}\), so a different graph cannot beat the biclique benchmark there. At \((d,n)=(3,6)\), the prism supplies the strict counterexample. This proves the stated minimum order.

**Compatibility with weighted inequalities.** For each real \(z\in[0,1]\), \(F_B(z)-F_P(z)=2(1-z)^3\ge0\). Therefore the example does not contradict the known extremal inequality for the antiferromagnetic two-spin partition function. Integrating or taking cumulative coefficients is a different operation: pointwise generating-function domination need not imply domination of every partial sum of coefficients.

## Verification
The included standalone `verify.py` uses only the Python standard library. It independently computes each polynomial (i) by literally enumerating all \(64\) subsets and their induced edges and (ii) via the two closed-form combinatorial constructions given above. It verifies all ten coefficients and threshold differences. It also enumerates all \(\binom{15}{9}=5005\) nine-edge graphs on a fixed six-vertex set, identifies the \(70\) cubic graphs, and checks that exactly \(10\) have complementary cycles \((3,3)\) and \(60\) have complementary cycle \((6)\), each with the asserted polynomial. The script terminates with `VERIFY_OK` if every assertion passes. The mathematical proof is self-contained and does not rely on treating a sample of graphs as exhaustive: the classification of 2-regular complements proves exhaustiveness.

## Relationship to prior work
Gaia Carenini, *Counting almost independent sets in regular graphs* (first public 2026-09-22, arXiv:2609.28527v1), studies \(i_\gamma(G)=\#\{S:e_G(S)\le\gamma dn\}\) for regular graphs. Its Question 1.3 asks whether disjoint unions of \(K_{d,d}\) maximize this count for all \(\gamma\ge0\), when the divisibility condition permits such a union. The present six-vertex computation gives a definite **negative answer to the unrestricted formulation**, even though the paper's asymptotic upper bounds remain unaffected.

Sah, Sawhney, Stoner and Zhao's *A reverse Sidorenko inequality* (arXiv:1809.09462) establishes relevant pointwise weighted partition-function comparisons. This does not imply the conjectured cumulative coefficient inequality: the present identity demonstrates directly that pointwise domination and cumulative-count domination can coexist in opposite directions. Zhao's *The Number of Independent Sets in a Regular Graph* (arXiv:0909.3354) controls the coefficient at zero induced edges, where \(K_{3,3}\) indeed wins \(15\) to \(13\).

The precise counterexample, complete six-vertex cubic threshold diagram, and minimal-order observation are the claimed contribution. No assertion is made that the elementary polynomial identity or graph classification was historically unknown in every possible terminology.

## Limitations
The result disproves only the universal extremal statement for cumulative almost-independent-set counts. It does not disprove or sharpen the quantitative large-graph upper bounds in the motivating paper, nor does it classify maximizers for other values of \(d,n\). It does not contradict the partition-function inequality or the independent-set extremal theorem. Historical priority of the small counterexample has been checked against targeted mathematical sources, but cannot be certified exhaustively.

## References
1. G. Carenini, *Counting almost independent sets in regular graphs*, arXiv:2609.28527v1, first posted 2026-09-22, https://arxiv.org/abs/2609.28527.
2. A. Sah, M. Sawhney, D. Stoner and Y. Zhao, *A reverse Sidorenko inequality*, arXiv:1809.09462, 2018, https://arxiv.org/abs/1809.09462.
3. Y. Zhao, *The Number of Independent Sets in a Regular Graph*, arXiv:0909.3354, 2009, https://arxiv.org/abs/0909.3354.
