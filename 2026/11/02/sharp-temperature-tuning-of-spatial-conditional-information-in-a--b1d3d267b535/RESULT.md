# Sharp temperature tuning of spatial conditional information in an active harmonic chain

## Finding

Consider the equal-time stationary velocity field of the infinite nearest-neighbor inertial active Ornstein–Uhlenbeck harmonic chain specified below. Write \(t=T/m\), \(a=T_a/m\), and
\[
 A=1+\gamma\tau+2\tau^2\omega_E^2,\qquad B=2\tau^2\omega_E^2,\qquad \alpha=A/B>1.
\]
Let \(r_0=\alpha-\sqrt{\alpha^2-1}\in(0,1)\). At any \(t>0\), define
\[
 H=A+a/t,\quad \Delta=\sqrt{H^2-B^2},\quad r=(H-\Delta)/B\in(0,r_0).
\]
The inverse equal-time velocity covariance (spatial precision) has the **exact** entries
\[
 J_0=\frac1t-\frac{a}{t^2\Delta},\qquad
 J_{\pm n}=-\frac{a}{t^2\Delta}r^n\quad (n\ge1).
\]
When \(t=0\), instead \(J_0=A/a\), \(J_{\pm1}=-B/(2a)\), and \(J_{\pm n}=0\) for \(n\ge2\). Thus the active-only velocity field is a nearest-neighbor Gaussian Markov random field, whereas **every** positive thermal temperature induces nonzero all-other-velocities-conditioned dependence at **every** separation.

For \(n\ge1\), define the all-rest-conditioned partial correlation and information
\[
 \rho_n(t)=\operatorname{Corr}\left(V_0,V_n\mid (V_j)_{j\in\mathbb Z\setminus\{0,n\}}\right),\qquad
 I_n(t)= I\left(V_0;V_n\mid (V_j)_{j\notin\{0,n\}}\right).
\]
(The conditioning means *every* other site, not only sites between the selected pair.) For \(t>0\),
\[
 \rho_n(t)=\frac{a r^n}{t\Delta-a}
 =\frac{r^{n-1}(r_0-r)(r_0^{-1}-r)}{2(\alpha-r)},\qquad
 I_n(t)=-\tfrac12\log\bigl(1-\rho_n(t)^2\bigr).
\]
For the nearest-neighbor pair, \(\rho_1(t)\) is strictly decreasing in \(t\ge0\) and its maximum is \(B/(2A)\) at \(t=0\). In sharp contrast, for **every** integer \(n\ge2\), \(I_n(t)\) is zero at \(t=0\), positive for every finite \(t>0\), tends to zero as \(t\to\infty\), and has a **unique global maximizer** \(t_n>0\). Precisely, \(t_n=a/[\frac B2(r_n+r_n^{-1})-A]\), with \(r_n\) the unique root in \((0,r_0)\) of
\[
 \frac{n-1}{r_n}-\frac1{r_0-r_n}-\frac1{r_0^{-1}-r_n}
   +\frac1{\alpha-r_n}=0.
\]
The optimal thermal noise **increases strictly with distance**: \(t_{n+1}>t_n\) for every \(n\ge2\). The sharp large-separation laws are
\[
 r_0-r_n\sim \frac{r_0}{n},\qquad
 t_n\sim\frac{a}{\sqrt{A^2-B^2}}n,
 \qquad\max_{t>0}\rho_n(t)\sim\frac{r_0^n}{e n},
 \qquad\max_{t>0}I_n(t)\sim\frac{r_0^{2n}}{2e^2n^2}.
\]
All results hold simultaneously for every choice of positive \(m,\gamma,\tau,\omega_E,T_a\) and every integer separation; no weak-activity or continuum approximation is used.

## Assumptions and scope

