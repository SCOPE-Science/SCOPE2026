# Mixed-dimensional neighborhood homotopy of complete-graph cycle products

## Finding
For every pair of integers \(m\geq4\) and \(n\geq5\), let \(G_{m,n}=K_m\mathbin{\square} C_n\) be the Cartesian product of a complete graph and a cycle. Its Lovász **open-neighborhood complex**, formed by all nonempty vertex subsets that have a common adjacent vertex, has homotopy type
\[
\mathcal N(G_{m,n})\simeq S^1\vee\bigvee^{n}S^{m-2}\vee\bigvee^{n(m^2-3m+1)}S^2.
\]
All wedge summands are based and connected. In particular the integral homology is torsion-free and the fundamental group is \(\mathbb Z\). When \(m=4\), the two kinds of two-sphere summands combine into exactly \(6n\) two-spheres; when \(m=5\), there are \(11n\) two-spheres and \(n\) three-spheres. No claim is made for \(m=3\) or \(n\le4\).

## Assumptions and scope
The graph has labeled vertices \(v_{a,i}\) for \(a\in\{0,\ldots,m-1\}\), \(i\in\mathbb Z/n\mathbb Z\), where distinct vertices are adjacent precisely if they have equal cycle coordinate and unequal color, or equal color and adjacent cycle coordinates. The neighborhood complex is **open**, so the center of a neighborhood is not included among its own neighbors. This is not the closed-neighborhood complex or the total cut complex.

Write \(R_i=\{v_{a,i}:0\le a<m\}\) and \(B_i=\partial\Delta(R_i)\cong S^{m-2}\), the boundary of the simplex on a single complete-graph layer. The proof constructs homotopy equivalences uniformly for all the stated integers; small finite calculations only corroborate them.

## Proof
**1. Exact simplices and the first collapse.** Each neighborhood of \(v_{a,i}\) is exactly
\[
F_{a,i}=(R_i\setminus\{v_{a,i}\})\cup\{v_{a,i-1},v_{a,i+1}\}.
\]
The complex is the union of the full simplices on these \(mn\) sets. Since \(n\ge5\), the pair \(P_{a,i}=\{v_{a,i-1},v_{a,i+1}\}\) occurs together in no other such neighborhood: the two vertices lie two steps apart along one color and have the unique common neighbor \(v_{a,i}\). Choose any \(h_{a,i}\in R_i\setminus\{v_{a,i}\}\). Among faces containing \(P_{a,i}\), pair \(P_{a,i}\cup A\) with \(P_{a,i}\cup A\cup\{h_{a,i}\}\) for every \(A\subseteq R_i\setminus\{v_{a,i},h_{a,i}\}\). In decreasing order of \(|A|\), these are actual elementary free-face collapses. Distinct centers use disjoint face sets. All faces containing both opposite-layer vertices disappear.

**2. The one-wing collapses.** Each remaining simplex meeting one vertex \(u=v_{a,i\pm1}\) and at least two vertices in \(R_i\) belongs to the unique neighborhood simplex centered at \(v_{a,i}\). Put \(H=R_i\setminus\{v_{a,i}\}\) and choose its pivot \(h=h_{a,i}\). Pair \(\{u\}\cup A\) with \(\{u,h\}\cup A\), for \(A\subseteq H\setminus\{h\}\) and \(|A|\ge2\), again in descending dimension. These too are free-face collapses, disjoint between wings. Exactly \(m-2\) triangles \(\{u,h,w\}\) remain in each of the \(2mn\) wings, where \(w\in H\setminus\{h\}\); each entire row boundary \(B_i\) remains intact.

**3. The collapsed core.** The resulting complex comprises the \(n\) row-boundary spheres \(B_i\), all interlayer edges \(\{v_{b,i},v_{a,i+1}\}\) with \(a\ne b\), and exactly \(2m(m-2)\) surviving triangles per consecutive-layer interface. There are no higher-dimensional mixed faces. Each interlayer triangle contains two edges between the adjacent rows and one edge inside a row. In the interface between layers \(i\) and \(i+1\), label its \(E=m(m-1)\) cross edges by ordered pairs \((b,a)\) with \(b\ne a\). A triangle identifies two cross edges sharing one endpoint, modulo a path in the corresponding \(B_i\) or \(B_{i+1}\). The surviving fan triangles connect all edges at each fixed endpoint by a star (one central edge and the remaining \(m-2\) edges). Thus the graph of these triangle relations is connected: it has the same connected components as the line graph of the connected crown graph \(K_{m,m}\) minus its diagonal matching. Select \(E-1\) triangles whose relations form a spanning tree on the cross edges.

