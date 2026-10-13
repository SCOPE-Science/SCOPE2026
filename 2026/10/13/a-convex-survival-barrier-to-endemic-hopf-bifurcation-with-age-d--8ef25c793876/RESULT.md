# A convex-survival barrier to endemic Hopf bifurcation with age-dependent infectivity

## Finding

**Theorem (endemic spectral barrier).** In the closed-population infection-age renewal model defined below, suppose that the residence-time probability density is nonincreasing with infection age. For every nonnegative, integrable infection-age infectivity profile with reproduction number \(\mathcal R_0>1\), the unique endemic equilibrium has **no characteristic root in the closed right half-plane**. In fact, the real part of its characteristic determinant is strictly positive throughout that half-plane. This rules out local Hopf bifurcation at endemic coexistence for *every* infectivity profile in the stated class, not merely exponentially decaying profiles.

If the residence-time survival function has a positive exponential moment, the endemic **incidence equilibrium is locally exponentially asymptotically stable** for sufficiently small bounded, compatible incidence-history perturbations. Without such a tail assumption the theorem asserts the characteristic-root exclusion but does not assert exponential convergence.

The condition includes all gamma residence-time distributions with shape \(0<j\leq1\) and arbitrary positive rate, finite mixtures of exponential durations, and uniform residence times. Thus oscillatory loss of endemic stability in this model requires a residence-time density that is *not* nonincreasing (when such a density exists).

## Assumptions and scope

Time and infection age are nonnegative real variables. Let \(K:[0,\infty)\to[0,\infty)\) be a Lebesgue-integrable, almost-everywhere nonincreasing probability density, with \(\int_0^\infty K(a)\,da=1\). Define the survival function
\[
F(a)=\int_a^\infty K(u)\,du,\qquad m=\int_0^\infty F(a)\,da\in(0,\infty).
\]
Let \(\beta\in L^1([0,\infty))\) be nonnegative and not zero on the support of \(F\). Set \(A(a)=\beta(a)F(a)\) and \(\mathcal R_0=\int_0^\infty A(a)\,da\). Assume \(\mathcal R_0>1\); scaling \(\beta\) realizes this domain. The incidence \(b(t)\) satisfies the model's nonlinear renewal equation
\[
b(t)=\left(1-\int_0^\infty F(a)b(t-a)\,da\right)
       \int_0^\infty A(a)b(t-a)\,da.
\]
The infected fraction is \(I(t)=\int F(a)b(t-a)\,da\), and susceptible fraction is \(S(t)=1-I(t)\). The nonzero constant-incidence equilibrium and its fractions are uniquely determined by
\[
b_* =\frac{1-\mathcal R_0^{-1}}{m},\quad
S_* =\mathcal R_0^{-1},\quad I_*=1-\mathcal R_0^{-1}.
\]
The extra tail hypothesis used **only** for exponential local stability is: \(\int_0^\infty e^{\eta a}F(a)\,da<\infty\) for some \(\eta>0\). Incidence-history perturbations are bounded and compatible with the renewal relation at their initial time.

## Proof

**1. Exact endemic linearization.** Put \(b(t)=b_*+x(t)\) and write \((G*x)(t)=\int_0^\infty G(a)x(t-a)\,da\). Expanding the nonlinear equation gives
\[
x=H*x-(F*x)(A*x),\quad
H(a)=\frac{A(a)}{\mathcal R_0}-\frac{\mathcal R_0-1}{m}F(a).
\]
Here \(b_*\mathcal R_0=(\mathcal R_0-1)/m\), so there is no omitted coefficient. The characteristic determinant for the linearization is
\[
\Delta(z)=1-\frac{\widehat A(z)}{\mathcal R_0}
+\frac{\mathcal R_0-1}{m}\widehat F(z),\qquad
\widehat G(z)=\int_0^\infty e^{-za}G(a)\,da.
\]
This is the endemic characteristic equation of Scarabel, Coldwell and Cassidy, written as \(\Delta(z)=0\).

