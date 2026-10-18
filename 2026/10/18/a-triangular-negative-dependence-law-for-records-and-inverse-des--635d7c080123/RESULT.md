# A triangular negative-dependence law for records and inverse descents

## Finding
Let \(\pi=(\pi_1,\ldots,\pi_n)\) be uniformly distributed over the permutations of \(\{1,\ldots,n\}\), with integer \(n\ge2\). Set
\[
R_i=\mathbf 1\{\pi_i=\max(\pi_1,\ldots,\pi_i)\},\quad 1\le i\le n,
\]
and let \(J_j=\mathbf 1\{\pi^{-1}(j)>\pi^{-1}(j+1)\}\) be the inverse-descent indicator at *value rank* \(j\), for \(1\le j<n\). Then
\[
\boxed{\operatorname{Cov}(R_i,J_j)=
\begin{cases}
-\dfrac{i-1}{2n(n-1)}\dfrac{\binom{j-1}{i-2}}{\binom{n-2}{i-2}},&2\le i\le j+1,\\[5pt]
0,&\text{otherwise}.
\end{cases}}
\]
In particular the \((n-1)\)-square cross-covariance matrix with rows \(R_2,\ldots,R_n\) and columns \(J_1,\ldots,J_{n-1}\) is upper triangular with strictly negative diagonal, hence has full rank. Its zero pattern is exact, not asymptotic.

More strongly, write \(\mathbf R=(R_1,\ldots,R_n)\). For every fixed \(j\), the two conditional distributions \(\mathcal L(\mathbf R\mid J_j=0)\) and \(\mathcal L(\mathbf R\mid J_j=1)\) have a coupling \((\mathbf R^+,\mathbf R^-)\) satisfying \(\mathbf R^+\ge\mathbf R^-\) coordinatewise almost surely. They differ, when they differ at all, in precisely one record coordinate, and
\[
\Pr\{\mathbf R^+\ne\mathbf R^-\}=\frac{2}{(n-j+1)(n-j)}.
\]
Thus every coordinatewise nondecreasing function \(f:\{0,1\}^n\to\mathbb R\) satisfies
\[
\mathbb E[f(\mathbf R)\mid J_j=0]\ge\mathbb E[f(\mathbf R)\mid J_j=1].
\]
This is stochastic domination of a complete vector of record indicators, not just a covariance-sign statement.

Writing \(K_n=\sum_{i=1}^nR_i\), summing the kernel yields
\[
\operatorname{Cov}(K_n,J_j)=-\frac1{2(n-j)(n-j+1)},
\qquad
\operatorname{Cov}\bigl(K_n,\sum_{j=1}^{n-1}J_j\bigr)=-\frac{n-1}{2n}.
\]
For any fixed integer \(k\ge1\) and \(n>k\), the top \(k\) value-rank inverse descents contribute exactly \(-k/[2(k+1)]\) to the latter covariance. This makes the boundary localization quantitative. The *aggregate* covariance identity is not claimed new: it agrees with earlier results about global Euler–Stirling statistics and with a previously established record–position-descent covariance. The new contribution here is the exact value-by-position triangular kernel and the simultaneous monotone coupling.

## Assumptions and scope
The permutation is exactly uniform, and \(n\) is any integer at least two. Records are **strict left-to-right upper records** in the ordinary one-line representation; inverse descents compare the *positions* of the **consecutive values** \(j,j+1\), not adjacent positions of the permutation word. Boundary indicator \(R_1\) is identically one; there is no \(J_n\). The binomial ratio is only used when \(2\le i\le j+1\), so both binomial coefficients are defined and the denominator is positive. No independence of different inverse-descent indicators is assumed.

## Proof
Fix \(j\) and write \(m=n-j+1\), the number of values in \(H=\{j,j+1,\ldots,n\}\). The events \(J_j=0\) and \(J_j=1\) have probability one half each, because transposing the **values** \(j\) and \(j+1\) is a measure-preserving bijection between them. Sample a uniform \(\pi^+\) conditional on \(J_j=0\), and obtain \(\pi^-\) by this value transposition. It has the conditional law given \(J_j=1\).

Only the record status at the two positions occupied by \(j,j+1\) can change: prior and subsequent running maxima are unaffected by exchanging adjacent values. Since \(j\) appears first in \(\pi^+\), its position has the same record status before and after the swap. The later position, occupied by \(j+1\), is a record in \(\pi^+\) and not in \(\pi^-\) precisely if the first two values from \(H\) encountered in the word are, in order, \(j,j+1\). Call this event \(E\). Outside \(E\) the two complete record vectors are identical. On \(E\) there is exactly one lost record indicator, at the position \(T_2\) of the second occurrence of a member of \(H\). This establishes the coordinatewise coupling and its one-coordinate structure.