Take the translation-invariant, infinite one-dimensional harmonic chain of particles of mass \(m>0\), drag per mass \(\gamma>0\), Einstein frequency \(\omega_E>0\), and independent onsite active Ornstein–Uhlenbeck forces with correlation time \(\tau>0\) and intensity \(T_a>0\). Independent white thermal forces have temperature \(T\ge0\). Linearized displacements obey the normal-mode equation with stiffness \(\omega_q^2=4\omega_E^2\sin^2(q/2)\); the Gaussian stationary **velocity** Fourier covariance, as established in Marconi–Löwen–Caprini (2024, Eq. (28)), is
\[
 C(q)=\frac{T}{m}+
 \frac{T_a/m}{1+\gamma\tau+4\tau^2\omega_E^2\sin^2(q/2)}
 =t+\frac{a}{A-B\cos q},\qquad -\pi\le q\le\pi.
\]
Because \(A>B>0\) and \(a>0\), this symbol is uniformly bounded above and below by positive constants even at \(T=0\). It defines a strictly positive, stationary Gaussian velocity field on \(\mathbb Z\). There is no claim that the absolute displacement field has a normalizable translation-invariant stationary distribution: its zero mode may diffuse. Conditioning on the other velocity coordinates is defined through the inverse Toeplitz covariance, equivalently as the Gaussian finite-volume conditional covariance limit.

The physical thermal optimum is \(T_n=m t_n\), with all remaining parameters held fixed. The word 'information' always means classical Gaussian conditional mutual information in natural-log units (nats), not quantum von Neumann information or thermodynamic entropy production.

## Proof

**1. The source covariance and its independently reconstructed normalization.** For any nonzero Fourier mode with harmonic stiffness \(k=\omega_q^2>0\), put \(u\) for displacement, \(v=\dot u\), and \(f\) for the active-force acceleration. Their linear stationary equations satisfy \(\dot u=v\), \(\dot v=-\gamma v-ku+f+\eta\), and \(\dot f=-f/\tau+\zeta\), with independent thermal and active noises, chosen so that \(\mathbb E[f^2]=\gamma T_a/(m\tau)\). The stationary cross-moment identities are
\[
 \mathbb E[uv]=0,\quad
 \mathbb E[uf]=\tau\mathbb E[vf],\quad
 (\gamma+1/\tau+k\tau)\mathbb E[vf]=\mathbb E[f^2],
 \quad\gamma\mathbb E[v^2]=\gamma T/m+\mathbb E[vf].
\]
Consequently \(\mathbb E[v^2]=T/m+(T_a/m)/(1+\gamma\tau+k\tau^2)\), reproducing exactly the quoted covariance. The zero-wavevector velocity mode is interpreted as the continuous limit \(k\downarrow0\).

**2. Precision kernel.** The spectral inverse is
\[
 \frac1{C(q)}=\frac1t-\frac{a/t^2}{H-B\cos q},\qquad t>0.
\]
Here \(H>B\), and writing \(r=(H-\sqrt{H^2-B^2})/B\) gives the exact absolutely convergent Fourier identity
\[
 \frac1{H-B\cos q}=\frac1\Delta
 \sum_{j\in\mathbb Z}r^{|j|}e^{ijq}.
\]
Fourier-coefficient comparison proves the displayed precision formula. At \(t=0\), \(1/C(q)=(A-B\cos q)/a\), which has only three nonzero Fourier coefficients. For finite periodic chains, the same distinction holds: if \(t>0\), write the precision as \(t^{-1}I-(a/t^2)[H I-(B/2)(S+S^{-1})]^{-1}\). The bracketed inverse is entrywise strictly positive via a convergent Neumann series over walks on a connected cycle, because \(H>B\). At \(t=0\), it is a nearest-neighbor cyclic matrix. The uniform spectral gap gives convergence of fixed-separation ring coefficients to the infinite-chain kernel.

