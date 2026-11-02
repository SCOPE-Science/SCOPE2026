# Sharp speed-relative residual gain for front-pinned ignition profiles

## Finding

For every integer \(q\geq2\), let
\[
\Theta_q(y)=\log\frac{y}{1-y}-\sum_{j=1}^{q-1}\frac1{j y^j},\quad
 a_q=\frac{q-1}{q},\quad G_q(y)=y^{q-1}(1-y),\qquad 0<y<1.
\]
Consider the entire ignition orbit \(\dot y=y^q(1-y)\), with \(\dot{}\) denoting the unscaled time derivative, and its logarithmic state \(v=\log y\). Pin it at the unique time \(t_*\) for which \(y(t_*)=a_q\). Let \(\mathcal L_q\) send a bounded measurable speed-relative forcing \(\varepsilon\) to the solution of the continuous **linearized pinned** problem
\[
\dot w=F_q'(v(t))w+G_q(y(t))\varepsilon(t),\quad
w(t_*)=0,\qquad F_q(v)=e^{(q-1)v}-e^{qv}.
\]
Then \(\mathcal L_q:L^\infty(\mathbb R)\to L^\infty(\mathbb R)\) has the **sharp**, finite norm
\[
\boxed{\|\mathcal L_q\|=B_q=\frac{1-y_q}{q-1-qy_q},}
\]
where \(y_q\) is the **unique** point in \((0,a_q)\) satisfying
\[
\boxed{\Theta_q(a_q)-\Theta_q(y_q)
=\frac1{y_q^{q-1}(q-1-qy_q)}.}
\]
The unique point of maximum absolute response to \(\varepsilon\equiv1\) occurs strictly *before* the speed-maximizing pin. The bound holds on any finite subinterval containing the pin and is attained whenever that interval also contains \(y_q\) along the orbit.

For large reaction order, the locations and gains obey the nontrivial universal law
\[
\boxed{q(1-y_q)\longrightarrow z_*=4.300640970392\ldots,\qquad
qB_q\longrightarrow\frac{z_*}{z_*-1}=1.302971455838\ldots,}
\]
where \(z_*>1\) is the unique root of
\[
\int_1^{z_*}\frac{e^u}{u}\,\mathrm du=\frac{e^{z_*}}{z_*-1}.
\]
For example, \(y_2=0.01679841497\ldots\), \(B_2=1.01738240881\ldots\), whereas \(y_3=0.15082073841\ldots\) and \(B_3=0.54872925879\ldots\). Every \(B_q\) strictly exceeds \(1/(q-1)\).

## Assumptions and scope

The orbit is the increasing heteroclinic \(y:\mathbb R\to(0,1)\), so the pin exists uniquely. Forcing is measured by \(\|\varepsilon\|_\infty=\|r/G_q(y)\|_\infty\), not by the unweighted \(\|r\|_\infty\). The statement concerns the exact continuous linearization with a fixed pin value, not a nonlinear residual-to-error bound. On a finite interval, take the restriction of this orbit with the same pinned condition; the sharp constant is attained only if the restricted interval includes the global worst-response state \(y_q\).

## Proof

