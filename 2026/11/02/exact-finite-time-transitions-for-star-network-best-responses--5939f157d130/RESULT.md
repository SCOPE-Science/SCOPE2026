# Exact finite-time transitions for star-network best responses

## Finding

For every integer \(s\ge2\), consider a star with one hub and \(s\) leaves in the linear strategic-substitutes public-good game. Let \(0<\delta<1\). Under the **leaf-first sweep** (update each leaf exactly once in any order, then update the hub), write \(R_s(\delta)\) for the maximum, over all initial states, of the number of completed sweeps before the hub first becomes exactly inactive. In the regime \(1/s<\delta<1\), this maximum is finite, attained by initial hub activity \(1\), and has the exact formula

\[
R_s(\delta)=\begin{cases}
\left\lceil\dfrac{\log \Theta}{\log(s\delta^2)}\right\rceil,&s\delta^2\ne1,\\[6pt]
\left\lceil\dfrac{1}{\sqrt{s}-1}\right\rceil,&s\delta^2=1,
\end{cases}
\qquad
\Theta=\frac{s\delta-1}{s\delta(1-\delta)}.
\]

After those hub-ending sweeps, one further leaf-only sweep attains the exact unique equilibrium, with hub activity zero and every leaf activity one. For \(0<\delta\le1/s\), the leaf-first trajectory starting with hub activity one never attains its equilibrium in finitely many sweeps. Thus \(1/s\) is the exact finite-versus-asymptotic threshold for this protocol. For fixed \(s\ge2\), its exact worst-case cutoff has symmetric endpoint growth

\[
R_s(\delta)=\frac{\log(1/(\delta-1/s))}{\log s}+O_s(1)
\quad(\delta\downarrow1/s),\qquad
R_s(\delta)=\frac{\log(1/(1-\delta))}{\log s}+O_s(1)
\quad(\delta\uparrow1).
\]

One sweep makes the hub inactive from every initial state precisely when \(s\delta(1-\delta)\ge1\). This occurs for some \(\delta\) if and only if \(s\ge4\), and then exactly on
\[
\frac{1-\sqrt{1-4/s}}2\le\delta\le
\frac{1+\sqrt{1-4/s}}2.
\]
In particular, with four leaves, this one-sweep window is the single point \(\delta=1/2\).

The same regime has an **exact finite-absorption guarantee under random asynchronous best responses**: when a single uniformly random agent updates each step, from every initial state the process hits the exact equilibrium in finite time almost surely, with an explicit geometric tail. Starting instead from hub activity one and zero leaf activities and updating each vertex once in a uniformly random permutation, the probability of deactivating the hub within that one pass is exactly
\[
\frac{\max\{0,s-\lceil1/[\delta(1-\delta)]\rceil+1\}}{s+1}.
\]

## Assumptions and scope

The graph is the unweighted, undirected star \(K_{1,s}\). Each activity lies in \([0,1]\). The hub and leaf best-response maps are
\[
B_0(\ell_1,\ldots,\ell_s)=\max\{0,1-\delta\sum_{i=1}^s\ell_i\},\qquad
B_i(c)=\max\{0,1-\delta c\}=1-\delta c,
\]
where \(0<\delta<1\). A leaf-first sweep means precisely one update for each leaf, with the hub fixed, followed by exactly one hub update. The last probability formula instead concerns one uniformly random *permutation* of all agents, and the almost-sure absorption statement concerns independent uniformly random selections *with replacement*. These are three distinct scheduling conventions; no conclusion equates their hitting-time distributions.

For the stochastic tail define \(r=R_s(\delta)\), \(L=r(s+1)+s\), and
\[
q=\frac{(s!)^{r+1}}{(s+1)^L}>0.
\]
For the first time \(T\) when the exact equilibrium is reached, measured in individual updates, the bound is
\[
\Pr\{T>jL\}\le(1-q)^j\quad(j=0,1,2,\ldots),
\qquad \mathbb E[T]\le L/q.
\]
The bound is explicit and generally conservative; it is not asserted to be the optimal expected hitting time.

