# A strict renewal-variability window and positive fourth cumulants under nearest-site resetting

## Finding

Consider one-dimensional Brownian motion with generator \(D\partial_{xx}\) and instantaneous Poisson resets of rate \(r\) to the *nearest* point of the regular lattice \(\ell\mathbb Z\). For every \(D,\ell,r>0\), start at the lattice point \(X_0=0\) and use the unwrapped real-line coordinate. Let \(\tau\) be the time until the first arrival at an adjacent lattice site \(\pm\ell\), either by diffusion or by a reset. Define \(\alpha=(\ell/2)\sqrt{r/D}\), \(s=\sinh\alpha\), and \(c=\cosh\alpha\).

The squared coefficient of variation of this nearest-neighbor renewal time is
\[
 \operatorname{CV}^2(\tau)=1+\frac{s-\alpha}{s^3}-\frac{\alpha}{2s},
 \qquad \boxed{\frac23<\operatorname{CV}^2(\tau)<1}.
\]
Both bounds are sharp limits: the lower is approached as \(r\downarrow0\), the upper as \(r\uparrow\infty\), with \(D,\ell\) fixed. Neither is attained for positive \(r\).

Write \(\kappa_4(X_T)=\mathbb E[X_T^4]-3\mathbb E[X_T^2]^2\), and
\[
 F(\alpha)=2\sinh^3\alpha+6\sinh\alpha-3\alpha\sinh^2\alpha-6\alpha.
\]
Then the exact long-time fourth-cumulant growth coefficient is
\[
 \boxed{\lim_{T\to\infty}\frac{\kappa_4(X_T)}T
 =\frac{r\ell^4\cosh\alpha}{4\sinh^5\alpha}\,F(\alpha)>0.}
\]
Thus *every strictly positive nearest-site resetting rate* yields positive asymptotic excess kurtosis, even within the previously identified diffusion-enhancement region. In contrast, unreset Brownian motion has identically zero fourth cumulant. The effective diffusivity, included here to normalize the result, is the previously known expression
\[
 D_{\mathrm{eff}}=D\alpha^2\operatorname{csch}(\alpha)\coth(\alpha).
\]
In particular,
\[
 \lim_{T\to\infty}T\left(\frac{\mathbb E[X_T^4]}{\mathbb E[X_T^2]^2}-3\right)
 =\frac{r\ell^4\cosh\alpha\,F(\alpha)}{16D_{\mathrm{eff}}^2\sinh^5\alpha}>0.
\]
At the published diffusion-optimal \(\alpha\approx1.6061153\), the coefficient equals approximately \(0.07048228\,\ell^2/D\). The small-rate asymptotic is \(\kappa_4(X_T)/T\sim r\ell^4/80\); for large rate it is asymptotic to \(r\ell^4 e^{-\alpha}\). The comparisons hold with positive \(D\) and \(\ell\) fixed.

## Assumptions and scope

The model has ordinary Brownian variance \(2Dt\) between events, a spatially homogeneous rate-\(r\) Poisson clock independent of Brownian motion, instantaneous jumps to the closest site of \(\ell\mathbb Z\), and no waiting time at a site. Reset-site ties occur with probability zero. The initial position is a lattice site, and the observed coordinate is the unwrapped displacement, not a bounded coordinate on a finite circle. All parameters \(D,\ell,r\) are strictly positive. The fourth cumulant and coefficient of variation use their ordinary centered definitions. Limits in time hold for each fixed parameter triple, not uniformly in joint scaling of parameters and time.

## Proof

**1. Regeneration.** Beginning at any site \(j\ell\), stop the path upon first reaching one of \((j-1)\ell\) and \((j+1)\ell\), whether continuously or by a resetting jump. Before this time the path remains within one site spacing of \(j\ell\). A reset from the central Voronoi interval returns to \(j\ell\); a reset from either outer half of this two-neighbor interval completes the excursion. By the strong Markov property and translation symmetry, these waiting times are independent and identically distributed. Reflection symmetry gives equal probabilities for the two directions and, importantly, independence of the \(\pm\ell\) displacement from its waiting time.

