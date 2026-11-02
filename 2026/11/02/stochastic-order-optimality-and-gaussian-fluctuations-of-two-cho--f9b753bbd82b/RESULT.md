# Stochastic-order optimality and Gaussian fluctuations of two-choice cycle coverage

## Finding

Let \(n\ge3\) and let \(C_n\) be the undirected \(n\)-cycle. A walker starts at an arbitrary vertex (counted as visited). At every discrete step it is offered two independent uniformly sampled neighboring vertices, **with replacement**, and a controller chooses one; controllers may be history-dependent and randomized, but cannot see future offers. Let \(T_n^\pi\) be the first time all \(n\) vertices have been visited under controller \(\pi\).

Define policy \(\pi_*\) by moving, whenever the two offers differ, toward whichever endpoint of the *currently visited contiguous arc* is nearer, breaking ties arbitrarily. When both offers agree it must accept the offered neighbor. A move from the visited arc to an unvisited vertex extends the arc by one vertex.

**Theorem (one claim, with quantitative consequences).** For all \(n\ge3\), every admissible policy \(\pi\), and every integer \(t\ge0\),
\[
\Pr(T_n^{\pi_*}>t)\le\Pr(T_n^\pi>t).
\]
Thus the same fixed policy minimizes *every* cover-time tail and every increasing loss, not merely expected cover time. Under \(\pi_*\), the cover time is a sum of independent, non-identically distributed exit times, has the exact finite-size variance given below, and satisfies
\[
\operatorname{Var}(T_n^{\pi_*})=6n-\frac{129}{4}+O\!\left(n3^{-n/2}\right),\qquad
\frac{T_n^{\pi_*}-\mathbb ET_n^{\pi_*}}{\sqrt{6n}}\Longrightarrow N(0,1).
\]
The previously known exact mean is included for normalization but is **not claimed as new**:
\[
\mathbb ET_n^{\pi_*}=2n-\frac92+\frac{3}{2\cdot3^{\lceil(n-1)/2\rceil}}+\frac{1}{3^{\lfloor(n-1)/2\rfloor}}.
\]

More explicitly, let \(X_L\) denote the time to expand a visited arc containing \(L\) vertices, starting at either endpoint and following \(\pi_*\), for \(1\le L\le n-1\). The variables \(X_1,\ldots,X_{n-1}\) can be chosen independent with
\[
T_n^{\pi_*}\stackrel d=\sum_{L=1}^{n-1}X_L.
\]
For every integer \(m\ge1\), their exact moments are
\[
\begin{aligned}
\mathbb EX_{2m-1}&=2-3^{1-m},&
\operatorname{Var}(X_{2m-1})&=6-\frac{8m-4}{3^{m-1}}-\frac{2}{9^{m-1}},\\
\mathbb EX_{2m}&=2-\frac{2}{3^m},&
\operatorname{Var}(X_{2m})&=6-\frac{16m-2}{3^m}-\frac8{9^m}.
\end{aligned}
\]
These formulas include the degenerate first exit \(X_1=1\).

## Assumptions and scope

Only independent neighbor offers, a simple undirected cycle, and discrete steps are assumed. The initial vertex is observed at time zero. Optimality is among *all* nonanticipative, possibly randomized or nonstationary policies. Stochastic order \(A\preceq_{\mathrm{st}} B\) means \(\Pr(A>t)\le\Pr(B>t)\) for every \(t\). The central limit theorem concerns the cover time **under the stated optimal policy**, not arbitrary policies. Cycles have at least three vertices, avoiding a degree-one two-vertex convention.

## Proof

**1. Arc decomposition.** Before cover, the visited vertices on a nearest-neighbor cycle form a single contiguous arc. The first visit to a new vertex always occurs by exiting one of its two ends, and leaves the walker at an endpoint of a new arc. Translation and reflection make the exit-time law at a given arc size independent of its position and of which endpoint the walker occupies. All future offers are independent of the past.

