# Exact leaf-parent orthogonality in uniform random recursive trees

## Finding

For a uniformly random recursive rooted tree on \(n\) labeled vertices, let \(L_n\) denote the number of leaves, \(P_n\) the number of protected vertices, and \(Q_n\) the number of distinct parents having a leaf child. The three classes partition the vertex set, and for every integer \(n\ge3\),
\[
\operatorname{Cov}(L_n,P_n)=-\frac n{12},\qquad
\operatorname{Cov}(L_n,Q_n)=0,\qquad
\operatorname{Var}(L_n)=\frac n{12}.
\]
The respective covariances and the variance are zero at \(n=1,2\). The zero covariance is **not** independence: for \(n=4\) the event \(L_4=3\) forces \(Q_4=1\), while \(Q_4=2\) also has positive probability.

The useful structural identity is a cancellation between an exact bivariate mixed derivative and a marginal derivative of the increasing-tree generating function. This gives the all-size covariance without asymptotic approximation.

## Assumptions and scope

A recursive tree on labels \(1,\ldots,n\) is rooted at 1 and every nonroot vertex \(j\) has a parent in \(\{1,\ldots,j-1\}\). Under the uniform model these parent choices are independent and uniformly distributed. There are exactly \((n-1)!\) trees for each \(n\ge1\).

A **leaf** has no children; a **protected vertex** has at least one child and no child that is a leaf; a **leaf parent** has at least one direct child that is a leaf. These conditions partition the vertices, so \(L_n+P_n+Q_n=n\) deterministically. In particular, a leaf parent is counted **once**, regardless of how many leaf children it has. The root is treated by these rooted definitions, not by undirected degree.

All probabilities are for a fixed tree size \(n\); claims apply to every integer \(n\ge1\), with the covariance formula explicitly beginning at \(n=3\).

## Proof

**Root decomposition.** Define the labeled exponential generating function, as a formal power series in \(z\),
\[
F(z,u,v)=\sum_{n\ge1}\frac{z^n}{n!}
\sum_{T\in\mathcal R_n}u^{L(T)}v^{P(T)},
\]
where \(\mathcal R_n\) is the set of recursive trees on \(n\) labels. An increasing-tree root has an unordered set of increasing child subtrees. The standard increasing-tree differential construction leads to
\[
\frac{\partial F}{\partial z}
=e^{F}+(u-1)+(v-1)\bigl(e^{F-uz}-1\bigr),\qquad F(0,u,v)=0.
\tag{1}
\]
Here the correction \(u-1\) marks a root with no children as a leaf. Among trees with a nonempty set of children, a root is protected exactly when none of its children is a singleton (a singleton subtree contributes \(uz\)); therefore the protected-root correction is \((v-1)(e^{F-uz}-1)\). This proves (1) directly from the definitions, including the singleton boundary.

