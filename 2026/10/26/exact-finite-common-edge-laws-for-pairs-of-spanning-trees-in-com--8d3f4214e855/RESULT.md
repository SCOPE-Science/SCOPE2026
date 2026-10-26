# Exact finite common-edge laws for pairs of spanning trees in complete bipartite graphs

## Finding

Let \(K_{a,b}\) have labelled bipartition classes \(A\) and \(B\), of sizes \(a\) and \(b\). Independently and uniformly choose two spanning trees \(T_1,T_2\) and put \(X_{a,b}=|E(T_1)\cap E(T_2)|\).

**Theorem 1 (exact binomial core).** For all integers \(a\ge2\) and \(b\ge2a-2\), there exists an integer-valued random variable \(Y_{a,b}\), supported on \(\{0,1,\ldots,3(a-1)\}\), such that
\[
X_{a,b}\ \overset{\mathrm d}{=}\ \operatorname{Bin}\!\left(b-2a+2,\frac1a\right)+Y_{a,b},
\]
with the two summands independent. Thus the probability-generating polynomial is divisible over the nonnegative probability-polynomial semiring by \(\big((a-1+t)/a\big)^{b-2a+2}\). This is an **exact finite-size** statement, not only an asymptotic approximation.

**Theorem 2 (complete three-by-\(n\) law).** For every integer \(n\ge4\), set
\[
p(t)=\frac{2+t}{3},\qquad q(t)=\frac{1+2t}{3}.
\]
Then the entire overlap distribution for two independent uniform spanning trees of \(K_{3,n}\) is given by
\[
\mathbb E[t^{X_{3,n}}]=p(t)^{n-4}\,Q_n(t),
\]
where the nonnegative probability polynomial of degree at most six is
\[
\begin{aligned}
Q_n(t)=\frac1{n^3}\bigg[&
(n-1)(n-2)(n-3)q(t)^4\\
&+\frac{2(n-1)(n-2)}3(7t+2t^2)q(t)^2p(t)\\
&+(n-1)p(t)^2\left(t^2+4t^2q(t)+\frac{t^4+2t^3+3t^2}{3}\right)\\
&+t^3p(t)^3\bigg].
\end{aligned}
\]
In particular, \(X_{3,n}\overset{\mathrm d}{=}\operatorname{Bin}(n-4,1/3)+Y_n\), with \(Y_n\) independent and supported on \(\{0,1,\ldots,6\}\).

**Corollary (exact tree-packing census).** For \(n\ge4\),
\[
\Pr(X_{3,n}=0)=\frac{(n-1)(n-2)(n-3)}{81n^3}\left(\frac23\right)^{n-4}.
\]
The number of **ordered**, edge-disjoint pairs of spanning trees of labelled \(K_{3,n}\) is therefore exactly
\[
9n(n-1)(n-2)(n-3)6^{n-4}.
\]
Moreover,
\[
\mathbb E X_{3,n}=\frac{(n+2)^2}{3n},\qquad
\operatorname{Var}(X_{3,n})=\frac{2(n-1)(n^2+n+1)}{9n^2}.
\]

## Assumptions and scope

Graphs are finite, simple, undirected, and labelled; the bipartition is fixed. The two random trees are independent and each is uniform among **all** spanning trees of its graph. A common edge means an identical unordered edge of the original labelled graph; an ordered pair of spanning trees distinguishes the first tree from the second. Theorem 1 requires \(a\ge2\), \(b\ge2a-2\); Theorem 2 and its corollary require \(n\ge4\). Probability polynomials are formal polynomials, and distributional equality does not assert independence of the original edge indicators.

## Proof

