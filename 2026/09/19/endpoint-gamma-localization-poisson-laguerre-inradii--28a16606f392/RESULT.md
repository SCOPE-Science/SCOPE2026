# Endpoint-Gamma localization for large Poisson–Laguerre inradii

## Result

Let \(d\ge 3\). Consider the stationary marked Poisson process used by Schulte and Švarc Petráková to generate a Poisson–Laguerre tessellation in \(\mathbb R^d\), with ground intensity \(\gamma>0\), i.i.d. marks \(M\sim\mathbb Q\), and observation windows \(W_\rho=\rho W\), where \(W\) has volume one. Assume that the marks have finite essential upper endpoint \(A>0\), and strengthen the endpoint hypothesis to
\[
\mathbb Q([A-y,A])\sim C y^\beta\qquad(y\downarrow0)
\]
for constants \(C>0\) and \(\beta>0\).

Write \(v_d\) for the volume of the unit ball, \(c_d=2^dv_d\), and define the endpoint-localization scale
\[
 t_{d,\rho}:=d(v_d\gamma)^{2/d}(\log \rho^d)^{(d-2)/d}.
\]
Let \(s_{d,\rho}\) be any correct shift in the sense of Schulte--Švarc Petráková, i.e. a shift for which the expected number of cells above normalized inradius level \(u\) tends to \(e^{-u}\).

Define the refined extreme-cell point process
\[
\Xi_\rho^*=
\sum_{(x,m)\in\eta\cap(W_\rho\times[0,A])}
\delta_{\left(x/\rho,\ t_{d,\rho}(A-m),\ c_d\gamma r((x,m),\eta)^d-s_{d,\rho}\right)}.
\]
Then
\[
\boxed{\Xi_\rho^*\ \Longrightarrow\ \Pi_d^*}
\]
in the locally finite point-measure topology, where \(\Pi_d^*\) is a Poisson process on \(W\times[0,\infty)\times\mathbb R\) with product intensity
\[
\boxed{\lambda_d|_W\otimes \Gamma_{\beta,\,2A}\otimes\mathbb K.}
\]
Here \(\Gamma_{\beta,2A}\) denotes the Gamma law with shape \(\beta\) and rate \(2A\), and \(\mathbb K([u,v])=e^{-u}-e^{-v}\).

Consequently, if \((X_{\max,\rho},M_{\max,\rho},R_{\max,\rho})\) denotes the nucleus, mark and inradius of the cell with largest inradius in \(W_\rho\), then
\[
\boxed{
\left(\frac{X_{\max,\rho}}\rho,\ t_{d,\rho}(A-M_{\max,\rho}),\ c_d\gamma R_{\max,\rho}^d-s_{d,\rho}\right)
\Longrightarrow (U,Y,G),
}
\]
where \(U\sim\operatorname{Unif}(W)\), \(Y\sim\Gamma(\beta,2A)\), and \(G\sim\operatorname{Gumbel}\) are independent. Thus
\[
A-M_{\max,\rho}=\Theta_{\mathbb P}\!\left((\log\rho)^{-(d-2)/d}\right).
\]

## Three-dimensional explicit shift

For \(d=3\), put \(L_\rho=\log\rho^3\) and \(t_\rho=3(v_3\gamma)^{2/3}L_\rho^{1/3}\). Equation (1.7) of Schulte--Švarc Petráková gives
\[
s_{3,\rho}=L_\rho-t_\rho\mathbb E M^2+\log\mathbb E e^{t_\rho M^2}+\log\gamma.
\]
The endpoint assumption implies
\[
\mathbb E e^{tM^2}\sim e^{tA^2}C\Gamma(\beta+1)(2At)^{-\beta}.
\]
Hence
\[
\boxed{
 s_{3,\rho}=L_\rho+t_\rho(A^2-\mathbb E M^2)-\beta\log t_\rho
 +\log\!\left(\frac{\gamma C\Gamma(\beta+1)}{(2A)^\beta}\right)+o(1).
}
\]
Equivalently, with \(a_3=3(v_3\gamma)^{2/3}\),
\[
\boxed{
 s_{3,\rho}=L_\rho+a_3(A^2-\mathbb E M^2)L_\rho^{1/3}
 -\frac\beta3\log L_\rho
 +\log\!\left(\frac{\gamma C\Gamma(\beta+1)}{(2Aa_3)^\beta}\right)+o(1).
}
\]

