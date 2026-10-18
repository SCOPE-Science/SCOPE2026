# Strict conditional root-degree ordering by parity-class size in uniform labeled trees

## Finding
Fix an integer \(n\ge3\). Draw a uniformly random tree from the \(n^{n-2}\) labeled trees on \(\{1,\ldots,n\}\) and root it at vertex 1. Let \(A\) be the number of vertices at even graph distance from the root, including the root, let \(B=n-A\), and let \(D\) be the root degree. For each integer \(1\le a\le n-1\),
\[
\Pr(A=a)=\binom{n-1}{a-1}\frac{a^{n-a-1}(n-a)^{a-1}}{n^{n-2}},
\qquad D\mid(A=a)\stackrel d=1+\operatorname{Binomial}(n-a-1,1/a).
\]
The conditional laws are **strictly decreasing in likelihood-ratio order** as \(a\) increases. Thus, for any strictly increasing real functions \(f\) and \(g\) on the finite supports,
\[
\operatorname{Cov}(f(D),g(A))<0.
\]
A more detailed conditional statement describes all degrees at once. Condition on the actual bipartition \((V_0,V_1)\) of the tree into even- and odd-depth vertices, with \(|V_0|=a\), \(|V_1|=b=n-a\). Then the two full excess-degree vectors are independent:
\[
(\deg(v)-1)_{v\in V_0}\sim\operatorname{Multinomial}(b-1;1/a,\dots,1/a),\qquad
(\deg(w)-1)_{w\in V_1}\sim\operatorname{Multinomial}(a-1;1/b,\dots,1/b).
\]
For a deterministic integer sequence \(a=a(n)\) with \(a/n\to\theta\in(0,1)\), the root degree has the conditional limit
\[
D\mid(A=a(n))\ \xrightarrow{d}\ 1+\operatorname{Poisson}\bigl((1-\theta)/\theta\bigr).
\]

## Assumptions and scope
All labeled trees are equally likely. Distances are ordinary undirected graph distances. The root is the vertex labeled 1. The even/odd sets are defined from this root, and both are nonempty for \(n\ge2\). Conditional on an *actual* bipartition, its vertex sets are fixed; conditional only on the size \(A=a\), the nonroot even labels are uniformly distributed among the \(\binom{n-1}{a-1}\) possible subsets. The endpoint laws are included: for \(a=1\), \(D=n-1\) with probability one; for \(a=n-1\), \(D=1\) with probability one. The strict covariance assertion requires both test functions strictly increasing; merely nondecreasing functions can be constant.

## Proof
**Bipartite representation.** Every tree has a unique proper two-coloring in which vertex 1 has color zero. Fix a color-zero set \(V_0\) containing 1, with size \(a\); its complement \(V_1\) has size \(b\). Trees with this color assignment are exactly the spanning trees of the complete bipartite graph \(K_{a,b}\). Their number is \(a^{b-1}b^{a-1}\), the classical complete-bipartite tree count. Multiplying by the \(\binom{n-1}{a-1}\) root-containing choices and dividing by Cayley's \(n^{n-2}\) yields the displayed marginal law of \(A\).

**Weighted degree enumerator.** Give each vertex \(v\in V_0\) a variable \(x_v\) and each \(w\in V_1\) a variable \(y_w\). Give edge \(vw\) weight \(x_vy_w\). A weighted matrix-tree determinant, or equivalently the two-word bipartite Prüfer coding, gives
\[
\sum_{T\text{ spanning tree of }K_{a,b}}
\prod_{v\in V_0}x_v^{\deg_T(v)-1}
\prod_{w\in V_1}y_w^{\deg_T(w)-1}
=\Bigl(\sum_{v\in V_0}x_v\Bigr)^{b-1}
\Bigl(\sum_{w\in V_1}y_w\Bigr)^{a-1}.
\]
For completeness, this identity follows by deleting one row and column of the weighted Laplacian of \(K_{a,b}\), taking its Schur complement and factoring the result as the full edge-weight tree polynomial \((\prod x_v)(\prod y_w)(\sum x_v)^{b-1}(\sum y_w)^{a-1}\), then dividing by \((\prod x_v)(\prod y_w)\). It is valid also when one class has size one. After dividing by the value at all variables equal to one, the displayed polynomial factors into the two probability-generating polynomials of independent uniform multinomials. For root 1 in \(V_0\), its excess degree is \(\operatorname{Binomial}(b-1,1/a)\). This law does not depend on which other vertices lie in \(V_0\), so it holds conditional only on \(A=a\).

