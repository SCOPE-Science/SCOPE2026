# Work-noise order reversal for covariance-matched run-and-rest and telegraph drives

## Finding

Two stationary propulsion mechanisms can have **identical force autocovariances, identical position autocovariances at every lag, and identical mean active-work rates**, yet show opposite orderings of their long-time work variance as the switching and trap rates cross. The distinction is visible only beyond second-order trajectory statistics.

For all \(k,g,v>0\), compare a three-state run-and-rest drive with values \(-v,0,v\) to a two-state telegraph drive with values \(\pm v/\sqrt2\), as defined below. Both satisfy
\[
\mathbb E[U_t]=0,\qquad \mathbb E[U_0U_t]=\frac{v^2}{2}e^{-g|t|},\qquad
\lim_{T\to\infty}\frac{\mathbb E W_T}{T}=\frac{gv^2}{2(k+g)}.
\]
Nevertheless their active-work variance rates are exactly
\[
\boxed{V_3=\frac{gv^4}{4(k+g)^2},\qquad
V_2=\frac{gkv^4}{2(k+g)^3}.}
\]
Consequently,
\[
\boxed{\frac{V_3}{V_2}=\frac{k+g}{2k},\qquad
V_3<V_2\ \Longleftrightarrow\ g<k,\qquad
V_3=V_2\ \Longleftrightarrow\ g=k.}
\]
The inequalities reverse for \(g>k\). Both work functionals satisfy a stationary central limit theorem,
\[
\frac{W_T-\mu T}{\sqrt{T}}\ \Longrightarrow\ \mathcal N(0,V_j),\quad
\mu=\frac{gv^2}{2(k+g)},\quad j\in\{2,3\}.
\]
As a further diagnostic, with fixed \(k,v\), \(V_3\) reaches its unique maximum at \(g=k\), whereas \(V_2\) reaches its unique maximum at \(g=k/2\).

## Assumptions and scope

For both models the continuous coordinate obeys the deterministic, overdamped, harmonically confined equation
\[
\dot X_t=-kX_t+U_t.
\]
Model 3 (run-and-rest) is the irreducible continuous-time Markov chain with states \(-v,0,v\): each running state jumps to rest at rate \(g\), and rest jumps to either running state at rate \(g/2\). Its stationary state probabilities are \(1/4,1/2,1/4\). Model 2 (telegraph) takes values \(\pm v/\sqrt2\) and flips sign at rate \(g/2\), with stationary probabilities \(1/2,1/2\). These rate and amplitude normalizations are essential for covariance matching.

Initialize the joint processes in their unique stationary laws, in which
\[
X_t=\int_{-\infty}^{t}e^{-k(t-s)}U_s\,ds.
\]
Define the time-integrated mechanical work done by the active force,
\[
W_T=\int_0^T U_t\,dX_t
=\int_0^T\big(U_t^2-kU_tX_t\big)\,dt.
\]
As \(X_t\) is continuous and absolutely continuous between finitely many switch times on compact intervals, this is an ordinary pathwise Lebesgue–Stieltjes integral; no stochastic calculus convention is required. Thermal translational noise is absent. Work is **not** asserted to equal a convention-independent total entropy-production functional.

## Proof

**Stationarity and matched second-order observations.** In Model 3, the generator of \(U_t\) maps the observable \(u\) to \(-gu\). In Model 2 the sign-flip rate \(g/2\) likewise gives \(Lu=-gu\). Both stationary laws have \(\mathbb EU=0\) and \(\mathbb EU^2=v^2/2\). The Markov property thus gives their identical full force autocovariance above. Linear harmonic filtering proves equality of every two-time covariance of \(X\), as well as mixed force-position covariances. Applying the joint generator to \(x u\) and \(x^2\) yields, for either model,
\[
\mathbb E[XU]=\frac{v^2}{2(k+g)},\qquad
\mathbb E[X^2]=\frac{v^2}{2k(k+g)}.
\]
The common mean work rate is \(\mu=\mathbb E[U^2-kXU]=gv^2/[2(k+g)]\).

**Three-state Poisson equation.** Put \(Q=u^2\), \(P=xu\), and \(f(x,u)=u^2-kxu\). The joint generator for Model 3 satisfies
\[
LQ=gv^2-2gQ,\qquad LP=Q-(k+g)P.
\]
Consequently the bounded polynomial
\[
\Phi_3(x,u)=\frac{u^2}{2(k+g)}-\frac{kxu}{k+g}
\]
solves \(L\Phi_3=\mu-f\) at all three values of \(u\). Dynkin's formula makes
\[
M_T=W_T-\mu T+\Phi_3(X_T,U_T)-\Phi_3(X_0,U_0)
\]
a purely discontinuous square-integrable martingale. Write \(a=1/[2(k+g)]\) and \(b=-k/(k+g)\). At a run-to-rest jump, the change in \(\Phi_3\) is \(-av^2-bXU\); at a rest-to-run jump with equally likely signs it is \(av^2+bX(\pm v)\). The predictable squared-jump intensity averaged over the stationary process is
\[
\begin{aligned}
V_3&=g\big[a^2v^4+2abv^2\mathbb E(XU)+b^2v^2\mathbb E(X^2)\big]\\
&=\frac{gv^4}{4(k+g)^2}.
\end{aligned}
\]
Here the last two contributions cancel **exactly**, by the displayed stationary moments. The formula correctly includes the random direction chosen at rest-to-run jumps; dropping those direction-dependent increments would be incorrect.

