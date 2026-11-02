# A sharp choice threshold and contrasting root-hitting laws on regular trees

## Finding

**Theorem.** Fix integers \(b\ge2\) and \(k\ge1\). In the complete rooted \(b\)-ary tree of height \(h\), start a walk from any leaf. At each step the walk is offered \(k\) independent uniform neighbors, sampled **with replacement**, and may choose one of them. The goal is to minimize the expected time \(T_h\) to first hit the root. Put
\[
p=1-\left(\frac b{b+1}\right)^k,\quad q=1-p,\quad r=\frac qp,\quad \delta=p-q.
\]
The optimal policy chooses the parent whenever it appears among the offers; ties among children are immaterial. For every \(h\ge1\), \(\delta\ne0\) and the exact optimal expected time is
\[
\boxed{\mathbb E T_h=\frac{h}{\delta}-\frac{2pq}{\delta^2}(1-r^h).}
\]
The exact minimum number of offered neighbors needed for linear-in-height expected hitting is
\[
\boxed{k_{\mathrm{crit}}(b)=\left\lfloor\frac{\log 2}{\log(1+1/b)}\right\rfloor+1.}
\]
For fixed \(b,k\), as \(h\to\infty\), there are two mutually exclusive laws:

* If \(k\ge k_{\mathrm{crit}}(b)\), then \(\delta>0\),
\[
\mathbb E T_h=\frac h\delta+O(1),\qquad
\frac{T_h-h/\delta}{\sqrt h}\ \xrightarrow{d}N\!\left(0,\frac{4pq}{\delta^3}\right).
\]
* If \(k<k_{\mathrm{crit}}(b)\), then \(q>p\),
\[
\mathbb E T_h\sim\frac{2pq}{(q-p)^2}\left(\frac qp\right)^h,\qquad
\frac{T_h}{\mathbb E T_h}\ \xrightarrow{\ d\ }\ \operatorname{Exp}(1).
\]

For example, \((b,k)=(2,2)\) has \(p=5/9\) and \(\mathbb E T_h=9h-40(1-(4/5)^h)\), while \((b,k)=(3,2)\) has \(p=7/16\) and \(\mathbb E T_h=-8h+(63/2)((9/7)^h-1)\). Both asymptotic statements concern fixed \(b,k\), not simultaneous growth of branching or offers.

## Assumptions and scope

The tree has one root at level zero, exactly \(b\) children per nonleaf vertex, and leaves at depth \(h\). All offers are independent between visits and between offered positions. The controller sees all offers at each step and can use arbitrary randomized history dependence. Time counts single edge traversals; the root is absorbing for the first-hitting problem. The parameter \(k\) counts offers, not the degree. The stochastic limits use the usual weak convergence of real random variables. The optimality statement is among every admissible history-dependent policy and is not an assertion about cover time, online routing without knowing the root, or cost other than first root hitting.

## Proof

**1. Optimal policy.** On levels \(0,1,\ldots,h\), consider the policy which always takes the parent if offered. Let \(H_i\) be its expected remaining root-hitting time from level \(i\). The finite state system is absorbing and has finite mean: from each vertex the chance that every offer equals its parent is at least \((b+1)^{-k}\) (or one at a leaf), so repeated blocks of at most \(h\) steps uniformly have a positive chance of absorption. For \(1\le i<h\), exactly one neighbor is the parent, so
\[
H_0=0,\quad H_h=1+H_{h-1},\quad H_i=1+pH_{i-1}+qH_{i+1}.
\]
For \(\Delta_i=H_i-H_{i-1}\), these give \(\Delta_h=1\) and
\[
\Delta_i=\frac{1+q\Delta_{i+1}}p>0\qquad(1\le i<h).
\]
Thus \(H_i\) strictly increases with depth. Selecting a parent when offered is exactly the action with least next-state value among each set of offers; when not offered all children have the same value. Therefore \(H\) satisfies the optimality (Bellman) equations on *every individual tree vertex*. If \(V\) is any admissible policy's remaining-hitting cost, then the process \(t+H_{\operatorname{depth}(X_t)}\) stopped on reaching the root is a submartingale under that policy. Optional stopping at the bounded times \(t\wedge T\) and nonnegativity give \(H\le\mathbb E T\), including policies of infinite mean. Consequently the stated parent-preference policy is globally optimal, not merely optimal among radial policies.

