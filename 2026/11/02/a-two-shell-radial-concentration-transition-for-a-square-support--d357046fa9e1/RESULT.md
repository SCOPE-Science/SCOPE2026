# A two-shell radial concentration transition for a square-supported run-and-tumble particle

## Finding
For the stationary two-dimensional, four-direction harmonic run-and-tumble particle, there is an exact **two-shell threshold** at \(\beta=\gamma/\mu=1/2\). Whenever \(0<\beta<1/2\), the radial probability density has an integrable infinite peak at the inscribed circle \(\rho=1\), a unique strict interior minimum, and a second integrable infinite peak at the outer support circle \(\rho=\sqrt2\). For \(\beta\ge1/2\), the density decreases strictly on the entire outer interval \(1<\rho<\sqrt2\). At equality, the inscribed-circle singularity is logarithmic while the outer-end density has the finite positive limit \(2\sqrt2/\pi\).

## Assumptions and scope
The athermal overdamped model is \(\dot{\boldsymbol r}=-\mu\boldsymbol r+\sqrt2 v_0\boldsymbol\sigma\), with \(\mu>0\), \(v_0>0\), four orientations \(\boldsymbol\sigma\in\{\pm\boldsymbol e_x,\pm\boldsymbol e_y\}\), and each permissible clockwise or anticlockwise quarter-turn occurring at rate \(\gamma>0\). This is the precise four-state Markov chain of Smith, Le Doussal, Majumdar and Schehr (2022), not uniform angular redraws. Write \(L=v_0/\mu\), \(\beta=\gamma/\mu\), and \(\rho=|\boldsymbol r|/L\). Let \(p_\beta\) denote the probability density of this *radial random variable*, not the planar density per unit area. The rotated normalized Cartesian coordinates \(U=(x+y)/(\sqrt2L)\), \(V=(x-y)/(\sqrt2L)\) are independent and identically distributed with \(f_\beta(z)=(1-z^2)^{\beta-1}/B(1/2,\beta)\) for \(|z|<1\). Hence \(S=\rho^2=U^2+V^2\) is a sum of two independent \(\mathrm{Beta}(1/2,\beta)\) variables, with support \((0,2)\).

The full classification proved here concerns \(0<\beta\le1\) on both radial subintervals and all \(\beta>0\) on the outer subinterval. No assertion is made concerning all critical points for \(\beta>1\) inside \(0<\rho<1\).

## Proof
Write \(C_\beta=B(1/2,\beta)^{-2}\), and \(g_\beta\) for the density of \(S\). Convolution of the two squared-coordinate beta densities gives, for \(0<s<1\),
\[
 g_\beta(s)=C_\beta\int_0^1 \frac{[(1-sz)(1-s(1-z))]^{\beta-1}}{\sqrt{z(1-z)}}\,dz,\qquad p_\beta(\rho)=2\rho g_\beta(\rho^2).
\]
For \(0<\beta<1\), each factor inside the power is positive and decreasing in \(s\), and the exponent \(\beta-1\) is negative: the integrand strictly increases with \(s\). At \(\beta=1\) it is independent of \(s\). The positive radial Jacobian \(2\rho\) therefore makes \(p_\beta\) strictly increasing throughout \(0<\rho<1\) for all \(0<\beta\le1\).

For \(1<s<2\), put \(t=2-s\in(0,1)\), \(w=t/(2-t)\), and
\[
 H_\beta(w)={}_2F_1(\tfrac12,\tfrac12;\beta+\tfrac12;w^2)
 =\sum_{n=0}^\infty \frac{(1/2)_n^2}{(\beta+1/2)_n\,n!}w^{2n}.
\]
Changing convolution variables to the two deficits from the upper beta endpoints and then centering the beta integral yields the exact identity
\[
 p_\beta(\sqrt{2-t})=
 \frac{4B(\beta,\beta)}{B(1/2,\beta)^2}\,
 \frac{t^{2\beta-1}}{\sqrt{2-t}}H_\beta\!\left(\frac{t}{2-t}\right).
 \tag{1}
\]
Indeed, the centered deficit has a \(\mathrm{Beta}(\beta,\beta)\) law, and its even centered moments are \((1/2)_n/(\beta+1/2)_n\), which produces the coefficients in \(H_\beta\). In particular, the power-series coefficients are strictly positive for every \(\beta>0\).

