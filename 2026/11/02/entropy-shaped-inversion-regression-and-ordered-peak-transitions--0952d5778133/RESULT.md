# Entropy-shaped inversion regression and ordered peak transitions in recursive separable permutations

## Finding
For every integer \(n\geq2\) and every \(p\in(0,1)\), consider the random recursive separable permutation \(\sigma_n\) obtained by starting from \((1)\) and repeatedly choosing one current entry uniformly, replacing it by two consecutive values in increasing order with probability \(p\), or in decreasing order with probability \(q=1-p\), adjusting larger values to preserve a permutation. Define its inversion count \(I_n\), its gap-descents \(B_k=\mathbf1\{\sigma_n(k)>\sigma_n(k+1)\}\), and \(D_n=\sum_{k=1}^{n-1}B_k\). Write \(H_0=0\) and \(H_m=\sum_{j=1}^{m}j^{-1}\).

**Exact positional regression.** The variables \(B_1,\ldots,B_{n-1}\) are independent Bernoulli variables with parameter \(q\). For every realizable descent signature,
\[
\mathbb E[I_n\mid B_1,\ldots,B_{n-1}]
 =\sum_{k=1}^{n-1}w_{n,k}B_k,
\qquad
w_{n,k}=nH_{n-1}-kH_{k-1}-(n-k)H_{n-k-1}-1.
\]
The weights are positive and symmetric, and satisfy
\[
w_{n,k+1}-w_{n,k}=H_{n-k-1}-H_k
\quad(1\leq k\leq n-2).
\]
They strictly increase toward the middle and then strictly decrease, with a two-gap plateau only when \(n\) is odd. In particular,
\[
\operatorname{Cov}(I_n,B_k)=pq\,w_{n,k},\qquad
\mathbb E[I_n\mid D_n=d]=\frac{nd}{2}
\quad(0\leq d\leq n-1).
\]
For any \(\alpha\in(0,1)\), with \(k_n=\lfloor\alpha n\rfloor\),
\[
\frac{w_{n,k_n}}n\longrightarrow
h(\alpha)=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha),
\qquad w_{n,1}=H_{n-1}\sim\log n.
\]
Thus an interior gap has influence of order \(n\), with a binary-entropy profile, whereas an endpoint gap has influence only of order \(\log n\).

**Consequent ordered peak-covariance phase diagram.** For \(n\geq3\) and \(2\leq i\leq n-1\), let \(P_i=\mathbf1\{\sigma_n(i-1)<\sigma_n(i)>\sigma_n(i+1)\}\). Then
\[
\operatorname{Cov}(I_n,P_i)
=pq\left(pw_{n,i}-qw_{n,i-1}\right).
\]
This covariance changes sign *exactly once* as \(p\) passes
\[
p^*_{n,i}=\frac{w_{n,i-1}}{w_{n,i-1}+w_{n,i}}:\quad
\operatorname{Cov}(I_n,P_i)<0\ (p<p^*_{n,i}),\quad
=0\ (p=p^*_{n,i}),\quad >0\ (p>p^*_{n,i}).
\]
For fixed \(n\geq4\), the thresholds \(p^*_{n,2},\ldots,p^*_{n,n-1}\) are *strictly increasing*, and \(p^*_{n,n+1-i}=1-p^*_{n,i}\). Their left and right boundary values converge respectively to \(1/3\) and \(2/3\) as \(n\to\infty\), while \(p^*_{n,\lfloor\alpha n\rfloor}\to1/2\) at every fixed interior proportion \(\alpha\in(0,1)\).

## Assumptions and scope
This is the recursively inflated separable-permutation distribution, **not** the uniform distribution on all separable permutations. The integer \(n\) is finite and arbitrary, while the increasing-inflation probability is a common fixed \(p\in(0,1)\). A peak is defined only at an interior position. The displayed limit in \(n\) is pointwise for fixed \(\alpha\) (or fixed boundary offset), and does not assert a uniform two-parameter limit when \(p\) or the gap position moves with \(n\).

