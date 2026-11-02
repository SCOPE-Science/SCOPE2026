# Ordered nonlinear energy-correlation thresholds in a telegraph-driven inertial oscillator

## Finding
Consider the stationary one-dimensional oscillator
\[
\dot X=V,\qquad \dot V=-V-kX+\sigma,
\]
where \(k>0\), and \(\sigma\in\{-1,1\}\) reverses sign independently at constant rate \(u/2>0\). Denote the excess fourth cumulants by \(K_X=\mathbb E[X^4]-3\mathbb E[X^2]^2\) and \(K_V=\mathbb E[V^4]-3\mathbb E[V^2]^2\), and the mixed energy covariance by \(C_{XV}=\operatorname{Cov}(X^2,V^2)\). Their signs exhibit an exact, strict ordering of thresholds.

Let
\[
\begin{aligned}
B(u)&=26u^2+68u+51,\\
C(u)&=3u^4+24u^3+72u^2+69u+18,\\
k_c(u)&=\frac{B(u)+\sqrt{B(u)^2+36C(u)}}{18}.
\end{aligned}
\]
For each \(u>0\), the mixed covariance is strictly negative for \(0<k<k_c(u)\), zero only at \(k=k_c(u)\), and strictly positive for \(k>k_c(u)\). Moreover \(k_c(u)>6\), it is strictly increasing in \(u\), and
\[
k_c(u)=6+\frac{159}{19}u+O(u^2)\quad(u\downarrow0),
\qquad k_c(u)\sim 3u^2\quad(u\to\infty).
\]

For every \(u>0\), the velocity cumulant \(K_V\) changes from negative to positive at a unique stiffness \(k_v(u)\), and
\[
0<k_v(u)<k_c(u).
\]
For \(0<u\le4/3\), the position cumulant satisfies \(K_X<0\) for all \(k>0\). For \(u>4/3\), it changes from negative to positive at a unique stiffness \(k_x(u)\), and the full strict hierarchy is
\[
\boxed{0<k_v(u)<k_c(u)<k_x(u).}
\]
Thus the kinetic fourth cumulant turns positive first, the potential–kinetic energy covariance turns positive second, and (when it exists) the position fourth cumulant turns positive last. The zeros are exact sign crossovers of stationary observables; no dynamical or thermodynamic phase transition is claimed.

## Assumptions and scope
The sign process is an autonomous stationary, symmetric two-state continuous-time Markov chain with the specified flip rate, independent of the initial oscillator state. The oscillator has positive stiffness and damping normalized to one. The homogeneous matrix \(\left(\begin{smallmatrix}0&1\\-k&-1\end{smallmatrix}\right)\) is Hurwitz for all \(k>0\), so the unique stationary solution is the convergent convolution of its stable impulse response with the stationary sign process. In particular all polynomial moments are finite. These conclusions concern the stationary joint law, not finite-time trajectories.

For the physical model \(m\ddot x+\gamma\dot x+\mu x=a_0\sigma\), where the sign flips at rate \(1/\tau_a\), set
\[
s=\frac{\gamma t}{m},\qquad X=\frac{\gamma^2x}{a_0m},\qquad V=\frac{\gamma v}{a_0},\qquad k=\frac{m\mu}{\gamma^2},\qquad u=\frac{2m}{\gamma\tau_a}.
\]
The potential and kinetic energies are positive multiples of \(X^2\) and \(V^2\), respectively; hence their covariance has the sign of \(C_{XV}\). In particular, every nonpositive-energy-covariance range contains the entire overdamped regime \(k\le1/4\), while the positive-covariance regime is necessarily strongly underdamped, \(k>6\). The force amplitude does not influence any of the thresholds.

## Proof
Let \(M_{ij}^{(s)}=\mathbb E[X^iV^j\sigma^s]\) for integers \(i,j\ge0\) and \(s\in\{0,1\}\). Put negative-index moments equal to zero. Stationarity applied to the polynomial generator gives, without closure approximations,
\[
0=iM_{i-1,j+1}^{(s)}-jM_{ij}^{(s)}-kjM_{i+1,j-1}^{(s)}+jM_{i,j-1}^{(1-s)}-suM_{ij}^{(s)}.
\]
Starting with \(M_{00}^{(0)}=1\), \(M_{00}^{(1)}=0\), the equations solve successively for the sign-weighted moments of odd degree and the ordinary moments of even degree. Symmetry under \((X,V,\sigma)\mapsto(-X,-V,-\sigma)\) eliminates the complementary parity. To degree four one obtains
\[
\mathbb E[X^2]=\frac{u+1}{k(k+u+u^2)},\quad
\mathbb E[V^2]=\frac{u}{k+u+u^2},\quad \mathbb E[XV]=0.
\]
Define the strictly positive common denominator
\[
H=(4k+3)(k+u+u^2)^2(9k+3u+u^2)(k+2+3u+u^2).
\]
Exact elimination of the degree-three sign-weighted and degree-four ordinary moments gives
\[
C_{XV}=-\frac{2uP_c(k,u)}{H},\qquad
K_X=-\frac{6P_x(k,u)}{kH},\qquad
K_V=-\frac{6uP_v(k,u)}{H},
\]
where
\[
\begin{aligned}
P_c={}&-9k^2+(26u^2+68u+51)k+3u^4+24u^3+72u^2+69u+18,\\
P_x={}&(12-9u)k^2+(33+119u+112u^2+26u^3)k\\
&+18+69u+102u^2+72u^3+24u^4+3u^5,\\
P_v={}&-9k^3+(-18+16u+26u^2)k^2\\
&+(6u+10u^2+4u^3+3u^4)k+6u^2+9u^3+3u^4.
\end{aligned}
\]
All algebraic identities are regenerated independently from the displayed generator recurrence by the accompanying checker.

