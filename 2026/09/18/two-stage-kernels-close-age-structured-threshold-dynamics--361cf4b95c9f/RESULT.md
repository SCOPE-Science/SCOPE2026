# Two-stage reproductive kernels force complete threshold convergence in a bistable age-structured population model

## Result

Consider the Gurtin--MacCamy problem
\[
\partial_tu+\partial_au=-\mu(a)u,\qquad
u(t,0)=f\!\left(\int_0^\infty \beta(a)u(t,a)\,da\right),
\qquad u(0,\cdot)=u_0\in L^1_+(0,\infty),
\]
under Assumption 1.1 of Griette--Herrera (2026): \(\mu\in L^\infty_+\) is bounded below by a positive constant, \(f\in C^1(\mathbb R_+,\mathbb R_+)\) is strictly increasing with bounded derivative, its only fixed points are \(0<\kappa_1<\kappa_2\) together with \(0\),
\[
f'(0)<1,\qquad f'(\kappa_1)>1,\qquad f'(\kappa_2)<1,
\]
and \(\limsup_{x\to\infty}f(x)/x<1\).

Let
\[
M(a)=\int_0^a\mu(s)\,ds.
\]
Choose rates \(r_1,r_2>\|\mu\|_\infty\). If \(r_1\ne r_2\), relabel them so that \(r_1<r_2\) and prescribe the noncompact fertility rate
\[
\boxed{
\beta(a)=e^{M(a)}K(a),\qquad
K(a)=\frac{r_1r_2}{r_2-r_1}\left(e^{-r_1a}-e^{-r_2a}\right).
}
\]
If \(r_1=r_2=r\), use the continuous Erlang-2 limit \(K(a)=r^2ae^{-ra}\).
Then \(\beta\in L^\infty_+(0,\infty)\), \(\beta(a)>0\) for \(a>0\), and
\[
\int_0^\infty \beta(a)e^{-M(a)}\,da=\int_0^\infty K(a)\,da=1.
\]
Thus this is an admissible, genuinely noncompact fertility rate. It is not in the eventually-constant class treated in Theorem 1.3 of Griette--Herrera. In the coincident-rate case the corresponding fertility is \(\beta(a)=r^2ae^{M(a)-ra}\).

For every nonnegative initial datum, the full age-structured solution converges in \(L^1\) to exactly one of the three equilibria
\[
\bar\varphi_j(a)=\kappa_j e^{-M(a)},\qquad j=0,1,2,
\]
with \(\kappa_0=0\). In particular, there are no non-equilibrium periodic, quasiperiodic, or other recurrent long-time states for this two-stage reproductive kernel.

More precisely, define
\[
\beta_1(a)=r_1e^{M(a)-r_1a},\qquad
X(t)=\int_0^\infty\beta_1(a)u(t,a)\,da,
\qquad
Y(t)=\int_0^\infty\beta(a)u(t,a)\,da.
\]
Then \((X,Y)\) obeys the exact planar system
\[
\boxed{
X'=r_1\bigl(f(Y)-X\bigr),\qquad
Y'=r_2(X-Y).
}
\]
Consequently the basin of \(\bar\varphi_j\) is exactly the inverse image, under
\[
u_0\mapsto \left(\int\beta_1u_0,\int\beta u_0\right),
\]
of the basin of \((\kappa_j,\kappa_j)\) for this planar system. The data converging to the intermediate equilibrium \(\bar\varphi_1\) are exactly the inverse image of the stable manifold \(W^s(\kappa_1,\kappa_1)\).

For every monotone one-parameter family \(\{u_\lambda\}_{\lambda\ge0}\) satisfying Assumption 1.2 of Griette--Herrera, either every solution goes extinct, or there is a unique threshold parameter \(\lambda^*>0\) such that
\[
 u^\lambda(t,\cdot)\to
 \begin{cases}
 0,&\lambda<\lambda^*,\\
 \bar\varphi_1,&\lambda=\lambda^*,\\
 \bar\varphi_2,&\lambda>\lambda^*,
 \end{cases}
 \qquad\text{in }L^1(0,\infty).
\]
Thus, for this noncompact two-stage class, the threshold solution has a completely determined asymptotic state: it converges to the unstable intermediate equilibrium rather than displaying persistent oscillation.

## Proof

### 1. Exact two-stage reduction

