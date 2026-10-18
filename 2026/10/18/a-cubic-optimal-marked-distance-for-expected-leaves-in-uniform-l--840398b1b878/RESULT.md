# A cubic-optimal marked distance for expected leaves in uniform labeled trees

## Finding

Let \(T_n\) be a uniform unrooted labeled tree on the vertex set \([n]\), where \(n\ge 2\). Fix two distinct marked vertices \(u,v\). Let \(D=d_{T_n}(u,v)\) be their graph distance and let \(L\) be the *total* number of unrooted leaves (vertices of degree one, including either marked vertex when appropriate). Every distance \(1\le k\le n-1\) has positive probability. The exact conditional mean is
\[
\boxed{\mu_n(k):=\mathbb E[L\mid D=k]
 =\left(n-k+1-\frac{2}{k+1}\right)
\left(1-\frac1n\right)^{n-k-2}.}
\tag{1}
\]
For every \(1\le k\le n-2\), consecutive means obey
\[
\boxed{\mu_n(k+1)-\mu_n(k)
=\frac{2(n-1)-k(k+1)^2}{n(k+1)(k+2)}
\left(1-\frac1n\right)^{n-k-3}.}
\tag{2}
\]
Consequently, define the first nonnegative-sign-change index
\[
k_*(n):=\min\{k\in\{1,\ldots,n-1\}: k(k+1)^2\ge 2(n-1)\}.
\]
The set of **all** maximizing distances is \(\{k_*(n)\}\), except that if \(k_*(n)(k_*(n)+1)^2=2(n-1)\), it is exactly \(\{k_*(n),k_*(n)+1\}\). The latter equality is possible only when the second index is in range (automatically so for \(n\ge3\)); it occurs at infinitely many values \(n=1+k(k+1)^2/2\) for integers \(k\ge1\). For \(n=2\) there is only distance one, with one maximizer.

As \(n\to\infty\),
\[
\boxed{k_*(n)\sim(2n)^{1/3},\qquad
\max_{1\le k\le n-1}\mu_n(k)-\mathbb E L\longrightarrow e^{-1}.}
\tag{3}
\]
In particular, the distance maximizing total expected leaves is on a cube-root rather than the classical square-root scale of a typical marked-pair distance. This is an exact finite-sample *conditional-mean* result; it does not assert concentration or distributional ordering of leaf counts.

## Assumptions and scope

The law on labeled trees is uniform among all \(n^{n-2}\) possibilities. Both marks are fixed distinct labels; exchangeability allows uniform distinct sampled marks as well. Distances count edges. The term “leaf” refers to an unrooted degree-one vertex and not to a rooted terminal node. Set \(q=1-1/n\). In (1) and (2), negative integer exponents at the farthest-distance endpoint are interpreted as ordinary rational powers; no limiting convention is needed.

For \(n\ge3\), the index \(k_*(n)\) lies at most \(n-2\); thus a two-point tie never references an impossible distance. At \(n=3\), exactly distances one and two tie. The ordinary unconditioned expectation is \(\mathbb E L=nq^{n-2}\), and (1) gives the exact identity \(\mu_n(1)=\mathbb E L\). These classical marginal/edge-symmetry facts are not novelty claims.

## Proof

**1. Count a prescribed marked path.** Write \((a)_{b}=a(a-1)\cdots(a-b+1)\) for a falling factorial. The classical forest-extension identity says that a fixed forest on \([n]\) with component sizes \(s_1,\ldots,s_c\) occurs in precisely \(n^{c-2}\prod_i s_i\) labeled trees. To have \(D=k\), choose an ordered list of \(k-1\) distinct intermediate vertices and require the resulting \(u\)-to-\(v\) path. Its vertex set forms a single component of size \(k+1\), and the other \(n-k-1\) vertices are isolated. Hence the number of trees with \(D=k\) is
\[
A_{n,k}=(n-2)_{k-1}(k+1)n^{n-k-2},\qquad 1\le k\le n-1.
\tag{4}
\]
At \(k=n-1\), the power \(n^{-1}\) cancels the factor \(k+1=n\), giving \((n-2)!\); the formula also works at \(n=2\).

