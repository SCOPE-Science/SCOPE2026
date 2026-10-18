# Strict Schur-concavity of coupon coverage under independent losses

## Finding

**Theorem (simultaneous-coverage optimization).** Let \(n\ge 2\) and let \(w=(w_1,\ldots,w_n)\) be a vector of positive drawing probabilities with \(\sum_i w_i=1\). Starting from the empty set, independently draw one coupon label with law \(w\) at each integer time \(s\ge1\), add that label to the currently present set, and *after the draw* independently retain each currently present type with probability \(q_s\in(0,1]\). The retention decisions are independent across types, times, and draws, while \(q_s\) is common to the types at time \(s\).

Fix a target set \(A\subseteq[n]\) with \(m=|A|\ge2\), and write
\[
F_{A,t}(w)=\Pr_w\{A\subseteq S_t\}.
\]
For every \(t\ge m\), this probability is **strictly Schur-concave in the positive coordinates \((w_i)_{i\in A}\)** with their sum fixed and all probabilities outside \(A\) fixed. Specifically, replacing any unequal pair \(w_i,w_j\), with \(i,j\in A\), by a strictly more balanced positive pair with the same sum strictly increases \(F_{A,t}\). Thus, conditional on a fixed total drawing mass assigned to \(A\), the unique optimal allocation among its types is equal allocation. In particular, for \(A=[n]\), the uniform drawing law uniquely maximizes the probability of complete coverage at every \(t\ge n\).

If \(q_s=q\in(0,1)\) for all \(s\), the finite-state chain has a unique stationary distribution \(\pi_w\). Its target coverage probability \(\pi_w\{A\subseteq S\}\) obeys the **same strict Schur-concavity and unique equal-allocation principle**. For \(n=2\), writing \(w_1=a\), \(w_2=1-a\), the stationary probability is explicitly
\[
\pi_w\{\{1,2\}\subseteq S\}
=\frac{q^3(2-q)a(1-a)}{1-q+q^2a(1-a)}.
\]
The stationary strictness assumption \(q<1\) is essential: at \(q=1\), every positive drawing law eventually reaches complete coverage, so stationary complete coverage has probability one.

## Assumptions and scope

A type that is selected is present just before the loss step, even if it was previously absent. It must survive that same loss step to be present afterwards. Each loss is applied independently to each currently present type; there is no single reset erasing all types simultaneously. The draw vector \(w\) is fixed across rounds. Loss-retention probabilities \((q_s)\) may vary arbitrarily in time, but not across coupon types. All target drawing weights are strictly positive; at boundary vectors with a missing target type, its coverage probability is zero.

The optimized event is simultaneous presence at the **specified observation time**, not the event that simultaneous presence has occurred at *some earlier time*. No hitting-time stochastic order is asserted. The stationary assertion requires a time-homogeneous \(q\in(0,1)\).

## Proof

**1. Last-selection identity.** Fix \(t\) and condition on the entire drawing word \((C_1,\ldots,C_t)\). If type \(i\) has not appeared, it is absent. Otherwise let \(L_i=\max\{s\le t:C_s=i\}\). Since there is no later refresh of that type, it is present at time \(t\) precisely when it survives the independent loss decisions in rounds \(L_i,L_i+1,\ldots,t\). Define
\[
Q_t(s)=\prod_{r=s}^t q_r.
\]
Then \(\Pr(i\in S_t\mid C_1,\ldots,C_t)=Q_t(L_i)\), and conditional independence of the losses for distinct types gives
\[
\Pr(A\subseteq S_t\mid C_1,\ldots,C_t)
=\prod_{i\in A}Q_t(L_i)
\]
when every member of \(A\) has appeared, and zero otherwise. Observe that \(Q_t(s)\) is nondecreasing in \(s\) and is positive.

**2. Conditioning on the two-type superposition.** Choose \(i,j\in A\), let \(h=w_i+w_j\), and set \(a=w_i/h\), \(b=1-a\). Fix the locations \(s_1<\cdots<s_M\) of all draws from \(\{i,j\}\), as well as the labels of every other draw. This conditioning does not depend on \(a\) as long as \(h\) and the other weights are fixed. At these \(M\) locations, the two labels are independent, with probabilities \(a,b\).

If \(M<2\), simultaneous presence of \(i,j\) is impossible. Suppose \(M\ge2\). Let \(K\in\{1,\ldots,M\}\) denote the length of the terminal monochromatic run in the two-type word; \(K=M\) means all \(M\) labels agree. For every \(1\le k\le M\), the elementary exact identity is
\[
\Pr(K\ge k\mid s_1,\ldots,s_M)=a^k+b^k.
\]
For \(1\le k<M\) define
\[
f(k)=Q_t(s_M)Q_t(s_{M-k}),\qquad f(M)=0.
\]
The two types' last draws are at \(s_M\) and \(s_{M-K}\) when \(K<M\), so the conditional joint-presence probability is exactly \(\mathbb E[f(K)]\). Because \(Q_t\) is nondecreasing, \(f\) is nonincreasing, and \(f(1)>0\).

The tail-sum identity now yields the exact positive-coefficient decomposition
\[
\mathbb E[f(K)]
=f(1)-\sum_{k=2}^M\bigl(f(k-1)-f(k)\bigr)
\bigl(a^k+(1-a)^k\bigr).
\tag{1}
\]
Each coefficient \(f(k-1)-f(k)\) is nonnegative; their sum equals \(f(1)>0\). For every integer \(k\ge2\), \(a^k+(1-a)^k\) strictly increases with \(|a-1/2|\). Therefore (1) strictly increases when the allocation \((a,1-a)\) is balanced toward \((1/2,1/2)\), as long as \(M\ge2\).

