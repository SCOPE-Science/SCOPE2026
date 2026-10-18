# Degree normalization reverses sharp heat-gradient ordering on complete bipartite graphs

## Finding
Fix an integer \(n\ge4\). For a split \(a+b=n\) into positive integers, let \(G_{a,b}=K_{a,b}\) be the unweighted complete bipartite graph. For \(0\le\theta\le1\) define the continuous-time Markov generator
\[
 (Q_{a,b,\theta}f)(u)=d(u)^{-\theta}\sum_{v\sim u}(f(v)-f(u)),
 \qquad H_{a,b,\theta}(t)=\exp(tQ_{a,b,\theta}).
\]
Write \(\operatorname{Lip}_G(g)=\max_{u\sim v}|g(u)-g(v)|\) and define the sharp endpoint gradient coefficient
\[
 C_{a,b}^{(\theta)}(t)=\sup_{\|f\|_{\infty}\le1}\operatorname{Lip}_G(H_{a,b,\theta}(t)f),\qquad t>0.
\]
Put \(\alpha=b^{1-\theta}\), \(\beta=a^{1-\theta}\). Then for every \(a,b\ge1\), \(0\le\theta\le1\), and \(t>0\),
\[
 \boxed{C_{a,b}^{(\theta)}(t)=2\left[\left(1-\frac1a\right)e^{-\alpha t}+\left(1-\frac1b\right)e^{-\beta t}+\left(\frac1a+\frac1b-1\right)e^{-(\alpha+\beta)t}\right].} \tag{1}
\]
The supremum is attained by a real-valued input taking only the values \(+1\) and \(-1\).

At fixed \(n\) and for every \(t>0\), these sharp coefficients obey **opposite strict partition orders** at the two canonical normalizations. If \(1\le a<c\le\lfloor n/2\rfloor\), with \(b=n-a\) and \(d=n-c\), then
\[
 \boxed{C_{a,b}^{(0)}(t)>C_{c,d}^{(0)}(t),\qquad
 C_{a,b}^{(1)}(t)<C_{c,d}^{(1)}(t).} \tag{2}
\]
Thus the star is the unique worst member at each time for the unnormalized Laplacian, and the unique best member for the degree-normalized generator; the most balanced split gives the respective opposite extreme. These strict comparisons also hold after taking the time-weighted supremum \(\sup_{t>0}\sqrt t\,C_{a,b}^{(\theta)}(t)\) at \(\theta=0,1\).

For every intermediate \(0<\theta<1\), the two types of ordering necessarily **cross in time** for every strict pair of splits: for all sufficiently small positive \(t\),
\[
 C_{a,b}^{(\theta)}(t)<C_{c,d}^{(\theta)}(t),
\]
whereas for all sufficiently large \(t\),
\[
 C_{a,b}^{(\theta)}(t)>C_{c,d}^{(\theta)}(t). \tag{3}
\]
In particular at least one positive crossing time exists. No uniqueness of the crossing over the entire positive time axis is asserted.

There is also an explicit boundary layer near unnormalized diffusion. For each fixed strict pair of splits there is, for all sufficiently small \(\theta>0\), a locally unique positive crossing time emerging from zero, and it satisfies
\[
 \boxed{t_{a,c}(\theta)=\theta\frac{\log(cd/(ab))}{cd-ab}+O_{n,a,c}(\theta^2),\qquad\theta\downarrow0.} \tag{4}
\]
Here \(cd-ab>0\). Local uniqueness means uniqueness among crossing times in a sufficiently small fixed neighborhood of \(t=0\), not global uniqueness.

## Assumptions and scope
The vertex set is partitioned into groups \(A,B\) of cardinalities \(a,b\); every cross-part edge has unit weight, and there are no same-part edges. Vertex functions may be real- or complex-valued and have the unweighted coordinate supremum norm. The Lipschitz seminorm uses unit graph-edge lengths. The parameter \(\theta=0\) is the combinatorial continuous-time generator \(-L\), whereas \(\theta=1\) is the unit-exit-rate continuous-time random walk generator \(-D^{-1}L\). No stationary-measure weighting is imposed on the input supremum norm. Comparison assertions require the same total vertex count \(n\) and a strict inequality of the smaller part sizes; balanced cases are included.

