# Integral homology and a perfect Morse model for the \(5\times5\) king-placement complex

## Finding

Let \(G=P_5\boxtimes P_5\) be the ordinary nonperiodic king-attack graph and let \(K=\operatorname{Ind}(G)\). The space \(K\) is 2-connected and has complete reduced **integral** homology

\[
\widetilde H_i(K;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{45},& i=3,\\
\mathbb Z^{32},& i=4,\\
\mathbb Z^{2},& i=5,\\
0,&\text{otherwise}.
\end{cases}
\]

There is a concrete acyclic discrete-Morse matching giving a CW model with one critical vertex, 45 critical three-cells, 32 critical four-cells and two critical five-cells. **Every integer Morse boundary coefficient is zero**. Hence \(\pi_3(K)\cong\mathbb Z^{45}\) by the Hurewicz theorem.

## Assumptions and scope

The 25 squares are \((r,c)\) with \(r,c\in\{0,1,2,3,4\}\), numbered \(5r+c\). Two *distinct* squares are adjacent in \(G\) when \(\max(|r-r'|,|c-c'|)=1\). There is no wraparound. A face of \(K\) is any set of pairwise nonadjacent squares; every cardinality is permitted. Chains use increasing vertex labels for orientations and coefficients in \(\mathbb Z\). The graph equals the strong product of two paths, rather than the ordinary Cartesian grid graph. Here 2-connected means path-connected with vanishing \(\pi_1\) and \(\pi_2\).

## Proof

**1. Exact face census.** For a set of already selected squares and an allowed mask, choose the smallest allowed square, include it, and restrict later choices to allowed squares not attacked by it. Enumerating all branches gives precisely 6,426 nonempty faces. The face numbers by simplex dimension \(0\) through \(8\) are

\[
(25,228,964,1987,1974,978,242,27,1).
\]

The recursive algorithm and its independent checks are in `verify_kings5.py`.

**2. An acyclic discrete-Morse matching.** Work on the nonempty-face poset. Starting with all faces, repeatedly identify maximal surviving simplices. If a maximal simplex \(\tau\) has a codimension-one facet \(\sigma\) whose *only* surviving codimension-one coface is \(\tau\), match \((\sigma,\tau)\) and remove both from consideration. If there are no such pairs anywhere, mark one maximal simplex critical and remove it alone. The priority choices (fixed pseudorandom tie-break generator and dimensions) are specified in the code and make this an entirely reproducible finite certificate. Every matched pair is a free maximal-facet pair in the then-surviving subcomplex, and every singly removed critical face is maximal. Accordingly the resulting matching is acyclic; independently, orient paired Hasse edges upwards and all other Hasse edges downwards, and topologically sort this directed graph. The verifier visits all 6,426 faces, certifying no directed cycles.

There are exactly 3,173 matched pairs and 80 critical simplices, distributed as

\[
(c_0,c_3,c_4,c_5)=(1,45,32,2),
\]

with every other \(c_i=0\). Discrete Morse theory therefore supplies a CW model with precisely those cell counts.

**3. Exact integral Morse boundary.** For every oriented simplex \([v_0,\ldots,v_k]\), construct \(\partial[v_0,\ldots,v_k]=\sum_{j=0}^k(-1)^j[v_0,\ldots,\widehat{v_j},\ldots,v_k]\). For each matched pair \((\sigma,\tau)\), let \(s=\langle\partial\tau,\sigma\rangle\). The verifier checks \(s\in\{+1,-1\}\) *at every elimination*, and for every remaining boundary column \(h\) of the same dimension replaces

\[
\partial h\ \longleftarrow\ \partial h -
\frac{\langle\partial h,\sigma\rangle}{s}\,\partial\tau.
\]

It then removes the corresponding paired rows/columns. This is a unimodular chain contraction, not field-only Gaussian elimination. After all 3,173 cancellations, every boundary of every surviving critical cell is *exactly zero over the integers*. The reduced cellular chain groups are therefore \(\mathbb Z^{45}\) in degree 3, \(\mathbb Z^{32}\) in degree 4, \(\mathbb Z^2\) in degree 5, and zero otherwise. There is no homology torsion.

**4. Connectivity and Hurewicz.** The resulting CW model has one vertex and no one- or two-cells. Therefore it is 2-connected. The integral Hurewicz theorem identifies its third homotopy group with \(H_3(K;\mathbb Z)\), giving \(\pi_3(K)\cong\mathbb Z^{45}\).

## Verification

The included standard-library-only `verify_kings5.py` independently reconstructs every face, confirms matching legality, topologically sorts the full directed Hasse diagram, executes exact signed integral chain contractions, and separately computes all mod-two simplicial boundary ranks. Running `python3 verify_kings5.py` reproduces `verifier_output.txt`. The mod-two boundary ranks for dimensions 1 through 8 are \((24,204,760,1182,760,216,26,1)\). In particular the mod-two Betti vector agrees with the integral answer, but the integral conclusion relies on signed unit-pivot cancellation rather than this comparison.

## Relationship to prior work

Engström's 2005 work [1] develops homotopy methods for graph independence and anti-Rips complexes; it does not compute this 25-square strong-product complex. Barmak [2] provides general star-cluster methods. Carnero Bravo [3, Section 5] explicitly identifies king graphs as \(P_n\boxtimes P_m\), and determines homotopy types of the strips of widths two, three and four, along with related induced subgraphs. Its stated width range does not cover this \(5\times5\) graph, and the inspected section supplies neither these three integral Betti ranks nor this perfect Morse model. The current calculation gives a precise natural first-width-five datum beyond that published range; it neither asserts a uniform formula for larger widths nor claims prior results on narrower widths as new.

## Limitations

Although the integral cellular differential of the Morse model vanishes, this **does not prove** a wedge-of-spheres decomposition: the two five-cell attaching maps may contain undetected order-two components in the fourth homotopy of the three-sphere summands. No assertion is made about higher homotopy, cup products or Steenrod squares, nor about boards of other sizes. A finite exhaustive certificate proves exactly the stated finite case, not a uniform theorem. Novelty is assessed against accessible published and indexed sources and is not a guarantee against all unindexed work.

## References

[1] A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148v1, initially public 2005-08-08, especially Sections 3–4. https://arxiv.org/abs/math/0508148

[2] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, initially public 2010-07-02. https://arxiv.org/abs/1007.0418

[3] A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457v2, 2025-11-11 revision of work first public 2025-05-09, especially Section 5, Propositions 25–28, Corollary 29 and Theorem 31. https://arxiv.org/html/2505.06457v2

[4] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, for acyclic matchings and their CW models.
