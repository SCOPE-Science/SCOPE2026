# Optimal path coverage with offered neighbours: exact cost and Gaussian fluctuations

## Finding
Consider a nearest-neighbour walk on the path with vertices \(\{0,1,\ldots,n\}\), where \(n\ge1\). At each step a controller sees \(c\ge1\) independent uniformly drawn neighbours (draws with replacement) and chooses one. The controller may use arbitrary past observations, previous offers, and internal randomness. Let \(T\) be the first time all vertices have been visited, and let \(V_{n,i}^{(c)}\) be the infimum of \(\mathbb E_i T\) over all such policies, starting at vertex \(i\). The infimum is attained by first choosing an offered step toward the nearest endpoint whenever possible, and, after an endpoint has been visited, choosing an offered step toward the opposite endpoint whenever possible.

For \(c=1\),
\[
V_{n,i}^{(1)}=n^2+i(n-i),\qquad \max_i V_{n,i}^{(1)}=n^2+\lfloor n^2/4\rfloor.
\]
For each fixed integer \(c\ge2\), put
\[
q=2^{-c},\quad p=1-q,\quad \delta=p-q,\quad \tau=q/p,\quad K=2pq/\delta^2,\quad m=\lfloor n/2\rfloor,\quad d=\min\{i,n-i\}.
\]
Then the exact optimal cover time is
\[
V_{n,i}^{(c)}=C_n+E_{n,d},\qquad C_n=\frac n\delta-K(1-\tau^n),
\]
with
\[
E_{n,d}=\begin{cases}
\displaystyle\frac d\delta-K\tau^{m-d}(1-\tau^d),&n=2m,\\[5pt]
\displaystyle\frac d\delta-\frac q{\delta^2}\tau^{m-d}(1-\tau^d),&n=2m+1.
\end{cases}
\]
The maximum is attained exactly at the central vertex (even \(n\)) or the two central vertices (odd \(n\)); in particular,
\[
\max_i V_{n,i}^{(c)}=\frac{3n}{2\delta}+O_c(1).
\]
For two offers, the finite-horizon values sharpen to
\[
\max_i V_{2m,i}^{(2)}=3(2m)-3+\frac32\left(3^{-2m}+3^{-m}\right)
\]
for \(m\ge1\), and
\[
\max_i V_{2m+1,i}^{(2)}=3(2m+1)-\frac72+3^{-m}+\frac32\,3^{-(2m+1)}
\]
for \(m\ge0\). Thus the optimal worst-start expectation drops from order \(n^2\) with one offer to \(3n+O(1)\) with two.

The same optimal feedback policy has a central limit theorem. For any fixed \(c\ge2\) and any starting positions \(i_n\) with \(i_n/n\to u\in[0,1]\), let \(\eta=\min\{u,1-u\}\). Then under this policy,
\[
\frac{T_{n,i_n}-V_{n,i_n}^{(c)}}{\sqrt n}
\;\Longrightarrow\;
N\!\left(0,\frac{4pq(1+\eta)}{\delta^3}\right).
\]
In particular, at the worst starting position with two offers, \((T_{n,i_n}-3n)/\sqrt n\Longrightarrow N(0,9)\).

## Assumptions and scope
All offers are independent from step to step and across simultaneous alternatives, and each offer samples a neighbour uniformly with replacement. A degree-one endpoint has a deterministic next move. A policy may condition on the entire observed history, so the optimality assertion is not restricted to memoryless policies. At the midpoint a tie may be resolved arbitrarily; both choices produce the same distance process. The limit distribution concerns the specified minimizing policy, not every policy having a similar expectation. The number of offers \(c\) is fixed for the limit theorem. Cover time is measured in steps after the starting vertex is already observed.

