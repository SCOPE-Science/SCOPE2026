# A harmonic power-rank law for uniformly random Catalan transformations

## Finding
Let \(\mathcal K_n\) be the monoid of all maps \(f:[n]\to[n]\) satisfying \(f(i)\le i\) and \(f(i)\le f(i+1)\). Choose \(F_n\) uniformly from \(\mathcal K_n\) and let \(R_{n,k}=|\operatorname{im}(F_n^k)|\), with \(F_n^0\) the identity. For each fixed integer \(k\ge0\),
\[
\frac{R_{n,k}}n\longrightarrow\frac1{k+1}\quad\text{in }L^2\qquad(n\to\infty).
\]
The statement holds jointly for each finite list of fixed nonnegative powers. In particular, the limiting normalized image ranks of the successive powers are \(1,1/2,1/3,1/4,\ldots\). This identifies a natural algebraic decay profile rather than merely the eventual stabilization time.

## Assumptions and scope
The maps are full, not partial, endomaps of \([n]=\{1,\ldots,n\}\). Order-preserving means nondecreasing and order-decreasing means \(f(i)\le i\). The random measure is uniform over the \(\frac1{n+1}\binom{2n}{n}\) labeled transformations, not uniform over a quotient or a generating set. Composition is ordinary function composition. The limit is for each *fixed* \(k\) as \(n\to\infty\); no uniformity when the exponent grows with \(n\) is claimed.

## Proof
**1. Parent forests and plane trees.** Necessarily \(f(1)=1\). List the fixed points as \(1=r_1<\cdots<r_s\). For each block from \(r_j\) to just before \(r_{j+1}\) (or to \(n\) for the last block), monotonicity and regressivity imply that every non-root element maps to an earlier element in the same block. Make \(f(i)\) the parent of \(i\) when \(f(i)<i\), with \(r_j\) as block root. The parent indices are nondecreasing within each block. This is precisely the breadth-first labeling of a plane rooted tree: a vertex's children form a consecutive interval, and parents of vertices met from left to right never decrease. Conversely, breadth-first-label any ordered forest of plane rooted trees, concatenate the labels of its components, and map each non-root vertex to its parent and each component root to itself. These two constructions are mutual inverses. Adding an auxiliary root above the component roots gives a bijection with plane rooted trees having \(n\) edges.

**2. Iterated images are nearly a fringe-height statistic.** Fix \(k\ge1\). Let \(A_{n,k}\) count the non-auxiliary vertices of the corresponding tree that have a descendant exactly \(k\) levels below them **inside their own forest component**. For every nonfixed vertex \(v\), \(v\in\operatorname{im}(f^k)\) if and only if \(v\) has a descendant at distance at least \(k\), hence at distance exactly \(k\). All component roots belong to \(\operatorname{im}(f^k)\) regardless of descendant height, because they are fixed points. Consequently,
\[
0\le R_{n,k}-A_{n,k}\le s.
\]
The discrepancy is confined to at most the \(s\) component roots. For \(k=0\), \(R_{n,0}=n\) exactly. An ordinary rooted-tree fringe-height statistic counts the auxiliary root as well; that adds at most one to \(A_{n,k}\).

**3. Fixed-point count is tight.** Write \(S(z)=(1-\sqrt{1-4z})/2\), the generating function for nonempty plane rooted trees by vertices. The parent-forest bijection yields
\[
\#\{f\in\mathcal K_n:|\operatorname{Fix}(f)|=s\}=[z^n]S(z)^s
=\frac{s}{2n-s}\binom{2n-s}{n},\qquad1\le s\le n.
\]
For each fixed \(s\ge1\), division by the Catalan number and Stirling's formula give \(\Pr(s(F_n)=s)\to s/2^{s+1}\). Since \(\sum_{s\ge1}s/2^{s+1}=1\), this convergence implies tightness of \(s(F_n)\). Therefore \(s(F_n)/n\to0\) in probability. Fixed-point counting itself is established prior work; it is used here only for the vanishing root correction.