**3. Conditional information.** For a Gaussian field with bounded invertible covariance operator, conditioning on all but sites \(0,n\) leaves the bivariate conditional precision
\[
 \begin{pmatrix}J_0&J_n\\J_n&J_0\end{pmatrix}.
\]
Thus \(\rho_n=-J_n/J_0\) and \(I_n=-\frac12\log(1-\rho_n^2)\). Since the covariance is strictly positive, \(0<\rho_n(t)<1\) at every \(t>0\). Inverting \(r=(H-\Delta)/B\), we have
\[
 H=\tfrac B2(r+r^{-1}),\quad
 \Delta=\tfrac B2(r^{-1}-r),\quad
 t=\frac{a}{\frac B2(r+r^{-1})-A}.
\]
The last expression is a strictly increasing bijection from \(0<r<r_0\) to \(0<t<\infty\), because \(dH/dr=\frac B2(1-r^{-2})<0\). As \(r_0+r_0^{-1}=2\alpha\), substituting into \(\rho_n\) yields the factored expression. Its endpoint limits prove the vanishing assertion for \(n\ge2\), and \(\rho_1(0)=B/(2A)\).

**4. Exactly one optimum.** For \(n\ge2\), differentiating the logarithm of the positive factored expression gives
\[
 f_n(r):=\frac{d}{dr}\log\rho_n(r)
 =\frac{n-1}{r}-\frac1{r_0-r}
   -\frac1{r_0^{-1}-r}+\frac1{\alpha-r}.
\]
Now \(\alpha>r_0\), so
\[
 f_n'(r)=-\frac{n-1}{r^2}-\frac1{(r_0-r)^2}
 -\frac1{(r_0^{-1}-r)^2}+\frac1{(\alpha-r)^2}<0.
\]
The strict inequality follows because \((\alpha-r)^{-2}<(r_0-r)^{-2}\). Moreover \(f_n(r)\to+\infty\) at \(r\downarrow0\) and \(f_n(r)\to-\infty\) at \(r\uparrow r_0\). Therefore \(f_n\) has exactly one root, yielding the unique global maximum of both \(\rho_n\) and \(I_n\). For \(n=1\), \(f_1(r)<0\) directly from the same inequality, proving strict monotonic decay. Also \(f_{n+1}(r)=f_n(r)+1/r\); at the unique zero \(r_n\), this is positive, so strict decrease of \(f_{n+1}\) places its zero to the right: \(r_{n+1}>r_n\), hence \(t_{n+1}>t_n\).

**5. Sharp distance asymptotics.** Since \(r_n\) is increasing and bounded above by \(r_0\), its limit exists. The root equation forces this limit to equal \(r_0\): otherwise the diverging term \((n-1)/r_n\) could not be canceled. At the root, all terms except \((n-1)/r_n\) and \(-1/(r_0-r_n)\) remain bounded; hence
\[
 \frac1{r_0-r_n}=\frac{n-1}{r_n}+O(1),
 \qquad n(r_0-r_n)\longrightarrow r_0.
\]
Because \(dH/dr|_{r_0}=-\Delta_0/r_0\), where \(\Delta_0=\sqrt{A^2-B^2}\), we obtain \(H(r_n)-A\sim\Delta_0/n\), and thus \(t_n\sim(a/\Delta_0)n\). Finally, the identity \(2(\alpha-r_0)=r_0^{-1}-r_0\) reduces the factored partial correlation near \(r_0\) to
\[
 \rho_n(r_n)\sim r_n^{n-1}(r_0-r_n).
\]
The limit \((r_n/r_0)^n\to e^{-1}\) therefore gives \(\max\rho_n\sim r_0^n/(en)\). The expansion \(-\frac12\log(1-z^2)\sim z^2/2\) as \(z\to0\) gives the final information asymptotic. This completes the proof.

## Verification

The independently executable standard-library-only file `verify.py` solves the stationary three-variable Lyapunov moment system for five nonzero Fourier modes per parameter set and compares it with the spectral covariance. It reconstructs finite ring covariance matrices from Fourier sums, performs independent matrix inversions, compares precision coefficients with the reciprocal Fourier symbol and cold nearest-neighbor limit, and checks the uniqueness and large-distance optimizer formulas for several active and thermal parameter sets. It passed **6020 checks** via `python verify.py` on the extracted package. These tests support the independent normalizations and computations; the strict all-distance and all-parameter conclusions rely on the analytic arguments in Steps 2–5, not on finite enumeration.