**2. Fixed-horizon exit optimality, stronger than an expectation Bellman equation.** For an arc with \(L\) visited sites, label sites \(1,\ldots,L\) and the two absorbing exterior sites \(0,L+1\). Let \(u_t(j)\) be the infimum over all admissible controllers of \(\Pr_j(\tau>t)\), where \(\tau\) is the first exterior hit. The finite-horizon dynamic recursion is
\[
u_0(j)=1\quad(1\le j\le L),\qquad u_t(0)=u_t(L+1)=0,
\]
\[
 u_{t+1}(j)=\tfrac34\min\{u_t(j-1),u_t(j+1)\}+\tfrac14\max\{u_t(j-1),u_t(j+1)\}.
\]
The probabilities \(3/4\) and \(1/4\) follow by enumerating the four ordered pairs of independent neighbor offers. Symmetry \(u_t(j)=u_t(L+1-j)\) is preserved.

Put \(m=\lceil L/2\rceil\) and \(d_j=u_t(j)-u_t(j-1)\) for \(1\le j\le m\). The cone
\[
 d_j\ge0,\qquad d_{j+1}\le3d_j\quad (1\le j<m)
\]
is invariant under the nonlinear recursion. Here is the full boundary check. For \(m\ge2\), the next differences satisfy
\[
 d'_1=\tfrac14(d_1+d_2),\qquad
 d'_j=\tfrac34d_{j-1}+\tfrac14d_{j+1}\ (2\le j<m).
\]
At the last index, if \(L=2m-1\), then \(d'_m=\tfrac34d_{m-1}-\tfrac14d_m\); if \(L=2m\), then \(d'_m=\tfrac34d_{m-1}\). In the odd case nonnegativity follows from \(d_m\le3d_{m-1}\). At the left boundary \(3d'_1-d'_2=\tfrac14(3d_2-d_3)\ge0\) when \(m\ge3\); every interior comparison is a nonnegative combination of \(3d_{j-1}-d_j\) and \(3d_{j+1}-d_{j+2}\). At the right boundary \(3d'_{m-1}-d'_m\) is \(\tfrac34(3d_{m-2}-d_{m-1})+d_m\) in the odd case and \(\tfrac34(3d_{m-2}-d_{m-1})+\tfrac34d_m\) in the even case, when \(m\ge3\). At \(m=2\), direct subtraction gives respectively \(d_2\) and \(\tfrac34d_2\); at \(m=1\) the assertion is immediate. Initially \((d_1,d_2,\ldots)=(1,0,\ldots)\), so induction proves the cone for every horizon.

Therefore \(u_t(j)\) is nondecreasing from either exterior boundary toward the middle for **every** \(t\). The fixed nearer-boundary choice attains the minimum in the recursion at *every horizon*; consequently its exit time is stochastically no larger than the exit time under any other policy, from any initial arc position. This argument establishes more than a finite-horizon optimal expected exit time.

**3. From exits to the entire cover time.** Under the nearer-boundary policy, successive expansion durations \(X_L\) are independent by the strong Markov property of fresh offers and the arc symmetries. For a competing history-dependent policy, conditional on the history at the start of stage \(L\), that stage's duration stochastically dominates the fixed distribution of \(X_L\). A sequential conditional-quantile coupling makes each competing duration at least an independent draw from the corresponding \(X_L\) law. Summation preserves the pathwise inequality under this coupling, proving the theorem's all-tail stochastic order.

**4. Exact moments.** Fold the arc around its midpoint. In distance-to-nearest-exterior states \(j=1,\ldots,m\), the optimal chain moves down with probability \(3/4\) and up with probability \(1/4\) for \(j<m\); reaching state zero ends the stage. For odd \(L=2m-1\), the middle state \(m\) moves deterministically to \(m-1\); for even \(L=2m\), it moves down with probability \(3/4\) and remains at \(m\) with probability \(1/4\).

