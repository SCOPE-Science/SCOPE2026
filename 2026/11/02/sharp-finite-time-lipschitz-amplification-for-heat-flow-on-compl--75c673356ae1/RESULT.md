# Sharp finite-time Lipschitz amplification for heat flow on complete bipartite graphs

## Finding

Let \(p,q\ge1\) be integers. On the unit-edge complete bipartite graph \(K_{p,q}\), let \(L=D-A\) be the **combinatorial**, not degree-normalized, graph Laplacian, and let \(H_t=e^{-tL}\) for \(t\ge0\). For a real vertex function write
\[
\operatorname{Lip}(f)=\max_{uv\in E(K_{p,q})}|f(u)-f(v)|.
\]
This is the graph-metric Lipschitz seminorm, and constants are quotiented out. Write \(m=\min\{p,q\}\) and \(n=\max\{p,q\}\). The exact induced seminorm at every time is
\[
\boxed{\Lambda_{p,q}(t):=\sup_{\operatorname{Lip}(f)\le1}\operatorname{Lip}(H_tf)=\frac{2(n-1)}{n}e^{-mt}-\frac{n-2}{n}e^{-(m+n)t}.}
\]
This uniform formula also holds for the one-edge graph \(p=q=1\), where it reads \(e^{-2t}\). The supremum is attained at every time.

It follows that \(\Lambda_{p,q}(0)=1\) and
\[
\Lambda_{p,q}'(0)=n-m-2.
\]
The semigroup contracts the graph-metric Lipschitz seminorm at every nonnegative time exactly when \(n-m\le2\). In that case it contracts strictly at every positive time. If \(n-m\ge3\), its Lipschitz norm initially exceeds one, has a unique strict positive-time maximum at
\[
t_* =\frac1n\log\!\left(\frac{(n-2)(m+n)}{2m(n-1)}\right),
\]
and thereafter decreases strictly to zero. The peak equals
\[
\boxed{\Lambda_{p,q}(t_*)=\frac{2(n-1)}{m+n}\left(\frac{2m(n-1)}{(n-2)(m+n)}\right)^{m/n}.}
\]
The bound \(\Lambda_{p,q}(t)<2\) holds for all finite \(p,q\ge1\) and \(t\ge0\), and is sharp uniformly over the family: for any fixed \(m\ge1\), the above peaks tend to \(2\) as \(n\to\infty\). Thus the supremum of the time-and-graph amplification factors is \(2\), and it is not attained.

By Kantorovich duality, the same \(\Lambda_{p,q}(t)\) is the exact Wasserstein-\(1\) distance (with unit-edge graph distance) between the two time-\(t\) heat distributions originating at any adjacent pair of vertices.

## Assumptions and scope

Vertices in the first and second parts have degrees \(q\) and \(p\), respectively. The process jumps along **each incident edge at rate one**; the holding rate is therefore the vertex degree. The graph metric assigns length one to every edge. Functions and norms are real, with no vertex-mass weighting. All formulas hold for every pair of positive integers and all real \(t\ge0\). They are not formulas for a degree-normalized random walk, which has a different generator on unbalanced graphs.

## Proof

**Heat decomposition.** Write the parts as \(A=\{a_1,\dots,a_p\}\) and \(B=\{b_1,\dots,b_q\}\), and write \(\bar a=p^{-1}\sum_i f(a_i)\), \(\bar b=q^{-1}\sum_j f(b_j)\). The mean-zero variation inside \(A\) is a \(q\)-eigenvector of \(L\), the mean-zero variation inside \(B\) is a \(p\)-eigenvector, and their part-mean difference evolves with eigenvalue \(p+q\). Consequently, for every cross-edge \(a_i b_j\),
\[
(H_tf)(a_i)-(H_tf)(b_j)
=e^{-qt}(f(a_i)-\bar a)-e^{-pt}(f(b_j)-\bar b)
+e^{-(p+q)t}(\bar a-\bar b).
\]
Define \(x=e^{-qt}\), \(y=e^{-pt}\), \(z=e^{-(p+q)t}=xy\). Then the edge difference equals
\[
z(f(a_i)-f(b_j))+(x-z)(f(a_i)-\bar a)
+(y-z)(\bar b-f(b_j)).
\]
For \(p\ge2\), let \(a_{-i}\) be the arithmetic mean of the other \(p-1\) values in \(A\); for \(p=1\), omit all terms involving \(a_{-i}\). Define \(b_{-j}\) analogously. Set
\[
u=\frac{p-1}{p}(x-z),\qquad v=\frac{q-1}{q}(y-z).
\]
These are nonnegative. The edge difference is exactly
\[
 z(f(a_i)-f(b_j))+u(f(a_i)-a_{-i})+v(b_{-j}-f(b_j)),
\]
with a missing-part term interpreted as zero when its coefficient is zero.

**Sharp Lipschitz edge bound.** Suppose \(\operatorname{Lip}(f)\le1\). Every cross-part difference has absolute value at most one; every same-part difference has absolute value at most two by a path of length two. If \(u\le v\), split the last expression as
\[
z(f(a_i)-f(b_j))
+u\bigl[(f(a_i)-a_{-i})+(b_{-j}-f(b_j))\bigr]
+(v-u)(b_{-j}-f(b_j)).
\]
The bracket is \((f(a_i)-f(b_j))+(b_{-j}-a_{-i})\), hence at most two. The entire expression is therefore at most \(z+2v\). Equality is realized by assigning value zero to every vertex of \(A\), value \(-1\) to \(b_j\), and value \(+1\) to all other vertices of \(B\), provided \(q\ge2\). For \(u\ge v\), interchange the roles: the corresponding bound \(z+2u\) is realized by assigning \(+1\) to \(a_i\), \(-1\) to all other vertices of \(A\), and zero to all of \(B\) (if \(p\ge2\)). The cases with singleton parts follow by omitting the absent term. Applying the same argument to \(-f\) gives the absolute-value norm
\[
 \sup_{\operatorname{Lip}(f)\le1}|(H_tf)(a_i)-(H_tf)(b_j)|=z+2\max\{u,v\}.
\]
All edges lie in one graph-automorphism orbit, so the edge bound is the global induced seminorm.

