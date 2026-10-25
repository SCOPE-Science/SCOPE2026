# Exact two-agent WEF1 census and an entitlement–sign entropy transition

## Finding
Consider two agents with positive entitlements \(w_1,w_2\) and \(m=p+q\ge1\) distinct indivisible items, each valued at \(+1\) by both agents for \(p\) items and at \(-1\) by both agents for \(q\) items. Write \(\alpha=w_1/(w_1+w_2)\), \(\beta=1-\alpha\), and
\[
z=q+\alpha(p-q)=\alpha p+\beta q.
\]
The exact number of labeled allocations satisfying **weighted envy-freeness up to one item** (WEF1), as defined by deletion of one positive item from the recipient or one negative item from the observer, is given below. Every allocation is Pareto optimal.

For integers \(n,k\), let \(B(n,k)=\binom nk\) when \(0\le k\le n\), and \(B(n,k)=0\) otherwise. If \(z\) is an integer, the answer is exactly \(B(m,z)\); in that case WEF1 and exact weighted envy-freeness (WEF) are equivalent on this instance. If \(z\notin\mathbb Z\), set \(k=\lfloor z\rfloor\), \(f=z-k\), and define two counts:
\[
L=\begin{cases}
B(m,k),&f\le\min\{\alpha,\beta\},\\
B(m,k)-B(q,k-p),&\alpha>\beta,\ \beta<f\le\alpha,\\
B(m,k)-B(p,k-q),&\beta>\alpha,\ \alpha<f\le\beta,\\
0,&f>\max\{\alpha,\beta\},
\end{cases}
\]
\[
U=\begin{cases}
B(m,k+1),&1-f\le\min\{\alpha,\beta\},\\
B(m,k+1)-B(p,k+1),&\alpha>\beta,\ \beta<1-f\le\alpha,\\
B(m,k+1)-B(q,k+1),&\beta>\alpha,\ \alpha<1-f\le\beta,\\
0,&1-f>\max\{\alpha,\beta\}.
\end{cases}
\]
Then the exact number is \(N_{p,q}(\alpha)=L+U\). The cases for each expression are mutually exclusive and exhaustive.

Two exact consequences are:

* With equal entitlements, for **any** distribution of the common positive and negative unit items, the WEF1 count is \(\binom{m}{m/2}\) for even \(m\), and \(2\binom{m}{(m-1)/2}\) for odd \(m\).
* With \(p=q\), for **every** positive entitlement pair, WEF1 coincides with exact WEF and the count is \(\binom{2p}{p}\). Hence unweighted random allocation is WEF1 with probability asymptotic to \(\sqrt{2/(\pi m)}\) in the even, zero-net-value case, independent of entitlement asymmetry.

More generally, choose each item's recipient independently and fairly. For fixed \(0<\alpha<1\) and sequences of mixed instances with \(p/m\to\lambda\in(0,1)\), put \(t=\alpha\lambda+\beta(1-\lambda)\) and \(H(t)=-t\log t-(1-t)\log(1-t)\). Then
\[
\lim_{m\to\infty}\frac1m\log\Pr(\mathrm{WEF1})=H(t)-\log2.
\]
This rate is strictly negative precisely when \(\alpha\ne1/2\) and \(\lambda\ne1/2\): with fixed unequal entitlements and a fixed nonzero signed-item imbalance, a uniformly sampled Pareto-optimal allocation is exponentially unlikely to satisfy WEF1, even though fair allocations exist.

The crossover is explicit. If \(T=p-q\) satisfies \(T/\sqrt m\to\tau\), define
\[
K_m=\#\{j\in\mathbb Z:|j-(m/2+(\alpha-1/2)T)|\le\max\{\alpha,\beta\}\}.
\]
Then \(K_m\in\{1,2\}\) and
\[
\Pr(\mathrm{WEF1})=\sqrt{\frac{2}{\pi m}}\exp\left(-2(\alpha-\tfrac12)^2\tau^2\right)(K_m+o(1)).
\]
The integer factor records a genuine lattice-phase effect; no limiting prefactor is asserted when \(K_m\) oscillates.

