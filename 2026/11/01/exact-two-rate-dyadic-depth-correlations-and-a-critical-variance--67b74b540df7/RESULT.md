# Exact two-rate dyadic-depth correlations and a critical variance crossover in a random interval map

## Finding

For the non-expanding/expanding random interval-map pair defined below, the stationary dyadic-depth observable has an exact **two-exponential** autocovariance at every lag. Put \(q=1-\alpha\), \(s=1-q/2\), \(r=(1-q)/2\) and \(B=2q(1-q)/(1+q)^2\). For every integer \(n\geq0\),
\[
\operatorname{Cov}(K_0,K_n)=2s^n+Br^n.
\]
The centered depth sums \(S_N=\sum_{t=0}^{N-1}(K_t-2/(1+q))\) consequently have exact finite-time variance
\[
\operatorname{Var}(S_N)=2R_N(s)+BR_N(r),\qquad
R_N(z)=\frac{N(1+z)}{1-z}-\frac{2z(1-z^N)}{(1-z)^2}.
\]
For every fixed \(0<q\leq1\), a stationary central limit theorem holds:
\[
\frac{S_N}{\sqrt N}\ \Longrightarrow\ \mathcal N(0,\sigma^2(q)),\qquad
\sigma^2(q)=\frac8q-2+\frac{2q(1-q)(3-q)}{(1+q)^3}.
\]
In particular \(q\sigma^2(q)\to8\) as \(q\downarrow0\). More sharply, for any sequence \(q_N>0\) with \(q_N\to0\) and \(Nq_N\to t\in[0,\infty)\), with a separate stationary start at each parameter,
\[
\lim_{N\to\infty}\frac{\operatorname{Var}(S_N)}{N^2}
=F(t)=4\int_0^1(1-u)e^{-tu/2}\,du
=\begin{cases}2,&t=0,\\
16\bigl(t/2-1+e^{-t/2}\bigr)/t^2,&t>0.
\end{cases}
\]
The crossover \(F(t)\sim8/t\) for large \(t\) connects the quadratic-time and diffusive-time variance regimes.

## Assumptions and scope

Fix \(0\leq\alpha<1\) and set \(q=1-\alpha>0\). At each discrete time independently choose \(\tau_1\) with probability \(\alpha\) or \(\tau_2\) with probability \(q\):
\[
\tau_1(x)=\begin{cases}x,&0\leq x\leq1/2,\\2x-1,&1/2<x\leq1,\end{cases}
\qquad
\tau_2(x)=\begin{cases}2x,&0\leq x\leq1/2,\\2x-1,&1/2<x\leq1.\end{cases}
\]
The choices at dyadic endpoints are immaterial for the absolutely continuous stationary law. The state \(X_0\) is sampled from the absolutely continuous stationary probability whose density is \(2/(1+q)\) on \([0,1/2)\) and \(2q/(1+q)\) on \([1/2,1)\). The density is a previously known result, independently checked by the two-cell balance equations. Define the integer dyadic depth, away from dyadic endpoints of stationary measure zero, by
\[
K_t=k\quad\Longleftrightarrow\quad 2^{-k-1}<X_t\leq2^{-k},\qquad k\in\{0,1,2,\ldots\}.
\]
All covariance, central-limit and crossover assertions are **annealed** (jointly over the stationary initial point and independent map choices). They are not claimed for the singular stationary measures at \(\alpha=1\), for fixed individual initial points, or for quenched random environments.

## Proof

**1. Countable Markov coding.** The invariant density is constant inside each dyadic cell. Conditional on the entire history of observed depths, the remaining binary suffix of the current point is uniform: this follows inductively since identity leaves a conditional uniform dyadic-cell law unchanged, while either doubling branch maps a restricted dyadic interval affinely and uniformly onto the next cell. Therefore \(K_t\) is a countable-state Markov chain with transition probabilities
\[
P(0,j)=2^{-j-1}\quad(j\geq0),\qquad
P(k,k)=1-q,\quad P(k,k-1)=q\quad(k\geq1).
\]
The level zero transition resets to a geometric depth; on positive levels the chain holds with probability \(1-q\) or descends by one. Its strictly positive stationary distribution, checked by direct balance, is
\[
\pi_0=\frac q{1+q},\qquad \pi_k=\frac{2^{-k}}{1+q}\quad(k\geq1).
\]
The chain is irreducible and aperiodic for \(q>0\). Its stationary mean and variance are
\[
m=\mathbb E_\pi K=\frac2{1+q},\qquad
v=\operatorname{Var}_\pi(K)=\frac{2(3q+1)}{(1+q)^2}.
\]