At \(u=v=1\), the solution is \(F(z,1,1)=-\log(1-z)\). Put
\[
a(z)=F_u(z,1,1),\quad b(z)=F_v(z,1,1),\quad c(z)=F_{uv}(z,1,1).
\]
Formal differentiation of (1), with zero constant terms, gives
\[
\begin{aligned}
a'&=\frac{a}{1-z}+1,\\
b'&=\frac{b}{1-z}+\frac{e^{-z}}{1-z}-1,\\
c'&=\frac{c+ab}{1-z}+\frac{e^{-z}(a-z)}{1-z}.
\end{aligned}
\tag{2}
\]
In particular,
\[
a(z)=\frac{z(2-z)}{2(1-z)},\qquad
b(z)=\frac{1-e^{-z}-z+z^2/2}{1-z}.
\tag{3}
\]
Substitution of (3) into the last equation of (2), with \(c(0)=0\), yields the exact formal identity
\[
\boxed{\displaystyle c(z)=\frac z2 b'(z)-\frac{z^3}{12(1-z)}.}
\tag{4}
\]
For reproducibility one may verify (4) by differentiating both sides and substituting (2); both sides have constant coefficient zero. An explicit equivalent expression, useful for an independent substitution check, is
\[
c(z)=\frac{1}{4(1-z)^2}-\frac{z^2e^{-z}}{2(1-z)^2}
-\frac{1}{3(1-z)}+\frac{(1-z)^2}{12}.
\]

**Coefficient normalization and covariance.** Since \(|\mathcal R_n|=(n-1)!\), coefficient extraction gives
\[
\mathbb E L_n=n[z^n]a(z),\quad
\mathbb E P_n=n[z^n]b(z),\quad
\mathbb E(L_nP_n)=n[z^n]c(z).
\]
From (3), \(\mathbb E L_n=n/2\) for every \(n\ge2\). For \(n\ge3\), identity (4) implies
\[
\begin{aligned}
\mathbb E(L_nP_n)
&=n\left(\frac n2[z^n]b(z)-\frac1{12}\right)\\
&=\frac n2\mathbb E P_n-\frac n{12}.
\end{aligned}
\]
Consequently \(\operatorname{Cov}(L_n,P_n)=-n/12\). For reference, differentiating the second equation in (3) also gives
\[
\mathbb E P_n=n\left(\frac12-\sum_{j=0}^{n}\frac{(-1)^j}{j!}\right),\qquad n\ge2,
\]
consistent with the previously established expectation of protected nodes.

**Leaf variance.** For \(n\ge2\), when vertex \(n+1\) is added, let \(I_n\) indicate that its randomly chosen parent is currently a leaf. Conditionally on the tree,
\[
I_n\sim\operatorname{Bernoulli}(L_n/n),\qquad
L_{n+1}=L_n+1-I_n.
\]
Total variance and \(\mathbb E L_n=n/2\) give
\[
V_{n+1}=\left(1-\frac2n\right)V_n+\frac14,
\quad V_n:=\operatorname{Var}(L_n),\quad V_2=0.
\]
Thus \(V_3=1/4\), and induction establishes \(V_n=n/12\) for all \(n\ge3\).

Finally, the deterministic partition \(Q_n=n-L_n-P_n\) yields
\[
\operatorname{Cov}(L_n,Q_n)
=-\operatorname{Var}(L_n)-\operatorname{Cov}(L_n,P_n)=0.
\]
At \(n=1,2\), the leaf count is deterministic and both covariances vanish.

**Not independent.** On four labels the star with parent sequence \((1,1,1)\) has \((L_4,Q_4)=(3,1)\), and the tree with parent sequence \((1,1,2)\) has \((L_4,Q_4)=(2,2)\). Every rooted four-vertex tree with three leaves is a star, so \(\Pr(Q_4=2\mid L_4=3)=0\) while \(\Pr(Q_4=2)>0\).

## Verification

The accompanying standalone `verify_protected_leaves.py` uses exact rational arithmetic. It independently enumerates **46,233 trees** for sizes \(2\) through \(9\), checks all three displayed moment identities and the partition, then independently computes the coefficient recurrences (2) to degree \(120\), checking 118 degrees from \(3\) to \(120\). It also checks a nonindependence witness. Execute `python verify_protected_leaves.py` with Python 3 and no third-party dependencies. Finite enumeration corroborates but does not replace the formal power-series proof.

## Relationship to prior work

Devroye and Janson (2013) treat protected nodes as fringe-subtree statistics and establish limiting protected-node proportions for random recursive trees, among other classes. Mahmoud and Ward (2015) establish exact protected-node expectations and variance growth bounds for random recursive trees. Their mean formula is independently recovered by (3). The present assertion concerns **the exact finite-size cross-covariance with rooted leaves and exact orthogonality with the count of leaf parents**, rather than either marginal statistic or a limiting proportion.

Holmgren and Janson (2014/2015) develop general fringe-tree limit laws, which are closely relevant to joint asymptotic questions. Hartle and Krapivsky (2025/2026) study the leaf-degree distribution of growing trees, including a related zero-leaf-neighbor class. In the accessible inspected materials no statement establishing this exact finite-size covariance identity was found. Broader theoretical machinery may nonetheless imply it, so priority should not be interpreted as independently settled.

## Limitations

The theorem applies to **rooted** uniform recursive trees, not arbitrary random trees and not the undirected degree-one convention at the root. It states zero covariance, not independence or conditional independence; the nonindependence witness is explicit. No claim of a joint central limit theorem, a universal behavior under nonuniform attachment, or a sign law for general nonlinear transforms is made. The originality assessment is limited by inaccessible full text of some related studies; independent literature audit has not been performed.

## References

1. Luc Devroye and Svante Janson, *Protected nodes and fringe subtrees in some random trees*, arXiv:1310.0665v1 (first posted 2 October 2013).
2. Hosam M. Mahmoud and Mark D. Ward, *Asymptotic Properties of Protected Nodes in Random Recursive Trees*, Journal of Applied Probability 52 (2015), 290–297, DOI:10.1239/jap/1429282623.
3. Cecilia Holmgren and Svante Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Random Recursive Trees*, arXiv:1406.6883 (2014); Electronic Journal of Probability 20 (2015), DOI:10.1214/EJP.v20-3627.
4. Harrison Hartle and P. L. Krapivsky, *Statistics of leaves in growing random trees*, arXiv:2511.04085 (first posted 6 November 2025); Journal of Statistical Mechanics (2026), DOI:10.1088/1742-5468/ae3a6a.