## Assumptions and scope
There are exactly two agents, every item has identical additive unit value for both, all items are individually distinguishable, every item is allocated, and entitlements are arbitrary positive real numbers. The random-allocation experiment independently chooses one of the two recipients for each item with probability \(1/2\); it does not sample uniformly from entitlement-aware allocations or from WEF1 allocations. WEF1 uses the standard mixed-manna rule in which an observer may remove one positively valued item from the other bundle or one negatively valued item from the observer's bundle. All logarithms are natural. The asymptotic entropy statement fixes \(\alpha\) and requires both sign classes to have positive limiting proportions; the critical-window statement has \(m\to\infty\) with compatible integer counts \(p,q\ge0\).

## Proof
**1. A complete arithmetic characterization.** Let agent 1 receive \(a\) positive and \(b\) negative items; her utility is \(x=a-b\), agent 2's is \(T-x\), and \(T=p-q\). Exact weighted non-envy of either agent is equivalent to \(x=\alpha T\). If \(x<\alpha T\), only agent 1 envies. Removing one negative item from her bundle is available exactly when \(b>0\), and repairs envy exactly when \(\alpha T-x\le\beta\); removing a positive item from agent 2's bundle is available exactly when \(p-a>0\), and repairs it exactly when \(\alpha T-x\le\alpha\). If \(x>\alpha T\), only agent 2 envies; removal of her own negative item works exactly when \(q-b>0\) and \(x-\alpha T\le\alpha\), while removal of a positive item from agent 1 works exactly when \(a>0\) and \(x-\alpha T\le\beta\). These equivalences follow by multiplying the defining inequalities by the positive quantity \(w_1w_2/(w_1+w_2)\). They cover all bundles, including empty ones.

**2. Exact counting.** Put \(y=x+q=a+(q-b)\). Every allocation is encoded by a length-\(m\) binary word indicating the positive items assigned to agent 1 and the negative items assigned to agent 2, so the number with \(y=j\) is \(B(m,j)\). The arithmetic inequalities in step 1 imply \(|y-z|<1\), hence only \(\lfloor z\rfloor\) and \(\lceil z\rceil\) can contribute. When \(z\) is integral, only \(y=z\) works and gives exact WEF. For nonintegral \(z\), every allocation in the lower layer works if \(f\le\min\{\alpha,\beta\}\): at least one corrective item must exist, since otherwise agent 1 would already have the maximal possible utility \(p\), contradicting envy. If only deletion from agent 2's positive items is effective, the excluded lower-layer assignments give all \(p\) positives to agent 1, a set counted by \(B(q,k-p)\). If only deletion from agent 1's negative items is effective, the excluded assignments give all \(q\) negatives to agent 2, counted by \(B(p,k-q)\). The corresponding upper-layer arguments, with agents reversed, exclude respectively \(B(p,k+1)\) when every negative goes to agent 1 and \(B(q,k+1)\) when every positive goes to agent 2. This proves the stated piecewise formula, including all boundary equalities.

At equal weights \(z=m/2\), so the only qualifying layers are the central one (even \(m\)) or the two central ones (odd \(m\)), with no deletability exceptions. If \(p=q\), then \(z=m/2\) is integral for any weight, proving the zero-net-value collapse to exact WEF. Finally, the aggregate utility \(v(A_1)+v(A_2)=p-q\) is allocation-independent. A Pareto improvement would strictly increase this sum, which is impossible; hence every allocation is PO.

**3. Entropy rate.** In a uniform random allocation, the \(m\) binary indicators counted in \(y\) are independent fair Bernoulli variables; consequently \(y\sim\operatorname{Bin}(m,1/2)\), even though some original item values are negative. Write \(\gamma=\max\{\alpha,\beta\}\). Every WEF1 allocation belongs to one of the one or two integer layers \(|y-z|\le\gamma\). There is always at least one such layer. For \(p/m\to\lambda\in(0,1)\), \(z/m\to t\in(0,1)\). Conditional on any contributing layer, the four boundary events that could prevent deletion (all positives on one side or all negatives on one side) have probabilities exponentially small in \(m\). For example, when \(y=j\), the probability that all \(p\) positives are assigned to agent 1 is at most \((j/m)^p\), and the probability that none are is at most \(((m-p)/m)^j\); analogous bounds hold for the \(q\) negatives. The fractions stay bounded away from one, and their exponents are linear in \(m\). Therefore each eligible layer contributes \((1-e^{-\Omega(m)})B(m,j)\) allocations. Stirling's formula for the one or two layers with \(j/m\to t\) yields the entropy rate. The identity \(t-1/2=(\alpha-1/2)(2\lambda-1)\) gives the strict-negativity criterion.