**2. Convex-survival Fourier lemma.** Since \(K\) is nonincreasing, \(F'=-K\) is nondecreasing (in the distributional sense), so \(F\) is decreasing and convex. Fix \(\sigma\geq0\) and let \(g(a)=e^{-\sigma a}F(a)\). The product of these positive decreasing convex functions is convex: in distributional notation, \(g''=e^{-\sigma a}(F''-2\sigma F'+\sigma^2F)\geq0\). Also \(g\) is integrable, decreases to zero, and its derivative tends to zero. Thus there is a nonnegative curvature measure \(\mu_g=g''\) on \((0,\infty)\) satisfying
\[
g(a)=\int_{(a,\infty)}(u-a)\,\mu_g(du).
\]
For every real \(\omega\ne0\), Fubini's theorem (valid since \(\int g<\infty\)) gives
\[
\begin{aligned}
\Re\widehat F(\sigma+i\omega)
&=\int_0^\infty g(a)\cos(\omega a)\,da\\
&=\int_{(0,\infty)}\left(\int_0^u(u-a)\cos(\omega a)\,da\right)\mu_g(du)\\
&=\frac{1}{\omega^2}\int_{(0,\infty)}(1-\cos(\omega u))\,\mu_g(du)\geq0.
\end{aligned}
\]
For \(\omega=0\), the same real part is \(\int g(a)\,da>0\). Therefore \(\Re\widehat F(z)\geq0\) for every \(\Re z\geq0\), without assumptions on the sign or monotonicity of \(\beta'\).

**3. A strictly positive real characteristic determinant.** For \(z=\sigma+i\omega\) with \(\sigma\geq0\), positivity of \(A\) implies
\[
\Re\frac{\widehat A(z)}{\mathcal R_0}
=\frac1{\mathcal R_0}\int_0^\infty A(a)e^{-\sigma a}\cos(\omega a)\,da\leq1.
\]
It is **strictly** below one if \(\sigma>0\); it is also strictly below one if \(\sigma=0\) and \(\omega\ne0\), because a nonzero integrable density cannot be supported on the discrete set where \(\cos(\omega a)=1\). At \(z=0\) the cosine bound is an equality, but \(\widehat F(0)=m>0\). Since \(\mathcal R_0-1>0\), combining these facts with step 2 proves
\[
\boxed{\Re\Delta(z)>0\quad\text{for every }\Re z\geq0.}
\]
In particular \(\Delta(z)\ne0\) throughout the closed right half-plane, so no real or imaginary unstable characteristic exponent, including a Hopf crossing, exists under the stated hypotheses.

**4. Additional exponential stability when the tail is light.** Suppose \(\int e^{\eta a}F(a)\,da<\infty\). For some \(\eta_0>0\), both \(F\) and \(A=\beta F\) have finite \(e^{\eta_0a}\)-weighted integrals (for \(A\), use \(\beta\in L^1\) and \(\sup_a e^{\eta_0a}F(a)<\infty\), reducing \(\eta_0\) if necessary). Thus \(H\) has an exponential moment. Its Laplace transform is analytic in a left neighborhood of the imaginary axis and tends uniformly to zero as \(|\Im z|\to\infty\) on closed vertical substrips, by a uniform Riemann--Lebesgue argument. By step 3 and compactness, there is \(\delta>0\) such that \(1-\widehat H(z)\ne0\) whenever \(\Re z\geq-\delta\). The causal convolution resolvent belongs to weighted \(L^1\): the Wiener invertibility criterion for the unitized causal convolution algebra, applied to \(e^{\delta a}H(a)\), gives an inverse of the form identity plus a kernel \(r\) with \(\int_0^\infty e^{\delta a}|r(a)|\,da<\infty\). Split the linear convolution at the initial time; the past contributes a forcing that decays exponentially for bounded histories, because \(H\) has an exponential moment. The quadratic term \(-(F*x)(A*x)\) is locally Lipschitz with a quadratic smallness bound in the exponentially weighted supremum norm. Applying the weighted convolution resolvent and a contraction argument in a sufficiently small ball proves exponential decay of all sufficiently small compatible incidence-history perturbations. This is local, not global, stability.

## Verification

The companion `verify.py` constructs the exact rational Jacobians of the finite-dimensional closure for mixture-of-exponential residence-time laws and exponentially waning infectivity, then checks their numerical eigenvalues for \(126\) fixed parameter instances, including positive waning rates. It also checks the closed-form uniform-duration cosine-transform sign and the monotonicity derivative of gamma densities with shapes \(0<j\leq1\). Running the file with Python 3 and NumPy must return `VERIFY_OK`. These computations are *finite consistency checks only*: the unrestricted theorem is proved by the Fourier lemma and strict real-part estimate above.

## Relationship to prior work

Scarabel, Coldwell and Cassidy [1] define the same infection-age renewal equation (their equation (7)) and derive its endemic characteristic equation (the unnumbered endemic equation immediately following their equation (10) in the arXiv preprint). Their numerical examples produce Hopf bifurcations for sufficiently concentrated gamma residence times (notably shape near \(8.31\) and shape \(20\)). The present result gives an exact opposite-side structural barrier for *all* decreasing residence-time densities and *all* nonnegative infection-age infectivity profiles, including nonexponential ones. This barrier is not established by their numerical evidence.

Nakata and Röst [2] establish global endemic stability with general residence-time distributions in a classical SIS model whose transmission coefficient is **constant over infection age**. The present result instead allows unrestricted nonnegative age-varying \(\beta\) (with \(\beta\in L^1\)), which is essential to [1]'s Hopf mechanism, but has a recovery-density shape restriction and asserts only local stability under exponential tails. Neither result subsumes the other. Diekmann and Montijn [3] examine Fourier-root crossings for a temporary-immunity model with **deterministic** return time, not nonincreasing residence-time densities. Chen, Yang and Zhang [4] study a different SIRS compartment structure with separate recovery and additional assumptions; no verified theorem in the inspected accessible source establishes this all-infectivity convex-survival criterion.

## Limitations

The hypotheses are sufficient, not necessary: a residence-time density that increases somewhere may still lead to a stable endemic equilibrium. The absence of unstable characteristic roots excludes local endemic Hopf bifurcation, **not** large-amplitude periodic orbits, bistability far from the equilibrium, stochastic epidemic variability, or nonlinear global convergence. For heavy-tailed residence times the proof does not claim a spectral gap or exponential stability. An independent scientific audit has not been performed, and unindexed general renewal-equation theorems may overlap with portions of the argument.

## References

[1] F. Scarabel, H. Coldwell and T. Cassidy, *Genuine and spurious bistability in a simple epidemic model with waning immunity*, arXiv:2511.09196v1 (first public November 12, 2025), https://arxiv.org/abs/2511.09196; subsequently *Mathematical Biosciences* 396 (2026), 109671, doi:10.1016/j.mbs.2026.109671.

[2] Y. Nakata and G. Röst, *Global stability of an SIS epidemic model with a finite infectious period*, arXiv:1704.04225 (2017), https://arxiv.org/abs/1704.04225.

[3] O. Diekmann and R. Montijn, *Prelude to Hopf bifurcation in an epidemic model: analysis of a characteristic equation associated with a nonlinear Volterra integral equation*, *Journal of Mathematical Biology* 14 (1982), 117–127; open author preprint https://ir.cwi.nl/pub/7639/7639D.pdf.

[4] Y. Chen, J. Yang and F. Zhang, *The global stability of an SIRS model with infection age*, *Mathematical Biosciences and Engineering* 11 (2014), 449–469, doi:10.3934/mbe.2014.11.449.
