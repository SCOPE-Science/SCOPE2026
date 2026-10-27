# An exact dispersion law for asymmetric instantaneous-reset Brownian ratchets

## Finding

For a free Brownian particle repeatedly captured at asymmetric periodic well basins at independent Poisson times, the long-time **unwrapped** drift and dispersion both admit closed hyperbolic formulas. The drift formula is known from the instantaneous-ratchet limit of Roberts–Sezik–Lardet; the dispersion formula, the explicit duration–jump correlation correction, and the accompanying all-asymmetry optimization and diffusion-enhancement assertions are the assessed results here.

Put \(x=(L/2)\sqrt{r/D}\), \(0<c<1\), and \(S(x,c)=\sinh(cx)/\sinh x\). Then

\[
 v=\lim_{t\to\infty}\frac{\mathbb E X_t}{t}
 =\frac{2Dx^2}{L}S(x,c),
\]

\[
 D_{\mathrm{eff}}=\lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}{2t}
 =D\left[\frac{x^2\cosh(cx)\cosh x}{\sinh^2x}
 +\frac{x^3}{2}S(x,c)\,\partial_xS(x,c)\right].
\]

The second summand is strictly negative: \(\partial_xS(x,c)<0\) for every \(x>0\), \(0<c<1\). It is the indispensable covariance correction between a completed reset displacement and its waiting duration. In particular,

\[
 \frac{D_{\mathrm{eff}}}{D}=1+\frac{1+3c^2}{6}x^2+O(x^4)\quad(x\downarrow0),
 \qquad D_{\mathrm{eff}}\longrightarrow0\quad(x\to\infty)
\]

for every fixed \(c\in(0,1)\). Therefore sufficiently weak nonzero resetting simultaneously generates positive drift and increases long-time dispersion above bare Brownian diffusivity; sufficiently strong resetting suppresses dispersion below bare diffusivity.

The **physical** drift speed \(v\), viewed as a function of \(r\) at fixed \(D,L,c\), has exactly one positive global maximum, characterized by

\[
 \frac{2}{x_*}+c\coth(cx_*)-\coth x_*=0,
 \qquad r_* =\frac{4D x_*^2}{L^2}.
\]

The unique \(x_*(c)\), hence \(r_*(c)\), increases strictly with asymmetry \(c\). For \(c\uparrow1\), \((1-c)x_*(c)\to2\). The conclusion is for \(0<c<1\); at exactly \(c=0\), the current vanishes identically and there is no distinguished drift-optimal rate.

## Assumptions and scope

Fix \(D>0\), cell spacing \(L>0\), Poisson intensity \(r>0\), and an asymmetry parameter \(0<c<1\). Put \(a=L(1+c)/2\) and \(b=L(1-c)/2\), so \(a+b=L\) and \(a>b>0\). Let \(X_0=0\) and, between independent rate-\(r\) Poisson alarms, evolve \(X_t\) by \(dX_t=\sqrt{2D}\,dB_t\). At an alarm, when the pre-alarm position belongs to the half-open interval \([jL-a,jL+b)\), set the position instantly to \(jL\), with \(j\in\mathbb Z\). The endpoints are probabilistically irrelevant. The position is **not wrapped modulo the lattice** when moments are taken. All resetting excursions have zero physical return duration. Limits concern long-time unwrapped mean and variance, not finite-time cumulants or noninstantaneous return potentials.

## Proof

**Renewal reduction.** Let \(T\sim\mathrm{Exp}(r)\) be one excursion duration and \(Y\), conditionally on \(T=t\), be normal with mean zero and variance \(2Dt\). The next capture-well increment is \(Z=LN\), where \(N=\lfloor(Y+a)/L\rfloor\). Excursion pairs \((T,Z)\) are independent and identically distributed, but their two coordinates are **not independent**. The integrated Brownian density of \(Y\) is the two-sided Laplace density \(k e^{-k|y|}/2\), with \(k=\sqrt{r/D}\). Thus, for every integer \(n\ge1\),

\[
 \Pr(N\ge n)=\tfrac12 e^{-k((n-1)L+b)},\qquad
 \Pr(N\le-n)=\tfrac12 e^{-k((n-1)L+a)}.
\]

Summation of the positive and negative integer tails yields exact cycle moments

\[
 m=\mathbb E N=\frac{S(x,c)}2,
 \qquad q=\mathbb E N^2
 =\frac{\cosh(cx)\cosh x}{2\sinh^2 x}.
\]

Since \(\mathbb E N=\int_0^\infty r e^{-rt}\mathbb E[N\mid T=t]dt\), differentiation under the integral gives

\[
 \mathbb E[NT]=\frac{m}{r}-\frac{\partial m}{\partial r}
 =\frac{m}{r}-\frac{x\,\partial_x S(x,c)}{4r}.
\]

This derivative identity is crucial: replacing \(\mathbb E[NT]\) with \(\mathbb E N\,\mathbb ET\) would miss a nonzero contribution. All required cycle moments are finite by exponential-tail bounds.

**Renewal–reward dispersion.** The renewal reward strong law and central-limit variance formula, applied to \((T,Z)\), imply

\[
 v=\frac{\mathbb E Z}{\mathbb E T}=rLm,
 \quad 2D_{\mathrm{eff}}=\frac{\mathbb E[(Z-vT)^2]}{\mathbb ET}
 =r\,\mathbb E[(LN-vT)^2].
\]

