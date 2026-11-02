# Exact negative leaf–path covariance and an obstruction to stochastic ordering in random binary search trees

## Finding

Let \(T_n\) be a binary search tree obtained by inserting a uniformly random permutation of \(\{1,\ldots,n\}\). Write \(P_n\) for the sum of depths of **key-bearing vertices**, with the root at depth zero, and \(L_n\) for the number of **key-bearing vertices with no children** (not the \(n+1\) null external child positions). For every \(n\geq2\),

\[
\operatorname{Cov}(P_n,L_n)=-\frac{n^2+n-6}{9n}.
\]

This covariance vanishes at \(n=2\), is strictly negative for every \(n\geq3\), and equals \(-n/9-1/9+2/(3n)\). Moreover,

\[
\lim_{n\to\infty}\sqrt n\,\operatorname{Corr}(P_n,L_n)
=-\sqrt{\frac{5}{18(7-2\pi^2/3)}}.
\]

The negative covariance **cannot** be strengthened to a universal stochastic-order assertion for the conditional path-length distributions. Already at \(n=7\), the two conditional distribution functions \(P_7\mid\{L_7=3\}\) and \(P_7\mid\{L_7=4\}\) cross:

\[
\begin{aligned}
\Pr(P_7\leq10\mid L_7=3)&=0,
&\Pr(P_7\leq10\mid L_7=4)&=\frac5{17},\\
\Pr(P_7\leq11\mid L_7=3)&=\frac{13}{36},
&\Pr(P_7\leq11\mid L_7=4)&=\frac5{17}.
\end{aligned}
\]

## Assumptions and scope

The insertion order is uniform over all \(n!\) permutations of distinct keys. Both the empty tree and the tree on a single key are included in the subtree recurrence. For an empty subtree put \((P_0,L_0)=(0,0)\); for a singleton put \((P_1,L_1)=(0,1)\). The leaf statistic does not count the empty root or null children. The correlation expression applies when both variances are nonzero, in particular for all sufficiently large \(n\). No stochastic ordering claim is made in either direction.

## Proof

**Root split.** In a random binary search tree on \(n\geq2\) keys, the left-subtree size \(K\) is uniform on \(\{0,\ldots,n-1\}\), the right size is \(J=n-1-K\), and, conditional on their sizes, the two subtrees are independent random binary search trees. Therefore

\[
P_n=P_K+P'_J+n-1,\qquad L_n=L_K+L'_J.
\]

Set \(p_n=\mathbb E P_n\), \(\ell_n=\mathbb E L_n\), \(a_n=\mathbb E(P_nL_n)\); all three are zero at index zero, and \((p_1,\ell_1,a_1)=(0,1,0)\). Independent subtrees give for \(n\geq2\)

\[
\begin{aligned}
np_n&=2\sum_{k<n}p_k+n(n-1),\\
n\ell_n&=2\sum_{k<n}\ell_k,\\
na_n&=2\sum_{k<n}a_k
+2\sum_{k<n}p_k\ell_{n-1-k}
+2(n-1)\sum_{k<n}\ell_k.
\end{aligned}
\]

The first two recurrences solve to

\[
p_n=2(n+1)H_n-4n,\qquad \ell_n=\frac{n+1}{3}\quad(n\geq2),
\]

where \(H_n=\sum_{j=1}^n1/j\). To solve the mixed recurrence, let \(P(z)=\sum_{n\geq0}p_nz^n\), \(B(z)=\sum_{n\geq0}\ell_nz^n\), and \(A(z)=\sum_{n\geq0}a_nz^n\). Then

\[
P(z)=\frac{-2z-2\log(1-z)}{(1-z)^2},\qquad
B(z)=\frac{(1-z)^{-2}-(1-z)}3,
\]

and coefficient extraction gives the exact differential equation

\[
A'(z)=\frac{2A(z)}{1-z}+2P(z)B(z)
+2z\left(\frac{B(z)}{1-z}\right)',\qquad A(0)=0.
\]

Direct substitution yields the unique formal-power-series solution

