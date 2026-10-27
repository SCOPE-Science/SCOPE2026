# A universal deadline-independent sentinel ranking on stars and a sharp discrete-time reversal

## Finding
Consider stochastic susceptible–infected (SI) infection on an \(n\)-vertex star with one uniformly random initial infected vertex, perfect instantaneous monitoring of exactly \(k\) vertices, and independent successful edge transmissions per step with probability \(p\in(0,1)\). Assume integers \(n\ge3\) and \(2\le k\le n-1\). Write \(q=1-p\), \(r=n-k\), and \(S_k(q)=\sum_{j=0}^{k-1}q^j\).

There are just two monitor-placement types under star automorphisms: \(H\), containing the hub and \(k-1\) leaves; and \(L\), containing \(k\) leaves and omitting the hub. Let \(T_H,T_L\) be the first monitoring times, counting the initially infected vertex at time zero. For every integer \(t\ge0\),
\[
\Pr(T_H\le t)-\Pr(T_L\le t)=
\frac{\bigl(r-S_k(q)\bigr)(1-q)(q^t-q^{kt})}{n(q-q^k)}.
\]
For every finite \(t\ge1\), the sign of this difference is therefore independent of the horizon. The arrangement with larger cumulative detection probability is first-order stochastically earlier; it optimizes *every* finite detection deadline and every nondecreasing cost of detection delay, including expected delay. In particular,
\[
\mathbb E[T_L]-\mathbb E[T_H]=\frac{r-S_k(q)}{n(1-q^k)}.
\]

This yields a complete sharp classification:

1. If \(r=1\), monitoring \(k\) leaves is strictly better than including the hub for every \(0<p<1\).
2. If \(r\ge k\), including the hub is strictly better for every \(0<p<1\).
3. If \(1<r<k\), there is a unique \(q_*\in(0,1)\) satisfying \(\sum_{j=0}^{k-1}q_*^j=r\). Write \(p_*=1-q_*\). Including the hub is strictly better when \(p>p_*\), monitoring only leaves is strictly better when \(p<p_*\), and both placement types have identical complete detection-time distributions when \(p=p_*\).

The smallest population with a transmission-dependent switch is \(n=5,k=3\): here \(p_*=(3-\sqrt5)/2\). At \(p=2/5\), \(\mathbb E[T_L]-\mathbb E[T_H]=1/98\); at \(p=1/3\) the difference equals \(-3/95\).

In the analogous continuous-time SI process with independent rate-\(\beta>0\) exponential infection clocks, the same placements instead obey, for every \(t\ge0\),
\[
\Pr(T_H\le t)-\Pr(T_L\le t)=\frac{(r-k)(e^{-\beta t}-e^{-k\beta t})}{n(k-1)},
\qquad
\mathbb E[T_L]-\mathbb E[T_H]=\frac{r-k}{nk\beta}.
\]
Consequently, continuous-time placement cannot undergo a transmission-rate-driven reversal: only the integer comparison \(r\lessgtr k\) matters. The discrete switch in the range \(1<r<k\) is a genuinely finite-step effect.

## Assumptions and scope
The graph is a simple undirected star on \(n\) labeled vertices, one hub and \(n-1\) leaves. A single index case is selected uniformly from those vertices at time zero. Infection is permanent (SI, with no recovery). In the discrete model, an infected vertex independently attempts infection of each susceptible neighbor at each integer step; with probability \(p\) an attempt succeeds, and new infections begin transmitting only at the following integer step. There are no exogenous infections. A fixed set of exactly \(k\) monitored vertices detects without delay or test error, including at time zero. The continuous model replaces each infection wait across an edge after the source becomes infectious by an independent exponential clock of rate \(\beta\), with the same initial-index and monitor conventions. All random infection trials/clocks are independent where specified.

Strict stochastic dominance refers to all **finite positive** deadlines; both types detect with probability \(k/n\) at time zero and converge to detection probability one as time tends to infinity. The formulas concern *detection* rather than final outbreak size or intervention effectiveness.

## Proof
**Exact discrete detection laws.** Let \(q=1-p\), \(r=n-k\), and \(\gamma=q^k\). A single hub-to-leaf or leaf-to-hub wait is geometric on \(\{1,2,\dots\}\) with success probability \(1-q\). Starting at an infected hub, the wait until any of \(k\) monitored leaves is geometric with success probability \(1-q^k=1-\gamma\), because the \(k\) independent leaves are tested in parallel at every step. A source in an unmonitored leaf in arrangement \(L\) requires an independent leaf-to-hub wait followed by an independent hub-to-monitored-leaf minimum wait. The sum \(X+Y\) of these two geometric waits has
\[
C_t=\Pr(X+Y\le t)
=1-\frac{(1-\gamma)q^t-(1-q)\gamma^t}{q-\gamma},\qquad t\ge0.
\]
The identity follows by conditioning on the first success time of \(X\) and summing the finite geometric series, or by multiplying the two geometric probability-generating functions. It is well-defined since \(k\ge2\) and \(0<q<1\) imply \(0<\gamma<q\). Note \(C_0=C_1=0\), as the two steps cannot happen simultaneously.