## Proof
**1. Independent signed internal nodes.** The inflation construction has a full plane binary-tree representation: each insertion splits one uniformly selected leaf and independently gives the new internal node a positive sign with probability \(p\) or a negative sign with probability \(q\). Reading the leaves left to right and interpreting each internal node as a direct or skew sum gives exactly the permutation. In particular, each internal node is canonically located at the unique *gap* between its left and right leaf subtrees. Its sign is negative precisely when the two adjacent permutation entries across that gap form a descent. As the tree is formed without reference to signs, the complete ordered descent signature consists of independent Bernoulli-\(q\) signs and is independent of the unsigned tree.

For an internal node at gap \(k\), let \(L_k\) and \(R_k\) be its left and right *leaf* subtree sizes. Each pair of leaf positions has exactly one lowest common ancestor. The corresponding pair of permutation values is inverted precisely if that ancestor carries a negative sign. Hence, for every tree and every sign assignment,
\[
 I_n=\sum_{k=1}^{n-1}B_kL_kR_k.
\tag{1}
\]
Taking conditional expectations over the tree yields the desired regression with \(w_{n,k}=\mathbb E[L_kR_k]\), provided the weights are computed.

**2. Unsigned tree and independent priorities.** Starting from the first split, the counts of descendant leaves on the root's two sides evolve as a two-color Pólya urn, initially with one leaf of each color. Consequently, at total size \(n\), the left-root leaf count is uniform on \(\{1,\ldots,n-1\}\). Conditional on these counts, the left and right growth histories are independent uniform-leaf-splitting trees. This recursion is identical to that of a random binary search tree on the \(n-1\) ordered gap keys. It may therefore be constructed from independent uniform priorities \(U_1,\ldots,U_{n-1}\): the lowest-priority gap is the root, and the construction recurses on the gaps to its left and right.

For a fixed gap \(k\), the left leaf count equals the distance to the nearest gap strictly to its left with priority below \(U_k\), or to boundary zero if no such gap exists; the right count is defined similarly using boundary \(n\). Conditional on \(U_k=t\), the left and right priorities are independent. The tail-sum identity gives
\[
 \mathbb E[L_k\mid U_k=t]=\sum_{j=0}^{k-1}(1-t)^j
 =\frac{1-(1-t)^k}{t},
\]
\[
 \mathbb E[R_k\mid U_k=t]=\sum_{j=0}^{n-k-1}(1-t)^j
 =\frac{1-(1-t)^{n-k}}{t}.
\]
As a result,
\[
 w_{n,k}=\int_0^1\frac{(1-(1-t)^k)(1-(1-t)^{n-k})}{t^2}\,dt.
\tag{2}
\]
For \(a=k\), \(b=n-k\), substitute \(s=1-t\) and integrate by parts. The boundary term is \(-1\), while
\[
 \int_0^1\frac{s^{a-1}(1-s^b)}{1-s}\,ds=H_{a+b-1}-H_{a-1}.
\]
Equation (2) therefore equals
\[
 -1+k(H_{n-1}-H_{k-1})+(n-k)(H_{n-1}-H_{n-k-1}),
\]
which is the claimed harmonic formula. This independently verifies every normalization, including \(n=2\), where the sole weight is \(1\).

**3. Monotonicity, conditional regression, and limits.** Subtracting consecutive harmonic expressions gives
\[
 w_{n,k+1}-w_{n,k}=H_{n-k-1}-H_k.
\tag{3}
\]
This proves symmetry and the indicated unimodality. In every full binary tree the pairs separated at different internal nodes partition all unordered pairs of leaves; therefore \(\sum_k L_kR_k=\binom n2\), and \(\sum_k w_{n,k}=\binom n2\). Equation (1), independence of signs and tree, and conditional exchangeability of the \(B_k\)'s given \(D_n=d\) now yield
\[
 \operatorname{Cov}(I_n,B_k)=pq\,w_{n,k},\qquad
 \mathbb E[I_n\mid D_n=d]
 =\frac{d}{n-1}\binom n2=\frac{nd}{2}.
\]
Finally, \(H_{m-1}=\log m+\gamma+O(m^{-1})\) gives \(w_{n,\lfloor\alpha n\rfloor}/n\to h(\alpha)\). The formula at \(k=1\) simplifies exactly to \(H_{n-1}\). At fixed positive \(k\), it also yields \(w_{n,k}=k\log n+O_k(1)\).

