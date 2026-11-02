# Exact heat-kernel transport on complete multipartite graphs

## Finding

Let \(r\geq3\), let \(n_1,\ldots,n_r\) be positive integers, and set \(N=\sum_{i=1}^r n_i\). On the unit-edge complete multipartite graph \(G=K_{n_1,\ldots,n_r}\), let \(L=D-A\) be the combinatorial graph Laplacian and \(H_t=e^{-tL}\) for \(t\geq0\). Write
\[
b=e^{-Nt},\qquad a_i=e^{-(N-n_i)t},\qquad U_i=\left(1-\frac1{n_i}\right)a_i+\frac{b}{n_i}.
\]
For any distinct vertices \(x,y\), the exact graph-metric Wasserstein-\(1\) distance between heat-kernel rows is
\[
W_1\bigl(H_t(x,\cdot),H_t(y,\cdot)\bigr)=
\begin{cases}
2a_i,&x,y\text{ belong to the same part }i,\\
2\max\{U_i,U_j\}-b,&x\text{ lies in part }i\text{ and }y\text{ in part }j\ne i.
\end{cases}
\]
In particular, with \(s=\max_i n_i\) and the graph-Lipschitz seminorm \(\operatorname{Lip}(f)=\max_{xy\in E(G)}|f(x)-f(y)|\), the exact attained operator norm is
\[
\boxed{\|H_t\|_{\operatorname{Lip}\to\operatorname{Lip}}
=b+2\left(1-\frac1s\right)\left(e^{-(N-s)t}-b\right).}
\]
Thus the entire sharp norm profile depends on the part sizes *only* through \(N\) and the largest part size \(s\); different complete multipartite graphs with the same two parameters have identical profiles. For example, \(K_{3,3,2}\) and \(K_{3,2,2,1}\) have identical sharp Lipschitz norm curves, although their heat matrices and edge sets differ. This does **not** assert equality of their full pairwise distance tables.

For \(m=N-s\), the norm is strictly below \(1\) for every \(t>0\) exactly when \(s-m\leq2\). If \(s-m\geq3\), it initially exceeds \(1\) and has the unique peak
\[
t_* =\frac1s\log\!\left(\frac{(s-2)(m+s)}{2m(s-1)}\right),
\qquad
\|H_{t_*}\|_{\operatorname{Lip}\to\operatorname{Lip}}
=\frac{2(s-1)}{m+s}\left(\frac{2m(s-1)}{(s-2)(m+s)}\right)^{m/s}.
\]
The supremum of these norms over all complete multipartite graphs with at least three parts and all \(t\geq0\) is \(2\), which no finite graph attains.

## Assumptions and scope

The graph is simple, finite, connected, complete multipartite, unweighted, and carries its shortest-path metric. Heat flow uses the **combinatorial**, not degree-normalized, Laplacian, and the vertices have counting measure. Functions are real-valued. The Wasserstein distance is the ordinary shortest-path cost \(W_1\) on probability measures. The operator norm acts on real functions modulo constants with the graph-Lipschitz seminorm. All statements quantify over every positive integer part profile with \(r\geq3\) and every real \(t\geq0\); no regularity or ordering of part sizes is assumed.

## Proof

**1. Spectral decomposition.** Let \(\bar f=N^{-1}\sum_{v\in V}f(v)\) and \(\bar f_i=n_i^{-1}\sum_{v\in V_i}f(v)\). Constant functions form the zero eigenspace of \(L\). Vectors constant on each part and of total sum zero form an eigenspace with eigenvalue \(N\). On each part \(i\), vectors supported there and summing to zero form an eigenspace with eigenvalue \(N-n_i\). These mutually orthogonal subspaces exhaust the vertex-function space. Consequently, for \(x\in V_i\),
\[
(H_t f)(x)=\bar f+b(\bar f_i-\bar f)+a_i(f(x)-\bar f_i).
\]
This identity also holds for singleton parts, whose within-part zero-sum subspace is trivial.

**2. The two heat rows on different parts.** Fix \(x\in V_i\) and \(y\in V_j\), \(i\ne j\), and put \(\sigma=H_t(x,\cdot)-H_t(y,\cdot)\). The only nonzero entries of \(\sigma\) are
\[
\sigma(x)=U_i,\quad
\sigma(z)=-\frac{a_i-b}{n_i}\quad(z\in V_i\setminus\{x\}),\quad
\sigma(y)=-U_j,\quad
\sigma(z)=\frac{a_j-b}{n_j}\quad(z\in V_j\setminus\{y\}).
\]
Here \(a_i,a_j\geq b\), \(U_i,U_j\geq b\). The negative mass on \(V_i\setminus\{x\}\) totals \(U_i-b\), while the positive mass on \(V_j\setminus\{y\}\) totals \(U_j-b\).

Suppose \(U_i\geq U_j\). Transport \(U_j\) units from \(x\) to \(y\) at cost \(1\), transport the remaining \(U_i-U_j\) units from \(x\) to the other vertices of \(V_i\) at cost \(2\), and transport the \(U_j-b\) units on \(V_j\setminus\{y\}\) to the remaining negative mass on \(V_i\setminus\{x\}\) at cost \(1\). The respective totals match, and this constructs a coupling of cost \(2U_i-b\). For a lower bound, use the graph-\(1\)-Lipschitz potential taking value \(1\) at \(x\), \(-1\) on \(V_i\setminus\{x\}\), and \(0\) outside \(V_i\). Its integral against \(\sigma\) equals \(2U_i-b\). Kantorovich duality proves equality. Interchanging the parts treats \(U_j\geq U_i\), including equality. Empty sets when a part is a singleton cause no problem because their prescribed masses vanish.

