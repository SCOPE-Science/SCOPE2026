# Phase-cycled ballistic laws for a logarithmically periodic telegraph process

## Finding

A persistent particle can have mean-square displacement of exact ballistic order while having **no unique ballistic weak limit**. Let a unit-speed particle flip direction at time-dependent rate
\[
\lambda(t)=\frac{r(\log(1+t))}{1+t},\qquad t\geq0,
\]
where \(r\) is any positive, continuous, \(T\)-periodic function. Its displacement divided by elapsed time converges along logarithmic-phase subsequences to a unique periodic *family* of probability laws, rather than necessarily to one law. More precisely, for every phase \(\theta\),
\[
\frac{X_{\exp(nT+\theta)-1}}{\exp(nT+\theta)-1}
\ \Longrightarrow\ \nu_\theta\qquad(n\to\infty),
\]
where \(\nu_\theta\) is the position marginal of an explicit two-sided filtered telegraph process. The phase family is independent of the initial orientation and determines every subsequential limit. It is independent of phase **if and only if** \(r\) is constant. Thus every nonconstant positive periodic modulation gives at least two different ballistic subsequential laws.

Write \(a(s)\) for position--velocity correlation and \(q(s)\) for the variance of this limiting family. They are the unique positive periodic solution of
\[
 a'=1-[1+2r(s)]a,\qquad q'=2a-2q,
\]
and satisfy the exact integral representations
\[
 a(s)=\int_0^\infty\exp\!\left[-u-2\int_{s-u}^s r(v)\,dv\right]du,
 \quad q(s)=2\int_0^\infty e^{-2u}a(s-u)\,du.
\]
In particular, \(0<\min_s q(s)\leq\max_s q(s)<1\), so \(\mathbb E[X_t^2]\) remains of ballistic order even though its coefficient oscillates in \(\log(1+t)\).

For the physically natural harmonic protocol \(r(s)=c+\varepsilon\cos(\omega s)\), with \(c>0\), \(\omega>0\), \(|\varepsilon|<c\), and \(k=1+2c\), the exact linear response of the periodic variance is
\[
q_\varepsilon(s)=\frac1k-\frac{4\varepsilon}{k}\operatorname{Re}\!\left[
 \frac{e^{i\omega s}}{(k+i\omega)(2+i\omega)}\right]
 +O(\varepsilon^2),
\]
uniformly in \(s\). Hence its first-order oscillation amplitude is
\[
 \frac{4|\varepsilon|}{k\sqrt{k^2+\omega^2}\sqrt{4+\omega^2}}
 +O(\varepsilon^2).
\]

## Assumptions and scope

Let \(r:\mathbb R\to(0,\infty)\) be continuous, \(T\)-periodic for some \(T>0\), and obey \(0<r_*\le r(s)\le r^*<\infty\). Start \(X_0=0\); the orientation \(S_0\in\{-1,+1\}\) may have any initial distribution. At physical time \(t\ge0\), \(S_t\) changes sign according to an inhomogeneous Poisson counting process of deterministic intensity \(\lambda(t)\), and \(X_t=\int_0^t S_u\,du\). For variance and mean-square statements we take \(S_0\) symmetric; the asymptotic laws do not depend on this choice. The positive harmonic protocol is a special case; the distributional classification holds for every continuous positive periodic \(r\), without a small-amplitude assumption.

On logarithmic time \(s\ge0\), define
\[
 J_s=S_{e^s-1},\qquad Z_s=e^{-s}X_{e^s-1}.
\]
The state \((Z_s,J_s)\) belongs to \([-1,1]\times\{-1,+1\}\). Its generator at phase \(s\), acting on differentiable \(f\), is
\[
 L_sf(z,j)=(j-z)\partial_z f(z,j)
 +r(s)[f(z,-j)-f(z,j)].
\]
All statements concern this explicitly specified one-particle continuous-time model, not general persistent random walks with arbitrary feedback or spatial interactions.

## Proof

**1. Logarithmic reduction.** Since \(dt/ds=e^s=1+t\), the time-changed orientation flips at rate \(r(s)\). Differentiation gives \(dZ_s/ds=J_s-Z_s\) between jumps, proving the generator identity. The physical integrated hazard satisfies
\[
 \int_0^t\lambda(u)\,du=\int_0^{\log(1+t)}r(v)\,dv\ge r_*\log(1+t)\to\infty.
\]
Thus there are infinitely many reversals almost surely; the ballistic order is not caused by eventual freezing of orientation.