## Version-1 correction to the source examples

The source paper's equation (1.7) contains \(+\log\gamma\), and its Poisson--Voronoi specialization has shift \(\log(\gamma\rho^d)\). In arXiv:2609.20750v1, however, the two displayed \(d=3\) shifts in Example 3.11, equations (3.23) and (3.24), omit \(+\log\gamma\).

For \(\mathbb Q_1=\sum_{i=1}^Kp_i\delta_{A_i}\), the corrected polished formula is
\[
\boxed{\log\rho^3+3(v_3\gamma)^{2/3}(A_K^2-\mathbb EM_1^2)(\log\rho^3)^{1/3}+\log p_K+\log\gamma.}
\]
For density \(2s/A^2\) on \([0,A]\), the corrected formula is
\[
\boxed{\log\rho^3+3(v_3\gamma)^{2/3}(A^2-\mathbb EM_2^2)(\log\rho^3)^{1/3}-\frac13\log\log\rho^3-\log\!\big(3(v_3\gamma)^{2/3}A^2\big)+\log\gamma.}
\]
Without this term, \(G_{3,\rho}\) tends to \(\gamma\), rather than \(1\), at the proposed shift; the formulas are therefore correct as written only for \(\gamma=1\). This is a version-specific correction to arXiv:2609.20750v1.

## Proof

Schulte--Švarc Petráková reduce the bounded-mark intensity to
\[
G_{d,\rho}(x)=\gamma\int_0^A\exp\!\left(-x-\sum_{i=1}^{\lfloor d/2\rfloor}\beta_{i,d}(s)(\log\rho^d+x)^{(d-2i)/d}\right)\,\mathbb Q(ds),
\]
where \(\beta_{i,d}(s)=\alpha_{i,d}\mathbb E(M^2-s^2)^i\). Their Taylor coefficient is \(c_{1,d}=d2^{d-2}\), hence
\[
\alpha_{1,d}=d(v_d\gamma)^{2/d}.
\]
If \(x_\rho=s_{d,\rho}-\log\rho^d\), their Corollary 3.3 gives \(x_\rho=o(\log\rho^d)\). Uniformly for bounded score shifts, the leading mark-dependent factor near \(s=A\) is therefore
\[
\exp\{t_{d,\rho}(s^2-A^2)+o(1)\}.
\]
For \(s=A-y/t_{d,\rho}\), this exponent is \(-2Ay+o(1)\). For every \(i\ge2\), \(\beta_{i,d}(s)\) is a polynomial in \(s^2\) with bounded derivative, and its endpoint variation is
\[
O\!\left((\log\rho^d)^{(d-2i)/d}/t_{d,\rho}\right)=O\!\left((\log\rho^d)^{-2(i-1)/d}\right)=o(1).
\]
Thus higher terms do not change the endpoint scale or rate \(2A\).

The endpoint assumption gives the vague convergence
\[
t^\beta\mathbb Q\big(t(A-M)\in dy\big)\Longrightarrow C\beta y^{\beta-1}dy.
\]
After exponential weighting,
\[
\frac{\mathbb E[e^{tM^2}\mathbf 1\{t(A-M)\in dy\}]}{\mathbb E e^{tM^2}}
\Longrightarrow \frac{(2A)^\beta}{\Gamma(\beta)}y^{\beta-1}e^{-2Ay}dy,
\]
whose Laplace transform is \((2A/(2A+z))^\beta\). This identifies \(\Gamma(\beta,2A)\). The scalar endpoint-Gamma tilting mechanism is classical; its use here is to refine the large-inradius marked process.

