# Sharp heat-variation contraction threshold for complete multipartite graphs

## Finding

**Theorem.** Let \(r\ge2\), let \(n_1,\ldots,n_r\) be positive integers, let \(N=\sum_{i=1}^r n_i\), and let \(G=K_{n_1,\ldots,n_r}\) be the complete multipartite *simple unweighted* graph. Let \(L\) be its counting-measure combinatorial Laplacian and \(H_t=\exp(-tL)\). Define the edge total variation of a real vertex signal by
\[
J_G(f)=\sum_{\{u,v\}\in E(G)}|f(u)-f(v)|.
\]
Then
\[
\boxed{\quad J_G(H_t f)\le J_G(f)\ \text{for every real }f\text{ and }t\ge0
\quad\Longleftrightarrow\quad 2\max_i n_i\le N+2.\quad}
\]
When \(2\max_i n_i>N+2\), choose a vertex \(v\) in a largest part of size \(s=\max_i n_i\). Its singleton indicator has strictly positive initial variation derivative:
\[
\left.\frac{d}{dt}\right|_{0+}J_G(H_t\mathbf1_{\{v\}})
=(N-s)(2s-N-2)>0.
\]
Consequently, it gives strict variation amplification for every sufficiently small positive time. The equality boundary \(2s=N+2\) belongs to the contractive regime.

## Assumptions and scope

All parts are nonempty, \(r\ge2\), and \(N\ge2\). Each edge has conductance one, each vertex has mass one, and the same unit edge weights are used in the variation. The Laplacian is \((Lf)(u)=\sum_{v\sim u}(f(u)-f(v))\). Real vertex data, all nonnegative times, and *one-input* variation are covered. The theorem also gives the two-input bound \(J_G(H_tf-H_tg)\le J_G(f-g)\), by linearity, in the contractive regime.

## Proof

**1. A reduction to cuts.** Put \(Q=-L\). For a nonempty proper vertex subset \(S\), let \(g=\mathbf1_S\). At time zero the derivative \(h=Qg\) satisfies \(h(u)=-d_{S^c}(u)\) for \(u\in S\) and \(h(v)=d_S(v)\) for \(v\notin S\), where \(d_A(z)\) counts neighbors of \(z\) in \(A\). Thus the right derivative \(D_G(S)\) of \(J_G(H_tg)\) at zero is
\[
D_G(S)=\sum_{uv\in E(S)}|d_{S^c}(u)-d_{S^c}(v)|
+\sum_{uv\in E(S^c)}|d_S(u)-d_S(v)|
-\sum_{uv\in\partial S}\big(d_{S^c}(u_S)+d_S(v_{S^c})\big),
\]
where \(u_S\) and \(v_{S^c}\) are respectively the inside and outside endpoints of each crossing edge. This follows by differentiating the absolute value at nonzero edge jumps, and using the one-sided derivative of \(|t\alpha+O(t^2)|\) at zero jumps.

If \(D_G(S)\le0\) for every cut, then \(J_G(H_tf)\) is nonincreasing for every real \(f\). Indeed, sort the distinct values of \(f\) and write \(f=c\mathbf1+\sum_j\delta_j\mathbf1_{S_j}\) with \(\delta_j>0\) and nested upper level sets \(S_j\). Coarea gives \(J_G(f)=\sum_j\delta_jJ_G(\mathbf1_{S_j})\), while the triangle inequality and constant preservation give \(J_G(H_tf)\le\sum_j\delta_jJ_G(H_t\mathbf1_{S_j})\). The two sides agree at zero, so the right derivative of \(J_G(H_tf)\) at zero is at most \(\sum_j\delta_jD_G(S_j)\le0\). Apply the same argument to \(H_sf\) for each \(s\ge0\); the resulting continuous, locally Lipschitz function of time has nonpositive right derivative everywhere and is therefore nonincreasing. Conversely, contraction forces every \(D_G(S)\le0\).

**2. Partition-pair decomposition.** For an arbitrary cut, put \(a_i=|S\cap V_i|\), \(b_i=n_i-a_i\). On an inside vertex in part \(i\), the number of outside neighbors is \(|S^c|-b_i\); on an outside vertex, its inside-neighbor number is \(|S|-a_i\). Grouping cut-derivative terms by the two parts incident to an edge gives
\[
D_G(S)=\sum_{i<j} E(a_i,b_i,a_j,b_j;R_{ij}),\qquad R_{ij}=N-n_i-n_j,
\]
where for nonnegative integers \(a,b,c,d,R\),
\[
E(a,b,c,d;R)=ac|b-d|+bd|a-c|-ad(a+d+R)-bc(b+c+R).
\]
Note that \(R_{ij}\) counts vertices outside the two parts, and that the formula also applies when any of the cut counts is zero.

