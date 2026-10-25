# Sparse-part Gaussian exposure transition for bipartite PQ adjacency polytopes

## Finding

For an integer \(n\ge 3\), let \(A_n\sqcup B_n=[n]\) with \(|A_n|=p_n\), \(|B_n|=q_n\), and \(p_n+q_n=n\). For the complete bipartite graph \(K_{p_n,q_n}\), take its PQ-type adjacency polytope
\[
P_n=\operatorname{conv}\{(e_i,e_j)\in\mathbb R^{2n}:i=j\text{ or }i\in A_n,j\in B_n\text{ or }i\in B_n,j\in A_n\}.
\]
Its affine tangent space is \(L_n=\{(u,v):\sum_i u_i=\sum_j v_j=0\}\), of dimension \(d_n=2n-2\). Let \(U_n\) be uniformly distributed on the unit sphere of \(L_n\). Write \(W_n=h_{P_n}(U_n)+h_{P_n}(-U_n)\) for its intrinsic directional width and \(I_n\) for the indicator that the vertex uniquely exposed by \(U_n\) has the form \((e_i,e_i)\).

Set
\[
a=\sqrt2-1,\quad \beta=a^2=3-2\sqrt2,\quad C_*=a(4\pi)^a,\quad r_n=\sqrt{2\log n},
\]
\[
b_m=\sqrt{2\log m}-\frac{\log\log m+\log(4\pi)}{2\sqrt{2\log m}},\qquad
\eta_d=\sqrt2\,\frac{\Gamma((d+1)/2)}{\Gamma(d/2)}.
\]
For every fixed \(\delta\in\mathbb R\), define
\[
q_n=\left\lfloor C_*e^{a\delta}n^\beta(\log n)^a\right\rfloor,
\qquad p_n=n-q_n,
\]
for sufficiently large \(n\) so that \(2\le q_n<p_n\). Let \(G_0,G_1,G_2,G_3,G_4\) be independent standard Gumbel variables, with distribution \(\Pr(G_i\le x)=\exp(-e^{-x})\). Put
\[
T_\delta=\max\left\{\sqrt2G_0,\ \delta+G_1+a^{-1}G_2,\ \delta+G_3+a^{-1}G_4\right\}.
\]
Let \(T_\delta^+\) and \(T_\delta^-\) be independent copies of \(T_\delta\). Then
\[
\boxed{r_n\left(\frac{\eta_{d_n}}2 W_n-\sqrt2b_{p_n}\right)
\ \Longrightarrow\ \frac{T_\delta^++T_\delta^-}{2}.}
\]
The corresponding expected-width correction also converges:
\[
\boxed{\lim_{n\to\infty}r_n\left(\frac{\eta_{d_n}}2\mathbb EW_n-\sqrt2b_{p_n}\right)
=\mathbb ET_\delta.}
\]
Define the continuous increasing distribution function
\[
F_a(s)=\int_0^\infty\exp\bigl(-u-e^{-s}u^{-1/a}\bigr)\,du.
\]
The one-sided support correction has explicit distribution
\[
\boxed{\Pr(T_\delta\le t)=\exp(-e^{-t/\sqrt2})F_a(t-\delta)^2.}
\]
Furthermore, the limiting spherical proportion of directions exposing a diagonal vertex is
\[
\boxed{\lim_{n\to\infty}\Pr(I_n=1)
=P_\delta:=\mathbb E\left[F_a(\sqrt2G_0-\delta)^2\right].}
\]
Here \(0<P_\delta<1\), it decreases strictly and continuously with \(\delta\), and \(P_\delta\to1\) as \(\delta\to-\infty\) while \(P_\delta\to0\) as \(\delta\to+\infty\). Each cross-part orientation receives limiting probability \((1-P_\delta)/2\).

There is a sharp polynomial-scale threshold as well. If instead \(q_n=\lfloor n^\gamma\rfloor\) with fixed \(0<\gamma<1\), then
\[
\Pr(I_n=1)\longrightarrow
\begin{cases}
1,&\gamma<3-2\sqrt2,\\
0,&\gamma>3-2\sqrt2.
\end{cases}
\]
At the borderline exponent, the additional factor \((\log n)^{\sqrt2-1}\) is necessary to retain a nondegenerate competition; its prefactor parametrizes the full transition.

## Assumptions and scope

The ambient inner product is the ordinary Euclidean inner product on \(\mathbb R^{2n}\), restricted to the two-block zero-sum tangent space. The polytope is not asserted to be centrally symmetric. A random direction has a unique exposed vertex almost surely because all listed vertices are distinct. The probability statement concerns the *kind* of that exposed vertex, not an individual vertex. The limit takes \(n\to\infty\) with fixed real \(\delta\), respectively fixed \(\gamma\) away from the critical exponent. The formulas specify the actual spherical width normalization, including its intrinsic dimension.

## Proof

