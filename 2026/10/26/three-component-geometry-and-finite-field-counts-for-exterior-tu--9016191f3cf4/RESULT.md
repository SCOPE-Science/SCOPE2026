# Three-component geometry and finite-field counts for exterior tuples in a four-step flag

## Finding

Let \(k\) be any algebraically closed field and \(\mathfrak n_4(k)\) the associative algebra of strictly upper-triangular \(4\times4\) matrices. For every integer \(r\geq2\), the **reduced** variety
\[
\mathcal E_r(k)=\{(X_1,\ldots,X_r)\in\mathfrak n_4(k)^r:\ X_i^2=0\ (1\leq i\leq r),\quad X_iX_j+X_jX_i=0\ (i<j)\}
\]
has **exactly three geometrically irreducible, rational components**, one of dimension \(4r\) and two of dimension \(3r+1\). This is valid in **every characteristic**, including characteristic two. It is the variety of fixed-complete-flag, strictly nilpotent representations of the exterior algebra on \(r\) generators, with the convention that generator squares vanish also in characteristic two.

More precisely, writing the six strictly upper-triangular entries of each matrix as \((a_i,b_i,c_i,d_i,e_i,f_i)=(X_{i,12},X_{i,23},X_{i,34},X_{i,13},X_{i,24},X_{i,14})\), assemble each four-tuple into
\[
H_i=\begin{pmatrix}a_i&d_i\\-c_i&e_i\end{pmatrix}.
\]
The components are (i) the linear locus \(L\) with all \(a_i=c_i=0\), (ii) the locus \(C_{\mathrm{im}}\) with all \(b_i=0\) and all \(H_i\) having a **common image line**, and (iii) the locus \(C_{\mathrm{ker}}\) with all \(b_i=0\) and all \(H_i\) having a **common kernel line**. Zero matrices are allowed, so the incidence conditions are understood by existence of a line rather than by a uniquely determined line at degenerate points.

The pairwise component intersections have dimensions
\[
\dim(L\cap C_{\mathrm{ker}})=3r,\quad
\dim(L\cap C_{\mathrm{im}})=2r+1,\quad
\dim(C_{\mathrm{im}}\cap C_{\mathrm{ker}})=2r+2.
\]
The triple intersection is \(L\cap C_{\mathrm{im}}\), of dimension \(2r+1\). Consequently \(\mathcal E_r\) is non-equidimensional for all \(r\ge2\).

For **every** finite field \(\mathbb F_q\), of arbitrary characteristic, and every integer \(r\ge1\), the exact number of such ordered tuples is
\[
\boxed{N_r(q)=q^{4r}-q^{3r}+q^r\bigl[1+(q+1)^2(q^r-1)+2(q+1)(q^r-1)(q^r-q)\bigr].}
\]
This arithmetic statement includes the one-generator case; the three-component geometric assertion begins at two generators.

## Assumptions and scope

The algebra \(\mathfrak n_4(k)\) is the six-dimensional **associative**, nonunital matrix algebra, rather than the full algebra of all nilpotent matrices or the upper-triangular algebra with diagonal entries. A tuple is admitted precisely when **both** the square relations and the pairwise anticommutator relations hold. For characteristic two these relations become commuting-plus-square-zero, and the square-zero condition is not redundant. Geometric claims concern the reduced affine variety, not its potentially nonreduced coordinate scheme. The integer \(r\) is arbitrary with the bounds stated above.

## Proof

### 1. Complete equations and the linear branch

For a matrix whose nonzero coordinates are \((a,b,c,d,e,f)\) in the specified order, multiplication gives only three potentially nonzero entries:
\[
(X_iX_j)_{13}=a_ib_j,\qquad (X_iX_j)_{24}=b_ic_j,\qquad (X_iX_j)_{14}=a_ie_j+d_ic_j.
\]
Hence the square and anticommutation relations, **without division by two**, are the equations
\[
\begin{aligned}
&a_ib_i=b_ic_i=a_ie_i+d_ic_i=0 &&(1\le i\le r),\\
&a_ib_j+a_jb_i=b_ic_j+b_jc_i=0 &&(i<j),\\
&a_ie_j+a_je_i+d_ic_j+d_jc_i=0 &&(i<j).
\end{aligned}
\]
If \(b_h\ne0\) for some index \(h\), the diagonal equations give \(a_h=c_h=0\); the cross equations with index \(h\) then give \(a_j=c_j=0\) for every \(j\). If all \(b_i=0\) we are in the complementary branch. Therefore the set of solutions is exactly \(L\cup\{b_i=0\ \forall i,\ \det H(t)=0\ \forall t\in k^r\}\), where \(L=\{a_i=c_i=0\ \forall i\}\) and \(H(t)=\sum_i t_iH_i\). Indeed, \(\det H_i=a_ie_i+d_ic_i\), and its mixed polarization coefficients are the third displayed cross equations. This equivalence works in every characteristic because the coefficients of \(t_i^2\) are separately imposed by the square relations.

