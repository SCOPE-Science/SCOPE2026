# Thermal inequality monotonicity and light-tailed equilibrium in a bounded trap-diffusion wealth model

## Finding

Let a cycle of \(L\ge3\) sites have fixed depths \(\phi_i\in[0,1]\) and a total of \(M\ge2\) tracked but economically identical money units. Each unit, independently of all others, proposes a move to either neighboring site with probability \(1/2\) and accepts a proposal from \(i\) to \(j\) with probability \(a_{ij}=\min\{1,e^{(\phi_j-\phi_i)/T}\}\), at \(T>0\). For definiteness use independent rate-one continuous-time attempt clocks. The unique stationary wealth counts are
\[
X\sim\operatorname{Multinomial}(M;p_1(T),\ldots,p_L(T)),\qquad
p_i(T)=\frac{e^{\phi_i/T}}{\sum_j e^{\phi_j/T}}.
\]
The same law is the unique stationary law if, instead, one label is chosen uniformly at random per discrete attempt, or if each label attempts once at each discrete tick and the single-unit chain is aperiodic. In both discrete protocols for nonconstant depths, counts also converge to it from any start. For equal depths, simultaneous non-lazy updates on an even cycle leave the multinomial law invariant but do not in general make it unique or yield convergence. Uniform one-label-at-a-time updates on an even cycle are irreducible and retain uniqueness, but periodicity can prevent convergence; independent continuous-time attempt clocks avoid both exceptional behaviors.

For the random sampled Gini coefficient and vacant-site fraction
\[
G(X)=\frac{1}{LM}\sum_{i<j}|X_i-X_j|,\qquad V(X)=\frac{1}{L}\sum_i\mathbf1_{\{X_i=0\}},
\]
the expectations under the multinomial equilibrium are strictly decreasing in \(T\) for every nonconstant depth vector. This strict ordering also holds when averaged over a temperature-independent distribution supported on nonconstant depths. At high temperature the limits are the uniform-multinomial expectations. If there is a unique deepest site, both expectations tend to \((L-1)/L\) as \(T\downarrow0\).

If the depths are independent uniform draws on \([0,1]\), \(M_L/L\to m\in(0,\infty)\), and \(T>0\) is fixed, the equilibrium fraction of sites with count \(k\) tends in probability, for every integer \(k\ge0\), to
\[
q_T(k)=\int_0^1 e^{-\lambda_T(u)}\frac{\lambda_T(u)^k}{k!}\,du,
\qquad \lambda_T(u)=\frac{m e^{u/T}}{T(e^{1/T}-1)}.
\]
Putting \(\Lambda_T=\lambda_T(1)\), for \(k>\Lambda_T\) the upper tail satisfies \(\sum_{j\ge k}q_T(j)\le (e\Lambda_T/k)^k\). This rules out an asymptotic Pareto tail in this equilibrium limit.

## Proof

### Invariance, uniqueness and update protocols

For \(r_i=e^{\phi_i/T}\), the single-unit edge flux satisfies \(r_i a_{ij}/2=r_j a_{ji}/2=\min(r_i,r_j)/2\). The single-unit chain is irreducible since both rates on every edge are positive. For independent clocks the labelled chain is irreducible by moving the labels one at a time along paths in the cycle; its invariant law is the product of the single-unit Gibbs probabilities. The same argument with one-label-per-step transitions gives irreducibility in discrete time. Equivalently the continuous-time count rates \(x_i a_{ij}/2\) satisfy detailed balance with the multinomial law; the discrete one-label count probabilities are those rates divided by \(M\) on off-diagonal moves. Thus both count chains have the unique stated stationary law. When the depths are nonconstant there exists an edge with unequal depths, giving a self-loop at its higher-depth endpoint and an aperiodic single-unit kernel. Consequently the simultaneous product kernel is irreducible and aperiodic (a finite irreducible aperiodic kernel has all entries positive at sufficiently large powers). For uniform one-label updates there is also a self-loop at some labelled state and hence aperiodicity by irreducibility.

Equal-depth odd cycles are aperiodic, by their two-step returns and odd cycle. For equal depths and an even cycle, an independent simultaneous step reverses every unit's site parity, so their relative parities are conserved. For \(M=2\), the two closed classes of equal and opposite site parities have stationary laws given by the uniform product conditioned on the class. They give distinct occupancy laws, since in one class both units are on sites of the same parity and in the other they are on sites of opposite parity. More generally, for \(M\ge2\) the event that all units have the same parity is invariant and has nontrivial product probability, and conditioning on it or its complement gives distinct stationary occupancy laws. Under equal-depth one-label discrete updates on an even cycle, each update instead flips the parity of the total number of units on even sites, allowing periodicity but not loss of irreducibility.