**1. Exact finite-dimensional support identity.** Let \((g_i)_{i=1}^n\) and \((h_i)_{i=1}^n\) be two independent families of independent \(N(0,1)\) variables. Define \(D_A=\max_{i\in A_n}(g_i+h_i)\), \(D_B=\max_{i\in B_n}(g_i+h_i)\), and \(M^g_A=\max_{i\in A_n}g_i\), with the analogous three other group maxima. Maximizing a linear form over the defining vertex set gives the exact equality
\[
H_n(g,h):=h_{P_n}(g,h)=\max\{D_A,D_B,M_A^g+M_B^h,M_B^g+M_A^h\}.
\tag{1}
\]
All candidates correspond to permitted vertices and their entries are continuous random variables. The unique exposed vertex is diagonal exactly when the maximum in (1) is supplied by \(D_A\) or \(D_B\).

**2. Critical normalization.** Since \(q_n/n\to0\), \(p_n/n\to1\), \(r_n/b_{p_n}\to1\), and \(r_n/b_{q_n}\to1/a\). Write \(L=\log n\) and \(c=C_*e^{a\delta}\). From
\[
\log q_n=a^2L+a\log L+\log c+o(1)
\]
and Taylor expansion of the defining expression for \(b_m\), one obtains
\[
r_n(b_{q_n}-a b_{p_n})
=\frac{\log(c/a)}{a}-\log(4\pi)+o(1)=\delta+o(1).
\tag{2}
\]
This explains both the critical power \(a^2\) and the logarithmic factor \((\log n)^a\).

**3. Gaussian maxima and the joint limit.** If \(M_m\) is the maximum of \(m\) independent standard Gaussians, the elementary normal-tail estimate yields
\[
b_m(M_m-b_m)\Longrightarrow G,
\tag{3}
\]
where \(G\) is standard Gumbel. The four group maxima in the cross terms of (1) involve distinct independent Gaussian families. Consequently, by (2),
\[
r_n(M_A^g+M_B^h-\sqrt2b_{p_n})\Longrightarrow\delta+G_1+a^{-1}G_2,
\]
\[
r_n(M_B^g+M_A^h-\sqrt2b_{p_n})\Longrightarrow\delta+G_3+a^{-1}G_4.
\tag{4}
\]
For the diagonal part write \(Z_i=(g_i+h_i)/\sqrt2\). The \(Z_i\) are standard normal and independent across indices; hence
\[
r_n(D_A-\sqrt2b_{p_n})\Longrightarrow\sqrt2G_0.
\tag{5}
\]
Meanwhile \(D_B/r_n\to\sqrt2a<\sqrt2\) in probability, whereas \(D_A/r_n\to\sqrt2\), so \(D_B\) is negligible.

The five Gumbel variables in (4)--(5) are *jointly independent in the limit*, even though \(Z_i\) shares its underlying coordinates with \(g_i\) and \(h_i\). Indeed, for a fixed index in \(A_n\), the standardized forms \(g_i,h_i,Z_i\) have all pairwise correlations less than one (their largest is \(1/\sqrt2\)). For two standardized centered Gaussians of correlation \(\rho<1\), the joint exceedance of thresholds \(b_{p_n}+O(1/b_{p_n})\) obeys
\[
p_n\Pr(X>b_{p_n}+O(1/b_{p_n}),Y>b_{p_n}+O(1/b_{p_n}))
\le p_n^{1-2/(1+\rho)+o(1)}\longrightarrow0.
\tag{6}
\]
This follows by bounding the sum \(X+Y\) with its normal tail. The union-of-rare-exceedances formula then gives a product of Gumbel distribution functions; hence asymptotic independence. The two groups are independent by construction. Equations (1)--(6) prove
\[
r_n(H_n(g,h)-\sqrt2 b_{p_n})\Longrightarrow T_\delta.
\tag{7}
\]

The same argument applies *jointly* to \((g,h)\) and \((-g,-h)\). All distinct signed standardized linear forms have pairwise correlation strictly below one (including correlation \(-1\), for which simultaneous positive exceedance is impossible). Therefore their upper-tail point processes are asymptotically independent, giving two independent copies \(T_\delta^+\), \(T_\delta^-\) in the limits for \(H_n(g,h)\) and \(H_n(-g,-h)\).

**4. Euclidean spherical normalization and mean.** Let \(\Pi_n\) be orthogonal projection onto \(L_n\) and \(R_n=\|\Pi_n(g,h)\|_2\). Then \(R_n\) has the chi law in dimension \(d_n=2n-2\), is independent of \(U_n=\Pi_n(g,h)/R_n\), and \(\mathbb ER_n=\eta_{d_n}\). Subtracting means from both Gaussian coordinate groups translates the Gaussian support by an additive scalar, which cancels in widths. Therefore the exact identity
\[
R_nW_n=H_n(g,h)+H_n(-g,-h)
\tag{8}
\]
holds under this coupling. Since \(R_n/\eta_{d_n}=1+O_{\mathbb P}(n^{-1/2})\) and the right side of (8) is \(O_{\mathbb P}(r_n)\), replacing \(R_n\) by \(\eta_{d_n}\) makes an error of \(o_{\mathbb P}(1/r_n)\). This proves the asserted spherical-width distribution.

