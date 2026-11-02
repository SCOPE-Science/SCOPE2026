# Exact critical thinning phase for matroid-rank quantile shares

## Finding

Fix an integer \(n\ge2\). Independently include each good of a finite set \(G\) in a random benchmark bundle \(X_p\) with probability \(p\in(0,1)\). A bundle \(S\) is **\(q\)-quantile fair** to a valuation \(v\) when
\[
\Pr\bigl(v(X_p)\le v(S)\bigr)\ge q.
\]
For the class of all \(n\)-agent profiles of matroid-rank valuations, on arbitrary finite ground sets, the **largest uniformly feasible** quantile level is exactly
\[
\boxed{Q_n(p)=\begin{cases}
(1-p)^{n-1},&0<p\le 1/n,\\
0,&1/n<p<1.
\end{cases}}
\]
For \(0<p<1/n\), the auxiliary binomial tails \(F_t(p)=\Pr\{\operatorname{Bin}(nt-1,p)\le t-1\}\) strictly increase in the integer \(t\ge1\); they are nondecreasing at \(p=1/n\), with strict increase if \(n\ge3\), and are constant at \(n=2,p=1/2\). Above \(p=1/n\), these tails approach zero. In the thinning parameterization \(p=c/n\), the exact phase boundary is \(c=1\).

## Assumptions and scope

There are \(n\ge2\) agents and \(m\ge0\) indivisible goods. Each valuation \(v_i:2^G\to\mathbb Z_{\ge0}\) is the rank function of a finite matroid on \(G\). Different agents may have different matroids. A deterministic allocation is a partition \((S_1,\ldots,S_n)\) of \(G\), including empty bundles. The random bundle \(X_p\) is used only to define the individual fairness benchmark and need not coincide with any component of an actual random allocation. For each fixed \((n,p)\), \(Q_n(p)\) is the supremum of all \(q\in[0,1]\) such that every profile with any number of goods has an allocation simultaneously satisfying all agents' \(q\)-quantile tests.

## Proof

**Step 1: a binomial monotonicity lemma.** Fix \(n\ge2\), \(0<p\le1/n\), and integer \(t\ge1\). Let \(Z_t\sim\operatorname{Bin}(nt-1,p)\), \(Y\sim\operatorname{Bin}(n,p)\) independent, and set \(a_j=\Pr(Z_t=j)\), with \(a_j=0\) outside the support. By convolution, \(Z_t+Y\sim\operatorname{Bin}(n(t+1)-1,p)\). Comparing the two left tails gives the exact identity
\[
F_{t+1}(p)-F_t(p)
=a_t\Pr(Y=0)-\sum_{j=2}^n\Pr(Y=j)\sum_{h=1}^{j-1}a_{t-h}.
\tag{1}
\]
For every \(1\le k\le t\) in the support, the binomial adjacent-mass ratio obeys
\[
\frac{a_{k-1}}{a_k}=\frac{k(1-p)}{(nt-k)p}
\le\frac{1-p}{p(n-1)}=:r.
\]
Consequently \(a_{t-h}\le a_t r^h\), also when \(t-h<0\). Put \(z=p/(1-p)\), so \(r=1/((n-1)z)\). Substituting the bound into (1) yields
\[
F_{t+1}-F_t\ge a_t(1-p)^n\bigl(1-H_n(z)\bigr),\quad
H_n(z)=\sum_{j=2}^n\binom nj\sum_{h=1}^{j-1}\frac{z^{j-h}}{(n-1)^h}.
\tag{2}
\]
Every coefficient of this polynomial is nonnegative, and at least one is positive. Since \(p\le1/n\) is equivalent to \(z\le1/(n-1)\), it remains to calculate
\[
H_n\!\left(\frac1{n-1}\right)
=\sum_{j=2}^n\binom nj\frac{j-1}{(n-1)^j}
=1.
\tag{3}
\]
The last equality follows from
\[
\sum_{j=2}^n\binom nj(j-1)u^j
=(1+u)^{n-1}((n-1)u-1)+1
\]
at \(u=1/(n-1)\). Thus \(F_{t+1}\ge F_t\), strictly if \(p<1/n\). At \(p=1/n\), the adjacent modes of \(Z_t\) are \(t-1,t\); if \(n\ge3\), the term with \(Y=3\) and \(a_{t-2}<a_t\) makes (1) strictly positive, whereas for \(n=2\) symmetry gives equality. In every case
\[
\inf_{t\ge1}F_t(p)=F_1(p)=(1-p)^{n-1}.
\tag{4}
\]

