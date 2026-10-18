# Entropy law and opposite contact transitions for the canonical ellipsoids of direct sums

## Finding
Let \(k\ge2\), and let \(B_i\subset\mathbb R^{d_i}\) be origin-symmetric full-dimensional convex bodies, with \(d_i\ge1\), \(N=\sum_i d_i\), and \(w_i=d_i/N\). Write \(J_i\) and \(L_i\) for their unique John (maximum-volume inscribed) and Löwner (minimum-volume enclosing) ellipsoids. For \(1\le p\le\infty\), set
\[
K_p=\{(x_1,\ldots,x_k):\|(\|x_1\|_{B_1},\ldots,\|x_k\|_{B_k})\|_{\ell_p}\le1\},
\]
where \(\|\cdot\|_{B_i}\) is the Minkowski gauge. Define \(E_1\oplus_2\cdots\oplus_2 E_k\) as the centered ellipsoid \(\sum_i\|x_i\|_{E_i}^2\le1\). With \(t=|1/p-1/2|\) and \(1/\infty=0\), the *unique* canonical ellipsoids of \(K_p\) are
\[
\begin{array}{c|cc}
 &J(K_p)&L(K_p)\\\hline
1\le p<2&\displaystyle\bigoplus_{2,i} w_i^{1/p-1/2}J_i&\displaystyle\bigoplus_{2,i}L_i\\
p=2&\displaystyle\bigoplus_{2,i}J_i&\displaystyle\bigoplus_{2,i}L_i\\
2<p\le\infty&\displaystyle\bigoplus_{2,i}J_i&\displaystyle\bigoplus_{2,i}w_i^{1/p-1/2}L_i
\end{array}
\]
Consequently, with \(H(w)=-\sum_iw_i\log w_i\),
\[
\boxed{\frac{\operatorname{vol}L(K_p)}{\operatorname{vol}J(K_p)}
=\left(\prod_i\frac{\operatorname{vol}L_i}{\operatorname{vol}J_i}\right)
\exp\bigl(NH(w)|1/p-1/2|\bigr).}
\]
The canonical-ellipsoid volume ratio has its unique minimum over \(1\le p\le\infty\) at \(p=2\), with a strict cusp in the reciprocal-exponent variable \(1/p\).

The result also gives the *complete contact sets*. Put \(C_i^J=\partial B_i\cap\partial J_i\) and \(C_i^L=\partial B_i\cap\partial L_i\). For \(p<2\), every John contact, and no other, is \((w_1^{1/p}y_1,\ldots,w_k^{1/p}y_k)\) with \(y_i\in C_i^J\), whereas every Löwner contact has exactly one active block, belonging to \(C_i^L\). For \(p>2\), the roles reverse: every John contact has exactly one active block from \(C_i^J\), while every Löwner contact is \((w_i^{1/p}y_i)_i\) with \(y_i\in C_i^L\), including the endpoint \(p=\infty\). At \(p=2\), John and Löwner contacts are exactly the vectors \((r_iy_i)_i\) satisfying \(r_i\ge0\), \(\sum_i r_i^2=1\), with \(y_i\in C_i^J\) or \(C_i^L\) respectively whenever \(r_i>0\). Each asserted contact family is nonempty.

## Assumptions and scope
Each \(B_i\) is a compact centrally symmetric convex body containing \(0\) in its interior. All volumes use Lebesgue measure in the indicated fixed Euclidean coordinates. The direct-sum decomposition uses the standard orthogonal product Euclidean structure; the theorem is affine-covariant under separate invertible transformations of the blocks. The result applies to all integer block dimensions, arbitrary numbers of blocks \(k\ge2\), and the full closed exponent range including \(p=1\) and \(p=\infty\). No smoothness, strict convexity, or polyhedral hypothesis is required.

