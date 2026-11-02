# Genericity inversion for finite quantum forcing frames

## Finding

Let \(W=[n]\) with \(n\geq1\). A **forcing frame** is a pair \((Q,M)\), where \(Q\subseteq W^2\) is reflexive and symmetric and \(M\subseteq W^2\) satisfies
\[
 uMv\ \land\ uQw\quad\Longrightarrow\quad wMv
 \qquad(u,v,w\in W).
\]
The frames are labelled and have no propositional valuations. Write \(A_n\) for the number with arbitrary \(M\), and \(B_n\) for the number with \(M\) an equivalence relation. For a simple graph \(G\), let \(\kappa(G)\) be its number of connected components; let \(\Pi_n\) be the set of partitions of \(W\). Then
\[
 A_n=\sum_{G\subseteq K_n}2^{n\kappa(G)},\qquad
 B_n=\sum_{\pi\in\Pi_n}2^{\sum_{C\in\pi}\binom{|C|}{2}}.
\]
The first count has a two-term defect expansion:
\[
\begin{aligned}
 \frac{A_n}{2^{n^2}}={}&1+\binom n2 2^{-n}\\
 &+\left(4\binom n3+3\binom n4\right)2^{-2n}
 +O(n^6 2^{-3n}).
\end{aligned}
\]
The second count satisfies
\[
\frac{B_n}{2^{\binom n2}}
=1+n2^{-(n-1)}+O(n^2 2^{-3n/2}).
\]
All asymptotics are as \(n\to\infty\). Consequently a uniformly sampled arbitrary-accessibility forcing frame has discrete \(Q\) with probability \(1-\binom n2 2^{-n}+O(n^4 2^{-2n})\). A uniformly sampled equivalence-accessibility forcing frame has universal \(M\) with probability \(1-n2^{-(n-1)}+O(n^2 2^{-3n/2})\). Conditional on failure of these respective generic properties, the first model has exactly one off-diagonal undirected \(Q\)-edge with probability tending to one, while the second has an \(M\)-partition of block sizes \((n-1,1)\) with probability tending to one. In the latter event, \(Q\) has precisely two connected components, of sizes \((n-1,1)\), with conditional probability tending to one.

## Assumptions and scope

Loops in \(Q\) are mandatory; all other unordered compatibility edges are independent combinatorial choices before imposing the forcing condition. Loops and all ordered pairs, including loops, are allowed in arbitrary \(M\). In the second ensemble \(M\) must be reflexive, symmetric and transitive. Counting is uniform over **pairs of relations**, not uniform over compatibility graphs or over modal isomorphism classes. No assumption is made that \(Q\) is an equivalence relation or a Hilbert-space representable orthogonality relation.

The motivating forcing condition and its component-invariance consequence belong to Tokuo's relational quantum modal semantics. The results here concern the full finite combinatorial frame class, without valuations, and do not assert any statistical statement for a physically specified distribution of quantum states.

## Proof

**1. Normal forms.** Regard the off-diagonal edges of \(Q\) as an undirected simple graph \(G\). Because \(Q\) is symmetric, forcing in both directions says that the entire \(M\)-successor row is constant along each \(G\)-edge, hence on every connected component. Conversely any assignment of one arbitrary successor subset of \(W\) to each component satisfies forcing. This gives exactly \(2^{n\kappa(G)}\) possibilities and proves the formula for \(A_n\).

When \(M\) is an equivalence relation, forcing is equivalent to \(Q\subseteq M\). Necessity follows because for \(uQv\), reflexivity gives \(uMu\), forcing gives \(vMu\), and symmetry gives \(uMv\). Sufficiency follows from transitivity: \(uMv\) and \(uQw\subseteq uMw\) imply \(wMv\). Thus every compatibility edge must lie within one block of the \(M\)-partition. For a prescribed partition \(\pi\), there are \(2^{\sum_{C\in\pi}\binom{|C|}{2}}\) compatibility graphs, establishing \(B_n\).

**2. First two unrestricted-accessibility defects.** Put \(r=n-\kappa(G)\), the size of a spanning forest of \(G\), and let \(g_{n,r}\) count graphs of this rank. The rank-zero graph is edgeless, and \(g_{n,1}=\binom n2\). A rank-two graph has either one connected triple (four choices of connected simple graph on each chosen triple) or two disjoint edges (three matchings on each chosen quadruple). Hence
\[
 g_{n,2}=4\binom n3+3\binom n4.
\]
For every \(r\), choose a spanning forest with \(r\) edges. All further edges remain within its components. If their sizes are \(s_i\), then \(\sum_i(s_i-1)=r\) and
\[
 \sum_i\binom{s_i}{2}\leq \binom{r+1}{2}.
\]
Therefore, with \(N=\binom n2\),
\[
 g_{n,r}\leq\binom Nr\,2^{\binom{r+1}{2}}.
\]
For \(3\leq r\leq n/2\), the successive upper bounds \(\binom Nr2^{\binom{r+1}{2}-nr}\) have ratio at most \(N2^{r+1-n}\leq n^2 2^{-n/2+1}\), which tends to zero. Their sum is \(O(n^6 2^{-3n})\). For \(n/2<r\leq n-1\), use \(\binom Nr\leq N^r\) and \(\binom{r+1}{2}\leq nr/2\) to bound the sum by \(\sum_{r>n/2}(N2^{-n/2})^r\), which is smaller still. Since
\[
 \frac{A_n}{2^{n^2}}=\sum_{r=0}^{n-1}g_{n,r}2^{-nr},
\]
the asserted expansion follows. Rank one is exactly a single compatibility edge, giving its conditional first-defect law.

