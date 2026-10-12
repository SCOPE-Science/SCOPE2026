# A boundary-localized covariance of extreme search cost and leaf count in random binary search trees

## Finding
Let \(T_n\) be the binary search tree obtained by inserting a uniformly random permutation of the ordered keys \(1,\ldots,n\). Let \(R_n\) denote the number of occupied nodes visited in a successful search for the largest key (equivalently, the number of nodes on the root-to-maximum right spine), and let \(L_n\) denote the number of nodes with **no children** (occupied/internal leaves, not external null pointers). For every integer \(n\ge2\),
\[
\boxed{\operatorname{Cov}(R_n,L_n)=\frac{(n-2)(n+1)}{12n(n-1)}=\frac1{12}-\frac1{6n(n-1)}.}
\]
Thus the covariance vanishes at \(n=2\), is positive at every \(n\ge3\), and approaches \(1/12\) from below. The associated correlation vanishes: 
\[
\operatorname{Corr}(R_n,L_n)\sim\sqrt{\frac5{32}}\frac1{\sqrt{n\log n}}.
\]
The mixed covariance created at a new root depends **only** on the four extreme allocations of nodes to the right subtree. Generic balanced splits contribute zero at that step.

## Assumptions and scope
All \(n!\) insertion orders of \(1,\ldots,n\) are equiprobable. There are no ties, rebalancing operations, or deletions. \(R_n\) includes the root and the target node, so \(R_1=1\). The empty tree has \(R_0=L_0=0\); a singleton tree has \(L_1=1\). Variance and covariance refer to the insertion-order distribution. The covariance identity starts at \(n=2\); the correlation asymptotic is for \(n\to\infty\). These statistics must not be confused with the height of the tree or the number of external missing-child pointers.

## Proof
Write \(H_m=\sum_{j=1}^{m}1/j\), with \(H_0=0\). The first inserted key has uniform rank. Conditional on the number \(m\in\{0,\ldots,n-1\}\) of keys larger than the root, the left and right subtrees are independent random binary search trees with sizes \(n-1-m\) and \(m\). Consequently, for \(n\ge2\),
\[
R_n=1+R_m,\qquad L_n=L_m+L_{n-1-m}.
\]
For \(n=1\), the root itself is a leaf, as specified above. Let \(r_m=\mathbb E R_m\), \(\ell_m=\mathbb E L_m\), and \(c_m=\operatorname{Cov}(R_m,L_m)\). The first recurrence yields \(r_0=0\) and
\[
r_n=1+\frac1n\sum_{m=0}^{n-1}r_m=H_n.
\]
For leaves, \(\ell_0=0\), \(\ell_1=1\), and the second recurrence gives \(\ell_m=(m+1)/3\) for each \(m\ge2\); substitution proves this by induction (the \(n=2\) base case has exactly one leaf).

By total covariance and conditional independence of the two subtrees,
\[
c_n=\frac1n\sum_{m=0}^{n-1}c_m+\operatorname{Cov}_{M}(H_M,\ell_M+\ell_{n-1-M}),
\]
where \(M\) is uniform on \(\{0,\ldots,n-1\}\). Set \(b_m=\ell_m-(m+1)/3\). Its only nonzero entries are \(b_0=-1/3\) and \(b_1=1/3\). For every \(n\ge3\), including the coincident corrections at \(n=3\),
\[
\ell_m+\ell_{n-1-m}=\frac{n+1}{3}+b_m+b_{n-1-m}.
\]
The mean of the correction is zero because the four signed boundary contributions sum to zero (with multiplicities), so its covariance with \(H_M\) equals
\[
a_n=\frac{H_1+H_{n-2}-H_0-H_{n-1}}{3n}
=\frac{n-2}{3n(n-1)}.
\]
The formula also gives \(a_2=0\). Thus \(c_0=c_1=c_2=0\), \(c_3=1/18\), and for \(n\ge3\),
\[
c_n=\frac1n\sum_{m<n}c_m+\frac{n-2}{3n(n-1)}.
\]
Eliminating the prefix sum between successive equations gives, for \(n\ge4\),
\[
c_n-c_{n-1}=\frac1{3n(n-1)(n-2)}.
\]
The stated rational expression solves this recurrence with \(c_3=1/18\). The sign and limit follow directly.

For the correlation, the right-spine nodes are precisely upper records in the random insertion order. Their indicators are independent Bernoulli random variables with success probabilities \(1/j\), so \(\operatorname{Var}(R_n)=H_n-H_n^{(2)}\), where \(H_n^{(2)}=\sum_{j=1}^n j^{-2}\). The established exact leaf variance is \(\operatorname{Var}(L_n)=2(n+1)/45\) for \(n>3\) [1, Example 8.1]. Using \(H_n\sim\log n\) and the covariance limit gives the asserted \(\sqrt{5/32}\) coefficient. This conclusion concerns Pearson correlation, not conditional expectation or nonlinear association.

## Verification
A standalone standard-library checker, `verify.py`, exhaustively builds all insertion-permutation trees for \(2\le n\le8\), compares the direct rational covariance against the formula, and separately verifies the root-split recurrence and closed form for all \(2\le n\le500\). It also checks the claimed leaf means and right-spine means on the exhaustive range. The finite computations test the proof but are not substituted for it. To reproduce, run `python verify.py` with Python 3.9 or later.

## Relationship to prior work
Holmgren and Janson [1] study fringe-subtree counts for this exact random binary-search-tree law and reproduce the exact mean and variance of leaf counts, together with covariance formulas **between** fringe-count statistics. Their Section 8.1, Example 8.1 does not supply covariance with the path to the maximum key. Grübel and Stefanoski [2] study depth distributions of specified keys, including the extreme-key case, but their primary results are marginal depth limits rather than mixed leaf-count moments. The present statement combines a global extreme-key path and a local occupancy count and identifies a root-boundary mechanism not entailed by the cited marginal formulas alone. An unindexed joint generating function could imply the result; no exhaustive priority claim is made.

## Limitations
This is an exact second-moment identity for a uniformly random insertion-order binary search tree, not for uniformly Catalan-distributed binary trees or for dynamic/rebalanced variants. It does not determine a joint distribution, a conditional expectation, or a functional limit. The archive comparison is limited to the cited full texts and searchable literature; historical priority is not independently established.

## References
[1] C. Holmgren and S. Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Recursive Trees*, arXiv:1406.6883v1, publicly submitted 26 June 2014, https://arxiv.org/html/1406.6883v1 (Section 8.1, Example 8.1; primary MSC 60C05).

[2] R. Grübel and N. Stefanoski, *Mixed Poisson Approximation of Node Depth Distributions in Random Binary Search Trees*, *Annals of Applied Probability* 15 (2005), 279–297, arXiv:math/0503738v1, https://arxiv.org/pdf/math/0503738 (Theorem 1, depth decomposition).
