# A sharp double-reversal threshold for transient habitat-occupancy rankings

## Finding

A species can occupy one habitat more frequently both immediately after a change and in the final equilibrium, yet occupy the other habitat more frequently throughout a nonempty intermediate interval, even while the two habitats' colonization and extinction rates remain constant. In the two-habitat, independent, linear colonization–extinction model, the following criterion is necessary and sufficient for exactly two **strict positive-time sign reversals** of the occupancy association; it also gives the sharp collision law for the two reversal times.

Let \(\gamma_i,\epsilon_i>0\), \(r_i=\gamma_i+\epsilon_i\), \(q_i=\gamma_i/r_i\), and \(0\le p_i(0)\le1\) for habitats \(i=1,2\). Suppose both the initial and limiting occupancy differences strictly favor habitat 1: \(p_1(0)>p_2(0)\) and \(q_1>q_2\). Define \(d=q_1-q_2>0\) and \(A(t)=p_1(t)-p_2(t)\). If \(r_1=r_2\), there cannot be two reversals. Otherwise let \(r_f=\max\{r_1,r_2\}\), \(r_s=\min\{r_1,r_2\}\) and define \((u,v)\) by

\[
(u,v)=\begin{cases}
(p_1(0)-q_1,\;p_2(0)-q_2),&r_1>r_2,\\
(q_2-p_2(0),\;q_1-p_1(0)),&r_2>r_1.
\end{cases}
\]

Then \(A(t)=d+u e^{-r_f t}-v e^{-r_s t}\). Precisely two positive-time sign changes occur **if and only if** \(u>0\), \(v>0\), \(r_fu>r_sv\) and

\[
0<d<m,\qquad
m=v\left(1-\frac{r_s}{r_f}\right)
\left(\frac{r_fu}{r_sv}\right)^{-r_s/(r_f-r_s)}.
\]

(The standing assumption \(A(0)=d+u-v>0\) is essential.) The two simple crossing times \(t_-<t_+\) straddle the unique minimum time

\[
t_*=\frac{\log(r_fu/(r_sv))}{r_f-r_s}>0.
\]

The association \(A(t)\) is positive before \(t_-\), negative between \(t_-\) and \(t_+\), and positive after \(t_+\). Equality \(d=m\) gives only a tangency and **no** sign reversal. When \(u,v,r_f,r_s\) are fixed and an admissible family approaches this boundary as \(d=m-\eta\) with \(\eta\downarrow0\), the duration of the misleading interval is

\[
t_+-t_-=2\sqrt{\frac{2\eta}{r_fr_s m}}+O(\eta).
\]

This threshold is nonvacuous on an open set of strictly interior ecological parameters. For example, choose \((q_1,q_2)=(3/5,1/2)\), \((r_1,r_2)=(4,1)\) and \((p_1(0),p_2(0))=(4/5,3/4)\). These correspond to strictly positive colonization and extinction rates \((\gamma_1,\epsilon_1)=(12/5,8/5)\) and \((\gamma_2,\epsilon_2)=(1/2,1/2)\). With \(x=e^{-t}\),

\[
A(t)=\frac1{10}+\frac15x^4-\frac14x.
\]

This is \(1/20>0\) at \(t=0\), \(-1/80<0\) at \(t=\log2\), and tends to \(1/10>0\) as \(t\to\infty\). The two crossing times are approximately \(0.127598992901\) and \(0.852234164747\).

## Assumptions and scope

Each habitat consists conceptually of an ensemble of comparable patches, with homogeneous time-independent colonization rate \(\gamma_i\), extinction rate \(\epsilon_i\), and instantaneous expected occupancy \(p_i(t)\), satisfying \(\dot p_i=\gamma_i(1-p_i)-\epsilon_i p_i\). Habitats are independent in the sense that their occupancy expectations obey separate linear equations; no dispersal-mediated feedback, observation error, seasonality, spatial correlation, or interaction is included. Initial and limiting occupancy rankings strictly favor habitat 1. The theorem concerns **the sign of a difference of expected occupancy fractions**, not organismal habitat choice or a change in intrinsic habitat quality. Initial occupancies may reflect a previous regime or intervention. A reversal means a strict sign change at a positive time; zeros of even multiplicity are not counted as reversals.

## Proof

**Exact response.** Integrating each affine differential equation gives \(p_i(t)=q_i+[p_i(0)-q_i]e^{-r_it}\), hence the displayed two-exponential form for \(A\). The two sign conditions at the endpoints are \(A(0)>0\) and \(\lim_{t\to\infty}A(t)=d>0\).

**At most two zeros.** If the rates agree, \(A\) is an affine function of a single strictly decreasing exponential, so has at most one zero. If the rates differ, its derivative is \(A'(t)=-r_fu e^{-r_ft}+r_sv e^{-r_st}\). The equation \(A'(t)=0\) is equivalent, whenever both coefficients are nonzero, to \(e^{(r_f-r_s)t}=r_fu/(r_sv)\), and therefore has at most one real solution. Rolle's theorem bounds the number of distinct positive zeros of \(A\) by two.