**2. Exact mean and sharp threshold.** Iterating the difference equation gives
\[
\Delta_i=\frac1\delta-\frac{2q}{\delta}\left(\frac qp\right)^{h-i}
\qquad(1\le i\le h,\;\delta\ne0).
\]
Summing over \(i\) yields the boxed exact mean. [At the hypothetical \(p=q=1/2\), the difference recursion instead gives \(\mathbb E T_h=h^2\).] Such a tie is impossible for integer \(b\ge2,k\ge1\): the equality \(p=q\) would give \(2b^k=(b+1)^k\), contradicting coprimality of \(b\) and \(b+1\), since \((b+1)^k\) cannot divide two. Hence \(p>q\) exactly when \((1+1/b)^k>2\). This proves the formula for \(k_{\mathrm{crit}}\), the two expected-time regimes, and the explicit examples.

**3. Gaussian law in the inward-bias phase.** Assume \(p>q\), with \(b,k\) fixed. Let \(Y_{h,i}\) be the time for the radial chain to first go from depth \(i\) to \(i-1\), starting at \(i\), for \(1\le i\le h\). Strong Markov at successive first-descents from \(h\) to \(0\) makes these \(h\) passage times independent, and \(T_h\overset d=\sum_{i=1}^hY_{h,i}\). At \(i=h\), the passage is one forced step. When the reflecting leaf boundary lies \(s=h-i\) levels beyond the starting level, the passage time is obtained by reflecting a nearest-neighbor walk with inward-step probability \(p\), outward probability \(q\). Let \(\tau\) be the unreflected time for such a walk, starting at zero, to first hit \(-1\). For \(p>q\) it has an exponential moment near zero and
\[
\mathbb E\tau=\delta^{-1},\qquad
\operatorname{Var}(\tau)=4pq\,\delta^{-3}.
\]
Indeed, the first-step generating function \(f(z)=\mathbb E[z^\tau]\) is the analytic near-one root of \(f(z)=z(p+q f(z)^2)\); differentiating once and twice at \(z=1\) gives these identities. Couple the reflected passage \(Y_{h,i}\) and \(\tau\) using the same steps until the first attempted step above its reflecting boundary at offset \(s\). The probability of reaching that offset before \(-1\) is at most \(C(q/p)^s\) by the biased gambler's-ruin formula (with \(C\) depending only on \(p,q\)). Reflection only hastens the descent, so \(Y_{h,i}\le\tau\) in this coupling, giving uniform moments of every fixed order. Hölder's inequality then gives exponentially small differences of the first two moments between \(Y_{h,i}\) and \(\tau\), as \(s\to\infty\). Summing over \(s=0,\ldots,h-1\),
\[
\mathbb E T_h=\frac h\delta+O(1),\qquad
\operatorname{Var}(T_h)=\frac{4pq}{\delta^3}h+O(1).
\]
The independent triangular array of centered \(Y_{h,i}\) has uniformly bounded third absolute moments, so Lyapunov's theorem implies the stated normal limit. The exact first-moment expression from step 2 is an independent check of its centering.

