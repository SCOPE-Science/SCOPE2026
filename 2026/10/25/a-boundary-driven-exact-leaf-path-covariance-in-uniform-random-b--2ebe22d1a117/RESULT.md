# A boundary-driven exact leaf–path covariance in uniform random binary search trees

## Finding
For each integer \(n\ge2\), a binary search tree is formed by inserting a uniform random permutation of \(n\) distinct ordered keys into an initially empty tree. Write \(L_n\) for the number of **stored vertices having no nonempty left or right child** and \(T_n\) for the sum of depths of all stored vertices (root depth zero). Then
\[
\boxed{\operatorname{Cov}(L_n,T_n)=-\frac{(n+3)(n-2)}{9n}.}
\]
The covariance is zero at \(n=2\), strictly negative for every \(n\ge3\), and equals \(-n/9+O(1)\) as \(n\to\infty\). A local structural identity driving the result is that the covariance of the two conditional expectations, given the root split, is exactly \(-4(H_{n-1}-1)/(3n)\), concentrated at the extreme root splits.

## Assumptions and scope
The keys are distinct; every insertion order is equally likely. The tree is the standard *unbalanced* binary search tree, not a uniformly chosen Catalan shape or a random recursive (increasing-parent) tree. For the empty tree put \(L_0=T_0=0\); for the one-vertex tree \(L_1=1\) and \(T_1=0\). An internal leaf is a stored key with two absent children; the \(n+1\) null external pointers are **not** counted as leaves. Every random variable has a finite second moment at fixed \(n\). Let \(H_m=\sum_{a=1}^m a^{-1}\), with \(H_0=0\).

## Proof
**1. Conditional split.** The number \(K\) of keys sent to the left subtree is uniform on \(0,\dots,n-1\). Given \(K=k\), the left and right subtrees are independent uniform BSTs of sizes \(k\) and \(n-1-k\). For \(n\ge2\),
\[
L_n=L_k^{(1)}+L_{n-1-k}^{(2)},\qquad
T_n=T_k^{(1)}+T_{n-1-k}^{(2)}+(n-1).
\]
At size one the exceptional leaf contribution is already incorporated in the initial condition.

**2. First moments and a boundary correction.** The same recursion, or induction on size, gives
\[
\ell_m:=\mathbb E L_m=\frac{m+1}{3}\quad(m\ge2),\qquad
 t_m:=\mathbb E T_m=2(m+1)H_m-4m\quad(m\ge0).
\]
For clarity the formula for \(t_m\) also holds at \(m=0,1\), but \(\ell_0=0\) and \(\ell_1=1\). Define \(\delta_0=-1/3\), \(\delta_1=1/3\), and \(\delta_m=0\) for \(m\ge2\). Then \(\ell_m=(m+1)/3+\delta_m\) for all \(m\ge0\), and for each \(n\ge2\),
\[
\mathbb E[L_n\mid K=k]=\frac{n+1}{3}+\delta_k+\delta_{n-1-k},\qquad
\mathbb E[T_n\mid K=k]=t_k+t_{n-1-k}+n-1.
\]
The deviations of the leaf regression from its constant baseline occur only for \(k\in\{0,1,n-2,n-1\}\) (with possible overlap at small sizes). The sum \(\sum_{k=0}^{n-1}\delta_k=0\) for \(n\ge2\). Consequently
\[
\begin{aligned}
B_n&:=\operatorname{Cov}(\mathbb E[L_n\mid K],\mathbb E[T_n\mid K])\\
&=\frac{2}{n}\sum_{k=0}^{n-1}\delta_k\bigl(t_k+t_{n-1-k}\bigr)\\
&=\frac{2}{3n}\bigl(t_{n-2}-t_{n-1}\bigr)
=-\frac{4}{3n}(H_{n-1}-1),\qquad n\ge2,
\end{aligned}
\]
where \(t_m-t_{m-1}=2(H_m-1)\) for \(m\ge1\). This formula also gives \(B_2=0\).