**2. Off-path leaves.** For a specific third vertex \(w\notin\{u,v\}\), if \(w\) is a leaf and \(D=k\), deleting \(w\) leaves a tree on \(n-1\) labels with the same marked distance, and the deleted leaf had exactly \(n-1\) attachment choices. For \(k\le n-2\),
\[
\Pr(w\text{ leaf}\mid D=k)
=\frac{(n-1)A_{n-1,k}}{A_{n,k}}
=\frac{n-k-1}{n-2}q^{n-k-2}.
\tag{5}
\]
When \(k=n-1\) there are no off-path vertices, and the total off-path contribution is again zero. Summing (5) over \(n-2\) exchangeable nonmarked vertices gives the conditional expected number of nonmarked leaves:
\[
(n-k-1)q^{n-k-2}.
\tag{6}
\]

**3. Marked endpoint leaves.** For \(k\ge2\), requiring \(u\) to be a leaf means it is the endpoint of the marked path. Delete \(u\), count a distance-\((k-1)\) tree on \(n-1\) vertices between its former neighbor and \(v\), and choose that neighbor in \(n-2\) ways. Dividing by (4) gives
\[
\Pr(u\text{ leaf}\mid D=k)
=\frac{(n-2)A_{n-1,k-1}}{A_{n,k}}
=\frac{k}{k+1}q^{n-k-2}.
\tag{7}
\]
At \(k=1\), a leaf at \(u\) must attach to \(v\). Removing \(u\) directly gives \(\Pr(u\text{ leaf}\mid D=1)=\tfrac12q^{n-3}\), the same as (7). At \(n=2\) the only tree has both endpoints leaves, again agreeing with (7). By symmetry both marked endpoints together contribute \(2kq^{n-k-2}/(k+1)\). Adding this to (6) yields (1).

**4. Exact extremum.** Substitute \(k\) and \(k+1\) into (1), put over the common positive factor \(q^{n-k-3}/[n(k+1)(k+2)]\), and simplify. The resulting numerator is exactly \(2(n-1)-k(k+1)^2\), proving (2). The function \(k\mapsto k(k+1)^2\) is strictly increasing for positive integers. Thus \(\mu_n(k)\) strictly increases up to \(k_*(n)\), then strictly decreases, with a single horizontal step exactly when equality holds; this proves the complete maximizer and tie statements. The equality parameter \(n=1+k(k+1)^2/2\) is an integer for every integer \(k\ge1\), since \(k(k+1)^2\) is even, and the resulting \(k+1\) is a valid distance. (For \(n=2\) there is just one distance.)

**5. Asymptotic position and height.** The extremal criterion implies
\[
(k_*(n)-1)k_*(n)^2<2(n-1)\le k_*(n)(k_*(n)+1)^2,
\]
with the left inequality omitted when \(k_*(n)=1\). Taking cube roots shows \(k_*(n)\sim(2n)^{1/3}\). For any sequence \(k=k(n)=O(n^{1/3})\), the elementary expansion \(\log(1-1/n)=-1/n-1/(2n^2)+O(n^{-3})\) in (1) gives, uniformly on that scale,
\[
\mu_n(k)=e^{-1}\left(n+\frac52-\frac{2}{k+1}\right)+O(n^{-1/3}).
\tag{8}
\]
At \(k=k_*(n)\), the last fraction tends to zero, so \(\max_k\mu_n(k)=e^{-1}(n+5/2)+o(1)\). In contrast, \(\mu_n(1)=\mathbb E L=nq^{n-2}=e^{-1}(n+3/2)+O(n^{-1})\). Subtracting proves (3). The classical pair-distance law from (4) lives on the \(\sqrt n\) scale; this is distinct from the maximizer of the conditioned leaf mean.

