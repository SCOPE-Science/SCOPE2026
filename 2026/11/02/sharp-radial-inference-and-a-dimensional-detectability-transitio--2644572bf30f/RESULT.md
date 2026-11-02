# Sharp radial inference and a dimensional detectability transition in intermittently trapped Brownian motion

## Finding

A particle subject to an intermittently activated isotropic harmonic trap retains a common, dynamically fluctuating positional variance across all spatial coordinates. We classify, exactly, the optimal single-snapshot decision about the hidden trap state, locate its dimension-dependent transition from a constant decision to a unique radial threshold, and give the sharp two-correction high-dimensional threshold and its strictly positive residual classification error.

Let \(a=q_{\mathrm{on}}/(2k)>0\) and \(b=q_{\mathrm{off}}/(2k)>0\). For every integer dimension \(d\ge1\), the optimal equal-loss decision based on one stationary position observation \(X\) chooses the off state precisely when
\[
R_d\!\left(\sqrt{k/D}\,\|X\|\right)\ge1,
\quad
R_d(r)=\frac{\int_0^\infty v^a e^{-bv}(1+v)^{-d/2}\exp[-r^2/(2(1+v))]\,dv}{\int_0^\infty v^{a-1}e^{-bv}(1+v)^{-d/2}\exp[-r^2/(2(1+v))]\,dv}.
\]
The function \(r\mapsto R_d(r)\) is strictly increasing for \(r>0\), and \(R_d(r)\sim r/\sqrt{2b}\) as \(r\to\infty\). If \(a\le b\), exactly one positive boundary exists in every dimension. If \(a>b\), there is a unique positive real \(d_c(a,b)\) determined by \(R_{d_c}(0)=1\). For integer \(d\le d_c\) the off decision is optimal at every observation (up to a null boundary); for integer \(d>d_c\) it changes once, from on to off, at a unique radius \(r_d>0\).

For fixed \(a,b>0\), in sufficiently high dimension the unique boundary obeys
\[
\boxed{\displaystyle r_d^2=2d+8(b-a)+\frac{16(1+b-a)}d+O_{a,b}(d^{-2}).}
\]
In particular, equal on/off switching rates yield \(r_d^2=2d+16/d+O_a(d^{-2})\). Despite high-dimensional concentration, the optimal misclassification probability never tends to zero:
\[
\boxed{\displaystyle \lim_{d\to\infty}\mathcal E_d=\frac{b}{a+b}\Pr\{G_a>1\}+\frac{a}{a+b}\Pr\{G_{a+1}\le1\}>0,}
\]
where \(G_s\sim\operatorname{Gamma}(s,\mathrm{rate}\ b)\). For \(a=b=1\), the limiting value is \((1-e^{-1})/2\). All claims concern a single simultaneous snapshot of the coordinates, not a time series.

## Assumptions and scope

Let \(k,D,q_{\mathrm{on}},q_{\mathrm{off}}>0\). The trap state \(J_t\in\{\mathrm{on},\mathrm{off}\}\) is a stationary two-state continuous-time Markov chain, with on-to-off rate \(q_{\mathrm{on}}\), off-to-on rate \(q_{\mathrm{off}}\), independent of a standard \(d\)-dimensional Brownian motion \(B\). In the on state,
\[dX_t=-kX_t\,dt+\sqrt{2D}\,dB_t;\]
in the off state, \(dX_t=\sqrt{2D}\,dB_t\). The same switch state acts on every coordinate. The stationary solution is uniquely defined as the pullback solution, since positive-duration on intervals yield almost-sure contraction. The dimensionless observation is \(Z=\sqrt{k/D}\,X\). Equal costs for the two possible incorrect state labels and the genuine stationary state priors are assumed. Both fixed \(d\) and \(d\to\infty\) assertions allow arbitrary fixed positive \(a,b\).

## Proof

