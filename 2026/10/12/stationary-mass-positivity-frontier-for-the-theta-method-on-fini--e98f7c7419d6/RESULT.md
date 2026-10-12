# Stationary-mass positivity frontier for the \(\theta\)-method on finite Markov generators

## Finding
Let \(Q\) be the row generator of an arbitrary **irreducible continuous-time Markov chain** on \(n\ge2\) states, with nonnegative off-diagonal entries and \(Q\mathbf1=0\). Write \(q_i=-Q_{ii}>0\), and let \(\pi\) be the unique strictly positive stationary probability row vector, \(\pi Q=0\). For \(0\le\theta\le1\), \(h>0\), the one-step \(\theta\)-method matrix is
\[
T_{\theta,h}=(I-\theta hQ)^{-1}(I+(1-\theta)hQ).
\]
Set \(\theta_c=1-\min_i\pi_i\) and \(R(s)=(I-sQ)^{-1}\). The **sharp probability-preservation classification** is as follows.

1. Explicit Euler (\(\theta=0\)) is entrywise nonnegative exactly for \(0<h\le1/\max_iq_i\).
2. For \(0<\theta<\theta_c\), there is exactly one positive finite threshold \(h_c(\theta)\), defined without ambiguity by
\[
\min_i R_{ii}(\theta h_c(\theta))=1-\theta.
\]
The matrix \(T_{\theta,h}\) is strictly entrywise positive for \(0<h<h_c(\theta)\), is nonnegative with at least one zero diagonal entry at equality, and has a negative diagonal entry for every \(h>h_c(\theta)\).
3. For \(\theta_c\le\theta\le1\), \(T_{\theta,h}\) is strictly entrywise positive and row-stochastic for **every finite** \(h>0\).

The threshold has a universal boundary-layer law. Define \(S=\{i:\pi_i=\min_j\pi_j\}\). Let \(H_i\) be the time to the first return to \(i\) **after the first departure from \(i\)**, starting the clock at that departure, and define
\[
c_i=\tfrac12\pi_i^2q_i\,\mathbb E[H_i^2],\qquad c_*=\min_{i\in S}c_i>0.
\]
Then
\[
\lim_{\theta\uparrow\theta_c}\theta_c(\theta_c-\theta)h_c(\theta)=c_*.
\]
Consequently, the all-step boundary depends only on the least stationary mass, whereas the finite threshold and its divergence constant depend on the transition geometry.

## Assumptions and scope
All assertions concern finite, irreducible continuous-time Markov generators in the **row-stochastic convention**. No reversibility, normality, diagonalizability, uniform rates, or graph symmetry is assumed. Zero off-diagonal rates are allowed so long as the directed transition graph is strongly connected. The step \(T_{\theta,h}\) advances row probability vectors on the right. Its inverse exists for every \(h>0\) and \(\theta>0\). The first-departure holding rate \(q_i\) and the post-departure return time \(H_i\) are defined separately; \(H_i\) excludes the original holding time at \(i\).

## Proof
**1. Resolvent reduction.** For \(s>0\), the Markov resolvent has the exponential-mixture representation
\[
R(s)=\int_0^\infty e^{-u}e^{suQ}\,du.
\]
Irreducibility gives \(R(s)_{ij}>0\) for all \(i,j\), and \(R(s)\mathbf1=\mathbf1\). For \(\theta>0\), elementary matrix algebra gives
\[
T_{\theta,h}=\frac1\theta R(\theta h)-\frac{1-\theta}{\theta}I.
\]
Hence every off-diagonal entry of \(T_{\theta,h}\) is strictly positive, its row sums equal one, and its nonnegativity is equivalent to
\[
\min_iR_{ii}(\theta h)\ge1-\theta.
\]
For \(\theta=0\), \(T_{0,h}=I+hQ\), which proves assertion 1.

**2. A regenerative identity valid without reversibility.** Fix a state \(i\). The first holding time \(E_i\) in that state is exponential with rate \(q_i\). By the strong Markov property, the time \(H_i\) from its first departure to its next return is independent of \(E_i\), strictly positive almost surely, and has finite moments of every order (finite irreducibility). The successive visits and departures form renewal cycles of duration \(E_i+H_i\), each with reward \(E_i\) spent at \(i\).

For Laplace parameter \(z>0\), let \(\phi_i(z)=\mathbb E[e^{-zH_i}]\). Summing the discounted holding-time reward over successive cycles gives
\[
\int_0^\infty e^{-zt}\Pr_i(X_t=i)\,dt
=\frac{\mathbb E[\int_0^{E_i}e^{-zt}\,dt]}{1-\mathbb E[e^{-z(E_i+H_i)}]}
=\frac1{z+q_i(1-\phi_i(z))}.
\]
Substituting \(z=1/s\) yields the exact diagonal resolvent formula
\[
\boxed{R_{ii}(s)=\frac1{1+q_is\bigl(1-\mathbb E[e^{-H_i/s}]\bigr)}}.
\]
This identity applies even to nonreversible, nonnormal directed generators.

**3. Strict monotonicity and stationary limit.** For each fixed \(u>0\), the function \(f_u(s)=s(1-e^{-u/s})\) is strictly increasing, since
\[
f_u'(s)=1-(1+u/s)e^{-u/s}>0.
\]
Thus every \(R_{ii}(s)\) is continuous and strictly decreasing for \(s>0\), with \(R_{ii}(0+)=1\). The renewal reward theorem or direct cycle averaging gives
\[
\pi_i=\frac{\mathbb E E_i}{\mathbb E E_i+\mathbb E H_i}
=\frac1{1+q_i\mathbb E H_i}.
\]
Dominated convergence in the diagonal formula therefore gives \(R_{ii}(s)\downarrow\pi_i\) as \(s\to\infty\), strictly above \(\pi_i\) for every finite \(s\).

