# The two-thirds covariance threshold for fringe subtree sizes in random binary search trees

## Finding

Construct a binary search tree \(T_n\) by inserting a uniformly random permutation of \(n\ge2\) distinct keys. Let \(I_n\) be the number of keys in its root's left subtree, and put
\[
Q_n=(2I_n-(n-1))^2.
\]
For each \(1\le k\le n\), let \(X_{n,k}\) count vertices whose fringe subtree (the vertex and all its descendants) has exactly \(k\) vertices. For **every** integer pair \(n\ge2\) and \(1\le k<n\),
\[
\boxed{\operatorname{Cov}(Q_n,X_{n,k})=
\frac{4k(3k+1-2n)}{3n}.}
\tag{1}
\]
Consequently, the covariance is negative for \(k<(2n-1)/3\), positive for \(k>(2n-1)/3\), and zero exactly when \(3k+1=2n\). The spectrum across sizes therefore changes sign exactly once, with a possible single zero. This is a sharp finite-size threshold, not an asymptotic approximation.

The dependence on the first split is also explicit. Write
\[
\alpha_k=\frac2{(k+1)(k+2)},\qquad
 d_k(m)=\begin{cases}
-\alpha_k(m+1),&0\le m<k,\\
\frac{k}{k+2},&m=k,\\
0,&m>k.
\end{cases}
\]
Then for every \(0\le i<n\) and \(1\le k<n\),
\[
\boxed{\mathbb E[X_{n,k}\mid I_n=i]
=\alpha_k(n+1)+d_k(i)+d_k(n-1-i).}
\tag{2}
\]
No separation assumption on the two boundary layers in (2) is needed: they may overlap.

Two exact conservation identities clarify how the sign reversal relates to global tree complexity:
\[
\sum_{k=1}^{n-1}\operatorname{Cov}(Q_n,X_{n,k})=0,
\tag{3}
\]
\[
\sum_{k=1}^{n-1}(k-1)\operatorname{Cov}(Q_n,X_{n,k})
=\frac{(n-2)(n-1)(n+1)}9.
\tag{4}
\]
The last identity is the known cubic covariance between root imbalance and internal path length, now resolved into exact positive and negative fringe-size contributions. It is a consistency consequence of (1), not an independently claimed discovery.

## Assumptions and scope

The tree is the standard random-permutation binary search tree on \(n\) keys, with empty subtrees allowed. The root split \(I_n\) is uniform on \(\{0,\ldots,n-1\}\). Conditional on \(I_n=i\), the two children are independent random binary search trees on \(i\) and \(n-1-i\) keys. Each vertex has one fringe subtree, including itself.

Formula (1) excludes \(k=n\): the entire tree is the sole fringe subtree of size \(n\), so \(X_{n,n}=1\) deterministically and its covariance with \(Q_n\) is zero. At \(n=2\), \(Q_n\) is constant and (1) correctly gives zero for \(k=1\). Strict negative/positive signs occur across sizes for every \(n\ge3\). These are covariance statements, not claims of stochastic dominance or causation.

## Proof

Write \(f_k(m)=\mathbb E[X_{m,k}]\), including \(f_k(0)=0\). For \(m<k\), clearly \(f_k(m)=0\); for \(m=k\), \(f_k(k)=1\). Uniform root splitting gives, for every \(m>k\),
\[
f_k(m)=\frac2m\sum_{j=0}^{m-1}f_k(j).
\tag{5}
\]
At \(m=k+1\), equation (5) gives \(f_k(k+1)=2/(k+1)\). Subtracting the recurrence at successive sizes, or using induction, gives
\[
f_k(m)=\alpha_k(m+1),\quad m>k,\qquad
\alpha_k=\frac2{(k+1)(k+2)}.
\tag{6}
\]
For all integers \(m\ge0\), equations (5)--(6) can be summarized by \(f_k(m)=\alpha_k(m+1)+d_k(m)\), with \(d_k\) exactly as defined in the Finding.

For \(k<n\), the root itself cannot contribute to \(X_{n,k}\). Conditioning on its left-subtree size therefore gives
\[
\mathbb E[X_{n,k}\mid I_n=i]=f_k(i)+f_k(n-1-i),
\]
which is (2). The finite boundary defect has three cancellation moments:
\[
\sum_{m=0}^{k}d_k(m)=0,\qquad
\sum_{m=0}^{k}m\,d_k(m)=\frac{k}{3},\qquad
\sum_{m=0}^{k}m^2d_k(m)=\frac{k(3k-1)}6.
\tag{7}
\]
To check (7) directly, use \(d_k(m)=-\alpha_k(m+1)\) for \(m<k\), \(d_k(k)=1-\alpha_k(k+1)\), and the elementary sums
\[
\sum_{m=0}^{k}m(m+1)=\frac{k(k+1)(k+2)}3,
\]
\[
\sum_{m=0}^{k}m^2(m+1)=\frac{k(k+1)(k+2)(3k+1)}{12}.
\]
In particular, \(\mathbb E[X_{n,k}]=\alpha_k(n+1)\), including when the two boundary regions overlap.

