# A sharp outer-wall slowdown layer in active-Brownian annular escape

## Finding
Consider a planar active Brownian particle with translational diffusivity \(D>0\), rotational diffusivity \(D_{\mathrm{rot}}>0\), and signed propulsion speed \(v\), killed upon reaching either circle bounding a concentric annulus of radii \(\alpha R\) and \(R\), with arbitrary fixed \(0<\alpha<1\). Its initial propulsion angle is uniform and independent of its starting position. Set
\[
 s=|X_0|/R,\qquad \beta=D_{\mathrm{rot}}R^2/D,\qquad p=vR/D,\qquad L=\log(1/\alpha),\qquad c=(1-\alpha^2)/(4L).
\]
The normalized orientation-averaged mean exit time has the even weak-propulsion expansion
\[
 \frac D{R^2}\mathbb E_{s,\mathrm{uniform}}\tau
 =U_0(s)+p^2 B_\beta(s)+O_{\alpha,\beta,s}(p^4),\qquad
 U_0(s)=\frac{1-s^2}{4}+c\log s.
\]
Define \(h(s)=c/s-s/2\), \(S=h(\alpha)+h(1)\), and
\[
 y_*(\alpha)=-\frac{2S}{Lh(1)}>0.
\]
Then the following is a sharp, parameter-global statement in \(\alpha\), in the fast-rotation limit \(\beta\to\infty\):
\[
 \lim_{\beta\to\infty}\beta^{5/2} B_\beta(1-y/\beta)
 =\frac{Sy}{2L}+\frac{h(1)y^2}{4}
 \quad\text{for every fixed }y\ge0,
\]
with convergence of one derivative in \(y\) locally. Consequently, for every \(0<\alpha<1\) and all sufficiently large \(\beta\), the weak-activity correction is **strictly positive immediately inside the outer absorbing boundary**, but strictly negative immediately inside the inner absorbing boundary and at every fixed interior radius. There is a local sign-changing zero
\[
 s_\beta=1-\frac{y_*(\alpha)+o(1)}{\beta}.
\]
The positive susceptibility layer has sharp radial width of order \(\beta^{-1}\), thinner than the order-\(\beta^{-1/2}\) angular resolvent boundary layer. No global uniqueness of other zeros is asserted.

## Assumptions and scope
The stochastic dynamics is \(dX_t=v(\cos\theta_t,\sin\theta_t)\,dt+\sqrt{2D}\,dW_t\) and \(d\theta_t=\sqrt{2D_{\mathrm{rot}}}\,dB_t\), with independent Brownian motions, starting strictly inside the open annulus and absorbed on its two circular components. The initial heading is uniform. All limits in \(\beta\) refer to the coefficient \(B_\beta\) obtained by differentiating at \(p=0\); they are **not** a joint limit at fixed nonzero propulsion. The annulus ratio \(\alpha\) remains fixed strictly between zero and one.

## Proof
**1. Backward equation and weak-activity coefficients.** Rotation invariance reduces the dimensionless backward generator, using the heading angle \(\phi\) relative to the radial direction, to
\[
 \mathcal L_p=\partial_s^2+s^{-1}\partial_s+(s^{-2}+\beta)\partial_\phi^2
 +p\bigl(\cos\phi\,\partial_s-s^{-1}\sin\phi\,\partial_\phi\bigr).
\]
The exit-time function solves \(\mathcal L_p T_p=-1\) with zero Dirichlet data at \(s=\alpha,1\) and angular periodicity. Uniform ellipticity for fixed \(\beta>0\), positive translational diffusion, and invertibility of the killed generator give an analytic solution in sufficiently small \(p\). Reversing propulsion is equivalent to shifting \(\phi\) by \(\pi\); the uniform-heading mean is therefore even. The zeroth coefficient is the stated \(U_0\), whose derivative is \(h\).