**Two-state Poisson equation.** For Model 2, \(U^2=v^2/2\) is constant. The corrector
\[
\Phi_2(x,u)=-\frac{kxu}{k+g}
\]
obeys \(L\Phi_2=\mu-f\). A flip \(u\to-u\) changes this corrector by \(2kxu/(k+g)\), and flips occur at rate \(g/2\). Their stationary quadratic variation gives
\[
V_2=\frac{g}{2}\,\mathbb E\left[\frac{4k^2X^2U^2}{(k+g)^2}\right]
=\frac{gkv^4}{2(k+g)^3}.
\]

**Long-time limits and optimization.** Since the force is bounded and the harmonic dynamics contracts, \(|X_t|\le v/k\) in the stationary state of either model. The correctors, jump intensities, and jump sizes are bounded. Stationary ergodicity implies \(\langle M\rangle_T/T\to V_j\) almost surely. The bounded-jump martingale central limit theorem proves the stated Gaussian limits. The endpoint corrector difference is uniformly bounded, so its contribution to the variance divided by \(T\) vanishes by Cauchy–Schwarz; thus \(\mathrm{Var}(W_T)/T\to V_j\). Algebra gives \(V_3/V_2=(k+g)/(2k)\). Direct differentiation in \(g\) yields signs \(\operatorname{sgn}(k-g)\) for \(dV_3/dg\) and \(\operatorname{sgn}(k-2g)\) for \(dV_2/dg\); continuity and positivity yield the unique maxima.

## Verification

The standalone file `verification/verify_algebra.py` reconstructs the joint generators state by state, verifies both Poisson identities, both stationary quadratic-jump variance identities, the ratio, and derivative factorizations by exact SymPy algebra. Run `python verification/verify_algebra.py` with Python 3 and SymPy installed.

Independently, `verification/check_event_driven.cpp` generates exact exponential switching events, propagates the harmonic coordinate exactly between events, and integrates mechanical work on each deterministic segment. Compile with `g++ -O2 -std=c++17 verification/check_event_driven.cpp -o check_event_driven` and run `./check_event_driven`. The reported sample size is 50,000 trajectories per model and parameter set, with a burn-in of \(40/k\) and observation horizon \(250\). At \(k=1,v=1.4\), the six relative numerical discrepancies in variance rates were between approximately 0.09% and 1.2%, consistent with sampling and finite-horizon variability. This experiment is not used as proof of an infinite-time limit.

## Relationship to prior work

Sun, Ye and Podgornik [1] define the finite-run/finite-tumble particle under harmonic confinement and determine stationary position moments and distributions, including the equal-rate case. Basu and collaborators [2] previously solved the equal-rate, three-internal-state stationary position distribution. Both are credited for the underlying model and stationary-state analysis; the present contribution is **not** a new stationary distribution.

Semeraro and collaborators [3] study integrated active-work fluctuations for an active **Ornstein–Uhlenbeck** (Gaussian) propulsion in a harmonic trap. Their Gaussian force model does not provide the finite-state run-and-rest jump intensities or the covariance-matched two-versus-three-state reversal. A pre-existing two-state active-work computation in the presence of translational diffusion implies the two-state comparator by an appropriate zero-diffusion limit; the two-state formula **alone is not claimed as original**. The new content is the exact three-state work variance, its cancellation mechanism, and the strict noise-order reversal despite identical second-order trajectory observables. General Markov-additive central limit theorems guarantee qualitative Gaussian behavior but do not, without explicit computation, determine these rational variance rates or their sign crossing.

## Limitations

The classification assumes strictly positive \(k,g,v\), stationary starts, Markovian exponential dwell times, a harmonic force, and no independent translational Brownian noise. The two drives have different full path laws and higher-order force correlations; only second-order observables are matched. Their work functional is a specified mechanical active-work observable, not a full entropy-production identity. The analysis does not determine a global large-deviation rate function, treat interactions, or cover non-exponential rest durations. Scientific originality is based on the specifically inspected literature and comparisons, not a proof of publication priority; independent scientific review has not been performed.

## References

1. A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578, initial public version 2024-09-01, https://arxiv.org/abs/2409.00578.
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083, initial public version 2019-10-22, https://arxiv.org/abs/1910.10083.
3. M. Semeraro, G. Gonnella, A. Suma, M. Zamparo, *Work fluctuations for a harmonically confined Active Ornstein-Uhlenbeck Particle*, arXiv:2302.12535, initial public version 2023-02-24, https://arxiv.org/abs/2302.12535.