**Ordering the two terms.** Without loss of generality \(p=m\le n=q\). When \(p=1\), \(u=0\). For \(p\ge2\),
\[
\frac vu=\frac{p(q-1)}{q(p-1)}\frac{e^{qt}-1}{e^{pt}-1}\ge1
\]
for \(t>0\); the expression is interpreted by continuity at \(t=0\). Hence \(\max\{u,v\}=v\), which gives precisely the displayed closed formula. In this orientation an explicit sharp input for every \(q\ge2\) is \(f|_A=0\), \(f(b_j)=-1\), and \(f(b_k)=1\) for \(k\ne j\). For \(p=q=1\), a unit edge difference is sharp.

**Time transition and optimal peak.** For \(n\ge3\), differentiation yields
\[
\Lambda_{p,q}'(t)=\frac{e^{-mt}}n\Big[(n-2)(m+n)e^{-nt}-2m(n-1)\Big].
\]
The bracket is strictly decreasing in \(t\), with value \(n(n-m-2)\) at zero. This proves strict monotone decay if \(n-m\le2\), and a unique positive critical time if \(n-m\ge3\). Solving the critical-point equation gives \(t_*\). At that point the second exponential contributes exactly \(2m(n-1)/(n(m+n))\) times the first exponential, giving the peak expression. For \(n=1,2\), the original closed formula is a strictly decreasing single exponential, so the same contraction classification applies. The derivative at time zero follows by direct differentiation.

**Global amplification barrier.** If \(n\ge3\), the subtracted term is nonnegative, so \(\Lambda_{p,q}(t)\le 2(n-1)e^{-mt}/n<2\); for \(n=2\) the formula is \(e^{-mt}\), and for \(n=1\) it is \(e^{-2t}\). With fixed \(m\) and \(n\to\infty\), one has \(t_*\to0\) and \(e^{-mt_*}\to1\), while \(2(n-1)/(m+n)\to2\). The peak formula therefore converges to two. No finite graph and time attain two.

**Transport interpretation.** For any adjacent vertices \(a_i,b_j\), the two heat-kernel rows are probability measures. Kantorovich–Rubinstein duality equates their graph-metric Wasserstein-\(1\) distance with the supremum of the corresponding heat-output difference over unit-Lipschitz inputs. All edges have the same supremum by symmetry. A path decomposition then shows that the induced global Lipschitz seminorm equals the maximal adjacent-pair transport distance, completing the claim.

## Verification

The included standalone file `verify_heat_lipschitz.py` uses only Python's standard library. It constructs the exact rational heat matrix at \(t=\log 2\) and \(t=2\log 2\) by polynomial spectral interpolation for all \(1\le p,q\le5\). It independently maximizes the edge output over all integer vertices of the bounded graph-Lipschitz potential polytope, using total unimodularity of the directed incidence constraints, and checks the formula exactly in 50 cases. It also samples and checks the predicted monotonicity and unique-peak inequalities. Execute:

`python3 verify_heat_lipschitz.py`

The expected output begins with `CHECK_OK`. The finite tests are reproducibility checks, **not** proofs of the all-size statement; the proof above is analytic and applies to every size and time. Additional independent floating-point checks of matrix exponentials against linear programming were carried out for \(1\le p,q\le7\) at five positive times each, without contributing to the infinite proof.

## Relationship to prior work

Ollivier's coarse-Ricci theory introduced transport-based contraction of Markov kernels, and Veysseire developed the continuous-time curvature and Wasserstein contraction framework. Lin, Lu and Yau studied graph curvatures for degree-normalized random-walk Laplacians. Cheng, Li and Wu subsequently treated graph Markov processes, including complete bipartite examples for the **normalized** generator and a **modified** transport metric; their results concern coupling-based exponential estimates, not this exact all-time original-metric profile for unit rates per edge. A separate existing graph-variation result establishes the same **contractivity threshold** for the combinatorial heat semigroup on multipartite graphs, so that threshold is not asserted to be new. The claim here is the sharp full-time operator norm, its optimizing potentials, the explicit peak and the optimal universal amplification factor.

## Limitations

This calculation is restricted to complete bipartite graphs with identical unit edge conductances, unit graph distances, and the combinatorial Laplacian. It does not establish the corresponding profile for degree-normalized or weighted generators, nonbipartite graph families, other Wasserstein exponents, or general metric-measure spaces. The literature comparison does not exclude unindexed earlier equivalent computations. No independent scientific audit has been performed.

## References

1. Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886v1 (first public 2007-01-30), J. Funct. Anal. 256 (2009), 810–864. https://arxiv.org/abs/math/0701886
2. Y. Lin, L. Lu, S.-T. Yau, *Ricci curvature of graphs*, Tohoku Math. J. 63 (2011), 605–627. https://doi.org/10.2748/tmj/1325886283
3. L. Veysseire, *Coarse Ricci curvature for continuous-time Markov processes*, arXiv:1202.0420v1 (first public 2012-02-02). https://arxiv.org/abs/1202.0420
4. L. Cheng, R. Li, L. Wu, *Ricci curvature and \(W_1\)-exponential convergence of Markov processes on graphs*, arXiv:1907.11036v1 (2019-07-25), particularly Examples 2.11 and 3.21. https://arxiv.org/abs/1907.11036