**1. A bounded skeleton.** In every spanning tree \(T\) of \(K_{a,b}\), the sum of degrees of its \(b\) vertices on side \(B\) is \(a+b-1\). Thus
\[
\sum_{v\in B}(\deg_T(v)-1)=a-1.
\]
At most \(a-1\) vertices on side \(B\) can have degree greater than one. Denote their set by \(C_T\) (the *core*), and retain all edges of \(T\) incident with it to form its *skeleton* on \(A\cup C_T\). Each omitted vertex of \(B\) has degree exactly one. Deleting those leaves preserves connectivity and acyclicity on the remaining vertices, so this skeleton is a tree on \(A\cup C_T\). Conversely, attach each vertex of \(B\setminus C_T\) by a single edge to **any** vertex of \(A\); the resulting graph is a spanning tree with precisely the same core. Hence, conditional on the core and skeleton, all these attachments are independent and uniform choices from the \(a\) vertices of \(A\). No tree is counted twice, because its core and skeleton are unique.

**2. Extracting an exactly independent binomial component.** Condition on both skeletons and set \(U=C_{T_1}\cup C_{T_2}\) and \(r=|U|\le2(a-1)\). Each of the \(b-r\) vertices in \(B\setminus U\) is a leaf in both trees, and its two independent uniform attachments coincide with probability \(1/a\). These coincidence indicators are independent across vertices and independent of all intersection contributions at the core vertices \(U\), conditional on the skeletons. Thus the conditional generating polynomial factors as
\[
\left(\frac{a-1+t}{a}\right)^{b-r}H_U(t)
\]
for a probability polynomial \(H_U(t)\) with nonnegative coefficients. Let \(s=2(a-1)\), and factor out the common term \(((a-1+t)/a)^{b-s}\); the residual conditional polynomial is \(((a-1+t)/a)^{s-r}H_U(t)\). Averaging over skeleton pairs gives a probability polynomial \(R_{a,b}(t)\) with nonnegative coefficients and \(R_{a,b}(1)=1\). Moreover, every overlap contains at most \(a+b-1\) edges. Since the common binomial factor has strictly positive leading coefficient, \(\deg R_{a,b}\le(a+b-1)-(b-s)=3(a-1)\). Taking an independent variable with probability polynomial \(R_{a,b}\) establishes Theorem 1.

**3. Enumerating the three-by-\(n\) skeletons.** Suppose \(a=3\). Since the excess degree sum on \(B\) is two, the only skeleton types are:

- Type I: one distinguished \(B\)-vertex of degree three, joined to all three vertices of \(A\). There are \(n\) possible skeletons; each extends to \(3^{n-1}\) full trees.
- Type II: two distinguished \(B\)-vertices of degree two each, whose four edges form a path joining the three vertices of \(A\). There are \(3n(n-1)\) skeletons, each extending to \(3^{n-2}\) full trees.

Consequently the total number of trees is \(n3^{n-1}+3n(n-1)3^{n-2}=n^2 3^{n-1}\). Each specified type-I skeleton has probability \(1/n^2\) and each specified type-II skeleton probability \(1/(3n^2)\). In the following table, the count is the number of **ordered skeleton pairs** of the stated type; the last column is the conditional overlap probability polynomial, including the \(B\)-vertices that are leaves in both trees.

| Ordered skeleton relation | Count | Conditional polynomial |
|---|---:|---|
| I–I, same core vertex | \(n\) | \(t^3p^{n-1}\) |
| I–I, distinct core vertices | \(n(n-1)\) | \(t^2p^{n-2}\) |
| I–II or II–I, disjoint cores | \(6n(n-1)(n-2)\) | \(tq^2p^{n-3}\) |
| I–II or II–I, one shared core | \(12n(n-1)\) | \(t^2qp^{n-2}\) |
| II–II, disjoint cores | \(9n(n-1)(n-2)(n-3)\) | \(q^4p^{n-4}\) |
| II–II, one shared core, same incident two-edge set | \(12n(n-1)(n-2)\) | \(t^2q^2p^{n-3}\) |
| II–II, one shared core, different incident two-edge sets | \(24n(n-1)(n-2)\) | \(tq^2p^{n-3}\) |
| II–II, both cores shared; respectively \(4,3,2\) common skeleton edges | \(3n(n-1),6n(n-1),9n(n-1)\) | \(t^4p^{n-2},t^3p^{n-2},t^2p^{n-2}\) |

