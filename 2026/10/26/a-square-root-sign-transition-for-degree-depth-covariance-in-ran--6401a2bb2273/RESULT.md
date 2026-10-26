# A square-root sign transition for degree–depth covariance in random recursive trees

## Finding

In a uniformly random recursive tree, the covariance between the outdegree of a prescribed vertex and the insertion depth of the last vertex changes sign at a vertex label of order \(\sqrt n\). More precisely, for all integers \(n\ge3\) and \(1\le j<n\),

\[
C_{n,j}:=\operatorname{Cov}(X_{n,j},D_n)
=\frac1j-\sum_{t=j}^{n-1}\frac1{t^2}.
\]

The profile is strictly increasing:

\[
C_{n,j+1}-C_{n,j}=\frac{1}{j^2(j+1)}>0\quad(1\le j\le n-2).
\]

Its endpoints have opposite signs: \(C_{n,1}=-\sum_{t=2}^{n-1}t^{-2}<0\) and \(C_{n,n-1}=(n-2)/(n-1)^2>0\). Write \(j_+(n)\) for the least index with strictly positive covariance. Then

\[
\frac{j_+(n)}{\sqrt n}\longrightarrow\frac1{\sqrt2}.
\]

More precisely, if the integer sequence \(j_n\) obeys \(j_n/\sqrt n\to c>0\), then

\[
n C_{n,j_n}\longrightarrow1-\frac1{2c^2}.
\]

If instead \(j_n-\sqrt{n/2}\to\beta\in\mathbb R\), the critical correction is

\[
n^{3/2}C_{n,j_n}\longrightarrow2\sqrt2\left(\beta-\frac16\right).
\]

Thus the sign transition sits at a square-root label scale, with a nontrivial lattice-scale correction. A zero covariance is allowed at at most one label by strict monotonicity.

## Assumptions and scope

For every integer \(n\ge2\), take vertices with labels \(1,2,\ldots,n\). Vertex \(1\) is the root. Independently for each \(t=2,\ldots,n\), its parent \(P_t\) is uniform on \(\{1,\ldots,t-1\}\). Put \(D_1=0\), \(D_t=1+D_{P_t}\), and \(X_{n,j}=\sum_{t=j+1}^n\mathbf1_{\{P_t=j\}}\). Covariances are under this finite product measure. There is no conditioning on degree, depth, or a tree shape.

The exact formula and sign statements require \(n\ge3\); the asymptotic statements concern \(n\to\infty\). The moment comparison concerns the newest vertex's depth, not the total path length of the tree.

## Proof

Write \(H_m=\sum_{s=1}^m1/s\) and \(H_0=0\). The depth recurrence gives \(\mathbb E D_u=H_{u-1}\). Fix \(t>j\), and let \(A_{t,n}\) denote the event that vertex \(t\) lies on the ancestral path from \(n\) to its root; for \(t=n\), this event is certain. Since \(A_{t,n}\) depends only on parent choices at labels strictly larger than \(t\), it is independent of \(P_t\) and of all depths through label \(t\).

For \(t<n\), induction on the new label proves \(\mathbb P(A_{t,n})=1/t\). Indeed, for \(k>t\),

\[
\mathbb P(A_{t,k})=\frac{1+\sum_{u=t+1}^{k-1}\mathbb P(A_{t,u})}{k-1}.
\]

The base case is \(\mathbb P(A_{t,t+1})=1/t\), and the constant solution \(1/t\) satisfies the recurrence. Set \(a_t:=1+H_{j-1}-H_{t-1}\). Conditional on \(P_t=j\), the expected depth \(D_t\) is \(1+H_{j-1}\), while its unconditional mean is \(H_{t-1}\). On \(A_{t,n}\), changing \(P_t\) changes \(D_n\) exactly through \(D_t\); off that event it has no effect. Therefore independence of the event and parent choice yields

\[
\operatorname{Cov}(\mathbf1_{\{P_t=j\}},D_n)
=\frac{\mathbb P(A_{t,n})}{t-1}\,a_t
=\begin{cases}
\displaystyle\frac{a_t}{t(t-1)},&j<t<n,\\
\displaystyle\frac{a_n}{n-1},&t=n.
\end{cases}
\]

Summing over \(t=j+1,\ldots,n\), using \(a_{t+1}-a_t=-1/t\) and partial summation, gives