## Proof

**1. Sweep reduction.** The current hub activity is \(c\in[0,1]\). After all leaves respond, each has activity \(1-\delta c\) independently of its previous value and of leaf update order. The new hub activity is therefore
\[
F(c)=\max\{0,a+bc\},\qquad a=1-s\delta,\quad b=s\delta^2>0.
\]
The map is nondecreasing in \(c\), so for any initial hub \(c_0\in[0,1]\), its activity after \(r\) sweeps is at most \(F^r(1)\). Starting from \(c_0=1\) attains equality, regardless of initial leaf values. In particular, the resulting worst-case sweep cutoff is sharp rather than merely an upper bound.

**2. Exact equilibrium and phase boundary.** In any equilibrium with positive hub activity, all leaves have activity \(1-\delta c>0\), and the hub equation is
\[
(1-s\delta^2)c=1-s\delta.
\]
For \(s\delta<1\), this has the unique feasible solution \(c_*=(1-s\delta)/(1-s\delta^2)\in(0,1)\). At \(s\delta=1\), the only feasible equilibrium has \(c=0\). For \(s\delta>1\), a positive solution is impossible: if \(s\delta^2\le1\) the signs conflict; otherwise the formal solution \((s\delta-1)/(s\delta^2-1)>1\). Thus for \(s\delta\ge1\), the unique equilibrium is \((c,\ell_1,\ldots,\ell_s)=(0,1,\ldots,1)\). The hub best response there is zero.

For \(s\delta<1\), the sweep iterates from \(c_0=1\) remain positive and obey \(c_r-c_*=b^r(1-c_*)>0\); they never reach the equilibrium in finite time. At \(s\delta=1\), they obey \(c_r=s^{-r}>0\) and likewise never hit the equilibrium. The zero versus positive distinction is exact, not a numerical tolerance effect.

**3. Sharp integer cutoff.** Suppose \(s\delta>1\). Until the hub first hits zero, the untruncated recurrence is \(y_0=1\), \(y_{r+1}=a+by_r\). Since \(a<0\), once \(y_r\le0\) all subsequent untruncated iterates are negative; clipping therefore does not alter the first crossing index. For \(b\ne1\),
\[
y_r=b^r+a\frac{b^r-1}{b-1}.
\]
Putting \(\Theta=(s\delta-1)/[s\delta(1-\delta)]\), note that \(\Theta-1=(b-1)/[s\delta(1-\delta)]\). Algebra gives \(y_r\le0\) if and only if \(b^r\le\Theta\) for \(b<1\), and if and only if \(b^r\ge\Theta\) for \(b>1\). Both regimes give the displayed ceiling formula. At \(b=1\), \(y_r=1-r(\sqrt s-1)\), giving its stated branch. The hub is zero after exactly \(R_s(\delta)\) sweeps when \(c_0=1\), and is zero no later from any other initial hub activity. The leaves at the last hub update equal \(1-\delta c_{r-1}<1\); they become exactly one during one further leaf sweep, after which the profile is an equilibrium and stays unchanged.

The one-sweep condition is \(F(1)=0\), equivalently \(s\delta(1-\delta)\ge1\). Because the maximum of \(\delta(1-\delta)\) over \((0,1)\) is \(1/4\), this is feasible exactly when \(s\ge4\), with the displayed closed interval of solutions. The lower-end asymptotics follow from \(\Theta\asymp_s \delta-1/s\) and \(b\to1/s\); the upper-end asymptotics follow from \(\Theta\asymp_s (1-\delta)^{-1}\) and \(b\to s\). Taking logarithms and accounting for the ceiling gives both \(O_s(1)\) remainders.