**3. Other target types and strictness.** The conditional survival contribution from the other target types is a nonnegative factor
\[
G=\prod_{\ell\in A\setminus\{i,j\}}Q_t(L_\ell),
\]
with \(G=0\) if any such type is never drawn. This factor is independent of the allocation \(a,b\) and of the two-type word. Multiplying (1) by \(G\) and averaging proves weak Schur-concavity. Because \(t\ge m\) and every target type has positive drawing weight, there is positive probability of a drawing pattern containing at least two pair draws and at least one draw of every other target type. On that event \(G>0\), so the increase is strict. The standard finite sequence of two-coordinate balancing transfers gives strict Schur-concavity and the unique equal-allocation maximizer.

**4. Stationarity.** Fix \(q\in(0,1)\) and extend the iid drawing sequence to all integer times. The post-loss presence of type \(i\) at time zero is determined by its most recent draw and the independent loss decisions since that draw. Each positive-weight type was drawn at a finite negative time almost surely, so this constructs the stationary distribution. The pair-conditioning argument carries over to the infinitely many positions \(\cdots<s_2<s_1\le0\) of draws from \(\{i,j\}\), indexed from newest to oldest. The terminal run \(K\) is almost surely finite for \(a,b>0\); put \(f(k)=q^{(-s_1+1)+(-s_{k+1}+1)}\), which strictly decreases to zero as \(k\to\infty\). Its expectation is
\[
\mathbb Ef(K)=f(1)-\sum_{k=2}^{\infty}\bigl(f(k-1)-f(k)\bigr)
\bigl(a^k+(1-a)^k\bigr).
\tag{2}
\]
This follows by truncation and bounded convergence. Every other target type has a finite latest draw almost surely and hence a strictly positive conditional survival factor. Thus the same two-coordinate balancing is strictly improving in stationarity. Irreducibility and aperiodicity on the finite state space for \(q\in(0,1)\) and positive weights imply uniqueness of this stationary law.

**5. A separately checkable stationary recurrence.** With \(s_B=\pi_w\{B\subseteq S\}\), \(s_\emptyset=1\), and \(W_B=\sum_{i\in B}w_i\), conditioning on the newest draw and independent survival gives, for each nonempty \(B\subseteq[n]\),
\[
s_B=\frac{q^{|B|}\sum_{i\in B}w_i s_{B\setminus\{i\}}}
{1-q^{|B|}(1-W_B)}.
\tag{3}
\]
For \(n=2\), (3) gives the displayed rational expression. Equation (3) provides an independent exact-arithmetic check of the stationary part of the theorem, but is not needed for the Schur-concavity proof.

## Verification

Run `python check.py` using Python's standard library. It independently computes finite-time subset-presence probabilities (i) by enumerating all drawing words and using last-selection survival products and (ii) by exact rational finite-state Markov updates. It checks two-coordinate balancing across different rational sampling vectors, target subsets, and time-dependent positive retention schedules. It also verifies the last-run power-sum law by direct enumeration and stationary subset moments from (3) against a separately solved full-state stationary linear system. The current package checker passes 1,188 exact assertions. These finite checks are reproducibility evidence; the universal assertions are proved in steps 1–5 above.

## Relationship to prior work

Cruciani and Dudeja introduce the post-draw loss model with **uniform draws** and examine metastability and completion-time scales [1]. Their analysis does not establish optimality over unequal sampling distributions at every finite observation time or under an arbitrary common loss schedule. Anceaume, Busnel, Schulte-Geers, and Sericola prove majorization optimality for **permanent** coupon collection, where types cannot be lost [2]. That no-loss result is recovered as the finite-time special case \(q_s=1\), but does not itself provide the erasure-dependent two-type identity (1) or the nontrivial stationary assertion.

Long analyzes stationary-entry fluxes for uniform-sampling clumsy/careless collectors and a separate single-reset model [3], and studies deterministic sliding-window expiration [4]. Stationary entry frequency, finite-time simultaneous presence under independently refreshed losses, and deterministic common expiration are distinct quantities and mechanisms. A published analysis of **nonuniform reset-button** collectors [5] proves a related Schur-concavity of reset-free *excursion success*, but its reset wipes the entire collection at once; it does not imply (1) for independent losses per present type.

## Limitations

The result is specific to independent **type-symmetric** loss probabilities at each time. It need not hold if different types have different retention probabilities: even in the two-type stationary model, selecting the less persistent type more frequently can improve coverage. The result is for a prescribed-time presence event and, in the stationary case, its equilibrium probability; it does not compare first hitting times or stationary entrance fluxes. The theorem provides no quantitative lower bound for the improvement under balancing that is uniform over all model parameters. Priority relative to general stochastic majorization results for dynamic caching and randomly expiring items remains a residual literature risk.

## References

1. E. Cruciani and A. Dudeja, *The Careless Coupon Collector's Problem*, arXiv:2602.20705, first posted 2026-02-24. https://arxiv.org/abs/2602.20705
2. E. Anceaume, Y. Busnel, E. Schulte-Geers and B. Sericola, *Optimization results for a generalized coupon collector problem*, arXiv:1504.03878 (2015); J. Appl. Prob. 53 (2016), 622–629. https://arxiv.org/abs/1504.03878
3. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511 (2026). https://arxiv.org/abs/2605.14511
4. C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298 (2026). https://arxiv.org/abs/2604.26298
5. *Balanced non-uniform reset coupon collectors: profile rates and heterogeneity penalties*, published research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-balanced-nonuniform-reset-coupon-rates--7b9ca5a2ebed