The \(r\) coordinates \(f_i\) never occur in the equations. The linear space \(L\) has free coordinates \((b_i,d_i,e_i,f_i)\) and is therefore irreducible of dimension \(4r\).

### 2. A rank-one matrix-subspace lemma

**Lemma.** If \(W\subseteq M_2(k)\) is a linear subspace whose matrices all have rank at most one, then either their images lie in a fixed line of \(k^2\), or their kernels contain a fixed line of \(k^2\). The zero subspace satisfies both alternatives.

**Proof.** Pick a nonzero \(uv^T\in W\). If \(u'v'^T\in W\) is nonzero, the identity \(\det(uv^T+u'v'^T)=0\) forces \(u'\) proportional to \(u\), or \(v'\) proportional to \(v\). If both an element with new image and an element with new row line existed, the sum of those two elements would have rank two; indeed, their image and row directions would both be independent. Hence all nonzero matrices use the same image direction or all use the same row direction. \(\square\)

Apply this lemma to \(W=\mathrm{span}\{H_1,\dots,H_r\}\). The determinant equations established in Step 1 say exactly that \(W\) is such a rank-at-most-one subspace. Thus the branch \(b=0\) splits into precisely \(C_{\mathrm{im}}\cup C_{\mathrm{ker}}\).

### 3. Components, dimensions, rationality and intersections

For each image line \(\ell\in\mathbb P^1(k)\), the space of matrices with image contained in \(\ell\) has dimension two; choosing \(r\) such matrices and the \(r\) free central coordinates gives a rank-\(3r\) vector bundle over \(\mathbb P^1\). Its proper incidence projection has closed image \(C_{\mathrm{im}}\). The projection is generically one-to-one for \(r\ge2\), since a generic tuple spans a two-dimensional space of matrices and determines its image line. Thus \(C_{\mathrm{im}}\) is geometrically irreducible, rational and of dimension \(3r+1\). The identical argument for kernel lines proves the same assertions for \(C_{\mathrm{ker}}\). All constructions are defined over the prime field, so geometric irreducibility is uniform in characteristic.

The two ruling components are different for \(r\ge2\): matrices with two independent row directions but a common image have no common kernel, and the transposed example has common kernel but not common image. Neither is contained in \(L\), because each has points with some \(a_i\) or \(c_i\) nonzero. Conversely, \(L\) has points with some \(b_i\ne0\), which neither ruling component permits. The three are therefore all maximal irreducible closed subsets, and no additional component exists by Step 2.

For the intersections, observe that \(L\cap\{b=0\}\) consists of \(H_i=\begin{psmallmatrix}0&d_i\\0&e_i\end{psmallmatrix}\), which always have the common kernel line spanned by the first basis vector. Thus \(L\cap C_{\mathrm{ker}}\) has \(2r\) freely chosen \((d,e)\) coordinates and \(r\) central \(f\) coordinates, giving dimension \(3r\). To have a common image as well, the \(2\times r\) matrix with columns \((d_i,e_i)^T\) must have rank at most one. Its determinantal variety has dimension \(r+1\); with the central coordinates this gives \(\dim(L\cap C_{\mathrm{im}})=2r+1\).

Both a common image and a common kernel force the span of the \(H_i\) to have dimension at most one. Conversely, if the \(H_i\) span a line generated by a rank-one matrix they have both common structures. Such a tuple is specified by a point on the three-dimensional affine rank-one cone of \(2\times2\) matrices and an \(r\)-tuple of scalars, modulo a one-dimensional scaling on the nonzero stratum, for dimension \(3+r-1=r+2\); add the \(r\) free \(f\)-coordinates to get \(2r+2\). The triple intersection is the preceding rank-at-most-one sublocus with \(a=c=0\), of dimension \(2r+1\). \(\square\)

### 4. Uniform finite-field enumeration

