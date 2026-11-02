# A doubled resetting threshold and logarithmic edge singularity for Glauber–Ising spatial correlations

## Finding

For the infinite, one-dimensional ferromagnetic Glauber–Ising chain reset as a whole to the deterministic all-plus spin configuration at independent Poisson times, the stationary **spatially averaged two-spin correlation** at each fixed separation has an exactly parameterized continuous distribution. Its lower-edge density changes from divergent to vanishing at the **separation-independent** threshold \(r_c=2[1-\tanh(2J/(k_BT))]\). At the threshold the density diverges as a square root of a logarithm. The threshold is twice the magnetization-distribution threshold of the self-review; the latter has a finite, constant density at its own transition.

More precisely, put \(\gamma=\tanh(2J/(k_BT))\in(0,1)\), \(a=2(1-\gamma)\), \(q=(1-\sqrt{1-\gamma^2})/\gamma\), and \(\theta=r/a\). For any fixed integer spin separation \(n\ge1\), define
\[
S_n(t)=e^{-2t}\left[I_0(2\gamma t)+2\sum_{j=1}^{n-1}I_j(2\gamma t)+I_n(2\gamma t)\right],\qquad
c_n=\frac{n}{\sqrt{\pi\gamma}},
\]
where \(I_j\) is the modified Bessel function. The no-reset Glauber correlation is the strictly decreasing function
\[
C_n(t)=q^n+a\int_t^\infty S_n(s)\,ds
=1-a\int_0^t S_n(s)\,ds,
\qquad C_n(0)=1,\quad \lim_{t\to\infty}C_n(t)=q^n.
\]
For the stationary reset age \(A\sim\mathrm{Exp}(r)\), the observable \(U_n=C_n(A)\) has support \((q^n,1)\) and density
\[
f_n(u)=\frac{r e^{-r t_n(u)}}{aS_n(t_n(u))},\qquad
q^n<u<1,\qquad C_n(t_n(u))=u.
\]
The inverse is unique. At the lower edge \(y=u-q^n\downarrow0\), its cumulative law and density satisfy
\[
\mathbb P(U_n-q^n\le y)\sim
\left(\frac{\sqrt{\pi\gamma/a}}{n}\right)^\theta
 y^\theta\,[\log(1/y)]^{\theta/2},
\]
\[
f_n(q^n+y)\sim
\theta\left(\frac{\sqrt{\pi\gamma/a}}{n}\right)^\theta
 y^{\theta-1}[\log(1/y)]^{\theta/2}.
\]
Consequently \(f_n\) diverges at this edge when \(0<r\le a\) (including the logarithmic critical divergence at equality), and vanishes when \(r>a\). At the upper edge \(\lim_{u\uparrow1} f_n(u)=r/a\). The zero-coupling boundary \(\gamma=0\) is different: then \(C_n(t)=e^{-2t}\) and \(f_n(u)=(r/2)u^{r/2-1}\) on \((0,1)\), with **no logarithmic factor**.

An associated stationary two-point expectation has the closed spatial profile
\[
\overline C_n=\mathbb E[U_n]=b+(1-b)\xi^n,\qquad
b=\frac r{r+a},\qquad
\xi=\frac{2\gamma}{r+2+\sqrt{(r+2)^2-4\gamma^2}}.
\]
Its nonzero limit as \(n\to\infty\) reflects the shared reset age. The connected infinite-separation limit is
\[
\lim_{n\to\infty}\left(\overline C_n-\overline m^2\right)
=\frac{r(1-\gamma)^2}{[r+2(1-\gamma)][r+(1-\gamma)]^2}>0,
\quad\overline m=\frac r{r+1-\gamma}.
\]

## Assumptions and scope