**Strict likelihood-ratio order.** Write \(p_a(d)=\Pr(D=d\mid A=a)\). For \(a>1\) and consecutive values in its support,
\[
\frac{p_a(d+1)}{p_a(d)}=\frac{n-a-d}{d(a-1)},\qquad 1\le d<n-a.
\]
For fixed admissible \(d\), this ratio strictly decreases when \(a\) increases: the numerator decreases and the denominator increases. Meanwhile the supports \(\{1,\dots,n-a\}\) are nested. These observations give the strict reverse likelihood-ratio order (the comparison with \(a=1\) follows because its distribution is concentrated at the largest possible degree). In particular, coupling the independent Bernoulli trials or applying stochastic-order theory gives strict stochastic ordering for each neighboring pair of \(a\)'s. Therefore \(\mathbb E[f(D)\mid A=a]\) strictly decreases with \(a\) for every strictly increasing \(f\). For independent copies \(A,A'\), the covariance identity
\[
2\operatorname{Cov}(f(D),g(A))
=\mathbb E\big[(g(A)-g(A'))(h(A)-h(A'))\big],
\qquad h(a)=\mathbb E[f(D)\mid A=a],
\]
is strictly negative because every value \(1\le a\le n-1\) has positive probability, \(g\) is strictly increasing, and \(h\) is strictly decreasing.

**Poisson limit.** If \(a/n\to\theta\in(0,1)\), then \(n-a-1\to\infty\), \(1/a\to0\), and \((n-a-1)/a\to(1-\theta)/\theta\). The elementary binomial-to-Poisson limit proves the final assertion.

## Verification
The companion standard-library script `verify.py` independently enumerates all Prüfer sequences through \(n=7\), checks every finite conditional root-degree mass and color-class count as rational identities, checks adjacent conditional survival probabilities, and separately checks the complete bipartite degree-vector counts for selected partitions. It completes 340 exact assertions. These finite checks are confirmations; the weighted determinant, likelihood-ratio argument, and binomial limit establish the universal result.

## Relationship to prior work
The enumeration \(a^{b-1}b^{a-1}\) of spanning trees of \(K_{a,b}\), as well as bipartite degree-generating identities, is classical and **not** claimed as new. Scoins studied trees with alternating-parity color classes (1962); Hartsfield and Werth gave a bipartite spanning-tree enumeration proof (1990). Janson (arXiv:math/0509471, first posted 21 September 2005), especially Section 2.3 and Theorem 2.12, studied the limiting distribution of depth-congruence class sizes in conditioned Galton–Watson trees, including Cayley trees. The contribution here is the explicit degree-profile conditioning on the root's parity-class size and the complete strict likelihood-ratio/negative-regression ordering, with its conditional local Poisson limit. A published result on root degree conditioned on distance to a *single marked vertex* concerns a different sigma-field and does not yield this conditioning without further proof.

## Limitations
This is a finite-tree theorem in the uniform *labeled*, not recursive-tree, model. It asserts stochastic dependence, not independence, between \(D\) and \(A\). The marginal color-class size distribution and bipartite Prüfer generating function have historical antecedents, so only the assembled conditional ordering and its consequences are assessed as potentially original. An inaccessible original source by Scoins may contain an implicit statement: historical priority is not independently certified. The formula for the limit assumes a sequence of conditioning levels with a positive interior fraction, not extreme levels.

## References
- Scoins, H. I., *The number of trees with nodes of alternate parity*, Proceedings of the Cambridge Philosophical Society 58 (1962), 12–16, doi:10.1017/S0305004100036173.
- Hartsfield, N. and Werth, J. S., *Spanning Trees of the Complete Bipartite Graph*, in *Topics in Combinatorics and Graph Theory* (1990), 339–346, doi:10.1007/978-3-642-46908-4_38.
- Janson, S., *Congruence properties of depths in some random trees*, arXiv:math/0509471v1 (posted 21 September 2005), Sections 2.3 and 5.