**2. Exactly two covariance modes.** Define summable signed row vectors \(w\) and \(v_*\) by
\[
w_k=\pi_k(k-m),\qquad
(v_*)_0=-\frac1{1+q},\quad(v_*)_k=\pi_k\ (k\geq1).
\]
Direct substitution in the transition probabilities, separately at level zero and levels \(k\geq1\), gives
\[
v_*P=rv_*,\qquad wP=sw+dv_*,\qquad
d=\frac{q(1-m)}2,\quad s-r=\frac12.
\]
It follows without truncating the infinite chain that
\[
wP^n=s^n w+\frac{d}{s-r}(s^n-r^n)v_*.
\]
Pair with the depth column \((0,1,2,\ldots)^{\mathsf T}\). The pairings are \(\langle w,k\rangle=v=2+B\) and \(\langle v_*,k\rangle=m\), while \(2dm=-B\). Consequently
\[
\operatorname{Cov}(K_0,K_n)=\langle wP^n,k\rangle=2s^n+Br^n
\]
for every \(n\geq0\), including the boundary and the deterministic doubling case \(q=1\).

**3. Variance and limit theorem.** Stationarity implies
\[
\operatorname{Var}(S_N)=NC_0+2\sum_{j=1}^{N-1}(N-j)C_j.
\]
Substituting the two geometric modes and summing yields the displayed \(R_N\) formula. Both mode factors have modulus less than one for every fixed \(q>0\); hence the Green–Kubo sum \(C_0+2\sum_{j\geq1}C_j\) converges and reduces to the stated \(\sigma^2(q)\).

For completeness, define \(h(0)=0\) and, for \(k\geq1\),
\[
h(k)=\frac{k(k+1)/2-mk}{q}.
\]
The identity \((I-P)h(k)=k-m\) holds at every positive level by direct subtraction. At level zero, use the geometric reinjection moments \(\mathbb E J=1\), \(\mathbb E[J(J+1)/2]=2\) and \(qm=2-m\) to obtain the same identity. Thus \(S_N\) is the sum of a square-integrable stationary martingale difference sequence and the telescoping boundary \(h(K_0)-h(K_N)\). The latter is \(o_{\mathbb P}(\sqrt N)\) by stationarity and the geometric tails; the martingale central limit theorem applies because the chain is stationary ergodic with finite polynomial moments. Its variance agrees with the Green–Kubo limit by the covariance formula and the same boundary control.

**4. Critical finite-window crossover.** In the triangular regime \(q_N\to0\), \(Nq_N\to t\), uniformly for \(0\leq u\leq1\) along the grid, \((1-q_N/2)^{\lfloor Nu\rfloor}\to e^{-tu/2}\). The fast-mode coefficient \(B=O(q_N)\) and \(0\leq r\leq1/2\), so its contribution to the variance divided by \(N^2\) tends to zero. The slow-mode covariance sum is a Riemann sum converging to \(4\int_0^1(1-u)e^{-tu/2}du\). Elementary integration gives the explicit piecewise formula and its two endpoint limits.

## Verification

The included standalone `verify.py` uses exact SymPy arithmetic to check the stationary moments, both row-vector transition identities (including their reinjection boundaries), the quadratic Poisson equation at all levels, the coefficients of the exact two-mode covariance, the rational asymptotic variance, twenty independently summed exact rational finite-time variance instances, and the critical variance constant. Execution produced a `PASS` message with all assertions satisfied. The infinite-time central limit theorem and triangular-array crossover rest on the arguments above, not on finite experiments.

## Relationship to prior work

Maldonado and Pérez Otero (2021) introduced this random map and established the absolutely continuous stationary density; Pérez Otero's 2023 thesis, Chapter 4, Section 4.4 (printed pages 49–52), gives the same maps and density explicitly. Those results are used as background, not claimed as new. The thesis's Section 4.5.6 considers numerical correlations for **another** randomly parameterized map exhibiting a phase transition. General results about stationary Markov chains and martingale central limit theorems are also established background. The asserted new content is the complete **unbounded dyadic-depth** covariance sequence, exact finite-time variance, and critical crossover for the specific 2021 map. Neither the published description nor the accessible thesis material examined reports those formulas. Related coordinate-observable calculations do not imply the formulas for this singular depth observable; the renewal structure here is a distinct countable-state representation rather than the two-cell density transfer matrix.

## Limitations

The source article's complete publisher text was not accessible for direct comparison; the accessible author's thesis reproduces the model and stationary-density analysis but cannot rule out an uninspected discussion in the original article. Independent prior-art searching and exact implication checks reduce but do not eliminate publication-priority risk. No quenched central limit theorem or uniform-in-parameter fixed-start limit theorem is claimed. For \(q=0\), irreducibility fails and the family has additional invariant measures; the formulas describe only the limit from \(q>0\).

## References

1. C. Maldonado and R. A. Pérez Otero, *Phase transition in piecewise linear random maps in the interval*, Chaos 31 (2021), 093112. DOI: `10.1063/5.0051242`.
2. R. A. Pérez Otero, *Invariant densities and phase transition phenomenon in random maps in the interval*, doctoral thesis, IPICYT (2023), Chapter 4, Section 4.4. Repository handle `11627/5859`.
3. S. Pelikan, *Invariant densities for random maps of the interval*, Transactions of the American Mathematical Society 281 (1984), 813–825. DOI: `10.2307/2000087`.