In hub-monitoring arrangement \(H\), \(k\) possible index cases are already monitored and each of \(r\) other (leaf) index cases reaches the monitored hub by time \(t\) with probability \(1-q^t\). Thus
\[
nF_H(t)=k+r(1-q^t).
\]
In leaves-only arrangement \(L\), \(k\) index cases are already monitored, one unmonitored hub index case has detected by time \(t\) with probability \(1-q^{kt}\), and each of \(r-1\) unmonitored leaf index cases has detected by time \(t\) with probability \(C_t\). Therefore
\[
nF_L(t)=k+(1-q^{kt})+(r-1)C_t.
\]
Subtracting these expressions and simplifying with \(S_k(q)=(1-q^k)/(1-q)\) proves the displayed factorization.

**Universal ordering and switch.** For every integer \(t\ge1\), \((1-q)(q^t-q^{kt})/[n(q-q^k)]>0\), so all deadlines have exactly the sign of \(r-S_k(q)\). The finite-state process reaches every vertex eventually with probability one, so both detection times are a.s. finite and have exponentially bounded tails. Summing \(F_H(t)-F_L(t)\) over \(t\ge0\) and using \(\mathbb E[T]=\sum_{t\ge0}(1-F(t))\) gives
\[
\mathbb E[T_L]-\mathbb E[T_H]=
\frac{r-S_k(q)}{n(1-q^k)}.
\]
First-order stochastic dominance also minimizes the expectation of any nondecreasing cost function when its expectation exists, by stochastic coupling or tail summation. Since \(S_k(q)\) is strictly increasing on \((0,1)\), with endpoint limits \(1\) and \(k\), the three claimed cases and uniqueness of the interior switch follow. For \(n=5,k=3\), \(1+q+q^2=2\) yields \(q_*=(\sqrt5-1)/2\), and the two rational examples follow by substitution into the exact delay difference. No smaller admissible star can have \(1<r<k\): since \(k\ge3\) and \(r\ge2\), one must have \(n=k+r\ge5\).

**Continuous-time contrast.** If the unmonitored leaf is the index case, the two independent stages are exponential with rates \(\beta\) and \(k\beta\), respectively. Their convolution CDF is
\[
C_t^{\mathrm{ct}}=1-\frac{k e^{-\beta t}-e^{-k\beta t}}{k-1}.
\]
The other cases give \(nF_H^{\mathrm{ct}}(t)=k+r(1-e^{-\beta t})\) and \(nF_L^{\mathrm{ct}}(t)=k+(1-e^{-k\beta t})+(r-1)C_t^{\mathrm{ct}}\). Subtracting proves the continuous-time CDF formula, and integrating its positive/negative tail difference over \(t\ge0\) proves the mean difference. No coefficient changes sign with \(\beta\). If the discrete-step duration is \(\delta\) and \(p=1-e^{-\beta\delta}\), the corresponding geometric waits times \(\delta\) converge to these exponential waits, recovering the continuous classification as \(\delta\downarrow0\).

## Verification
The independent, dependency-free Python program `check_star_sentinels.py` constructs exact-rational SI state-transition distributions directly on labeled stars, without using the closed two-placement formulas for its transition probabilities. Run `python check_star_sentinels.py`; its recorded completion is `PASS: 5797 exact checks; all monitored-subset symmetry classes verified.` It checks every size \(4\le n\le7\), every admissible \(k\), every sensor subset, three rational transmission probabilities, and deadlines \(0\le t\le6\). It also checks the exact five-vertex switching witnesses and compares truncated rational tail sums with the exact expected-delay expression. These computations support, but do not replace, the preceding all-\(n\), all-\(p\) proof. They are finite checks, not exhaustive tests of all parameter values.

## Relationship to prior work
Batlle, Bruna, Fernandez-Granda and Preciado formulate stochastic network outbreak monitoring, detection deadlines and test-set optimization, proving general structural properties of coverage objectives and giving examples, but not the arbitrary-order star law or the universal horizon-independent placement switch derived here. Holme's analyses study network epidemiological node importance and sentinel effectiveness, mainly via comparative objectives and finite networks. Heavey and collaborators establish general epidemic-sensor selection frameworks rather than the present sharp complete star classification. The elementary geometric and exponential waiting-time convolutions are classical; the claimed new result is the complete, source-averaged all-deadline dominance identity, budget-dependent sharp switch, and its continuous-time non-reversal within this precisely stated monitoring problem. No claim is made that submodularity, geometric convolutions, or stochastic dominance themselves are new.

## Limitations
Uniform index-case distribution, perfect fixed sensing, a star, homogeneous independent transmissions and permanent infection are essential to the proved classification. Nonuniform seeding, recovery, false-negative testing, heterogeneous edges, dynamic monitoring or more general graphs may change the ordering. The result is a fully analytical toy-network benchmark, not an empirical surveillance-policy recommendation or a general epidemic optimality theorem. General pre-existing stochastic network monitoring theory could imply this specialization even if the inspected sources do not state it explicitly; publication-priority certainty is not asserted.

## References
1. P. Batlle, J. Bruna, C. Fernandez-Granda and V. M. Preciado, *Adaptive Test Allocation for Outbreak Detection and Tracking in Social Contact Networks*, arXiv:2011.01998 (first public 2020-11-03), https://arxiv.org/abs/2011.01998; journal DOI:10.1137/20M1377874.
2. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, Physical Review E 96, 062305 (2017), DOI:10.1103/PhysRevE.96.062305.
3. P. Holme, *Objective measures for sentinel surveillance in network epidemiology*, Physical Review E 98, 022313 (2018), DOI:10.1103/PhysRevE.98.022313.
4. Heavey et al., *Provable Sensor Sets for Epidemic Detection over Networks with Minimum Delay*, AAAI (2022), DOI:10.1609/aaai.v36i9.21260.
