# Universal geometric width law for first-order true-twin quotients on the random circle

## Finding

Let \(G_n(r)\) be the loopless graph on \(n\) independent, uniformly distributed circle points, with edges exactly at circular distance at most a fixed \(r\in(0,1/2)\). Define a graph-theoretic equivalence relation \(x\equiv y\) by equality of **closed neighborhoods**, \(N[x]=N[y]\). This relation is first-order definable using the edge predicate and equality: two vertices are equivalent when every vertex is either adjacent to both (or equal to both as appropriate) or to neither. Denote by \(C_{n,j}\) the number of its classes having exactly \(j\) vertices, \(Q_n\) the number of classes, and \(T_n\) the number of unordered pairs of distinct equivalent vertices.

**Theorem.** For every fixed integer \(j\ge1\), jointly for any finite selection of such indices,
\[
 \frac{C_{n,j}}n\xrightarrow{\mathsf P}c_j:=\frac49\,3^{-(j-1)}.
\]
Moreover,
\[
 \frac{Q_n}{n}\xrightarrow{\mathsf P}\frac23,
 \qquad \frac{T_n}{n}\xrightarrow{\mathsf P}\frac12.
\]
When a quotient class is chosen uniformly from the \(Q_n\) classes, its size converges in distribution to a geometric variable \(J\) with \(\Pr(J=j)=\frac23(\frac13)^{j-1}\). In particular, the asymptotic retained fraction of a natural first-order definable quotient is \(2/3\), independent of the fixed admissible radius.

## Assumptions and scope

The metric circle is \(\mathbb T=\mathbb R/\mathbb Z\), equipped with \(d(x,y)=\min(|x-y|,1-|x-y|)\), with representatives in \([0,1)\). The radius \(r\) is fixed throughout the limit and satisfies \(0<r<1/2\). The locations are independent and atomless, so distance equalities have probability zero. A closed neighborhood includes the vertex itself, and hence two distinct vertices with equal closed neighborhoods are adjacent. The result concerns the positive number of equivalence classes, not the number of unlabeled quotient-graph isomorphism types.

## Proof

**Step 1 (local adjacency criterion and localization).** Sort the sampled locations cyclically as \(X_{(1)},\ldots,X_{(n)}\), with \(X_{(n+1)}=X_{(1)}+1\). Set \(D_i=X_{(i+1)}-X_{(i)}\). Choose a fixed \(\eta>0\) smaller than \(r\), \(1-2r\), and the separation of the two boundary points \(\pm r\) on the circle. Whenever \(0<D_i<\eta\), the consecutive vertices are true twins exactly when there is no other sample point in either of the disjoint length-\(D_i\) arcs
\[
(X_{(i)}-r, X_{(i+1)}-r),\qquad
(X_{(i)}+r, X_{(i+1)}+r),
\]
where the arcs are understood modulo one and endpoints have probability zero. The arcs form the symmetric difference of the two radius-\(r\) neighborhoods. The two vertices are automatically mutually adjacent since \(D_i<r\).

A uniformly random sample has maximum circular spacing \(o_{\mathsf P}(1)\): for each fixed \(\delta>0\), partition the circle into sufficiently short deterministic subarcs; a gap longer than \(\delta\) forces one of finitely many such arcs to be empty, an event with exponentially small probability. For vertices at circular distance at least \(\eta\), equality of their closed neighborhoods requires all remaining vertices to avoid a symmetric difference of arcs with strictly positive measure. That measure has a positive infimum over displacements \(\eta\le d\le r\), since distinct radius-\(r\) circle arcs cannot agree modulo null sets. A union bound over at most \(n^2\) pairs shows that, with probability tending to one, **all distinct true-twin pairs are within circular distance \(\eta\)**. Make \(\eta\) additionally small enough that \(2\eta<r\) if convenient; no other restrictions are needed.