**2. Construct the periodic family and prove attraction.** On the whole logarithmic-time line construct an inhomogeneous Poisson *refresh* process of intensity \(2r(s)\). At each refresh assign a new orientation independently and uniformly in \(\{-1,+1\}\). A refresh produces an actual sign change with conditional probability \(1/2\), so its effective sign-flip rate is exactly \(r(s)\). Since the accumulated refresh intensity to the past is infinite, the most recent refresh before each \(s\) exists almost surely. Call the resulting two-sided orientation \(J_s^*\) and set
\[
 Z_s^*=\int_{-\infty}^s e^{-(s-v)}J_v^*\,dv.
\]
This integral is absolutely convergent and \(|Z_s^*|\le1\). The law \(\mu_s=\mathcal L(Z_s^*,J_s^*)\) satisfies \(\mu_{s+T}=\mu_s\) because the refresh process has \(T\)-periodic intensity and independent marks.

Couple any initial process \((Z_0,J_0)\), with \(|Z_0|\le1\), to \((Z_0^*,J_0^*)\) using the same marked refresh process after zero. If \(H\) is its first nonnegative refresh time, then \(\Pr(H>u)\le e^{-2r_*u}\) and the orientations agree after \(H\). Therefore
\[
 \Pr(J_s\ne J_s^*)\le e^{-2r_*s},
\]
\[
\mathbb E|Z_s-Z_s^*|
\le2e^{-s}+2\int_0^s e^{-(s-u)}e^{-2r_*u}\,du.
\]
For the metric \(d((z,j),(z',j'))=|z-z'|+\mathbf 1_{\{j\ne j'\}}\), these inequalities give a bounded-Lipschitz/Wasserstein coupling bound \(O((1+s)e^{-\beta s})\), \(\beta=\min\{1,2r_*\}>0\). Any other periodic solution, evolved over whole multiples of the period and subjected to this coupling, must coincide with \(\mu_s\); hence the periodic law is unique and attracts all initial laws.

The distribution of \(Z_s\) approaches \(\operatorname{pr}_z\mu_s\). For \(t=e^s-1>0\),
\[
 \left|\frac{X_t}{t}-Z_s\right|
 =\frac{|X_t|}{t(1+t)}\le\frac1{1+t},
\]
using \(|X_t|\le t\). Therefore \(X_t/t\) approaches the position marginal \(\nu_{\log(1+t)}\) in bounded-Lipschitz distance. Compactness of phase mod \(T\) proves that precisely the phase-family values constitute the set of subsequential weak limits, allowing coincident laws at different phases. The displayed subsequences realize each value.

**3. Moment equations and nonconstant-law criterion.** Symmetric refresh marks make \(\mu_s\) invariant under \((z,j)\mapsto(-z,-j)\); thus its mean position and orientation vanish. Apply the generator to \(zj\) and \(z^2\) to obtain
\[
 a'(s)=1-(1+2r(s))a(s),\qquad q'(s)=2a(s)-2q(s),
\]
where \(a=\mathbb E_{\mu_s}[ZJ]\) and \(q=\mathbb E_{\mu_s}[Z^2]\). Solving stable linear equations from the infinite past yields the two stated integral formulas. Positivity of their integrands gives \(a,q>0\). Since \(r_*>0\), the two-sided orientation has a positive chance of changing over every interval; its exponentially weighted average lies strictly between \(-1\) and \(1\) almost surely, hence \(q<1\). Continuity and periodicity make the lower and upper bounds uniform.

