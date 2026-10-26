# Root–leaf covariance in degree-proportional attachment trees

## Finding

Start with the single edge on vertices \(1,2\). For each \(n\ge2\), construct the \((n+1)\)-vertex tree by attaching vertex \(n+1\) to an old vertex, choosing old vertex \(v\) with probability \(\deg(v)/(2(n-1))\). Let \(D_n\) be the degree of vertex \(1\), and let \(L_n\) be the total number of degree-one vertices (leaves). Put
\[
p_n=\frac{1}{4^{n-2}}\binom{2n-4}{n-2}.
\]
Then for **every integer \(n\ge2\)**,
\[
\boxed{\operatorname{Cov}(D_n,L_n)
 =\frac{2p_n}{3}\bigl[n-2(2n-3)p_n\bigr].}
\]
The covariance vanishes for \(n=2,3\), is strictly positive for every \(n\ge4\), and satisfies
\[
\operatorname{Cov}(D_n,L_n)
=\frac{2}{3\sqrt\pi}\sqrt n-\frac{8}{3\pi}+O(n^{-1/2}).
\]
For the nondegenerate correlations (\(n\ge4\)),
\[
\boxed{\sqrt n\,\operatorname{Corr}(D_n,L_n)
 \longrightarrow\sqrt{\frac{2}{\pi-2}}.}
\]
In particular the covariance grows like \(\sqrt n\), but the correlation decays like \(n^{-1/2}\).

## Assumptions and scope

The graph is a labeled **tree**, with exactly one new edge per arrival and **attachment probability proportional to the current undirected degree**, with no self-loops. Both initial vertices have degree one. The vertex whose degree is counted is one particular **initial vertex**; the leaf count includes **all** vertices, including the root when its degree remains one. These conventions matter: the uniform recursive-tree model and the plane-oriented recursive-tree model use different attachment weights.

The asymptotic constant concerns the limit \(n\to\infty\) of this exact process, not a continuum or mean-field approximation. At \(n=2,3\), \(L_n\) is deterministic, so correlation is undefined although covariance is zero.

## Proof

**1. Initial-vertex survival and means.** The event \(\{D_n=1\}\) occurs precisely when vertex \(1\) has never been chosen as an attachment endpoint after the initial edge. On this event its selection probability at tree size \(j\) is \(1/(2(j-1))\). Thus, with the empty product equal to one,
\[
\mathbb P(D_n=1)
=\prod_{j=2}^{n-1}\frac{2j-3}{2j-2}
=\frac{1}{4^{n-2}}\binom{2n-4}{n-2}=p_n,
\qquad
\frac{p_{n+1}}{p_n}=\frac{2n-3}{2n-2}.
\]
Write \(d_n=\mathbb ED_n\) and \(\ell_n=\mathbb EL_n\). An arriving vertex increases the root degree with conditional probability \(D_n/(2(n-1))\), and increases the leaf count by one unless it attaches to an old leaf, which occurs conditionally with probability \(L_n/(2(n-1))\). Consequently
\[
d_{n+1}=\left(1+\frac1{2(n-1)}\right)d_n,
\qquad
\ell_{n+1}=\left(1-\frac1{2(n-1)}\right)\ell_n+1.
\]
With \(d_2=1\) and \(\ell_2=2\), direct substitution using the recurrence for \(p_n\) gives
\[
\boxed{d_n=(2n-3)p_n,\qquad
\ell_n=\frac{2(n-1)+4p_n}{3}.}
\]

**2. The exact mixed moment.** Let \(I_n\) indicate an attachment to vertex \(1\) at step \(n+1\), and let \(J_n\) indicate an attachment to any old leaf. We have \(D_{n+1}=D_n+I_n\) and \(L_{n+1}=L_n+1-J_n\). Conditional on the current tree \(T_n\),
\[
\mathbb E(I_n\mid T_n)=\frac{D_n}{2(n-1)},\quad
\mathbb E(J_n\mid T_n)=\frac{L_n}{2(n-1)},\quad
\mathbb E(I_nJ_n\mid T_n)=\frac{\mathbf1_{\{D_n=1\}}}{2(n-1)}.
\]
The two terms involving \(D_nL_n/[2(n-1)]\) cancel when expanding \((D_n+I_n)(L_n+1-J_n)\). Hence, writing \(c_n=\mathbb E[D_nL_n]\),
\[
c_{n+1}=c_n+d_n+\frac{d_n-p_n}{2(n-1)}
=c_n+d_{n+1}-\frac{p_n}{2(n-1)}.
\]
As \(c_2=2\), the candidate
\[
\boxed{c_n=\frac{2n-1}{3}d_n+p_n}
\]
satisfies the recurrence exactly: its successive difference is \(d_{n+1}+p_{n+1}-p_n\). Subtracting \(d_n\ell_n\) yields the stated covariance.

