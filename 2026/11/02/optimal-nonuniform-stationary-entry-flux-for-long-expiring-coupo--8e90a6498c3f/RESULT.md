# Optimal nonuniform stationary entry flux for long expiring-coupon windows

## Finding

Fix an integer \(n\ge 2\). Draw independent coupon labels \((X_t)_{t\in\mathbb Z}\) from \(\{1,\ldots,n\}\) with a probability vector \(p=(p_1,\ldots,p_n)\), where \(p_i\ge 0\) and \(\sum_i p_i=1\). A length-\(M\) window is *complete* when it contains every label. Write \(\mu_{n,M}(p)\) for its stationary *new-entry flux*, the probability that the preceding window is incomplete but the current one is complete, for \(M\ge n\).

For every integer \(k\ge1\), let \(c_k>0\) denote the unique solution of
\[
\frac1{c_k}-1+\frac{k-1}{e^{c_k}-1}=0,
\]
and put
\[
C_k=k c_k e^{-c_k}(1-e^{-c_k})^{k-1}.
\]
Then the sharp optimization law in the **fixed-alphabet, long-window regime** is
\[
\boxed{\lim_{M\to\infty}M\max_{p\in\Delta_{n-1}}\mu_{n,M}(p)=C_{n-1}.}
\]
The asymptotically optimal probability profiles are unique up to relabeling: a sequence \(p^{(M)}\) satisfies \(M\mu_{n,M}(p^{(M)})\to C_{n-1}\) **if and only if** the coordinates can be relabeled for each \(M\) so that
\[
\boxed{p_n^{(M)}\to1,\qquad M p_i^{(M)}\to c_{n-1}\quad(1\le i<n).}
\]
Thus one coupon becomes overwhelmingly common and the remaining \(n-1\) coupon types have equal, optimally tuned rare-arrival rates. The constants \(C_k\) increase strictly with \(k\), with \(C_1=e^{-1}\). For example, \(C_2=0.520690982698\ldots\), \(C_3=0.622813464691\ldots\). If the second limit \(k\to\infty\) is taken after the fixed-alphabet long-window limit, then \(C_k\sim (\log k)/e\).

For comparison, the uniform sampling law has \(\mu_{n,M}(1/n,\ldots,1/n)\sim(1-1/n)^M\) as \(M\to\infty\) with \(n\) fixed. Hence optimizing stationary entries changes the scale from exponential to inverse-window-length decay. This is not an assertion that biased sampling minimizes the first completion time from an initially empty collection.

## Assumptions and scope

All coupon draws are independent with a fixed sampling vector \(p\); there are \(n\ge2\) types, and each coupon remains active for exactly \(M\ge n\) draws. The stationary law is the two-sided i.i.d. construction; no mixing-time or rare-event approximation is required for the definition of \(\mu_{n,M}\). The asymptotic variable is \(M\to\infty\) with \(n\) fixed, and the optimization allows the sampling vector to vary with \(M\). The simplex \(\Delta_{n-1}\) includes its boundary (whose zero-probability components make the complete-window event impossible).

## Proof

**1. Exact nonuniform entrance formula.** The consecutive windows overlap in a block of \(M-1\) draws. A new entry occurs exactly when that common block omits a unique coupon type \(i\), contains each of the other \(n-1\) types, the appended label is \(i\), and the departing label is not \(i\). Independence of the departing, common, and appended coordinates gives
\[
\mu_{n,M}(p)=\sum_{i=1}^n p_i(1-p_i)\,\Pr_p\{N_i=0,\ N_j\ge1\ (j\ne i)\},
\tag{1}
\]
where \(N_j\) counts occurrences of label \(j\) in the common block. Inclusion--exclusion yields the fully finite expression
\[
\mu_{n,M}(p)=\sum_{i=1}^n p_i(1-p_i)
\sum_{A\subseteq[n]\setminus\{i\}}(-1)^{|A|}
\left(1-p_i-\sum_{j\in A}p_j\right)^{M-1}.
\tag{2}
\]
For each finite \(M\) this is a continuous function on the compact simplex, so its maximum exists.

**2. Compactification of every possible optimizer.** Consider any sequence \(M\to\infty\) and sampling vectors \(p^{(M)}\). Along a subsequence, each extended rare rate \(M p_i^{(M)}\) converges in \([0,\infty]\). At least one rate tends to infinity because the probabilities sum to one. Let \(I\) be the indices with finite limiting rate \(c_i\in[0,\infty)\), and let \(k=|I|\le n-1\).

If \(M p_i^{(M)}\to\infty\), its term in (1), after multiplication by \(M\), is bounded by
\[
M p_i^{(M)}(1-p_i^{(M)})^M
\le (M p_i^{(M)})e^{-M p_i^{(M)}}\to0.
\]
(The stronger factor \(1-p_i\) in (1) is essential if \(p_i\) itself approaches one.) For \(i\in I\), the vector of common-block counts \((N_j)_{j\in I}\) converges jointly to independent Poisson variables with means \((c_j)_{j\in I}\), while every index outside \(I\) is represented in the common block with probability tending to one, by a union bound. Thus (1) gives the subsequential limit
\[
M\mu_{n,M}(p^{(M)})\longrightarrow
G_k(c_1,\ldots,c_k):=\sum_{i=1}^k c_i e^{-c_i}
\prod_{j\ne i}(1-e^{-c_j}),
\tag{3}
\]
with the convention \(G_0=0\). Equation (3) remains valid when some \(c_i=0\).