## Proof
**1. Block structure.** Each independent block sign change \(x_i\mapsto-x_i\) preserves \(K_p\). Uniqueness of the John and Löwner ellipsoids, together with central symmetry, forces both centers to be the origin and their quadratic forms to have zero off-block entries. Thus every candidate canonical ellipsoid has the form \(E_1\oplus_2\cdots\oplus_2E_k\) for positive-definite centered block ellipsoids \(E_i\). This reduction does not assume any additional symmetry inside a block.

**2. Exact John containment.** For such an ellipsoid \(E\), put \(a_i=\max\{\|x\|_{B_i}:x\in E_i\}\). These positive maxima are attained. The largest \(p\)-power of the \(K_p\)-gauge on \(E\) is exactly
\[
\max_{r_i\ge0,\,\sum_i r_i^2\le1}\sum_i(a_ir_i)^p
\]
for finite \(p\), and is \(\max_i a_i\) for \(p=\infty\). Exactness follows because the maximizing block vectors can be chosen independently. For \(1\le p<2\), Hölder's inequality gives the maximum \((\sum_i a_i^q)^{p/q}\) with \(q=2p/(2-p)\). For \(p\ge2\) it is \((\max_i a_i)^p\). Hence containment holds exactly when \(\sum_i a_i^q\le1\) for \(p<2\), and when every \(a_i\le1\) for \(p\ge2\).

As \(E_i\subseteq a_iB_i\), uniqueness of \(J_i\) gives \(\operatorname{vol}(E_i)\le a_i^{d_i}\operatorname{vol}(J_i)\), with equality exactly at \(E_i=a_iJ_i\). The volume of the orthogonal ellipsoid sum is \(\kappa_N\prod_i\operatorname{vol}(E_i)/\kappa_{d_i}\), where \(\kappa_m\) denotes the Euclidean unit-ball volume. For \(p<2\), weighted arithmetic-geometric mean (or a Lagrange multiplier with a strictly concave log objective) shows that \(\prod_i a_i^{d_i}\), subject to \(\sum_i a_i^q\le1\), has its *unique* maximizer at \(a_i^q=d_i/N=w_i\). For \(p\ge2\), the unique maximizer is \(a_i=1\). This proves both John formulas and uniqueness of every block.

**3. Exact Löwner containment.** Write \(G=\bigoplus_{2,i}G_i\) and \(c_i=\max\{\|y\|_{G_i}:y\in B_i\}\). Then \(B_i\subseteq c_iG_i\), so \(\operatorname{vol}(G_i)\ge c_i^{-d_i}\operatorname{vol}(L_i)\), with equality exactly for \(G_i=c_i^{-1}L_i\). Independently choosing norm-attaining vectors shows that \(K_p\subseteq G\) if and only if
\[
\max_{s_i\ge0,\,\|(s_i)_i\|_{\ell_p}\le1}\sum_i(c_is_i)^2\le1.
\]
For \(p\le2\), the maximum is \(\max_i c_i^2\). For \(2<p\le\infty\), it is \((\sum_i c_i^q)^{2/q}\), where \(q=2p/(p-2)\) and \(q=2\) at \(p=\infty\). The same strictly optimal product calculation, now *minimizing* \(\prod_i c_i^{-d_i}\), gives \(c_i=1\) when \(p\le2\), and \(c_i^q=w_i\) when \(p>2\). This proves the Löwner formulas including both endpoints. Equivalently the Löwner statement also follows by polar duality from the John statement and \((K_p)^\circ=(B_1^\circ)\oplus_{p^*}\cdots\oplus_{p^*}(B_k^\circ)\).