Define \(Q_\beta(w)=wH_\beta'(w)/H_\beta(w)\). Its value is the mean of the nonnegative even integer \(2n\) under weights proportional to the positive terms \(a_n w^{2n}\). Differentiating with respect to \(\log w\) gives precisely \(\operatorname{Var}_w(2n)>0\) for \(0<w<1\). Thus \(Q_\beta\) is positive and strictly increasing. Logarithmically differentiating (1) gives
\[
 \eta_\beta(t):=t\frac{d}{dt}\log p_\beta(\sqrt{2-t})
 =2\beta-1+\frac{t}{2(2-t)}+\frac{2}{2-t}Q_\beta\!\left(\frac{t}{2-t}\right).
 \tag{2}
\]
Every nonconstant term in (2) strictly increases with \(t\in(0,1)\), so \(\eta_\beta\) is strictly increasing. Its limit at \(t\downarrow0\) is \(2\beta-1\). When \(0<\beta<1/2\), the hypergeometric exponent \((\beta+1/2)-(1/2)-(1/2)=\beta-1/2\) is negative, so as \(w\uparrow1\) the positive function \(H_\beta\) diverges as \((1-w^2)^{\beta-1/2}\). Consequently \(Q_\beta(w)\to+\infty\), and \(\eta_\beta(t)\to+\infty\) as \(t\uparrow1\). Exactly one root \(t_\beta\in(0,1)\) therefore exists. Since \(t=2-\rho^2\) decreases when \(\rho\) grows, the sign of \(d p_\beta/d\rho\) is opposite to the sign of \(\eta_\beta\): the root corresponds to precisely one strict radial minimum, \(\rho_*(\beta)=\sqrt{2-t_\beta}\). When \(\beta\ge1/2\), equation (2) is strictly positive throughout \((0,1)\), so the radial density decreases strictly throughout \((1,\sqrt2)\).

The leading singular constants are independently obtained by scaling the beta convolution near its corners. Put \(b_\beta=B(1/2,\beta)\). If \(0<\beta<1/2\), then
\[
 p_\beta(\rho)\sim
 \begin{cases}
 \dfrac{4B(1/2,1/2-\beta)}{b_\beta^2}(1-\rho^2)^{\beta-1/2},&\rho\uparrow1,\\
 \dfrac{4B(\beta,1/2-\beta)}{b_\beta^2}(\rho^2-1)^{\beta-1/2},&\rho\downarrow1,\\
 \dfrac{2\sqrt2 B(\beta,\beta)}{b_\beta^2}(2-\rho^2)^{2\beta-1},&\rho\uparrow\sqrt2.
 \end{cases}
 \tag{3}
\]
Both singular exponents exceed \(-1\), so they are integrable with respect to \(d\rho\). At \(\beta=1/2\), each side of \(\rho=1\) has \(p_{1/2}(\rho)\sim(4/\pi^2)\log[1/|1-\rho^2|]\), while (1) gives \(p_{1/2}(\sqrt2-)=2\sqrt2/\pi\). For \(\beta>1/2\) the inscribed-circle density has finite value \(2B(\beta-1/2,\beta-1/2)/b_\beta^2\). Finally, expanding (2) for small \(t\) near \(\beta=1/2\), with \(Q_\beta(w)=O(w^2)\), yields \(t_\beta=4(1-2\beta)+O((1-2\beta)^2)\). This completes the sharp classification claimed.

## Verification
The standalone file `CHECK.py` computes the radial density in two algebraically independent representations: direct convolution with high-order endpoint-aware numerical quadrature, and the exterior hypergeometric representation (1). It checks their numerical agreement, normalization consistency, monotonic logarithmic derivatives, valley roots, and critical scaling for multiple noninteger and threshold-near parameter choices. The program reports `PASS: 120 direct-convolution, root, monotonicity and critical-scaling checks` in the source package. These finite computations test the analytic formulas but are not a substitute for the positive-coefficient variance proof or the endpoint asymptotics.

For illustration, at \(\beta=1/4\), the unique minimum is at \(t_\beta\approx0.6353250926701733\), or \(\rho_*(\beta)\approx1.168193009450847\). It lies between the singular circles \(1\) and \(\sqrt2\).

## Relationship to prior work
Smith, Le Doussal, Majumdar and Schehr (2022) derive the independent rotated-coordinate beta laws and the exact **two-dimensional stationary density** used here. They also analyze the angular marginal and shape change in the planar density; these facts are prior results and are not claimed as new. The additional theorem concerns the **radial** distribution, the two different geometric singular shells, and the *uniqueness* of their separating minimum using positive-coefficient hypergeometric monotonicity. Guéneau, Majumdar and Schehr (2026) determine the radial law for **uniformly redrawn isotropic orientations**, whose circularly symmetric support has a single turning radius. That orientation process is not the four-discrete-state quarter-turn process with square support treated here. No equivalent double-shell classification was identified in the examined relevant publications or mathematical research records; this is a qualified same mathematical model literature assessment, not an independently certified priority claim.

## Limitations
The result is a statement about the stationary **radial probability density** of an athermal, noninteracting, four-orientation particle in an isotropic harmonic trap; it is not a dynamical phase transition. There is no claim about arbitrary orientation distributions, thermal diffusion, interactions, anisotropic traps, or the complete mode count below the inscribed circle when \(\beta>1\). Independently established publication priority and independent validation have not been performed. A generic older paper not exposed by the targeted literature comparisons could imply the same radial facts; this remains a residual risk.

## References
Smith, N. R., Le Doussal, P., Majumdar, S. N., and Schehr, G., “Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions,” arXiv:2207.10445v1 (first publicly available 2022-07-21), revised arXiv:2207.10445v2 (2022-11-16); *Physical Review E* 106, 054133 (2022). https://arxiv.org/abs/2207.10445 ; full lawful text https://arxiv.org/html/2207.10445v2.

Guéneau, M., Majumdar, S. N., and Schehr, G., “Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential,” arXiv:2602.08436v1 (2026-02-09), revised arXiv:2602.08436v2 (2026-07-02). https://arxiv.org/html/2602.08436v2. (Contrasting isotropic orientation-redraw process.)
