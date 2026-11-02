# A sharp phase-only identifiability window for a coupled two-layer climate response

## Finding

For the positive two-layer linear energy-balance model under sinusoidal forcing, the surface-temperature **phase lag as a function of the interlayer exchange coefficient** has exactly one strict minimum. Consequently, a single forcing frequency can associate two distinct positive exchange coefficients with exactly the same surface phase lag, even when the forcing, radiative feedback, and both heat capacities are known. The two coefficients have different transfer magnitudes, so a jointly observed complex response resolves the ambiguity.

More precisely, let the parameters \(C,D,\lambda,\omega>0\) be fixed, with \(\kappa>0\) variable. Define the positive lag \(\phi(\kappa)=-\arg H(\kappa)\) for the harmonic surface transfer function \(H\). The unique turning point is

\[
\kappa_* = \frac{D}{C+D}\left(\sqrt{\lambda^2+\omega^2C(C+D)}-\lambda\right).
\]

The lag decreases strictly on \((0,\kappa_*)\) and increases strictly on \((\kappa_*,\infty)\). Put

\[
\phi_* = \phi(\kappa_*),\quad
\phi_0 = \arctan\left(\frac{\omega C}{\lambda}\right),\quad
\phi_\infty=\arctan\left(\frac{\omega(C+D)}{\lambda}\right).
\]

Then \(0<\phi_*<\phi_0<\phi_\infty<\pi/2\). A prescribed observed phase in \((\phi_*,\phi_0)\) has **exactly two** distinct positive exchange coefficients; a phase equal to \(\phi_*\) or in \([\phi_0,\phi_\infty)\) has **exactly one**; all other phases have **none**. In particular, the upper endpoint \(\phi_\infty\) is not attained by finite positive coupling.

The inverse transfer \(Z(\kappa)=1/H(\kappa)\) traces exactly the open right semicircle

\[
\left(\operatorname{Re} Z-\lambda\right)^2+
\left(\operatorname{Im} Z-\omega(C+D/2)\right)^2
=\left(\frac{\omega D}{2}\right)^2,\qquad
\operatorname{Re}Z>\lambda,
\]

as \(\kappa\) runs through all positive real numbers. **Sharp bounded-parameter experiment design.** If \(\kappa\) is restricted in advance to a closed interval \([a,b]\) with \(0<a<b\), define

\[
\Omega(s)=\sqrt{\frac{(C+D)s^2+2\lambda D s}{CD^2}},\quad s>0.
\]

The phase-only response is noninjective on \([a,b]\) **if and only if**

\[
\boxed{\Omega(a)<\omega<\Omega(b).}
\]

At the frequency endpoints and outside that strict interval, the phase-only map is injective. Thus the ambiguity is not a generic assumption about fitting: it has an exact, testable design boundary under the stated known-parameter conditions.

## Assumptions and scope

The model is

\[
C\dot T(t)=F_0\cos(\omega t)-\lambda T(t)-\kappa(T(t)-U(t)),\qquad
D\dot U(t)=\kappa(T(t)-U(t)),
\]

where \(T\) and \(U\) are respectively upper- and deep-reservoir temperature anomalies. All of \(C,D,\lambda,\omega,F_0,\kappa\) are strictly positive, the forcing amplitude \(F_0\) and angular frequency \(\omega\) are known, and the only unknown parameter in this classification is the positive thermal exchange \(\kappa\). Heat capacities and feedback are constant. There are no stochastic shocks, efficacy corrections, nonlinear feedbacks, or additional layers. The claim concerns the unique asymptotic sinusoidal steady state, not transient initial-condition fits. The imaginary unit is \(i^2=-1\), and the convention \(T(t)=\operatorname{Re}\{F_0H e^{i\omega t}\}\) makes \(\phi=-\arg H>0\) a **positive** temporal phase lag.

The homogeneous coefficient matrix is stable: its trace is negative, and its determinant is \(\lambda\kappa/(CD)>0\). Hence every initial condition converges exponentially to the unique forced harmonic response and its phase is well-defined.

## Proof

**1. Harmonic transfer and inverse susceptibility.** Insert \(T(t)=\operatorname{Re}\{\widehat T e^{i\omega t}\}\) and \(U(t)=\operatorname{Re}\{\widehat Ue^{i\omega t}\}\). The second equation gives \(\widehat U=\kappa\widehat T/(\kappa+i\omega D)\). Dividing the first complex balance by \(\widehat T\), we obtain

