# Quantile curvature and endpoint rates for two-gamma sums

## Statement

Let \(X_1,X_2\) be independent \(\Gamma(r,1)\) random variables with \(r>0\), and define
\[
Z_\alpha=\alpha X_1+(2-\alpha)X_2.
\]
For \(q\in(0,1)\), write \(Q_q(\alpha)\) for the \(q\)-quantile of \(Z_\alpha\). Let \(G_s\) denote the \(\Gamma(s,1)\) distribution function and put
\[
a=2r,\qquad m_q=G_a^{-1}(q).
\]
Then, as \(\varepsilon\to0\),
\[
\boxed{
Q_q(1+\varepsilon)
=m_q-
\frac{m_q(a+1-m_q)}{2(a+1)}\,\varepsilon^2
+O(\varepsilon^4).
}
\]
Consequently, with
\[
q_*(r)=G_{2r}(2r+1),
\]
the equal-weight point \(\alpha=1\) is a strict local maximum of \(Q_q\) when \(q<q_*(r)\), and a strict local minimum when \(q>q_*(r)\). At the critical quantile the quadratic coefficient vanishes, but the next term is positive:
\[
\boxed{
Q_{q_*(r)}(1+\varepsilon)
=2r+1+\frac{2r+1}{2(2r+3)}\,\varepsilon^4+O(\varepsilon^6).
}
\]
Thus the equal-weight quantile has a quartically flat strict local minimum at the transition. Since \(G_{2r}(2r)>1/2\), one has \(q_*(r)>1/2\), so the median lies on the local-maximum side, consistently with the known global median theorem.

The endpoints also admit explicit first derivatives. If \(u_q=G_r^{-1}(q)\), then
\[
\boxed{
Q_q(\alpha)=2u_q+(r-u_q)\alpha+O(\alpha^2),\qquad \alpha\downarrow0,
}
\]
and, for the signed regime \(\alpha>2\),
\[
\boxed{
Q_q(2+\delta)=2u_q+(u_q-r)\delta+O(\delta^2),\qquad \delta\downarrow0.
}
\]
For \(q=1/2\), the gamma median satisfies \(u_q<r\), so these derivatives have the signs required by the known monotonicity results.

## Consequences for variance-gamma and McKay medians

For the variance-gamma parametrization in Gaunt and Ouimet, let
\(V_{R,\theta,\sigma}\sim\mathrm{VG}(R,\theta,\sigma,0)\), with \(R>0\), \(\theta>0\), and put \(s=R/2\). If \(g_s\) denotes the median of \(\Gamma(s,1)\), then
\[
\boxed{
\operatorname{Med}(V_{R,\theta,\sigma})
=2\theta g_s-\frac{s-g_s}{2\theta}\sigma^2+O(\sigma^4),
\qquad \sigma\downarrow0.
}
\]
Hence the gamma-limit median in their Corollary 2.3 is approached quadratically in the noise scale.

For the McKay Type I parametrization \(Z_{m,c,\phi}\) used there, let \(s=m+1/2>0\) and keep \(\phi>0\) fixed. Then
\[
\boxed{
\operatorname{Med}(Z_{m,c,\phi})
=2\phi g_s+\phi(s-g_s)(c-1)+O((c-1)^2),
\qquad c\downarrow1,
}
\]
while, as \(c\to\infty\),
\[
\boxed{
\operatorname{Med}(Z_{m,c,\phi})
=\phi g_{2s}
-\phi\frac{g_{2s}(2s+1-g_{2s})}{2(2s+1)}c^{-2}
+O(c^{-4}).
}
\]
Thus the two gamma endpoints in the McKay interpolation are approached at different rates: linearly at \(c\downarrow1\) and quadratically at \(c\to\infty\).

## Proof of the equal-weight expansion