## Proof
**1. The cover problem separates into two hitting problems.** A nearest-neighbour path has been completely visited exactly when both its endpoints have been hit. Until the first endpoint is hit, the controller can minimize its first-hit time; after that, the remaining problem is to reach the opposite endpoint. By path reflection, the minimum expected crossing time is the same from either endpoint. Conditional on first hitting either endpoint, any policy has at least that crossing expectation for its remaining duration. Conversely, concatenate optimizers for these two hitting problems. The strong Markov property of future offers makes the expectations additive, proving \(V_{n,i}^{(c)}=C_n+E_{n,d}\), once the displayed first-stage and crossing policies are shown optimal.

**2. One-dimensional Bellman inequalities certify global optimality.** If the target is the right endpoint, the value \(H_x\) strictly decreases with the current vertex \(x\). Choosing the greatest offered neighbour minimizes the next value; the Bellman equations are
\[
H_n=0,\quad H_0=1+H_1,\quad H_x=1+pH_{x+1}+qH_{x-1}\ (1\le x<n).
\]
For \(c\ge2\), their unique solution is
\[
H_x=\frac{n-x}{\delta}-\frac{2pq}{\delta^2}(\tau^x-\tau^n).
\]
Indeed \(H_x-H_{x+1}=\delta^{-1}-K\tau^x(1-\tau)>0\), because its smallest value occurs at \(x=0\) and equals \(1>0\). Thus the policy that chooses the offered vertex with least \(H\) satisfies the full Bellman equation, not merely the greedy-restricted equation. In particular \(C_n=H_0\). For \(c=1\), the unbiased difference equations give \(H_x=n^2-x^2\).

Until the first endpoint, the distance to the nearer endpoint is \(d=\min\{x,n-x\}\). Its value \(E_d\) is strictly increasing in \(d\), as is verified directly below. For \(1\le d<m\),
\[
E_d=1+pE_{d-1}+qE_{d+1},\qquad E_0=0.
\]
At \(d=m\) for \(n=2m\), both neighbours move to distance \(m-1\), hence \(E_m=1+E_{m-1}\). For \(n=2m+1\), the neighbours lead to distances \(m-1\) and \(m\), and \(E_m=1+pE_{m-1}+qE_m\). Solving the two boundary-value problems gives exactly the two formulas above. Their differences are strictly positive: in the even case,
\[
E_d-E_{d-1}=\frac1\delta-K\tau^{m-d}(1-\tau)>0,
\]
while in the odd case the same calculation replaces \(K\) by \(q/\delta^2\). In the even case the smallest difference is the central one \(1\), and in the odd case it is \(1/p\). Consequently the displayed policy minimizes the Bellman expectation among all selections of the actual offered neighbours. For \(c=1\), the unbiased gambler's-ruin equation gives \(E_d=d(n-d)\). All these policies hit their stopping sets almost surely with finite expectation; for example, every block of \(n\) steps has a uniform positive chance of a fully prescribed directed traversal, independent of the chosen policy. Standard finite-state Bellman optional stopping therefore proves optimality even against randomized, history-dependent policies.

**3. Exact worst-start value.** Strict monotonicity in \(d\) proves that \(d=m\) alone maximizes the first-exit expectation. Inserting \(m\) gives the displayed maximum, parity formulas, and asymptotic expansion. For \(c=1\), \(\max_i i(n-i)=\lfloor n^2/4\rfloor\).

**4. Gaussian fluctuations.** Fix \(c\ge2\) and let independent \(\xi_j\in\{-1,+1\}\) have \(\Pr(\xi_j=+1)=p\), \(\Pr(\xi_j=-1)=q\). A policy choosing toward a fixed target corresponds to a positive-drift walk with these increments, except for reflection at the path's opposite endpoint. Each attempted return to the reflecting endpoint after departing it has probability at most \(\tau=q/p<1\), by the positive-drift gambler's-ruin bound. The number of reflecting-endpoint visits is therefore tight as \(n\to\infty\), and its accumulated displacement correction is \(O_{\mathsf P}(1)\), uniformly over starting positions. For the distance-to-nearest-endpoint stage the drift is instead toward smaller distances; at the central reflecting boundary its correction is likewise \(O_{\mathsf P}(1)\), both for even midpoint reflection and for the odd central holding move.