Here \(p\) is the overlap polynomial for two independent choices among three neighbours; \(q\) is the overlap polynomial of a uniformly attached leaf with a predetermined two-edge star. In the II–II row with both core labels shared, fixing the first skeleton leaves exactly six possibilities for the second; their numbers of common skeleton edges are respectively \(4,3,2\) with multiplicities \(1,2,3\). The stated row counts follow by choosing labelled core vertices and the middle vertex of each three-vertex path.

**4. Summation and normalization.** Multiply each table entry by the product of its skeleton probabilities, namely \(1/n^4\) for I–I, \(1/(3n^4)\) for I–II, and \(1/(9n^4)\) for II–II. Their sum, grouped by powers of \(p\), is precisely \(p^{n-4}Q_n\). Every summand is a nonnegative polynomial; hence \(Q_n\) has nonnegative coefficients, and evaluating at \(t=1\) gives \(Q_n(1)=1\). This proves Theorem 2. Differentiating the displayed expression at \(t=1\), and using the standard first and second factorial moments of a probability generating function, yields the stated mean and variance.

**5. Edge-disjoint pairs.** The only row that can contribute a constant coefficient is II–II with four distinct core vertices: every other row has at least one forced common edge. At each of the four core vertices, the other tree must attach its leaf to the unique vertex of \(A\) outside the first tree's two-edge neighbourhood, giving one choice. Each of the other \(n-4\) vertices has \(3\cdot2=6\) choices for two different leaf attachments. There are \(9n(n-1)(n-2)(n-3)\) ordered pairs of disjoint-core type-II skeletons. This independently gives \(9n(n-1)(n-2)(n-3)6^{n-4}\) ordered edge-disjoint tree pairs. Dividing by the square of the total tree count gives the stated zero-overlap probability.

## Verification

The self-contained Python standard-library program `verify.py` constructs trees from edge subsets using a disjoint-set forest test and, independently, evaluates the rational polynomial in Theorem 2. It compares all overlap probabilities for \(n=4\) and \(n=5\): respectively \(432\) trees and \(186{,}624\) ordered pairs; \(2025\) trees and \(4{,}100{,}625\) ordered pairs. It checks the zero-overlap count independently, and exact coefficient positivity, normalization, mean, variance and zero-overlap formulas for every \(4\le n\le40\). The replay result is `VERIFY_OK exhaustive_pairs= 4287249 additional_rational_laws= 37`. Finite tests only corroborate the all-parameter proof above.

## Relationship to prior work

Bóna, Burghart and Wagner study intersections of independently sampled spanning trees, prove asymptotic laws for several graph classes, and explicitly observe that the fixed-small-side complete-bipartite case is *approximately* binomial; their discussion does not give the finite-size polynomial or ordered tree-packing census above. The general exact binomial extraction, explicit \(K_{3,n}\) correction polynomial, and closed-form zero-overlap enumeration strengthen that qualitative observation. Dong and Ge enumerate spanning trees **containing a prescribed forest**, a different count from the whole overlap distribution of a random *pair*; their extension identity provides relevant background but not the stated formulas by itself. A separate two-row overlap identity for \(K_{2,b}\) is a smaller special case, not a determination of the \(K_{3,n}\) polynomial. No assertion of definitive historical priority is made.

## Limitations

The exact independent binomial-factor theorem requires \(b\ge2a-2\), and the explicit bounded-degree correction is computed here for \(a=3\), \(n\ge4\). The construction of \(Y_{a,b}\) for general \(a\) is an existence proof via probability polynomials; it does not give an explicit closed form for that residual distribution. The zero-overlap census is for **ordered** pairs of labelled spanning trees and does not count unoriented decomposition classes. This report does not treat nonuniform spanning-tree distributions or arbitrary bipartite graphs. Historical priority and the proof are not independently audited.

## References

1. M. Bóna, F. Burghart and S. Wagner, *On the intersection of pairs of trees*, arXiv:2501.18570 (first public version 2025-01-30; version 4, 2026-09-09), especially §5, https://arxiv.org/html/2501.18570v4.
2. F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294, https://arxiv.org/abs/2103.05294.
3. W. Wang and J. Ge, *On enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, arXiv:2602.03602, https://arxiv.org/abs/2602.03602.