**3. First equivalence-accessibility defect.** For a partition \(\pi\), let
\[
 d(\pi)=\sum_{\substack{C,D\in\pi\\C<D}}|C||D|
 =\binom n2-\sum_{C\in\pi}\binom{|C|}{2}.
\]
The notation \(C<D\) merely counts each pair of distinct blocks once. Thus
\[
 \frac{B_n}{2^{\binom n2}}=\sum_{\pi\in\Pi_n}2^{-d(\pi)}.
\]
The one-block partition contributes one. Exactly \(n\) partitions have block sizes \((n-1,1)\) for \(n\geq3\), and each contributes \(2^{-(n-1)}\). Every other partition has one of two forms. Either it has a block of size \(n-j>3n/4\), with \(j\geq2\), or all blocks have size at most \(3n/4\). In the first case, choose its \(j\)-element complement and partition those \(j\) elements arbitrarily. There are at most \(\binom nj\,\mathrm{Bell}(j)\leq(en)^j\) choices, and at least \(j(n-j)\geq3jn/4\) forbidden cross-block edges. Summing over \(2\leq j<n/4\) gives \(O(n^2 2^{-3n/2})\). In the second case,
\[
 d(\pi)=\tfrac12\left(n^2-\sum_{C\in\pi}|C|^2\right)\geq n^2/8.
\]
There are at most \(n^n\) set partitions, so the second contribution is at most \(n^n2^{-n^2/8}=o(n^2 2^{-3n/2})\). This establishes the second expansion and the sharp conditional block-shape assertion.

For a fixed \(M\)-partition of type \((n-1,1)\), uniform admissible \(Q\) is an independent fair-edge graph on the large block and an isolated vertex. Such a graph is connected on its large block with probability tending to one: the probability of a nontrivial cut with no edge is at most
\[
 \sum_{j=1}^{\lfloor (n-1)/2\rfloor}
 \binom{n-1}{j}\,2^{-j(n-1-j)}=o(1).
\]
This completes the conditional component assertion.

**4. Genericity contrast.** In the first ensemble the edgeless graph has \(2^{n^2}\) compatible modal relations; all nonedgeless graphs together have a smaller relative mass of order \(\binom n2 2^{-n}\). In the equivalence-restricted ensemble, universal \(M\) is compatible with all \(2^{\binom n2}\) graphs, while all nonuniversal \(M\) together have relative mass of order \(n2^{-(n-1)}\). Division by the total counts proves both probability statements. The classical Boolean stable-set algebra for discrete \(Q\) follows directly from \(X^\perp=W\setminus X\).

## Verification

A standalone standard-library Python file, `checker.py`, verifies all finite counts below. It independently enumerates every reflexive symmetric compatibility relation and every arbitrary modal relation through three worlds, directly testing the forcing implication and equivalence axioms. It also enumerates all undirected compatibility graphs and all set partitions through six worlds, reproducing the analytic counting formulas and rank-two coefficient.

| \(n\) | \(A_n\) | \(B_n\) |
|---:|---:|---:|
| 1 | 2 | 1 |
| 2 | 20 | 3 |
| 3 | 736 | 15 |
| 4 | 95,584 | 121 |
| 5 | 46,101,248 | 1,665 |
| 6 | 87,161,615,360 | 43,883 |

Run `python3 checker.py` from the same directory. These computations are finite consistency tests, not a replacement for the all-size proof.

## Relationship to prior work

Tokuo, *Component Modalities of Quantum Logic* (2026), establishes the forcing condition's componentwise successor-row characterization and studies equivalence accessibility semantically. The two normal forms are direct uses of that setting, not independent claims of novelty. The first enumeration is also the complete-graph random-cluster partition function evaluated at cluster weight \(2^n\) and unit edge activity, a standard combinatorial identity. The classical random-cluster literature analyzes different parameter regimes, notably fixed cluster weight and sparse edge probabilities. The contribution assessed here is the **paired finite-frame counting and sharp, opposing first-defect laws** for unrestricted versus equivalence modal accessibility under the same forcing condition. An unpublished or older treatment of these precise weighted graph/partition asymptotics could subsume the claim; historical priority is not asserted absolutely.

## Limitations

This is a count of labelled relational frames, not valuations, formula equivalence classes, isomorphism types, physically realizable quantum systems, or arbitrary stability-preserving modal operators. It uses a specific uniform distribution on all admissible pairs; other sampling schemes may yield different genericity laws. The component-normal-form theorem and random-cluster identity are already known; only the stated quantitative juxtaposition and first-defect analysis are assessed as potentially new. The most relevant 2026 paper's arXiv HTML introduction and formal definitions were inspected, but a complete page-by-page inspection of its entire body was not available in this run; this is a historical-coverage risk, not a mathematical limitation of the derivation.

## References

1. Kenji Tokuo, *Component Modalities of Quantum Logic*, arXiv:2607.14757, first posted 2026-07-16. https://arxiv.org/abs/2607.14757
2. Kenji Tokuo, *Quantum modal logic*, *Logic Journal of the IGPL* 33 (2025), DOI:10.1093/jigpal/jzae123, first online 2024-11-12. https://doi.org/10.1093/jigpal/jzae123
3. Béla Bollobás, Geoffrey Grimmett, Svante Janson, *The random-cluster model on the complete graph*, *Probability Theory and Related Fields* 104 (1996), 283–317. https://doi.org/10.1007/BF01213683
4. Darion Mayes, *The random cluster model on the complete graph via large deviations*, arXiv:2201.05485, 2022. https://arxiv.org/abs/2201.05485
