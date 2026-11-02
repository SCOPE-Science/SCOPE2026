# Three strict invasion levels for six-block seasonal SEIR calendars

## Finding
Consider the linear disease-free exposed–infectious subsystem of a seasonally forced SEIR population. In any six-block period containing exactly three high-contact and three low-contact blocks, with fixed positive lengths for each contact type, the invasion multipliers take exactly three strictly ordered values. With the physically chronological schedule written from left to right, their order is
\[
\rho(\mathrm{HHHLLL})<\rho(\mathrm{HHLHLL})=\rho(\mathrm{HHLLHL})<\rho(\mathrm{HLHLHL}).
\]
The equality classes include all cyclic rearrangements; every one of the twenty labeled six-block schedules belongs to exactly one of the three levels (class sizes six, twelve, and two respectively). In particular, strict alternation maximizes linear invasion, whereas clustering minimizes it. When low contact is subcritical, the three classes have strictly separated critical high-contact rates; hence the three contact arrangements can give different invasion verdicts despite identical durations and contact levels.

## Assumptions and scope
Fix progression rate \(\sigma>0\), removal rate \(\gamma>0\), transmission rates \(0<\beta_\mathrm{L}<\beta_\mathrm{H}\), and block durations \(\tau_\mathrm{L},\tau_\mathrm{H}>0\). Throughout every low/high block, the infection-level linearization is
\[
\frac{d}{dt}\binom{E}{I}=G_\beta\binom{E}{I},\qquad G_\beta=\begin{pmatrix}-\sigma&\beta\\\sigma&-\gamma\end{pmatrix}.
\]
Let \(L=\exp(\tau_\mathrm{L}G_{\beta_\mathrm{L}})\), \(H=\exp(\tau_\mathrm{H}G_{\beta_\mathrm{H}})\). Each word has three copies each of \(H\) and \(L\); the corresponding monodromy is the product of those matrices. Its Perron eigenvalue \(\rho\) is the multiplier over the full six-block period, and local invasion occurs when \(\rho>1\). Reversing the chronological convention transposes the ordering of factors but leaves the three classes and spectra unchanged in dimension two. This is a deterministic disease-free linearization; nonlinear peak prevalence is not claimed.

## Proof
**1. Universal two-dimensional trace identities.** For arbitrary real \(2\times2\) matrices \(H,L\), write \(K=-\det(HL-LH)\). Cayley–Hamilton, \(X^2-\operatorname{tr}(X)X+\det(X)I=0\), gives the exact polynomial identities
\[
\begin{aligned}
\operatorname{tr}(H^2LHL^2)-\operatorname{tr}(H^3L^3)&=\operatorname{tr}(H)\operatorname{tr}(L)K,\\
\operatorname{tr}((HL)^3)-\operatorname{tr}(H^2LHL^2)&=\operatorname{tr}(HL)K.
\end{aligned}
\]
For completeness, expanding \(H^2=\operatorname{tr}(H)H-\det(H)I\) and its \(L\) counterpart into each difference reduces it to \(2\operatorname{tr}((HL)^2)-\operatorname{tr}(HL)^2\) and the scalar invariants; substituting \(\det(HL-LH)\) gives the displayed equations. This identity is also checked symbolically as a polynomial identity in eight independent matrix entries in `verify.py`. A direct enumeration of the twenty words, using cyclic trace invariance and Cayley–Hamilton, yields trace class sizes six, twelve and two; the middle representatives \(H^2LHL^2\) and \(H^2L^2HL\) have equal traces. Each word has the same determinant \(\det(H)^3\det(L)^3\).

**2. Strict sign special to SEIR.** Put
\[
\kappa_b=\sqrt{(\sigma-\gamma)^2/4+\sigma b},\quad
u_b(t)=e^{-(\sigma+\gamma)t/2}\frac{\sinh(\kappa_b t)}{\kappa_b}>0.
\]
Since every \(2\times2\) exponential is affine in its generator, \(e^{tG_b}=v_b(t)I+u_b(t)G_b\) for a scalar \(v_b(t)\). Hence
\[
[H,L]=u_{\beta_\mathrm{H}}(\tau_\mathrm{H})
 u_{\beta_\mathrm{L}}(\tau_\mathrm{L})[G_{\beta_\mathrm{H}},G_{\beta_\mathrm{L}}].
\]
Direct multiplication gives \(\det[G_{\beta_\mathrm{H}},G_{\beta_\mathrm{L}}]=-\sigma^2(\beta_\mathrm{H}-\beta_\mathrm{L})^2\), so
\[
K=\sigma^2(\beta_\mathrm{H}-\beta_\mathrm{L})^2u_{\beta_\mathrm{H}}(\tau_\mathrm{H})^2u_{\beta_\mathrm{L}}(\tau_\mathrm{L})^2>0.
\]
Both exponential matrices have strictly positive entries because their generators are irreducible Metzler matrices. Thus \(\operatorname{tr}H\), \(\operatorname{tr}L\), and \(\operatorname{tr}(HL)\) are positive, giving the strict trace inequalities of Step 1. The determinant of every six-block monodromy equals \(D=e^{-3(\sigma+\gamma)(\tau_\mathrm{H}+\tau_\mathrm{L})}>0\). For any strictly positive \(2\times2\) matrix with trace \(T\) and determinant \(D\), its Perron eigenvalue equals \( (T+\sqrt{T^2-4D})/2\), strictly increasing with \(T\) for fixed \(D\). This proves the three-level statement for all positive parameters, including unequal high/low block durations.

