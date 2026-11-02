# Sharp Gaussian positivity exponents on clique-leaf coronas

## Finding
For integers \(n\ge 3\) and \(t\ge 1\), let \(G_{n,t}\) consist of a complete graph on \(n\) core vertices, with exactly \(t\) new pendant vertices joined to each core vertex. Equip its \(N=n(t+1)\) vertices with unweighted shortest-path distance \(d\). Define
\[
F(p)=1+3^p-2^{p+1},\qquad
H_{n,t}(p)=(n-1)F(p)+\left(1-\frac1t\right)2^p-2.
\]
The equation \(H_{n,t}(p)=0\) has a unique root \(\alpha_{n,t}\) in \((1,2)\). For every real \(p\ge0\), the Gaussian distance-power kernel
\[
K_{\lambda,p}(x,y)=\exp\!\left(-\lambda d(x,y)^p\right),\qquad \lambda>0,
\]
is positive semidefinite for **every** \(\lambda>0\) if and only if \(0\le p\le\alpha_{n,t}\). Whenever this holds, the kernel is in fact strictly positive definite for each \(\lambda>0\); whenever \(p>\alpha_{n,t}\), it is indefinite at every sufficiently small positive \(\lambda\).

The power-distance matrix is strictly conditionally negative definite below \(\alpha_{n,t}\). At \(p=\alpha_{n,t}\), its restriction to the mean-zero coefficient space has a **one-dimensional** nullspace, spanned by the vector taking value \(-t\) at each core vertex and \(1\) at every pendant vertex. Consequently the minimum Euclidean dimension realizing \(d(x,y)^{\alpha_{n,t}}\) as squared distances is \(N-2\), compared with \(N-1\) below the critical exponent.

The exponent \(\alpha_{n,t}\) decreases strictly as either integer parameter increases. With
\[
c=3\log 3-4\log 2>0,
\]
its distinct asymptotic regimes are
\[
\alpha_{n,t}=1+\frac{2}{t c(n-1)}+O_t(n^{-2})\quad(n\to\infty,\ t\text{ fixed})
\]
and
\[
\alpha_{n,t}=1+\frac{2}{t[(n-1)c+2\log2]}+O_n(t^{-2})
\quad(t\to\infty,\ n\text{ fixed}).
\]
For example, \(\alpha_{3,1}=1.709511291351\ldots\), whereas \(\alpha_{3,2}=1.380182355386\ldots\).

## Assumptions and scope
All graph edges have length one. Vertices are distinct, \(n\ge3\), \(t\ge1\), exponents are real and nonnegative, and the kernel scale \(\lambda\) ranges over every positive real. For \(p=0\), the diagonal convention is \(d(x,x)^0=0\) and every off-diagonal entry of the powered distance matrix is one. All spectral claims concern the real mean-zero space \(\{z:\sum_x z_x=0\}\) of dimension \(N-1\). The minimum Euclidean dimension refers to embeddings whose squared pairwise Euclidean distances equal the powered graph distances.

## Proof
**1. Symmetry decomposition.** Set \(a=2^p\), \(b=3^p\). Distances between distinct vertices are: core to core, one; core to its own leaf, one; core to another core's leaf, two; distinct leaves of the same core, two; and leaves of different cores, three.

The mean-zero coefficient space splits orthogonally into the following invariant quadratic-form sectors. Within each pendant cluster, the sum-zero subspace has dimension \(t-1\) and the powered-distance form acts as \(-a\) times the identity. These subspaces together have dimension \(n(t-1)\).

For a unit vector \(v\in\mathbb R^n\) orthogonal to the all-ones vector, put core weights \(u v_i\) and pendant weights \(w v_i/\sqrt t\) on each of the \(t\) leaves at core \(i\). Direct multiplication gives the standard-sector quadratic form
\[
\begin{pmatrix}u&w\end{pmatrix}
B_{n,t}(p)
\begin{pmatrix}u\\w\end{pmatrix},\qquad
B_{n,t}(p)=\begin{pmatrix}
-1&\sqrt t(1-a)\\
\sqrt t(1-a)&(t-1)a-tb
\end{pmatrix}.
\]
There are \(n-1\) copies. Finally, one mean-zero direction is constant on the cores and constant on all pendants, with respective coefficients \(-t\) and \(1\). On this vector the quadratic form is
\[
nt^2 H_{n,t}(p).
\]
The dimensions add to \(n(t-1)+2(n-1)+1=N-1\), so these sectors are exhaustive.

**2. The global root.** For \(0\le p\le1\), concavity of \(x\mapsto x^p\) gives \(F(p)\le0\), whence
\[
H_{n,t}(p)\le\left(1-\frac1t\right)2-2=-\frac2t<0.
\]
At \(p=1\), \(H_{n,t}(1)=-2/t\), while at \(p=2\), \(H_{n,t}(2)=2(n-1)+4(1-1/t)-2>0\). For \(p\ge1\),
\[
F'(p)=3^p\log3-2^{p+1}\log2>0,
\]
because it is positive at one and the ratio of the first exponential factor to the second increases with \(p\). Therefore \(H_{n,t}\) is strictly increasing for \(p\ge1\), has the asserted unique root in \((1,2)\), and is positive for all exponents above that root.

**3. The standard blocks do not obstruct the threshold.** The leading principal entry of \(B_{n,t}(p)\) is \(-1\), so the block is negative definite exactly when its determinant is positive. The determinant divided by \(t\) is
\[
\frac{\det B_{n,t}(p)}t
=b+a-a^2-1+\frac a t
=F(p)-(a-1)(a-2)+\frac a t.
\]
For \(0\le p\le1\), the concavity-majorization inequality \(3^p+2^p\ge4^p+1\) shows this is at least \(a/t>0\).

