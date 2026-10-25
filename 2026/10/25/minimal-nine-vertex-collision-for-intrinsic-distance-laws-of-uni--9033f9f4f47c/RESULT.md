# Minimal nine-vertex collision for intrinsic distance laws of unit-edge metric trees

## Finding
Let \(T\) be a finite combinatorial tree with all its edges realized as unit-length intervals, equipped with its intrinsic shortest-path metric and the probability measure obtained by normalizing its total arclength. For two independent points \(X,Y\) sampled from this probability measure, let \(\mathcal D(T)\) denote the law of \(d_T(X,Y)\).

**Theorem.** The smallest number of vertices for two nonisometric unit-edge metric trees with identical \(\mathcal D\) is **nine** (eight edges). In fact, there exist such nine-vertex trees with different numbers of leaves—five and four—whose common distance density is
\[
 f(r)=\begin{cases}
 (4+r)/16,&0\le r\le1,\\
 5/16,&1\le r\le2,\\
 (9-2r)/16,&2\le r\le4,\\
 (5-r)/16,&4\le r\le5,\\
 0,&\text{otherwise}.
 \end{cases}
\]
The endpoint conventions do not affect the probability law. For any tree with fewer than nine vertices, equality of these distance laws implies isometry as unit-edge metric trees.

## Assumptions and scope
All edges have length exactly one, including edges incident to degree-two vertices; the vertex count refers to this specified unit-edge realization. Points are sampled independently from **normalized one-dimensional Hausdorff (arclength) measure on the full realized tree**, not from uniform vertices or leaves. Distance means intrinsic geodesic distance. The theorem makes no analogous minimality claim when arbitrary positive edge lengths are allowed.

Write each tree by the following unordered edge sets on vertices \(\{0,1,\ldots,8\}\):

\[
\begin{aligned}
E_A={}&\{(1,0),(1,2),(1,4),(0,5),(0,8),(2,3),(5,6),(5,7)\},\\
E_B={}&\{(1,0),(1,2),(0,4),(0,6),(0,8),(2,3),(4,5),(6,7)\}.
\end{aligned}
\]

Their sorted degree multisets are respectively \((1,1,1,1,1,2,3,3,3)\) and \((1,1,1,1,2,2,2,2,4)\), which prove nonisomorphism and intrinsic nonisometry. The respective numbers of leaves are five and four.

## Proof
**1. Edge-pair decomposition.** Let a unit-edge tree have \(m\) edges. For two distinct edges \(e,f\), let \(k(e,f)\) be the minimum combinatorial distance between their endpoints, so adjacent edges have \(k(e,f)=0\). Write \(N_k(T)\) for the number of unordered pairs of distinct edges with separation \(k\). Let \(u_+=\max\{u,0\}\), and define the triangular density
\[
 g(u)=\begin{cases}u,&0\le u\le1,\\ 2-u,&1\le u\le2,\\ 0,&\text{otherwise}.\end{cases}
\]
If sampled sites lie on the same edge, their distance has density \(2(1-r)_+\) on \(r\ge0\). For sites on distinct edges of endpoint separation \(k\), the unique geodesic joins two independently uniform edge offsets and has density \(g(r-k)\). Since each ordered edge pair has probability \(m^{-2}\), the exact density is
\[
 f_T(r)=\frac{2m(1-r)_++2\sum_{k\ge0}N_k(T)g(r-k)}{m^2},\qquad r\ge0.
\]
This identity is a finite decomposition, with no probabilistic limiting argument.

**2. The collision.** Enumerating the \(\binom82=28\) unordered edge pairs using the displayed edge sets gives, for both trees,
\[
 (N_0,N_1,N_2,N_3)=(10,10,6,2),\qquad N_k=0\text{ for }k\ge4.
\]
Substitute this histogram with \(m=8\) into the exact identity in Step 1. Collecting the linear pieces yields the displayed common density. This proves equality of full distributions, not merely moments, while the degree multisets prove nonisometry.

**3. Reducing minimality to a finite invariant.** For a tree with \(m\) unit edges, \(f_T(0+)=2/m\), because distinct-edge contributions vanish at zero. Thus identical laws have the same edge count, and therefore the same number of vertices. The triangular translates \(g(r-k)\) for integer \(k\ge0\) are linearly independent over finite collections: examining the first unit interval where a nonzero coefficient appears forces it to vanish, recursively. Consequently, for a fixed \(m\), equality of full distance laws is equivalent to equality of the entire edge-separation histogram \(\{N_k\}\).

