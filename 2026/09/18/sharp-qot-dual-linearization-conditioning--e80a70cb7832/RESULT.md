# Sharp small-regularization conditioning of the QOT dual linearization

## Statement

Assume the smooth continuous quadratic-cost setting of Assumption 1.1 in González-Sanz and Nutz, *Geometry and Convergence of Quadratically Regularized Optimal Transport I* (arXiv:2609.20400), and let
\[
\ell=\varepsilon^{1/(d+2)}.
\]
Let \(E_\varepsilon\) be the support of the optimal quadratically regularized coupling. On
\[
\mathcal H_\oplus=\{(u,v):\int u\,d\mu=\int v\,d\nu\},
\]
the self-adjoint support operator from the optimizer linearization in arXiv:2509.08547 has quadratic form
\[
\langle (u,v),M_{\varepsilon,\oplus}(u,v)\rangle
=\iint_{E_\varepsilon}(u(x)+v(y))^2\,d\mu(x)d\nu(y).
\]
Define the positive dual curvature operator
\[
H_\varepsilon=\varepsilon^{-1}M_{\varepsilon,\oplus}.
\]
Then, for all sufficiently small \(\varepsilon\), there are constants \(0<c<C<\infty\), depending only on the fixed problem data, such that
\[
\boxed{c\|w\|^2\le \langle w,H_\varepsilon w\rangle\le C\ell^{-2}\|w\|^2\qquad(w\in\mathcal H_\oplus).}
\]
Both orders are sharp. If
\[
\underline\lambda_\varepsilon=\inf_{w\ne0}\frac{\langle w,H_\varepsilon w\rangle}{\|w\|^2},
\qquad \overline\lambda_\varepsilon=\|H_\varepsilon\|,
\]
then
\[
\boxed{\underline\lambda_\varepsilon\asymp1,\qquad
\overline\lambda_\varepsilon\asymp\varepsilon^{-2/(d+2)},\qquad
\kappa(H_\varepsilon)\asymp\varepsilon^{-2/(d+2)}.}
\]
Thus smooth QOT has an order-one soft curvature scale and a stiff scale of order \(\varepsilon^{-2/(d+2)}\) at the dual optimizer.

## Proof