## Verification

A standalone exact-rational program `verify.py` replays the model, definitions, and formulas. It exhaustively enumerates all \(n^{n-2}\) Prüfer codes for \(2\le n\le7\), computes the marked-path length and number of degree-one vertices in each tree, and checks (4), (1), (5)–(7), and (2). It then checks all discrete sign transitions and extremizing indices for \(2\le n\le300\). Its output is `passed 994 exact assertions`. All finite tests supplement the independent all-size counting argument in the proof; they are not an infinite certificate.

Run with standard Python 3: `python verify.py`. The checker uses only the standard library and computes exact rational quantities.

## Relationship to prior work

Berzunza Ojeda and Janson (arXiv:2009.00572, first public version 2020-09-01; primary MSC2020 60C05) analyze the distance profile of rooted and unrooted simply generated random trees, including the Cayley case and leaf marking. Their full open text provides asymptotic distance-profile results and leaf-bias constructions, but no stated finite regression of *total* leaves against a *fixed marked-pair distance* or a cubic-scale maximizer.

Addario-Berry, Donderwinkel, Maazoun and Martin (arXiv:2107.09726, first public version 2021-07-20) give a modern account of Cayley and rooted-forest counting and explicit random-tree distance arguments. Their open article supplies natural background for (4); the inspected sections do not state the total-leaf conditional mean, its sign-changing discrete derivative, or its optimizing scale.

A published exact degree-versus-distance result for uniform Cayley trees (published-finding corpus, “Exact negative regression between endpoint degree and distance in a uniform Cayley tree,” identifier `d9ddfb06a9ae`) gives the conditional distribution of the degree of **one marked endpoint** at a specified distance. That implies the marked-endpoint portion (7), but not the off-path leaf contribution (6) or the complete conditional total-leaf optimizer. The present assertion is not a claim of novelty for that endpoint-degree law, for the forest-extension identity, or for the unconditioned mean of leaves.

Targeted searches for conditional Cayley-tree leaf counts, marked-distance regression, equivalent bivariate generating functions, and a cube-root maximizer found no explicit version of the complete extremal classification. Absence of a retrieved match is not proof of absolute novelty; an older general joint generating function may yield the same formula upon specialization.

## Limitations

The result is an exact conditional **expectation** for uniform labeled trees, not a conditional distribution law, stochastic ordering, leaf variance formula, or universality statement for other random-tree models. The optimizing excess above the marginal leaf mean tends to the finite constant \(e^{-1}\), rather than increasing with \(n\). The crucial forest-extension identity is classical. Historical-priority uncertainty remains about possible implicit equivalents under generating-function notation. Independent external mathematical validation has not been performed.

## References

1. G. Berzunza Ojeda and S. Janson, “The distance profile of rooted and unrooted simply generated trees,” arXiv:2009.00572 (first posted 2020-09-01); *Combinatorics, Probability and Computing* 31 (2022), 368–410, DOI 10.1017/S0963548321000304. Primary MSC2020 60C05.
2. L. Addario-Berry, S. Donderwinkel, M. Maazoun and J. B. Martin, “The Foata–Fuchs proof of Cayley’s formula, and its probabilistic uses,” arXiv:2107.09726 (first posted 2021-07-20); *Electronic Communications in Probability* 28 (2023), article 32, DOI 10.1214/23-ECP523.
3. J. Pitman, “Coalescent Random Forests,” Berkeley Statistics Technical Report 457 (1996), later *Journal of Combinatorial Theory, Series A* 85 (1999), 165–193. Background on forest-extension counting.
4. “Exact negative regression between endpoint degree and distance in a uniform Cayley tree,” published published-finding corpus mathematical finding, identifier `2026/10/4/SCOPE-exact-negative-regression-between-endpoint-degree-and-distance-i--d9ddfb06a9ae` (published 2026). Closest explicit finite conditioned degree result, distinct from total leaf counts.