\[
\begin{aligned}
A(z)&=\frac{P(z)+zP'(z)}3+R(z),\\
R(z)&=-\frac{z}{9(1-z)^2}-\frac{z}{9(1-z)}
-\frac23\log(1-z)-\frac{4z}{9}.
\end{aligned}
\]

For every \(n\geq2\), the coefficient of \(z^n\) in \(R(z)\) is \(-(n+1)/9+2/(3n)\). Thus

\[
a_n=\frac{n+1}{3}p_n-\frac{n+1}{9}+\frac{2}{3n},
\]

which subtracts \(p_n\ell_n\) to prove the covariance formula. This derivation is exact and does not invoke any unproved independence assertion.

**The finite stochastic-order obstruction.** Define \(F_0(u,v)=1\), \(F_1(u,v)=u\), and for every \(n\geq2\)

\[
F_n(u,v)=\frac{v^{n-1}}n\sum_{k=0}^{n-1}
 F_k(u,v)F_{n-1-k}(u,v).
\]

By the independent root split, \(F_n(u,v)=\mathbb E[u^{L_n}v^{P_n}]\). In the exact coefficient distribution \(7!F_7\), the total coefficients for \(L=3\) and \(L=4\) are respectively \(2880\) and \(272\). With \(P\leq10\), the corresponding cumulative coefficient sums are \(0\) and \(80\); with \(P\leq11\), they are \(1040\) and \(80\). Division by those positive totals gives the four asserted conditional probabilities. Since their difference changes sign, neither conditional law is stochastically smaller than the other. A separate permutation enumeration checks these coefficient sums independently.

**Asymptotic correlation.** The path-length variance, obtainable by squaring the root-split recurrence, is

\[
\operatorname{Var}(P_n)=n(7n+13)-2(n+1)H_n-4(n+1)^2H_n^{(2)},
\]

where \(H_n^{(2)}=\sum_{j=1}^n j^{-2}\). Similarly, squaring the leaf recursion yields \(\operatorname{Var}(L_n)=2(n+1)/45\) for every \(n\geq4\). Consequently \(\operatorname{Var}(P_n)/n^2\to7-2\pi^2/3\) and \(\operatorname{Var}(L_n)/n\to2/45\). Combining these limits with the exact covariance proves the correlation limit.

## Verification

The standalone `verify.py` implements exact-fraction root-split moment recurrences through \(n=100\), an independent full bivariate distribution recurrence through \(n=8\), and direct exhaustive enumeration of the \(n!\) insertion orders through \(n=8\). It verifies the finite conditional-distribution crossing and the covariance formula without floating-point approximations. Run with `python verify.py`; only the Python standard library is required. The general assertion is proved analytically above; finite checks do not substitute for the proof.

## Relationship to prior work

Holmgren and Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Recursive Trees* (arXiv:1406.6883v1), give fringe-count limit laws and identify total path length as a growing-toll statistic outside the bounded-toll regime discussed there. Their Section 3 contains exact mixed covariances of **fixed** fringe-subtree counts, not the mixed leaf-count/whole-tree path-length law. Drmota and Hwang, *Profiles of Random Trees: Correlation and Width of Random Recursive Trees and Binary Search Trees* (2005), analyze dependence among depth-profile sizes, not the terminal-node count paired with their depth-weighted sum. A survey by Neininger and Rüschendorf treats multivariate path-length-related costs without the present leaf/path statistic. Earlier and more general tree-moment methods could conceivably imply the covariance after specialization; a literature search cannot establish absolute historical uniqueness.

## Limitations

The theorem is for ordinary random binary search trees with a uniform insertion order, not arbitrary search-tree distributions or recursive trees. The asymptotic correlation uses the classical second moments of path length and terminal leaf count. The exhibited crossing refutes an unrestricted stochastic order; it does not classify all finite-size conditional distribution comparisons. The claimed novelty is limited to the explicit finite-sample mixed covariance and its stochastic-order boundary, not to the underlying BST recurrences, classical variance laws, or general fringe-tree machinery. Historical priority is subject to undiscovered equivalent formulations.

## References

1. C. Holmgren and S. Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Recursive Trees*, arXiv:1406.6883v1 (26 June 2014), https://arxiv.org/html/1406.6883v1.
2. M. Drmota and H.-K. Hwang, *Profiles of Random Trees: Correlation and Width of Random Recursive Trees and Binary Search Trees*, *Advances in Applied Probability* **37** (2005), 321–341, https://doi.org/10.1017/S0001867800000203.
3. R. Neininger and L. Rüschendorf, *A Survey of Multivariate Aspects of the Contraction Method*, https://www.math.uni-frankfurt.de/~neiningr/multsur.pdf.
4. M. Bóna and B. Pittel, *On a Random Search Tree: Asymptotic Enumeration of Vertices by Distance from Leaves*, arXiv:1412.2796 (2014), https://arxiv.org/abs/1412.2796.
