# Exact greedy survival and terminal abundance in a symmetric hierarchical ecological chain

## Finding
Consider the deterministic hierarchical May–Leonard mean-field model with \(N\geq1\) species arranged in a directed path. If every species has the same reproduction rate \(r\), the same mortality rate \(d\), and every directed predation coefficient is strictly positive, then for \(r>d>0\) **every nonempty nonnegative initial community converges exponentially to one equilibrium**. Its surviving species are determined exactly by the *left-to-right greedy selection* of the initially occupied sites: select the smallest occupied index, remove its immediate successor if occupied, and repeat with the next still-eligible occupied index. All selected species retain strictly positive limiting densities, and all other species have zero limiting densities. The result applies for arbitrarily many species, all positive predation strengths, and all initial population magnitudes.

In particular, a full-support community converges to coexistence of species \(1,3,5,\ldots\), with every even-indexed species becoming extinct. The limiting total population is \(K=1-d/r\). In the three-species full-support case, put
\[
R=\frac{x_3(0)}{x_1(0)}\exp\!\left(-\frac{p_2x_2(0)}{p_1x_1(0)}\right).
\]
Then the limit is exactly
\[
\lim_{t\to\infty}(x_1(t),x_2(t),x_3(t))
=\left(\frac{K}{1+R},0,\frac{KR}{1+R}\right).
\]
The **survivor set**, unlike the final surviving abundances, does not depend on the numerical values of the positive predation coefficients.

## Assumptions and scope
For \(i=1,\ldots,N\), let \(x_i(t)\) denote species density, \(T(t)=\sum_{j=1}^Nx_j(t)\), and set \(p_0x_0(t)=0\). Consider
\[
\dot x_i=x_i\bigl[r(1-T)-d-p_{i-1}x_{i-1}\bigr],
\qquad r>d>0,\quad p_i>0\ (1\leq i<N).
\]
All initial states satisfy \(x_i(0)\geq0\) and \(0<T(0)\leq1\), so the nonnegative unit-population simplex is forward invariant. Let \(H=\{i:x_i(0)>0\}\). Define \(G\subseteq H\) by scanning indices in increasing order, accepting a present index unless its immediate predecessor was accepted. This is the *first-available* greedy independent subset of the directed path; it is not an arbitrary independent set and is not a stochastic graph algorithm.

The theorem concerns a deterministic, well-mixed, fixed-parameter ODE with homogeneous reproduction and death rates. It does not assume equal predation rates. The claim does not cover heterogeneous demographic rates, stochastic finite-site trajectories, mutation or migration, or continuously replenished absent species.

## Proof
**Step 1 (invariance and a uniform nonextinction bound).** The species coordinate faces are invariant. At \(T=1\),
\[
\dot T=-d-\sum_{i=1}^{N-1}p_ix_ix_{i+1}<0,
\]
so the simplex is invariant. Let \(a=r-d>0\), \(P(t)=\sum_{i=1}^{N-1}p_ix_ix_{i+1}\), and \(p_*:=\max(\{p_1,\ldots,p_{N-1}\}\cup\{0\})\). Then
\[
\dot T=aT-rT^2-P(t),\qquad 0\leq P(t)\leq p_*T(t)^2.
\]
Scalar logistic comparison gives the uniform bound
\[
T(t)\geq T_*:=\min\!\left\{T(0),\frac{a}{r+p_*}\right\}>0
\quad(t\geq0).
\]

**Step 2 (a triangular exact time change).** Put \(m=\min H\). Earlier coordinates vanish identically; the \(m\)-th coordinate has no extant predator. For \(i\geq m\), define \(u_i(t)=x_i(t)/x_m(t)\), so \(u_m=1\). Direct logarithmic differentiation gives, for each \(i>m\),
\[
\frac{d}{dt}u_i(t)=-p_{i-1}x_{i-1}(t)u_i(t).
\]
Thus every ratio \(u_i\) is nonincreasing, and
\[
\frac{x_m(t)}{T(t)}=\frac{1}{1+\sum_{i=m+1}^Nu_i(t)}
\geq\frac{x_m(0)}{T(0)}>0.
\]
Step 1 therefore implies \(x_m(t)\geq\delta:=T_*x_m(0)/T(0)>0\). The biological clock
\[
\tau(t)=\int_0^t x_m(s)\,ds
\]
strictly increases to infinity and satisfies \(\tau(t)\geq\delta t\). With derivatives now taken with respect to \(\tau\), the ratio equations become the autonomous triangular cascade
\[
\frac{du_i}{d\tau}=-p_{i-1}u_{i-1}u_i,
\qquad u_m\equiv1,\quad i=m+1,\ldots,N.
\]
In particular, for every initially present index \(i>m\),
\[
u_i(\tau)=u_i(0)\exp\!\left(-p_{i-1}\int_0^\tau u_{i-1}(s)\,ds\right).
\]

