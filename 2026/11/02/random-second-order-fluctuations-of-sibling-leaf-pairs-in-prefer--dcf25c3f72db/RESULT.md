# Random second-order fluctuations of sibling-leaf pairs in preferential attachment trees

## Finding
Consider a random tree \(T_n\) started from one edge at \(n=2\). Each new vertex attaches to an existing vertex with probability proportional to the existing vertex's undirected degree. For a vertex \(v\), let \(d_v(n)\) be its degree and \(\ell_v(n)\) the number of its neighbors that are leaves. Count each **unordered pair of leaves with a common neighbor** once, even if that neighbor has more than two leaves:
\[
 C_n=\sum_{v\in T_n}\binom{\ell_v(n)}2.
\]
Put \(H_0=0\) and \(H_j=\sum_{k=1}^{j}k^{-1}\). Then, for every integer \(n\ge3\),
\[
 \boxed{\mathbb E C_n=1+\frac{n-1}{4}H_{n-3}-\frac{n(n-3)}{8(n-2)}.}
\]
Define the quadratic-degree process
\[
 M_n=\frac{\sum_{v\in T_n}d_v(n)^2}{n-1}-2H_{n-1},\qquad n\ge2.
\]
It is an \(L^2\)-bounded martingale with a nondegenerate almost-sure and \(L^2\) limit \(M_\infty\). With \(\gamma\) denoting Euler's constant,
\[
 \boxed{\frac{C_n}{n}-\frac14\log n\ \xrightarrow[n\to\infty]{\mathrm{a.s.},\,L^2}\ \frac\gamma4-\frac18+\frac18M_\infty.}
\]
In particular \(C_n/(n\log n)\to1/4\) almost surely and in \(L^2\); the centered order-\(n\) correction has a nonconstant random limit, with variance at least \(1/576\). No Gaussian distribution is asserted for that limit.

## Assumptions and scope
The graph is a simple labeled tree; at size two it is the deterministic edge between vertices 1 and 2. Conditionally on \(T_n\), its next attachment vertex \(V_n\) satisfies
\[
 \Pr(V_n=v\mid T_n)=\frac{d_v(n)}{2(n-1)},\qquad v\in T_n,\quad n\ge2.
\]
The new vertex \(n+1\) is a leaf. Degrees and leaf-neighbor counts are computed in the **unrooted** tree; no choice of root is involved. For \(n=2\), each vertex is a leaf and the stated conditional recurrences below begin at \(n=3\), when no leaf is adjacent to another leaf. All convergence statements concern the coupling of trees obtained by continuing this same infinite attachment sequence. The logarithm is natural.

## Proof
**1. Closed conditional drift identities.** Write
\[
 S_n=\sum_v d_v(n)^2,\qquad X_n=\sum_v d_v(n)\ell_v(n),\qquad U_n=\sum_v d_v(n)^3.
\]
For \(n\ge3\), an attachment at a nonleaf of degree \(d\) and leaf-neighbor count \(\ell\) changes \((S_n,X_n,C_n)\) by \((2d+2,d+\ell+1,\ell)\). An attachment at a leaf with nonleaf neighbor of degree \(d_w\) and leaf-neighbor count \(\ell_w\) changes them by \((4,2-d_w,-(\ell_w-1))\). Summing these increments with weights \(d_v/[2(n-1)]\), using \(\sum_vd_v=2(n-1)\), \(\sum_vd_v\ell_v=X_n\), and \(\sum_v\ell_v(\ell_v-1)=2C_n\), yields the exact conditional identities
\[
 \begin{aligned}
 \mathbb E(S_{n+1}\mid T_n)&=\frac n{n-1}S_n+2,\\
 \mathbb E(X_{n+1}-X_n\mid T_n)&=1+\frac{S_n}{2(n-1)},\\
 \mathbb E(C_{n+1}\mid T_n)&=\frac{n-2}{n-1}C_n+\frac{X_n}{2(n-1)}.
 \end{aligned}
\]
For the cubic-degree sum, the attachment changes it by \(3d_v^2+3d_v+2\), giving
\[
 \mathbb E(U_{n+1}\mid T_n)=U_n+\frac{3U_n}{2(n-1)}+\frac{3S_n}{2(n-1)}+2.
\]
At size three, \((S_3,X_3,C_3)=(6,4,1)\) deterministically; at size two \(S_2=X_2=2\) and \(C_2=0\).