Here \(\mathbb ET=1/r\) and \(\mathbb ET^2=2/r^2\). Substitute the displayed formulas for \(m,q,\mathbb E NT\), expand the square, and simplify to obtain the claimed drift and dispersion. The displacement from the last completed reset to the observation time has uniformly bounded second moment because the age of the current exponential cycle is stochastically bounded by an exponential variable. Hence this residual does not affect the \(t^{-1}\) limiting mean or variance.

**Strict negative correction.** Since \(u\mapsto u\coth u\) is strictly increasing for \(u>0\),
\(\partial_x\log S=c\coth(cx)-\coth x<0\). Thus the correction \(Dx^3S\partial_xS/2\) is strictly negative. Taylor expansion of the exact expression yields the small-\(x\) formula. For fixed \(0<c<1\), exponential asymptotics \(S=O(e^{-(1-c)x})\) and \(\cosh(cx)\cosh x/\sinh^2x=O(e^{-(1-c)x})\) prove \(D_{\mathrm{eff}}\to0\), while positive variance ensures \(D_{\mathrm{eff}}>0\).

**Unique optimal drift.** The sign of \(\partial_x v\) is the sign of

\[
 H(x,c)=\frac2x+c\coth(cx)-\coth x.
\]

For \(x>0\),

\[
 \partial_xH=-\frac2{x^2}-c^2\operatorname{csch}^2(cx)+\operatorname{csch}^2 x<0,
\]

because \(c/\sinh(cx)>1/\sinh x\). Also \(H(x,c)\to+\infty\) as \(x\downarrow0\) and \(H(x,c)\to c-1<0\) as \(x\to\infty\). Therefore exactly one critical point exists, and since \(v\to0\) at both endpoints it is the unique global maximum. Its derivative with respect to asymmetry follows from

\[
 \partial_cH=\coth(cx)-cx\operatorname{csch}^2(cx)>0,
 \qquad \frac{dx_*}{dc}=-\frac{\partial_cH}{\partial_xH}>0.
\]

As \(c\uparrow1\), bounded \(x_*\) would contradict \(H(x_*,1)=2/x_*>0\), hence \(x_*\to\infty\). Apply the mean-value theorem to \(g_x(u)=u\coth(ux)\): for some \(\theta\in(c,1)\), \(\coth x-c\coth(cx)=(1-c)[\coth(\theta x)-\theta x\operatorname{csch}^2(\theta x)]\). Along \(x=x_*(c)\to\infty\), the bracket tends to one, since \(\theta\ge c\to1\). In the optimality equation \(2/x_*=(1-c)(1+o(1))\), therefore \((1-c)x_*\to2\). This completes the proof.

## Verification

A standalone Python checker (`check.py`) calculates the cycle moments through **separate numerical integration of Brownian Gaussian tails against the exponential waiting-time density**; it compares these numerical integrals to the hyperbolic formulas, including \(\mathbb E[NT]\), the effective drift, and the dispersion. It also checks several optimizer equations and weak/strong resetting regimes. Execution of the packaged checker returned **44 passed assertions**. Numerical computations test representative parameters only; the continuous all-parameter conclusions follow from the analytic proof above. Run with `python check.py` using NumPy and SciPy.

## Relationship to prior work

Ghosh, Nayak, Liu, Li and Marchesoni (2023) analyzed stochastic-resetting ratchets with a static asymmetric potential. Roberts, Sezik and Lardet (2024), Sec. IV, equation (24), gave the **same exact mean current in the instantaneous-potential limit**; the drift expression above is stated for context and is **not** claimed to be new. That paper also considers physical reset-phase currents and efficiency, but in the relevant full text it does not derive the unwrapped long-time effective diffusivity with the jump–duration covariance correction or prove the displayed all-asymmetry strict drift-rate uniqueness. Alston and Bertrand (2024) gave the symmetric nearest-site local-reset diffusivity; setting \(c=0\) here recovers that result, which is another **known** limiting case, not an additional claim of novelty. The present contribution concerns **nonzero asymmetry and the coupled exact drift–diffusion law**; its closest antecedent formulas are clearly identified.

## Limitations

The derivation requires exponential reset times, pure Brownian motion between alarms, instantaneous projection onto fixed periodic basins, and a constant fixed asymmetry \(0<c<1\). It does not describe return times, energetic costs, large deviations, or finite-time dispersions. The low-rate enhancement statement does **not** determine the number of crossings of \(D_{\mathrm{eff}}=D\), and no globally optimal dispersion rate is claimed. The current formula and symmetric diffusivity are previously known; novel priority of the asymmetric dispersion and covariance formula remains subject to independent expert literature comparison, particularly against general effective-diffusion formulas for flashing ratchets and renewal reward processes.

## References

- S. Ghosh, S. Nayak, J. Liu, Y. Li and F. Marchesoni, *Autonomous Ratcheting by Stochastic Resetting*, arXiv:2307.06202, first public version July 12, 2023. https://arxiv.org/abs/2307.06202
- C. Roberts, E. Sezik and E. Lardet, *Ratchet-mediated resetting: Current, efficiency, and exact solution*, arXiv:2405.10698, first public version May 17, 2024. https://arxiv.org/abs/2405.10698
- A. R. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772, first public version January 23, 2024. https://arxiv.org/abs/2401.12772
- J. Liu et al., *Ratcheting by Stochastic Resetting with Fat-Tailed Time Distributions*, DOI:10.1002/cphc.202400313 (2024). https://doi.org/10.1002/cphc.202400313
