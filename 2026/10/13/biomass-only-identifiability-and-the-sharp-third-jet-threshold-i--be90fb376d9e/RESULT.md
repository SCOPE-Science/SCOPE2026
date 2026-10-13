# Biomass-only identifiability and the sharp third-jet threshold in the nonspatial Klausmeier model

## Finding

Consider the nonspatial normalized Klausmeier model
\[
\dot w=a-(1+u^2)w,\qquad \dot u=u^2w-mu,
\]
where \(u\) denotes plant biomass, \(w\) water availability, and \(a,m>0\) are unknown constant rainfall-input and vegetation-mortality parameters. All other coefficients are fixed by normalization. Only the exact biomass function \(u(t)\), not \(w(t)\), is observed.

**Theorem (complete positive-output dichotomy and sharp local derivative order).** On any nonempty open observation interval, if \(u>0\) is nonconstant, biomass alone uniquely determines \(a,m\) and the hidden water trajectory. A positive constant biomass \(u=s\) instead determines exactly the ratio \(a/m=s+s^{-1}\), allowing every choice \(m>0\) with \(a=m(s+s^{-1})\) and \(w=m/s\). The identically zero biomass output determines neither parameter.

Define the two biomass-derived functions
\[
B(t)=u(t)+\frac1{u(t)}-\frac{\dot u(t)}{u(t)^2},\qquad
A(t)=\frac{d}{dt}\left(\frac{\dot u(t)}{u(t)^2}\right)
 +(1+u(t)^2)\frac{\dot u(t)}{u(t)^2}.
\]
For every positive nonconstant output \(B\) is nonconstant, and for any \(t_1,t_2\) with \(B(t_1)\ne B(t_2)\) the reconstruction is
\[
\boxed{\quad m=\frac{A(t_1)-A(t_2)}{B(t_2)-B(t_1)},\quad
 a=A(t_1)+mB(t_1),\quad w(t)=\frac{\dot u(t)+m u(t)}{u(t)^2}.\quad}
\]
At a single instant, even a complete second-order derivative jet \((u,\dot u,\ddot u)\) never identifies both parameters. A third-order jet determines them if and only if \(\dot B\ne0\) at that instant, through
\[
\boxed{\quad m=-\frac{\dot A}{\dot B},\qquad a=A+mB.\quad}
\]
For any nonconstant positive trajectory the times where \(\dot B=0\) form a discrete subset of the observation interval. These exceptional instants may occur off equilibrium.

## Assumptions and scope

The vector field is the two-dimensional **ordinary** differential equation above, not its spatial PDE extension. Parameters \(a,m\) are constant and positive, all nondimensional units and the water-loss coefficient are known, and the unobserved water initial condition is unrestricted apart from \(w\ge0\). Observations are exact, continuous in time, and have the derivatives used in the formulas; because the vector field is polynomial, all its solutions are analytic on their existence intervals. An initial positive biomass stays positive on every finite existence interval; an initially zero biomass stays zero. The conclusions concern identifiability in the exact mathematical model, not numerical estimation from noisy measurements.

## Proof

**1. Input–output equation.** For \(u>0\), the biomass equation gives
\[
w=\frac{\dot u+mu}{u^2}=\frac{\dot u}{u^2}+\frac m u.
\]
Substituting this expression and its time derivative into \(\dot w+(1+u^2)w=a\) yields identically
\[
\boxed{a=A(t)+mB(t).}
\]
This identity is valid at every time of any positive solution, without assuming that the biomass is monotone or that the hidden water is measured.

**2. Nonconstant biomass forces nonconstant \(B\).** Suppose to the contrary that \(B(t)=b\) throughout an interval. By the definition of \(B\),
\[
\dot u=u^3-bu^2+u.
\]
Consequently \(\dot u/u^2=u-b+u^{-1}\), and direct differentiation gives
\[
A(t)=2u(t)\bigl(u(t)^2-bu(t)+1\bigr).
\]
But \(a=A+mb\) requires \(A\) to be constant. A nonconstant continuous \(u\) assumes an interval of values; the nonconstant polynomial \(2z(z^2-bz+1)\) cannot be constant on any nondegenerate interval. Therefore \(u\) must be constant, proving the contrapositive. If \(u\) is nonconstant, choose any two times of unequal \(B\) to obtain the displayed unique reconstruction. No distinct positive parameter pair can generate the same full biomass observation.

**3. Equilibria and desert output.** When \(u=s>0\) is constant, \(\dot u=0\) enforces \(w=m/s\), and \(\dot w=0\) enforces \(a=m(s+s^{-1})\). Conversely every \(m>0\) with this relation supplies the same constant biomass \(s\), so the ratio and no individual parameter are identifiable. If \(u=0\), then \(\dot u=0\) identically and \(\dot w=a-w\); any positive \(a,m\) allows the zero biomass output. Because \(\dot u=u(uw-m)\), nonnegative biomass trajectories cannot pass from \(u=0\) to \(u>0\) or vice versa in finite time.

