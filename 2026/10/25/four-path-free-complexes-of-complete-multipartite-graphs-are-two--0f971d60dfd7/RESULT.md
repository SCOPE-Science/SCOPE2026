# Four-path-free complexes of complete multipartite graphs are two-sphere wedges

## Finding
Let \(r\ge 3\) and let \(n_1,\ldots,n_r\) be arbitrary positive integers. Write \(G=K_{n_1,\ldots,n_r}\), \(N=\sum_i n_i\), and
\[
 e_j=\sum_{1\le i_1<\cdots<i_j\le r}n_{i_1}\cdots n_{i_j}\quad(j=2,3).
\]
Let \(\operatorname{PF}_4(G)\) be the simplicial complex of vertex subsets whose induced graph contains no subgraph isomorphic to the four-vertex path \(P_4\). Here *subgraph* does not require the path to be induced. Then
\[
 \operatorname{PF}_4(G)\simeq\bigvee^{\,e_2+e_3-(r-1)(N-1)} S^2.
\]
A zero-fold wedge is a point. In particular, all reduced integral homology is free and concentrated in degree two, with rank \(e_2+e_3-(r-1)(N-1)\), and the fundamental group is trivial.

## Assumptions and scope
The graph is finite, simple and complete multipartite, with at least three **nonempty** parts, and every part size is unrestricted above. All face conditions use the ordinary (not necessarily induced) four-vertex path. There is no assumption of shellability or of equal part sizes. This is an infinite-family, nonequivariant integral homotopy statement, not a claim for \(P_t\) when \(t\ne4\).

## Proof
**1. Face classification.** Let \(V_1,\ldots,V_r\) be the graph parts, and set \(D(W)=\{\varnothing\}\cup\{\{v\}:v\in W\}\), the discrete vertex complex. Put
\[
 T=\left(D(V_1)*\cdots*D(V_r)\right)^{(2)},\qquad
 F_i=\Delta(V_i)*D(V\setminus V_i).
\]
The superscript \((2)\) denotes the ordinary two-skeleton; \(\Delta(V_i)\) is the full simplex on that part. We claim
\[
 \operatorname{PF}_4(G)=T\cup\bigcup_{i=1}^r F_i.
\]
Indeed, a vertex subset contained in one part has no edges; a subset with vertices in two parts and at most one in one of them induces a star (possibly with isolated vertices), with no four-vertex path. A subset with at most one vertex in each of at most three parts has at most three vertices. Conversely, two occupied parts each containing at least two vertices contain a copy of \(K_{2,2}\), and hence a four-vertex path. Three occupied parts with at least two vertices in one part contain the path \(a_1-b-a_2-c\), with \(a_1,a_2\) in the repeated part and \(b,c\) in two other parts. Four occupied parts contain a four-vertex path by taking one vertex from each. This exhausts the occupancy patterns and establishes the identity. It also independently recovers the \(t=4\) specialization of the structural decomposition in the first reference.

**2. Intersections and simple connectivity.** Every \(F_i\) is contractible, since it is the join of a nonempty simplex with a discrete complex. Define \(B_i=F_i\cap T\). Its vertices are all \(N\) vertices and its edges are exactly those joining \(V_i\) to its complement, so
\[
 B_i\cong K_{n_i,N-n_i},\qquad
 \operatorname{rank} H_1(B_i;\mathbb Z)=(n_i-1)(N-n_i-1).
\]
In particular, each \(B_i\) is connected. For distinct \(i,j\), a face in \(F_i\cap F_j\) cannot use two vertices of either of those parts, and cannot use two vertices outside both; it therefore has at most two vertices and uses different parts. Thus \(F_i\cap F_j\subseteq T\). Consequently, for any ordering of the \(F_i\), the intersection of \(F_i\) with \(T\cup\bigcup_{j<i}F_j\) is precisely \(B_i\).

The full join \(J=D(V_1)*\cdots*D(V_r)\) is simply connected because it is the join of at least three nonempty discrete spaces (possibly contractible singleton spaces). Attaching cells of dimension at least three does not change \(\pi_1\); hence its two-skeleton \(T\) is simply connected. Adjoining each contractible \(F_i\) along the connected \(B_i\) preserves simple connectivity by van Kampen. Therefore \(K=\operatorname{PF}_4(G)\) is simply connected.