**4. Sharp classification, including equality.** The continuous function \(s\mapsto\min_iR_{ii}(s)\) is strictly decreasing: for two arguments, choose an index attaining the earlier minimum and use strict decrease of that component. It decreases from one to \(\min_i\pi_i\), never reaching its limit at finite \(s\). Therefore for \(0<\theta<1-\min_i\pi_i\) it crosses \(1-\theta\) exactly once, and otherwise stays strictly above that level. Combining this with Step 1 proves assertions 2 and 3 and the exact boundary behavior. At the crossing at least one diagonal entry is zero, while all off-diagonal entries remain strictly positive.

**5. Critical-window asymptotic.** Because all return-time moments are finite, Taylor expansion with a dominated remainder yields
\[
s\bigl(1-\mathbb E[e^{-H_i/s}]\bigr)
=\mathbb E H_i-\frac{\mathbb E[H_i^2]}{2s}+O(s^{-2}).
\]
Using \(\pi_i=(1+q_i\mathbb EH_i)^{-1}\) in the exact resolvent identity gives
\[
R_{ii}(s)=\pi_i+\frac{c_i}{s}+O(s^{-2}).
\]
For \(\theta\) sufficiently close to \(\theta_c\) from below, states with \(\pi_i>\min_j\pi_j\) cannot determine the first crossing. Among the finitely many states in \(S\), the least \(c_i\) determines the leading correction. Substituting \(s=\theta h_c(\theta)\) into the crossing equation gives
\[
\theta_c-\theta=\frac{c_*}{\theta h_c(\theta)}+O(h_c(\theta)^{-2}),
\]
and the asserted limit follows because \(h_c(\theta)\to\infty\) and \(\theta\to\theta_c>0\).

**6. Same stationary probabilities, different cutoffs.** Two row generators on three states both have stationary distribution \((1/3,1/3,1/3)\): the one-way unit-rate cycle \(Q=P-I\), where \(P\) is the cyclic permutation, and the complete graph with unit-rate jumps \(Q=\mathbf1\mathbf1^{\mathsf T}-3I\). For the cycle,
\[
R_{ii}(s)=\frac{(1+s)^2}{1+3s+3s^2};
\]
for the complete graph,
\[
R_{ii}(s)=\frac13+\frac{2}{3(1+3s)}.
\]
Their common unconditional threshold is \(\theta_c=2/3\), but at \(\theta=1/2\) their sharp stepsize cutoffs are respectively \(1+\sqrt5\) and \(2\). Thus the stationary mass controls unconditional positivity but cannot determine the finite cutoff.

## Verification
Run the complete standalone standard-library checker with `python3 check_theta.py`. It forms exact rational generators, computes stationary distributions and post-departure return-time moments using absorbing subgenerator linear systems, checks the renewal-reward identity and the exact leading resolvent coefficient against a deviation-matrix computation, verifies strict monotonicity of sampled resolvent diagonals, and checks stochasticity, positivity conditions, and the two three-state contrasts by exact rational arithmetic. The completed run reported: `VERIFY_OK 63 irreducible generators; 2205 stationarity/return-moment/diagonal checks; 2205 exact-rational theta matrices; two distinct cutoffs at common stationary law`. No finite test is used as a proof of the universal statement.

## Relationship to prior work
Horváth (1998, 2005) treats positivity thresholds for Runge–Kutta methods over broad classes of positive differential equations, particularly through absolute-monotonicity radii; the present theorem instead fixes an arbitrary **conservative irreducible Markov generator** and finds its exact all-steps boundary from its stationary law. Ferracina and Spijker (2005) study optimal monotonicity-preserving Runge–Kutta representations rather than this chain-specific diagonal-resolvent classification. Higueras and Roldán (2023) obtain sharp positivity cutoffs for particular heat-equation discretizations with boundary conditions; their nonconservative matrices do not imply the stationary-mass theorem. The direct Cayley-transform reduction for Crank–Nicolson on arbitrary finite Markov generators, and its reversible spectral threshold analysis, are also prior: the present proof does not claim this linear-algebra reduction as new. Birth–death and one-way-cycle analyses supply further prior specialized instances, including the cycle boundary law. The present contribution is the all-parameter and all-generator classification, including strict monotonicity for nonreversible chains and the general return-time moment asymptotic.

## Limitations
The theorem concerns one endpoint map of the \(\theta\)-family, not stage positivity, local truncation error, higher-order Runge–Kutta schemes, reducible generators, or countably infinite chains. For general generators, the finite cutoff is characterized by a strictly monotone resolvent equation; a closed expression in radicals is not asserted. The critical-window coefficient requires the second moment of post-departure return times. The mathematical proof is complete within its stated finite irreducible setting, but completeness of historical novelty searches cannot be guaranteed.

## References
1. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356; available online 27 October 2004. DOI: `10.1016/j.apnum.2004.08.026`.
2. Z. Horváth, *Positivity of Runge-Kutta and diagonally split Runge-Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326. DOI: `10.1016/S0168-9274(98)00050-6`.
3. L. Ferracina and M. N. Spijker, *Computing optimal monotonicity-preserving Runge-Kutta methods*, Leiden report dated 7 April 2005, `https://math.leidenuniv.nl/reports/files/2005-07.pdf`.
4. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation*, preprint of 3 January 2023, `arXiv:2301.01066`.