Take spins \(s_i(t)\in\{-1,+1\}\) indexed by \(i\in\mathbb Z\), coupling \(J>0\), finite temperature \(T>0\), zero external field, and Glauber single-spin flip rate
\[
w_i(s)=\frac12\left[1-\frac\gamma2 s_i(s_{i-1}+s_{i+1})\right],\qquad
\gamma=\tanh\!\left(\frac{2J}{k_BT}\right)\in(0,1).
\]
The time unit is fixed by this flip-rate normalization. An independent global Poisson clock of rate \(r>0\) simultaneously replaces every spin by \(+1\). The infinite-volume process is observed in its stationary renewal regime. Each \(U_n\) is the thermodynamic-limit spatial average of spin products \(s_i s_{i+n}\), conditional on the age since the last reset, and **not** the \(\{-1,+1\}\)-valued instantaneous product at a single specified bond. Concretely, conditional on reset age \(t\), the infinite-volume spatial ergodic average equals \(C_n(t)=\mathbb E[s_0(t)s_n(t)]\) for the no-reset process begun all-plus. Stationary sampling gives the common random age \(A\sim\mathrm{Exp}(r)\). All statements concern fixed integer \(n\) before any limit in separation; no simultaneous large-separation/near-edge uniform asymptotic is claimed.

## Proof

**Closed hierarchy and boundary.** Translation invariance and the stated Glauber generator imply, for every integer \(n\ge1\),
\[
\dot C_n(t)=-2C_n(t)+\gamma(C_{n-1}(t)+C_{n+1}(t)),\qquad C_0(t)=1,\quad C_n(0)=1.
\]
The unique bounded equilibrium solution is \(C_n(\infty)=q^n\), where \(\gamma(q+q^{-1})=2\) and \(0<q<1\). Differentiating the hierarchy and writing \(W_n=-\dot C_n\) yields the killed discrete heat equation with Dirichlet boundary \(W_0=0\) and constant initial data \(W_n(0)=a\). Its positive semigroup kernel is
\[
K_t(n,m)=e^{-2t}\big[I_{|n-m|}(2\gamma t)-I_{n+m}(2\gamma t)\big],\qquad n,m\ge1.
\]
The image construction (subtracting the reflected whole-line walk kernel) verifies both the generator and the Dirichlet condition. Summing over \(m\ge1\) telescopes to
\[
\sum_{m=1}^\infty K_t(n,m)=S_n(t).
\]
Thus \(W_n(t)=aS_n(t)>0\), proving strict monotonicity. Since the Glauber evolution converges to its unique one-dimensional Gibbs state for \(0<\gamma<1\), integration of \(\dot C_n=-aS_n\) from infinity gives the displayed formula for \(C_n(t)\). This also proves \(C_n(0)=1\) and \(C_n(\infty)=q^n\) without assuming any finite-volume mixing limit interchange.

**Precise late-time tail.** For every fixed integer \(j\), the classical Bessel asymptotic is
\[
I_j(2\gamma t)=\frac{e^{2\gamma t}}{\sqrt{4\pi\gamma t}}[1+O(t^{-1})].
\]
The weights in \(S_n\) sum to \(2n\). Hence \(S_n(t)=c_n t^{-1/2}e^{-at}[1+O(t^{-1})]\). Because \(a>0\), exponential-tail integration gives
\[
C_n(t)-q^n=c_nt^{-1/2}e^{-at}[1+O(t^{-1})],\qquad
-\dot C_n(t)=a c_nt^{-1/2}e^{-at}[1+O(t^{-1})].
\]
In particular, the leading algebraic factor is \(t^{-1/2}\) rather than a pure exponential; this is what generates the logarithmic edge correction.

**Stationary distribution and threshold.** By Poisson renewal, \(A\sim\mathrm{Exp}(r)\). Since \(C_n\) is continuously strictly decreasing, the inverse time \(t_n(u)\) exists for every \(q^n<u<1\), and a change of variables from \(A\) proves the exact density. For \(y\downarrow0\), write \(t=t_n(q^n+y)\). Then
\[
y=c_nt^{-1/2}e^{-at}(1+o(1)),\quad
 t\sim\frac{\log(1/y)}a,\quad
\mathbb P(U_n-q^n\le y)=e^{-rt}.
\]
Eliminating \(t\) yields the displayed asymptotic cumulative probability with constant \(c_n^{-\theta}a^{-\theta/2}\). Since \(-\dot C_n\sim ay\), the change-of-variables density has the stated asymptotic with multiplicative factor \(\theta=r/a\). Consequently \(\theta<1\) yields a power divergence, \(\theta=1\) yields a square-root logarithmic divergence, and \(\theta>1\) yields vanishing density. At \(t\downarrow0\), \(S_n(t)\to1\), yielding the upper-edge limit \(r/a\). At \(\gamma=0\), the Glauber hierarchy decouples and yields the separate beta-density formula exactly.