**Necessity and sufficiency.** With positive endpoint values, two sign changes require an interior strict negative minimum. For \(A'\) to change from negative to positive, the coefficient of the slowly decaying derivative must be positive and that of the rapidly decaying derivative must be negative. This forces \(v>0\), \(u>0\). Moreover \(A'(0)<0\) forces \(r_fu>r_sv\), giving the unique \(t_*>0\). The stationary-point identity \(r_fu e^{-r_ft_*}=r_sv e^{-r_st_*}\) gives

\[
A(t_*)=d-v\left(1-\frac{r_s}{r_f}\right)e^{-r_st_*}=d-m.
\]

Therefore \(A(t_*)<0\) is exactly \(d<m\). Since \(A\) is strictly decreasing to \(t_*\) and strictly increasing afterward, the positive endpoint values give exactly one simple crossing on either side. At \(d=m\), the sole positive-time zero is a quadratic tangency, not a sign change. If any strict condition fails, two reversals are impossible. In original ecological terms, if the faster habitat is habitat 1, both habitats must start **above** their equilibria; if the faster habitat is habitat 2, both must start **below** their equilibria, with sufficient contrast in the two relaxation amplitudes.

**Coalescence law.** At the stationary point,

\[
A''(t_*)=(r_f-r_s)r_sv e^{-r_st_*}=r_fr_s m>0.
\]

At \(d=m-\eta\), Taylor expansion about \(t_*\) gives \(A(t)=-\eta+\tfrac12r_fr_sm(t-t_*)^2+O((t-t_*)^3)\). The implicit local quadratic inversion yields \(t_\pm=t_*\pm\sqrt{2\eta/(r_fr_sm)}+O(\eta)\); subtracting proves the duration formula. The limiting family is asserted only where its probabilities remain in \([0,1]\), as in a neighborhood of the interior example.

**Sharp admissible witness.** In the explicit example, the polynomial in \(x=e^{-t}\) has opposite signs at \(x=1\), \(x=1/2\), and \(x=0\). Hence continuity supplies a sign-changing zero in each of \((1/2,1)\) and \((0,1/2)\). The at-most-two-zeros proof makes these all the positive-time zeros, proves their simplicity and establishes the advertised phase pattern. Because every sign and parameter inequality is strict, the witness persists under sufficiently small parameter perturbations.

## Verification

A standalone standard-library program, `verify_two_reversals.py`, checks exact rational endpoint/intermediate signs, locates the two simple example roots by bisection, tests the local square-root duration asymptotic at three distances from the threshold, and performs 2,456 admissible randomized phase classifications from 5,000 seeded samples. The mathematical proof above establishes the general classification and is independent of these finite checks. Execute with `python verify_two_reversals.py`.

## Relationship to prior work

Levins (1969) established an ecological motivation for habitat heterogeneity and colonization–extinction balance. MacKenzie et al. (2003) developed inference for colonization, local extinction, and imperfect detection, but not this deterministic two-habitat association phase diagram. Most directly, Yackulic et al. (2015) analyze transient occupancy–environment associations under time-invariant colonization and extinction rates, including an initially unoccupied invasion and a possible subsequent change in the association sign. Their reported calculations motivate this question but do not in the accessed theoretical treatment provide the present necessary-and-sufficient **two-positive-reversal** criterion under two arbitrary, strictly ordered nonzero initial occupancies, its admissible witness, or the quadratic tangency duration law. The elementary solution of each habitat equation is prior art; only this joint classification and its sharp boundaries are assessed here. A broader published theorem on zeros of exponential polynomials could imply the generic zero bound, but would still require a biologically admissible sharp criterion and witness.

## Limitations

This is a mean-occupancy theorem for a narrowly specified two-environment linear model. It does not predict observed reversals when occupancy is measured with error, establish actual host choices, describe the nonlinear feedback models also studied by Yackulic et al., or prove that the behavior is common in real ecosystems. The sharp square-root law holds near a nondegenerate interior tangency with fixed amplitudes and relaxation rates. Historical originality is a best-knowledge literature comparison, not an independent priority certification; direct access to the full publisher-hosted 2015 paper and all supplements was incomplete, so an uninspected broader discussion remains a residual risk.

## References

1. R. Levins (1969), “Some Demographic and Genetic Consequences of Environmental Heterogeneity for Biological Control,” *Bulletin of the Entomological Society of America* 15, 237–240. DOI: 10.1093/besa/15.3.237.
2. D. I. MacKenzie et al. (2003), “Estimating Site Occupancy, Colonization, and Local Extinction When a Species Is Detected Imperfectly,” *Ecology* 84, 2200–2207. DOI: 10.1890/02-3090.
3. C. B. Yackulic, J. D. Nichols, J. Reid and R. Der (2015), “To Predict the Niche, Model Colonization and Extinction,” *Ecology* 96, 16–23. DOI: 10.1890/14-1361.1.
