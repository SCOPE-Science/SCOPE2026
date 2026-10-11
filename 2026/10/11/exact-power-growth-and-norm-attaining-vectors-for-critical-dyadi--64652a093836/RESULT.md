# Exact power growth and norm-attaining vectors for critical dyadic backward shifts

## Finding
For every real exponent \(1\le p<\infty\), the positive weighted backward shift on the complex dyadic \(c_0\)-sum defined below has the following **entire** power-norm profile, for every integer \(n\ge1\):

\[
\|T_p^n\|^p=
\begin{cases}
17/6,&n=1,\\
37/6,&n=5,\\
n+1,&n\ge2,\ n\ne5.
\end{cases}
\]

In particular, the exact best uniform multiplier in the published power-growth lower bound is
\[
\sup_{n\ge1}\frac{\|T_p^n\|}{(n+1)^{1/p}}=(17/12)^{1/p},
\]
with equality in this normalized upper estimate exactly at \(n=1\). The ordinary lower bound \(\|T_p^n\|\ge(n+1)^{1/p}\) is an equality at every power except \(n=1\) and \(n=5\).

The complete norm-attaining unit-vector criterion is also explicit: for \(n\ge2\) with \(n\ne5\), a unit vector \(x\) attains \(\|T_p^n\|\) if and only if \(|x_{n+1}|=1\); for \(n\in\{1,5\}\), a unit vector attains the norm if and only if \(|x_{n+2}|=|x_{n+3}|=1\). The remaining coordinates may be chosen arbitrarily subject to the defining norm-one and \(c_0\)-tail constraints. The special coordinates in the exceptional case lie in distinct dyadic source blocks.

## Assumptions and scope
Fix \(1\le p<\infty\) and use complex scalars. For \(j\in\mathbb N_0\), set
\[
I_j=\{2^j,\ldots,2^{j+1}-1\},\qquad
X_p=\left(\bigoplus_{j\ge0}\ell_p(I_j;\mathbb C)\right)_{c_0}.
\]
Thus \(x=(x_m)_{m\ge1}\) belongs to \(X_p\) when its dyadic block norms tend to zero, and
\[
\|x\|_{X_p}=\sup_{j\ge0}\left(\sum_{m\in I_j}|x_m|^p\right)^{1/p}.
\]
Define the bounded positive backward shift
\[
(T_px)_m=\left(\frac{m+1}{m}\right)^{1/p}x_{m+1}\quad(m\ge1).
\]
The scalar exponents are real; the statements concern the same natural family of operators as Theorem 1.4 of Li and Li [1], not arbitrary weighted shifts or other block decompositions.

## Proof
**Telescoping and a block optimization lemma.** For every integer \(n\ge1\),
\[
(T_p^nx)_m=\left(\frac{m+n}{m}\right)^{1/p}x_{m+n}.
\]
Consequently, for an output block \(I_j=[a,2a)\cap\mathbb N\), with \(a=2^j\), its \(p\)-th power contribution is
\[
Q_{n,a}(x)=\sum_{m=a}^{2a-1}\left(1+\frac nm\right)|x_{m+n}|^p.
\]
The shifted interval \([a+n,2a+n)\) intersects at most two dyadic source blocks: it has length \(a\), and each dyadic block beginning at or after \(a\) has length at least \(a\). Each source block independently has \(p\)-th power budget at most one for a unit vector. In a given source block this budget is used optimally at its *smallest* available output index, because \(1+n/m\) decreases strictly with \(m\). Hence the maximum of \(Q_{n,a}\) on the unit ball equals the sum of one maximal coefficient for each intersected source block; it is attained by one coordinate of modulus one in each source block. Since the norm on the outer direct sum is the supremum of the output block norms, the operator norm is the supremum of these exact block maxima.

**The singleton output block.** For \(a=1\), the block consists only of output index \(m=1\). Its maximum is precisely \(n+1\), attained by \(|x_{n+1}|=1\).

**All blocks with \(a\ge4\).** If the shifted interval meets one source block, its maximum is at most \(1+n/a\), strictly smaller than \(n+1\) for \(n\ge1\). If it meets two source blocks, the first available output indices lie at least at \(a\) and \(a+1\), respectively. The maximum is thus at most
\[
2+n\left(\frac1a+\frac1{a+1}\right)\le2+\frac{9n}{20}.
\]
For \(n\ge2\), this is strictly less than \(n+1\), because \(2+9n/20<n+1\) for all integer \(n\ge2\). For \(n=1\), it is at most \(49/20<17/6\). Thus none of these blocks can tie the eventual winning block.

