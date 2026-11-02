# A drifting worst-case Bernoulli rate for ex-post EF1 with two goods per participant

## Finding
Fix an integer \(n\ge2\), and allocate \(2n\) distinct indivisible goods before their utility values are observed, with exactly two goods assigned to each of \(n\) participants. For every participant–good pair, independently draw an additive value in \(\{0,1\}\) with common success probability \(p\in[0,1]\). The allocation is envy-free in expected utilities. Its probability of being envy-free up to one good (EF1) after the values are realized equals
\[
P_n(p)=\left(1-(1-p)^2\left[1-(1-p^2)^{n-1}\right]\right)^n.
\]
For every \(n\ge2\), this probability has a **unique global minimum** on \([0,1]\), attained at the unique \(p_n\in(0,1)\) solving
\[
(n-1)p_n(1-p_n)(1-p_n^2)^{n-2}=1-(1-p_n^2)^{n-1}.
\]
The minimizing parameter decreases strictly in \(n\); in particular, \(p_2=1/2\) and \(p_n<1/2\) for \(n>2\). Its precise asymptotic scale and the worst EF1 probability are
\[
p_n^2=\frac{\log n+\log\log n-\log 2+o(1)}{2n},
\]
\[
\log P_n(p_n)=-\frac n2\log n+\frac n2\log\log n+\frac n2\log2+o(n).
\]
The minimal bundle size at which EF1 can fail is two; an allocation with at most one good per participant is automatically EF1 for nonnegative additive values. Thus this is the first nontrivial equal-bundle regime, not an arbitrarily chosen number of goods.

## Assumptions and scope
Let \(N=\{1,\ldots,n\}\) and \(M=\{1,\ldots,2n\}\). Fix any deterministic partition \(A=(A_i)_{i\in N}\) with \(|A_i|=2\). For each ordered pair \((i,g)\in N\times M\), let \(X_{ig}\) be an independent Bernoulli\((p)\) variable, with independence **both across goods and across participants**. Write \(v_i(S)=\sum_{g\in S}X_{ig}\). Ex-ante envy-freeness here means \(\mathbb E v_i(A_i)\ge\mathbb E v_i(A_j)\) for every \(i,j\); since both expectations are \(2p\), this holds with equality. Realized EF1 means that for each pair of distinct participants \(i,j\) there exists \(g\in A_j\) with \(v_i(A_i)\ge v_i(A_j\setminus\{g\})\). Probabilities are entirely over the exogenous utility variables; the allocation is not randomized or adapted to them.

## Proof
**Exact probability.** For each participant \(i\), the best deletion from a rival's two-good bundle leaves value \(\min\{X_{ig_1},X_{ig_2}\}\), either zero or one. Consequently, a realized EF1 violation by \(i\) occurs if and only if its own two goods both have value zero and at least one rival's two goods both have value one *from that participant's perspective*. The own-zero event has probability \((1-p)^2\); the \(n-1\) rival double-one events are independent with probability \(p^2\) each. The participant's failure probability is
\[
f_m(p)=(1-p)^2\left[1-(1-p^2)^m\right],\qquad m=n-1.
\]
Crucially, different participants' conditions concern disjoint sets of random variables \(\{X_{ig}:g\in M\}\), even when they compare the same physical goods. They are therefore independent, giving \(P_n(p)=(1-f_{n-1}(p))^n\).

**Single interior minimizer and population monotonicity.** Put \(m=n-1\), \(r=1-p^2\). On \(0<p<1\), differentiation gives
\[
f_m'(p)=2(1-p)\left[mp(1-p)r^{m-1}-(1-r^m)\right].
\]
Using \(1-r^m=(1-r)\sum_{k=0}^{m-1}r^k\), the sign is that of \(1-G_m(p)\), where
\[
G_m(p)=\frac{p}{m(1-p)}\sum_{j=0}^{m-1}(1-p^2)^{-j}.
\]
Each summand and the leading odds factor are positive and nondecreasing in \(p\), and the leading factor is strictly increasing; hence \(G_m\) is strictly increasing from zero to infinity. Thus \(f_m\) first increases and then decreases, and its unique maximum corresponds to the claimed unique minimum of \(P_n\). Both endpoints have \(f_m=0\). For fixed \(p\in(0,1)\), the average of the first \(m\) terms of the strictly increasing sequence \(r^{-j}\) strictly increases with \(m\). Therefore \(G_{m+1}(p)>G_m(p)\), and the unique roots \(p_n\) strictly decrease as \(n\) increases. At \(m=1\), \(G_1(p)=p/(1-p)\), hence \(p_2=1/2\). Direct substitution gives \(P_2(p_2)=225/256\).

