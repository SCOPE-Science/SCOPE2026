# Exact joint law of cyclic and terminal vertices in uniform random mappings

## Finding

Let \(F:[n]\to[n]\) be chosen uniformly from all \(n^n\) functions, with \(n\ge2\). Let \(C\) count vertices on directed cycles of the functional digraph and let \(Z\) count terminal vertices (vertices with indegree zero). For every \(1\le k<n\), put \(m=n-k\). Conditional on \(C=k\), the variable \(Z\) has the law of the number of specified \(m\) boxes not hit by \(m-1\) independent uniform draws from \([n]\). Thus, for each \(0\le r\le m\),

\[
\mathbb E[(Z)_{\underline r}\mid C=k]
=(m)_{\underline r}\left(1-\frac r n\right)^{m-1},
\]

where falling factorials have value one at order zero. Equivalently, for \(0\le z\le m\),

\[
\mathbb P(Z=z\mid C=k)
=\frac{\binom mz}{n^{m-1}}
\sum_{j=0}^{m-z}(-1)^j\binom{m-z}{j}(n-z-j)^{m-1}.
\]

At \(C=n\), \(Z=0\) almost surely. Together with the classical cyclic-point distribution
\[
\mathbb P(C=k)=\frac{k(n)_{\underline k}}{n^{k+1}}
\qquad (1\le k\le n),
\]
this is an exact bivariate finite-sample law, including all boundary cases.

In particular, with \(q_n=1-1/n\), the conditional mean is
\[
\mathbb E[Z\mid C=k]=(n-k)q_n^{n-k-1}
\quad(1\le k<n),\qquad
\mathbb E[Z\mid C=n]=0.
\]
It decreases **strictly** with \(k\), so for every strictly increasing real function \(h\) on \(\{1,\ldots,n\}\),
\[
\operatorname{Cov}(h(C),Z)<0.
\]

Writing \(c_n=\sum_{j=1}^n(n)_{\underline j}/n^j\), with \(c_1=1\), the exact covariance and its first-order asymptotics are
\[
\operatorname{Cov}(C,Z)=nq_n^n(c_{n-1}-c_n)<0,
\qquad
\operatorname{Cov}(C,Z)\sim-\frac1e\sqrt{\frac{\pi n}{8}}.
\]
Moreover, the correlation has the asymptotics
\[
\operatorname{Corr}(C,Z)
\sim-\sqrt{\frac{\pi}{8(2-\pi/2)(e-2)}}\,n^{-1/2}.
\]

## Assumptions and scope

A functional digraph has the directed edge \(v\to F(v)\) for every \(v\in[n]\); loops count as directed cycles. The indegree of \(v\) is \(|F^{-1}(v)|\). A terminal vertex has indegree zero, not outdegree zero. No acyclicity or connectedness conditioning is imposed. All statements apply to each integer \(n\ge2\), including \(k=1\), \(k=n-1\), and \(k=n\). The zero-order falling factorial and the empty-draw occupancy experiment take their standard values.

## Proof

**1. Conditional rooted-forest law.** Fix a set \(S\) of \(k\) cyclic vertices. Every mapping whose cyclic set is exactly \(S\) is uniquely a permutation of \(S\) together with a directed forest on \([n]\) whose roots are \(S\), all other edges pointing toward roots. The number of these forests is \(k n^{m-1}\) when \(m=n-k\ge1\). Indeed, the directed matrix-tree theorem gives the relevant principal Laplacian determinant
\[
\det(nI_m-J_m)=k n^{m-1},
\]
with eigenvalues \(n\) of multiplicity \(m-1\) and \(k=n-m\) of multiplicity one. Conditional on \(C=k\) and \(S\), the rooted forest is uniform; cyclic vertices cannot be terminal.

**2. Terminal-vertex factorial moments.** Mark any \(r\) distinct nonroots, with \(0\le r\le m\), and require that they have indegree zero. Removing them leaves a forest on \(n-r\) vertices rooted at the same \(k\) roots. Conversely, reattach each removed vertex by one edge to any of the \(n-r\) remaining vertices; these are all and only the allowed forests. The resulting count is \(k(n-r)^{m-1}\) (also when no nonroots remain, by direct attachment counting). Dividing by \(k n^{m-1}\) yields
\[
\mathbb P(\text{the prescribed }r\text{ nonroots are terminal}\mid C=k,S)
=\left(1-\frac r n\right)^{m-1}.
\]
Summing over ordered \(r\)-tuples gives the displayed falling-factorial moments. Independent occupancy of \(m-1\) draws in \(n\) boxes has exactly these avoidance probabilities for any \(r\) specified target boxes; because the random variable is supported on \(\{0,\ldots,m\}\), its factorial moments determine its law. Binomial inversion then gives the displayed probability mass function. The expression is independent of the chosen root set.

