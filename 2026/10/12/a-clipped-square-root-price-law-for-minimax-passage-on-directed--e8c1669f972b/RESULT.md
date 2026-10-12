# A clipped square-root price law for minimax passage on directed rings

## Finding

For any integer \(n\ge3\), let a directed ring have one permitted transition \(i\to i+1\pmod n\) from each vertex, at positive continuous-time exponential rate \(r_i\). The cost of unit rate on this arc is \(c_i>0\), and the normalized resource constraint is
\[
\sum_{i=1}^n c_i r_i=1.
\]
For distinct vertices \(a,b\), write \(H_{ab}\) for the mean first-passage time from \(a\) to \(b\); same-state first returns are **not** part of the objective. Minimize \(\mathcal T(r)=\max_{a\ne b}H_{ab}\).

There is a unique scalar \(\theta>0\) such that
\[
\sum_{i=1}^n\left(1-\frac{c_i}{\theta}\right)_+=1,
\qquad (u)_+:=\max\{u,0\}.
\]
Set
\[
Z=\sum_{i=1}^n\frac{c_i}{\sqrt{\max\{c_i,\theta\}}}.
\]
Then the **unique** global optimum and its exact minimax passage time are
\[
\boxed{r_i^*=\frac{1}{Z\sqrt{\max\{c_i,\theta\}}}},\qquad
\boxed{\min_{r>0,\ \sum c_i r_i=1}\mathcal T(r)=Z^2}.
\]
In particular, all optimal jump rates are strictly positive. At least two prices satisfy \(c_i<\theta\). Every such cheap edge receives the same rate; for \(c_i\ge\theta\), its rate is proportional to \(1/\sqrt{c_i}\). This is a clipped square-root price allocation.

Uniform rates are optimal if and only if
\[
(n-1)\max_i c_i\le\sum_i c_i.
\]
For \(n=3\), this becomes the triangle inequality on the three positive prices. For example, \((c_1,c_2,c_3)=(1,3,100)\) gives \(\theta=4\), \(Z=12\), and
\[
(r_1^*,r_2^*,r_3^*)=(1/24,1/24,1/120),\qquad \mathcal T(r^*)=144.
\]
The equal-rate design instead has minimax time \(208\). The optimal construction follows from sorting the prices in \(O(n\log n)\) arithmetic operations.

## Assumptions and scope

Rates are strictly positive and independent, with no imposed stationary distribution and no maximum-rate caps. Each holding time is exponential with mean \(1/r_i\); only the clockwise arc is permitted. Costs \(c_i\) are arbitrary positive real numbers. Time and rates are physical continuous-time quantities. The objective uses **all ordered pairs of distinct vertices**, not stationary-weighted average passage time, return time, cover time, or spectral gap. Numerical tests are supplementary; the proof covers every \(n\ge3\) and every positive price vector.

## Proof

**1. Reduce all directed hitting times to a single worst omitted edge.** Starting from vertex \(a\) and stopping at the first visit to \(b\ne a\), the chain traverses the unique forward path from \(a\) to \(b\). By the exponential holding-time expectation (or the first-step Poisson equations), its mean is the sum of \(1/r_i\) along that path. Every path uses at most \(n-1\) arcs; for every \(j\), the path from \(j+1\) to \(j\) uses exactly all arcs except \(j\). Positivity therefore gives
\[
\mathcal T(r)=\max_j\sum_{i\ne j}\frac1{r_i}
=\sum_i\frac1{r_i}-\min_j\frac1{r_j}.
\tag{1}
\]

**2. Construct a global lower bound without any minimax interchange assumption.** For any probability vector \(q=(q_i)\) on the \(n\) arcs, averaging the \(n\) quantities in the first expression of (1) yields
\[
\mathcal T(r)\ge\sum_i\frac{1-q_i}{r_i}.
\]
The Cauchy--Schwarz inequality and the unit cost constraint then imply
\[
\mathcal T(r)\ge
\left(\sum_i\sqrt{c_i(1-q_i)}\right)^2.
\tag{2}
\]
Define \(S(q)=\sum_i\sqrt{c_i(1-q_i)}\). This strictly concave continuous function has a unique maximizer on the compact probability simplex. That maximizer has every \(q_i<1\): if \(q_j=1\), transferring a small amount from \(j\) to any other coordinate increases the \(j\)-term by order \(\sqrt\varepsilon\) while decreasing the other term only by order \(\varepsilon\).

**3. Solve the concave dual maximization.** Its Karush--Kuhn--Tucker conditions have a positive common threshold \(\theta\) and give
\[
q_i^*=\left(1-\frac{c_i}{\theta}\right)_+.
\tag{3}
\]
Indeed, on positive coordinates the derivative \(-\sqrt{c_i}/(2\sqrt{1-q_i})\) is a common value \(-\sqrt{\theta}/2\); on a zero coordinate, the derivative is no larger precisely when \(c_i\ge\theta\). The simplex condition is exactly the threshold equation in the finding. The function \(\sum_i(1-c_i/\theta)_+\) is continuous, increases strictly whenever positive, starts at zero and approaches \(n\), so its level one has exactly one solution. One active summand is strictly smaller than one, so there are at least two indices with \(c_i<\theta\).