**4. Peaks and critical probabilities.** The adjacent signs satisfy \(P_i=(1-B_{i-1})B_i\). Independence gives
\[
 \operatorname{Cov}(B_i,P_i)=p^2q,\qquad
 \operatorname{Cov}(B_{i-1},P_i)=-pq^2,
\]
with all other sign covariances zero. The inversion regression immediately yields the stated peak covariance and its unique zero at \(p^*_{n,i}\). Moreover, (3) has strictly decreasing successive differences because
\[
 (w_{n,k+2}-w_{n,k+1})-(w_{n,k+1}-w_{n,k})
 =-\frac1{n-k-1}-\frac1{k+1}<0.
\]
Thus the positive weight sequence is strictly concave and hence strictly log-concave at its interior positions. The ratios \(w_{n,i}/w_{n,i-1}\) strictly decrease with \(i\), so the critical values \(p^*_{n,i}=1/(1+w_{n,i}/w_{n,i-1})\) strictly increase. Symmetry gives the reflected-threshold identity. Finally, \(w_{n,k}=k\log n+O_k(1)\) yields \(p^*_{n,2}\to1/3\), reflection gives \(p^*_{n,n-1}\to2/3\), and the entropy limit yields the bulk critical probability \(1/2\). All claims follow.

## Verification
A standalone Python 3 program, `check_recinv.py`, constructs the original permutation-inflation Markov chain with exact rational probabilities independently of the priority-tree proof. For every size \(2\le n\le7\) and biases \(p\in\{1/2,2/3\}\), it enumerates every reachable permutation and checks (i) all complete descent-signature masses, (ii) every conditional inversion expectation, (iii) every gap-inversion covariance, (iv) every peak-inversion covariance, and (v) threshold ordering/symmetry. It reports 624 passed exact assertions; no floating-point tolerance is used. Execute `python3 check_recinv.py` from a directory containing that file. These finite checks are not a substitute for the all-size argument above.

## Relationship to prior work
Féray and Rivera-Lopez introduced the recursive separable-permutation law and established its tree representation and Bernoulli distribution for the *total* number of descents. Their Proposition 1.7 specifies each permutation's probability, and their Lemma 4.8 uses independent node signs. These facts are prerequisites; they do not state the gap-wise conditional inversion regression, its binary-entropy sensitivity profile, or the ordered local peak-covariance critical probabilities derived here. Chen, Kitaev and Zhang obtain generating functions for ascent/descent and extremal statistics in the **uniform** separable-permutation setting, rather than the signed recursive law or its inversion–peak regression. The random binary-search-tree distribution of unsigned shapes is classical; the contribution here is the exact model-specific identification of its product-subtree influence kernel and the resulting local/global dependence classification, not the BST representation itself.

The novelty assessment is relative to the sources inspected, not a guarantee of historical priority. In particular, the source's exact point probabilities formally determine all finite moments, and an unlocated alternative evaluation of those probabilities could contain the same formulas.

## Limitations
The result does not assert independence of inversions and descents (their covariance is positive), a central limit theorem, higher conditional moments, or a generalization to uniformly sampled separable permutations. The phase thresholds pertain to individual **interior peaks**, not to an arbitrary pattern statistic. The large-size statements hold in the stated fixed-position or fixed-proportion regimes, without uniform error bounds in a moving parameter. Independent mathematical validation has not been performed.

## References
1. V. Féray and K. Rivera-Lopez, *The permuton limit of random recursive separable permutations*, arXiv:2306.04278 (first posted 2023-06-07), Confluentes Mathematici 15 (2023), 45–82, DOI:10.5802/cml.92. Primary source for the inflation process, increasing-tree representation and descent distribution.
2. J. N. Chen, S. Kitaev and P. B. Zhang, *Distributions of statistics on separable permutations*, arXiv:2404.18517 (2024), Discrete Applied Mathematics 355 (2024), 169–179. Uniform-separable statistics, distinct sampling law.
3. J. I. Munro, K. Nicholson, L. Seelbach Benkner and S. Wild, *Hypersuccinct Trees—New universal tree source codes for optimal compressed tree data structures* (2021). Standard random-BST uniform-split representation (Appendix E); no claim of a new random-tree representation is made.
