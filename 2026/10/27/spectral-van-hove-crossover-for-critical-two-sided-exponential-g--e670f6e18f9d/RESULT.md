# Spectral van Hove crossover for critical two-sided-exponential Gabor windows

## Finding
For every \(a>0\), let \(g_a(t)=\sqrt a\,e^{-a|t|}\) and let \(S_a\) be its critical unit-square-lattice Gabor frame operator. Under the unitary Zak transform, \(S_a\) is multiplication by \(H_a(x,\omega)=|Zg_a(x,\omega)|^2\). Its normalized spectral measure is the pushforward of unit area on \([0,1)^2\) under \(H_a\), not the ordinary Hilbert-space trace of \(S_a\).

Put \(q=e^{-a}\), \(D(\theta)=1-2q\cos\theta+q^2\), \(h=\sinh(a/2)\), and \(c=\cosh(a/2)\). For \(-\pi\le\theta\le\pi\) define
\[
 L(\theta)=\frac{16aq^2h^2\cos^2(\theta/2)}{D(\theta)^2},\qquad
 E(\theta)=\frac{16aq^2\{h^2\cos^2(\theta/2)+c^2\sin^2(\theta/2)\}}{D(\theta)^2},\qquad
 U(\theta)=L(\theta)+E(\theta)h^2.
\]
The spectral measure is absolutely continuous, supported on \([0,\Lambda_a]\), has mean one, and has density
\[
 \rho_a(s)=\frac1{2\pi a}\int_{-\pi}^{\pi}
 \frac{\mathbf1_{\{L(\theta)<s<U(\theta)\}}}{\sqrt{(s-L(\theta))(s-L(\theta)+E(\theta))}}\,d\theta,\qquad 0<s<\Lambda_a,
\]
for almost every \(s\). The upper endpoint and the only interior saddle and seam-critical values are
\[
 \Lambda_a=a\coth^2(a/2),\quad s_a=a\operatorname{csch}^2(a/2),\quad e_a=a\tanh^2(a/2),\quad \Lambda_a-s_a=a.
\]
In particular, the saddle and seam-critical values change order at the unique parameter
\[
 a_*=2\operatorname{arsinh}\sqrt{\frac{1+\sqrt5}{2}}=2.122550123810071\ldots.
\]
For \(0<a<a_*\), \(e_a<s_a\); for \(a>a_*\), \(s_a<e_a\); and they coincide only at \(a=a_*\).

The sharp endpoint constants are
\[
 \rho_a(0+)=\frac{(1+q)^3}{4a^2q(1-q)},\qquad
 \rho_a(s)\sim K_a\sqrt{\Lambda_a-s}\quad(s\uparrow\Lambda_a),
 \qquad K_a=\frac{1-q}{\pi\sqrt2\,a^{5/2}\coth^2(a/2)\sqrt q}.
\]
At the interior saddle, on either side, including when the saddle and seam values coincide,
\[
 \rho_a(s)=C_a\log\frac1{|s-s_a|}+O_a(1),\qquad
 C_a=\frac1{2\pi a s_a\sqrt{1/4+2q/(1-q)^2}}.
\]
If \(a\ne a_*\), then \(\rho_a\) is finite and continuous at \(e_a\) and has a one-sided square-root cusp. Explicitly, with
\[
 A_a=2a^2\tanh(a/2),\qquad B_a=\frac{2e_aq}{(1+q)^2},\qquad J_a=\frac{2}{\pi A_a\sqrt{B_a}},
\]
one has \(\rho_a(e_a+\varepsilon)=\rho_a(e_a)-J_a\sqrt\varepsilon+O_a(\varepsilon)\) and \(\rho_a(e_a-\varepsilon)=\rho_a(e_a)+O_a(\varepsilon)\) as \(\varepsilon\downarrow0\). Hence the complete spectral singularity pattern changes order at an explicit golden-ratio threshold.

## Assumptions and scope
The lattice translations and modulations are \(T_k f(t)=f(t-k)\) and \(M_mf(t)=e^{2\pi imt}f(t)\), for \(k,m\in\mathbb Z\); the Zak variable is \(\omega\in[0,1)\) and \(\theta=2\pi\omega\) modulo \(2\pi\). The window \(g_a\) has \(\|g_a\|_2=1\). All conclusions hold for every real \(a>0\); they do not concern noncritical lattices. Density asymptotics describe the absolutely continuous pushforward law. They do not assert a trace-class spectral density of \(S_a\) on \(L^2(\mathbb R)\).