For \(1\le p\le\alpha_{n,t}\), the global inequality \(H_{n,t}(p)\le0\) implies
\[
\frac a t\ge (n-1)F(p)+a-2.
\]
Consequently
\[
\frac{\det B_{n,t}(p)}t\ge nF(p)-(a-2)^2.
\]
To bound the right side, write \(q=\log_2 3\), so \(3^p=a^q\). On \(2\le a\le4\), the function
\[
\phi(a)=a^q-\frac12a^2-1
\]
vanishes at both endpoints and is strictly concave, since \(1<q<8/5\) gives \(\phi''(a)=q(q-1)a^{q-2}-1<0\). Thus \(\phi(a)\ge0\), equivalently
\[
F(p)\ge\frac12(a-2)^2\qquad(1\le p\le2).
\]
For \(n\ge3\) and \(1<p<2\), the determinant lower bound is therefore strictly positive. At \(p=1\) the original determinant expression equals \(2/t>0\). All standard blocks remain negative definite through the critical root, and the internal leaf-cluster modes always have eigenvalue \(-a<0\).

**4. Gaussian equivalence and endpoint dimension.** The preceding decomposition proves that \([d(x,y)^p]\) is conditionally negative semidefinite precisely for \(p\le\alpha_{n,t}\), and strictly so below the root. At the root only the global sector vanishes; all other sectors remain strictly negative. The classical finite Schoenberg equivalence between conditionally negative distance powers and universal positive-definite exponential kernels proves the kernel statement. Strict positive definiteness at each positive scale follows from the strictly positive Gaussian radial-basis kernel on the distinct points of the corresponding finite Euclidean realization. If \(p>\alpha_{n,t}\), the global contrast gives a positive mean-zero powered-distance quadratic form, so its exponential kernel has a negative quadratic form for all sufficiently small positive \(\lambda\) by the first-order expansion \(e^{-\lambda x}=1-\lambda x+O(\lambda^2)\). Centered double-centering of the powered-distance matrix shows the minimum squared-Euclidean realization rank is the rank of minus its restriction to the mean-zero space, hence \(N-2\) at the root and \(N-1\) below it.

**5. Monotonicity and asymptotics.** For \(1<p<2\), \(F(p)>0\), so increasing \(n\) raises \(H_{n,t}(p)\); increasing \(t\) also raises it through \(1-1/t\). Its unique zero therefore decreases strictly in either parameter. Taylor expansion at \(p=1\) gives
\[
H_{n,t}(1+\delta)=-\frac2t+
\left[(n-1)c+2\left(1-\frac1t\right)\log2\right]\delta
+O\!\left((n+1)\delta^2\right).
\]
Because \(H_{n,t}\) has derivative at least \((n-1)c\) on \([1,2]\), the mean-value theorem gives the uniform estimate \(0<\alpha_{n,t}-1\le 2/[t(n-1)c]\). The displayed Taylor remainder is uniform for \(1\le p\le2\). Substituting the estimate into the expansion proves the two stated asymptotic formulas, including the displayed error orders.

## Verification
The standalone Python 3 script `corona_negative_type_checker.py` rebuilds the graph and its shortest-path distance matrix independently. It checks all entries, the complete mean-zero decomposition's quadratic forms, the root signs, standard-block determinants, strict monotonicity, and both large-parameter regimes. Run `python3 corona_negative_type_checker.py` from a directory containing this file. The observed replay reported `CHECKS_PASSED 26836`, covering 35 graph sizes with seven exponent evaluations each and 49 monotonicity parameter pairs. Those finite checks corroborate, but do not substitute for, the all-parameter proof above.

## Relationship to prior work
Sánchez's *On the supremal p-negative type of a finite metric space* (first public arXiv version dated 2011-08-02) gives a general finite-metric matrix criterion and the complete-bipartite sharp exponent. It does not state the corona classification above. Indulal and Stevanović's *The distance spectrum of corona and cluster of two graphs* (available online 2015-12-03) computes the ordinary distance-matrix spectrum of regular coronas. That calculation concerns the unpowered distance matrix, not the entire family of distance powers or universal Gaussian positivity. The present argument uses and extends the symmetry-block approach to prove a sharp all-exponent threshold, strict monotonicity, and the one-dimensional endpoint obstruction. The classical Schoenberg kernel equivalence is background and is not claimed as new.

## Limitations
The result covers complete-core graphs with the **same positive number** of attached independent leaves at every core vertex; unequal leaf counts, noncomplete cores, weighted distances, and graph powers are not treated. The numerical values are approximations to the uniquely defined roots. The originality comparison is bounded by accessible published sources and does not establish absolute historical novelty; in particular, an equivalent formulation could occur in less-indexed distance-kernel or graph-metric literature. Independent mathematical validation has not been conducted.

## References
1. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, 2011-08-02. https://arxiv.org/abs/1108.0451
2. G. Indulal and Dragan Stevanović, *The distance spectrum of corona and cluster of two graphs*, AKCE International Journal of Graphs and Combinatorics 12 (2015), 186–192; online availability dated 2015-12-03. https://draganstevanovic.wordpress.com/wp-content/uploads/2016/10/published-version.pdf
3. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536, https://doi.org/10.1090/S0002-9947-1938-1501980-0 (background theory).