**Step 3 (inductive greedy selection and exponential convergence of ratios).** The baseline \(u_m\) is a positive constant. Suppose the status of all preceding indices has been determined, and every preceding positive-limit ratio converges exponentially while each zero-limit ratio either vanishes identically or decays exponentially. If \(u_i(0)=0\), then \(u_i\equiv0\). Otherwise, if the immediately preceding ratio tends to a positive limit, its integral diverges at least linearly; hence \(u_i\) decays exponentially. If instead the preceding ratio is identically zero or decays exponentially, its integral is finite, so the displayed formula gives \(u_i(\infty)>0\), approached exponentially. This completes induction for the finite chain. A present species survives if and only if its immediate predecessor was not selected, which is exactly \(G\). Every pair of adjacent indices has at least one exponentially vanishing ratio; since \(x_m\leq1\) and \(\tau\geq\delta t\), it follows that \(P(t)=O(e^{-\eta t})\) for some \(\eta>0\) depending on the initial condition and parameters.

**Step 4 (exact population limit and individual convergence).** Let \(K=a/r\), and \(E(t)=T(t)-K\). The exact identity
\[
\dot E=-rT(t)E-P(t)
\]
combined with \(T(t)\geq T_*>0\) and exponentially decreasing \(P\) gives \(E(t)\to0\) exponentially by variation of constants (a polynomial factor in a resonant estimate can be absorbed into a slower positive exponential). Each \(u_i(t)\) converges exponentially to a finite \(u_i^\infty\), with \(u_i^\infty>0\) precisely for \(i\in G\). Therefore
\[
\boxed{\displaystyle
\lim_{t\to\infty}x_i(t)=
\begin{cases}
K\,u_i^\infty\big/\sum_{j=m}^N u_j^\infty,&i\geq m,\\
0,&i<m.
\end{cases}}
\]
The ratios and \(T\) approach their limits exponentially, so every species density does as well. At the limit there are no adjacent positive populations and \(T=K\), which makes every right-hand side zero. Hence the limit is an equilibrium.

**Step 5 (closed form for three species).** For \(N=3\) and \(x_1(0),x_2(0),x_3(0)>0\), the triangular cascade yields
\[
 u_2(\tau)=\frac{x_2(0)}{x_1(0)}e^{-p_1\tau},\qquad
 u_3(\tau)=\frac{x_3(0)}{x_1(0)}
 \exp\!\left[-\frac{p_2x_2(0)}{p_1x_1(0)}(1-e^{-p_1\tau})\right].
\]
Consequently \(u_3^\infty=R\), \(u_2^\infty=0\), and Step 4 gives the exact displayed three-species formula.

## Verification
The derivation of the triangular equations uses exact cancellation of the common per-capita term. The nonextinction estimate and exponential ratio induction constitute the infinite-time argument; no finite simulation is used as a proof. The accompanying executable `verify_hierarchy.py` integrates the original equations with tight tolerances, checks the explicit three-species limit, and checks the predicted survivor sets and total population for full-support and boundary-support communities of three, five, six and seven species. It returned `VERIFY_OK` with Python, NumPy and SciPy. These numerical checks are diagnostic only.

## Relationship to prior work
Samanta, Dawn, Jahiruddin, Bhattacharyya, Hens and Nag Chowdhury (arXiv:2609.09027v1, September 8, 2026) introduce the directed hierarchical model, show the symmetric *equilibrium* independent-set restriction (Proposition 1), enumerate independent sets using Fibonacci numbers, and analyze local transverse stability and numerical outcomes. Their statements do not provide a trajectorywise global convergence proof, a support-determined greedy *selection* rule, or terminal abundance formula. This theorem is confined to their homogeneous-demography specialization; it does not claim that their unequal-rate numerical regimes follow the greedy rule.

Baigent and Ching (2020) establish attracting balance simplices for broader three-species May–Leonard flows. Attracting a simplex alone does not decide a unique limiting point on a continuum of equilibria or give the explicit surviving abundance split; their theorem does not imply the arbitrary-length greedy rule. Hou (2007) gives conditions for one *common* globally attracting equilibrium in competitive Lotka–Volterra systems. Such a single-point-attractor conclusion cannot apply directly when different full-support initial ratios yield distinct equilibria by the formula above. No claim is made that the underlying ratio reduction is a novel general technique.

## Limitations
The strict common \(r,d\) hypothesis is essential: with heterogeneous rates, log-ratios contain noncancelling terms, and the paper reports different long-run supports. If \(r\leq d\), logistic comparison instead forces total-population extinction, so the positive-limit theorem is inapplicable. If some \(p_i=0\), the corresponding forced exclusion may fail. Extremely small but positive selected populations can take a long time to become visible; full-support asymptotics must not be identified with finite-horizon numerical or finite-population stochastic survival. The theorem does not prove a uniform-in-initial-condition convergence rate. The precise relationship with every older competitive-system classification is not exhaustively settled by a literature search; previously unindexed statements could overlap.

## References
1. R. Samanta, S. Dawn, S. Jahiruddin, S. Bhattacharyya, C. Hens and S. Nag Chowdhury, *Selection Rules for Species Coexistence in a Hierarchical May–Leonard Model*, arXiv:2609.09027v1 (first posted 2026-09-08), https://arxiv.org/abs/2609.09027 ; accessible full text https://arxiv.org/html/2609.09027v1 .
2. S. Baigent and A. Ching, *Balance simplices of 3-species May–Leonard systems*, Journal of Biological Dynamics 14 (2020), 187–199, https://doi.org/10.1080/17513758.2020.1736656 ; open text https://discovery.ucl.ac.uk/id/eprint/10093501/ .
3. Z. Hou, *Global attractor in competitive Lotka–Volterra systems*, arXiv:0711.3385 (2007), https://arxiv.org/abs/0711.3385 .