**4. Sharp finite-jet threshold.** Fix any time with positive biomass and abbreviate its input–output functions by \(A,B\). Given a true state \((u,w,a,m)\), for sufficiently small nonzero real \(\varepsilon\) define a second admissible local initial-value problem by
\[
m_\varepsilon=m+\varepsilon,\qquad
w_\varepsilon=w+\frac\varepsilon u,\qquad
a_\varepsilon=a+\varepsilon B.
\]
The resulting solutions have exactly the same \(u,\dot u,\ddot u\) at that instant, as follows directly from the biomass equation and \(a=A+mB\). Positivity persists for sufficiently small \(\varepsilon\). Thus a second-order biomass jet never globally identifies both parameters.

Differentiating \(a=A+mB\) along an actual trajectory gives \(0=\dot A+m\dot B\). Since \(\dot B\) depends only on \(u,\dot u,\ddot u\) and \(\dot A\) additionally on \(u^{(3)}\), the third jet identifies the two parameters when \(\dot B\ne0\). When \(\dot B=0\), the perturbation above also matches the third jet: its third-biomass-derivative difference is precisely \(-\varepsilon u^2\dot B=0\). Hence the stated condition is both necessary and sufficient.

The analytic function \(\dot B\) cannot vanish identically on a nonconstant positive solution by Step 2. Therefore its zeros are isolated. In particular almost every interior observation instant admits third-jet reconstruction. The exceptional-set qualification is necessary: at \((a,m,u,w)=(6,1,2,1)\), one has \(\dot u=2\) but \(\dot B=0\), while \(\ddot B=20\). This initial-value problem is positive and nonstationary, yet its instantaneous third jet is singular.

## Verification

The self-contained symbolic checker `verify_klausmeier.py` uses SymPy to recompute the first three Lie derivatives of the biomass, verify \(A+mB=a\) and \(\dot A+m\dot B=0\), check the two-jet perturbation and the exact third-jet difference, verify the polynomial obstruction and the equilibrium family, and evaluate nonsingular and singular positive rational initial states. Run it with `python verify_klausmeier.py` after installing SymPy. Its expected output begins `VERIFY_OK`. The proof, not a finite set of numerical examples, establishes the all-trajectory quantifiers.

## Relationship to prior work

Klausmeier's 1999 vegetation–water model and subsequent nondimensionalizations supply the biological equations. Köhnke and Malchow (2017) derive the model's nonspatial equilibria, but do not establish identifiability from the unobserved-water experiment. Cruz de la Cruz and collaborators (2023, Section 4.2) study Bayesian inversion for a generalized fractional Klausmeier model with an observation vector involving both water and biomass, not the exact single-output differential reconstruction here. A published 2026 analysis of the nonspatial model gives full-state trajectory identifiability and equilibrium-only Fisher correlation; **full-state observability does not imply identifiability with water hidden**. Beer, Kuehn and Piazzola (2026) investigate parameter-estimation difficulties near a fold. Related inverse-source results for spatial reaction–diffusion systems use different observation models. The present claim is solely the positive biomass-only trichotomy and its minimal instantaneous derivative order, not the source model, its equilibria, general structural-identifiability principles, or noise-robust estimation.

## Limitations

Reconstruction assumes exact biomass derivatives through order two at two instants, or order three at a nonsingular instant; differentiation can amplify observation noise. Near an equilibrium or where \(\dot B\) is small, numerical inversion can be arbitrarily ill-conditioned despite structural uniqueness. Constant forcing and both known unit normalizations are essential. There is no claim for spatially varying biomass, unknown additional coefficients, variable rainfall, discrete/noisy samples, experimental feasibility, or an independent external certification. Full text of the original 1999 publication and of a directly relevant 2026 preprint was not available for complete comparison, so undiscovered stronger prior coverage remains a literature risk.

## References

1. C. A. Klausmeier, *Regular and irregular patterns in semiarid vegetation*, Science **284** (1999), 1826–1828, doi:10.1126/science.284.5421.1826.
2. M. C. Köhnke and H. Malchow, *Impact of Parameter Variability and Environmental Noise on the Klausmeier Model of Vegetation Pattern Formation*, Mathematics **5** (2017), 69, doi:10.3390/math5040069.
3. M. P. Cruz de la Cruz et al., *On a generalized Klausmeier model*, Mathematical Biosciences and Engineering **20** (2023), 16447–16470, doi:10.3934/mbe.2023734.
4. L. Beer, C. Kuehn and C. Piazzola, *The Role of Bifurcations in Parameter Estimation: A UQ Analysis of the Non-spatial Klausmeier Model*, arXiv:2609.18231 (2026).
5. *Exact identifiability dichotomy and Fisher-correlation floor in the non-spatial Klausmeier model*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-klausmeier-identifiability-fisher-correlation-floor--962dc48d4a2e .
6. X. Luo, M. Yamamoto and J. Cheng, *Inverse source problems with reduced interior data for a coupled reaction-diffusion system*, Inverse Problems and Imaging (2026), doi:10.3934/ipi.2026050.
