# The unique eight-generator one-round refinement collision in finite distributive lattices

## Finding

For a finite nonempty poset \(P\), let \(J(P)\) be its lattice of order ideals, ordered by inclusion. For \(I\in J(P)\) define
\[
 d_-(I)=|\{H\in J(P):H\subsetneq I\}|,\qquad
 d_+(I)=|\{H\in J(P):I\subsetneq H\}|,
\]
and let \(\Sigma(P)\) be the multiset of ordered pairs \((d_-(I),d_+(I))\) over every \(I\in J(P)\).

**Theorem (complete first-collision layer).** Among all finite distributive lattices having between one and eight join-irreducible elements, exactly one unordered pair of nonisomorphic lattices has the same \(\Sigma\) signature. There is no collision with at most seven join-irreducibles; at eight there is precisely one. Both exceptional lattices have eighteen elements, and their distinct join-irreducible posets have predecessor masks, in a displayed topological numbering \(0,\ldots,7\),
\[
 P_A:(0,0,1,3,5,15,23,63),\qquad
 P_B:(0,0,1,3,5,15,23,95).
\]
A mask records the set of smaller-numbered strict predecessors by its binary indicator: bit \(i\) represents predecessor \(i\). The heights of \(P_A\) and \(P_B\), counting points in longest chains, are four and five, respectively. Hence the lattices are nonisomorphic by Birkhoff duality. The eighteen pairs in their common signature, including multiplicities, are
\[
\begin{gathered}
(0,17),(1,13),(1,15),(2,12),(3,8),(3,12),\\
(4,8),(5,10),(7,7),(7,7),(8,3),(8,4),\\
(10,5),(12,2),(12,3),(13,1),(15,1),(17,0).
\end{gathered}
\]
In the one-binary-strict-order vocabulary, equality of \(\Sigma\) is precisely equality of the global colour histograms after the first synchronous two-direction counting-refinement round, starting uniformly. The exceptional pair is **not** indistinguishable by full two-variable counting logic: their global histograms already differ after round two.

## Assumptions and scope

All posets are finite, and all lattice isomorphisms preserve the order direction. A nontrivial finite distributive lattice is considered via its canonical poset of join-irreducibles. The range is \(1\le |P|\le8\), i.e. precisely one through eight join-irreducibles; the one-element lattice with none has a unique signature and adds no ambiguity. The claim concerns a one-round order-degree invariant, not the full stable colour partition. No statement about lattices with more than eight join-irreducibles, or minimal lattice cardinality without a join-irreducible bound, is made.

## Proof

**Step 1: exhaustive normal form.** Every \(n\)-point poset has a maximal element \(v\). Its strict predecessor set is an order ideal of the poset remaining after deleting \(v\). Conversely, for every \((n-1)\)-point poset \(Q\) and every order ideal \(D\subseteq Q\), adjoining one new maximal point whose strict predecessor set is precisely \(D\) defines a poset. Induction shows this extension rule generates every finite poset. Exact directed-graph isomorphism on the transitively closed strict relation removes all duplicated presentations. This is also the one-maximal-point construction discussed by Erné–Heitzig–Reinhold (2002, section 2).

**Step 2: Birkhoff conversion and invariant.** The finite Birkhoff representation sends each poset \(P\) to \(J(P)\) and is injective on isomorphism types; the number of join-irreducibles of \(J(P)\) is exactly \(|P|\). An order ideal is an indicator subset \(S\) satisfying \(\operatorname{Pred}(i)\subseteq S\) for every \(i\in S\). Thus exact enumeration of all \(2^{|P|}\) candidate subsets determines \(J(P)\). Inclusion comparisons determine \(d_-\) and \(d_+\) for every lattice member, without approximation. Equality of \(\Sigma\) between two lattices is exactly agreement of their one-round global two-direction counting-colour histograms, because the initial colour is uniform and the noncomparability counts are determined by the order and the carrier size.

**Step 3: exhaustive collision test.** The supplied first standalone program implements Steps 1 and 2, with isomorphism rejection via exact directed-graph isomorphism. The counts of representatives at \(n=1,2,\ldots,8\) are, respectively,
\[
1,\ 2,\ 5,\ 16,\ 63,\ 318,\ 2045,\ 16999.
\]
It compares the signatures across **all** \(19449\) nontrivial representative posets (including across different values of \(n\)); the signature partition has \(19448\) blocks, exactly one of size two and every other block a singleton. The two presentations stated above are the members of that block. The algorithm's coverage is a finite exhaustive proof, not an inference from random sampling; the eight-point endpoint is a proved finite cutoff.

**Step 4: independent direct witness check.** A second standalone program independently enumerates the eighteen ideal sets for each exceptional poset using combinations of vertices, recomputes all strict inclusion counts, and checks agreement of their paired-degree histograms. It also directly checks the poset heights \(4\) and \(5\), nonisomorphism, and the first two synchronous directed-refinement rounds on their disjoint union. The first-round histograms agree and the second-round histograms do not. These computations separately check the example; the completeness assertion comes from Step 3.

## Verification

Run \(\texttt{python verify\_degree\_profiles.py}\) and \(\texttt{python verify\_witness.py}\) using Python 3 and NetworkX. Both scripts contain executable assertions; the recorded successful output files are \(\texttt{exhaustive\_output.txt}\) and \(\texttt{witness\_output.txt}\). Exact reference dependency versions appear in \(\texttt{requirements.txt}\). The exhaustive enumeration is finite and deterministic, using no randomness, heuristic isomorphism acceptance, or external graph databases. Isomorphism is tested on the full directed transitive-closure graph, not merely on a degree fingerprint. All reported counts and comparisons are integer-exact.

## Relationship to prior work

Birkhoff's finite distributive-lattice representation and the exhaustive maximal-element extension method are established background. Erné, Heitzig and Reinhold (2002) enumerate distributive lattices and explicitly describe the one-point construction; the new invariant collision threshold is not stated in their inspected article. Arvind, Köbler, Rattan and Verbitsky (2015) establish the colour-refinement and two-variable counting-logic framework, including amenability, but do not state this lattice-specific one-round threshold. The result here is an exact finite model-theoretic boundary for a canonical coarse local invariant, not a new lattice-enumeration method and not a claimed counterexample to full counting-logic identification. Known counts alone do not determine the pairwise degree-histogram collision result without the additional comparison.

## Limitations

The independent mathematical audit has not been performed. The exhaustive search is bounded by eight join-irreducibles; its truth depends on the stated finite enumeration algorithm and exact execution, which are provided. The result does not rule out earlier specialised publications of the same degree-profile collision, nor does it establish global uniqueness outside the finite range. The computer-assisted completeness proof uses standard finite exact directed-graph isomorphism, not a formal proof assistant or externally certified computation.

## References

1. Marcel Erné, Jobst Heitzig, Jürgen Reinhold, *On the Number of Distributive Lattices*, Electronic Journal of Combinatorics 9 (2002), R24. DOI: 10.37236/1641. Public source dated 2002-04-01. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v9i1r24.
2. V. Arvind, Johannes Köbler, Gaurav Rattan, Oleg Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first public 2015-02-04. https://arxiv.org/abs/1502.01255.
3. Andreas Krebs, Oleg Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first public 2014-07-11. https://arxiv.org/abs/1407.3175.
