# Sharp periodic reversal-budget bounds for active-particle diffusivity

## Finding

A particle moving on the real line at speed \(v>0\) with velocity sign reversed at the event times of an inhomogeneous Poisson process may be driven by a nonnegative, measurable, \(T\)-periodic reversal rate \(\lambda\). Write \(\Lambda=\int_0^T\lambda(s)\,ds>0\) for the fixed number of expected reversals per period. Its long-time diffusivity \(D=\lim_{t\to\infty}\operatorname{Var}(X_t)/(2t)\) exists and obeys the **sharp complete rate-allocation bounds**

\[
\boxed{\frac{v^2T}{2\Lambda}\ \leq\ D[\lambda]\ <\ \frac{v^2T}{2}\coth\Lambda.}
\]

The lower bound is attained **if and only if** \(\lambda(t)=\Lambda/T\) for almost every \(t\). The upper bound is a strict supremum over integrable protocols: it is approached by concentrating the entire reversal budget into a single progressively shorter time window each period. In the enlarged class of periodic atomic hazard measures, it is attained by one impulse per period. Thus clustering reversals in time can enhance spreading by a factor approaching \(\Lambda\coth\Lambda\) relative to the homogeneous reversal schedule with the same reversal budget and period.

## Assumptions and scope

Fix any real \(v,T,\Lambda>0\). Let \(\lambda:\mathbb R\to[0,\infty)\) be Lebesgue-measurable and \(T\)-periodic almost everywhere, with \(\lambda\in L^1([0,T])\) and period integral \(\Lambda\). Let \(N(t)\) be an inhomogeneous Poisson counting process with deterministic rate \(\lambda(t)\), independent of \(S_0\), where \(\Pr(S_0=+1)=\Pr(S_0=-1)=1/2\). Define \(S_t=S_0(-1)^{N(t)}\) and \(X_t=v\int_0^t S_s\,ds\), for \(t\ge0\). The variance and asymptotic diffusion coefficient refer to this unbiased ensemble, with no boundaries, obstacles, translational Brownian noise, or feedback. The observation clock is ordinary physical time, not period count. At a Poisson event, the sign **reverses**, rather than being redrawn independently.

## Proof

**1. Two-time covariance.** The Poisson parity generating function gives, for \(0\le s\le t\),
\[
\mathbb E[S_sS_t]=\mathbb E[(-1)^{N(t)-N(s)}]
=\exp\!\left(-2\int_s^t\lambda(r)\,dr\right).
\]
The initially unbiased sign implies \(\mathbb E[X_t]=0\) at all times. Integrating the covariance over the square yields
\[
\operatorname{Var}(X_t)=2v^2\int_0^t ds\int_0^{t-s}du\,
\exp\!\left(-2\int_s^{s+u}\lambda(r)\,dr\right).
\]
For every \(s\), a time interval of length \(u\) contains at least \(\lfloor u/T\rfloor\) complete periods of rate integral \(\Lambda\). Thus the exponential is bounded by \(\exp(-2\Lambda\lfloor u/T\rfloor)\), uniformly integrable in \(u\). Dominated convergence for the upper integration limit and averaging over a periodic variable establish
\[
D[\lambda]=\frac{v^2}{T}\int_0^Tds\int_0^\infty du\,
\exp\!\left(-2\int_s^{s+u}\lambda(r)\,dr\right).
\]
Put \(M_s(w)=\int_s^{s+w}\lambda(r)\,dr\) for \(0\le w\le T\). Splitting \(u=kT+w\), \(k\ge0\), and summing a geometric series gives the exact identity
\[
\boxed{D[\lambda]=\frac{v^2}{T(1-e^{-2\Lambda})}
\int_0^Tdw\,\frac1T\int_0^Tds\,T e^{-2M_s(w)}.}
\]
Equivalently, \(D[\lambda]=v^2[1-e^{-2\Lambda}]^{-1}\int_0^T A(w)\,dw\), where \(A(w)=T^{-1}\int_0^T e^{-2M_s(w)}\,ds\).

**2. Exact deterministic budget identity.** Periodicity and Fubini give
\[
0\le M_s(w)\le\Lambda,\qquad
\frac1T\int_0^T M_s(w)\,ds=\frac{\Lambda w}{T}
\quad(0\le w\le T).
\]
The bounds hold without any smoothness or positivity lower bound on the rate.