**Asymptotic location and minimum.** Let \(m=n-1\), \(p=p_n\), and \(t=mp^2\). Choosing the test point \(p=\sqrt{(\log m)/m}\) for large \(m\) shows \(\max_{p\in[0,1]}f_m(p)\to1\). Since \(f_m(p_n)\le(1-p_n)^2\) and \(f_m(p_n)\le1-(1-p_n^2)^m\), this forces \(p_n\to0\) and \((1-p_n^2)^m\to0\), hence \(t\to\infty\). Logarithms of the critical equation yield
\[
(m-1)[-\log(1-p^2)]=\log(mp(1-p))-\log\left(1-(1-p^2)^m\right)
=\tfrac12\log(mt)+o(1).
\]
The left-hand side is at least \((1-1/m)t\), which forces \(t=O(\log m)\). Hence \((m-1)[-\log(1-p^2)]=t+O(t^2/m)+O(t/m)=t+o(1)\). It follows that
\[
2t=\log m+\log t+o(1),\qquad t\sim\tfrac12\log m,
\]
and substituting the latter estimate back gives
\[
2t=\log m+\log\log m-\log2+o(1).
\]
Replacing \(m=n-1\) by \(n\) yields the stated expansion for \(p_n^2\). Also, the critical equation implies
\[
(1-p_n^2)^m=\frac{(1-p_n^2)\left[1-(1-p_n^2)^m\right]}{mp_n(1-p_n)}\sim\frac1{mp_n}.
\]
Writing \(q_n=1-f_m(p_n)\), we obtain
\[
q_n=2p_n-p_n^2+(1-p_n)^2(1-p_n^2)^m=2p_n(1+o(1)),
\]
since the final term is \(o(p_n)\) by \(mp_n^2=t\to\infty\). Finally, \(\log P_n(p_n)=n\log q_n=n\log(2p_n)+o(n)\), yielding the logarithmic expansion claimed above. This proof uses exact finite probability identities and a deterministic asymptotic analysis, not a finite experiment to infer an infinite theorem.

## Verification
Run `python3 verify.py` with the standard Python 3 library. The checker independently enumerates full binary utility rows for \(2\le n\le6\) at three rational parameters, and full agent–good utility matrices for selected \(n=2,3\) cases. It compares exact rational probabilities to the formula, numerically brackets the unique critical root through \(n=200\), checks strict movement, and checks its asymptotic scale through \(n=100000\). Finite checks are supplementary; the proof above establishes the claim for every integer \(n\ge2\) and every real \(p\in[0,1]\).

## Relationship to prior work
Chen and Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness* (2026), analyze randomized **online allocation** on deterministic valuation instances against nonadaptive adversaries; their EF1 success bounds address the randomness of allocation rules, rather than the probability that a *predetermined equal-size allocation* satisfies EF1 under mutually independent Bernoulli valuations. Bu, Li, Liu, Lu and Tao, *Best-of-Both-Worlds Fair Allocation of Indivisible and Mixed Goods* (2024), obtain ex-ante and ex-post guarantees by **choosing suitable randomized allocations conditional on fixed known valuations**. The present result instead quantifies the exact risk faced by a nonadaptive balanced assignment with stochastic valuations, and finds the worst common success parameter. Their guarantees do not give this formula, root uniqueness, population monotonicity or rare-event logarithmic asymptotics. The broader literature of binary-valuation EF1 usually prescribes allocations after values are known; it does not automatically determine the chance that a frozen assignment is fair.

## Limitations
The result assumes independence for every participant–good pair and one common Bernoulli parameter. It does not extend as stated to common shocks, heterogeneous probabilities, nonbinary values, unequal bundle sizes or valuations observed before allocation. Nor does it assert the fixed allocation is optimal under any policy that can adapt to realizations. The logarithmic asymptotic has an \(o(n)\) remainder and is not a uniform finite-\(n\) approximation bound. An earlier unindexed equivalent theorem may exist; independent priority and proof audits have not been performed.

## References
1. Tianqi Chen and Jingxiao Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness*, arXiv:2609.23577v1, first available 2026-09-20, https://arxiv.org/abs/2609.23577 (especially Sections 2 and 4).
2. Xiaolin Bu, Zihao Li, Shengxin Liu, Xinhang Lu and Biaoshuai Tao, *Best-of-Both-Worlds Fair Allocation of Indivisible and Mixed Goods*, arXiv:2410.06877v1, first available 2024-10-09, https://arxiv.org/abs/2410.06877 (especially Sections 1 and 2).
