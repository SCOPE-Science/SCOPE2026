# Spectral saturation and irradiation-strength crossover of semi-grey planetary inversion depths

## Finding

The familiar single-beam semi-grey atmospheric temperature law admits a sharp multiband irradiation-depth classification. For finitely many positive stellar absorption bands with fixed thermal opacity, the temperature has **at most one interior minimum**. Its existence is determined by one exact weighted spectral excess. If that minimum exists and the irradiation intensity is increased without changing the spectral fractions, its optical depth has two different limiting behaviors: it **saturates at a finite depth** when any sufficiently transparent visible band is present, but grows **logarithmically without bound** when all active bands are strongly absorbing. A two-band subfamily has an exact crossover function interpolating between these behaviors as the strength of a weak transparent band changes.

For each \(i=1,\ldots,n\), let \(j_i>0\) be a stellar-flux weight and let \(\lambda_i>0\) be the ratio of its visible absorption opacity to the thermal opacity, divided by its incidence-direction cosine. Let \(T_{\mathrm{int}}>0\) be the intrinsic effective temperature and \(s>0\) multiply every stellar-flux weight. Define \(T_s(\tau)>0\), for thermal optical depth \(\tau\geq0\), by

\[
T_s(\tau)^4=\frac{3T_{\mathrm{int}}^4}{4}\left(\frac23+\tau\right)
 +\frac{3s}{4}\sum_{i=1}^n j_i\left[\frac23+\frac1{\lambda_i}
 +\left(\frac{\lambda_i}{3}-\frac1{\lambda_i}\right)e^{-\lambda_i\tau}\right].
\]

Put \(B=3T_{\mathrm{int}}^4>0\), and form the nonnegative exponential sums

\[
P(\tau)=\sum_{\lambda_i>\sqrt3}j_i(\lambda_i^2-3)e^{-\lambda_i\tau},\qquad
Q(\tau)=\sum_{\lambda_i<\sqrt3}j_i(3-\lambda_i^2)e^{-\lambda_i\tau}.
\]

Bands with \(\lambda_i=\sqrt3\) do not contribute to either derivative sum. Write \(H=P(0)-Q(0)\). Then:

1. **Sharp existence and uniqueness.** If \(H\leq0\), there is no interior temperature extremum for any \(s>0\). If \(H>0\), define \(s_c=B/H\). For \(s\leq s_c\), the temperature is strictly increasing on \((0,\infty)\); equality at \(s=s_c\) gives only a zero boundary derivative at \(\tau=0\). For every \(s>s_c\), there is exactly one interior stationary point \(\tau_s>0\), a strict global minimum, and it solves

\[
P(\tau_s)-Q(\tau_s)=B/s.
\]

The minimum depth increases strictly with \(s\). Its onset is linear:

\[
\tau_s=\frac{H}{-\big(P'(0)-Q'(0)\big)}
\left(\frac{s}{s_c}-1\right)+O\left(\left(\frac{s}{s_c}-1\right)^2\right)
\quad(s\downarrow s_c).
\]

2. **Finite saturation versus logarithmic deepening.** Assume \(H>0\). If \(Q\) is nonzero, there is a unique finite \(\tau_\infty>0\) with \(P(\tau_\infty)=Q(\tau_\infty)\), and

\[
0<\tau_s<\tau_\infty,\qquad
\tau_\infty-\tau_s=
\frac{B}{s\big[Q'(\tau_\infty)-P'(\tau_\infty)\big]}+O(s^{-2}).
\]

The denominator is strictly positive. If instead \(Q\equiv0\), let \(\lambda_0=\min\{\lambda_i:\lambda_i>\sqrt3\}\), and let \(A_0=\sum_{\lambda_i=\lambda_0}j_i(\lambda_i^2-3)>0\). Then

\[
\tau_s=\frac1{\lambda_0}\log\left(\frac{sA_0}{B}\right)+o(1)
\quad(s\to\infty).
\]