The uniform remainder estimate in the source paper's Lemma 3.4 applies equally to shrinking endpoint windows, so the exact large-inradius intensity has the same limit. The stabilization/Palm approximation in Proposition 3.10 is unchanged after replacing the mark coordinate \(m\) by \(t_{d,\rho}(A-m)\), because the exceedance event and stabilization neighborhoods are identical. Applying the same approximation on bounded score windows and the preceding intensity convergence yields the refined Poisson-process limit. The maximum-cell statement follows from the source paper's unique-argmax continuous-mapping argument.

For \(d=3\), writing \(Y=A-M\) gives
\[
e^{-tA^2}\mathbb E e^{tM^2}=\mathbb E e^{-t(2AY-Y^2)}\sim C\Gamma(\beta+1)(2At)^{-\beta},
\]
by the Laplace--Stieltjes/Karamata theorem, and substitution into equation (1.7) gives the explicit shift.

For the continuous distribution in Example 3.11,
\[
\mathbb E e^{tM^2}=\frac{e^{A^2t}-1}{A^2t},
\]
so equation (1.7) directly gives the corrected formula with \(+\log\gamma\). The discrete case is analogous. Omitting \(+\log\gamma\) shifts the normalization by \(-\log\gamma\), multiplying the limiting expected exceedance count by \(\gamma\).

## Verification

`artifacts/verify_endpoint_localization.py` checks two independent consequences. For the continuous Example 3.11 law with \(A=1.7\), \(\gamma=0.4\), the formula without \(+\log\gamma\) approaches normalization \(0.4\), while the corrected formula approaches \(1\). For \(M=AX\), \(X\sim\mathrm{Beta}(2.3,1.5)\), direct quadrature verifies both the predicted endpoint Laplace constant and convergence of the scaled tilted endpoint gap to \(\Gamma(1.5,2A)\). Numerical output is in `artifacts/verification.txt`.

## Relation to prior work and originality scope

Schulte and Švarc Petráková (2026) prove the Gumbel extreme-inradius point-process limit for bounded marks and show that for \(d\ge3\) the unscaled extreme-cell mark converges to \(A\). They give an exact correct shift for \(d=3\) and selected explicit examples, but do not state a non-degenerate endpoint rescaling or limiting law.

Gamma limits under strong exponential tilting are classical. Balkema, Klüppelberg and Resnick studied normal/Gamma domains of attraction for natural exponential families, and Karamata's Laplace--Stieltjes theory supplies the transform asymptotic. No novelty is claimed for that scalar principle alone.

The claimed contribution is restricted to the refined marked Poisson limit and maximum-cell localization law, the dimension-dependent scale \((\log\rho)^{-(d-2)/d}\), the general \(d=3\) endpoint-tail shift with its \(-\beta\log\log\rho/3\) term, and the missing-\(+\log\gamma\) correction to Example 3.11 of arXiv:2609.20750v1. These claims are made to the best of our knowledge.

## Limitations

The endpoint assumption is a pure power law with constant \(C\); slowly varying endpoint factors are not stated. The refined process inherits the bounded-mark, stationarity and Poisson assumptions of the source theorem. No quantitative convergence rate is proved. The explicit shift expansion is given only for \(d=3\). The source-formula correction refers specifically to arXiv:2609.20750v1 and may be fixed in a later version.

## References

1. M. Schulte and M. Švarc Petráková, *Point process convergence of large inradii of Poisson–Laguerre tessellations*, arXiv:2609.20750v1 (2026). https://arxiv.org/abs/2609.20750v1
2. O. Bobrowski, M. Schulte and D. Yogeshwaran, *Poisson process approximation under stabilization and Palm coupling*, Annales Henri Lebesgue 5 (2022), 1489–1534. https://doi.org/10.5802/ahl.156
3. A. A. Balkema, C. Klüppelberg and S. I. Resnick, *Domains of attraction for exponential families*, Stochastic Processes and their Applications 107 (2003), 83–103. https://doi.org/10.1016/S0304-4149(03)00060-7
4. A. A. Balkema, C. Klüppelberg and S. I. Resnick, *Limit laws for exponential families*, Bernoulli 5 (1999), 951–968. https://doi.org/10.2307/3318554
5. N. H. Bingham, C. M. Goldie and J. L. Teugels, *Regular Variation*, Cambridge University Press (1987).