### Thermal monotonicity

Sort depths in decreasing order and let \(b=1/T\) and \(S_k=\sum_{i\le k}p_i\). For each \(1\le k<L\), differentiation gives
\[
\frac{dS_k}{db}=S_k(1-S_k)\bigl(\overline\phi_{\le k}-\overline\phi_{>k}\bigr),
\]
where both averages use their groups' conditional Gibbs probabilities. This is nonnegative, and some partial sum strictly increases for nonconstant depths, so the colder vector majorizes the warmer one and is not a permutation of it. The mean vacancy is \(L^{-1}\sum_i(1-p_i)^M\), strictly Schur-convex on the positive simplex for \(M\ge2\).

For the sampled Gini numerator hold all other probabilities and the sum \(s=p_a+p_b\) fixed, and vary \(q=p_a/s\). Condition on the pair total \(R=X_a+X_b\) and all other counts \(Y_j\). Their law does not depend on \(q\), and \(X_a\) is conditionally \(\operatorname{Binomial}(R,q)\). The part of the numerator depending on \(X_a=t\) is
\[
h(t)=|2t-R|+\sum_{j\ne a,b}\bigl(|t-Y_j|+|R-t-Y_j|\bigr).
\]
It is convex and symmetric under \(t\mapsto R-t\). The second derivative of its binomial average is \(R(R-1)\) times the average of the second forward differences of \(h\) with respect to \(\operatorname{Binomial}(R-2,q)\), for \(R\ge2\). Every difference is nonnegative, and at least one is positive by the kink in \(|2t-R|\); every weight is positive for \(0<q<1\). Thus the binomial average is strictly increasing in \(|q-1/2|\) when \(R\ge2\); for \(R<2\) it is constant. Since \(\Pr(R\ge2)>0\) for \(M\ge2\), every genuine pair balancing strictly lowers the mean Gini numerator. Successive pair balancings characterize majorization, proving strict decrease of the expected sampled Gini with \(T\). This is not the Gini coefficient of the vector of mean wealths. Both averages are constant for \(M=1\) or constant depths under the multinomial law. The temperature endpoints follow by taking the corresponding Gibbs limits; strict inequalities can be averaged over any fixed ensemble of nonconstant depths.

### Fixed-temperature population limit

The law of large numbers gives \(L^{-1}\sum_j e^{\phi_j/T}\to c_T=T(e^{1/T}-1)\). Conditional on the depths each \(X_i\) is binomial, \(p_i\le e^{1/T}/L\), and \(M_Lp_i\) is uniformly close to \(\lambda_T(\phi_i)\). The binomial-to-Poisson error is at most \(2M_Lp_i^2=O(1/L)\). Averaging the conditional occupation probabilities and using the law of large numbers proves convergence of the conditional expected fraction to \(q_T(k)\). Changing one of the independent Gibbs-drawn labels changes that fraction by at most \(2/L\); Efron–Stein therefore bounds its conditional variance by \(2M_L/L^2\). This gives convergence in probability. Every Poisson mean in the limit is at most \(\Lambda_T\). The Poisson Chernoff bound yields the stated upper bound uniformly over the means; it is super-exponential in \(k\).

## Reproduction and scope

The accompanying unchanged `verify.py` computes count-process detailed balance and independently checks the pair-binomial formulas, temperature ordering and a finite-size vacancy diagnostic. These are checks of the multinomial equilibrium, not of uniqueness for the periodic simultaneous update. For example \((1,2,4)\) Gibbs weights and \(M=4\) give \(\mathbb E G=134/343\) and \(\mathbb E V=286/1029\). The full quantifiers and tail bound use the proof above.

Aydiner, *A New Model for the Income Distribution*, arXiv:2610.08143v1, Sections III–V, motivates the rule with quenched depths, the stated Metropolis acceptance probability and finite-run vacancy, Gini and wealth-distribution profiles. The theorem explicitly stipulates symmetric proposals and treats independent labelled units, not a general pair-transaction interpretation of that model. Section IV runs a prescribed number of steps per particle, whereas the theorem is about the invariant law of the specified chain. It claims no mixing rate and does not contradict fitted Pareto ranges or nonmonotonic curves in finite-time data. There are no interactions, income changes, debts or saving-propensity exchanges, and the tail limit is not uniform as \(T\downarrow0\) with system size. The stationary-law, majorization and Poisson tools themselves are standard; the comparison concerns the exact finite-sample observables and limiting distribution in this model.