**The two-coordinate output block.** For \(a=2\), the output indices are \(m=2,3\); their source indices are \(n+2,n+3\). If these indices belong to the same dyadic source block, the block maximum is \(1+n/2<n+1\). If they belong to distinct dyadic blocks, then necessarily \(n+3\) is a power of two, and independent source budgets give the exact block maximum
\[
\left(1+\frac n2\right)+\left(1+\frac n3\right)=2+\frac{5n}{6}.
\]
The first two admissible positive powers are \(n=1\) and \(n=5\), yielding \(17/6\) and \(37/6\), respectively. Every later such power satisfies \(n\ge13\), for which \(2+5n/6<n+1\). Every other power has only one source block, so cannot beat \(n+1\). This exhausts all output blocks and proves the displayed profile, including the fact that the winning output block is unique: it is \(I_1\) for \(n=1,5\), and \(I_0\) for all other positive powers.

**All norm-attaining unit vectors.** Because the outer \(c_0\) structure makes each output block norm tend to zero, its supremum is achieved. The strict separation of the winning block from every other block means equality in the operator norm is equivalent to equality in its block-budget calculation. For the singleton block this is \(|x_{n+1}|=1\). In the two exceptional two-source blocks the two weights are strictly positive and each contributing coordinate lies in a separate source block, so both source budgets must saturate, exactly when \(|x_{n+2}|=|x_{n+3}|=1\). These conditions are sufficient as well, with all other coordinates constrained only by membership in the unit sphere. Finally, dividing the exact power profile by \(n+1\) gives ratios \(17/12\) at \(n=1\), \(37/36\) at \(n=5\), and \(1\) elsewhere; hence the stated sharp uniform multiplier and its unique maximizing positive power. \(\square\)

## Verification
A standalone standard-library checker is provided as `verify_dyadic_powers.py`. It computes the exact rational optimum of each output dyadic block using one budget per intersected source block, and compares the resulting maxima against the theorem for positive powers through \(n=500\) and output blocks through \(j=20\). It also checks the rational inequalities used in the global proof for finite sample powers. The universal assertions follow from the preceding analytic argument, **not** from finite enumeration. The checker needs Python 3 and has no third-party dependencies.

## Relationship to prior work
Li and Li [1], Theorem 1.4(i), introduce exactly this family and establish the two-sided estimate \((n+1)^{1/p}\le\|T_p^n\|\le2^{1/p}(n+1)^{1/p}\), as part of a sharp-order mean-L-stable power-growth construction. Their proof in Section 5 shows that each shifted dyadic output interval meets at most two source blocks, but does not evaluate their optimal weighted contributions or the exact power-by-power norm. Those definitions, the telescoping identity, the block-overlap observation, and the relation between the exponents are prior inputs. The present contribution is the **exact full power profile**, its exceptional-power classification, the sharp best upper multiplier, and every norm-attaining unit vector.

The general existence statement about prescribed power-norm profiles for irreducible weighted shifts in [2] concerns a different operator model and does not determine the norms of this fixed dyadic \(c_0\)-sum operator. Standard \(\ell_p\)-space backward shifts do not have the same independent source-block budgets and are not interchangeable here.

## Limitations
The classification is specific to the critical weights, dyadic partition, and outer \(c_0\)-sum above. Nothing is claimed for arbitrary weighting sequences, alternative partitions, or a full norm profile on arbitrary \(p\)-convex lattices. There has been no independent audit. Generic weighted-shift and block-matrix optimization techniques could yield equivalent statements in older, unindexed literature; unsuccessful search alone is not a proof of priority.

## References
[1] Jian Li and Jie Li, *Power growth of mean-L-stable operators on Banach spaces*, arXiv:2608.09694v1 (first public 2026-08-10 UTC); version 2, 2026-08-17. Theorem 1.4 and Section 5. https://arxiv.org/abs/2608.09694

[2] *Exact norm and essential-norm power profiles for irreducible weighted shifts*, published published-finding corpus record 2026/9/20/SCOPE-irreducible-weighted-shift-essential-power-profiles--d5ae263f185c. https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-irreducible-weighted-shift-essential-power-profiles--d5ae263f185c