**Step 2: rank-maximin shares satisfy the benchmark.** Fix one agent's matroid-rank valuation \(v\), and let \(k\) be its maximin share over \(n\) bundles. Truncate \(v\) at rank \(k+1\), writing \(\bar v(T)=\min\{v(T),k+1\}\). The matroid intersection construction in Babichenko--Feldman--Holzman--Narayan (2023, proof of Proposition 6; 2024, proof of Proposition 8) uses the direct sum of \(n\) copies of the truncated matroid and the partition matroid forbidding two uses of one good. Since \(n\) disjoint sets of truncated rank \(k+1\) would contradict the definition of \(k\), Edmonds' intersection formula provides subsets \(A_1,\ldots,A_n\subseteq G\) such that
\[
\sum_{i=1}^n\bar v(A_i)+\left|G\setminus\bigcap_i A_i\right|\le n(k+1)-1.
\]
Set \(A_0=\bigcap_i A_i\). Monotonicity of the rank function implies
\[
n\bar v(A_0)+m-|A_0|\le n(k+1)-1.
\]
In particular \(v(A_0)=\bar v(A_0)\le k\). Put \(t=k+1-v(A_0)\ge1\); then \(m-|A_0|\le nt-1\). For any \(X\subseteq G\), rank subadditivity and unit marginal increments give
\[
v(X)\le v(A_0)+|X\setminus A_0|.
\]
For the independent \(p\)-Bernoulli benchmark, the last count is binomial with \(m-|A_0|\) trials. Using monotonicity in the trial count and (4),
\[
\Pr\{v(X_p)\le k\}
\ge\Pr\{\operatorname{Bin}(nt-1,p)\le t-1\}
\ge(1-p)^{n-1}.
\]
Barman--Verma (2020/2021, Theorem 1) prove that every matroid-rank profile admits a single allocation giving each agent at least her maximin share. Apply the preceding estimate separately to every agent: this allocation is simultaneously \((1-p)^{n-1}\)-quantile fair, proving feasibility when \(p\le1/n\).

**Step 3: sharpness, and loss of any positive uniform guarantee above the boundary.** For \(0<p\le1/n\), take \(m=n-1\) goods and give every agent the uniform rank-one matroid. In any allocation at least one agent receives no goods. That agent's benchmark has value zero with probability exactly \((1-p)^{n-1}\); hence every larger \(q\) fails.

For \(p>1/n\), take any integer \(t\ge1\), let \(m=nt-1\), and give every agent the uniform rank-\(t\) matroid. Some agent gets at most \(t-1\) goods in every allocation and hence satisfies her quantile test with probability at most \(F_t(p)\). As \(t\to\infty\), the binomial count divided by \(t\) converges in probability to \(np>1\), because its mean divided by \(t\) tends to \(np\) and its variance divided by \(t^2\) tends to zero. Thus \(F_t(p)\to0\), so every fixed \(q>0\) fails for a sufficiently large uniform-rank instance. This proves the second branch and completes the claim.

## Verification

The standalone `verify_binomial.py` uses exact rational arithmetic. It verifies 3,068 binomial-tail identities, monotonicity comparisons, sharp-bound polynomial identities and strictness conditions on a finite parameter grid; it also exhaustively checks fair allocations in 1,560 small uniform-rank profiles. Execute `python verify_binomial.py` with Python 3. No floating-point calculation is needed. These finite checks are corroboration, not a substitute for the all-parameter proof above.

## Relationship to prior work

Babichenko, Feldman, Holzman and Narayan (first publicly posted December 4, 2023) introduce the quantile-share benchmark, establish the matroid-intersection and maximin-share reduction, and expressly conjecture the exact boundary value at \(p=1/n\) in their Remark 2 (Remark 3 in the July 2024 revision). Barman and Verma supply the preexisting maximin-share existence theorem. Fokkink, Papavassiliou and Pelekis (2022) prove a general mode-based tail comparison subsuming related critical-mean comparisons; the present claim does not assert priority over that comparison. The additional contribution is a full sharp **subcritical-to-supercritical Bernoulli parameter phase diagram for matroid-rank fairness**, including exact finite-population levels and universal impossibility beyond \(p=1/n\). Jain, Mizgerd and Ravichandran (May 2026) introduce the \(p=c/n\) thinning parameter and prove a different universal-feasibility result for unrestricted monotone valuations; they do not give this finite-\(n\) matroid-rank phase diagram in the inspected theorem and applications.

## Limitations

The positive guarantee requires matroid-rank valuations; it is not a claim about all monotone or weighted-rank valuations. For \(p>1/n\), the independent-Bernoulli benchmark is a mathematical comparator, not the marginal bundle of a uniform random \(n\)-way partition. The zero upper bound is uniform over arbitrarily many goods: individual bounded-size instances may admit positive levels. All originality comparisons are best-knowledge statements subject to possible unindexed prior work. No independent external audit has been performed.

## References

1. Y. Babichenko, M. Feldman, R. Holzman, V. V. Narayan, *Fair Division via Quantile Shares*, arXiv:2312.01874 (first posted 2023-12-04), especially Section 4.3, Proposition 6 and Remark 2; revised journal manuscript dated 2024-07-31, Section 4.3, Proposition 8 and Remark 3. https://arxiv.org/abs/2312.01874 ; https://holzman.technion.ac.il/files/2024/07/quantile_shares_journal.pdf
2. S. Barman and P. Verma, *Existence and Computation of Maximin Fair Allocations Under Matroid-Rank Valuations*, arXiv:2012.12710, Theorem 1. https://arxiv.org/abs/2012.12710
3. R. Fokkink, S. Papavassiliou, C. Pelekis, *On the Monotonicity of Tail Probabilities*, Probability and Mathematical Statistics 42(1), 133--141 (2022), Theorem 1.1 and Equation (1.2). https://doi.org/10.37190/0208-4147.00050
4. V. Jain, C. Mizgerd, S. Ravichandran, *Thinned Quantile Shares are Universally Feasible*, arXiv:2605.04300 (first posted 2026-05-05), Definitions 1.2--1.3 and Theorems 1.5--1.7. https://arxiv.org/abs/2605.04300