**4. Equality and contacts.** A contact between \(J(K_p)\) and \(K_p\) must make every inequality in step 2 an equality, including each active block's \(\|x_i\|_{B_i}\le a_i\|x_i\|_{E_i}\). For \(p<2\), strict Hölder equality uniquely fixes \(r_i^2=w_i>0\), and hence \(x_i=a_ir_iy_i=w_i^{1/p}y_i\) with \(y_i\in C_i^J\). For \(p>2\), strict \(\ell_p\)-versus-\(\ell_2\) equality forces exactly one \(r_i=1\), giving a sole factor contact. At \(p=2\), any Euclidean unit radius vector works, provided each active block contacts. The corresponding three Löwner contact descriptions follow from the equalities in step 3: for \(p<2\), only one \(s_i=1\) is possible; for \(2<p<\infty\), strict Hölder equality gives \(s_i^p=w_i\), while at \(p=\infty\) all \(s_i=1\); at \(p=2\), arbitrary Euclidean unit radii work. These equality arguments apply at \(p=1\) and \(p=\infty\) by the explicit maximal-norm expressions. Factor contact sets are nonempty because their canonical ellipsoids touch the boundary, so all displayed families occur.

**5. Volume and entropy.** The common \(\kappa_N/\prod_i\kappa_{d_i}\) volume factor cancels when the Löwner volume is divided by the John volume. In either regime, the remaining scale multiplier is \(\prod_i w_i^{-d_i|1/p-1/2|}\), which equals \(\exp(NH(w)|1/p-1/2|)\). Since \(k\ge2\) and all \(w_i>0\), \(H(w)>0\), proving strict minimization and the claimed cusp.

## Verification
The derivation needs only finite-dimensional uniqueness of John/Löwner ellipsoids, Hölder's inequality, and its equality conditions; no finite computation is used as an infinite-dimensional proof. The standalone `checker.py` tests the precise dimension-weighted Hölder normalization and entropy identity for three unequal block-dimension vectors and eight values of \(p\) (including both endpoints), plus 36,000 seeded independent scalar feasibility tests. It uses only Python's standard library. Execute `python3 checker.py` from the extracted package. The tested inequalities support—but do not replace—the analytical equalities proved above.

## Relationship to prior work
John's classical ellipsoid theorem and its known polar Löwner analogue provide the uniqueness and contact-condition framework. Ivanov–Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions* (arXiv:2212.11781, first submitted 2022-12-22), investigates general optimization conditions for functional and geometric positions, but does not specialize them to exact dimension-weighted formulas and the complete block-contact structure of finite \(\ell_p\)-direct sums. Grundbacher–Kobos, *Exact Banach–Mazur distances of certain \(\ell_p\)-sums and cones* (arXiv:2603.18268, first submitted 2026-03), proves an all-block Banach–Mazur distance formula and uses related Hölder inequalities. Banach–Mazur distance minimizes a *radius ratio under a change of position*, whereas the John and Löwner ellipsoids independently optimize *volumes* in the given affine coordinates; its Theorem 1.1 does not specify the two volume-optimal ellipsoids or classify their boundary contacts. The new contribution asserted here is the simultaneous exact canonical-ellipsoid construction, complete opposite contact localization, and dimension-entropy identity, **not** the underlying Hölder inequality or the general contact condition.

## Limitations
The statement assumes separate origin symmetry of every block; the proof does not apply unchanged to arbitrary nonsymmetric summands or non-orthogonal coupled norms. It determines only canonical ellipsoids, their boundary contacts, and their volume ratio, not the Banach–Mazur optimizing ellipsoid in general. Classical literature on normed-space direct sums is extensive, so an earlier equivalent combination of the formula and full contact characterization may exist under different terminology. Independent external mathematical validation has not occurred.

## References
1. F. John, *Extremum problems with inequalities as subsidiary conditions*, 1948 (classical extremal-ellipsoid characterization).
2. G. Ivanov and M. Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781, initial public version 2022-12-22, https://arxiv.org/html/2212.11781v2 .
3. F. Grundbacher and T. Kobos, *Exact Banach–Mazur distances of certain \(\ell_p\)-sums and cones*, arXiv:2603.18268, initial public version March 2026, https://arxiv.org/html/2603.18268v1 .
4. B. Klartag, *On John-Type Ellipsoids*, arXiv:math/0312065, initial public version 2003-12-02, https://arxiv.org/html/math/0312065v1 .