**3. Strict negative regression.** For \(1\le m\le n-1\), define \(g_m=mq_n^{m-1}\), and \(g_0=0\). The ratio
\[
\frac{g_m}{g_{m-1}}=\frac{m(n-1)}{n(m-1)}>1
\quad (2\le m\le n-1)
\]
shows that \(\mathbb E[Z\mid C=k]=g_{n-k}\) strictly decreases through all \(k=1,\ldots,n\), including the last step to zero. Let \(C'\) be an independent copy of \(C\). For increasing \(h\), twice the covariance of \(h(C)\) with \(g_{n-C}\) is
\[
\mathbb E[(h(C)-h(C'))(g_{n-C}-g_{n-C'})]<0,
\]
because every \(k\in\{1,\ldots,n\}\) has positive probability and both functions are strictly oppositely ordered. Conditioning on \(C\) gives the claimed covariance inequality.

**4. Covariance formula.** For a specified vertex \(v\), the probability it is not in the image of \(F\) is \(q_n^n\). Under that event, the restriction of \(F\) to the other \(n-1\) vertices is itself a uniform random mapping of size \(n-1\), while \(v\) cannot lie on a cycle. Consequently the conditional cyclic count has distribution \(C_{n-1}\). Summing the terminal indicators gives
\[
\mathbb E[CZ]=nq_n^n c_{n-1},\qquad
\mathbb E[Z]=nq_n^n,\qquad \mathbb E[C]=c_n.
\]
For completeness, counting the \(k\) cyclic points (or the birthday-collision exploration) gives
\(\mathbb P(C=k)=k(n)_{\underline k}/n^{k+1}\) and \(c_n=\sum_{j=1}^{n}(n)_{\underline j}/n^j\). For every fixed \(j\ge2\), the product \(\prod_{\ell=0}^{j-1}(1-\ell/n)\) strictly increases with \(n\), and hence \(c_n>c_{n-1}\). This proves the exact strictly negative covariance.

**5. Asymptotics.** Put \(a_{n,j}=(n)_{\underline j}/n^j\) for \(j\le n\), and zero otherwise. For \(j\) proportional to \(\sqrt n\),
\[
 a_{n,j}=\exp(-j(j-1)/(2n)+O(j^3/n^2)),
\qquad n\left(1-\frac{a_{n-1,j}}{a_{n,j}}\right)\longrightarrow \frac{x^2}{2}
 \quad \text{when }j/\sqrt n\to x.
\]
For \(j\le n/2\), the difference is dominated after scaling by a constant multiple of \((j^2/n^2)\exp(-j(j-1)/(2n))\); the remaining tail is exponentially small. Thus Riemann-sum dominated convergence gives
\[
\sqrt n(c_n-c_{n-1})\longrightarrow
\int_0^\infty \frac{x^2}{2}e^{-x^2/2}\,dx
=\sqrt{\frac\pi8}.
\]
The cyclic-point probability mass function converges after \(\sqrt n\)-scaling to the Rayleigh density \(xe^{-x^2/2}\), with Gaussian tails ensuring convergence of second moments; consequently \(\operatorname{Var}(C)/n\to2-\pi/2\). With \(p_n=q_n^n\), direct occupancy gives
\[
\operatorname{Var}(Z)=np_n(1-p_n)
+n(n-1)((1-2/n)^n-p_n^2),
\qquad \operatorname{Var}(Z)/n\to e^{-1}-2e^{-2}.
\]
Combining these limits with the covariance identity proves the asserted correlation coefficient. The constant in this limit is strictly positive because \(e>2\) and \(\pi<4\).

## Verification

The standalone `verify.py` enumerates all \(873{,}611\) mappings of sizes \(2\) through \(7\), recomputes cyclic and terminal counts directly from the functions, and makes \(333\) independent exact-rational assertions. Checks include every attainable joint probability, conditional factorial moments, marginals, strict covariance, and normalization. It uses only the Python standard library. Additional numerical large-size comparisons were performed against the asymptotic constant. Finite checks are corroboration, not a substitute for the all-size proof.

## Relationship to prior work

Classical random-mapping analysis determines the marginal cyclic-point and terminal-point distributions and supplies rooted-forest decompositions. Flajolet and Odlyzko (1990) analyze these marginal statistics; Soria (1996) analyzes leaf markings in functional graphs; Hansen and Jaworski (2006, 2010) treat cyclic points, exchangeable indegrees, and conditional component sizes. The present statement concerns a different joint pair: the **complete conditional terminal-count law given cyclic count**, its explicit occupancy representation, and strict negative regression for every increasing transform of the cyclic count. The cited inspected portions do not state this combined identity. Broad generating-function formalisms can support further coefficient extraction; the historical priority of an equivalent specialization is not proven.

## Limitations

Historical coverage is not certified exhaustive. In particular, older literature on terminal points and cyclic components and the uninspected portions of the 2010 paper could contain an equivalent formulation. The work does not establish stochastic dominance of the full conditional terminal-count distributions in the cyclic count; it establishes strict monotonicity of conditional means and therefore covariance inequalities. The correlation asymptotic is specific to uniform mappings and does not automatically extend to nonuniform independent-choice or constrained-indegree models. Independent validation has not been carried out.

## References

- P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, EUROCRYPT 1989 proceedings, LNCS 434, 1990, pp. 329–354. Accessible copy: https://www-users.cse.umn.edu/~odlyzko/doc/arch/random.mappings.pdf .
- M. Soria, *Distribution of Image Points in Random Mappings*, seminar of November 10, 1996, https://algo.inria.fr/seminars/sem96-97/soria.html .
- J. C. Hansen and J. Jaworski, *A new random mapping model*, first public preprint March 22, 2006, arXiv:math/0603529, https://arxiv.org/abs/math/0603529 .
- J. C. Hansen and J. Jaworski, *Random Mappings with a Given Number of Cyclical Points*, Ars Combinatoria 94 (2010), 341–359, https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/ .
- M. Drmota and M. Soria, *Images and Preimages in Random Mappings*, SIAM J. Discrete Math. 10 (1997), 246–269, DOI:10.1137/S0895480194268421 (general limit-distribution framework; abstract and related seminar exposition inspected).