**Mean spatial profile.** Resetting gives the stationary moment equation
\[
0=-(r+2)\overline C_n+\gamma(\overline C_{n-1}+\overline C_{n+1})+r,\quad n\ge1,\quad\overline C_0=1.
\]
Its unique bounded solution is \(\overline C_n=b+(1-b)\xi^n\), with \(b\) and \(\xi\) as stated. The one-spin equation gives \(\overline m=r/[r+(1-\gamma)]\). Direct subtraction yields the positive connected long-range limit. This last limit reflects the variance of \(e^{-(1-\gamma)A}\), not spontaneous Gibbs long-range order.

## Verification

The standalone file `verify.py` uses Bessel functions, direct numerical quadrature, and a separately assembled finite-volume spin-flip-plus-reset generator. It checks the killed kernel against the explicit Bessel sum; verifies the exact stationary renewal integral against the closed difference-equation solution; checks large-time Bessel coefficients; and independently solves the full reset-driven stationary Markov system on rings of six and eight spins to reproduce the finite-ring pair-correlation formula. The executable completed 231 finite checks in the reviewed run. The finite-ring identity used for this last comparison is
\[
\overline C_n^{(N)}=b+(1-b)\frac{\xi^n+\xi^{N-n}}{1+\xi^N},\qquad 1\le n<N.
\]
These tests are reproducibility checks, not proofs of an infinite-volume assertion. The analytical semigroup, Bessel asymptotic, inverse transformation, and stationary difference-equation arguments establish the theorem.

## Relationship to prior work

Magoni, Majumdar and Schehr's 2020 *Ising model with stochastic resetting* (arXiv:2002.04867) supplies the Glauber/resetting model, its renewal treatment, and the exact magnetization-distribution threshold \(r^*=1-\gamma\). Its concluding discussion identifies distributions of two-point correlations as a further problem. Here the spatially averaged pair-correlation law uses a distinct two-spin hierarchy and acquires a separation-independent doubled threshold plus a logarithmic singularity absent from the magnetization law. Chen and Zhong's 2024 *Crossover from Anomalous to Normal Diffusion: Ising Model with Stochastic Resetting* (arXiv:2407.11708) treats two-dimensional critical magnetization dynamics under Metropolis updating, not the present one-dimensional Glauber spatial pair-correlation distribution. The 1963 Glauber kinetic-Ising solution supplies the classical closure and discrete Bessel propagator; the new claim is the complete pushforward distribution and its sharp edge phase diagram under global Poisson reset, not the closure or Bessel formula in isolation.

## Limitations

The limit is the infinite, translation-invariant chain with all-plus global resetting and \(0<\gamma<1\). The observable is a thermodynamic spatial average, not a single-bond snapshot. The finite-size stationary pair-correlation profile has an exact formula but its finite-size correlation **distribution** is not claimed to have the same continuum edge behavior. No proof is given for resetting to heterogeneous configurations, for Metropolis dynamics, for higher-dimensional Ising models, or for arbitrary renewal waiting times. The logarithmic prefactor is not uniform as \(\gamma\downarrow0\), and the \(\gamma=0\) boundary has a different exact law. Independent validation and definitive publication-priority verification are not asserted.

## References

1. M. Magoni, S. N. Majumdar and G. Schehr, *Ising model with stochastic resetting*, arXiv:2002.04867 (first submitted 2020-02-12); *Physical Review Research* **2**, 033182 (2020), DOI:10.1103/PhysRevResearch.2.033182.
2. Y. Chen and W. Zhong, *Crossover from Anomalous to Normal Diffusion: Ising Model with Stochastic Resetting*, arXiv:2407.11708 (first submitted 2024-07-16); *Physical Review Research* **6**, 033189 (2024), DOI:10.1103/PhysRevResearch.6.033189.
3. R. J. Glauber, *Time-Dependent Statistics of the Ising Model*, *Journal of Mathematical Physics* **4**, 294–307 (1963), DOI:10.1063/1.1703954.