On this high-probability event, each true-twin class occupies a consecutive cyclic string of points. Indeed if its endpoints \(x,z\) occur within a short positively oriented arc and \(y\) is any intervening sample point, the two shifted boundary strips for \(x,y\) and for \(y,z\) are subsets of the strips for \(x,z\); also \(x,y,z\) are mutually within radius \(r\) at the needed pairs. Therefore \(N[x]=N[z]\) implies \(N[x]=N[y]=N[z]\). Equivalently, up to events of probability \(o(1)\), the true-twin classes are exactly the maximal runs of consecutive points joined by a *good gap*, where a good gap satisfies the displayed boundary-void criterion. We also have at least one bad gap with high probability, because the graph is neither complete nor a single equivalence class at fixed \(r<1/2\).

**Step 2 (local independent Bernoulli marks).** Let \(I\) be a uniformly sampled cyclic gap index, independent of the point configuration. Consider any fixed number of gaps neighboring \(I\). Under magnification by \(n\), the original consecutive spacings converge jointly to independent \(\operatorname{Exp}(1)\) random variables \(L_1,\ldots,L_h\). Moreover, point counts in disjoint magnified windows around the two macroscopically separated circle positions \(X_{(I)}-r\) and \(X_{(I)}+r\) converge jointly to two independent rate-one Poisson processes, independent of the original spacings. One may derive this joint limit by conditioning on finitely many displayed order statistics and applying binomial-to-Poisson limits to finitely many disjoint intervals of length \(O(1/n)\); equivalently it is the standard local limit of a binomial point process around finitely many distinct circle centers.

Conditionally on the limiting gaps, the two boundary windows associated with different consecutive gaps are disjoint within each boundary process. Hence the limiting good-gap marks are conditionally independent, each being true with conditional probability \(\exp(-2L_i)\). Integrating the independent exponential spacings gives independent Bernoulli variables of common success probability
\[
 p=\int_0^\infty e^{-l}e^{-2l}\,dl=\frac13,
 \qquad q=1-p=\frac23.
\]
Thus **every fixed local good/bad pattern** around a uniformly chosen gap has the law of an independent Bernoulli-\(1/3\) sequence in the limit.

For two independently chosen uniform cyclic positions, the two finite families of base and shifted sampling windows are disjoint with probability tending to one: the two starting positions have diffuse asymptotic separation, and the finitely many exceptional offsets \(0,\pm r,\pm2r\) have zero probability. The corresponding local patterns therefore converge jointly to independent copies. This two-root statement follows from the same disjoint-window binomial-to-Poisson calculation. As a consequence, any bounded local-pattern indicator averaged over all \(n\) cyclic positions has variance \(o(1)\): its diagonal contribution is \(O(1/n)\), and the covariance for two independently chosen distinct positions tends to zero.

**Step 3 (class-size frequencies).** For a fixed \(j\ge1\), a cyclic starting vertex is the first vertex of a run of size exactly \(j\) precisely when the preceding gap is bad, the following \(j-1\) gaps are good, and the next gap is bad. Write \(I_{i,j}\) for that pattern indicator. Step 2 gives
\[
 \mathbb E I_{i,j}\to q^2p^{j-1}
 =\frac49\,3^{-(j-1)},\qquad
 \operatorname{Var}\left(\frac1n\sum_{i=1}^n I_{i,j}\right)\to0.
\]
On the high-probability run representation from Step 1, \(\sum_i I_{i,j}=C_{n,j}\). The claimed convergence of \(C_{n,j}/n\) follows by Chebyshev's inequality, simultaneously for finitely many \(j\).

**Step 4 (quotient size and selected-class law).** A cyclic partition into runs with at least one bad gap has one class per bad gap. The law of large numbers from Step 2 for the one-gap indicator thus gives
\[
 Q_n/n\to q=2/3\quad\text{in probability}.
\]
For each fixed \(j\), the proportion of quotient classes of size \(j\) is \(C_{n,j}/Q_n\to c_j/q=qp^{j-1}\). Since \(\sum_{j\ge1}qp^{j-1}=1\), this yields a full probability distribution on positive integers and proves weak convergence of the randomly selected class size (no unverified tightness assumption).