**4. Critical window and lattice factor.** If \(T/\sqrt m\to\tau\), then \(p/m,q/m\to1/2\) and \(z=m/2+(\alpha-1/2)T\). The binomial local central limit theorem gives, uniformly over the at most two qualifying layers,
\[
2^{-m}B(m,j)=\sqrt{\frac2{\pi m}}\exp\left[-2(\alpha-\tfrac12)^2\tau^2\right](1+o(1)).
\]
The boundary-event exclusion is still exponentially smaller. Summing over exactly \(K_m\) admissible layers proves the displayed crossover with its lattice factor.

## Verification
The accompanying standalone script `verify.py` directly implements the defining two-direction WEF1 inequalities using exact rational arithmetic. It separately implements the derived count formula and checks every labeled allocation with \(1\le m\le11\), every feasible positive/negative item count, and seven nonidentical entitlement ratios: \(315{,}392\) direct classification checks, plus count checks and the equal-weight and zero-total identities. All passed. For example, \(m=20\), \(p=15\), \(q=5\), and \(w_1:w_2=3:1\) have exactly \(203{,}385\) WEF1 assignments of \(2^{20}\), while \(p=q=10\) gives \(184{,}756\) irrespective of the positive entitlement ratio. Finite tests do not prove the asymptotic statements; those follow analytically from the counting formula and Stirling/local-limit estimates.

## Relationship to prior work
Teh (2026, arXiv:2609.01580), particularly Definition 2.1, Theorem 3.1, and Section 4, provides the general mixed-item WEF1 framework, existence theorem, and equal-magnitude guarantees. Lin, Liu, Tao, and Zhou (2026, arXiv:2609.02724) independently establish general mixed-manna WEF1 existence and study lotteries with different ex-ante/ex-post fairness requirements. Garg and Sharma (2024, arXiv:2410.12966) give the earlier two-agent existence algorithm. Manurangsi, Suksompong, and Yokoyama (2025, arXiv:2504.21728) study asymptotic existence of fair allocations under random valuations, not the fraction of randomly selected allocations that are WEF1 under fixed, perfectly correlated signed valuations. None of the inspected relevant statements contains the exact signed-unit two-agent WEF1 enumeration or its entitlement–imbalance entropy transition. The result does not claim originality for binomial identities, Stirling's formula, or the general WEF1 definitions and existence theorems.

## Limitations
This is a structured two-agent equal-unit model, not a theorem for heterogeneous or arbitrary-magnitude valuations. The exponential rarity statement concerns *uniform uninformed* random assignment, not the computational difficulty of finding WEF1 (known algorithms find such allocations). A structural formula may be an unrecorded corollary of broader enumeration results; literature search and mathematical-record checks are not proof of priority. The exact closed count does not imply analogous counting formulas for three agents or for unequal unit magnitudes. Independent validation has not been performed.

## References
1. Nicholas Teh, *Weighted Fair Division of Indivisible Mixed Manna*, arXiv:2609.01580, first submitted 2026-09-01, https://arxiv.org/abs/2609.01580.
2. Zehan Lin, Shengxin Liu, Biaoshuai Tao, and Shengwei Zhou, *Almost Envy-Freeness for Additive Mixed Manna with Entitlements: Deterministic and Randomized Guarantees*, arXiv:2609.02724, first submitted 2026-09-02, https://arxiv.org/abs/2609.02724.
3. Jugal Garg and Eklavya Sharma, *EF1 for Mixed Manna with Unequal Entitlements*, arXiv:2410.12966, 2024-10-16, https://arxiv.org/abs/2410.12966.
4. Pasin Manurangsi, Warut Suksompong, and Tomohiko Yokoyama, *Asymptotic Analysis of Weighted Fair Division*, arXiv:2504.21728, 2025-04-30, https://arxiv.org/abs/2504.21728.
