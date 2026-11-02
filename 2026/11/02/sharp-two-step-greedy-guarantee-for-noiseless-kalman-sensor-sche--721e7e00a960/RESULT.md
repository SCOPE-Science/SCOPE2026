# Sharp two-step greedy guarantee for noiseless Kalman sensor scheduling

## Finding

Consider a diagonal two-state Gaussian system with one exact coordinate observation available at each of two times. Let \(G\) denote the cumulative posterior-trace error under the myopic schedule that minimizes the current posterior trace at each time, and \(O\) the minimum cumulative posterior-trace error among all four two-time schedules. For fixed diagonal dynamics \(A=\operatorname{diag}(a_1,a_2)\), the exact worst-case multiplicative loss is
\[
\sup_{p_1,p_2,q_1,q_2>0}\frac{G}{O}=1+\max\{a_1^2,a_2^2\}.
\]
Here \(p_i\) are the first-time prior variances and \(q_i\) the process-noise variances. Thus stable diagonal dynamics with \(\max_i|a_i|\le1\) admit the sharp universal factor \(2\), whereas unrestricted dynamics admit no finite uniform factor. Both two states and two measurement times are necessary for strict myopic regret in this setting.

More precisely, upon relabeling so that \(p_1\ge p_2\), the exact greedy cost and global optimum are
\[
G=p_2+\min\{q_1,a_2^2p_2+q_2\},\qquad O=\min\{G,p_1+q_2\}.
\]
Greedy is strictly suboptimal exactly when
\[
p_1-p_2<\min\{q_1-q_2,a_2^2p_2\}.
\]
When \(p_1=p_2\), the formulas apply to a greedy tie broken in favor of observing state 1. The universal sharp factor is a supremum, not generally attained for strictly positive input variances.

## Assumptions and scope

At the first observation time, the filtering prior covariance is \(P^-_1=\operatorname{diag}(p_1,p_2)\), with \(p_1,p_2>0\). Between observation times the state follows \(X_2=AX_1+W_1\), with \(A=\operatorname{diag}(a_1,a_2)\), \(a_i\in\mathbb R\), and independent centered process noise with covariance \(Q=\operatorname{diag}(q_1,q_2)\), \(q_i>0\). The initial state and noise are independent. The scheduler selects exactly one of the two states for a noise-free exact observation at each time. Posterior variances of observed states are zero, while those of unobserved states remain unchanged. The objective is \(J=\operatorname{tr}P^+_1+\operatorname{tr}P^+_2\), not the final-time trace alone. Decisions are nonadaptive with respect to measurement values; the covariance is deterministic for any schedule. Myopic means minimizing \(\operatorname{tr}P^+_k\) at each time without lookahead. All conclusions hold for arbitrary real \(a_i\), without a stability assumption unless explicitly stated.

## Proof

**Four exhaustive schedules.** Write \(ij\) for observing state \(i\) at time 1 and state \(j\) at time 2. Independence and exact measurement yield the full table
\[
\begin{array}{c|c}
\text{schedule}&J\\\hline
11&(1+a_2^2)p_2+q_2\\
12&p_2+q_1\\
21&p_1+q_2\\
22&(1+a_1^2)p_1+q_1.
\end{array}
\]
For example, after observing state 1 at time 1 the posterior covariance is \(\operatorname{diag}(0,p_2)\), so the next prior covariance is \(\operatorname{diag}(q_1,a_2^2p_2+q_2)\). Observing state 1 at time 2 leaves the second diagonal entry; observing state 2 instead leaves the first. This verifies both entries beginning with 1. The other two follow symmetrically.

**Exact lookahead criterion.** Assume \(p_1\ge p_2\), so the myopic first observation is state 1. At the second time the myopic scheduler leaves the smaller of the two predicted variances unobserved. Hence \(G=\min(J_{11},J_{12})\). Since \(J_{22}-J_{12}=(1+a_1^2)p_1-p_2\ge0\), the schedule \(22\) cannot improve on \(12\). The only additional global competitor is therefore \(21\), giving \(O=\min(G,p_1+q_2)\). Comparing these expressions gives the exact strict-suboptimality criterion in the finding. Relabeling covers \(p_2>p_1\).

**Universal factor.** If greedy is optimal, \(G/O=1\). Otherwise \(O=p_1+q_2\); therefore
\[
\frac GO\le\frac{(1+a_2^2)p_2+q_2}{p_1+q_2}\le1+a_2^2\le1+\max\{a_1^2,a_2^2\}.
\]
The middle inequality uses \(p_2\le p_1\), \(q_2>0\), and \(a_2^2\ge0\). This proves the bound for every admissible input.