The centered Gaussian maxima in (3) have bounded second moments on their Gumbel scales, by elementary Gaussian Mills-ratio bounds. Equations (1) and (5) bound the negative part of \(r_n(H_n-\sqrt2b_{p_n})\) by that of the diagonal maximum; its positive part is bounded by the sum of positive parts of the four centered candidates. For the smaller diagonal group, the positive part is bounded by the positive part of its own centered Gaussian maximum because \(b_{q_n}<b_{p_n}\) eventually; for the other three terms, their deterministic center differences remain bounded by (2). Standard Gaussian Mills bounds make all these positive parts uniformly square-integrable. Thus the sequence in (7) is uniformly integrable. Finally, independence of \(R_n\) and \(U_n\), combined with invariance of the uniform sphere under sign change, gives the *exact* identity \(\eta_{d_n}\mathbb EW_n=2\mathbb EH_n(g,h)\). The expectation limit follows.

**5. Explicit law and exposed type.** The transformation \(E=e^{-G}\) maps a standard Gumbel random variable to an independent standard exponential random variable. Conditioning on \(E=e^{-G_2}\) yields
\[
\Pr(G_1+a^{-1}G_2\le s)=\int_0^\infty e^{-u-e^{-s}u^{-1/a}}\,du=F_a(s).
\]
The independence in (7) gives the displayed distribution function of \(T_\delta\). Equality between a diagonal and a cross term in the limit has probability zero. Conditional on \(G_0\), both cross terms are smaller than the diagonal term with probability \(F_a(\sqrt2G_0-\delta)^2\), proving the exposure law. Continuity, strict monotonicity, and endpoint values of \(P_\delta\) follow by dominated convergence and the strict increase of \(F_a\). Symmetry between cross orientations gives their equal probability.

For \(q_n=\lfloor n^\gamma\rfloor\), \(0<\gamma<1\), the Gaussian maxima in (1) satisfy, in probability,
\[
D_A/r_n\to\sqrt2,\quad D_B/r_n\to\sqrt{2\gamma},\quad
(M_A^g+M_B^h)/r_n\to1+\sqrt\gamma,
\]
and the other cross term has the same limit. Comparing \(1+\sqrt\gamma\) with \(\sqrt2\) proves the off-critical dichotomy.

## Verification

The standalone `verify.py` uses direct exhaustive vertex enumeration to check (1) for several sizes and partitions, separately checks affine zero-sum projection invariance of width, evaluates the critical centering (2) for increasing logarithmic scales, and numerically compares the one-sided limiting CDF with independent Gumbel simulations. It also checks the diagonal-versus-cross maximizing rule for random finite cases. Run with `python verify.py` using NumPy and SciPy. All checks are finite consistency tests; they are not substitutes for the asymptotic Gaussian-tail argument.

## Relationship to prior work

Davis and Chen introduced and investigated the graph PQ adjacency-polytope framework in terms of normalized volume and draconian sequences [1]. Ohsugi and Tsuchiya computed Ehrhart and volume information for join graphs, including complete multipartite graphs [2]. Those geometric constructions and their volume results are established literature. Classical univariate Gaussian extremal normalization and asymptotic independence of Gaussian coordinates below correlation one are standard probability inputs [3].

The statement here concerns *intrinsic spherical directional widths and the solid-angle split between diagonal and cross-edge exposed vertices*. Those distributions, and particularly the critical exponent \(3-2\sqrt2\) with its nontrivial logarithmic window, are not implied by the prior volume formulas, Ehrhart data, or an enclosing-ellipsoid computation. No global assertion is made that the probabilistic maximum problem lacks an alternative formulation elsewhere.

## Limitations

The result is asymptotic and supplies no finite-\(n\) rate of convergence for the critical-window distribution. The polytope realization is the standard unweighted Euclidean one, not an arbitrary affine transformation. Only bipartite part sizes of the stated forms are covered. The law describes typical spherical exposure and width, not volume, face counts, or independent external certification. A possible equivalent statement in the general literature on masked Gaussian arrays and their extremes is a residual bibliographic risk.

## References

[1] Robert Davis and Tianran Chen, *Computing Volumes of Adjacency Polytopes via Draconian Sequences*, Electronic Journal of Combinatorics 29(1) (2022), P1.61; first publicly available arXiv:2007.11051, 2020-07-21. https://arxiv.org/abs/2007.11051 ; https://doi.org/10.37236/9768.

[2] Hidefumi Ohsugi and Akiyoshi Tsuchiya, *PQ-Type Adjacency Polytopes of Join Graphs*, Discrete & Computational Geometry 70 (2023), 214--235; arXiv:2103.15045, first version 2021-03-28. https://arxiv.org/abs/2103.15045 ; https://doi.org/10.1007/s00454-022-00447-z.

[3] Standard normal extreme-value theorem (Gumbel domain), Gaussian Mills ratios, and the chi distribution; classical probability facts used with their elementary tail implications shown above.