## Proof
**1. Exact Zak multiplier and fiber law.** For \(0\le x<1\), geometric summation gives
\[
 Zg_a(x,\omega)=\frac{2\sqrt a\,q}{D(\theta)}\bigl[\sinh(a(1-x))+e^{i\theta}\sinh(ax)\bigr].
\]
Write \(y=|x-1/2|\). The elementary identity
\[
 |\sinh(a(1-x))+e^{i\theta}\sinh(ax)|^2
 =4\{h^2\cosh^2(ay)\cos^2(\theta/2)+c^2\sinh^2(ay)\sin^2(\theta/2)\}
\]
then gives the *affine hyperbolic-fiber identity*
\[
 H_a(x,\omega)=L(\theta)+E(\theta)\sinh^2(ay).
\]
The map \(x\mapsto y\) gives density \(2\) on \([0,1/2]\), and \(s=L+E\sinh^2(ay)\) has derivative \(2a\sqrt{(s-L)(s-L+E)}\). Conditioning on the uniform angle and changing variables proves the integral density and absolute continuity (including no atoms). Since \(\int H_a\,dx\,d\omega=\|g_a\|_2^2=1\), its mean equals one.

**2. Critical levels and support.** Both \(L\) and \(U\) strictly decrease with \(|\theta|\in[0,\pi]\): in the original multiplier representation, for fixed \(x\), its numerator is \(p+r\cos\theta\) with \(p\ge r\ge0\), whereas \(D(\theta)\) strictly decreases as \(\cos\theta\) increases, making the quotient strictly increasing in \(\cos\theta\) (unless \(p=r=0\), impossible away from the Zak zero). Also \(E(\theta)>0\), so the multiplier strictly increases with \(y>0\). Thus the only smooth-cell critical points are \((y,\theta)=(0,0)\), a saddle, and \((0,\pi)\), a strict minimum; the boundary seam \(y=1/2\) has angular critical values at \(\theta=0,\pi\). Evaluating the four values yields \(0,s_a,e_a,\Lambda_a\). They all lie in \([0,\Lambda_a]\), and continuity on the connected torus gives the full range. The identity \(\coth^2 z-\operatorname{csch}^2 z=1\) gives \(\Lambda_a-s_a=a\). Equality \(s_a=e_a\) reduces to \(\sinh^4(a/2)=1+\sinh^2(a/2)\), whose unique positive solution is \(\sinh^2(a/2)=(1+\sqrt5)/2\); monotonicity gives the ordering.

**3. Lower edge.** Near the unique zero \((x,\theta)=(1/2,\pi)\), write \(u=x-1/2\), \(v=\theta-\pi\). Direct expansion of the exact multiplier gives
\[
 H_a=\alpha_a u^2+\beta_a v^2+O_a((|u|+|v|)^3),\quad
 \alpha_a=\frac{4a^3q}{(1+q)^2},\quad
 \beta_a=\frac{aq(1-q)^2}{(1+q)^4}.
\]
The Hessian is positive definite. The smooth Morse change of variables shows that the sublevel area in \(dx\,d\theta/(2\pi)\) is \(s/(2\sqrt{\alpha_a\beta_a})+O_a(s^2)\), including the differentiated version for its density. Consequently \(\rho_a(0+)=1/(2\sqrt{\alpha_a\beta_a})=(1+q)^3/[4a^2q(1-q)]\). The same conclusion follows directly by scaling the exact one-dimensional density integral.

**4. Logarithmic saddle.** Near \((u,v)=(0,0)\), the exact multiplier expands as
\[
 H_a=s_a+a^2s_a u^2-\gamma_a v^2+O_a((|u|+|v|)^3),\qquad
 \gamma_a=s_a\left(\tfrac14+\frac{2q}{(1-q)^2}\right)>0.
\]
The local Morse normal form \(X^2-Y^2\), together with \(dx\,d\theta/(2\pi)\), has pushforward density \([2\pi\sqrt{a^2s_a\gamma_a}]^{-1}\log(1/|s-s_a|)+O_a(1)\). Elsewhere the density is regular except possibly at the seam threshold, whose bounded square-root contribution cannot change the logarithmic leading coefficient. Substitution yields \(C_a\).