**2. Exact expectations.** Dividing the first drift identity by \(n\) and telescoping gives
\[
 \mathbb E S_n=2(n-1)H_{n-1}\qquad(n\ge2).
\]
The second then gives \(\mathbb E X_n=2+(n-1)H_{n-2}\) for \(n\ge2\). Multiplying the third by \(n-1\) and summing from size three gives
\[
 (n-2)\mathbb E C_n=1+\tfrac12\sum_{m=3}^{n-1}\mathbb E X_m.
\]
The identity \(\sum_{j=1}^{r}jH_{j-1}=[r(r+1)H_r-r(r+3)/2]/2\), or direct telescoping, reduces this expression to
\[
 \mathbb E C_n=1+\frac{n-1}{4}H_{n-3}-\frac{n(n-3)}{8(n-2)}.
\]
As \(H_{n-3}=\log n+\gamma+o(1)\), we obtain
\[
 \frac{\mathbb E C_n}{n}-\frac14\log n\longrightarrow \frac\gamma4-\frac18.
\]

**3. A nondegenerate quadratic-degree martingale.** Since \(H_n-H_{n-1}=1/n\), the first drift identity shows that \(M_n=S_n/(n-1)-2H_{n-1}\) is a mean-zero martingale. Its increment is exactly
\[
 M_{n+1}-M_n=\frac{2d_{V_n}(n)-S_n/(n-1)}n.
\]
The mean-square increment is bounded by
\[
 \mathbb E[(M_{n+1}-M_n)^2]\le\frac{2\mathbb E U_n}{n^2(n-1)}.
\]
Taking expectations in the cubic recurrence and using \(\mathbb E S_n=2(n-1)H_{n-1}\) gives
\[
 \mathbb E U_{n+1}=\left(1+\frac3{2(n-1)}\right)\mathbb E U_n+3H_{n-1}+2.
\]
The homogeneous product is \(O(n^{3/2})\) and the variation-of-constants forcing is summable after division by this product, since \(\sum_{m\ge3}(1+\log m)m^{-3/2}<\infty\). Thus \(\mathbb E U_n=O(n^{3/2})\). Therefore the martingale's total expected quadratic variation is finite:
\[
 \sum_{n\ge3}\mathbb E[(M_{n+1}-M_n)^2]<\infty.
\]
Consequently \(M_n\to M_\infty\) almost surely and in \(L^2\). At \(n=4\), the tree is a star or a four-vertex path, each with probability \(1/2\), and \(M_4\) is respectively \(1/3\) or \(-1/3\). Hence \(\operatorname{Var}(M_\infty)\ge\operatorname{Var}(M_4)=1/9\), establishing nondegeneracy.

**4. Transfer to the weighted leaf count.** Define martingale differences
\[
 \zeta_{n+1}=X_{n+1}-\mathbb E(X_{n+1}\mid T_n),\qquad n\ge3.
\]
The nonleaf increment satisfies \(|\Delta X|\le 2d_v+1\); the leaf increment satisfies \(|\Delta X|\le d_w+2\). Because the number of leaf neighbors of \(w\) is at most \(d_w\), their degree-weighted conditional second moments are bounded by \(K U_n/(n-1)\), for a deterministic constant \(K\). Thus \(\mathbb E\zeta_{n+1}^2=O(n^{1/2})\) and \(\sum_{n\ge3}\mathbb E\zeta_{n+1}^2/(n+1)^2<\infty\). The martingale series \(\sum_{n\ge3}\zeta_{n+1}/(n+1)\) converges almost surely and in \(L^2\). Kronecker's lemma and orthogonality of differences imply
\[
 \frac1n\sum_{m=3}^{n-1}\zeta_{m+1}\longrightarrow0
 \qquad\text{almost surely and in }L^2.
\]
Subtracting the expectation of the \(X\)-drift and telescoping yields
\[
 X_n-\mathbb E X_n=\frac12\sum_{m=3}^{n-1}M_m+\sum_{m=3}^{n-1}\zeta_{m+1}.
\]
Cesàro convergence therefore implies
\[
 \frac{X_n-\mathbb E X_n}{n}\longrightarrow \frac12M_\infty
 \qquad\text{almost surely and in }L^2.
\]