Conditional on \(J_j=0\), the order of the \(m\) members of \(H\) is uniformly distributed among the \(m!/2\) orders with \(j\) before \(j+1\). Exactly \((m-2)!\) of these begin with \(j,j+1\), so
\[
\Pr(E\mid J_j=0)=\frac{2}{m(m-1)}.
\]
The \(m\) positions occupied by members of \(H\) form an independent uniform \(m\)-subset of \(\{1,\ldots,n\}\). Thus, for \(2\le i\le n-m+2=j+1\),
\[
\Pr(T_2=i)=\frac{(i-1)\binom{n-i}{m-2}}{\binom nm},
\]
and this probability vanishes outside the stated range. Membership positions are independent of the relative order of the labels in \(H\), including the condition \(J_j=0\) and the event \(E\).

For any Bernoulli variable \(J\) with \(\Pr(J=1)=1/2\),
\[
\operatorname{Cov}(X,J)=\frac14\bigl(\mathbb E[X\mid J=1]-\mathbb E[X\mid J=0]\bigr).
\]
Applying this to each record coordinate and the coupling gives
\[
\operatorname{Cov}(R_i,J_j)
=-\frac{1}{2m(m-1)}\Pr(T_2=i)
=-\frac{i-1}{2n(n-1)}
\frac{\binom{j-1}{i-2}}{\binom{n-2}{i-2}},
\]
where the last equality follows by expanding the factorials in the two binomial ratios. The zero cases and strictly negative nonzero cases follow at once.

The matrix row indexed by \(i\in\{2,\ldots,n\}\) has zeros when \(j<i-1\). Its diagonal, at \(i=j+1\), equals \(-j/[2n(n-1)\binom{n-2}{j-1}]\), which is strictly negative; therefore its determinant is nonzero. Summing over all \(i\) uses \(\sum_i\Pr(T_2=i)=1\) and yields the exact rankwise total covariance. Finally, changing variables \(h=n-j\) gives
\[
\sum_{j=n-k}^{n-1}\operatorname{Cov}(K_n,J_j)
=-\frac12\sum_{h=1}^{k}\frac1{h(h+1)}
=-\frac{k}{2(k+1)}.
\]
All formulas include \(n=2\), where the only nonconstant record indicator and only inverse-descent indicator are perfectly anticorrelated.

## Verification
The standalone standard-library program `verify.py` exhaustively enumerates every permutation for each \(2\le n\le8\), computes all \(168\) individual covariance entries exactly as rational numbers, and compares them with the displayed formula. It also checks the value-swap coupling coordinatewise on every eligible permutation; a strict difference is verified to occur at exactly the predicted second-high-value position, and tests the column sums and aggregate telescoping identity. Run with `python3 verify.py`. The computation is finite corroboration; the proof above establishes the universal assertions independently of enumeration.

## Relationship to prior work
Gnedin and Gorin (arXiv:1202.3680, first posted 2012-02-16) study record-based probability laws on permutations; the uniform model is their basic reference distribution, but their record-dependent measures and boundary theory do not present this position-by-value inverse-descent covariance or pair-swap ordering. Baril and Vajnovszki (arXiv:1606.07913; freely available author manuscript, final version 2017) establish a broad **set-valued equidistribution** involving the record-position set and inverse-descent set. This is the closest earlier umbrella: it encodes related joint distributions by bijection, and makes exact-identity priority a real residual risk. Its displayed theorem gives no explicit conditional coordinatewise monotone swap coupling, triangular covariance entries, or boundary mass law. Jin (arXiv:2210.08789, 2022) gives generating functions for **numbers** of left-to-right maxima and inverse descents; these cover global count-level information but do not resolve the position-by-value kernel or vectorwise coupling directly. Earlier position-descent covariance formulas are genuinely different: their descent index refers to neighboring *positions*, not neighboring *values*. The aggregate covariance stated above has known coverage and is supplied only as a consistency check.

## Limitations
The result concerns exactly uniform permutations; no Mallows-parameter or other nonuniform extension is asserted. Stochastic domination is coordinatewise for the conditional record *vectors*, but no negative-association theorem for all inverse-descent indicators jointly is claimed. The provided coupling does **not** prove an exact total-variation distance between the conditional record-vector laws. A previous set-valued equidistribution provides broad related information, so an equivalent previously implicit derivation remains possible. Novelty and correctness have been assessed within the supplied proof and comparison, without independent scientific audit. Finite enumeration alone is not used to infer the all-size result.

## References
1. A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, arXiv:1202.3680 (first public posting 2012-02-16); Random Structures & Algorithms 46 (2015), 688–706. https://arxiv.org/abs/1202.3680
2. J.-L. Baril and V. Vajnovszki, *A permutation code preserving a double Eulerian bistatistic*, arXiv:1606.07913 (2016); Discrete Applied Mathematics 224 (2017), 9–15. https://jl.baril.u-bourgogne.fr/code.pdf
3. E. Y. Jin, *Symmetric generating functions and Euler–Stirling statistics on permutations*, arXiv:2210.08789 (2022); Journal of Combinatorial Theory, Series A 197 (2023), 105752. https://arxiv.org/abs/2210.08789