**3. A discrete pair inequality.** Suppose \(a+b>0\), \(c+d>0\), and
\[
2\max\{a+b,c+d\}\le a+b+c+d+R+2.
\]
We prove \(E(a,b,c,d;R)\le0\). By \(|b-d|\le b+d\) and \(|a-c|\le a+c\), its positive portion is no greater than \(ab(c+d)+cd(a+b)\). The difference between its negative portion and this upper bound is
\[
F=ad(a+d+R)+bc(b+c+R)-ab(c+d)-cd(a+b).
\]
Set \(x=a-c\), \(y=b-d\), and interchange the two parts if necessary so that \(\Delta=x+y=(a+b)-(c+d)\ge0\). Direct expansion gives
\[
F=(y-x)(cy-dx)+R(ad+bc).
\]
If \(\Delta\le2\), integrality forces \(x\) and \(y\) to have opposite weak signs, except possibly \(x=y=1\); hence \((y-x)(cy-dx)\ge0\), so \(F\ge0\).

If \(\Delta\ge3\), the hypothesis gives \(R\ge\Delta-2\), and the same identity at \(R=\Delta-2\) yields
\[
F\ge2\big[ad(x-1)+bc(y-1)\big].
\]
When \(x,y\ge1\), this is nonnegative. If \(x\le0\), then \(c\ge a\), \(b\ge d\), so \(bc\ge ad\), while \(y-1\ge1-x\); thus it is nonnegative. The case \(y\le0\) is symmetric. Hence \(F\ge0\) in every case, proving the pair inequality. The \(+2\) is precisely where the integer argument enters.

**4. Sufficiency and sharpness of the threshold.** If \(2\max_i n_i\le N+2\), the pair inequality applies to every term in the cut decomposition because \(a_i+b_i=n_i\), \(a_j+b_j=n_j\), and \(R_{ij}=N-n_i-n_j\). Thus \(D_G(S)\le0\) for all cuts; step 1 proves contraction for all signals and times.

If a part has size \(s\) with \(2s>N+2\), choose \(S\) consisting of one vertex in that part. Let \(d=N-s>0\) be its degree. The \(d\) boundary edges contribute \(-d(d+1)\), while the \(d(s-1)\) edges from the other \(s-1\) vertices of that part to outside vertices contribute \(+d(s-1)\). All remaining edge contributions vanish. Therefore
\[
D_G(S)=d(s-1)-d(d+1)=d(2s-N-2)>0,
\]
as claimed. Since the initial variation is differentiable from the right, strict amplification occurs at all sufficiently small positive times. This also proves the threshold cannot be strengthened.

## Verification

`verify.py` performs exact-integer checks of the pair identity and inequality (16,566 admissible parameter cases), all nontrivial class-count cuts for 183 integer multipartite profiles with at least two parts and total order at most 11 (32,017 comparisons), and direct edge-by-edge cut-derivative checks for smaller profiles (2,641 comparisons). It verifies strict singleton witnesses in every noncontractive profile, the equality boundary, and the examples \(K_{2,5}\), \(K_{1,4}\), \(K_{1,3}\). Run `python verify.py` with standard Python 3. These finite checks corroborate, but do not prove, the all-order theorem.

## Relationship to prior work

General Markov-chain curvature and transport contraction, including Ollivier's work [1], measure Lipschitz or Wasserstein contraction rather than the sum of edgewise absolute differences used here. The graph heat-gradient literature [2] gives Li–Yau and curvature-dimension estimates for positive solutions, not a sharp all-data, all-time edge-variation classification for complete multipartite graphs. Graph total-variation flow and denoising [3] use the nonlinear flow generated by the variation functional; the linear combinatorial heat flow is different. For these reasons none of the materially inspected statements supplies the equivalence above by specialization. A stronger hidden result in older semigroup literature cannot be excluded.

## Limitations

The threshold is proved only for finite complete multipartite graphs with unit conductances, unit vertex masses, and unit edge-variation weights. It does not classify graphs that are not complete multipartite, arbitrary weighted heat generators, nonlinear variation flows, or sharp amplification factors after contraction fails. It establishes no independence, external certification, or exhaustive literature novelty guarantee.

## References

[1] Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886 (first public version, 30 January 2007), especially the metric-transport definition and contraction discussions. https://arxiv.org/abs/math/0701886

[2] F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi, S.-T. Yau, *Li–Yau inequality on graphs*, arXiv:1306.2561 (first public version, 11 June 2013), Sections 1–4. https://arxiv.org/abs/1306.2561

[3] C. Kirisits, O. Scherzer, E. Setterqvist, *Invariant \(\varphi\)-minimal sets and total variation denoising on graphs*, arXiv:1807.10514 (first public version, 27 July 2018); comparison made from the accessible abstract, not its unavailable full text. https://arxiv.org/abs/1807.10514