**3. Two vertices in one part.** For distinct \(x,y\in V_i\), the spectral formula gives \(H_t(x,\cdot)-H_t(y,\cdot)=a_i(\delta_x-\delta_y)\). Since \(d(x,y)=2\), its \(W_1\) cost is \(2a_i\). This completes the all-pairs transport formula.

**4. The sharp Lipschitz norm.** The graph distance is the path metric, so a function's Lipschitz seminorm equals its largest edge difference. Kantorovich duality on each edge makes the operator norm the largest edge-row \(W_1\) distance. Write
\[
F(n)=b+2\left(1-\frac1n\right)\left(e^{-(N-n)t}-b\right),\qquad 1\leq n<N.
\]
For any edge joining parts \(i,j\), the exact row distance is \(\max\{F(n_i),F(n_j)\}\). At fixed \(N,t\geq0\), both factors \(1-1/n\) and \(e^{-(N-n)t}-b\) are nonnegative and nondecreasing in \(n\), so \(F(n)\) is nondecreasing. Every part meets some other part, so the sharp global norm is \(F(s)\). It is attained by the potential above centered at any vertex in a largest part (or by its negative), hence the equality is an operator-norm identity rather than merely an upper bound.

**5. Time behavior and sharp family limit.** Set \(m=N-s\geq1\). The norm is
\[
F(s)=\frac{2(s-1)}s e^{-mt}-\frac{s-2}s e^{-(m+s)t}.
\]
For \(s\geq2\), differentiation yields
\[
F'(s)=\frac{e^{-mt}}s\left(-2m(s-1)+(s-2)(m+s)e^{-st}\right).
\]
The bracket is strictly decreasing for \(s>2\). Its value at \(t=0\) equals \(s(s-m-2)\), which gives the strict contraction/temporary amplification dichotomy and, by setting it to zero, the displayed unique peak time and value. When \(s=1\), the norm is \(e^{-Nt}\); when \(s=2\), it is \(e^{-(N-2)t}\), so both contract strictly for \(t>0\). At the boundary \(s-m=2\), the initial derivative vanishes but is negative thereafter.

For every finite profile with \(s\geq2\), the form \(F(s)=b+2(1-1/s)(a_s-b)\) is strictly less than \(2\); if \(s=1\), it is at most \(1\). Conversely, on \(K_{s,1,1}\) with \(t=s^{-1/2}\), as \(s\to\infty\), one has \(a_s=e^{-2/\sqrt s}\to1\), \(b=e^{-(s+2)/\sqrt s}\to0\), and \(F(s)\to2\). Thus \(2\) is the unattained sharp universal supremum.

## Verification

The standalone `verify.py` constructs the heat matrix independently from the spectral blocks using exact rational parameters \(q=e^{-t}\in\{1,\tfrac12,\tfrac23\}\). For every integer partition of orders \(2\) through \(7\) with at least two parts, it enumerates all integer-valued graph-\(1\)-Lipschitz functions anchored at a vertex, verifies their admissibility, and maximizes the heat-row difference for every unordered vertex pair. Integer optimization is exhaustive because the graph-incidence inequalities form a totally unimodular system and the graph diameter is at most \(2\). In total, \(111\) exact-rational profile/time instances and \(1605\) vertex-pair checks agree with the displayed transport formulas. The analytic argument, not finite enumeration, proves the result for all orders and all real times.

Run `python verify.py` with Python 3. No third-party packages are required.

## Relationship to prior work

Ollivier's 2007 framework establishes graph-metric \(W_1\) contraction and curvature as mathematical objects, including a continuous-time formulation; Jost and Liu study neighbor-measure transport and local clustering, while Bauer and collaborators derive Li–Yau-type heat-gradient estimates on graphs. These sources do not provide the present all-time, pairwise exact transport table for combinatorial heat flow on arbitrary complete multipartite graphs. An earlier sharp formula for **bipartite** heat-flow Lipschitz norms is consistent with the two-part restriction, but does not by itself imply invariance under more general multipartite decompositions. An earlier **total-variation** contraction threshold for the complete multipartite family agrees with the threshold here, but is a statement in a different seminorm and does not determine the exact row-transport profiles. The contraction threshold and two-part special case are not asserted as separately new.

## Limitations

Only unweighted complete multipartite graphs, combinatorial heat generators, the original shortest-path metric, real Lipschitz seminorms and \(W_1\) are covered. The theorem says nothing about degree-normalized heat kernels, weighted edges, arbitrary graphs, higher Wasserstein exponents, or other function-space norms. For a fixed total order, the invariant \(s\) need not be at least half of \(N\); replacing all smaller parts by a single part may alter \(s\) and therefore alter the sharp curve. The claim makes no blanket assertion that every multipartite refinement leaves the norm invariant.

## References

1. Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, public arXiv preprint `math/0701886` (first submitted 2007-01-30), especially Definitions 2–3 and the continuous-time formulation.
2. Jürgen Jost and Shiping Liu, *Ollivier's Ricci curvature, local clustering and curvature dimension inequalities on graphs*, arXiv `1103.4037` (first submitted 2011-03-21), especially its neighbor-measure \(W_1\) formulation.
3. Frank Bauer, Paul Horn, Yong Lin, Gabor Lippner, Dan Mangoubi and Shing-Tung Yau, *Li-Yau inequality on graphs*, arXiv `1306.2561` (first submitted 2013-06-11), especially its heat-gradient framework and curvature-dimension definitions.