**1. Conditional scale representation.** Conditionally on the two-sided past of \(J\), the pullback solution is a centered isotropic Gaussian with variance \(D(1+V_t)/k\) per coordinate, where \(V\ge0\) evolves, in time rescaled by \(2k\), according to \(\dot V=-V\) in the on state and \(\dot V=1\) in the off state. The joint stationary transport equations, with switching rates \(a,b\), have zero net flux \(-vp_{\mathrm{on}}(v)+p_{\mathrm{off}}(v)=0\). Their normalized solutions are
\[
p_{\mathrm{on}}(v)=\frac{b}{a+b}\frac{b^a}{\Gamma(a)}v^{a-1}e^{-bv},\qquad
p_{\mathrm{off}}(v)=\frac{a}{a+b}\frac{b^{a+1}}{\Gamma(a+1)}v^ae^{-bv}=v p_{\mathrm{on}}(v),\quad v>0.
\]
Thus \(Z\mid V=v\sim N_d(0,(1+v)I_d)\), and the joint switching-state densities, including their priors, differ by precisely the factor \(v\). This Gaussian/Gamma scale representation builds upon the established stationary switching-trap theory cited below; the inference claims begin with this representation.

**2. Radial likelihood ratio and its strict order.** Dividing the two Gaussian mixtures gives exactly \(R_d(r)=\mathbb E_{\nu_{d,r}}V\), with \(\nu_{d,r}\) proportional to \(v^{a-1}e^{-bv}(1+v)^{-d/2}\exp[-r^2/(2(1+v))]dv\). Differentiation under the integral yields
\[
\frac{\partial R_d}{\partial(r^2)}=\operatorname{Cov}_{\nu_{d,r}}\!\left(V,-\frac1{2(1+V)}\right)>0,
\]
since both displayed functions of \(V\) are strictly increasing and the mixing law is nonatomic. Consequently, the Bayes decision changes at most once as radius increases. For fixed \(d\) and large \(r\), the exponent \(-bv-r^2/[2(1+v)]\) has its dominant saddle at \(1+v\sim r/\sqrt{2b}\). Standard one-dimensional Laplace localization (the remaining polynomial terms are lower order) yields \(R_d(r)\sim r/\sqrt{2b}\). Hence a radial crossing exists if and only if \(R_d(0)<1\).

**3. Dimension threshold.** Extend \(m_d=R_d(0)\) to real \(d\ge0\). The same differentiation-under-the-integral calculation gives
\[
\frac{dm_d}{dd}=-\frac12\operatorname{Cov}_{\nu_{d,0}}(V,\log(1+V))<0.
\]
The endpoint values are \(m_0=a/b\) and \(m_d\to0\) as \(d\to\infty\), the latter by concentration of the factor \((1+v)^{-d/2}\) at \(v=0\). Therefore \(a\le b\) gives \(m_d<1\) for every positive dimension; \(a>b\) gives a unique critical real dimension \(d_c\) with \(m_{d_c}=1\). Equality at \(r=0\) is a null event in the continuous stationary position law. All decision cases stated above follow.

**4. Sharp large-dimensional radius.** Write \(r^2=2d+c+h/d\), \(\varepsilon=d^{-1/2}\), and \(v=1+\varepsilon z\). The unnormalized posterior logarithm, apart from terms independent of \(z\), has a unique Laplace maximum approaching \(z=0\) and expansion
\[
-\frac{z^2}{16}+\varepsilon A_1(z)+\varepsilon^2 A_2(z)+\varepsilon^3 A_3(z)+O(\varepsilon^4 P(z)),
\]
where
\[
\begin{aligned}
A_1(z)&=(a-b-1+c/8)z+z^3/24,\\
A_2(z)&=(1-a)z^2/2-cz^2/16-3z^4/128-h/4,\\
A_3(z)&=(a-1)z^3/3+cz^3/32+z^5/80+hz/8.
\end{aligned}
\]
Equivalently, the coefficient of \(z^3\) in \(A_3\) is \((a-1)/3+c/32\). The expansion of the posterior mean relative to one follows from Gaussian moments under \(N(0,8)\):
\[
R_d(r)-1=\frac{8(a-b)+c}{d}+\frac{16(a-b)+h-16}{d^2}+O(d^{-3})
\]
**after** choosing \(c=8(b-a)\) in the second coefficient. The general second coefficient, before this choice, is
\[
-64ab+48a+64b^2-8bc-48b+4c+h-16.
\]
Setting first and second terms successively to zero gives \(c=8(b-a)\) and \(h=16(1+b-a)\). The remainder bound follows by splitting the \(v\)-integrals into a fixed neighborhood of the unique saddle \(v=1\) and its exponentially dominated complement, Taylor expanding the smooth local amplitude, and controlling the Gaussian tails. Because \(\partial_{r^2}R_d\sim d^{-1}\) in this window, the resulting \(O(d^{-3})\) odds error moves \(r_d^2\) by \(O(d^{-2})\), as asserted. The symbolic coefficient calculation is independently reproducible in `SYMBOLIC.py`.