**5. Upper edge and seam cusp.** Near the seam maximum \((x,\theta)=(0,0)\), using \(r\ge0\) for distance to the seam, direct one-sided Taylor expansion gives
\[
 H_a=\Lambda_a-A_a^{\rm top}r-B_a^{\rm top}\theta^2+O_a(r^2+r\theta^2+\theta^4),\quad
 A_a^{\rm top}=2a^2\coth(a/2),\quad B_a^{\rm top}=\frac{2\Lambda_aq}{(1-q)^2}.
\]
There are two sides of the seam. Integrating the level-set Jacobian over \(|\theta|<\sqrt{(\Lambda_a-s)/B_a^{\rm top}}\) gives \(\rho_a(s)=[2/(\pi A_a^{\rm top}\sqrt{B_a^{\rm top}})]\sqrt{\Lambda_a-s}+O_a(\Lambda_a-s)\), exactly \(K_a\).

Near the seam angular minimum \((x,\theta)=(0,\pi)\), the corresponding expansion is
\[
 H_a=e_a-A_a r+B_a(\theta-\pi)^2+O_a(r^2+r(\theta-\pi)^2+(\theta-\pi)^4),
\]
with the positive constants \(A_a,B_a\) in the statement. The spectral density has a smooth background across \(e_a\) unless \(e_a=s_a\). Above \(e_a\), the constraint \(s<U(\theta)\) deletes an angular interval of total length \(2\sqrt{(s-e_a)/B_a}+O_a((s-e_a)^{3/2})\); the limiting conditional density from both seam sides is \(2/A_a\). This yields the downward cusp coefficient \(2/(\pi A_a\sqrt{B_a})\). Below \(e_a\), no angular interval is deleted and the regular contribution varies by \(O_a(|s-e_a|)\). The claimed one-sided laws follow.

## Verification
The included standalone checker compares geometric-series Zak evaluations with the closed formula and its modulus; independently evaluates the spectral mean by midpoint quadrature; checks the Hessian at the unique zero; and verifies the exact golden-ratio crossover numerically. These are finite numerical checks only. The unrestricted claims follow from the fiber-law identity and local analytic arguments above.

## Relationship to prior work
Janssen's *On Generating Tight Gabor Frames at Critical Density* (2003), especially Eq. (2.3), Eq. (3.14), and Proposition 4, supplies the underlying exponential Zak transform and its simple zero. Kloos and Stoeckler's *Zak transforms and Gabor frames of totally positive functions and exponential B-splines* (first posted November 28, 2013) studies Zak zero rigidity and frame bounds. This work explicitly builds on those formulas. The additional result here is the exact normalized spectral-law integral, all endpoint and interior singularity coefficients, and the ordering transition of two qualitatively different spectral critical levels. A separate spectral-density calculation for a quadratic cardinal spline concerns another window; its polynomial multiplier does not imply the present seam cusp or the golden-ratio transition.

## Limitations
The result concerns a normalized spectral pushforward, not a trace-class density of states. The prior formula for the Zak multiplier is classical; mathematical originality resides solely in the subsequent complete spectral-law and critical-level analysis. Unindexed equivalent spectral calculations remain possible. At the crossover, the logarithmic singularity and seam cusp occur at the same value, and only the logarithmic leading asymptotic is asserted there. Independent external proof and novelty review have not been performed.

## References
- A. J. E. M. Janssen, *On Generating Tight Gabor Frames at Critical Density*, Journal of Fourier Analysis and Applications **9** (2003), 175–214, doi:10.1007/s00041-003-0011-3. Full text: https://pure.tue.nl/ws/files/3079889/Metis235352.pdf.
- T. Kloos and J. Stoeckler, *Zak Transforms and Gabor Frames of Totally Positive Functions and Exponential B-Splines*, arXiv:1311.7359v1, November 28, 2013, https://arxiv.org/abs/1311.7359.
