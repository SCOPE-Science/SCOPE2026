# A unique skewness reversal in a harmonically confined asymmetric run-and-tumble particle under position-only resetting

## Finding
For an asymmetric two-velocity active particle in a harmonic trap, independent Poisson resetting of **position but not orientation** changes the sign of stationary spatial skewness **exactly once** as the resetting rate increases. The unique positive critical rate exists for every strictly asymmetric orientation chain, without needing a special range of trap strengths or flip rates.

For \(g>0\) and \(z\in(0,1)\), the exact dimensionless critical resetting rate is the sole positive root \(t_*\) of the quartic
\[
P(t)=12(z-1)+(-zg^2-6zg+3g+28z-30)t
 +(zg^2-5zg+6g+23z-24)t^2
 +((3-z)g+8z-6)t^3+zt^4.
\]
At \(t<t_*\) the stationary centered third moment has sign \(-\operatorname{sign}(m)\); at \(t>t_*\) it has sign \(\operatorname{sign}(m)\). Thus the asymmetric orientational bias and spatial skewness necessarily oppose each other before resetting becomes strong, but agree afterward.

## Assumptions and scope
Let \(X\in\mathbb R\) obey \(\dot X=-\kappa X+vS\), with \(\kappa,v>0\). The orientation \(S\in\{-1,1\}\) flips from \(+1\) to \(-1\) at rate \(\alpha>0\), and from \(-1\) to \(+1\) at rate \(\beta>0\). At rate \(r\ge0\), independent position-only resets set \(X\mapsto0\) but leave \(S\) unchanged. The process has a unique stationary law; since \(|X|\le v/\kappa\) in stationarity, every moment exists. Define
\[
m=\frac{\beta-\alpha}{\alpha+\beta},\quad g=\frac{\alpha+\beta}{\kappa},\quad z=m^2,\quad t=\frac r\kappa.
\]
The theorem assumes \(\alpha\ne\beta\), hence \(0<z<1\). The symmetrically flipping case has zero third centered moment at every reset rate and is excluded from the sign-reversal assertion.

## Proof
The stationary generator gives coupled equations for \(a_n=\mathbb E[X^n]\), \(b_n=\mathbb E[SX^n]\), beginning at \(a_0=1\), \(b_0=m\):
\[
(n\kappa+r)a_n=nvb_{n-1},\qquad
(n\kappa+r+\alpha+\beta)b_n=nv a_{n-1}+(\beta-\alpha)a_n.
\]
Here the second identity uses the telegraph-generator equality \(\mathcal LS=-(\alpha+\beta)S+(\beta-\alpha)\), including the unchanged orientation at reset. Solving these triangular equations for \(n=1,2,3\) and forming \(\mu_3=a_3-3a_2a_1+2a_1^3\) yields the exact expression
\[
\mu_3=\frac{2mv^3P(t)}{\kappa^3(1+t)^3(2+t)(3+t)(g+1+t)(g+2+t)}.
\]
Every denominator factor is strictly positive on the stated domain. The quartic's constant coefficient is \(12(z-1)<0\) and leading coefficient is \(z>0\). Write \(c_j\) for the coefficient of \(t^j\). The exact identity
\[
c_2-c_1=2zg^2+(3+z)g+6-5z>0
\]
shows that \(c_1>0\) implies \(c_2>0\). If \(z\ge3/4\), then \(c_3=(3-z)g+8z-6>0\). If \(0<z<3/4\), set \(g_0=(6-8z)/(3-z)>0\); then \(c_3\le0\) implies \(0<g\le g_0\). As \(c_2(g)=zg^2+(6-5z)g+23z-24\) is strictly increasing for \(g\ge0\), and
\[
c_2(g_0)=\frac{47z^3-60z^2+117z-108}{(3-z)^2}<0,
\]
we have \(c_2>0\) only if \(c_3>0\). The numerator in the preceding fraction is negative because \(47z^3-60z^2=z^2(47z-60)<0\) and \(117z-108<0\) for \(0<z<3/4\). Consequently the coefficient sequence \(c_0,c_1,c_2,c_3,c_4\) can change sign only once, even when zero coefficients are omitted. Descartes' rule therefore gives exactly one positive root counted with multiplicity: existence also follows from \(P(0)<0\), \(P(t)\to+\infty\), and continuity. Its multiplicity is one and the sign switches there.

At zero resetting the closed expression simplifies to
\[
\mu_3(0)=-\frac{4mv^3(1-m^2)}{\kappa^3(g+1)(g+2)},
\]
while at strong resetting \(\mu_3(r)\sim2m^3v^3/r^3\). The variance is positive for both flip rates positive, so standardized skewness has the same sign. If \(m=0\), the model has symmetry \((X,S)\mapsto(-X,-S)\), giving zero odd centered moments.

## Verification
The included `check_moments.py` symbolically derives the three stationary moment recurrences, independently recomputes the central third moment and verifies the quartic identity exactly in SymPy. It also checks the coefficient-comparison formula, the auxiliary threshold substitution, and roots in several admissible parameter cases. Numerical root finding is illustrative; the proof of uniqueness is algebraic and does not depend on finite computations. Execute `python check_moments.py` with SymPy installed.

## Relationship to prior work
Harmonic trapping of run-and-tumble particles and stationary non-Boltzmann effects have been studied, including Wang et al. (2014). Evans and Majumdar (2018) analyze an unconfined, symmetric run-and-tumble process with various resetting protocols, including position-only reset. Smith et al. (2022) study harmonic trapping with symmetric orientation dynamics and resetting. Olsen (2023) derives moments under resetting for a harmonically confined run-and-tumble particle with symmetric telegraph dynamics; the present asymmetric, orientation-preserving process and its universal single-skewness-reversal classification are not established by the accessible descriptions of those models. The exact second and third stationary moment calculations alone do not establish novelty: the assessed contribution is the all-parameter strict one-crossing result for asymmetric telegraph forcing with position-only reset.

## Limitations
The theorem is restricted to two-state Markov orientation, strictly positive flip rates, harmonic drift, and independent resetting of position to the origin while preserving orientation. It gives a sign phase classification of the stationary marginal, not its complete distribution or a first-passage theorem. No uniform behavior as \(\alpha\) or \(\beta\) vanishes is claimed. Some closely relevant complete primary texts were inaccessible; their possible stronger implications represent residual priority risk. Independent external validation has not been performed.

## References
1. Z. Wang, H. Chen, Y.-J. Sheng and H.-K. Tsao, “Diffusion, sedimentation equilibrium, and harmonic trapping of run-and-tumble nanoswimmers,” *Soft Matter* **10** (2014), 3209–3217, DOI: 10.1039/C3SM53163E. First published 2014-01-23.
2. M. R. Evans and S. N. Majumdar, “Run and tumble particle under resetting: a renewal approach,” *J. Phys. A* **51** (2018), 475003, arXiv:1808.06450.
3. N. R. Smith, P. Le Doussal, S. N. Majumdar and G. Schehr, “Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions,” *Phys. Rev. E* **106** (2022), 054133, arXiv:2207.10445.
4. K. S. Olsen, “Steady-state moments under resetting to a distribution,” arXiv:2310.04840 (2023).