\[
Z(\kappa):=H(\kappa)^{-1}
=\lambda+i\omega C+\frac{i\omega D\kappa}{\kappa+i\omega D}.
\]

Set \(q=\omega D\). Rationalization yields the strictly positive real and imaginary parts

\[
X(\kappa)=\lambda+\frac{q^2\kappa}{\kappa^2+q^2},\qquad
Y(\kappa)=\omega C+\frac{q\kappa^2}{\kappa^2+q^2}.
\]

Therefore \(\phi(\kappa)=\arg Z=\arctan(Y/X)\) is in \((0,\pi/2)\). Eliminating \(\kappa\) gives the claimed **exact** semicircle

\[
\boxed{(X-\lambda)^2+(Y-\omega(C+D/2))^2=(\omega D/2)^2,\quad X>\lambda.}
\]

Both excluded endpoints correspond respectively to \(\kappa\downarrow0\) and \(\kappa\to\infty\). In fact \(\kappa\mapsto Z\) is an injective fractional-linear map, so the open arc is traversed once.

**2. Unique interior phase fold.** Since the arctangent is strictly increasing, the sign of \(\phi'(\kappa)\) is the sign of \(Y'X-YX'\). Direct differentiation and common-denominator cancellation give

\[
\phi'(\kappa)=
\frac{\omega^3D^2\left((C+D)\kappa^2+2\lambda D\kappa-\omega^2CD^2\right)}
{(\kappa^2+\omega^2D^2)^2\bigl(X(\kappa)^2+Y(\kappa)^2\bigr)}.
\]

The numerator's bracket is strictly increasing for \(\kappa\ge0\), negative at zero and unbounded above. Solving its unique positive zero gives exactly \(\kappa_*\) as stated. This proves strict decrease then strict increase (and excludes plateaus or additional turning points). The endpoint limits of \(Z\) give \(\phi_0\) and \(\phi_\infty\); the strict inequalities follow from the derivative signs and \(C,D,\lambda,\omega>0\). Counting preimages separately on the decreasing and increasing branches proves every phase multiplicity assertion, including the asymmetric exclusion of the \(\kappa=0\) and \(\kappa=\infty\) boundaries.

**3. Algebraic inversion and gain separation.** For a candidate phase \(\phi\in(0,\pi/2)\), put \(t=\tan\phi\). The equation \(Y/X=t\) is exactly

\[
\left(\omega(C+D)-t\lambda\right)\kappa^2
-t\omega^2D^2\kappa+
\left(\omega C-t\lambda\right)\omega^2D^2=0.
\]

The quadratic is only an algebraic restatement of the already proved multiplicities; no numerical root count is used as proof. If two distinct positive exchange coefficients gave both the same phase and the same gain, their complex transfers, hence their inverse transfers, would coincide. But the fractional-linear expression for \(Z\) is injective in \(\kappa>0\), contradiction. Thus phase plus calibrated amplitude removes this two-way degeneracy.

**4. The sharp frequency window for a known coefficient interval.** The derivative changes sign inside \((a,b)\) exactly when its increasing bracket is negative at \(a\) and positive at \(b\). Solving the two strict inequalities for \(\omega>0\) gives \(\Omega(a)<\omega<\Omega(b)\). In that case two distinct sufficiently nearby points on opposite sides of the interior minimum have the same lag, so the map is noninjective. Otherwise its derivative has one sign in the interval interior, making the map strictly monotone even if the derivative vanishes at an endpoint. This proves both necessity and sufficiency, with strict frequency endpoints.

## Verification

The standalone \(\texttt{verify.py}\) uses only Python's standard library and independently checks the exact rational semicircle identity, inverse response, derivative factorization and derivative signs across 19,000 reproducibly sampled positive rational parameter tuples. It checks the strict frequency-window equivalence on 18,000 further rational parameter sets and replays two exact phase-alias certificates. The replay output was \(\texttt{VERIFY_OK assertions=149742}\). These finite checks corroborate the displayed identities but **do not substitute for the preceding all-positive-parameters proof**.

An exact two-coefficient certificate is \(\lambda=C=\omega=1\), \(D=3\), with \(\kappa_1=1/2\) and \(\kappa_2=3/2\):

\[
Z(1/2)=\frac{55+40i}{37},\qquad
Z(3/2)=\frac{11+8i}{5},\qquad
\tan\phi(1/2)=\tan\phi(3/2)=\frac8{11}.
\]

The inverse-transfer squared magnitudes are \(125/37\) and \(37/5\), proving different gains at identical phases. The fold is \(\kappa_*=3(\sqrt5-1)/4\) and lies strictly between those coefficients.

As a scale illustration (not a calibrated physical inference), take \(\lambda=1.3\), \(C=8\), \(D=100\), a candidate exchange interval \([0.5,1.2]\), and a century-period forcing \(\omega=2\pi/100\) in consistent annual units. The exact interval formula gives a noninjective period window of approximately \((82.1911,141.8323)\) years. Within it, \(\kappa=0.7\) and approximately \(1.0935182\) have the same modeled lag, approximately \(16.2298\) degrees. These numerical values are illustrations of the proved deterministic model, not measurement-based estimates.

## Relationship to prior work

Held et al. (2010) introduced the coupled fast/slow climate response and its two-reservoir interpretation. Geoffroy et al. (2013, part I), in particular Appendix D and equations (D1)–(D9), **already provide the exact harmonic transfer, frequency gain and phase for fixed model parameters**. None of those formulas is claimed new. The distinct result proved here holds \(\omega\) fixed and varies the *interlayer coupling*, obtaining the open-semicircle transfer geometry, its one-and-only phase fold, complete positive-parameter alias multiplicity, and a sharp frequency-design interval for a prescribed coupling range. Fredriksen and Rypdal (2017) analyze stochastic multibox impulse responses and frequency-domain variability rather than phase-only coupling recovery. Cummins, Stephenson and Stott (2020) study full time-series and flux-based statistical parameter estimation with potentially more boxes, not phase-only identification at a single frequency; those richer observations are compatible with the present phase-only obstruction.

The mathematical classification may also admit a classical interpretation in two-node thermal or electrical equivalent circuits. A prior equivalent parameter-varying result in that wider literature is a remaining priority risk, despite the explicit comparisons reported here.

## Limitations

The theorem assumes \(\lambda,C,D\) and forcing frequency and phase are known; allowing them to vary introduces additional ambiguities and is not solved. An exact mathematical phase collision does not imply that realistic phase observations are accurate enough to distinguish models. The oscillatory forcing is idealized and the response is linear, deterministic and globally spatially aggregated. The result is not an empirical statement about observed climate change, nor a claim about stochastic inference, all parameter identifiability, or nonlinear/ocean-circulation climate dynamics. Historical priority against all thermal-network and circuit literature is not independently certified.

## References

1. Held, I. M., Winton, M., Takahashi, K., Delworth, T., Zeng, F., and Vallis, G. K. (2010). *Probing the Fast and Slow Components of Global Warming by Returning Abruptly to Preindustrial Forcing*. Journal of Climate 23, 2418–2427. https://doi.org/10.1175/2009JCLI3466.1 . Public online date verified as 2010-05-01.
2. Geoffroy, O., Saint-Martin, D., Olivié, D. J. L., Voldoire, A., Bellon, G., and Tytéca, S. (2013). *Transient Climate Response in a Two-Layer Energy-Balance Model. Part I: Analytical Solution and Parameter Calibration Using CMIP5 AOGCM Experiments*. Journal of Climate 26, 1841–1857, Appendix D. https://doi.org/10.1175/JCLI-D-12-00195.1 . Lawful full text: https://www.umr-cnrm.fr/old/IMG/pdf/2box_i.pdf .
3. Fredriksen, H.-B., and Rypdal, M. (2017). *Long-Range Persistence in Global Surface Temperatures Explained by Linear Multibox Energy Balance Models*. Journal of Climate 30, 7157–7168. https://doi.org/10.1175/JCLI-D-16-0877.1 . Open preprint: https://arxiv.org/pdf/1701.07355 .
4. Cummins, D. P., Stephenson, D. B., and Stott, P. A. (2020). *Optimal Estimation of Stochastic Energy Balance Model Parameters*. Journal of Climate 33, 7909–7926. https://doi.org/10.1175/JCLI-D-19-0589.1 . Lawful full text: https://eprints.whiterose.ac.uk/id/eprint/217829/1/clim-jcliD190589.pdf .