**4. Complete finite cutoff.** Each labeled tree on \(n\) vertices corresponds bijectively to a Prüfer word of length \(n-2\) over \(\{0,\ldots,n-1\}\). The accompanying independent executable `verify_tree_distance.py` iterates every such word for each \(2\le n\le8\), computes the edge-separation histogram directly by breadth-first search, and computes the exact unrooted tree-isomorphism type by center-rooted canonical parentheses. It checks that no histogram occurs with two distinct canonical types. The numbers of distinct types are respectively \(1,1,2,3,6,11,23\) for \(n=2,\ldots,8\). The longest check, \(n=8\), evaluates exactly \(8^6=262144\) labeled trees. This is an exhaustive finite certificate and hence excludes a smaller collision. Combined with Step 2 it proves the theorem.

## Verification
Run `python verify_tree_distance.py` using Python 3 and no nonstandard dependencies. The program independently recomputes both witness histograms, their degree multisets and unrooted canonical codes, and checks the density on the interior of every asserted linear region using exact rational arithmetic. It then exhausts every Prüfer word through eight vertices and reports `CERTIFICATE_OK` only if the minimality assertion holds. Its directly recorded outputs are: both histograms `((0, 10), (1, 10), (2, 6), (3, 2))`, distinct degree multisets as displayed, nonisomorphic-class counts \((1,1,2,3,6,11,23)\), and zero prior collisions. Analytical Steps 1–3 justify what the finite computation certifies; the program exhausts a **finite** census only.

## Relationship to prior work
Classical Hosoya/Wiener polynomials encode unordered **vertex** distance histograms, while the continuous metric-tree distance law concerns two arclength-uniform sites. Theorem 3.2 of Tratnik–Žigert Pleteršek (2017) relates the vertex and edge Hosoya polynomials of trees; the reduction to a discrete distance histogram is **not claimed to be new**. The two witness trees also have the same classical nonzero vertex-distance counts \((8,10,10,6,2)\). The claimed contribution is the sharp **nine-vertex** cutoff for the arclength-geodesic inverse problem, together with the explicit minimal nonisometric pair of different leaf counts and its exact distance law.

Mémoli–Needham study global and local distance distributions of metric graphs, giving noninjectivity examples for metric trees (Example 4.3), but their exhibited trees are much larger and the examined material does not give the nine-vertex minimality cutoff. Martin–Morin–Wagner (2006) show a pair of 11-vertex trees with identical subtree/path information in their Figure 2; their example does not establish the sharp smaller nine-vertex cutoff. The 2015 paper *On path sequences of graphs* uses **path vertex-cover numbers**, a different invariant. These are implication-level comparisons, not arguments from a missing search hit.

## Limitations
The smallest-size conclusion depends on the provided exhaustive **finite** Prüfer certificate, not an independent hand classification of the 23 eight-vertex tree types. In particular it does not assert rigidity for arbitrary edge lengths, local distance distributions, vertex-sampled measurements alone, or any larger number of points. Earlier graph-theoretic tables may already contain the equivalent nine-vertex vertex-distance collision; historical priority of the precise finite cutoff is not independently established. The analytic density identity and exhaustive computation are reproducible; no independent audit has been performed.

## References
1. J. L. Martin, M. Morin and J. D. Wagner, *On distinguishing trees by their chromatic symmetric functions* (first posted 2006-09-12), arXiv:math/0609339. https://arxiv.org/abs/math/0609339 .
2. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, arXiv:1810.09646, Section 4 and Example 4.3. https://arxiv.org/abs/1810.09646 .
3. N. Tratnik and P. Žigert Pleteršek, *Relationship Between the Hosoya Polynomial and the Edge–Hosoya Polynomial of Trees*, MATCH Commun. Math. Comput. Chem. **78** (2017), 181–187, Theorem 3.2. https://match.pmf.kg.ac.rs/electronic_versions/Match78/n1/match78n1_181-187.pdf .
4. S. Bakalarski and J. Zygadło, *On path sequences of graphs*, arXiv:1511.05384 (2015), Definition 1.1 and Proposition 4.3. https://arxiv.org/abs/1511.05384 .
5. G. Guo et al., *Hyper-Wiener vector, Wiener matrix sequence, and Wiener polynomial sequence of a graph*, Int. J. Quantum Chem. **106** (2006), 1756–1761.