**4. Uniform random asynchronous updates.** Partition the infinite stream of independently uniformly selected updating agents into consecutive chunks of length \(L\). Call a chunk successful if its first \(r\) subblocks consist of all \(s\) leaves once, in any order, then the hub, and its final \(s\) positions contain all leaves once. Its probability is \(q=(s!)^{r+1}/(s+1)^L\). For *every* possible state at the start of a successful chunk, the hub ends the \(r\) subblocks at zero by the monotonic sweep bound, and the final leaf updates make all leaves one, hence the process reaches the exact equilibrium. Successful chunks are independent across time. Failure to hit equilibrium through \(j\) chunks implies none of those chunks is successful. This proves \(\Pr\{T>jL\}\le(1-q)^j\) and summing the tail in length-\(L\) blocks gives \(\mathbb E[T]\le L/q\).

**5. One uniformly random permutation.** Initially the hub is one and all leaves are zero. If \(K\) leaves are visited before the hub, exactly those \(K\) leaves acquire activity \(1-\delta\); the hub's sole update sets its activity to \(\max\{0,1-\delta K(1-\delta)\}\). It cannot change during the remaining leaf updates. A uniform permutation makes \(K\) uniform on \(\{0,1,\ldots,s\}\). Counting the values that satisfy \(K\ge1/[\delta(1-\delta)]\) proves the probability formula, including integer-tie boundary cases.

## Verification

The standalone `verifier.py` uses Python's `fractions.Fraction` for exact rational best-response simulation. It checked the recurrence, the first hitting index and the one-sweep condition for 82,953 eligible \((s,\delta)\) pairs with \(2\le s\le30\) and rational \(\delta\) of denominator at most 80, plus varied initial hub activities. It checked finite nonattainment at and below the threshold, a deterministic certificate for arbitrary initial states, and the exact permutation-deactivation count by enumerating all vertex orders on 27 small parameter instances. The source code supplies the precise loops and assertions; these finite checks are not a substitute for the preceding all-parameter proof. To reproduce, run `python verifier.py` in the directory containing this file.

## Relationship to prior work

Misiak and Dziubiński, *Convergence rates of random-order best-response dynamics in public good games on networks* (arXiv:2602.15986, first public version February 17, 2026), give the same linear best-response model, analyze convergence in probability, and show numerical star/complete-bipartite convergence-time plots. Their Section 2 uses tolerance-based approximate stopping and Sections 3.1–3.2 focus on graph structure and active-set stability. The material inspected does not contain this exact leaf-first first-zero index, its two logarithmic endpoint laws, the four-leaf one-sweep threshold, the one-pass random-permutation probability, or the uniform exact-absorption tail. The stochastic and deterministic schedules must not be conflated.

Bramoullé, Kranton and D'Amours, *Strategic Interaction and Networks* (American Economic Review 104 (2014), 898–930), establish the general best-response model and, in Example 2, already characterize the Nash equilibria on a star. Accordingly, the equilibrium classification is **background, not claimed as novel**. The contribution is the exact transient first-hitting classification and its qualitative phase consequences. An equivalent unindexed analysis of sequential star updates remains possible.

## Limitations

Only unweighted stars with common substitution strength \(0<\delta<1\) are covered. The explicit sweep count is sharp for the stipulated leaf-first order and worst-case initial hub state, not for arbitrary fair orders or uniformly random schedules. The random hitting bound is valid but generally not sharp, and the permutation formula concerns hub deactivation, not completion of the entire equilibrium. At \(\delta=1\) a second equilibrium exists, so that boundary is intentionally excluded. This work neither analyzes general graph mixing times nor asserts that finite parameter checks prove an infinite theorem. No independent scientific validation has been performed.

## References

1. W. Misiak and M. Dziubiński, *Convergence rates of random-order best-response dynamics in public good games on networks*, arXiv:2602.15986v1 (February 17, 2026), https://arxiv.org/abs/2602.15986.
2. Y. Bramoullé, R. Kranton and M. D'Amours, *Strategic Interaction and Networks*, American Economic Review **104** (2014), 898–930, https://doi.org/10.1257/aer.104.3.898.