Work now over \(\mathbb F_q\), with no restriction on its characteristic. Let \(I_r(q)\) be the number of ordered \(r\)-tuples of \(2\times2\) matrices whose linear span contains only matrices of determinant zero. Such spans have dimensions zero, one or two by the lemma. Dimension-zero gives one tuple. There are \((q+1)^2\) one-dimensional subspaces generated by nonzero rank-one matrices, each with \(q^r-1\) tuples spanning it. Finally there are exactly \(q+1\) two-dimensional rank-at-most-one matrix subspaces of the common-image ruling and another \(q+1\) from the common-kernel ruling; in each fixed plane, the count of spanning ordered \(r\)-tuples is \((q^r-1)(q^r-q)\). The latter factor automatically vanishes at \(r=1\). Therefore
\[
I_r(q)=1+(q+1)^2(q^r-1)+2(q+1)(q^r-1)(q^r-q).
\]
The \(b=0\) branch has \(q^rI_r(q)\) elements after the free \(f\)-coordinates. The linear branch \(L\) has \(q^{4r}\) elements, and their intersection has \(q^{3r}\) elements because \(a=b=c=0\) leaves \(d,e,f\) free. Inclusion-exclusion gives the displayed formula. Each step counts the actual prescribed tuples, so no polynomial interpolation, asymptotic approximation, or characteristic-based extrapolation is involved. \(\square\)

## Verification

The accompanying `verify_square_zero_flags.py` computes square-zero matrices from literal entry multiplication and builds the pairwise-anticommutation incidence matrix independently over fields of orders \(2,3,4,5\). It counts ordered pairs directly and ordered triples via the exact trace of the cube of that incidence matrix; the unused top-right coordinates contribute a separately checked factor of \(q^r\). A direct single-matrix count tests the one-generator boundary. All twelve field/tuple-length configurations matched the closed formula. The finite field of order four is implemented from its quadratic polynomial relation rather than approximated by arithmetic modulo four. The optional second checker `verify_rulings.py` separately exhausts the common-image/common-kernel incidence counts for tuple length two over prime fields of orders two, three, and five.

Reproduce with `python verify_square_zero_flags.py` using Python and NumPy. Finite tests are corroboration only; the rank-one lemma and incidence-bundle argument prove the unlimited assertions.

## Relationship to prior work

The literature on commuting nilpotent tuples, notably Ngo and Šivic, concerns arbitrary nilpotent matrices with commutator zero, not the fixed strictly upper-triangular flag locus with exterior relations; in particular, its components do not imply the three components here. Chen and Wang classify full-matrix anticommuting **pairs**, in contrast with arbitrary-length square-zero exterior tuples restricted to a fixed flag, so their general pair decomposition does not directly provide these components or counts. Boos describes conjugation orbits of individual square-zero nilpotent matrices under parabolics, a different invariant from simultaneous exterior tuples. The standard rank-one matrix-space and Segre-quadric rulings are used here as classical tools and are not claimed new.

The claimed contribution is the complete uniform three-component classification, its explicit intersection geometry, and the exact all-characteristic finite-field formula for this natural flagged representation family. It is not a classification of unrestricted exterior-algebra representations, and implicit historical overlap remains possible.

## Limitations

No assertion is made about nonreduced scheme structures, multiplicities, moduli after quotienting by flag-preserving conjugation, or larger matrix sizes. The detailed geometric component theorem requires at least two generators; for one generator the union description and arithmetic formula remain valid, but the two ruling images coincide with the single determinant hypersurface in the \(b=0\) branch. While exact overlap checks were conducted against accessible primary studies, complete historical-priority verification and independent validation are not claimed.

## References

1. N. V. Ngo and K. Šivic, *On varieties of commuting nilpotent matrices*, arXiv:1308.4438 (initial public version 2013-08-20; revised 2014-03-26). https://arxiv.org/abs/1308.4438 .
2. X. Chen and W. Wang, *Anti-commuting varieties*, arXiv:1805.00378 (initial public version 2018-05-01), full text: https://arxiv.org/html/1805.00378v2 .
3. M. Boos, *Finite Parabolic Conjugation on Varieties of Nilpotent Matrices*, arXiv:1504.05367 (2015-04-21). https://arxiv.org/abs/1504.05367 .
4. R. Basili, *On commuting varieties of upper triangular matrices*, Communications in Algebra 45 (2017), 1533–1541, DOI:10.1080/00927872.2016.1178272 (publication information examined through the accessible abstract).