## Proof
**1. Exact two-rate heat-row difference.** A particle at an \(A\)-vertex jumps at total rate \(\alpha\) to a uniformly selected vertex of \(B\), and a particle at a \(B\)-vertex jumps at total rate \(\beta\) to a uniformly selected vertex of \(A\). Fix adjacent \(u\in A\) and \(v\in B\). Let \(x=e^{-\alpha t}\), \(y=e^{-\beta t}\), and \(z=e^{-(\alpha+\beta)t}=xy\). The aggregated two-state chain has eigenvalues \(0\) and \(-\alpha-\beta\); the within-\(A\) and within-\(B\) fluctuations have eigenvalues \(-\alpha\) and \(-\beta\), respectively. Consequently, subtracting the heat kernel row started at \(v\) from the row started at \(u\) gives, for every column \(j\),
\[
 H(t)_{uj}-H(t)_{vj}=
 \begin{cases}
  x\,\mathbf1_{\{j=u\}}+(z-x)/a,&j\in A,\\
  -y\,\mathbf1_{\{j=v\}}+(y-z)/b,&j\in B.
 \end{cases} \tag{5}
\]
This formula can alternatively be checked directly by differentiating it using the generator and matching the initial row difference.

Since \(0<z<x,y\), the single coefficient at \(u\) is strictly positive, the other \(A\)-coefficients are negative, the coefficient at \(v\) is strictly negative, and the other \(B\)-coefficients are positive. Statements about an empty collection are vacuous when a part has size one. The difference of two stochastic rows sums to zero, so its \(\ell^1\)-norm is twice its total positive mass:
\[
 \sum_j|H(t)_{uj}-H(t)_{vj}|
 =2\left[x-\frac{x-z}{a}+\frac{b-1}{b}(y-z)\right],
\]
which expands to (1). For any finite signed row \(r\), \(\sup_{\|f\|_\infty\le1}|\sum_jr_j f(j)|=\sum_j|r_j|\), attained by the signs of \(r_j\). Every edge is carried to every other edge by a graph automorphism. Thus this row norm equals the sharp \(\ell^\infty\)-to-edge-Lipschitz coefficient and the stated \(\pm1\) input attains it.

**2. Unnormalized strict ordering.** At \(\theta=0\), \(\alpha=b\), \(\beta=a\). Rearranging (1) and using \(n=a+b\) gives
\[
 \frac12e^{nt}C_{a,b}^{(0)}(t)=1+\psi_t(a)+\psi_t(b),\qquad
 \psi_t(s)=(s-1)\int_0^t e^{sr}\,dr. \tag{6}
\]
For every real \(s\ge1\) and \(t>0\),
\[
 \psi_t''(s)=\int_0^t e^{sr}\bigl(2r+(s-1)r^2\bigr)\,dr>0. \tag{7}
\]
For fixed sum \(n\), strict convexity makes \(\psi_t(a)+\psi_t(n-a)\) strictly decreasing as \(a\) increases through \([1,n/2]\). This proves the first inequality in (2), including its equality cases.

**3. Degree-normalized strict reverse ordering.** At \(\theta=1\), \(\alpha=\beta=1\). With \(\sigma=1/a+1/b\), (1) becomes
\[
 \frac12C_{a,b}^{(1)}(t)=(2-\sigma)e^{-t}+(\sigma-1)e^{-2t}. \tag{8}
\]
For fixed \(n\), \(\sigma\) is strictly decreasing for \(1\le a\le n/2\) under strict changes of the smaller integer part. The right side of (8) is strictly decreasing in \(\sigma\), since \(e^{-2t}-e^{-t}<0\). This proves the reverse inequality in (2). Each coefficient \(C(t)\) is positive, continuous, tends to \(2\) as \(t\downarrow0\), and decays exponentially as \(t\to\infty\). Therefore \(\sqrt t\,C(t)\) attains a positive maximum at a finite positive time. Evaluating a strictly dominant curve at the maximizer of a dominated curve gives the strict time-weighted comparison.

**4. Every intermediate exponent forces a time crossover.** Differentiating (1) at zero yields, for every \(\theta\in[0,1]\),
\[
 C_{a,b}^{(\theta)}(t)=2-2\bigl(a^{-\theta}+b^{-\theta}\bigr)t+O_{a,b,\theta}(t^2). \tag{9}
\]
For \(\theta>0\), \(s\mapsto s^{-\theta}\) is strictly convex on positive reals, so the coefficient of \(-t\) in (9) is strictly larger for the more imbalanced split. This proves the small-time ordering in (3). For \(0<\theta<1\) and \(a<b\), the slowest exponential in (1) is \(e^{-a^{1-\theta}t}\), with strictly positive coefficient \(2(1-1/b)\). Since \(a<c\), its decay exponent is strictly smaller than every exponent contributing to \(C_{c,d}^{(\theta)}\). Therefore
\[
 \frac{C_{a,b}^{(\theta)}(t)}{C_{c,d}^{(\theta)}(t)}\longrightarrow\infty
 \qquad(t\to\infty), \tag{10}
\]
proving the large-time ordering. Continuity gives at least one crossing.