**3. Covariance recursion.** Put \(c_n=\operatorname{Cov}(L_n,T_n)\) and \(c_0=c_1=0\). Conditional independence of the two subtrees, followed by the law of total covariance, gives for all \(n\ge2\)
\[
c_n=\frac{2}{n}\sum_{k=0}^{n-1}c_k-\frac{4}{3n}(H_{n-1}-1).
\]
Since \(c_2=0\), subtract the equation at size \(n\) from the equation at size \(n+1\):
\[
(n+1)c_{n+1}=(n+2)c_n-\frac4{3n},\qquad n\ge2.
\]
Thus
\[
\frac{c_n}{n+1}=-\frac43\sum_{k=2}^{n-1}\frac1{k(k+1)(k+2)}
=-\frac19+\frac{2}{3n(n+1)}.
\]
Multiplying by \(n+1\) and factoring proves the exact formula and its boundary and asymptotic assertions. No infinite-size approximation is used in the finite-size identity.

## Verification
The standalone \(\texttt{verify.py}\) runs two logically distinct finite checks: exact-rational joint-moment recursions for every size through \(n=100\) and enumeration of all \(46{,}233\) permutations across sizes \(1\) through \(8\) using explicit key insertion. It compares the resulting leaf, depth and mixed moments, and verifies the covariance formula. The enumerations do not establish the infinite theorem: the proof is the conditional decomposition and exact telescoping argument above. Run with \(\texttt{python3 verify.py}\), using only the Python standard library.

## Relationship to prior work
Flajolet, Gourdon and Martínez (1997) analyze fringe-pattern counts in uniform random BSTs and obtain the marginal leaf mean, variance, and local limit theorem; their increasing-tree encoding also equates leaf counts with peaks of a permutation. Bóna and Pittel (first posted 2014) study vertices by distance from leaves and include the same marginal leaf mean and a leaf generating function. Dekking and Meester (2003) study normalized tree path lengths. Chern, Fuchs, Hwang and Neininger (first posted 2015) study joint shape–path statistics for \(m\)-ary search trees with \(m\ge3\) and discuss leaf count versus path length for multidimensional quadtrees; their quadtree discussion explicitly treats dimensions \(d\ge2\). Eberl (2020) details the BST–quicksort path-length equivalence. Those sources provide the definitions and marginal components but do not, in the material inspected, state this exact finite-size leaf–internal-path covariance or its boundary-local conditional-mean mechanism. By that equivalence, the present statistic also measures covariance of BST terminal-node count with ordinary quicksort comparison cost, provided the same permutation coupling is used. Absence from searched sources does not establish historical priority.

## Limitations
This is an exact second-moment identity, not a statement of negative association or stochastic domination for the two variables. It does not cover external null-pointer leaf counts (which are deterministic), balanced variants of BSTs, or arbitrary insertion distributions. The full historical literature is not exhaustively checked, and one relevant older path-length source was only available as abstract and bibliographic data. Independent mathematical review has not been performed.

## References
1. P. Flajolet, X. Gourdon and C. Martínez, *Patterns in random binary search trees*, Random Structures & Algorithms 11 (1997), 223–244. Accessible author PDF: https://www.cs.upc.edu/~conrado/research/papers/rsa-fgm97.pdf . Public seminar record dated 1996-10-07: https://algo.inria.fr/seminars/sem96-97/flajolet.html .
2. M. Bóna and B. Pittel, *On a random search tree: asymptotic enumeration of vertices by distance from leaves*, arXiv:1412.2796, first posted 2014-12-08.
3. H.-H. Chern, M. Fuchs, H.-K. Hwang and R. Neininger, *Dependence and phase changes in random m-ary search trees*, arXiv:1501.05135, first posted 2015-01-21, especially Section 5.
4. F. M. Dekking and L. E. Meester, *An almost sure result for path lengths in binary search trees*, Advances in Applied Probability 35 (2003), 363–376, doi:10.1239/aap/1051201652.
5. M. Eberl, *Verified analysis of random binary tree structures*, Journal of Automated Reasoning 64 (2020), doi:10.1007/s10817-020-09545-0.