Set
\[
K_1(a)=r_1e^{-r_1a},\qquad
K_2(a)=K(a).
\]
These kernels satisfy
\[
K_1(0)=r_1,\qquad K_1'=-r_1K_1,
\]
\[
K_2(0)=0,\qquad K_2'=r_2(K_1-K_2).
\]
Since \(\beta_j=e^M K_j\), one has a.e.
\[
\beta_1'-\mu\beta_1=-r_1\beta_1,
\qquad
\beta'-\mu\beta=r_2(\beta_1-\beta).
\]
Testing the transport equation against these bounded Lipschitz weights, using the boundary value \(u(t,0)=f(Y(t))\), gives
\[
X'=r_1f(Y)-r_1X,
\]
\[
Y'=r_2X-r_2Y.
\]
The same identities follow directly from the characteristic formula, so they hold for the mild solutions considered in the source paper.

The condition \(r_1>\|\mu\|_\infty\) implies
\[
e^{M(a)}e^{-r_1a}\le e^{-(r_1-\|\mu\|_\infty)a},
\]
and hence both \(\beta_1\) and \(\beta\) are bounded. Positivity and normalization follow from the hypoexponential density \(K\).

### 2. A strict mechanical energy

Eliminating \(X\) via \(X=Y+Y'/r_2\) yields
\[
\boxed{
Y''+(r_1+r_2)Y'=r_1r_2\bigl(f(Y)-Y\bigr).
}
\]
Define
\[
V(Y)=r_1r_2\int_0^Y(s-f(s))\,ds,
\qquad
E(Y,Y')=\frac12(Y')^2+V(Y).
\]
Then
\[
\boxed{
\frac{dE}{dt}=-(r_1+r_2)(Y')^2\le0.
}
\]
The assumption \(\limsup_{y\to\infty}f(y)/y<1\) implies \(V(y)\to+\infty\). Thus each trajectory in the positive quadrant is precompact. The largest invariant subset of \(\{E'=0\}\) is obtained from \(Y'=0\) and then \(f(Y)=Y\), hence it consists only of
\[
(0,0),\quad(\kappa_1,\kappa_1),\quad(\kappa_2,\kappa_2).
\]
LaSalle's invariance principle therefore implies convergence of every planar trajectory to one of these three equilibria.

The Jacobian at \((\kappa,\kappa)\) is
\[
J_\kappa=\begin{pmatrix}
-r_1&r_1f'(\kappa)\\
r_2&-r_2
\end{pmatrix},
\]
with characteristic polynomial
\[
\lambda^2+(r_1+r_2)\lambda+r_1r_2(1-f'(\kappa)).
\]
Hence \((0,0)\) and \((\kappa_2,\kappa_2)\) are hyperbolic sinks, whereas \((\kappa_1,\kappa_1)\) is a hyperbolic saddle.

### 3. Lifting planar convergence to the age distribution

Let \(b(t)=f(Y(t))\). The characteristic formula is
\[
u(t,a)=
\begin{cases}
 e^{-M(a)}b(t-a),&0<a<t,\\
 e^{-[M(a)-M(a-t)]}u_0(a-t),&a\ge t.
\end{cases}
\]
If \((X(t),Y(t))\to(\kappa,\kappa)\), then \(b(t)\to\kappa\). Since \(\mu\ge\underline\mu>0\),
\[
\begin{aligned}
\|u(t,\cdot)-\kappa e^{-M}\|_1
&\le e^{-\underline\mu t}\|u_0\|_1
+\frac{\kappa}{\underline\mu}e^{-\underline\mu t}\\
&\quad+\int_0^t e^{-\underline\mu a}|b(t-a)-\kappa|\,da.
\end{aligned}
\]
The last convolution tends to zero because \(b\) is bounded and converges to \(\kappa\). Therefore \(u(t,\cdot)\to\bar\varphi_\kappa\) in \(L^1\). Hyperbolicity of the planar equilibria also gives exponential convergence once the orbit is sufficiently close to its limit, and the same characteristic estimate transfers an exponential rate (possibly reduced by \(\underline\mu\)) to the PDE.

### 4. The threshold set and its unique intersection with monotone families

The planar vector field is strongly cooperative on the interior because both off-diagonal derivatives are positive:
\[
\partial_Y X'=r_1f'(Y)>0,
\qquad
\partial_XY'=r_2>0.
\]
At the saddle \((\kappa_1,\kappa_1)\), the stable eigenvalue has an eigenvector with components of opposite sign. Hence the local stable manifold is unordered. The global stable manifold is unordered as well: if two distinct ordered points lay in it, strong monotonicity would make their forward images strictly ordered; sufficiently far forward both images would lie in the local stable manifold, contradicting its unorderedness.

Because every planar orbit converges to one of the three equilibria, the set of initial moments producing the intermediate equilibrium is exactly \(W^s(\kappa_1,\kappa_1)\), while the complementary points belong to the two sink basins.

For a family satisfying Assumption 1.2, positivity of \(\beta_1\) and \(\beta\) on \((0,\infty)\) makes
\[
\lambda\mapsto (X_\lambda(0),Y_\lambda(0))
\]
continuous and strictly increasing in both coordinates. Such a curve meets the unordered stable manifold at most once. If the family is not entirely in the extinction basin, continuity together with the two open sink basins forces exactly one intersection. Order preservation then places all smaller parameters in the extinction basin and all larger parameters in the upper basin. The threshold point lies on \(W^s\), so its PDE trajectory converges to \(\bar\varphi_1\).

## Relation to prior work and originality boundary

Griette--Herrera (2026) proved a unique sharp threshold for compactly supported fertility and for a particular noncompact eventually-constant class, but explicitly left the asymptotic behavior of the threshold solution open; they note that persistent oscillatory or periodic behavior can occur in related age-structured models. Their noncompact theorem assumes both fertility and mortality become positive constants for large age. The fertility above instead has infinite support and decays exponentially after survival compensation, so it lies outside that class.

Finite-dimensional representations of structured-population and distributed-delay models through gamma/Erlang or more general phase-type kernels are classical. Gurtin--MacCamy already gave special finite-dimensional reductions, and later linear-chain work systematized them. No originality is claimed for the linear-chain mechanism, for hypoexponential kernels, or for planar LaSalle theory by themselves. The source-specific contribution claimed here is the combination yielding a complete global classification for the 2026 bistable boundary-feedback model: the two-stage noncompact class has an exact damped-gradient reduction, every PDE solution converges to an equilibrium, the full threshold set is the moment-preimage of a planar stable manifold, and every nontrivial sharp threshold solution in a monotone family converges to the intermediate equilibrium.

A highly relevant older paper by Gurtin--MacCamy (1979) gives finite-dimensional reductions and rules out periodic solutions in many cases, but the accessible abstract and indexed text describe a different density-dependent formulation in which mortality and maternity depend on total population. Its full text was not independently inspected here, so it remains the main residual originality risk. Modern surveys and finite-dimensional representation papers confirm that the reduction technology itself is classical; no located source was found to state the bistable threshold theorem above for the Griette--Herrera boundary nonlinearity.

## Limitations

- The theorem is for the explicit two-stage hypoexponential survival-weighted reproductive kernel \(K=\beta e^{-M}\), including Erlang-2 as the equal-rate limit. It does not settle general noncompact fertility rates.
- The sufficient condition \(r_1>\|\mu\|_\infty\) is used only to ensure the constructed fertility rate is bounded; more general mortality/rate combinations are admissible whenever \(e^M K\in L^\infty\).
- The result determines the global asymptotic state but does not give a closed-form equation for the stable-manifold separatrix or the threshold parameter \(\lambda^*\).
- Higher-stage phase-type kernels lead to higher-dimensional systems and need not inherit this scalar damped-gradient reduction; no claim is made for them.

## References

1. Q. Griette and F. Herrera, *Sharp Threshold Dynamics for a Bistable Age-Structured Population Model*, Journal of Dynamics and Differential Equations (2026), DOI: 10.1007/s10884-026-10527-w. https://doi.org/10.1007/s10884-026-10527-w
2. M. Gyllenberg, *Mathematical aspects of physiologically structured populations: the contributions of J. A. J. Metz*, Journal of Biological Dynamics (2007), DOI: 10.1080/17513750601032737. https://doi.org/10.1080/17513750601032737
3. J. A. J. Metz and O. Diekmann, *Exact finite-dimensional representations of models for physiologically structured populations. I. The abstract foundations of linear chain trickery*, in Differential Equations with Applications in Biology, Physics and Engineering, Lecture Notes in Pure and Applied Mathematics 133 (1991), 269--289. https://ir.cwi.nl/pub/1559
4. O. Diekmann, M. Gyllenberg, and J. A. J. Metz, *Finite dimensional state representation of physiologically structured populations*, Journal of Mathematical Biology 80 (2020), 205--273, DOI: 10.1007/s00285-019-01454-0. https://doi.org/10.1007/s00285-019-01454-0
5. M. E. Gurtin and R. C. MacCamy, *Some simple models for nonlinear age-dependent population dynamics*, Mathematical Biosciences 43 (1979), 199--211, DOI: 10.1016/0025-5564(79)90049-X. https://doi.org/10.1016/0025-5564(79)90049-X