**2. First-passage transform.** For \(z\ge0\) let \(u_z(x)\) be the Laplace transform of the time to reach an adjacent site from position \(x\) between \(-\ell\) and \(+\ell\), and write \(f(z)=u_z(0)\). Symmetry imposes \(u'_z(0)=0\). The backward equations on the positive half-interval are
\[
 D u''_z=(z+r)u_z-rf(z)\quad(0<x<\ell/2),\qquad
 D u''_z=(z+r)u_z-r\quad(\ell/2<x<\ell),
\]
with \(u_z(\ell)=1\) and continuity of value and derivative at \(x=\ell/2\). The unique solution gives
\[
 f(z)=\frac{z+r\cosh a_z}{r\cosh a_z+z\cosh(2a_z)},
 \qquad a_z=\frac\ell2\sqrt{\frac{z+r}{D}}.
\]
This transform is also Eq. (13) in the published Alston--Bertrand model, and the equivalent equation in its original preprint. Direct matching of the two constant-coefficient ODEs verifies the expression independently. Compact-interval absorption gives \(\tau\) a continuous distribution and a finite exponential moment in a neighborhood of zero.

**3. Renewal pole and cumulants.** Denote \(\mu=\mathbb E\tau\) and \(m_2=\mathbb E\tau^2\). The renewal-site displacement has independent fair \(\pm\ell\) steps. Its moment generating function has a renewal denominator \(1-\cosh(k\ell)f(z)\); including the bounded within-excursion displacement changes only its analytic numerator and not the dominant pole. For real \(k\) near zero, the pole \(z=\Lambda(k)\) is uniquely specified by
\[
 \cosh(k\ell)f(\Lambda(k))=1,\qquad \Lambda(0)=0.
\]
The continuous exponentially integrable excursion law supplies a simple isolated pole and analytic \(\Lambda\) around zero. Hence \(\log\mathbb E e^{kX_T}=T\Lambda(k)+O(1)\), locally analytically in \(k\), so its second and fourth derivatives yield the cumulant growth limits. Expansion using \(f(z)=1-\mu z+(m_2/2)z^2+O(z^3)\) gives
\[
 \Lambda(k)=\frac{\ell^2}{2\mu}k^2
 +\frac{\ell^4(3m_2-5\mu^2)}{24\mu^3}k^4+O(k^6).
\]
Consequently \(D_{\mathrm{eff}}=\ell^2/(2\mu)\) and
\[
 \lim_{T\to\infty}\frac{\kappa_4(X_T)}T
 =\frac{\ell^4}{\mu}(3\operatorname{CV}^2(\tau)-2).
\]
This identity shows that \(2/3\), rather than \(1\), is the precise renewal-variability threshold for positive fourth-cumulant growth in this symmetric fixed-step setting.

**4. Exact renewal variability.** Differentiating the transform at \(z=0\) gives
\[
 \mu=\frac{2\sinh^2\alpha}{r\cosh\alpha},\qquad
 \operatorname{CV}^2(\tau)=1+\frac{\sinh\alpha-\alpha}{\sinh^3\alpha}
 -\frac{\alpha}{2\sinh\alpha}.
\]
The first expression recovers the published diffusivity and the second is the new sharp-window formula. Define \(F\) as above. An exact rearrangement yields
\[
 \operatorname{CV}^2(\tau)-\frac23=\frac{F(\alpha)}{6\sinh^3\alpha}.
\]
Now
\[
 2F(\alpha)=\sinh(3\alpha)+9\sinh\alpha
 -3\alpha\cosh(2\alpha)-9\alpha.
\]
The coefficients of \(\alpha\) and \(\alpha^3\) vanish, while for every integer \(n\ge2\) the coefficient of \(\alpha^{2n+1}\) is
\[
 \frac{3^{2n+1}+9-3(2n+1)4^n}{(2n+1)!}>0.
\]
For \(n=2\), positivity is immediate; for \(n\ge3\), the inequality \(9^n>(2n+1)4^n\) follows from the base \(n=3\) and multiplication by \(9/4>(2n+3)/(2n+1)\). This proves \(F(\alpha)>0\) for every \(\alpha>0\).

For the upper bound set \(G(\alpha)=\alpha(\sinh^2\alpha+2)-2\sinh\alpha\). Then
\[
 1-\operatorname{CV}^2(\tau)=\frac{G(\alpha)}{2\sinh^3\alpha},\qquad
 2G(\alpha)=\alpha(\cosh 2\alpha+3)-4\sinh\alpha.
\]
The coefficient of \(\alpha\) vanishes, and every coefficient of \(\alpha^{2n+1}\), \(n\ge1\), equals \(((2n+1)4^n-4)/(2n+1)!>0\). Thus \(G(\alpha)>0\). The two strict inequalities together prove the sharp open interval \((2/3,1)\).

**5. Fourth cumulant and endpoints.** Substitution into the renewal-cumulant identity gives the displayed closed positive formula. Since \(F(\alpha)=\alpha^5/20+O(\alpha^7)\) and \(\alpha^2=r\ell^2/(4D)\), the small-rate fourth-cumulant coefficient is \(r\ell^4/80+o(r)\). As \(\alpha\to\infty\), the coefficient is \(r\ell^4e^{-\alpha}(1+o(1))\). The explicit coefficient of variation tends to \(2/3\) and \(1\) at the corresponding endpoints. A renewal expansion also gives the positive long-time excess-kurtosis coefficient stated above.

## Verification

The accompanying standalone checker (`CHECKER.py`) was executed from its actual file bytes and reported 223 passing checks. These include exact symbolic coefficient identities, 62 additional positive-series coefficient tests in each bound, direct two-region first-passage ODE matching, derivatives of the original Laplace transform, and independently solved renewal-pole expansions for eight parameter values. These finite checks corroborate the equations; the all-parameter inequalities are established by the infinite positive-coefficient arguments above. To rerun: `python CHECKER.py` with `mpmath` and `sympy` installed. No stochastic simulation or truncated enumeration is used as an infinite proof.

## Relationship to prior work

Alston and Bertrand (arXiv:2401.12772v1, 2024; *Physical Review E* 111, 034114, 2025) introduce this exact local-nearest-site resetting process, prove the regular-array enhancement of its effective diffusivity, and derive the excursion-time Laplace transform used above. Those model facts and the diffusivity optimization are established antecedents, not claimed as new. Their main text and appendices do not report the sharp coefficient-of-variation window or the positive fourth-cumulant growth theorem. Meylahn, Sabhapandit and Touchette (2015) develop a broad renewal/pole framework for additive observables under **fixed-position** resetting; that mathematical framework motivates the pole method, but does not supply the present nearest-site first-passage inequality or its universal strict sign. Standard renewal theory alone gives the sign criterion, not its all-rate verification for this physical model. No claim of exhaustive publication priority is made.

## Limitations

This theorem is for an infinite equally spaced array, instantaneous resetting, homogeneous Poisson rate, and Brownian diffusion without drift. The fourth cumulant is strictly positive in its **long-time growth coefficient**, not asserted positive for all finite observation times. A positive asymptotic excess-kurtosis coefficient does not conflict with a central limit theorem: the excess tends to zero like \(T^{-1}\). The result does not classify irregular reset arrays, finite-speed returns, asymmetric hopping, or higher cumulants. An independent audit and independent literature-priority evaluation remain outstanding.

## References

1. H. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772v1 (first public 2024-01-23), https://arxiv.org/abs/2401.12772 ; open author preprint https://thibaultbertrand.com/assets/pdf/2024_arxiv_a.pdf .
2. H. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting*, Physical Review E **111**, 034114 (2025), https://doi.org/10.1103/PhysRevE.111.034114 (open publisher PDF).
3. J. M. Meylahn, S. Sabhapandit and H. Touchette, *Large deviations for Markov processes with resetting*, Physical Review E **92**, 062148 (2015), https://arxiv.org/abs/1510.02431 .
