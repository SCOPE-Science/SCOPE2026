# Sharp curvature-sign transition and cubic-root bubbles in meromorphic Bergman metrics

## Finding
For the normalized Hilbert Bergman space on the punctured disk with power-area weight \( (\beta+1)|z|^{2\beta}\), \(\beta>-1\), the canonical Bergman metric has a **sharp curvature-sign classification**. Put \(m=\lceil\beta\rceil\), \(\delta=\beta-m+1\in(0,1]\), and \(c=(1-\delta)/\delta\). With the Gaussian curvature convention specified below, the metric is strictly negatively curved everywhere on the punctured disk if \(c\le\sqrt{2}\). If \(c>\sqrt{2}\), it has precisely one zero-curvature circle, strictly positive curvature inside, and strictly negative curvature outside. Equivalently, positive curvature occurs precisely when \(0<\delta<\sqrt{2}-1\), the initial part of each interval of weights immediately above an integer (and in the interval \(-1<\beta<0\)).

The zero-curvature radius \(r_c\) obeys the sharp two-regime laws
\[
 r_c\sim \left(\frac{\sqrt2}{6(1+\sqrt2)}\right)^{1/2}(c-\sqrt2)^{1/2}\quad(c\downarrow\sqrt2),
 \qquad r_c\sim2^{-1/3}c^{-1/3}\quad(c\to\infty).
\]
In the latter regime \(c^{-1}\sim\delta\), so the positive-curvature disk has radius \(2^{-1/3}\delta^{1/3}(1+o(1))\); at any fixed point distinct from the puncture, curvature tends to \(-2\), whereas the limiting curvature at the puncture tends to \(+4\).

## Assumptions and scope
Let \(\mathbb D^*=\{z\in\mathbb C:0<|z|<1\}\), and let \(dA=dx\,dy/\pi\). For every real \(\beta>-1\), the Hilbert space \(\mathcal A^2_\beta\) consists of holomorphic functions on \(\mathbb D^*\) with square-integrable norm for the probability measure \((\beta+1)|z|^{2\beta}dA\). The reproducing kernel is \(K_\beta(z,w)\). Define the conformal coefficient
\[
 g_\beta(z)=\partial_z\partial_{\bar z}\log K_\beta(z,z)>0,
 \qquad ds_\beta^2=g_\beta(z)|dz|^2.
\]
Our Gaussian curvature convention is \(\mathcal K_\beta=-2g_\beta^{-1}\partial_z\partial_{\bar z}\log g_\beta\); in this convention the ordinary disk Bergman metric has constant curvature \(-2\). No assertion is made about different conformal normalizations; their curvature magnitudes rescale, but signs and zero locations agree.

## Proof
**1. Exact kernel and metric.** A Laurent monomial \(z^n\) is integrable exactly for integers \(n\ge-m\), where \(m=\lceil\beta\rceil\), and its squared norm is \((\beta+1)/(\beta+n+1)\). Summing the orthogonal reproducing-kernel series yields
\[
 K_\beta(z,w)=\frac{(z\bar w)^{-m}}{\beta+1}\frac{\delta+(1-\delta)z\bar w}{(1-z\bar w)^2},
 \quad \delta=\beta-m+1\in(0,1].
\]
For \(x=|z|^2\in(0,1)\) and \(c=(1-\delta)/\delta\), the terms \(-m\log x\) and the kernel normalizing constant are harmonic away from the puncture. Therefore
\[
 g_\beta(x)=\frac{2}{(1-x)^2}+\frac{c}{(1+cx)^2}.
\]
The metric coefficient is strictly positive throughout \(\mathbb D^*\).