**3. Sharp lower and upper bounds.** Strict convexity of \(x\mapsto e^{-2x}\) and Jensen yield \(A(w)\ge e^{-2\Lambda w/T}\). On the interval \([0,\Lambda]\), the graph of the same convex function lies below the chord through its endpoints, giving
\[
A(w)\le1-\frac wT(1-e^{-2\Lambda}).
\]
The two integrations over \(0\le w\le T\) are elementary and yield
\[
\frac{v^2T}{2\Lambda}\le D[\lambda]
\le\frac{v^2T}{2}\frac{1+e^{-2\Lambda}}{1-e^{-2\Lambda}}
=\frac{v^2T}{2}\coth\Lambda.
\]
If the lower equality holds, equality in Jensen holds for almost every interval length \(w\). Choose such lengths decreasing to zero. The corresponding constant phase averages \(M_s(w)/w\) converge at every Lebesgue point to \(\lambda(s)\), so \(\lambda\) is constant almost everywhere. Conversely, the constant rate attains the lower bound. For the upper bound, absolute continuity of the Lebesgue integral makes \(M_s(w)<\Lambda\) uniformly in \(s\) for all sufficiently small \(w>0\). Its phase average is strictly positive, hence \(0<M_s(w)<\Lambda\) on a positive-measure set of phases. The convex-chord inequality is then strict after phase averaging and integration: no admissible \(L^1\) rate attains the upper bound.

**4. Sharp upper-limit construction.** For \(0<\varepsilon<1\), set \(\lambda_\varepsilon=\Lambda/(\varepsilon T)\) on \([0,\varepsilon T)\) modulo \(T\), and zero elsewhere. For fixed \(0<w<T\), the interval hazard \(M_s(w)\) converges almost everywhere in phase to \(\Lambda\) when the interval crosses the selected periodic point, and to zero otherwise. The crossing fraction is \(w/T\), whence \(A_\varepsilon(w)\to1-(w/T)(1-e^{-2\Lambda})\). Dominated convergence proves \(D[\lambda_\varepsilon]\to(v^2T/2)\coth\Lambda\). This is only a limiting impulsive protocol; no finite-width protocol is asserted to attain it.

## Verification

The accompanying `periodic_flip_checker.py` independently evaluates the diffusivity of piecewise-constant rates using an exact periodic backward-resolvent recursion and, for selected cases, a separate two-time-covariance double quadrature. It compares 144 seeded random positive/zero rate allocations, several exact homogeneous benchmarks, and increasingly narrow pulsed protocols with the claimed bounds. The checker reports 188 passing deterministic assertions. These finite numerical tests corroborate formulas; the all-rate inequality and equality characterizations are established by the preceding measure-theoretic proof, not by sampling.

## Relationship to prior work

Classical run-and-tumble and telegraph motions, including long-time diffusion at stationary tumbling parameters, predate this analysis; see [1] and [2]. Work on transient dispersal [3] calculates asymptotic diffusivity in a discrete-time model with fixed state-transition probabilities and velocity persistence. Those established results do not imply, by a parameter substitution alone, both sharp bounds for **arbitrary deterministic periodic time modulation** with an integral reversal budget, or the singular concentrating optimizer. The present claim is only this complete temporal allocation theorem, not a first derivation of telegraph motion, velocity correlation, or homogeneous diffusivity.

## Limitations

The model requires nonnegative periodic intensity with a strictly positive finite period integral, unbiased initial velocity signs, and instantaneous sign flips. The upper optimizer does not lie in the stipulated \(L^1\) control class; its equality interpretation requires an enlarged measure-valued impulse model. The theorem neither covers stochastic feedback in the rate, orientation-redrawing tumbling, spatial confinement, interacting swimmers nor finite-horizon transport-optimal protocols. A prior equivalent result under another representation cannot be excluded without exhaustive historical review.

## References

[1] M. E. Cates and J. Tailleur, “When are active Brownian particles and run-and-tumble particles equivalent?”, arXiv:1206.1805v1 (8 June 2012). https://arxiv.org/abs/1206.1805.
[2] A. P. Solon, M. E. Cates and J. Tailleur, “Active Brownian Particles and Run-and-Tumble Particles: a Comparative Study”, arXiv:1504.07391v1 (28 April 2015). https://arxiv.org/abs/1504.07391.
[3] M. R. Shaebani and H. Rieger, “Transient Anomalous Diffusion in Run-and-Tumble Dynamics”, Frontiers in Physics 7, 120 (2019). https://doi.org/10.3389/fphy.2019.00120.