**5. Transfer to the sibling-leaf pairs.** Let
\[
 \eta_{n+1}=(n-1)\big(C_{n+1}-\mathbb E(C_{n+1}\mid T_n)\big).
\]
The absolute change of \(C\) when attaching to a nonleaf is at most \(d_v\), and when attaching to a leaf neighboring \(w\) is at most \(d_w\). The same cubic-degree argument as above yields \(\mathbb E\eta_{n+1}^2=O(n^{5/2})\) and \(\sum_{n\ge3}\mathbb E\eta_{n+1}^2/(n+1)^4<\infty\). Consequently, by martingale series convergence, Kronecker's lemma and orthogonality,
\[
 \frac1{n^2}\sum_{m=3}^{n-1}\eta_{m+1}\longrightarrow0
 \qquad\text{almost surely and in }L^2.
\]
The third drift identity is equivalent to the exact additive recurrence
\[
 (n-1)C_{n+1}=(n-2)C_n+\frac12 X_n+\eta_{n+1}.
\]
Since \(C_3=1\), subtracting expectations and iterating gives
\[
 \frac{C_n-\mathbb E C_n}{n}=
 \frac{\frac12\sum_{m=3}^{n-1}(X_m-\mathbb E X_m)+\sum_{m=3}^{n-1}\eta_{m+1}}{n(n-2)}.
\]
The weighted Cesàro implication \((X_m-\mathbb E X_m)/m\to M_\infty/2\) together with \(\sum_{m<n}m/n^2\to1/2\) yields
\[
 \frac{C_n-\mathbb E C_n}{n}\longrightarrow\frac18M_\infty
 \qquad\text{almost surely and in }L^2.
\]
Combining with the deterministic expectation asymptotic proves the finding. The variance of the limiting correction is \(\operatorname{Var}(M_\infty)/64\ge1/576\).

## Verification
The accompanying deterministic Python 3 checker uses rational arithmetic to enumerate every degree-proportional attachment history through nine vertices, recomputes degrees and leaf neighbors from the actual tree, verifies all four conditional drift identities at each state, verifies the three expectation formulas for each size, and checks the size-four martingale variance. Its recorded run passed 184,947 exact assertions. Enumeration is deliberately finite; the infinite theorem follows from the martingale proof above and not from this enumeration.

To repeat, save `check.py` beside the document and run `python3 check.py`. It uses only the Python standard library and no network access or supplementary data.

## Relationship to prior work
Hartle and Krapivsky, *Leaves of preferential attachment trees* (arXiv:2602.01021v1, 2026), give the joint degree/leafdegree distribution and its \(m_\ell\sim\ell^{-3}\) tail, plus fluctuations for fixed-degree classes and particular leaf statistics. That tail suggests a logarithmically divergent quadratic leafdegree aggregate but does not by itself justify the finite-size mean or the random order-\(n\) correction. The present statement concerns the global, degree-unbounded quadratic statistic \(\sum_v\binom{\ell_v}2\).

Magner, Janson, Kollias and Szpankowski, *On Symmetry of Uniform and Preferential Attachment Graphs* (2014), use sibling-leaf pairs ('cherries') in their symmetry arguments, without the present exact moments or random-limit law. Holmgren, Janson and Šileikis, *Multivariate normal limit laws for the numbers of fringe subtrees in m-ary search trees and preferential attachment trees* (arXiv:1603.08125, 2016), prove limit laws for counts of **fixed finite** fringe shapes; this unbounded quadratic statistic cannot be identified with any single fixed fringe shape. Literature overlap remains possible through more general additive-functional results, so historical priority is qualified, not definitive.

## Limitations
The model has exactly one added edge per arrival, initial condition a single edge, and degree-proportional attachment without additive attractiveness. No distributional formula, Gaussianity, or exact variance for \(M_\infty\) is proved. The asymptotic lower bound on limiting variance uses only size-four randomness. This result does not claim an extension to other preferential-attachment kernels. Finite-state computational checks do not establish the infinite assertion. An independent mathematical audit and definitive priority review have not been performed.

## References
1. H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021v1, publicly posted February 1, 2026. https://arxiv.org/html/2602.01021
2. A. Magner, S. Janson, G. Kollias and W. Szpankowski, *On Symmetry of Uniform and Preferential Attachment Graphs*, 2014. https://cs.pwr.edu.pl/cichon/Opus5/aofa2014-final-1.pdf
3. C. Holmgren, S. Janson and M. Šileikis, *Multivariate normal limit laws for the numbers of fringe subtrees in m-ary search trees and preferential attachment trees*, arXiv:1603.08125, 2016. https://arxiv.org/abs/1603.08125
4. G. Brightwell and M. Łuczak, *Vertices of high degree in the preferential attachment tree*, arXiv:1012.5550, 2010. https://arxiv.org/abs/1012.5550