**1. Exact time and propagator.** Direct differentiation gives
\(\Theta_q'(y)=1/[y^q(1-y)]\), so \(t-t_*=\Theta_q(y(t))-\Theta_q(a_q)\). Moreover \(\dot v=G_q(y)\), and differentiating its equation shows that \(G_q(y(t))\) is a nonzero homogeneous solution of the linearized equation. Variation of constants therefore gives, for every bounded measurable \(\varepsilon\),
\[
w(t)=G_q(y(t))\int_{t_*}^t\varepsilon(s)\,\mathrm ds.
\]
Consequently the exact forcing-to-response norm is
\[
\|\mathcal L_q\|=
\sup_{0<y<1}G_q(y)\,|\Theta_q(y)-\Theta_q(a_q)|,
\]
where equality follows with \(\varepsilon\equiv1\). Boundedness follows from the endpoint estimates below.

**2. Unique left-hand maximum.** On \(0<y<a_q\), define
\[
H_-(y)=G_q(y)[\Theta_q(a_q)-\Theta_q(y)],\quad
D_-(y)=\frac1{y^{q-1}(q-1-qy)}-[\Theta_q(a_q)-\Theta_q(y)].
\]
Since \(G_q'(y)=y^{q-2}(q-1-qy)>0\) on this interval and \(G_q(y)\Theta_q'(y)=1/y\), differentiation yields
\[
H_-'(y)=-G_q'(y)D_-(y),\qquad
\boxed{D_-'(y)=\frac{y^{1-q}}{(1-y)(q-1-qy)^2}>0.}
\]
The derivative of \(D_-\) has a nonintegrable positive singularity as \(y\downarrow0\) for all \(q\ge2\), so \(D_-(y)\to-\infty\) there; as \(y\uparrow a_q\), the first term of \(D_-\) diverges to \(+\infty\), while its second tends to zero. Thus exactly one root \(y_q\) exists, \(H_-\) strictly increases before it and strictly decreases afterwards. At its maximum, the defining root equation gives
\[
H_-(y_q)=\frac{G_q(y_q)}{y_q^{q-1}(q-1-qy_q)}
=\frac{1-y_q}{q-1-qy_q}.
\]
Integration of \(\Theta_q'\) at the lower endpoint shows
\(\lim_{y\downarrow0}H_-(y)=1/(q-1)\), and the strict increase near zero shows \(B_q>1/(q-1)\).

**3. Right-hand branch cannot win.** On \(a_q<y<1\), the velocity \(G_q\) decreases. Hence
\[
\begin{aligned}
H_+(y)&=G_q(y)[\Theta_q(y)-\Theta_q(a_q)]\\
&=\int_{a_q}^y\frac{G_q(y)}{tG_q(t)}\,\mathrm dt
\le \int_{a_q}^y\frac{\mathrm dt}{t}
\le\log\frac q{q-1}<\frac1{q-1}<B_q.
\end{aligned}
\]
Therefore the *global* absolute-response maximum is unique at \(y_q\), and it is attained with constant signed forcing, proving sharpness.

**4. Large-order universality.** Define \(z_q=q(1-y_q)>1\). Substituting \(y=1-z/q\) in the root equation gives
\[
\frac{(1-z_q/q)^{-(q-1)}}{z_q-1}
=\int_1^{z_q}\frac{(1-u/q)^{-q}}u\,\mathrm du.
\]
For any fixed \(z>1\), the left-minus-right difference tends as \(q\to\infty\) to
\[
E(z)=\frac{e^z}{z-1}-\int_1^z\frac{e^u}{u}\,\mathrm du,
\qquad E'(z)=-\frac{e^z}{z(z-1)^2}<0.
\]
Also \(E(z)\to+\infty\) as \(z\downarrow1\) and \(E(z)\to-\infty\) as \(z\to\infty\) (the integral of \(-E'\) diverges). Thus \(E\) has a unique root \(z_*\). For every pair \(1<z_1<z_*<z_2\), the finite-order difference has opposite signs at \(z_1,z_2\) for all sufficiently large \(q\). The already-proved uniqueness of \(y_q\) traps \(z_q\) between these two points, proving \(z_q\to z_*\). Finally the exact formula for \(B_q\) becomes \(qB_q=z_q/(z_q-1)\), which gives the limit.

**5. Why the residual weighting matters.** For the unweighted forcing \(r\equiv1\) on the finite ignition interval starting at \(y(0)=\delta\) and reaching the pin, the magnitude of the response at the left endpoint is exactly
\[
G_q(\delta)\int_\delta^{a_q}\frac{\mathrm dy}{y^{2q-1}(1-y)^2}
\sim \frac1{2(q-1)\delta^{q-1}}=\frac1{2\mu},
\qquad\mu=(q-1)\delta^{q-1}.
\]
Thus ordinary uniform forcing need not have a uniform small-layer bound. This last asymptotic is a lower bound on the unweighted inverse norm; it is **not** claimed to be the sharp global unweighted norm.

## Verification

Run `python3 verify.py` with Python 3's standard library. The standalone checker computes the unique roots numerically, reconstructs both formulas for the gain, tests monotonicity/pointwise maximization for eleven orders, checks the exact derivative identity by finite differences, and verifies the limiting root via composite quadrature. It passed **3,139 supplementary tests**. The infinite-dimensional operator norm, uniqueness, and the large-order asymptotic are proved analytically above; finite checks are not substitutes for those proofs.

## Relationship to prior work

Boros (arXiv:2610.27864v1, Proposition 4.1 and Theorem 4.2) derives the speed-ratio propagator for front-pinned ignition and warns that an unweighted residual integral can still grow with the long interval. That propagator is an acknowledged starting ingredient, not claimed new here. The new optimized object is the **exact norm with forcing relative to local orbit speed**, the proof that a unique pre-front state always controls it, and its universal high-reaction-order constant. Earlier Chebyshev mapping and integral-preconditioning literature treats different approximation or matrix-conditioning questions, not this optimized orbit response. A more general unpublished or specialized Green-operator extremum could still subsume the result.

## Limitations

The calculation proves a continuous, one-dimensional **linearized** statement; it does not prove a nonlinear a posteriori bound, an inverse bound for a discrete collocation Jacobian, or uniform stability for unweighted residuals. The forcing normalization uses the exact state-dependent speed \(G_q(y)\), which vanishes toward both equilibria; direct numerical use requires a justified approximate speed and attention to small denominators. No optimality among all possible residual weights or pins is claimed. Historical priority remains subject to independent review.

## References

- I. Boros, *Front-pinned spectral collocation for the flame problem and related ignition problems*, arXiv:2610.27864v1, publicly posted 20 October 2026. https://arxiv.org/html/2610.27864v1
- T. W. Tee and L. N. Trefethen, *A rational spectral collocation method with adaptively transformed Chebyshev grid points*, SIAM J. Sci. Comput. 28 (2006), 1798–1811. https://doi.org/10.1137/050641296
- K. Du, *On well-conditioned spectral collocation and spectral methods by the integral reformulation*, SIAM J. Sci. Comput. 38 (2016), A3247–A3263. https://doi.org/10.1137/15M1046629