**4. Exponential law in the outward-bias phase.** Assume \(q>p\), put \(r=q/p>1\), and start at the leaf \(h\). Decompose the trajectory into i.i.d. excursions, each beginning with the forced step to \(h-1\), and then ending upon the next visit to \(h\) (failure) or to \(0\) (success). Let \(C_h\) be excursion length and \(S_h\) its success event. Standard finite-interval gambler's ruin gives exactly
\[
s_h=\Pr(S_h)=\frac{r-1}{r^h-1}\ \longrightarrow\ 0.
\]
In a coupling with an unbounded walk of outward drift \(q-p>0\), the excursion length is bounded by \(C_\infty=1+\tau'\), where \(\tau'\) is the first passage from \(h-1\) to \(h\) for the unbounded walk. The bound has a finite exponential moment, with \(\mu=\mathbb E C_\infty=1+1/(q-p)=2q/(q-p)\). As \(h\to\infty\), the upper root boundary recedes from the excursion and the finite excursion converges almost surely to \(C_\infty\); the success indicator tends to zero almost surely. Dominated convergence yields
\[
\mathbb E[C_h;S_h^c]\to\mu,\quad
\mathbb E[C_h;S_h]\to0.
\]
Writing \(F_h(z)=\mathbb E[e^{-zC_h};S_h^c]\) and \(G_h(z)=\mathbb E[e^{-zC_h};S_h]\), the exact excursion renewal identity reads
\[
\mathbb E[e^{-zT_h}]=\frac{G_h(z)}{1-F_h(z)}.
\]
Uniform second moments permit the expansion, for each fixed \(x\ge0\) and \(z=xs_h/\mu\),
\[
1-F_h(z)=s_h+xs_h+o(s_h),\qquad G_h(z)=s_h+o(s_h).
\]
Thus \(s_hT_h/\mu\Rightarrow\operatorname{Exp}(1)\). In the same way, the exact renewal mean satisfies \(\mathbb E T_h=\mathbb E C_h/s_h\sim\mu/s_h\). Since \(\mu/(r-1)=2pq/(q-p)^2\), the asserted exponential mean and normalization follow. The deterministic initial move and the success-excursion duration are included in this argument.

## Verification

The standalone program `check_tree_choice.py` uses only Python's standard library and checks exact rational Bellman equations on the **full labeled tree vertices** for branching \(b\in\{2,3,4\}\), heights \(h\in\{1,2,3\}\), and offer counts \(k\in\{1,2,3,4\}\), enumerating every ordered offered tuple. It separately checks exact mean and second-moment recurrences, the gambler's-ruin boundary problem, absence of integer ties over a larger finite grid, and two numerical asymptotic sanity checks based on exact rational means. Executing `python3 check_tree_choice.py` produced `PASS 3481 exact and analytic consistency assertions`. These finite checks do **not** certify either infinite limit; the proofs in steps 3 and 4 establish them.

## Relationship to prior work

Georgakopoulos, Haslegrave, Sauerwald and Sylvester first publicly posted their power-of-two-choices random-walk manuscript on 2019-11-12. Their 2022 open-access paper treats the exact two-neighbor-offer model, gives general finite-graph hitting and cover-time bounds and notes the outward drift on an infinite four-regular tree (especially their introduction, Theorem 1.1, and Section 5). Those statements already motivate the bias threshold and are **not** claimed as new. The theorem here specializes to rooted regular trees but supplies an all-integer \(b,k\) optimum, an exact finite leaf-to-root expectation, and a contrasting Gaussian/exponential *distributional* classification under depth growth, none of which was found as a theorem in that source. These are results about individual target hitting, not the source's general cover-time bound. The passage-time, gambler's-ruin, and renewal ingredients are standard; the combined exact classification is the candidate contribution. No historical-priority or independent-mathematical certification is claimed.

## Limitations

The classification assumes full regularity of the finite tree, root known to the controller, uniform independent offers with replacement, and fixed \(b,k\) when \(h\) grows. It does not cover varying degree, moves with nonuniform weighting, adversarial offers, unknown-target search, or joint scaling of branching and offered choices. The results neither prove a universal optimal policy on arbitrary graphs nor imply an efficient general cover-time strategy. Full historical priority cannot be established by a bounded literature search.

## References

1. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *The Power of Two Choices for Random Walks*, first public arXiv version 2019-11-12, arXiv:1911.05170; *Combinatorics, Probability and Computing* **31** (2022), 73–100, DOI:10.1017/S0963548321000183. Open-access full text: https://wrap.warwick.ac.uk/152060/7/WRAP-Power-two-choices-random-walks-2021.pdf .
2. The classical one-dimensional gambler's-ruin formula and the first-passage generating-function identity are used as standard facts; the needed formulas and boundary conditions are independently derived or checked in the proof and checker.