**Sharpness for each fixed dynamics matrix.** Let \(R=\max\{a_1^2,a_2^2\}\). If \(R=0\), the upper bound proves that greedy is always optimal. If \(R>0\), relabel states so that the larger squared growth factor \(R\) belongs to state 2. Fix \(0<\delta<\min\{R,1\}\) and choose \(p_1=1+\delta\), \(p_2=1\), \(q_1=R+2\), and \(q_2=\delta\). Greedy observes state 1 at both times, so \(G=1+R+\delta\). The unique optimal schedule observes state 2 first and state 1 second, giving \(O=1+2\delta\). Consequently \(G/O\to1+R\) as \(\delta\downarrow0\), proving equality for the supremum. Taking \(R=1\) proves sharpness of the factor 2 among nonexpansive diagonal dynamics; taking \(R\to\infty\) proves the absence of a dynamics-independent factor.

**Minimality and noise robustness.** With one state there is no choice of coordinate; with one observation time the myopic choice is globally optimal by definition. Hence two states and two times are minimal for strict regret. For any fixed \(R>0\) and \(0<\delta<\min\{R,1\}\) in the sharpness family, all relevant greedy decisions and the optimum are strict. Replacing the exact observations by independent Gaussian measurements with a common sufficiently small positive variance preserves these inequalities by continuity of the scalar Kalman update \(v\mapsto vr/(v+r)\). This continuity observation does not extend the exact worst-case factor formula to positive measurement noise.

## Verification

The standalone Python 3 standard-library script `verify.py` evaluates all four schedules directly using exact rational arithmetic, checks the reduction to the stated formula and exact suboptimality criterion on 20,000 reproducible rational parameter draws, checks the universal bound, and evaluates sharpness families for distinct growth factors. It separately tests the continuity witness with small positive observation noise. Run `python verify.py` from the extracted package directory. This numerical test does not replace the algebraic proof, and no numerical finite sample is used to justify the supremum.

## Relationship to prior work

The optimization objective and finite-horizon sensor-scheduling setting are motivated by Dutta, Wilde and Smith (arXiv:2304.02692, first posted 5 April 2023), who formulate general trace-optimal schedules as mixed-integer programs and compare their performance with greedy schedules. Their model takes positive measurement-noise covariance, whereas the sharp formula here concerns its noiseless boundary; the strict counterexamples persist for small positive noise. Jawaid and Smith (2015) investigate submodularity and greedy sensor scheduling with terminal-state objectives, rather than this cumulative-trace, two-step worst-case ratio. Ye, Woodford, Roy and Sundaram (2020) prove broad hardness and arbitrarily bad greedy examples for design-time *steady-state sensor selection*, which neither entails nor contradicts the fixed-two-step, growth-dependent bound proved here. Han, Wu, Zhang and Shi (2016) analyze indefinite-horizon scheduling across independent linear dynamical processes, with a different objective and noisy local/remote sensing scheme.

These earlier results establish that unrestricted greedy sensor selection may fail and that combinatorial scheduling is hard. The narrower contribution here is the complete, explicitly sharp two-time guarantee, its exact failure criterion, and its stability-dependent worst-case constant. An equivalent special-case formula in other scheduling literature cannot be excluded without independent priority review.

## Limitations

The exact constant concerns two independent scalar states, two observations, diagonal dynamics, perfectly informative measurements, a sum of posterior traces, and a myopic policy defined by current posterior trace. It does not apply unchanged to correlated states, non-diagonal system matrices, longer horizons, noisy measurements, arbitrary feedback policies, or final-time-only objectives. The positive-noise robustness statement concerns individual strict examples, not a uniform noise-independent approximation ratio. Independent scientific review and publication-priority confirmation have not been performed.

## References

1. S. Dutta, N. Wilde, S. L. Smith, *A Unified Approach to Optimally Solving Sensor Scheduling and Sensor Selection Problems in Kalman Filtering*, arXiv:2304.02692, version 1 posted 2023-04-05. https://arxiv.org/abs/2304.02692
2. S. T. Jawaid, S. L. Smith, *Submodularity and Greedy Algorithms in Sensor Scheduling for Linear Dynamical Systems*, preprint dated 2015-08-09. https://ece.uwaterloo.ca/~sl2smith/papers/2015Aut_Greedy_Submodularity.pdf
3. L. Ye, N. Woodford, S. Roy, S. Sundaram, *On the Complexity and Approximability of Optimal Sensor Selection and Attack for Kalman Filtering*, arXiv:2003.11951, first posted 2020-03-24. https://arxiv.org/abs/2003.11951
4. D. Han, J. Wu, H. Zhang, L. Shi, *Optimal Sensor Scheduling for Multiple Linear Dynamical Systems*, arXiv:1604.04158, first posted 2016-04-14. https://arxiv.org/abs/1604.04158