Use the beta-gamma factorization
\[
S=X_1+X_2\sim\Gamma(a,1),\qquad
P=\frac{X_1}{S}\sim\mathrm{Beta}(r,r),
\]
with \(S\) and \(P\) independent. Set \(V=2P-1\). Then \(V\) is symmetric and
\[
Z_{1+\varepsilon}=S(1+\varepsilon V),
\]
with
\[
\mathbb EV^2=\frac1{a+1},\qquad
\mathbb EV^4=\frac{3}{(a+1)(a+3)}.
\]
Let \(F_\varepsilon(z)=\Pr\{Z_{1+\varepsilon}\le z\}\). For \(|\varepsilon|<1\),
\[
F_\varepsilon(z)=\mathbb E\,G_a\!\left(\frac{z}{1+\varepsilon V}\right).
\]
Symmetry of \(V\) makes \(F_\varepsilon\), and hence \(Q_q(1+\varepsilon)\), an even function of \(\varepsilon\). Write
\[
Q_q(1+\varepsilon)=m_q+A\varepsilon^2+O(\varepsilon^4).
\]
Taylor expansion of the preceding expectation at \((z,\varepsilon)=(m_q,0)\) gives
\[
0=f_a(m_q)\left[
A+\frac{m_q}{a+1}
+\frac{m_q^2}{2(a+1)}\frac{f_a'(m_q)}{f_a(m_q)}
\right]\varepsilon^2+O(\varepsilon^4),
\]
where
\[
\frac{f_a'(x)}{f_a(x)}=\frac{a-1-x}{x}.
\]
Solving for \(A\) yields
\[
A=-\frac{m_q(a+1-m_q)}{2(a+1)}.
\]
The sign change therefore occurs exactly at \(m_q=a+1\), proving the stated threshold.

At the critical value \(m_q=a+1\), put
\[
Q_{q_*}(1+\varepsilon)=a+1+B\varepsilon^4+O(\varepsilon^6).
\]
Carrying the same expansion to fourth order and using the displayed second and fourth moments of \(V\) gives
\[
0=f_a(a+1)\left[B-\frac{a+1}{2(a+3)}\right]\varepsilon^4+O(\varepsilon^6),
\]
so
\[
B=\frac{a+1}{2(a+3)}>0.
\]

## Endpoint derivatives

At \(\alpha\downarrow0\), condition on \(X_1=x\):
\[
F_\alpha(z)=\mathbb E\,G_r\!\left(\frac{z-\alpha X_1}{2-\alpha}\right).
\]
At \(z=2u_q\), differentiation at \(\alpha=0\) gives
\[
\partial_\alpha F_\alpha(2u_q)|_{0}
=\frac12 f_r(u_q)(u_q-r),
\qquad
\partial_zF_0(2u_q)=\frac12 f_r(u_q).
\]
Implicit differentiation of \(F_\alpha(Q_q(\alpha))=q\) therefore yields \(Q_q'(0+)=r-u_q\).

For \(\alpha=2+\delta\), write
\[
Z_{2+\delta}=(2+\delta)X_1-\delta X_2.
\]
Conditioning on \(X_2\) and differentiating at \(\delta=0+\) gives \(Q_q'(2+)=u_q-r\). Smoothness in a neighborhood of the positive reference quantile gives the stated quadratic remainders.

## Relation to prior work and originality scope

Gaunt and Ouimet (2026) prove global median monotonicity for the same two-gamma family and derive the variance-gamma and McKay consequences, including the endpoint limits. Bock, Diaconis, Huffer and Perlman (1987), and Diaconis and Perlman (1990), develop majorization and crossing theory for weighted sums of gamma variables. Yu (2017) proves broad unique-crossing results and discusses the earlier crossing-location theory. Those crossing and Schur-convexity results are prior art and are not claimed here.

The originality claim is deliberately narrower: to the best of our knowledge, the explicit local \(q\)-quantile curvature coefficient, the exact transition \(q_*(r)=G_{2r}(2r+1)\), the positive critical quartic coefficient, and the displayed variance-gamma/McKay median endpoint rates are not stated in the inspected sources or located by searches for equivalent formulations. The complete texts of Diaconis--Perlman (1990) and Bock et al. (1987) were not directly inspected, so they remain the main residual originality risk for the weighted-gamma component.

## Verification

`artifacts/verify_gamma_quantiles.py` numerically evaluates the exact beta-gamma integral for \(0<\alpha<2\), a one-dimensional gamma-difference integral for \(\alpha>2\), and then inverts the resulting cdfs. The accompanying output checks the quadratic coefficient on both sides of the quantile transition, convergence to the critical quartic coefficient, both endpoint derivatives, and the McKay/variance-gamma asymptotic formulas.

## Limitations

The theorem concerns two iid gamma summands and local parameter regimes. No global quantile crossing theorem is asserted beyond the already known median result, and no parameter-uniform remainder bounds are proved. The variance-gamma and McKay statements inherit the parametrizations of the source paper. The full Diaconis--Perlman (1990) and Bock et al. (1987) texts were not directly inspected, leaving residual originality uncertainty for the crossing-related component.

## References

1. R. E. Gaunt and F. Ouimet, *Bounds for the median of the generalized hyperbolic and related distributions*, arXiv:2609.20212 (2026), https://arxiv.org/abs/2609.20212.
2. M. E. Bock, P. Diaconis, F. W. Huffer and M. D. Perlman, *Inequalities for linear combinations of gamma random variables*, Canadian Journal of Statistics 15 (1987), 387--395, https://doi.org/10.2307/3315257.
3. P. Diaconis and M. D. Perlman, *Bounds for tail probabilities of weighted sums of independent gamma random variables*, Lecture Notes--Monograph Series 16 (1990), 147--166, https://doi.org/10.1214/lnms/1215457557.
4. Y. Yu, *On the unique crossing conjecture of Diaconis and Perlman on convolutions of gamma random variables*, arXiv:1607.02689 (2017), https://arxiv.org/abs/1607.02689.