3. **Exact two-band crossover.** Suppose \(P(\tau)=A e^{-h\tau}\) and \(Q(\tau)=\epsilon C e^{-\ell\tau}\), where \(h>\sqrt3>\ell>0\), \(A,C>0\), and \(0<\epsilon<A/C\). Let \(s>B/(A-\epsilon C)\), \(\Delta=h-\ell\),

\[
\tau_\infty=\frac{\log(A/(\epsilon C))}{\Delta},\quad
K_\epsilon=Ae^{-h\tau_\infty},\quad
\Xi=\frac{sK_\epsilon}{B}.
\]

Then the entire difference between the finite saturation depth and the actual minimum is the **exact** function \(\tau_\infty-\tau_s=\Psi(\Xi)>0\), where \(\Psi(\Xi)\) is the unique positive solution of

\[
e^{h\Psi}-e^{\ell\Psi}=\frac1\Xi.
\]

As a function of the positive crossover parameter, \(\Psi(\Xi)=h^{-1}\log(1/\Xi)+o(1)\) when \(\Xi\downarrow0\), and \(\Psi(\Xi)=1/(\Delta\Xi)+O(\Xi^{-2})\) when \(\Xi\to\infty\). The first asymptotic retrieves the essentially single-band logarithmic depth when the transparent band is extremely weak; the second retrieves the saturation correction. The identity is exact whenever the indicated minimum lies in the physical domain.

## Assumptions and scope

The underlying atmospheric approximation is plane-parallel, static, purely absorbing in the incident stellar bands, radiative (no convective adjustment), in local thermal equilibrium, and treated with the Eddington closure and the outer boundary convention of Guillot (2010, Equation 27). The single shared thermal absorption opacity is independent of depth; each visible-to-thermal ratio is fixed. The stellar field is represented by finitely many collimated, independently absorbed bands; its overall intensity changes through \(s\), keeping spectral proportions and incidence angles fixed. More explicitly, a band with incidence cosine \(0<\mu_i\leq1\), visible/thermal opacity ratio \(\gamma_i>0\), and positive reference irradiation temperature \(\Theta_i\) corresponds to \(\lambda_i=\gamma_i/\mu_i\), \(j_i=\mu_i\Theta_i^4\). The formula is the linear superposition of the separate forcing terms, **not** a claim about variable thermal opacities or arbitrary non-grey radiative equilibrium.

The optical depth \(\tau\) increases downward. Consequently, a strict temperature minimum at positive \(\tau\) delimits a region in which the upper atmosphere is hotter than the adjacent deeper region. These are mathematical temperature-profile statements. No empirical inference about a particular planet is asserted.

## Proof

**Step 1: Exact derivative and positivity.** Each irradiation bracket equals \(2/3+\lambda_i/3>0\) at \(\tau=0\) and tends to \(2/3+1/\lambda_i>0\) at infinity. Its derivative has constant sign, so it stays positive. Thus \(T_s(\tau)>0\). Term-by-term differentiation gives

\[
4\frac{d}{d\tau}\big[T_s(\tau)^4\big]
=B+s\big[Q(\tau)-P(\tau)\big].
\]