**3. Sign of the covariance.** Define \(q_n=2(2n-3)p_n/n\). One has \(q_3=1\) and, for each integer \(n\ge3\),
\[
\frac{q_{n+1}}{q_n}
=\frac{n(2n-1)}{(n+1)(2n-2)}<1,
\]
since the denominator minus numerator equals \(n-2>0\). Thus \(q_n<1\) for \(n\ge4\), proving strict positivity. Substitution gives the zero values at \(n=2,3\).

**4. Variance normalization and sharp asymptotics.** The same one-step Bernoulli computations, with initial values at \(n=2\), give
\[
\operatorname{Var}(D_n)=2(n-1)-d_n-d_n^2,
\qquad
\operatorname{Var}(L_n)=\frac{n-1+4p_n-16p_n^2}{9}.
\]
For completeness, the first identity follows from
\(\mathbb E[D_{n+1}^2]=(1+1/(n-1))\mathbb E[D_n^2]+d_n/(2(n-1))\),
while the second follows from
\[
\operatorname{Var}(L_{n+1})
=\left(1-\frac1{n-1}\right)\operatorname{Var}(L_n)
+\frac{\ell_n}{2(n-1)}-\frac{\ell_n^2}{4(n-1)^2}.
\]
The displayed solutions satisfy these recurrences and their initial conditions.
Stirling's formula for the central binomial coefficient gives \(p_n=1/\sqrt{\pi n}+O(n^{-3/2})\). It follows that
\[
\operatorname{Var}(D_n)=(2-4/\pi)n+O(\sqrt n),\qquad
\operatorname{Var}(L_n)=n/9+O(1).
\]
Substitution into the exact covariance and variance identities yields both displayed limits, including the constant \(\sqrt{2/(\pi-2)}\). No infinite assertion relies on numerical enumeration.

## Verification

A standalone Python 3 program, `verify.py`, enumerates the **complete degree-vector distribution** at every size from \(n=2\) through \(n=10\), using exact rational transition probabilities. Across these sizes it sums 6,917 states and checks the root mean, leaf mean, mixed moment, both variances, covariance, and strict sign. An independent exact-rational recurrence comparison checks 2,993 identities across \(n=2,\ldots,500\). Three large-size numerical tests check asymptotic convergence; those tests are illustrative, not infinite certificates. Run `python3 verify.py` without third-party dependencies.

## Relationship to prior work

Brightwell and Łuczak (2010, arXiv:1012.5550) study the degree profile and high-degree concentration for the **same degree-proportional attachment tree**. Their degree-count results do not state the mixed covariance between one aged initial vertex and the total leaf count. Peköz, Röllin, and Ross (2014, arXiv:1402.4686) establish joint laws of a fixed set of early-vertex degrees; that finite-dimensional statement does not include the growing global sum of leaf indicators. Hartle and Krapivsky (2026, arXiv:2602.01021) analyze leafdegree distributions and covariances of **global degree-count categories**, not the tagged initial vertex and the global leaf count.

Mahmoud, Smythe, and Szymański (1993, doi:10.1002/rsa.3240040204) study a related **plane-oriented recursive tree**, whose attachment rule weights each vertex by one plus its outdegree. That model differs from the present undirected-degree weighting, notably at the initial vertex. A previously recorded exact root-degree/leaf-count covariance for **uniform** random recursive trees likewise concerns attachment uniformly over existing vertices, rather than proportionally to degree. Neither model's identity implies the present formula by a parameter substitution.

## Limitations

The result gives exact second-order dependence and its sign, not the joint distribution of \((D_n,L_n)\), independence, or a stochastic ordering. Unindexed historical literature could contain an equivalent identity; inspection of the closest known published results does not establish historical priority. Independent mathematical audit has not been performed.

## References

1. G. Brightwell and M. J. Łuczak, *Vertices of high degree in the preferential attachment tree*, arXiv:1012.5550 (first submitted 2010-12-26).
2. E. Peköz, A. Röllin, and N. Ross, *Joint degree distributions of preferential attachment random graphs*, arXiv:1402.4686 (first submitted 2014).
3. H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021 (2026).
4. H. Mahmoud, R. T. Smythe, and J. Szymański, *On the Structure of Random Plane-Oriented Recursive Trees and Their Branches*, *Random Structures & Algorithms* 4 (1993), 151–176, doi:10.1002/rsa.3240040204.