**4. Local fringe limit.** A uniformly random plane rooted tree of \(n+1\) vertices is exactly a Galton–Watson plane tree with offspring distribution \(\Pr(\xi=j)=2^{-j-1}\), conditioned on total size \(n+1\): for a given plane tree, the product of offspring probabilities equals \(2^{-\sum_v(\deg(v)+1)}=2^{-(2n+1)}\), independent of its shape. The standard empirical-fringe-subtree law for conditioned critical Galton–Watson trees [Janson] says that, for every bounded indicator depending on the fringe subtree, its empirical mean converges in probability to the corresponding unconditioned Galton–Watson probability. In particular, use the indicator that fringe height is at least \(k\). (For a fixed \(k\), this is a bounded observable; it can also be approximated by finite truncations of the fringe tree.)

Let \(q_k\) be the probability that the unconditioned Galton–Watson tree contains a descendant in generation \(k\), with \(q_0=1\). Its offspring probability generating function is \(g(t)=1/(2-t)\), hence
\[
q_{k+1}=1-g(1-q_k)=\frac{q_k}{1+q_k},
\qquad q_k=\frac1{k+1}.
\]
It follows that \(A_{n,k}/n\to q_k\) in probability: the auxiliary root makes a difference of at most one. The inequality in step 2 and the tightness in step 3 prove \(R_{n,k}/n\to 1/(k+1)\) in probability. As \(0\le R_{n,k}/n\le1\), bounded convergence in probability to a constant also gives \(L^2\) convergence. Applying the same conclusion to finitely many fixed exponents gives joint vector convergence.

## Verification
The standalone \(\texttt{verify.py}\) enumerates **all** order-preserving, regressive transformations for each \(1\le n\le10\), checks the Catalan cardinality, independently composes each transformation to compute image ranks of powers, and compares these ranks with the exact parent-forest descendant criterion, allowing the root correction. The exhaustive run checked 23,713 maps and ended with \(\texttt{VERIFY\_OK}\). For \(n=10\), the aggregate image-rank numerators for powers \(k=0,1,2,3,4\) are respectively \(167960,92378,66197,52668,45695\), over 16,796 transformations; the finite-size ratios are not asserted to equal their limits. The probabilistic limit uses the published fringe-subtree theorem, not finite experiments.

## Relationship to prior work
The Catalan monoid and Catalan counting formula are classical. Toker [1] works with this exact order-preserving regressive monoid and studies its zero-divisor graph, not the decay of intermediate image ranks. Ayık–Ayık–Koç [2] determine the fixed-point spectrum; the fixed-point estimate in step 3 is prior knowledge. Yağcı–Korkmaz [3] enumerate \(m\)-potent and \(m\)-nilpotent elements of the same monoid, and even fixed-set-conditioned potency counts: **the stabilization-time distribution is therefore not a new contribution**. Those counts do not themselves state the normalized image-rank decay for each intermediate power. The generic conditioned Galton–Watson fringe law of Janson [4] is also prior knowledge; the algebra-specific identification of successive image ranks with a fringe survival statistic is the bridge used here. A broader literature statement may already identify this particular application, so priority remains provisional.

## Limitations
This is a fixed-exponent asymptotic. No rate of convergence, growing-exponent regime, fluctuation law, or claim about nonregressive maps is established. Existing exact potency enumerations supersede any claim of new stabilization-index enumeration. The proof relies on the published empirical-fringe theorem, invoked within its standard bounded-indicator assumptions. The result has not received independent mathematical audit or comprehensive publication-priority verification.

## References
[1] K. Toker, “Zero-divisor graphs of Catalan monoid,” *Hacettepe J. Math. Stat.* 50 (2021), 387–396, DOI:10.15672/hujms.702478 (published April 11, 2021).

[2] G. Ayık, H. Ayık and M. Koç, “Combinatorial results for order-preserving and order-decreasing transformations,” *Turkish J. Math.* 35 (2011), 617–625, DOI:10.3906/mat-1010-432.

[3] M. Yağcı and E. Korkmaz, “On Elements of Finite Semigroups of Order-Preserving and Decreasing Transformations,” *Bull. Malaysian Math. Sci. Soc.* 43 (2020), 3863–3870, DOI:10.1007/s40840-020-00899-7.

[4] S. Janson, “Asymptotic normality of fringe subtrees and additive functionals in conditioned Galton–Watson trees,” arXiv:1312.1211 (2013), *Random Structures & Algorithms* 48 (2016), 57–101.