For an indicative unit-mass example \(\gamma=\tau=\omega_E=T_a=m=1\), the derived parameters are \(A=4\), \(B=2\), \(a=1\), and \(r_0=2-\sqrt3\). The optimal normalized thermal temperatures are approximately \(t_2=0.287902176\), \(t_3=0.576643524\), and \(t_{10}=2.597774189\); they increase with separation. The corresponding \(\rho_2(t_2)\approx0.017310023\) and \(I_2(t_2)\approx0.000149841\) nats.

## Relationship to prior work

Marconi, Löwen and Caprini (2024) establish the active harmonic-chain dynamics, exact mode velocity covariance (their Eq. (28)), and its geometric spatial correlation function (Eq. (33)). Those formulas supply the model's starting point and are **not** claimed as new. The present theorem analyzes an intrinsically different observable: the inverse *total* covariance and two-site information conditioned on **all** other sites, not the ordinary marginal pair covariance. The cold-to-warm precision-graph change is one consequence; the distinctive finding is the global, exactly unique optimal thermal noise for every nonadjacent distance, its strict separation ordering, and the coefficient-exact long-distance laws. Their derivations require a separate reciprocal-spectrum inversion and a strictly concave optimization.

Paul, Dhar and Chaudhuri (2024) study harmonic-chain tracer and displacement/stretch correlations in a different active model; Malouf, Goold, Adesso and Landi (2018/2019) investigate conditional information across middle blocks of a boundary-driven **quantum** bosonic chain with auxiliary reservoirs. Neither supplies the current classical, all-rest-conditioned velocity optimization. The algebraic phenomenon that additive white noise converts Gaussian autoregressive covariance into a more densely supported precision kernel is familiar in time-series analysis; the general phenomenon is not claimed as independently novel. Chavez (2016) analyzes Gaussian time-series prediction information, a plausible general conceptual overlap, but the accessible abstract does not give the distance-indexed optimal noise result; its full text could not be examined.

## Limitations

This is a stationary **linear** and **Gaussian** equal-time velocity theorem on a uniform one-dimensional nearest-neighbor chain. It does not establish information optimization for non-Gaussian self-propulsion, nonuniform elastic couplings, position fields, or finite-time transport. Conditional information here is classical and conditioned on every other coordinate. The exact finite-ring positivity of long-distance precision entries is shown, but the distance-indexed optimal temperatures refer to the infinite-chain limit; finite-ring optimal temperatures need not equal them. No claim about entropy-production optimality, dynamical stability transitions, quantum correlations or general statistical-mechanical phases is made. The 2016 Gaussian prediction-information article was only abstract-accessible; its specific relevance to the new optimization remains a publication-priority risk. Independent scientific audit and independent publication-priority confirmation have not been performed.

## References

1. U. Marini Bettolo Marconi, H. Löwen, and L. Caprini, *Active fluctuations in the harmonic chain: phonons, entropons and velocity correlations*, arXiv:2401.07972 (first public 2024-01-15), Sections II and IV.1, Eqs. (8), (9), (28) and (30)–(34), Appendix C. https://arxiv.org/abs/2401.07972
2. S. Paul, A. Dhar, and D. Chaudhuri, *Dynamical crossovers and correlations in a harmonic chain of active particles*, arXiv:2402.11358 (first public 2024-02-17), Sections I and on active tracer correlations. https://arxiv.org/abs/2402.11358
3. W. T. B. Malouf, J. Goold, G. Adesso, and G. T. Landi, *Analysis of the conditional mutual information in ballistic and diffusive non-equilibrium steady-states*, arXiv:1809.09931 (first public 2018-09-26), Sections II–IV. https://arxiv.org/abs/1809.09931
4. G. Chavez, *Conditional and Marginal Mutual Information in Gaussian and Hyperbolic Decay Time Series*, Journal of Time Series Analysis 37 (2016), 851–861. https://doi.org/10.1111/jtsa.12199 (abstract inspected; full text not inspected).