If \(q\) is constant then \(q'=0\), so \(a=q\) is constant. The first moment equation gives \(r(s)=(1/a-1)/2\), also constant. Conversely, if \(r(s)=c\), the stable periodic solutions are \(a=q=1/(1+2c)\), independent of phase. Uniqueness of the periodic law and time homogeneity then imply that its entire distribution is constant. Thus nonconstant \(r\) forces nonconstant \(q\), which in turn forces at least two different weak limits (different second moments). For a symmetric initial orientation, \(\operatorname{Var}(X_t/t)\) approaches \(q(\log(1+t))\), and so lacks an ordinary limit. Boundedness of \(|X_t/t|\le1\) converts the distributional coupling into convergence of the second moments uniformly in phase.

**4. Harmonic response.** Set \(r(s)=c+\varepsilon\cos(\omega s)\), \(k=1+2c\). Stable periodic solutions depend analytically on \(\varepsilon\) near zero, with uniform remainder over one period. Writing \(a=a_0+\varepsilon a_1+O(\varepsilon^2)\) and \(q=q_0+\varepsilon q_1+O(\varepsilon^2)\), the zero-order equations give \(a_0=q_0=1/k\). The first-order equations are
\[
 a_1'+ka_1=-\frac2k\cos(\omega s),\qquad
 q_1'+2q_1=2a_1.
\]
The unique periodic solutions are
\[
 a_1(s)=-\frac2k\operatorname{Re}\left(\frac{e^{i\omega s}}{k+i\omega}\right),\quad
 q_1(s)=-\frac4k\operatorname{Re}\left(
 \frac{e^{i\omega s}}{(k+i\omega)(2+i\omega)}\right).
\]
This proves the stated amplitude and uniform remainder. The amplitude is positive for every \(c,\omega>0\), in agreement with the nonperturbative criterion.

## Verification

The included standalone script `verify.py` integrates the coupled moment ODE to its periodic orbit, checks the constant-rate solution, compares the periodic correlation with the independent exponential-integral formula at multiple phases, verifies nonzero variance modulation and tests the derived complex-frequency linear-response coefficient at small amplitude. These finite numerical checks are consistency tests, not a substitute for the coupling and moment arguments above. Run `python verify.py` with NumPy and SciPy.

## Relationship to prior work

Pradhan, Roy and Ray (2026) establish exact arbitrary-flip-probability correlation recurrences for a *discrete-time* persistent walk and the critical ballistic mean-square law for a pure inverse-time power protocol. Those exact second-moment recurrences are an important predecessor, not a result claimed here. The present theorem instead resolves the **full scaling-law question** for *continuously time-changed*, discrete-scale-invariant rates: a unique phase-entrained family, the if-and-only-if limit criterion, and a uniform harmonic amplitude. Their power-protocol formulas do not directly furnish these distributional conclusions.

Garra and Orsingher (2014) explicitly obtain the Euler--Poisson--Darboux/Beta-type telegraph law for inverse-time reversal rates. This constant-coefficient case is established prior work and is expressly excluded from any novelty claim. De Gregorio and Garra (2026) likewise treat constant singular telegraph damping and its fractional-integral representation. Cressoni, Viswanathan and da Silva (2018) obtain log-periodicity for a different *memory-damaged, non-Markovian discrete-time* walk; their phase mechanism and observable are distinct. The present input has an exogenous logarithmically periodic *Poisson reversal rate* and the output is a periodic family of complete rescaled displacement laws, detected by an exact variance criterion. Similarity of vocabulary alone does not establish coverage; the model equations and conclusions were compared.

## Limitations

The result concerns a single symmetric-speed continuous-time telegraph walker with deterministic positive periodic hazard on the logarithmic time axis; it does not assert the same classification for arbitrary random or quasiperiodic rates, spatial interactions, or discrete-time transition kernels. There is no assertion of a new Beta law in the constant-rate case. The result is mathematically proved here but has not undergone independent audit or external priority review; a more general unlocated theorem on nonautonomous filtered telegraph processes or evolution families could imply some conclusions. The finite reproducibility checks alone cannot establish the full weak-limit theorem or publication priority.

## References

1. A. Pradhan, R. Roy and P. Ray, *Diffusive-to-Ballistic transition in a Persistent Random Walk* (2026), arXiv:2605.20116, first publicly submitted 2026-05-19. https://arxiv.org/abs/2605.20116
2. R. Garra and E. Orsingher, *Random flights related to the Euler-Poisson-Darboux equation* (2014), arXiv:1411.0648, first publicly submitted 2014-11-03. https://arxiv.org/abs/1411.0648
3. A. De Gregorio and R. Garra, *Stochastic Solutions to Abstract Telegraph-Type Equations Involving Fractional Dynamics*, Journal of Theoretical Probability 39 (2026), article 81. https://doi.org/10.1007/s10959-026-01541-1
4. J. C. Cressoni, G. M. Viswanathan and M. A. A. da Silva, *Log-periodicity in piecewise ballistic superdiffusion: Exact results*, Phys. Rev. E 98, 052102 (2018). https://doi.org/10.1103/PhysRevE.98.052102
