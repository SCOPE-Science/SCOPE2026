# Exact negative root-degree–path-length covariance in uniform plane trees

## Finding
For each integer \(n\ge2\), take the uniform distribution over the \(C_{n-1}=\frac1n\binom{2n-2}{n-1}\) ordered rooted trees with \(n\) vertices. Write \(D_n\) for root outdegree and \(P_n\) for the sum of graph distances from the root to every vertex, with root depth zero. Define \(B_n=\binom{2n}{n}\) and \(A_n=\frac{(2n-1)4^n}{4B_n}\). Their mixed first moment and two means are
\[
\mathbb E D_n=\frac{3(n-1)}{n+1},\qquad
\mathbb E P_n=A_n-\frac n2,\qquad
\mathbb E[D_nP_n]=3A_n-\frac{7n-4}2.
\]
Hence the **exact finite-size covariance** is
\[
\operatorname{Cov}(D_n,P_n)
=\frac{\frac32(2n-1)4^n/B_n-2n^2-3n+2}{n+1}.
\]
It vanishes for \(n=2\), is **strictly negative** for every \(n\ge3\), and satisfies
\[
\operatorname{Cov}(D_n,P_n)
=-2n+3\sqrt{\pi n}-1+O(n^{-1/2}).
\]
The result quantifies finite-size dependence of the number of primary root branches and aggregate depth. Its negative sign is not inferred merely from the intuition that more root branches yield shallower trees; it follows from an exact binomial-coefficient inequality proved below.

## Assumptions and scope
A rooted plane tree has ordered children; different child orders define distinct objects. All \(C_{n-1}\) plane trees of size \(n\) receive equal probability. The root contributes zero to \(P_n\). There are no edge weights, no vertex labels and no implicit conditioning on height or root degree. The theorem covers every integer \(n\ge2\) and does not concern random recursive trees or binary-search trees. The covariance uses unnormalized \(P_n\), not average vertex depth; the covariance for mean depth is obtained by division by \(n\).

## Proof
Let \(T(z)=\sum_{n\ge1}C_{n-1}z^n\) be the plane-tree ordinary generating function. Root decomposition into an ordered list of children gives \(T=z/(1-T)\), so with \(s=\sqrt{1-4z}\) one has \(T=(1-s)/2\), \(z=T(1-T)\), and \(T'=1/(1-2T)\).

Define \(F(z)=\sum_{\mathcal T}P(\mathcal T)z^{|\mathcal T|}\). For a root with ordered subtrees \(\mathcal T_1,\ldots,\mathcal T_k\),
\[
P(\mathcal T)=\sum_{i=1}^k\bigl(P(\mathcal T_i)+|\mathcal T_i|\bigr).
\]
Consequently
\[
F=\frac{z(F+zT')}{(1-T)^2},\qquad
F=\frac{T^2(1-T)}{(1-2T)^2}
=\frac18\left(s^{-2}-s^{-1}-1+s\right).
\]
The generating functions marking root outdegree and root-outdegree-weighted path length are, respectively,
\[
G_D(z)=z\sum_{k\ge0}kT^k=\frac{T^2}{1-T},
\]
and
\[
G_{DP}(z)=z\sum_{k\ge0}k^2T^{k-1}(F+zT')
=\frac{T^2(1+T)}{(1-2T)^2}
=\frac18\left(3s^{-2}-7s^{-1}+5-s\right).
\]
Here \(F+zT'=T(1-T)^2/(1-2T)^2\). The identities are formal power-series identities; differentiation and root marking are legitimate termwise for \(|z|<1/4\) as well.

For \(n\ge2\), \([z^n]s^{-2}=4^n\), \([z^n]s^{-1}=\binom{2n}{n}=B_n\), and \([z^n]s=-B_n/(2n-1)\). Also \([z^n]T=C_{n-1}=B_n/[2(2n-1)]\). Using \(G_D=T/z+(s-3)/2\), we obtain \([z^n]G_D=C_n-C_{n-1}\). Dividing these four coefficients by \(C_{n-1}\) gives the stated means, mixed moment and covariance, with no asymptotic approximation.

For strict negativity set
\[
r_n=\frac{4^n}{B_n},\qquad
h_n=\frac{2(2n^2+3n-2)}{3(2n-1)}.
\]
The covariance is negative exactly when \(r_n<h_n\). At \(n=3\), \(r_3=16/5<h_3=10/3\). For integers \(n\ge3\), elementary cancellation yields
\[
\frac{r_{n+1}}{r_n}=\frac{2(n+1)}{2n+1},\qquad
\frac{h_{n+1}}{h_n}-\frac{r_{n+1}}{r_n}
=\frac{n-1}{(n+2)(2n+1)}>0.
\]
Induction proves \(r_n<h_n\) for every \(n\ge3\). At \(n=2\), the sole ordered rooted two-vertex tree is deterministic, so the covariance is zero. Finally, the central binomial expansion \(4^n/B_n=\sqrt{\pi n}(1+1/(8n)+O(n^{-2}))\), substituted in the exact identity, proves the stated \(-2n+3\sqrt{\pi n}-1+O(n^{-1/2})\) expansion.

## Verification
The standalone standard-library script `verify_plane_tree.py` exhaustively enumerates all plane trees of orders \(2\) through \(9\), independently computes their root degrees, path lengths and empirical rational moments, and compares them with all exact formulas. It additionally checks rational moment consistency for orders up to \(1200\), the inductive sign comparison up to \(700\), and three large-order asymptotic comparisons. In its tested execution it reported 3837 passing checks. These finite checks are corroboration, not an infinite proof; the proof above supplies the infinite assertion.

## Relationship to prior work
Janson's *The Wiener Index of Simply Generated Random Trees* (2003, DOI `10.1002/rsa.10074`) studies the internal path length jointly with the Wiener index and derives Brownian-excursion limits and mixed moments of those two quantities; it does not state the present root-outdegree/path-length covariance. Janson's *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation* (arXiv `1112.0510v1`, 2011) treats ordered trees as conditioned geometric Galton–Watson trees and analyzes the root degree, but not its joint finite-size covariance with internal path length. Those sources supply foundational objects and separate marginal theory, rather than a stronger implication covering this mixed statistic. Similar statements about root attachment and path length in random recursive trees apply to a different probability law and do not imply the uniform-plane-tree identity.

The equivalent Dyck-path formulation counts primitive factors and sums tree depths (related to the Dyck path area), but none of the inspected statements gave this finite-size covariance and all-order sign proof. General bivariate tree generating-function methods could potentially imply it upon additional differentiation; priority has not been independently established.

## Limitations
The theorem is limited to the uniform plane-tree law; it does not assert monotonicity of \(\mathbb E[P_n\mid D_n=k]\) in every root degree or any stochastic order. Its conclusion is an exact covariance, not independence or a joint limit theorem. The originality assessment relies on the specific full-text and database comparisons recorded separately; unnamed older Dyck-path area enumerations could conceal an equivalent identity. Independent scientific audit has not been performed.

## References
1. S. Janson, *The Wiener Index of Simply Generated Random Trees*, Random Structures & Algorithms 22 (2003), 337–358. DOI `10.1002/rsa.10074`; publisher lists first-publication date 2003-03-03.
2. S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv `1112.0510v1`, first publicly submitted 2011-12-02; especially Example 9.1 and Section 14.
3. R. Sedgewick and P. Flajolet, *An Introduction to the Analysis of Algorithms*, chapter 6, average path length in Catalan trees (public online chapter: `https://aofa.cs.princeton.edu/60trees/`; limited access to full HTML in this review).
