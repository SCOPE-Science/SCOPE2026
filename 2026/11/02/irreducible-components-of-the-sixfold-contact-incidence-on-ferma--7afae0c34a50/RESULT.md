# Irreducible components of the sixfold-contact incidence on Fermat fourfolds

## Finding
Let \(d\geq 6\) be an integer and let \(X_d\subset\mathbb P^5_{\mathbb C}\) be the smooth Fermat hypersurface
\[
X_d=\{[x_0:\cdots:x_5]:\textstyle\sum_{i=0}^{5}x_i^d=0\}.
\]
Let \(V_6(X_d)\) be the scheme of pointed projective lines \((p,\ell)\), with \(p\in X_d\cap\ell\), for which the intersection multiplicity at \(p\) is at least six (and lines contained in \(X_d\) have infinite contact). Then
\[
\boxed{\#\operatorname{Irr}\bigl(V_6(X_d)_{\mathrm{red}}\bigr)=15d^3+45d^2+90d+51.}
\]
Every irreducible component has dimension three. These components admit a complete classification by disjoint, nonempty coordinate blocks with at least two coordinates each, as described below. For every \(6\leq j\leq d\), the reduced pointed-contact loci coincide:
\[
V_6(X_d)_{\mathrm{red}}=V_j(X_d)_{\mathrm{red}}.
\]
Thus a line has either contact order at most five, contact order exactly \(d\), or lies entirely in \(X_d\): no finite intermediate contact order occurs.

## Assumptions and scope
Everything is over \(\mathbb C\). The ambient projective space has exactly six homogeneous coordinates, the degree satisfies \(d\ge6\), and components refer to irreducible components of the **reduced** pointed-line incidence, not its multiplicity or scheme structure. A line is a two-dimensional vector subspace of \(\mathbb C^6\); a pointed line is a line with a specified point. The incidence is closed inside the universal line over \(\operatorname{Gr}(2,6)\).

A *partial block partition* \(\mathcal P=\{S_1,\ldots,S_k\}\) consists of pairwise disjoint subsets \(S_a\subset\{0,1,2,3,4,5\}\), each of cardinality at least two. Put \(T=\bigcup S_a\) and \(R=\{0,\ldots,5\}\setminus T\). Exclude the single-block full-support choice \(\mathcal P=\{\{0,\ldots,5\}\}\). Write \(p_{S_a}\) for the vector obtained by restricting a lift of \(p\) to coordinates in \(S_a\) and zeroing the others.

For each permitted \(\mathcal P\), take points \(p\) satisfying \(p_i=0\) for \(i\in R\), \(p_i\ne0\) for \(i\in T\), and
\[
\sum_{i\in S_a}p_i^d=0\quad(a=1,\ldots,k).
\]
Choose a nonzero line direction modulo \(p\) represented by
\[
v=\sum_{a=1}^k\lambda_a p_{S_a}+w,\qquad w\in\mathbb C^R.
\]
Let \(Z_{\mathcal P}\) be the closure of the resulting pointed-line family. When a block \(S_a\) has size two, its Fermat equation has exactly \(d\) reduced projective solutions, and one must take a separate irreducible component for each such choice. The resulting irreducible subfamilies are all and only the irreducible components of \(V_6(X_d)_{\mathrm{red}}\).

## Proof
**1. Moment equations.** Let \((p,\ell)\in V_6(X_d)\) and choose lifts \(p,v\in\mathbb C^6\) spanning \(\ell\), with \(p\ne0\). Put \(T=\{i:p_i\ne0\}\), and on \(T\) define \(\lambda_i=v_i/p_i\) and \(b_i=p_i^d\). Expanding the Fermat equation along \(p+tv\) gives, for \(0\le j\le5\),
\[
[t^j]\sum_{i=0}^{5}(p_i+tv_i)^d
 =\binom dj\sum_{i\in T}b_i\lambda_i^j.
\]
The case \(j=0\) holds because \(p\in X_d\); the remaining five equations vanish by the sixfold-contact condition. Let the distinct values among the \(\lambda_i\) be \(\mu_1,\ldots,\mu_k\), and let \(S_a=\{i\in T:\lambda_i=\mu_a\}\). Then
\[
\sum_{a=1}^k\mu_a^jB_a=0\quad(0\le j\le5),\qquad B_a=\sum_{i\in S_a}b_i.
\]
Since \(k\le|T|\le6\), the first \(k\) rows form a square Vandermonde matrix with determinant \(\prod_{a<b}(\mu_b-\mu_a)\ne0\). Therefore \(B_a=0\) for every \(a\). Each block has at least two indices: an individual nonzero \(b_i\) cannot sum to zero. Because \(v\) is independent of \(p\), the excluded choice \(k=1,T=\{0,\ldots,5\}\) cannot occur.

**2. Converse and contact gap.** For any permitted blocks, equations \(\sum_{i\in S_a}p_i^d=0\) and direction \(v=\sum_a\lambda_a p_{S_a}+w\), with \(w\) supported on \(R\), give the exact polynomial identity
\[
\sum_{i=0}^{5}(p_i+tv_i)^d
 =\sum_a(1+t\lambda_a)^d\underbrace{\sum_{i\in S_a}p_i^d}_{0}
    +t^d\sum_{i\in R}w_i^d
 =t^d\sum_{i\in R}w_i^d.
\]
Thus every such line has contact at least \(d\), and every line with contact at least six occurs in one such family. If the last sum is zero the line is contained in \(X_d\); otherwise the contact order is exactly \(d\). This proves the asserted equality of reduced contact loci and the contact-order gap.

**3. Irreducibility and dimension.** Fix a partial partition and choose separately a root component for each size-two block. The base of allowed marked points, where every coordinate in \(T\) is nonzero, is an irreducible open subset of the projectivization of a product of affine Fermat cones. For a block of size at least three, the Fermat cone is irreducible (its positive-dimensional projective hypersurface is smooth); for a size-two block the chosen linear factor defines an irreducible cone. Its projective dimension is \(|T|-k-1\). The space of allowable line directions modulo the marked point is a projective space of dimension \(k+|R|-2\). Hence each family is irreducible of dimension
\[
(|T|-k-1)+(k+6-|T|-2)=3.
\]
The closures cover \(V_6(X_d)_{\mathrm{red}}\) by step 1. They are pairwise distinct: for a generic point of each family, the support \(T\) is exactly recoverable from \(p\), all \(\lambda_a\) can be chosen pairwise distinct, and the partition is recoverable as the equality classes of the ratios \(v_i/p_i\). Changing \(v\) by a multiple of \(p\) shifts all these ratios by the same constant, so their equality classes are intrinsic. Different root choices in size-two blocks are distinguished by the ratios of the marked-point coordinates. Thus all these three-dimensional irreducible closures are exactly the irreducible components.

**4. Component census.** A block of size two contributes \(d\) irreducible choices; a block of size three or more contributes one. The allowed block-size shapes, with counts *before* choices of pair roots, are
\[
\begin{array}{c|rrrrrrrrr}
\text{blocks}&(2)&(3)&(4)&(5)&(2,2)&(2,3)&(2,4)&(3,3)&(2,2,2)\\
\text{number}&15&20&15&6&45&60&15&10&15
\end{array}.
\]
Their weighted sum is
\[
15d+20+15+6+45d^2+60d+15d+10+15d^3
=15d^3+45d^2+90d+51.
\]
There is no single full-support block because it yields only the zero direction modulo \(p\). This exhausts the partial partitions and proves the formula.

## Verification
Run \(\texttt{python3 verify_components.py}\) using the supplied stand-alone standard-library Python program. It independently enumerates unordered set partitions of coordinate subsets, filters the geometric admissibility conditions, tabulates block shapes and the root-choice weighted polynomial, tests numerical specializations \(d=6,7,8\), and checks small exact Vandermonde determinants. The executable output ends in \(\texttt{VERIFY_OK}\). The symbolic Vandermonde argument and irreducibility reasoning above, not finite tests, prove the theorem for every \(d\ge6\).

## Relationship to prior work
Beheshti and Mukhopadhyay, *Higher-order tangent lines to smooth hypersurfaces* (arXiv:2610.28558v1, posted 2026-10-20), show that the sixfold-contact incidence of any smooth hypersurface of degree at least five in \(\mathbb P^5\) has dimension three, and mention the \(15d^3\) planes on Fermat hypersurfaces. Their statement does not describe the complete irreducible-component decomposition for Fermat hypersurfaces; the present computation classifies the pointed-contact components, including lines **not** contained in the hypersurface. Earlier work by Patel, Riedl, Smith and Tseng (*Lines highly tangent to a hypersurface*, arXiv:2208.04393) analyzes high-contact incidence and proves a dimension result at order five; it does not imply this Fermat-specific component census. Literature on Fermat curves and their osculating curves concerns a different ambient dimension and different incidence. The \(15d^3\) plane contribution is classical and is not claimed as new.

## Limitations
The statement is set-theoretic/reduced and does not compute the multiplicity, embedded structure, normalization, or intersections of irreducible components of the nonreduced contact scheme. It is restricted to the Fermat polynomial in six variables in characteristic zero and degree at least six. No claim is made for general smooth degree-\(d\) hypersurfaces or for contact orders below six. Literature-priority comparisons were bounded and cannot establish absolute novelty.

## References
1. R. Beheshti and S. Mukhopadhyay, *Higher-order tangent lines to smooth hypersurfaces*, arXiv:2610.28558v1 (2026-10-20), https://arxiv.org/html/2610.28558v1.
2. A. Patel, E. Riedl, G. Smith, D. Tseng, *Lines highly tangent to a hypersurface*, arXiv:2208.04393v1 (2022-08-08), https://arxiv.org/abs/2208.04393.
3. T. K. Moe and N. P. A. Toft, *The Fermat curves, arrangements of lines, and intersections of osculating curves*, arXiv:2412.16993v2 (2025-05-07), https://arxiv.org/html/2412.16993v2.