**3. Integral homology.** The complex \(T\) is two-dimensional and simply connected. Its numbers of vertices, edges and triangles are respectively \(N,e_2,e_3\), so its reduced integral homology vanishes except for
\[
 \widetilde H_2(T;\mathbb Z)\cong\mathbb Z^{N-e_2+e_3-1}.
\]
When \(F_i\) is adjoined, Mayer–Vietoris with \(F_i\) contractible and \(B_i\) connected, one-dimensional and with free integral first homology, gives the split short exact sequence
\[
 0\longrightarrow H_2(K_{i-1};\mathbb Z)
 \longrightarrow H_2(K_i;\mathbb Z)
 \longrightarrow H_1(B_i;\mathbb Z)\longrightarrow0,
\]
where \(K_0=T\) and \(K_i=K_{i-1}\cup F_i\). It also gives \(H_q(K_i;\mathbb Z)=0\) for every \(q\ge3\), and \(H_1(K_i;\mathbb Z)=0\). Thus
\[
 \operatorname{rank}\widetilde H_2(K;\mathbb Z)
 =N-e_2+e_3-1+\sum_i(n_i-1)(N-n_i-1).
\]
As \(\sum_i n_i(N-n_i)=2e_2\), the sum simplifies exactly to \(e_2+e_3-(r-1)(N-1)\). Each extension splits over the integers because its quotient is free abelian, proving torsion-freeness.

**4. Homotopy conclusion.** The Hurewicz map identifies \(\pi_2(K)\) with the free group \(H_2(K;\mathbb Z)\). Choose based sphere maps representing an integral basis, forming a map from the asserted wedge of two-spheres to \(K\). Both spaces are simply connected, and this map induces isomorphisms on all integral homology groups. The simply connected homology version of Whitehead's theorem makes the map a homotopy equivalence. The nonnegative sphere multiplicity is also manifest from the unsimplified sum of nonnegative ranks.

## Verification
The standalone file `verifier.py` independently enumerates actual four-vertex paths in the finite multipartite graphs, compares all subsets with the occupancy classification in Step 1, constructs every simplicial boundary over \(\mathbb F_2\), and computes all reduced Betti numbers by bitwise Gaussian elimination. It checks **336 ordered part-size tuples** having three to five parts and total order at most nine; these include nonpure examples with simplex dimensions exceeding two. All 336 checks agree with the rank formula and show no mod-two homology in other degrees. The text output is `verifier_output.txt`; run with `python3 verifier.py` using only the Python standard library. These finite tests corroborate but do not replace the infinite proof above; the integral and homotopy conclusions come from Mayer–Vietoris, van Kampen, Hurewicz and Whitehead.

Examples: \(\operatorname{PF}_4(K_{2,2,2})\simeq\bigvee^{10}S^2\), and \(\operatorname{PF}_4(K_{3,3,1})\simeq\bigvee^{12}S^2\). In the latter example, existing results also establish a failure of sequential Cohen–Macaulayness, illustrating that a sphere-wedge homotopy type need not arise from shellability.

## Relationship to prior work
Deshpande–Goyal–Sawant, arXiv:2607.05358v1, Lemma 3.5 gives a general decomposition of multipartite path-free complexes, including the specialized occupancy decomposition used here. Their Theorem 4.3 determines all \(t\) for **bipartite** graphs, and Theorem 4.5 determines \(t=3\) for multipartite graphs. Their Conjecture 4.7 asks for sphere-wedge homotopy types for arbitrary \(t\) and arbitrary complete multipartite graphs. The result here proves the full four-path case for **three or more** parts, with an explicit integral multiplicity. This is not an assertion of the full conjecture.

Deshpande–Singh, arXiv:2001.05448v2, Theorem 3.5 classifies higher independence complexes, a distinct family. In particular, \(\operatorname{PF}_4(K_{3,3,1})\) contains the four-vertex star with three vertices from one part and one from another, whereas the three-independence complex omits it. The published higher-independence classification therefore does not imply this statement by equality of complexes. The bipartite specialization of the present rank formula agrees with the already published even-parameter formula and is **not claimed as new**.

## Limitations
No equivariant homotopy splitting, stronger simple-homotopy classification, or result for \(t\ge5\) is established. The result does not assert shellability. Complete originality against unpublished or unindexed manuscripts cannot be guaranteed. Computational checks cover finitely many small instances only; the theorem rests on the proof given here. A mathematical peer review independent of this manuscript has not yet been performed.

## References
1. P. Deshpande, S. Goyal and R. Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358v1 (first posted 2026-07-06), especially Lemma 3.5, Theorems 4.3 and 4.5, and Conjecture 4.7. https://arxiv.org/pdf/2607.05358v1
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v2, Theorem 3.5; J. Ramanujan Math. Soc. 36 (2021), 53–71. https://arxiv.org/pdf/2001.05448v2
3. A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, foundational results on van Kampen, Hurewicz and Whitehead theorems.