**2. A polynomial with one possible positive root.** For any smooth positive radial \(g(x)\), \(\partial_z\partial_{\bar z}\log g=(\log g)'(x)+x(\log g)''(x)\). Introduce \(t=x/(1-x)>0\). Direct rational differentiation and collection of powers give
\[
 \mathcal K_\beta(x)=-\frac{4Q_c(t)}{\bigl[2(1+(1+c)t)^2+c\bigr]^3},
\]
where
\[
\begin{aligned}
Q_c(t)={}&-(c+2)(c^2-2)+12(c+1)(c+2)t\\
&+6(c+1)^2(c^2+4c+10)t^2\\
&+4(c+1)^3(c^2+5c+20)t^3\\
&+6(c+1)^4(c+10)t^4\\
&+24(c+1)^5t^5+4(c+1)^6t^6.
\end{aligned}
\]
Every nonconstant coefficient is strictly positive for \(c\ge0\), so \(Q_c'(t)>0\) for \(t\ge0\), and \(Q_c(t)\to+\infty\) as \(t\to\infty\). Its constant term is \(-(c+2)(c^2-2)\). Thus for \(c\le\sqrt2\) one has \(Q_c(t)>0\) for each \(t>0\), hence strictly negative curvature. For \(c>\sqrt2\), the polynomial has exactly one positive zero \(t_c\), with negative sign before it and positive sign after it. Since the curvature has the opposite sign, the unique zero-curvature circle is at \(r_c=\sqrt{t_c/(1+t_c)}\), with the asserted sign configuration. The equivalence \(c>\sqrt2\iff \delta<1/(1+\sqrt2)=\sqrt2-1\) is immediate.

**3. Critical and singular-parameter asymptotics.** At the threshold \(c_0=\sqrt2\), the zero of \(Q_{c_0}\) sits at \(t=0\) and \(\partial_t Q_{c_0}(0)=12(1+\sqrt2)(2+\sqrt2)>0\). Expanding \(Q_c(0)=-(c+2)(c^2-2)\) gives
\[
 t_c\sim\frac{\sqrt2}{6(1+\sqrt2)}(c-\sqrt2),
\]
whence the square-root asymptotic for \(r_c\). For the second regime, substitute \(t=c^{-2/3}y\) in the explicit polynomial. Uniformly on each compact subset of \([0,\infty)\),
\[
 c^{-3}Q_c(c^{-2/3}y)\longrightarrow4y^3-1.
\]
Its unique positive root is \(4^{-1/3}\). Strict monotonicity of each \(Q_c\) and sign comparison at fixed \(y\) on both sides of that root imply \(c^{2/3}t_c\to4^{-1/3}\); hence \(r_c\sim2^{-1/3}c^{-1/3}\).

**4. Boundary limits.** Evaluating the radial curvature formula at the omitted puncture by a limit gives
\[
 \lim_{|z|\downarrow0}\mathcal K_\beta(z)=\frac{4(c^2-2)}{(c+2)^2},
 \qquad\lim_{|z|\uparrow1}\mathcal K_\beta(z)=-2.
\]
For each fixed \(0<|z|<1\), as \(c\to\infty\) the additional term \(c/(1+cx)^2\) converges to zero together with its first two derivatives; consequently \(\mathcal K_\beta(z)\to-2\) there, while the first displayed limit approaches \(+4\). This proves the claimed shrinking positive-curvature bubble.

## Verification
The attached standalone `checker.py` independently checks the kernel-series identity, the curvature-polynomial identity, the limiting puncture curvature and exact rational-parameter root sign comparisons using symbolic rational arithmetic. It also evaluates selected numerical instances solely as consistency checks. All infinite-dimensional and asymptotic assertions above are established in the proof, not inferred from finite tests.

## Relationship to prior work
Ghiloufi and Snoun (arXiv:2009.04307) developed the relevant modified Bergman kernels and their zero sets. Ghiloufi and Zaway (arXiv:2309.00552) established the meromorphic Hilbert-space framework. Snoun (arXiv:2310.03519), especially Section 4.1, developed the kernel-induced metric and proved comparison inequalities with the Poincaré metric; its introduction describes the curvature as negative. The explicit formula here shows that this qualitative description cannot hold throughout the entire weight range under the paper's own metric definition: for example, choosing \(\beta=-7/10\) gives \(\delta=3/10\), \(c=7/3\) and positive curvature sufficiently close to the puncture. That prior paper does **not** give a proved universal curvature-sign theorem or a circle classification in its Section 4.1. Ghiloufi and Snoun (arXiv:2401.03941) use the same metric for Berezin transform estimates without deriving these sign-transition and cubic-root statements.

## Limitations
The curvature classification is for the outer Bergman weight exponent equal to zero, i.e. pure radial power \(|z|^{2\beta}\); it does not establish a sign diagram for arbitrary additional boundary weight \((1-|z|^2)^\alpha\). The puncture is omitted, so all values stated at \(z=0\) are limits, not curvatures assigned to that point. The theorem does not claim a previously unknown reproducing kernel or a new general metric construction. Historical priority remains provisional, because a broader general curvature theorem could imply portions of these formulas despite the targeted searches.

## References
1. N. Ghiloufi and S. Snoun, *Zeros of new Bergman kernels*, arXiv:2009.04307 (first public 2020-09-09).
2. N. Ghiloufi and M. Zaway, *Meromorphic Bergman spaces*, arXiv:2309.00552 (first public 2023-09-01).
3. S. Snoun, *Toeplitz operators via Carleson measures on beta-modified Bergman spaces*, arXiv:2310.03519 (first public 2023-10-05), §4.1.
4. N. Ghiloufi and S. Snoun, *Berezin transforms on modified Bergman spaces*, arXiv:2401.03941 (first public 2024-01-08), §4.