**5. Positive limiting Bayes error.** Conditional on \(V=v\), the coordinate squares are independent with common mean \(1+v\), hence \(\|Z\|^2/d\to1+v\) almost surely as \(d\to\infty\). The previous step gives \(r_d^2/d\to2\). Dominated convergence, using the continuous Gamma laws, transforms the exact threshold risk into
\[
\mathcal E_\infty=\pi_{\mathrm{on}}\Pr(G_a>1)+\pi_{\mathrm{off}}\Pr(G_{a+1}\le1).
\]
Both terms are strictly positive because the two Gamma laws have full support on \((0,\infty)\). With \(a=b=1\), their explicit tails give \(\mathcal E_\infty=(1-e^{-1})/2\). The error concerns classifying a latent state with overlapping, rather than disjoint, conditional variance distributions; measuring increasingly many coordinates identifies the variance but cannot eliminate this overlap.

## Verification

The accompanying `CHECK.py` independently evaluates the defining one-dimensional integrals, unique boundaries, the risk through generalized Laguerre quadrature, and the two-correction asymptotic at multiple dimensions and switching-rate pairs. It passed 106 finite numerical assertions with NumPy and SciPy. The accompanying `SYMBOLIC.py` independently checks the saddle coefficients exactly with SymPy. These finite calculations are diagnostics; they do not replace the proofs of strict monotonicity, existence/uniqueness, asymptotic localization, or limiting risk. Reproduction: `python CHECK.py` and `python SYMBOLIC.py` with Python, NumPy, SciPy, and SymPy installed.

## Relationship to prior work

Frydel's 2024 work investigates a Brownian particle in a fluctuating harmonic trap, including the stationary position laws and their mixture structure. Santra, Das, and Nath's 2021 work studies intermittent harmonic confinement and computes state-resolved characteristic functions. Frydel's 2026 age-structured paper explicitly develops Gamma-like conditional variance distributions. These ingredients are credited as known or directly implied by known stationary calculations. The present result addresses a different question: Bayes-optimal reconstruction of the unobserved current switching state from a single, possibly high-dimensional, positional snapshot. Its distinctive conclusions are the one-crossing/constant-decision classification, a unique real critical dimension, the two-term large-dimensional optimal radius, and a strictly positive asymptotic error formula. General theory of total positivity and Gaussian scale-mixture likelihoods supplies related ordering principles; possible stronger implicit priority coverage is not ruled out.

## Limitations

The theorem assumes a common two-state memoryless switch, isotropic harmonic confinement, independent Brownian coordinates, positive rates, a stationary initial joint state, and equal misclassification costs. The on/off Gamma variance distributions and their stationary mixture representation are prior ingredients, not claimed as new. The finite-dimensional threshold is implicit except in asymptotic form. The error floor pertains to a single position observation; a temporal trajectory may provide additional information. The large-dimensional coefficients hold with fixed positive \(a,b\), not uniformly for rates scaling with \(d\). The claim has not undergone independent scientific audit, and mathematical priority beyond the inspected literature is not certified.

## References

1. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213 (first version publicly submitted 2024-07-16), https://arxiv.org/abs/2407.12213.
2. I. Santra, S. Das, and S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609 (2021), https://arxiv.org/abs/2104.00609.
3. D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173 (2026), https://arxiv.org/abs/2607.05173.