Let \(T:X\to Y\) be the Brenier map, \(S=T^{-1}\), and write the optimal QOT density as
\[
h_\varepsilon(x,y)=\varepsilon^{-1}\bigl(f_\varepsilon(x)+g_\varepsilon(y)-\tfrac12|x-y|^2\bigr)_+.
\]
Pull the second coordinate back to \(X\):
\[
k_\varepsilon(x,z)=h_\varepsilon(x,T(z)).
\]
Since \(h_\varepsilon\) has both marginals equal to one and \(T_\#\mu=\nu\), \(k_\varepsilon\) is doubly stochastic with respect to \(\mu\). Let \(K_\varepsilon\) be its Markov operator.

The sharp geometry in arXiv:2609.20400 gives, at scale \(\ell\): support localization within \(O(\ell)\) of the Brenier graph; row and column section masses \(\Theta(\ell^d)\); row slack \(O(\ell^2)\), hence \(k_\varepsilon\le C\ell^{-d}\); and the local overlap estimate of Lemma 6.4. Consequently the symmetric two-step kernel
\[
P_\varepsilon(x,x')=\int k_\varepsilon(x,z)k_\varepsilon(x',z)\,d\mu(z)
\]
satisfies
\[
c\ell^{-d}{\bf1}_{|x-x'|\le a\ell}\le P_\varepsilon(x,x')
\le C\ell^{-d}{\bf1}_{|x-x'|\le B\ell}
\]
with the lower inequality understood on the smaller ball. Lemma 6.8 of that paper therefore yields, for mean-zero \(\phi\),
\[
\langle\phi,(I-P_\varepsilon)\phi\rangle\ge c\ell^2\|\phi\|_2^2.
\]
As \(P_\varepsilon=K_\varepsilon K_\varepsilon^*\),
\[
\|K_\varepsilon\|_{L^2_0\to L^2_0}\le1-c'\ell^2.
\]

For \((u,v)\in\mathcal H_\oplus\), put \(b=v\circ T\). Then \(u,b\) have the same mean \(m\). Writing \(u=m+u_0\), \(b=m+b_0\),
\[
\iint k_\varepsilon(x,z)(u(x)+b(z))^2\,d\mu(x)d\mu(z)
=4m^2+\|u_0\|_2^2+\|b_0\|_2^2+2\langle u_0,K_\varepsilon b_0\rangle
\ge c\ell^2(\|u\|_2^2+\|b\|_2^2).
\]
If \(A_\varepsilon=\{(x,z):(x,T(z))\in E_\varepsilon\}\), then \(k_\varepsilon\le C\ell^{-d}{\bf1}_{A_\varepsilon}\), so
\[
{\bf1}_{A_\varepsilon}\ge c\ell^d k_\varepsilon.
\]
Therefore
\[
\langle w,M_{\varepsilon,\oplus}w\rangle
\ge c\ell^{d+2}\|w\|^2=c\varepsilon\|w\|^2,
\]
which gives the uniform lower bound for \(H_\varepsilon\).

For the upper bound, the row and column section masses are \(O(\ell^d)\), hence
\[
\iint_{E_\varepsilon}(u+v)^2\,d\mu d\nu\le C\ell^d\|(u,v)\|^2,
\]
and thus \(\overline\lambda_\varepsilon\le C\ell^d/\varepsilon=C\ell^{-2}\).

The exponents are optimal. Taking \(u=v=1\) gives a Rayleigh quotient comparable to
\[
(\mu\otimes\nu)(E_\varepsilon)/\varepsilon\asymp\ell^d/\varepsilon=\ell^{-2},
\]
so \(\overline\lambda_\varepsilon\ge c\ell^{-2}\). For the lower edge, take a fixed nonconstant Lipschitz \(\phi\) with \(\int\phi\,d\mu=0\), set \(u=\phi\), \(v=-\phi\circ S\), and use the inverse support localization \(|x-S(y)|\le C\ell\) on \(E_\varepsilon\). Then \(|u(x)+v(y)|\le C\ell\), while \((\mu\otimes\nu)(E_\varepsilon)=O(\ell^d)\). Its \(H_\varepsilon\)-Rayleigh quotient is therefore \(O(\ell^{d+2}/\varepsilon)=O(1)\), proving \(\underline\lambda_\varepsilon\le C\).

## Linearized algorithmic consequence

For a scalar gradient-ascent step \(\eta\), the optimizer linearization is
\[
L_{\eta,\varepsilon}=I-\eta H_\varepsilon.
\]
Hence the local linearized stability ceiling is
\[
\eta<2/\overline\lambda_\varepsilon
=\Theta(\varepsilon^{2/(d+2)}).
\]
With the optimally tuned scalar step, the worst-case contraction factor is
\[
\frac{\kappa(H_\varepsilon)-1}{\kappa(H_\varepsilon)+1}
=1-\Theta(\varepsilon^{2/(d+2)}),
\]
and the linearized iteration count for error reduction by a factor \(\tau\) is
\[
\boxed{\Theta\!\left(\varepsilon^{-2/(d+2)}\log\frac1\tau\right).}
\]
This is strictly an optimizer-local linearized statement. The existing nonlinear gradient-ascent theorem uses the sufficient global restriction \(\eta<\varepsilon\), which also controls iterates away from the optimizer. No global validity of the larger local step is claimed.

## Relation to prior work

The linear-convergence paper arXiv:2509.08547 identifies \(M_{\varepsilon,\oplus}\) and proves strict contraction of the optimizer linearization, but does not quantify its small-\(\varepsilon\) condition number. The PL paper arXiv:2605.27175 gives explicit curvature constants in broader continuous and semi-discrete settings through generic support-overlap chains, not the sharp smooth-marginal exponent above. The new geometry paper arXiv:2609.20400 supplies the sharp support scale, local overlap, and nonlocal Poincare estimate used here and notes that its geometry can sharpen prior PL and algorithmic analyses, but does not state this spectral-conditioning theorem or the matching spectral-edge witnesses.

## Limitations

The result requires the smooth continuous quadratic-cost regime of Assumption 1.1 in arXiv:2609.20400 and sufficiently small \(\varepsilon\). It is not a global nonlinear convergence theorem. Semi-discrete transport, rough marginals, other costs, discretization error, and floating-point effects are outside scope.

The companion *Geometry and Convergence of Quadratically Regularized Optimal Transport II*, cited in arXiv:2609.20400 as a 2026 working paper, was not available for inspection and may contain overlapping small-regularization consequences. Originality is therefore asserted only to the best of our knowledge.

## References

1. A. González-Sanz and M. Nutz, *Geometry and Convergence of Quadratically Regularized Optimal Transport I*, arXiv:2609.20400 (2026), https://arxiv.org/abs/2609.20400.
2. A. González-Sanz, M. Nutz, and A. Riveros Valdevenito, *Linear Convergence of Gradient Descent for Quadratically Regularized Optimal Transport*, arXiv:2509.08547 (2026 version), https://arxiv.org/abs/2509.08547.
3. A. González-Sanz, M. Nutz, and A. Riveros Valdevenito, *Polyak-Lojasiewicz Inequality for Quadratically Regularized Optimal Transport*, arXiv:2605.27175 (2026), https://arxiv.org/abs/2605.27175.