Put \(N=n-1\), so that \(Q_n=(2I_n-N)^2\). Since \(Q_n\) is determined by the root split, the law of total covariance and (2) give
\[
\operatorname{Cov}(Q_n,X_{n,k})
=\frac1n\sum_{i=0}^{n-1}(2i-N)^2\bigl(d_k(i)+d_k(N-i)\bigr).
\]
By symmetry, this equals \(2/n\) times the contribution of the first defect with the quadratic multiplied by four, hence
\[
\begin{aligned}
\operatorname{Cov}(Q_n,X_{n,k})
&=\frac8n\sum_{i=0}^{k}(i-N/2)^2d_k(i)\\
&=\frac8n\left(\frac{k(3k-1)}6-N\frac{k}3\right)\\
&=\frac{4k(3k+1-2n)}{3n}.
\end{aligned}
\]
The quadratic constant disappears by the first equality in (7). This proves (1) for all admissible \(n,k\). Its sign classification follows because \(k>0\).

Finally, since every tree on \(n\) vertices has exactly \(n\) fringe subtrees in total, \(\sum_{k=1}^{n}X_{n,k}=n\) and \(X_{n,n}=1\). This gives (3). The internal path length equals \(\sum_{k=1}^{n}(k-1)X_{n,k}\): each vertex contributes one for each descendant other than itself. Using (1) and standard power sums in this identity gives (4). In particular, \(\sum_{k=1}^{n-1}k(3k+1-2n)=0\), while \(\sum_{k=1}^{n-1}(k-1)k(3k+1-2n)=n(n-2)(n-1)(n+1)/12\), and multiplying the latter by \(4/(3n)\) yields (4).

## Verification

The accompanying `verify.py` reconstructs a binary search tree for each of the \(1!,\ldots,8!\) possible insertion sequences (beginning at two keys), computes every fringe-size count and the squared root imbalance, and checks (1)--(2) using exact rational arithmetic. A separate exact finite-sum check covers all \(2\le n\le200\), every admissible \(k\), the sign classification, and the two sum rules. Run it using `python verify.py`; the expected terminal output is `VERIFY_OK`.

The finite checks serve as reproducibility tests. They do not prove the unrestricted formulas; that proof is the recurrence and the finite defect identities above.

## Relationship to prior work

Dennert and Grübel (2010) obtain the classical mean subtree-size profile, pairwise covariances among size counts, and the conditional root-split identity underlying (2). Their equation (3.3) implies the conditional decomposition used here; their equation (2.1) provides (6). These are expressly prior facts. The new assessed statement is the **fully evaluated mixed covariance spectrum** with the nonlinear first-split statistic \(Q_n\), including its unique \(2/3\)-scale sign transition; it is not among their stated cross-size covariance formulas or asymptotic processes.

Holmgren and Janson (2015) develop general fringe-tree additive-functional laws and restate the classical exact mean and fixed-size count covariance formulas. These cover the marginals and interactions between two fringe counts but do not explicitly calculate root-imbalance / single-size mixed moments.

Seelbach Benkner and Wagner (2020) study distinct isomorphism types of fringe trees and their compression relevance; their random-BST part explains why fringe-size statistics are natural. It is the dated motivating source here, not the origin of the classical mean formula.

The published finding *Squared root imbalance has an exact cubic covariance with random-BST path length* gives precisely the aggregate right side of (4), rather than the signed component-by-component spectrum (1). Formula (1) implies that previous aggregate by weighted summation, whereas one aggregate covariance does not identify the individual positive and negative contributions. The base conditional identities are sufficiently explicit that algebraic derivability from prior techniques is a genuine priority risk; the proposed contribution is the exact sign classification and decomposition, not the availability of the recurrence.

## Limitations

No assertion is made about independent audits, stochastic ordering, other random-tree models, root-selection biases, or a universal phase transition in tree structure. The transition is a covariance sign boundary within the given finite random BST. The sign of a covariance does not imply the sign of every conditional comparison. The theorem concerns individual fringe-subtree **sizes**, not the number of distinct isomorphism types.

Earlier work already supplies the ingredients of the calculation. An unrecognized prior explicit mixed moment or an equivalent statement in the extensive subtree-profile literature would preclude a historical novelty claim; the available inspections did not locate one. Independent mathematical review remains outstanding.

## References

1. F. Dennert and R. Grübel, *On the Subtree Size Profile of Binary Search Trees*, Combinatorics, Probability and Computing 19 (2010), 561–578, DOI: 10.1017/S0963548309990630; especially (2.1), (3.3), and Proposition 2.1.
2. C. Holmgren and S. Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Recursive Trees*, arXiv:1406.6883 (2014), especially Lemma 3.3 and Theorem 1.12.
3. L. Seelbach Benkner and S. Wagner, *On the Collection of Fringe Subtrees in Random Binary Trees*, arXiv:2003.03323 (first public release 2020-03-06), especially Section 4.
4. *Squared root imbalance has an exact cubic covariance with random-BST path length*, published-finding corpus, public record 2026/10/4/SCOPE-squared-root-imbalance-has-an-exact-cubic-covariance-with-random--6d69fbada9a9, `RESULT.md`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-squared-root-imbalance-has-an-exact-cubic-covariance-with-random--6d69fbada9a9.