**4. Match the bound by a positive rate vector.** From (3),
\[
1-q_i^*=\frac{c_i}{\max\{c_i,\theta\}},
\qquad
S(q^*)=\sum_i\frac{c_i}{\sqrt{\max\{c_i,\theta\}}}=Z.
\]
Equality in Cauchy--Schwarz in (2) forces
\[
r_i\ \propto\ \sqrt{(1-q_i^*)/c_i}
=1/\sqrt{\max\{c_i,\theta\}}.
\]
Budget normalization determines precisely \(r_i^*\) in the finding. These rates are positive. Let \(A=\{i:c_i<\theta\}\), with \(k=|A|\ge2\). The threshold equation implies
\[
\sum_{i\in A}c_i=(k-1)\theta,
\qquad
Z=(k-1)\sqrt{\theta}+\sum_{i\notin A}\sqrt{c_i}.
\tag{4}
\]
As \(1/r_i^*=Z\sqrt{\max\{c_i,\theta\}}\), its minimum is \(Z\sqrt\theta\). Equations (1) and (4) show
\[
\mathcal T(r^*)=
Z\left(k\sqrt\theta+\sum_{i\notin A}\sqrt{c_i}-\sqrt\theta\right)=Z^2.
\]
This equals the lower bound (2) at \(q^*\), proving global optimality. Any other optimizer must attain equality in (2) at the **same** unique maximizing \(q^*\); strict Cauchy--Schwarz equality and the budget force it to be \(r^*\). Hence the optimizer is unique, including at every price threshold.

**5. Identify the all-equal-rate regime and compute the threshold.** All optimal rates coincide exactly when every \(c_i\le\theta\), because at least one \(c_i<\theta\). Under this condition the threshold equation gives \(\theta=(\sum_i c_i)/(n-1)\). Thus equal rates are optimal if and only if \((n-1)\max_i c_i\le\sum_i c_i\). To compute \(\theta\), sort \(c_{(1)}\le\cdots\le c_{(n)}\). The active count \(k\ge2\) is characterized by
\[
\theta=\frac{\sum_{i=1}^k c_{(i)}}{k-1},\qquad
c_{(k)}<\theta\le c_{(k+1)}
\]
(with no upper inequality for \(k=n\)). A linear scan after sorting finds the unique compatible \(k\); equalities at the breakpoint are handled by the strict active-set definition.

## Verification

The companion standard-library checker at `checks/verify.py` verifies 385 exact rational threshold/KKT systems, 100 independent exact rational absorbing-generator hitting-time systems, and 1,815 feasible normalized random price comparisons. The exact example \((1,3,100)\) is also checked. Execute with `python3 checks/verify.py` after extracting the files. These are finite reproducibility checks only; statements for arbitrary \(n\) and arbitrary positive real costs follow from the five proof steps.

## Relationship to prior work

Yu, Karaman, and Rus study optimal cyclic dwell scheduling for event surveillance, balancing event capture and observation gaps under Poisson arrivals, not rate-priced minimization of worst first-hitting time in a continuous-time chain [1]. Agharkar, Patel, and Bullo optimize stationary-weighted mean first-passage objectives on transition matrices [2]. Carron, Patel, and Bullo derive pairwise hitting-time formulas for doubly weighted stochastic graphs but optimize a stationary-weighted aggregate [3]. Breen and Kirkland study the maximum first-passage time of discrete-time chains and characterize graphs on which a stationary-distribution bound is attained [4]. Its directed-cycle comparisons do not supply a price constraint or the present positive-rate optimum. None of these inspected texts gives the clipped-threshold allocation or its uniqueness for arbitrary continuous-time prices. An earlier specialized formula in unexamined literature cannot be ruled out.

## Limitations

The result is **not** a spectral-gap or stationary-distribution optimization theorem. It assumes only clockwise transitions with exponential state holding times and linear positive prices; adding counterclockwise arcs, fixing a stationary distribution, imposing rate caps, or optimizing cover/return times changes the mathematical problem. The first public date below belongs to the motivating primary source [1], not to the present mathematical statement. Novelty relative to all historical literature is not independently established.

## References

[1] J. Yu, S. Karaman, D. Rus, “Persistent Monitoring of Events with Stochastic Arrivals at Multiple Stations,” arXiv:1309.6041, first submitted 2013-09-24 UTC; https://arxiv.org/abs/1309.6041 .

[2] P. Agharkar, N. K. Patel, F. Bullo, “Robotic Surveillance and Markov Chains with Minimal First-Passage Time,” 2014 conference version; https://motion.me.ucsb.edu/pdf/2014b-apb-conference.pdf .

[3] A. Carron, N. K. Patel, F. Bullo, “Hitting Time for Doubly-Weighted Graphs with Application to Robotic Surveillance,” 2016 conference version; https://motion.me.ucsb.edu/pdf/2014k-pcb-conference.pdf .

[4] J. Breen, S. Kirkland, “Minimising the Largest Mean First Passage Time of a Markov Chain: The Influence of Directed Graphs,” Linear Algebra and its Applications (2017), author-hosted text; https://server.math.umanitoba.ca/~kirkland/LAA_mfp_lowerbound2.pdf .