Since the fourth root is increasing, the sign of \(T_s'(\tau)\) is precisely the sign of this expression.

**Step 2: The sharp inversion criterion.** If no exponent exceeds \(\sqrt3\), then \(P\equiv0\) and the derivative is positive. Otherwise consider

\[
R_s(\tau)=\frac{P(\tau)}{B/s+Q(\tau)}.
\]

For positive \(P\), the logarithmic derivative \(P'/P\) is a strictly negative weighted average of the high opacity exponents, and is strictly smaller than \(-\sqrt3\). Because every exponent entering \(Q\) is strictly smaller than \(\sqrt3\) and \(B/s>0\), the logarithmic derivative of \(B/s+Q\) is strictly greater than \(-\sqrt3\). Hence \(R_s'(\tau)<0\) for all finite \(\tau\geq0\), and \(R_s(\tau)\to0\) as \(\tau\to\infty\). The derivative of \(T_s^4\) has the sign of \(1-R_s\). Its initial value is negative exactly when \(s[P(0)-Q(0)]>B\); in that event the strict decrease of \(R_s\) gives exactly one zero, where the derivative changes from negative to positive. When equality holds initially, the derivative is strictly positive after the boundary. This proves both the count and the global-minimum character.

**Step 3: Monotonicity and onset.** Put \(f=P-Q\). Whenever \(f(\tau)>0\),

\[
f'(\tau)<-\sqrt3 f(\tau)<0,
\]

because each high-rate term decays faster than \(e^{-\sqrt3\tau}\) and each low-rate term decays more slowly. Thus \(f\) is strictly decreasing on the entire positive region containing the unique minimum, where \(f(\tau_s)=B/s\). Implicit differentiation yields \(d\tau_s/ds=-B/(s^2 f'(\tau_s))>0\). Since \(f'(0)<0\) when \(H=f(0)>0\), Taylor expansion of \(f\) at zero together with \(B/s=H\,(s_c/s)\) gives the displayed linear onset and its stated remainder.

**Step 4: Strong-irradiation alternatives.** Suppose \(Q\not\equiv0\). As each exponent in \(P\) exceeds each exponent in \(Q\), \(P/Q\) decreases strictly from \(P(0)/Q(0)>1\) to zero. There is exactly one \(\tau_\infty>0\) with \(P=Q\), and \(f>0\) strictly before that point. The unique solution \(f(\tau_s)=B/s\) increases to \(\tau_\infty\). At the limit \(f'(\tau_\infty)<0\): specifically, \(P'(\tau_\infty)<-\sqrt3 P(\tau_\infty)\) and \(Q'(\tau_\infty)>-\sqrt3 Q(\tau_\infty)\), with equal positive values of \(P,Q\). Taylor's theorem at \(\tau_\infty\) gives the \(s^{-1}\) deficit with an \(O(s^{-2})\) remainder. If \(Q\equiv0\), the finite positive high-band sum satisfies \(P(\tau)=A_0e^{-\lambda_0\tau}(1+o(1))\) at large depth, and its equation \(P(\tau_s)=B/s\) immediately yields the logarithmic asymptotic.

**Step 5: Exact two-band crossover.** For the stated two-band data, \(A e^{-h\tau_\infty}=\epsilon C e^{-\ell\tau_\infty}=K_\epsilon\). Setting \(y=\tau_\infty-\tau_s>0\) in \(P(\tau_s)-Q(\tau_s)=B/s\) gives \(K_\epsilon(e^{hy}-e^{\ell y})=B/s\), exactly the displayed equation. Its left-hand side is strictly increasing from zero to infinity for \(y>0\), proving uniqueness. For \(\Xi\to\infty\), Taylor expansion at \(y=0\) gives \(1/\Xi=\Delta y+O(y^2)\). For \(\Xi\downarrow0\), divide the equation by \(e^{hy}\) to obtain \(hy=\log(1/\Xi)-\log(1-e^{-\Delta y})\), and observe \(y\to\infty\), giving the stated expansion. These steps prove the complete theorem.

## Verification

A standalone standard-library program, `check.py`, independently evaluates the original multiband temperature profile and its analytical derivative; brackets and bisects stationary points; and checks exact two-band crossover and limiting relationships. Executing `python check.py` gives:

- 5,000 finite-difference derivative comparisons passed;
- 3,000 randomized profile classifications passed (2,778 with an interior minimum);
- exact two-band example, saturation and logarithmic limits passed;
- 1,000 two-band crossover identities passed.

The fixed example uses \(T_{\mathrm{int}}=1\), high-band \((\lambda,j)=(3,10)\) and low-band \((\lambda,j)=(1,2)\). Then \(B=3\), \(P(\tau)=60e^{-3\tau}\), \(Q(\tau)=4e^{-\tau}\), \(s_c=3/56\), and \(\tau_\infty=\frac12\log15\approx1.354025100551\). At \(s=1\), the sole interior minimum is \(\tau_s\approx0.848000916459\); at \(s=1000\), it is \(\tau_s\approx1.352576932764\). Removing the low band changes the \(s=1000\) minimum to \((\log 20000)/3\approx3.301162517512\), illustrating logarithmic deepening. Numerical evidence is auxiliary: finite samples do not establish universal monotonicity or zero counts.

## Relationship to prior work

Guillot (2010), specifically its Equation 27 and Section 2.4, derives the classical one-beam grey thermal profile and discusses the physical occurrence of an inversion; that one-beam profile and its inversion are **not** new here. Parmentier and Guillot (2013 preprint; 2014 journal article), Section 3.8 and Equation 98, **explicitly establish linear superposition of arbitrarily many visible opacity bands**. That superposition is also **not** new. Their two-thermal-opacity, non-grey model covers different physics and can have additional thermal-depth effects. Heng, Hayek, Pont and Sing (2011), Sections 1–3, analyze clouds, hazes, scattering and modified inversion criteria under a dual-band shortwave/longwave approximation; those altered closure and opacity assumptions are not those in the present theorem.

Tokarev (2011), Theorem 7 and Remark 8, provides a general variation-diminishing/Descartes rule for Laplace transforms, which **already covers the upper bound of one zero** for separated signed exponential sums. The mathematical one-zero principle is therefore **not claimed as original**. The proposed contribution is the particular sharp physical irradiation-intensity criterion, the finite-versus-logarithmic location law at strong forcing, its explicit leading coefficients, and the exact weak-transparent-band crossover after combining the planetary radiative profile with an ordered-opacity analysis. The inspected relevant portions of the named primary texts did not state that combined irradiation-depth classification. It is not established that every earlier paper has been exhaustively checked; a broader or specialized existing result may still imply parts of the claims.

## Limitations

The model is an idealized fixed-thermal-opacity Eddington superposition; results should not be extrapolated to thermal opacity varying with optical depth, non-grey infrared transport, realistic scattering, clouds, horizontal advection, convection or a multidimensional atmosphere. The optical-depth minimum is not itself an observable spectrum or a measurement of geometric altitude. The theory addresses the mathematical response to common scaling of stellar spectral fluxes, not the response to changing band weights, opacities or atmospheric chemistry with luminosity. The exact two-band crossover concerns the stated positive parameter domain only, and its limiting function is not an empirical retrieval formula. Historical originality is provisional pending further comparison with specialized radiative-profile literature. Verification runs are finite checks, not substitutes for universal proof.

## References

1. T. Guillot, *On the radiative equilibrium of irradiated planetary atmospheres*, Astronomy & Astrophysics **520** (2010), A27; arXiv:1006.4702v1 (first public 2010-06-24), https://arxiv.org/pdf/1006.4702, especially Equation 27 and Section 2.4.
2. V. Parmentier and T. Guillot, *A non-grey analytical model for irradiated atmospheres. I: Derivation*, Astronomy & Astrophysics **562** (2014), A133; arXiv:1311.6597v1 (2013-11-26), https://arxiv.org/pdf/1311.6597, especially Section 3.8 and Equation 98.
3. K. Heng, W. Hayek, F. Pont and D. K. Sing, *On the effects of clouds and hazes in the atmospheres of hot Jupiters: semi-analytical temperature-pressure profiles*, Monthly Notices of the Royal Astronomical Society (2012); arXiv:1107.1390, https://arxiv.org/pdf/1107.1390, Sections 1–3.
4. D. V. Tokarev, *A generalisation of Descartes' rule of signs*, Journal of the Australian Mathematical Society **91** (2011), 415–420, https://doi.org/10.1017/S144678871100156X, Theorem 7 and Remark 8.