Write \(T_p=U_0+pA(s)\cos\phi+p^2T_2+\cdots\). The first-order equation reads
\[
 H_\beta A=h,\qquad H_\beta=-\partial_s^2-s^{-1}\partial_s+s^{-2}+\beta,
 \qquad A(\alpha)=A(1)=0.
\]
Let \(B_\beta(s)=(2\pi)^{-1}\int_0^{2\pi}T_2(s,\phi)\,d\phi\). Averaging the second-order equation yields
\[
 (sB_\beta')'=-\tfrac12(sA)',\qquad B_\beta(\alpha)=B_\beta(1)=0.
\]
Hence the exact identities
\[
 B_\beta'(s)=-\frac{A(s)}2+\frac{C_\beta}{s},\qquad
 C_\beta=\frac1{2L}\int_\alpha^1 A(t)\,dt,
 \qquad B_\beta'(\alpha)=\frac{C_\beta}{\alpha},\quad B_\beta'(1)=C_\beta.
\]

**2. An exact homogeneous-boundary reduction.** The function \(h(s)=c/s-s/2\) satisfies \((H_\beta-\beta)h=0\). For \(\beta>0\), let \(w_\beta\) solve \(H_\beta w_\beta=0\) and match \(w_\beta(\alpha)=h(\alpha)\), \(w_\beta(1)=h(1)\). Uniqueness gives
\[
 A(s)=\frac{h(s)-w_\beta(s)}\beta.
\]
Because \(\int_\alpha^1 h(s)\,ds=U_0(1)-U_0(\alpha)=0\),
\[
 C_\beta=-\frac1{2L\beta}\int_\alpha^1 w_\beta(s)\,ds.
\]
This identity is exact, not a formal asymptotic expansion.

**3. The two boundary layers.** Put \(\kappa=\sqrt\beta\). Write \(w_\beta=h(\alpha)q_{\alpha,\kappa}+h(1)q_{1,\kappa}\), where \(q_{\alpha,\kappa}\) and \(q_{1,\kappa}\) solve the homogeneous radial equation and interpolate respectively the boundary values \((1,0)\) and \((0,1)\). Both are explicitly ratios of combinations of \(I_1(\kappa s)\) and \(K_1(\kappa s)\). Their large-positive-argument expansions give
\[
 \int_\alpha^1q_{\alpha,\kappa}(s)\,ds=\kappa^{-1}+O_\alpha(\kappa^{-2}),\qquad
 \int_\alpha^1q_{1,\kappa}(s)\,ds=\kappa^{-1}+O_\alpha(\kappa^{-2}),
\]
\[
 q_{1,\kappa}'(1)=\kappa+O_\alpha(1),\qquad
 q_{\alpha,\kappa}'(1)=O_\alpha(\kappa e^{-\kappa(1-\alpha)}).
\]
The estimates also follow directly from the standard boundary-layer forms \(q_{\alpha,\kappa}(\alpha+z/\kappa)\to e^{-z}\) and \(q_{1,\kappa}(1-z/\kappa)\to e^{-z}\), with exponentially decaying bounds, plus their differentiated Bessel representations.

**4. Strict sign and exact scale.** Let \(\alpha=e^{-t}\) for \(t>0\). Directly,
\[
 S=(1+\alpha)\frac{\sinh t-t}{2t}>0,
 \qquad h(1)=c-\frac12<0.
\]
The first inequality uses \(\sinh t>t\); the second uses \(1-e^{-2t}<2t\). By step 3,
\[
 C_\beta=-\frac{S}{2L}\beta^{-3/2}+O_\alpha(\beta^{-2}),
 \qquad A'(1)=-h(1)\beta^{-1/2}+O_\alpha(\beta^{-1}).
\]
Differentiating the exact relation for \(B_\beta'\) at the outer boundary, and using \(A(1)=0\), gives
\[
 B_\beta''(1)=-C_\beta-\frac{A'(1)}2
 =\frac{h(1)}2\beta^{-1/2}+O_\alpha(\beta^{-1}).
\]
On the shrinking strip \(1-y/\beta\le s\le1\) with \(y\) in any compact subset of \([0,\infty)\), the differentiated Bessel formulas bound \(B_\beta'''(s)\) uniformly. Taylor's theorem at \(s=1\), multiplied by \(\beta^{5/2}\), proves the displayed quadratic layer profile with locally uniform first-derivative convergence. The quadratic has the simple positive zero \(y_*=-2S/(Lh(1))\), and is strictly positive for \(0<y<y_*\) and strictly negative for \(y>y_*\). Uniform convergence and the nonzero derivative at \(y_*\) yield a nearby locally unique zero \(y_\beta=y_*+o(1)\).

At both physical boundaries, \(B_\beta'(\alpha)=C_\beta/\alpha<0\) and \(B_\beta'(1)=C_\beta<0\) for all sufficiently large \(\beta\). Thus the coefficient is negative just inside the inner boundary but positive just inside the outer boundary. Finally \(\beta A(s)\to h(s)\) for each fixed interior \(s\) and the integrated identity for \(B_\beta'\) gives \(\beta B_\beta(s)\to -U_0(s)/2<0\) at every such \(s\). The theorem follows.

## Verification
The included standalone `verify.py` independently solves the coupled radial boundary-value equations numerically and compares them against explicit modified-Bessel integral formulas. It also checks boundary signs, coefficients and the scaled sharp outer-wall profile for several annulus ratios and rotational diffusivities. In the supplied execution, all **171** finite diagnostic assertions passed. The infinite-parameter assertions and analytic boundary-layer limit follow from the proof, not from finite testing. Run with `python verify.py` in an environment with `numpy`, `scipy`, and `mpmath` installed.

## Relationship to prior work
Di Trapani, Franosch and Caraglio (2023) analyze an active Brownian particle inside a completely absorbing **disk**, giving a full propagator and first-passage distribution, but not the annular two-boundary coefficient or its rotational boundary layer. Iyaniwura and Peng (2025) derive the backward mean-first-passage equation in disks and annuli, compute first-order weak-activity corrections and explain why uniform-heading averages first change at second order. The present result starts exactly at that second order, determines its two opposite wall signs, and proves a sharp \(\beta^{-1}\) positive-layer scale and a limiting crossover profile. The standard Bessel large-argument expansions are credited to the NIST Digital Library of Mathematical Functions. A full propagator or first-order solution could implicitly permit deriving these statements, but does not by itself establish their signs and sharp scale.

## Limitations
The expansion concerns sufficiently weak propulsion for each fixed value of \(\beta\). The high-rotation asymptotics apply to its quadratic coefficient; no fixed-nonzero-speed joint-limit claim is made. The positive outer-wall correction becomes small, of order \(\beta^{-5/2}\) within its scaled skin, so the theorem is not a prediction of an experimentally large slowdown. The annulus is concentric, both boundary components are perfectly absorbing, the initial heading is uniform, and translational diffusion is strictly positive. The local sign-changing zero is established asymptotically; global uniqueness of zeros and nonperturbative propulsion-speed behavior remain unproved. Publication priority beyond the material compared here requires independent review.

## References
- Francesco Di Trapani, Thomas Franosch, Michele Caraglio, *Active Brownian Particles in a Circular Disk with an Absorbing Boundary*, arXiv:2306.12702v1 (first public 2023-06-22), https://arxiv.org/html/2306.12702v1 .
- Sarafa A. Iyaniwura, Zhiwei Peng, *Mean first passage time of active Brownian particles in two dimensions*, arXiv:2506.15813v1 (2025), https://arxiv.org/html/2506.15813v1 .
- NIST Digital Library of Mathematical Functions, §10.40, *Asymptotic Expansions for Large Argument*, https://dlmf.nist.gov/10.40 .