**3. Three distinct invasion boundaries.** Additionally assume \(0<\beta_\mathrm{L}<\gamma\). Hold \(\sigma,\gamma,\tau_\mathrm{L},\tau_\mathrm{H},\beta_\mathrm{L}\) fixed and vary \(b=\beta_\mathrm{H}\) over \(b\ge\beta_\mathrm{L}\). Each positive monodromy increases strictly entrywise, hence strictly in its Perron root, with \(b\): the variation-of-constants identity
\[
\partial_b e^{tG_b}=\int_0^t e^{(t-s)G_b}\begin{pmatrix}0&1\\0&0\end{pmatrix}e^{sG_b}\,ds
\]
has strictly positive entries for \(t>0\). At \(b=\beta_\mathrm{L}\), every word equals a constant-rate exponential with total duration \(3(\tau_\mathrm{H}+\tau_\mathrm{L})\), whose Perron root is below one because \(\beta_\mathrm{L}<\gamma\). As \(b\to\infty\), entries of the high-contact exponential and hence every positive word tend to infinity, forcing \(\rho\to\infty\). Each class therefore crosses one at a unique finite \(b_*\); strict multiplier inequalities at every \(b>\beta_\mathrm{L}\) imply \(b_*^{\mathrm{A}}<b_*^{\mathrm{M}}<b_*^{\mathrm{C}}\) for alternating, middle and clustered schedules respectively. The inequalities are strict and no periodic nonlinear endemic-equilibrium claim is made.

## Verification
Run `python verify.py` with Python 3, NumPy, SciPy and SymPy. It verifies the two trace differences symbolically for generic matrices, all twenty word traces, and the generator commutator determinant. Ninety-six seeded positive-parameter numerical tests reconstruct monodromy matrices using SciPy exponentials; these tests are supplementary, not a replacement for the analytic argument. At \(\sigma=\gamma=\tau_\mathrm{H}=\tau_\mathrm{L}=1\) and \(\beta_\mathrm{L}=1/5\), the high-contact thresholds are approximately \(2.10253825262173\) (clustered), \(1.96812746118054\) (middle), and \(1.88436935452332\) (alternating). At \(b=1.9\) only the alternating schedule invades; at \(b=2\), alternating and middle invade, while clustering does not.

## Relationship to prior work
Bacaër and Abdurahman (2008) studied the periodic epidemic threshold and emerging-disease resonance for SEIR and related contact-forcing models, including their linearization and sinusoidal-contact examples. The current result instead gives a necessary-and-sufficient *complete six-block word ordering* at fixed high/low contact exposures and a strict order of invasion thresholds. Diedrichs, Isihara and Buursma (2014; first online 2013) investigated calendar effects on recurrent nonlinear epidemic peaks, a different objective. Classical Cayley–Hamilton trace identities and cyclic-word reductions are known matrix techniques and are not claimed as inventions here. What is asserted here is the SEIR-specific strict sign and the resulting complete calendar/invasion classification. Published papers and mathematical-record searches inspected to the extents described in the accompanying review have not established this combined assertion; historical priority remains provisional.

## Limitations
This is an exact linearized disease-free result for one homogeneous SEIR model with exponential-stage residence times. It assumes constant positive contact levels within each of six deterministic blocks, equal durations within each level, and exactly three blocks of each kind. It does not assert the same ordering for arbitrary nonlinear outbreak peaks, heterogeneous populations, more than two infected states, correlated controls, or stochastic disease transmission. The algebraic trace identities are classical, and an inaccessible full paper on calendar effects or a stronger general two-matrix theorem could imply this particular specialization; formal historical uniqueness cannot be certified. All conclusions use positive infection and stage rates and strict contrast; at equality of contact levels the three values coincide.

## References
1. N. Bacaër and X. Abdurahman, “Resonance of the epidemic threshold in a periodic environment,” *Journal of Mathematical Biology* 57 (2008), 649–673; published online 7 May 2008; DOI 10.1007/s00285-008-0183-1; PMID 18461330.
2. D. R. Diedrichs, P. A. Isihara and D. D. Buursma, “The schedule effect: can recurrent peak infections be reduced without vaccines, quarantines or school closings?” *Mathematical Biosciences* 248 (2014), 46–53; first online 19 December 2013; DOI 10.1016/j.mbs.2013.12.004; PMID 24361495.
3. J. E. Cohen, S. Friedland, T. Kato and F. P. Kelly, “Eigenvalue inequalities for products of matrix exponentials,” *Linear Algebra and its Applications* 45 (1982), 55–95. https://pure.iiasa.ac.at/id/eprint/1854/ . This general matrix literature provides context for matrix-product comparisons, not an asserted identical six-block classification.
