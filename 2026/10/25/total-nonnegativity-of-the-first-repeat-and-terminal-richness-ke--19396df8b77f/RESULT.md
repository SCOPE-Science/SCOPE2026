# Total nonnegativity of the first-repeat and terminal-richness kernel

## Finding
Fix integers \(n\ge2\) and \(m\ge n\). Sample \(X_1,\ldots,X_n\) independently and uniformly from \(\{1,\ldots,m\}\). Let \(K\) be the number of distinct values sampled, and let \(T\) be the first repeated-value index, with \(T=n+1\) if there is no repeat. The joint counting kernel indexed by \(2\le t\le n+1\) and \(1\le k\le n\),
\[
H_n(t,k)=\frac{m^n\Pr(T=t,K=k)}{(m)_k},
\]
is independent of \(m\) and is **totally nonnegative**: every square minor, in increasing row and column order, is nonnegative. Here \((m)_k=m(m-1)\cdots(m-k+1)\).

For \(2\le t\le n\), \(H_n(t,k)=(t-1)S_{t-1}(n-1,k)\), where \(S_r(N,k)\) counts set partitions of \(\{1,\ldots,N\}\) into \(k\) blocks with the first \(r\) labels all in separate blocks. The last row satisfies \(H_n(n+1,k)=\mathbf1_{\{k=n\}}\).

Consequently the conditional law of \(T\) given \(K=k\) is monotone in the **likelihood-ratio order** as \(k\) increases, and hence in first-order stochastic order. The conditional laws admit a simultaneous increasing quantile coupling. These statements apply unchanged when the sample alphabet has any size \(m\ge n\); no claim of independence between \(T\) and \(K\) is made.

## Assumptions and scope
All \(n,m,k,t\) are integers in the ranges above. The samples are iid with equal category probabilities. The total-nonnegativity statement includes minors containing zeros and does not assert strict positivity of all minors. Conditional distributions refer only to positive-probability values \(1\le k\le n\).

## Proof
**Equality partitions.** Each word induces a set partition of \(\{1,\ldots,n\}\) by equality of its coordinates. Each partition into \(k\) blocks admits exactly \((m)_k\) distinct assignments of category labels; hence conditioning on \(K=k\) makes the equality partition uniform among \(S(n,k)\) set partitions, independent of \(m\). To force \(T=t\le n\), the first \(t-1\) elements must belong to distinct blocks and element \(t\) must join exactly one of these \(t-1\) blocks. Delete element \(t\), preserving its chosen block through the prior representative. This bijection gives \(H_n(t,k)=(t-1)S_{t-1}(n-1,k)\). If \(T=n+1\), all labels are distinct, so \(k=n\) and the partition is unique.

**Weighted planar paths.** Fix \(N=n-1\). For \(0\le r\le N\), \(S_r(N,k)\) is the sum of weights of directed lattice paths from \((r,r)\) to \((N,k)\) with unit time increments. A horizontal-in-height step \((i,j)\to(i+1,j)\) has weight \(j\); an upward step \((i,j)\to(i+1,j+1)\) has weight one. Indeed, at time \(r\) there is one restricted partition with \(r\) distinct singleton blocks, and each later element either joins one of \(j\) blocks or starts a new block. Thus the path weights satisfy the restricted Stirling recurrence with the correct initial condition.

**All minors.** Choose increasing sources \((r_1,r_1),\ldots,(r_d,r_d)\) and increasing sinks \((N,k_1),\ldots,(N,k_d)\). Apply the signed, weight-preserving tail-switching involution to any family of paths containing an intersection. For any permutation of sinks other than the identity, some pair of sources is assigned inverted sink heights. At the later source time the earlier path has height at most the later source height, while at the terminal time its assigned sink is higher; the paths must meet at a lattice vertex because height increments are zero or one. Thus **no nonintersecting family realizes a nonidentity sink permutation**. The determinant of \((S_{r_i}(N,k_j))_{i,j=1}^d\) therefore equals a sum of nonnegative products of weights of nonintersecting path families. It is nonnegative for every \(d\). Multiplying each row indexed by \(r=t-1\) by \(r>0\) preserves nonnegative minors. Adjoining the final row, which has its only nonzero entry in the last column, also preserves all minors: an included final row either contributes zero or expands with positive sign along the included last column. Hence \(H_n\) is totally nonnegative.

**Conditional likelihood ratios.** For each \(k\), \(\sum_t H_n(t,k)=S(n,k)\). Total nonnegativity of the two-by-two minors gives, for \(k_1<k_2\) and \(t_1<t_2\), \(\Pr(T=t_1\mid K=k_1)\Pr(T=t_2\mid K=k_2)\ge\Pr(T=t_1\mid K=k_2)\Pr(T=t_2\mid K=k_1)\). This is monotone likelihood-ratio order, including possible zero-probability cells. It implies stochastic order, and the common-uniform inverse-CDF construction couples all \(k\) monotonically. The supports differ because their largest values are \(k+1\) (for \(k<n\)) and \(n+1\) (for \(k=n\)), so the conditional distributions are not identical for distinct \(k\).

## Verification
Run `python3 verify.py` using only the Python standard library. The checker independently enumerates restricted-growth set partitions for \(2\le n\le9\), verifies each joint count and column sum, checks all two-by-two minors, checks minors of orders three and four through \(n=9\), and separately checks finite-step total positivity for uniform occupancy pure-birth transition kernels. It passed 166247 exact integer assertions. Finite checks are supporting evidence only; the planar-path argument proves all dimensions.

## Relationship to prior work
Broder introduced and studied the restricted \(r\)-Stirling numbers; their recurrence and combinatorial interpretation are classical, not claimed as new. The 2016 Arratia–DeSalvo work addresses random assemblies under specified component counts, principally their component-size profiles. Work on total positivity of fixed-parameter \(r\)-Stirling matrices concerns a different pair of varying indices. The claim here is about **all-order minors with the distinguished-element count and the final block count varying together at a fixed ground-set size**, plus its birthday/terminal-richness interpretation. General planar-network determinant machinery is acknowledged; the new point claimed is the concrete kernel identification and resulting all-order distributional order. Historical priority remains subject to comparison with older generalized-Stirling and total-positivity sources.

## Limitations
The result assumes uniform iid samples. It does not imply a refinement coupling of the full equality partitions, nor does it assert conditional independence, strict positivity of every minor, or analogous ordering for arbitrary nonuniform probabilities. A potentially close older original treatment of restricted Stirling numbers could not be examined in full. Independent review has not been performed.

## References
1. A. Z. Broder, *The r-Stirling Numbers*, Stanford technical report CS-TR-82-949 (1982); *Discrete Mathematics* 49 (1984), 241–259, DOI:10.1016/0012-365X(84)90161-4.
2. R. Arratia and S. DeSalvo, *Completely effective error bounds for Stirling Numbers of the first and second kind via Poisson Approximation*, arXiv:1404.3007 (2014-04-11).
3. R. Arratia and S. DeSalvo, *Poisson and independent process approximation for random combinatorial structures with a given number of components, and near-universal behavior for low rank assemblies*, arXiv:1606.04642 (2016-06-15).
4. X. Chen, B. Deb, A. Dyachenko, T. Gilmore and A. D. Sokal, *Coefficientwise Total Positivity of Some Matrices Defined by Linear Recurrences*, Séminaire Lotharingien de Combinatoire 85B (2021), article 30.