**4. Relative cell cancellation and the wedge.** Because \(m\ge4\), every \(B_i\cong S^{m-2}\) is simply connected. Regard each interface as a relative CW complex attached to \(B_i\sqcup B_{i+1}\). The boundary of each selected tree triangle is homotopic, relative to these row spheres, to the difference of its two cross edges: the intervening row path has no nontrivial based loop in its row sphere. Attaching the selected \(E-1\) two-cells successively eliminates all but one cross one-cell by standard \(1\)-\(2\) CW cancellation along a rooted tree. The resulting base is the two row spheres connected by a bridge and is simply connected. Every unselected interface triangle therefore attaches by a null-homotopic circle and splits off an \(S^2\) summand. The number of these summands per interface is
\[
\lambda_m=2m(m-2)-(E-1)=m^2-3m+1.
\]
These constructions can be performed separately on all \(n\) consecutive interfaces, leaving one bridge from each \(B_i\) to \(B_{i+1}\). The bridges form a single cycle, so the base is \(S^1\vee\bigvee^n B_i\). All the \(n\lambda_m\) other two-cells were null-attached within their own interfaces, and hence split off the asserted two-spheres. This proves the formula, including the integral and fundamental-group conclusions.

## Verification
Run `python3 verify_neighborhood_cycle_products.py` using Python 3 without external libraries. It reconstructs the open-neighborhood simplices **from graph adjacency**, executes and individually checks the two families of genuine elementary free-face collapses, compares the exact remaining faces against the stated core, checks the connectivity of the crown-graph cross-edge relations, and computes binary boundary ranks of the original complexes. For every \(4\le m\le7\) and \(5\le n\le8\), all sixteen cases match the theorem, with 23,920 verified collapses in total. This finite verification is not the proof for arbitrary \(m,n\).

## Relationship to prior work
Matsushita [1] relates the fundamental group of a neighborhood complex to a graph-theoretic fundamental group. That correspondence alone does not give the sphere dimensions or multiplicities here. Shukla [2] determines neighborhood-complex homotopy types for graphs of maximum degree at most three and for four-regular circulant graphs; the graphs here are \((m+1)\)-regular, of degree at least five, so these hypotheses do not include them. Chauhan--Shukla--Vinayak [3] compute a **total two-cut complex** for the same Cartesian-product graph family; that complex has facets complementary to independent pairs, whereas an open-neighborhood facet is the common neighbor set specified in step 1. The objects and their stated homotopy types differ: [3] has spheres in degree \(mn-4\), not the mixture of degrees \(1,2,m-2\) established above. Other related calculations for rook graphs \(K_m\square K_n\) or low-degree toroidal grids have different factors or hypotheses. No equivalence or domination of the present full statement was found in the checked literature; an unindexed equivalent formulation remains possible.

## Limitations
The hypothesis \(n\ge5\) guarantees unique centers for opposite-layer pairs, and \(m\ge4\) makes each row boundary simply connected; the argument does not silently extend past these boundaries. The theorem is a nonequivariant homotopy classification and does not classify homeomorphism types, natural symmetry actions, or persistence filtrations. The independent verification is finite, and the bibliography check is not a universal novelty certificate.

## References
[1] T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (first submitted 2012-10-10), published in J. Math. Sci. Univ. Tokyo 24 (2017), 321–353; primary MSC 55Q05.

[2] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (first submitted 2018-02-13), Electron. J. Combin. 26 (2019), P2.4.

[3] P. Chauhan, S. Shukla, K. Vinayak, *Total 2-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486 (first submitted 2025-12-04), particularly Theorem 1.5; this concerns a different simplicial complex.