For a drifted walk traversing a distance \(L_n\) with \(L_n/n\to\ell\ge0\), the stopping identity and the negligible reflection correction read
\[
L_n=\delta\,\sigma_n+\sum_{j=1}^{\sigma_n}(\xi_j-\delta)+O_{\mathsf P}(1).
\]
Positive drift and bounded increments imply \(\sigma_n/n\to\ell/\delta\) in probability. The functional central limit theorem (or the random-index form of the i.i.d. central limit theorem) gives
\[
\frac{\sigma_n-\mathbb E\sigma_n}{\sqrt n}\Longrightarrow
N\!\left(0,\frac{4pq\ell}{\delta^3}\right).
\]
Here exact expectation formulas differ from \(L_n/\delta\) by \(O_c(1)\), and a stage with \(\ell=0\) gives a degenerate zero limit. Apply this with \(L_n=d_n\), \(\ell=\eta\), to the first stage and with \(L_n=n\), \(\ell=1\), to the subsequent crossing. Their durations are independent, because fresh offers after the first boundary hit have a conditional law independent of the past and the crossing distribution is the same from both endpoints. Their Gaussian limits consequently add their variances, yielding \(4pq(1+\eta)/\delta^3\). At \(\eta=1/2,c=2\), the variance constant is \(9\), and the mean differs from \(3n\) by \(O(1)\).

## Verification
The accompanying standalone Python script `verify.py` uses exact fractions and independently enumerates all ordered offered-neighbour tuples in the finite Bellman equations. It tests all \(1\le n\le30\) and \(1\le c\le5\), totaling 3600 exact expectation, monotonicity and worst-start checks. Independently calculated finite-state second moments yield central-start variance divided by \(n\) close to the predicted constants for sample lengths 100, 500, and 1000 at three different values of \(c\). These finite tests corroborate, but do not substitute for, the global analytic optimality argument and stopping-time central limit theorem. Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work
Georgakopoulos, Haslegrave, Sauerwald and Sylvester introduced the choice-random-walk model with two independent neighbour offers and full controller memory; their linear bounded-degree-tree cover-time theorem gives the order of growth for paths but does not provide the optimal exact finite-path policy/value or path-cover Gaussian variance. The associated ITCS 2020 version similarly gives broad complexity and cover-time estimates. Known one-dimensional biased gambler's-ruin equations are used openly as ingredients. The contribution here is the complete path-cover control solution for any integer number of offers and the corresponding fluctuation law. This comparison does not claim novelty of the original model, the general linear bound, or biased-walk central limit theory.

## Limitations
The exact formulas are for simple undirected finite paths with uniform independent offered neighbours and equal cost per step. They do not apply unchanged to weighted paths, sampling candidate neighbours without replacement, unknown graph structure, or adversarially dependent offers. The central limit theorem assumes fixed \(c\ge2\), while \(c=1\) has a different time scale. Earlier exact results under alternative controlled-walk or stochastic-shortest-path terminology cannot be completely ruled out; independent historical-priority and formal proof reviews have not been performed.

## References
1. A. Georgakopoulos, J. Haslegrave, T. Sauerwald, J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170, initially public 2019-11-12; *Combinatorics, Probability and Computing* **31** (2022), 73–100, DOI 10.1017/S0963548321000183. Author manuscript: https://wrap.warwick.ac.uk/152060/7/WRAP-Power-two-choices-random-walks-2021.pdf.
2. A. Georgakopoulos, J. Haslegrave, T. Sauerwald, J. Sylvester, *Choice and Bias in Random Walks*, ITCS 2020, Article 76, DOI 10.4230/LIPIcs.ITCS.2020.76.
3. C. Avin and B. Krishnamachari, *The power of choice in random walks: An empirical study*, *Computer Networks* **52** (2008), 44–60, DOI 10.1016/j.comnet.2007.09.012. (Different adaptive visit-frequency heuristic; full text not verified.)