**Step 5 (adjacent-twin pair concentration).** Every unordered distinct true-twin pair is adjacent, and \(T_n=\sum_{j\ge1}\binom j2C_{n,j}\) exactly. The motivating paper's Theorem 1.2 gives the independently established expectation asymptotic \(\mathbb E T_n/n\to1/2\) in dimension one for fixed \(r\). For each fixed \(J\), the nonnegative truncated sum \(S_{n,J}=\sum_{j=1}^J\binom j2 C_{n,j}\) satisfies \(S_{n,J}/n\to a_J=\sum_{j=1}^J\binom j2 c_j\) in probability **and in mean**, because it is bounded by a finite constant. By the elementary geometric-series identity,
\[
 a_J\uparrow\sum_{j\ge1}\binom j2q^2p^{j-1}
 =\frac{p}{q}=\frac12.
\]
The last identity follows from the elementary derivative formula \(\sum_{j\ge1}\binom j2p^{j-1}=p/(1-p)^3=p/q^3\). Since \(T_n-S_{n,J}\ge0\), Markov's inequality and \(\lim_n\mathbb E(T_n-S_{n,J})/n=1/2-a_J\) show that the omitted tail divided by \(n\) is arbitrarily small in probability when \(J\) is chosen large. Hence \(T_n/n\to1/2\) in probability. No finite enumeration is used in any limiting argument. This completes the theorem.

## Verification

An accompanying standard-library `checker.py` derives all closed neighborhoods directly from sampled graphs and independently compares their equality-class size distribution with the good-gap run algorithm. It performs 2,250 seeded graph-by-graph checks at three radii and 480 additional independent larger-graph trials at four radii, comparing empirical sizes one through five and twin-pair densities with the theorem. The output is `ALL_CHECKS_OK`. These finite calculations test the exact structural reduction and numerical plausibility only; the asymptotic proof is the probabilistic argument above. Execute `python3 checker.py`.

## Relationship to prior work

Haber, Mirabi and Shelah, *First-Order Laws for Random Geometric Graphs on the Torus*, arXiv:2609.26230v1, first publicly posted August 12, 2026, establish the expected number of adjacent true-twin pairs for fixed radius in arbitrary torus dimension (their Theorem 1.2), and cite McColm's older zero-one law in dimension one. Their Section 6.2 derives the geometric disagreement-volume estimate underlying this fact. Their inspected full text does **not** identify the size distribution of equivalence classes of equal closed neighborhoods, quotient density, or a law of large numbers for the twin-pair count. The present argument uses their expectation result as a cited premise for the last conclusion, and proves the class-size spectrum and quotient-density results separately.

Badiu and Coon, *Structural Complexity of One-Dimensional Random Geometric Graphs* (2022), analyze possible graph structures and entropy, a distinct problem from the empirical size distribution of first-order definable true-twin classes. Classical proper-interval-graph twin-block structure motivates the contiguity argument, but does not by itself supply the radius-uniform constants for this circle model.

## Limitations

The radius must remain fixed strictly between zero and one half. The result does not determine central-limit fluctuations, moderate deviations, dependence across radii, or higher-dimensional class-size laws. The proof assumes uniformly independently sampled points on the circle. The concentration of \(T_n\) additionally uses the published Theorem 1.2 expectation asymptotic and is not claimed to be a wholly independent derivation of that mean. Literature checks cannot establish absolute historical priority: earlier results phrased in terms of proper interval graph modules, Poisson gap runs, or neighborhood-equivalence classes could overlap. The main finding is the precise size-frequency law and definable quotient density, not a new zero-one law.

## References

1. S. Haber, M. Mirabi, S. Shelah, *First-Order Laws for Random Geometric Graphs on the Torus*, arXiv:2609.26230v1 (first public date 2026-08-12). In particular Theorem 1.2 and Section 6.2.
2. M.-A. Badiu, J. P. Coon, *Structural Complexity of One-Dimensional Random Geometric Graphs*, IEEE Transactions on Information Theory 69 (2023), 794–812, early public manuscript 2022; DOI 10.1109/TIT.2022.3207819.
3. G. McColm, *First order zero-one laws for random graphs on the circle*, 1999 (as cited in Reference 1).