**3. Sharp and unique finite-dimensional Poisson maximum.** For \(k\ge1\), the function \(G_k\) continuously extends to the compactified cube \([0,\infty]^k\): at a zero coordinate it vanishes; at an infinite coordinate it reduces to \(G_{k-1}\) of the remaining coordinates. Let \(D_k=\max G_k\) over this cube and let \(D_0=0\). Choosing the first \(k-1\) coordinates at a positive maximizer and adding a sufficiently large finite last coordinate \(x\) increases the value, because
\[
G_k(c_1,\ldots,c_{k-1},x)
=G_{k-1}(c_1,\ldots,c_{k-1})
+e^{-x}\left[x\prod_{j<k}(1-e^{-c_j})-G_{k-1}(c_1,\ldots,c_{k-1})\right].
\]
Consequently \(D_k>D_{k-1}\), so every maximizer of \(G_k\) is interior. For positive coordinates set
\[
F=\prod_{i=1}^k(1-e^{-c_i}),\qquad
H=\sum_{i=1}^k\frac{c_i}{e^{c_i}-1};
\quad G_k=FH.
\]
Differentiating shows
\[
\frac{\partial G_k}{\partial c_i}
=\frac{F}{e^{c_i}-1}
\left(1+H-\frac{c_i}{1-e^{-c_i}}\right).
\tag{4}
\]
At an interior critical point, each \(c_i/(1-e^{-c_i})\) is the same. This is a strictly increasing function of \(c_i>0\), since its derivative has numerator \(1-(1+c_i)e^{-c_i}>0\). Hence all coordinates of every maximizer coincide.

On the diagonal,
\[
G_k(c,\ldots,c)=k c e^{-c}(1-e^{-c})^{k-1},
\]
whose logarithmic derivative is \(1/c-1+(k-1)/(e^c-1)\). This derivative is strictly decreasing from positive infinity to \(-1\), hence has exactly one zero \(c_k\). Therefore \(D_k=C_k\), with a unique maximizer \((c_k,\ldots,c_k)\), and \(C_k>C_{k-1}\).

**4. Sharpness and rigidity.** Equation (3), with \(k\le n-1\), bounds every subsequential limit by \(C_{n-1}\). Conversely choose
\[
p_1=\cdots=p_{n-1}=\frac{c_{n-1}}M,
\qquad p_n=1-\frac{(n-1)c_{n-1}}M
\]
for all sufficiently large \(M\). Then (3) converges to \(C_{n-1}\), giving equality in the sharp limit. If a sequence asymptotically attains \(C_{n-1}\), every extended-rate subsequential limit must have exactly \(n-1\) finite coordinates, all equal to \(c_{n-1}\), because the maxima \(C_k\) are strictly increasing and unique. Compactness then proves the stated asymptotic characterization up to permutation. The converse follows directly from (3).

**5. Secondary asymptotics.** For the uniform law, the exact formula in Long's theorem gives
\[
\mu_{n,M}=\frac{(n-1)(n-1)!S(M-1,n-1)}{n^M}
\sim \left(1-\frac1n\right)^M
\]
for fixed \(n\), using the classical fixed-alphabet surjection count. At the diagonal optimum the critical equation also gives \(e^{c_k}=(k c_k-1)/(c_k-1)\) for \(k\ge2\); from this \(c_k\sim\log k\), \(k e^{-c_k}\to1\) and \((1-e^{-c_k})^{k-1}\to e^{-1}\), proving \(C_k\sim(\log k)/e\).

## Verification

Run the standalone standard-library script `check.py` with `python check.py`. It compares the independent length-\(M+1\) event enumeration against (2) using exact rational probabilities for several two- and three-type cases, checks the two-type closed form over numerous parameter pairs, tests diagonal criticality and sampled inequalities, and evaluates constructed near-optimal profiles over multiple window lengths. The recorded execution passed **2378 checks**. For \(n=2,3,4,5\), the leading constants are approximately \(0.367879441171\), \(0.520690982698\), \(0.622813464691\), and \(0.700316244893\), respectively.

These numerical and finite exact tests check the formulas in representative cases only; they do not prove the global asymptotic theorem. The analytical compactification and optimization arguments above supply the proof for every fixed integer \(n\ge2\).

## Relationship to prior work

Christopher D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws* (arXiv:2604.26298v1, first public 2026-04-29), establishes the uniform-sampling stationary entry flux and rare-event results when the number of types grows. The event decomposition underlying (1) is already present in its Theorem 3.1 and is not claimed as new. This note instead optimizes the **nonuniform** flux, with fixed number of types and an unbounded retention window, and proves the unique asymptotically optimal, strongly asymmetric sampling profile. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors* (arXiv:2605.14511v1), concerns different refresh/loss mechanisms rather than the fixed-length sliding-window optimization. General nonuniform coupon collecting and optimization of deadline-constrained collectors are related but do not alone give the particular stationary-flux optimum.

## Limitations

The maximizing vector is classified to leading order only; there is no claim of a unique finite-\(M\) optimizer or a uniform result when the alphabet size grows simultaneously with \(M\). The result concerns the stationary frequency of **new transitions into** complete windows, not the stationary fraction of complete windows, the first completion time from an empty start, or a rare-event exponential hitting law under optimized sampling. The historical-priority assessment is not an independent exhaustive literature certification.

## References

1. C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1 (2026-04-29), https://arxiv.org/abs/2604.26298.
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1 (2026-05-14), https://arxiv.org/abs/2605.14511.
3. R. May, *Coupon Collecting with Quotas*, Electronic Journal of Combinatorics 15 (2008), N31, https://doi.org/10.37236/906. Background on nonuniform coupon completion; different event and regime.
4. I. Kleiner, *The Fragile Coupon Collector: Random Deadlines, Critical Fragility, and Optimal Sampling*, Mathematics 14 (2026), 3729, https://doi.org/10.3390/math14203729. Related optimal-sampling question with permanently safe observed types rather than expiring windows.