\[
\begin{aligned}
\operatorname{Cov}(X_{n,j},D_n)
&=\sum_{t=j+1}^{n-1}\frac{a_t}{t(t-1)}+\frac{a_n}{n-1}\\
&=\frac{a_{j+1}}j+\sum_{t=j+1}^{n-1}\frac{a_{t+1}-a_t}{t}\\
&=\frac1j-\sum_{t=j}^{n-1}\frac1{t^2}.
\end{aligned}
\]

Here an empty sum is zero, covering \(j=n-1\). Subtracting adjacent formulas establishes strict increase. The endpoint expressions follow by substitution.

For asymptotics, the elementary tail expansion, obtainable by Euler–Maclaurin summation or bounding the integrals of a twice-differentiated inverse-square function, is

\[
\sum_{t=j}^{n-1}t^{-2}
=\frac1j+\frac1{2j^2}+\frac1{6j^3}-\frac1n+O(j^{-5}+n^{-2})
\]

as \(j,n\to\infty\) with \(j<n\); the error is uniform when \(j\) is of order \(\sqrt n\). Consequently

\[
C_{n,j}=\frac1n-\frac1{2j^2}-\frac1{6j^3}+O(j^{-5}+n^{-2}).
\]

Substituting \(j/\sqrt n\to c>0\) gives the first limiting profile. Its opposite signs at any two constants on either side of \(1/\sqrt2\), together with strict increase, sandwich the first positive label and prove the threshold. Writing \(j=\sqrt{n/2}+\beta+o(1)\) and Taylor-expanding the preceding formula gives the critical limit \(2\sqrt2(\beta-1/6)\).

## Verification

The standalone script `verify_cov_profile.py` independently enumerates all \((n-1)!\) parent arrays for each \(n\) from \(3\) to \(9\), computes the true mixed moments using rational arithmetic, and compares them to the analytic covariance formula for every admissible label. It also checks rational adjacent-difference and endpoint identities across a wider finite range and tests the scaling threshold numerically. At preparation it printed `PASS exact assertions 4791 including independent exhaustive parent-array enumerations through n=9`. These finite computations check the formulas but do not replace the unrestricted proof.

To reproduce, run `python3 verify_cov_profile.py` with a standard Python 3 installation; no third-party modules or external data are used.

## Relationship to prior work

Devroye, Fawzi and Fraiman study last-inserted depth and height in uniform and scaled-attachment random recursive trees. Their depth limit results do not express its exact finite covariance with the outdegree of an arbitrary prescribed vertex. Kuba and Wagner provide an exact bijective description of depths in increasing trees, but their depth marginal does not yield this cross-vertex covariance profile. Lodewijks studies joint large-sample degree/depth behavior for vertices of prescribed labels, including asymptotic joint distributional results; these do not state or imply the finite exact covariance profile or its order-\(\sqrt n\) sign change at the finer \(1/n\) covariance scale. The rooted-tree literature also studies root-degree correlation with total path length, which is a distinct aggregate statistic, not the depth of the newest vertex.

## Limitations

The formula assumes independent, uniform recursive attachment. Preferential attachment, nonuniform attachment, and general increasing-tree families are not covered. Strict covariance order does not assert stochastic order or a causal effect of degree on depth. A label exactly at zero covariance is not excluded. Originality is provisionally assessed against the material inspected; general earlier covariance identities or unpublished treatments could contain equivalent consequences. Independent validation has not been performed.

## References

1. L. Devroye, O. Fawzi and N. Fraiman, *Depth Properties of Scaled Attachment Random Recursive Trees*, Random Structures & Algorithms 41 (2012), 66–98. First publicly available online December 23, 2011; DOI: 10.1002/rsa.20391. Author-posted full text: https://fraiman.web.unc.edu/wp-content/uploads/sites/12620/2016/08/sarrt.pdf.
2. M. Kuba and S. Wagner, *On the Distribution of Depths in Increasing Trees*, Electronic Journal of Combinatorics 17 (2010), R137. Published October 15, 2010. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v17i1r137/pdf/.
3. B. Lodewijks, *On Joint Properties of Vertices with a Given Degree or Label in the Random Recursive Tree*, arXiv:2204.09032 (initial version April 19, 2022). https://arxiv.org/abs/2204.09032.