**5. Emergence of the short-time crossing at \(\theta=0\).** Expanding (6) at zero gives
\[
 C_{a,b}^{(0)}(t)=2-4t+(3n-2ab)t^2+O_n(t^3). \tag{11}
\]
For fixed strict splits set \(F(\theta,t)=C_{a,b}^{(\theta)}(t)-C_{c,d}^{(\theta)}(t)\), and continuously extend \(R(\theta,t)=F(\theta,t)/t\) to \(t=0\). The exponential formula shows that \(R\) is real analytic near \((0,0)\). By (9) and (11),
\[
 R(0,0)=0,\qquad
 \partial_\theta R(0,0)=-2\log\frac{cd}{ab},\qquad
 \partial_tR(0,0)=2(cd-ab)>0. \tag{12}
\]
The analytic implicit-function theorem yields exactly one local nontrivial solution \(t=t_{a,c}(\theta)\) with \(t(0)=0\), and differentiation gives (4). Its positive derivative at zero proves that the crossing emerges at positive time for small positive \(\theta\). The sign changes across it locally because \(\partial_tR>0\) nearby. This completes the theorem.

## Verification
The accompanying `verify.py` uses the Python standard library and reconstructs the two neighboring heat-kernel rows by Poisson uniformization of the **vertex-level transition matrix**, without using (1) or spectral projectors. It compares their absolute row-difference norm against (1), checks all integer partitions up to designated finite sizes for the two endpoint orders, and checks the analytic small-time slopes and intermediate-exponent spectral ordering. Running `python3 verify.py` passed 4,880 finite numerical/identity assertions. These finite checks are diagnostic only; steps 1–5 provide the proofs for arbitrary admissible parameters.

As an illustration rather than a uniqueness assertion, for \(n=10\), the splits \((1,9)\) and \((5,5)\), and \(\theta=1/2\), one crossing occurs near \(t=0.20023007\); the more balanced graph has the larger coefficient before this crossing, while the star has the larger coefficient afterwards in the evaluated interval.

## Relationship to prior work
The graph heat-gradient and curvature-dimension literature, including Bauer–Horn–Lin–Lippner–Mangoubi–Yau (2013) and Münch (2014), provides general semigroup estimates and motivation for studying differences of heat-evolved bounded data. The three-eigenmode decomposition of complete bipartite chains is classical linear algebra and is not presented as a new spectral identity. The claimed additional result is the **sharp total-variation optimization together with the complete normalization-dependent partition-order trichotomy and quantitative small-exponent crossing law**, for the specified generator family and norm.

Kubo–Namba (2021) addresses monotonicity of a ratio of heat-kernel entries on regular bipartite graphs with four Laplacian eigenvalues, which is not the endpoint gradient norm studied here; its hypotheses also exclude unequal complete bipartite graphs. There are potential formulations in the Markov coupling and Dobrushin-coefficient literature for which a complete historical comparison remains open.

## Limitations
The conclusion concerns only complete bipartite graphs with unit cross edges, real degree exponent \(0\le\theta\le1\), unweighted input supremum norm, and edge-Lipschitz output seminorm. It does not assert analogous extremal orderings for general bipartite graphs, weighted graphs, \(L^p\) input norms, or a stationary-weighted gradient. For \(0<\theta<1\), one or more positive-time crossings are proved, but their global number and uniqueness are not determined. Source comparison remains subject to earlier equivalent statements under total-variation, coupling, or semigroup-contraction terminology.

## References
1. F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi and S.-T. Yau, *Li-Yau inequality on graphs*, arXiv:1306.2561, first submitted 2013-06-11, https://arxiv.org/abs/1306.2561.
2. F. Münch, *Li-Yau inequality on finite graphs via non-linear curvature dimension conditions*, arXiv:1412.3340, first submitted 2014-12-10, https://arxiv.org/abs/1412.3340.
3. T. Kubo and R. Namba, *Monotonic normalized heat diffusion for regular bipartite graphs with four eigenvalues*, arXiv:2103.08149, first submitted 2021-03-15, https://arxiv.org/abs/2103.08149.