The quadratic \(P_c\) has one positive and one negative root because its leading coefficient is negative and its constant term is positive. The positive root is exactly \(k_c\). Since \(P_c(6,u)=3u(u^3+8u^2+76u+159)>0\), its positive root exceeds six. The strictly positive derivatives \(B'(u)\) and \(C'(u)\) show \(k_c'(u)>0\). Expansion of the radical proves the stated asymptotics.

The coefficient signs of \(P_v\), read in descending powers of \(k\), have exactly one sign change for every positive \(u\). Its positive constant term and negative leading coefficient therefore give exactly one positive zero \(k_v\). Likewise \(P_x>0\) for \(u\le4/3\), whereas for \(u>4/3\) it has exactly one positive zero \(k_x\), with positive values below that zero and negative values above it.

It remains to compare these roots. Polynomial division in the variable \(k\) by \(P_c\) yields remainders \(R_v\) and \(R_x\) for \(P_v\) and \(P_x\). At \(k=k_c(u)\),
\[
\begin{aligned}
-9R_v={}&k(1532u^3+5888u^2+7911u+3681)\\
&+156u^5+1428u^4+5319u^3+8502u^2+5697u+1242>0,\\
3R_x={}&k(236u^2+476u+303)\\
&+12u^4+96u^3+387u^2+429u+126>0.
\end{aligned}
\]
Consequently \(P_v(k_c,u)<0\), while \(P_x(k_c,u)>0\). The single-crossing structures imply \(k_v<k_c\) in every case and \(k_c<k_x\) whenever \(k_x\) exists. This completes the complete sign hierarchy, including boundary equalities and the \(u=4/3\) case.

## Verification
Execute `python verify.py` in an environment with Python 3.10 or later and SymPy 1.12 or later. The script reconstructs the moment equations through total degree four, symbolically factors the three observables, checks the two polynomial remainder certificates and the exact threshold limits, and tests 168 rational moment substitutions plus seven root-ordering cases. All symbolic and rational checks passed. Numerical sampling is not used as proof of the universal statements.

## Relationship to prior work
Dutta, Kundu, Sabhapandit and Basu give the precise inertial run-and-tumble model, stationary second moments and a recurrence for arbitrary moments in their 2024 paper. In principle, that recurrence supplies the mixed fourth moment after further algebra. Their reported conclusions emphasize marginal fluctuation shapes, bounds and time-dependent second-order correlations; the strict potential–kinetic covariance sign boundary and its interlacing with two fourth-cumulant boundaries are not stated there. The contribution here is the global parameter classification, not an assertion that the moment recursion is new.

Méndez, Campos and Horsthemke analyze stationary energies of harmonic oscillators under *Gaussian* colored forcing. Their stationary position–velocity density factorizes because it is jointly Gaussian with zero position–velocity covariance, and thus its squared-position and squared-velocity covariance is zero. Telegraph forcing is non-Gaussian and yields the sign-changing observable above. Masoliver and Porrà's earlier dichotomous-noise oscillator study addresses second-order correlations and spectra, not the fourth-order threshold. These differences concern statements and force laws, not just different terminology.

## Limitations
The result assumes symmetric Poisson sign reversals, linear viscous damping and a harmonic trap. No thermal Gaussian noise, nonlinear potential, biased switching or multi-dimensional propulsion is included. The moment recurrence was already established in the motivating publication; the new claim is a sharp nontrivial sign classification derived from it. A broad literature search and direct comparisons do not certify priority against every unindexed or inaccessible text. The statistical sign crossovers are not transitions of the time-dependent dynamics.

## References
1. D. Dutta, A. Kundu, S. Sabhapandit, U. Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120v1 (10 June 2024), https://arxiv.org/html/2406.06120v1; revised v2, https://arxiv.org/html/2406.06120v2; *Physical Review E* **110**, 044107 (2024), https://doi.org/10.1103/PhysRevE.110.044107.
2. V. Méndez, D. Campos, W. Horsthemke, *Stationary energy probability density of oscillators driven by a random external force*, *Physical Review E* **87**, 062132 (2013), https://doi.org/10.1103/PhysRevE.87.062132.
3. J. Masoliver and J. M. Porrà, *Harmonic oscillators driven by colored noise: Crossovers, resonances, and spectra*, *Physical Review E* **48**, 4309 (1993), https://doi.org/10.1103/PhysRevE.48.4309.