Writing \(e_j=\mathbb E_j X_L\), the interior recurrence is \(e_j=1+\tfrac34e_{j-1}+\tfrac14e_{j+1}\), with \(e_0=0\). At the middle, \(e_m-e_{m-1}=c\), with \(c=1\) for odd \(L\) and \(c=4/3\) for even \(L\). The unique solution is
\[
 e_j=2j+(c-2)\frac{3^{j+1}-3}{2\cdot3^m}\quad (1\le j\le m).
\]
The second moments \(s_j=\mathbb E_jX_L^2\) satisfy \(s_j=2e_j-1+\tfrac34s_{j-1}+\tfrac14s_{j+1}\) in the interior, \(s_0=0\), and \(s_m-s_{m-1}=c(2e_m-1)\) at the middle. Their first difference recurrence yields the explicit boundary value
\[
 s_1=\frac{c(2e_m-1)}{3^{m-1}}+\sum_{k=1}^{m-1}\frac{4(2e_k-1)}{3^k}.
\]
Evaluating this finite geometric-arithmetic sum and subtracting \(e_1^2\) gives precisely the four displayed stage-moment formulas. The sum of the **variance deficits** \(6-\operatorname{Var}(X_L)\) over all \(L\ge1\) is
\[
\sum_{m\ge1}\left(\frac{8m-4}{3^{m-1}}+\frac2{9^{m-1}}\right)
+\sum_{m\ge1}\left(\frac{16m-2}{3^m}+\frac8{9^m}\right)=\frac{105}{4}.
\]
The remaining tail is \(O(n3^{-n/2})\), which gives \(\operatorname{Var}(T_n^{\pi_*})=6(n-1)-105/4+O(n3^{-n/2})\), equivalently the stated \(6n-129/4\) expansion.

**5. Gaussian fluctuations.** Compare the folded stage chain with a biased nearest-neighbor walk \(B\) on nonnegative integers, started at 1, absorbed at 0, taking a downward step with probability \(3/4\) and upward with probability \(1/4\). With the same independent Bernoulli offers, the folded chain remains at most \(B\) and thus \(X_L\le\tau\) pathwise, where \(\tau\) is \(B\)'s absorption time. Prior to visiting the folded midpoint, both chains coincide. The probability that \(B\), started at 1, reaches \(m\) before zero is \(2/(3^m-1)\) for \(m\ge2\). Consequently \(X_L\to\tau\) in distribution with exponentially small discrepancy. The hitting-time probability-generating function is
\[
\mathbb E[z^\tau]=\frac2z\left(1-\sqrt{1-\tfrac34z^2}\right),\qquad 0<z<2/\sqrt3.
\]
It has an exponential moment and gives \(\mathbb E\tau=2\), \(\operatorname{Var}(\tau)=6\). Since the independent stage durations are uniformly dominated by \(\tau\), their third moments are uniformly bounded. Their total variance is asymptotic to \(6n\). Lyapunov's triangular-array central limit theorem proves the displayed Gaussian limit.

## Verification

Execute `python check.py` with Python 3 and only its standard library. It independently computes the finite-horizon optimal Bellman recursion using exact rational arithmetic, checks every horizon's unimodality cone and matching fixed-policy action, independently replays the full-cycle finite-horizon Markov decision process, and solves the finite Markov-chain first and second moment equations, and checks the symbolic closed-form moments for arc sizes through 82. A successful replay reports `PASSED 39497 exact assertions`. These finite checks test the formulas and implementation; the unbounded all-policy assertion and limit theorem depend on the proofs above, not on the finite tests.

## Relationship to prior work

Georgakopoulos, Haslegrave, Sauerwald and Sylvester introduced the choice random walk and established linear-order cover-time bounds for fixed-dimensional tori, including cycles, and general finite-state methods. Those bounds and methods do not themselves provide an all-horizons cycle strategy, its stochastic dominance over arbitrary history-dependent policies, or the sharp Gaussian variance constant here. An earlier exact computation of the **expected** optimal cycle cover time is treated as known and is not an originality claim; an expectation minimum does not logically imply stochastic-order minimality or the variance/CLT. The theorem addresses that stronger distributional question.

## Limitations

The stochastic-order result requires degree two, independent with-replacement neighbor offers and sequential coverage of a simple cycle; it is not asserted for higher-degree graphs or correlated offers. The Gaussian theorem concerns the specified policy. No claim of independent mathematical verification or of absolute historical priority is made.

## References

1. A. Georgakopoulos, J. Haslegrave, T. Sauerwald, J. Sylvester, *The Power of Two Choices for Random Walks*, first publicly posted 2019-11-12, arXiv:1911.05170; *Combinatorics, Probability and Computing* **31** (2022), 73–100, DOI:10.1017/S0963548321000183. Full text: https://eprints.gla.ac.uk/250806/1/250806.pdf.
2. A. Georgakopoulos, J. Haslegrave, T. Sauerwald, J. Sylvester, *Choice and Bias in Random Walks*, ITCS 2020, DOI:10.4230/LIPIcs.ITCS.2020.76.
