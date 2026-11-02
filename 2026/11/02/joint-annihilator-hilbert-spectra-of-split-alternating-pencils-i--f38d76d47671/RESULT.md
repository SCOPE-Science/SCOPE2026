# Joint-annihilator Hilbert spectra of split alternating pencils in characteristic two

## Finding

Let \(k\) be a field of characteristic \(2\), \(r\ge 1\), and \(E=\bigwedge_k\langle x_1,y_1,\ldots,x_r,y_r\rangle\). For arbitrary \(\lambda_1,\ldots,\lambda_r\in k\), form two degree-two elements
\[
 f=\sum_{i=1}^r x_i y_i,\qquad g=\sum_{i=1}^r\lambda_i x_i y_i.
\]
This is the split semisimple normal-form family of regular pencils of alternating two-forms (it is **not** the family of all alternating pencils). Let \(K_j=\ker(m_f:E_j\to E_{j+2})\cap\ker(m_g:E_j\to E_{j+2})\) and \(K(t)=\sum_{j=0}^{2r}\dim_k(K_j)t^j\).

For a nonempty set \(T\subseteq\{1,\ldots,r\}\), put \(s=|T|\) and call \(T\) *constant* when all its \(\lambda_i\) are equal. The following is an **exact polynomial** (including all coinciding-eigenvalue strata):
\[
K(t)=(2t)^r+\sum_{\varnothing\ne T\subseteq\{1,\ldots,r\}}(2t)^{r-s}\begin{cases}
 t^2(1+t^2)^{s-1},&T\text{ constant},\\
 t^4(1+t^2)^{s-2},&T\text{ nonconstant}.
\end{cases}
\]
The second branch occurs only for \(s\ge2\). By perfect graded duality, the full quotient Hilbert series is
\[
 \operatorname{Hilb}(E/(f,g),t)=t^{2r}K(t^{-1}).
\]
Thus the simultaneous annihilator and the quotient Hilbert series depend only on the multiplicities of the values among \(\lambda_1,\ldots,\lambda_r\), not on the actual distinct values.

When \(k=\mathbb F_q\), with \(q\) a power of two, let \(m_a=|\{i:\lambda_i=a\}|\). For \(r\ge2\) the exact total dimension is
\[
 \dim_k\bigl(\operatorname{Ann}(f)\cap\operatorname{Ann}(g)\bigr)
 =2^{r-2}\left(2^r+3+\sum_{a\in\mathbb F_q}(2^{m_a}-1)\right).
\]
For \(r=1\) it is \(3\). Write \(r=qa+b\), \(0\le b<q\). The sharp **minimum** over all \(q^r\) parameter tuples, for \(r\ge2\), is
\[
2^{r-2}\left(2^r+3+(q-b)(2^a-1)+b(2^{a+1}-1)\right),
\]
attained precisely when the \(q\) value multiplicities differ by at most one. The sharp **maximum** is \(2^{2r-1}+2^{r-1}\), attained precisely when all \(\lambda_i\) coincide. In particular, if \(q\ge r\) and the parameters are distinct, the minimum simplifies to \(2^{r-2}(2^r+r+3)\).

The first all-distinct even-dimensional example not matching the characteristic-zero generic middle coefficient occurs at \(r=4\): for four distinct parameters in characteristic two,
\[
 \operatorname{Hilb}(E/(f,g),t)=1+8t+26t^2+40t^3+17t^4,
\]
whereas the established complex generic-two-quadrics middle coefficient in eight variables is \(16\). This comparison concerns the stated split characteristic-two pencils, not arbitrary pairs.

## Assumptions and scope

The characteristic is exactly \(2\), \(r\) is any positive integer, and \(f,g\) are the displayed two simultaneous hyperbolic-pair forms, permitting repeated or zero \(\lambda_i\). The quotient and annihilator are graded over the given field. The extremal formulas apply only to finite fields \(\mathbb F_q\). No assertion is made for non-split or non-semisimple alternating pencils, or odd ambient dimensions with singular pencil summands. 

## Proof

(1) Each four-dimensional factor \(B_i=\bigwedge_k\langle x_i,y_i\rangle\) decomposes as a graded vector space into \(k\{x_i,y_i\}\) in degree \(1\), on which multiplication by \(x_iy_i\) is zero, and \(k\{1,x_iy_i\}\) in degrees \(0,2\). Tensoring these decompositions partitions \(E\) into direct summands indexed by \(T\subseteq\{1,\dots,r\}\), in which factors indexed by \(T\) are the two-dimensional \(k\{1,x_iy_i\}\) parts and factors outside \(T\) contribute \(2^{r-|T|}\) copies in degree \(r-|T|\).

(2) On the \(T\)-summand, let \(z_i=x_iy_i\) for \(i\in T\). Multiplication by \(f,g\) becomes multiplication by the two linear forms \(L_1=\sum_{i\in T}z_i\) and \(L_2=\sum_{i\in T}\lambda_i z_i\) in \(S_T=k[z_i:i\in T]/(z_i^2:i\in T)\), each \(z_i\) assigned degree \(2\). In characteristic two, every linear change of the \(z_i\) preserves the square-zero relations (the square of each new linear form is zero), so any independent \(L_1,L_2\) are algebraically equivalent to \(z_1,z_2\).

(3) When \(T\ne\varnothing\) is constant, the span of \(L_1,L_2\) has dimension one; the common annihilator is the ideal \((z_1)\) after an invertible linear change, with Hilbert series \(t^2(1+t^2)^{s-1}\). Otherwise their coefficient vectors are linearly independent, and the common annihilator is \((z_1z_2)\), with series \(t^4(1+t^2)^{s-2}\). If \(T\) is empty, both operators vanish and the summand contributes \((2t)^r\). Multiplying each nonempty contribution by its complement factor \((2t)^{r-s}\) and summing yields the displayed complete formula.

(4) The top-degree exterior product defines a perfect pairing \(E_j\times E_{2r-j}\to k\). The orthogonal complement of the degree-\((2r-j)\) component of the ideal \((f,g)\) is precisely \(K_j\). Therefore \(\dim(E/(f,g))_{2r-j}=\dim K_j\), yielding the reciprocal Hilbert-series identity. This step is valid even when \(f\) and \(g\) are dependent.

(5) Evaluate at \(t=1\): the empty set contributes \(2^r\); each nonempty \(T\) contributes \(2^{r-1}\) if constant and \(2^{r-2}\) if nonconstant. There are \(2^r-1\) nonempty \(T\) and exactly \(\sum_a(2^{m_a}-1)\) constant nonempty subsets. Simplification proves the total dimension. The function \(u\mapsto2^u\) is strictly convex on nonnegative integers; moving one unit between multiplicities differing by at least two decreases the sum strictly. Hence balanced occupancies give exactly the minimum, whereas concentrating all mass in one occupancy gives exactly the maximum (strictly for \(r\ge2\)). For \(r=1\), direct inspection gives \(K(t)=2t+t^2\).

(6) For \(r=4\) with pairwise distinct eigenvalues, summing subsets of sizes \(0\) through \(4\) gives \(K(t)=17t^4+40t^5+26t^6+8t^7+t^8\). Reciprocity gives the eight-variable quotient series stated. The characteristic-zero comparison is only the known generic middle coefficient in the complex-field result of Crispin Quiñonez–Lundqvist–Nenashev.

## Verification

Run the supplied standalone `verify.py` with Python 3. It independently constructs both degree-two multiplication matrices on the squarefree exterior monomial basis over the fields \(\mathbb F_2\), \(\mathbb F_4\) and \(\mathbb F_8\), stacks the two matrices at every graded degree, and computes the common kernel dimension by Gaussian elimination. It tests all parameter tuples for \(1\le r\le4\) when \(q=2\), and for \(1\le r\le3\) when \(q=4,8\): \(698\) tuples altogether. It checks both the entire Hilbert polynomial and the ungraded multiplicity formula for each tuple. The observed marker is `SPLIT_ALTERNATING_PENCIL_COMMON_KERNEL_OK 698`. Exhaustive finite-field checks on these finite configurations corroborate but cannot establish the theorem for unbounded \(r\) or all fields.

## Relationship to prior work

Moreno-Socías–Snellman studied Hilbert series of generic ideals in exterior algebras, with a 2000 preprint; their even-form results and conjectures supply archival motivation, not this two-generator characteristic-two stratification. Nguyen (2014) classified when a single quadratic quotient is Koszul, but this is a different invariant. Sastry–Sin, Proposition 5.1, explicitly calculates characteristic-two cohomology of multiplication by **one nondegenerate alternating two-form** using hyperbolic tensor factors; that result covers the corresponding single-multiplier homology and is not claimed new. It does not state the common annihilator of two multipliers or its dependence on eigenvalue collision multiplicities. Crispin Quiñonez–Lundqvist–Nenashev (2018) studied a **pair of generic quadratic elements over \(\mathbb C\)**, including their split canonical form with distinct parameters and partial Hilbert-series information. Those complex-characteristic results do not imply the stated characteristic-two quotient spectrum. Standard linear-algebra congruence theory and Frobenius duality are acknowledged ingredients, not independent new claims.

## Limitations

The conclusion is restricted to the displayed split, simultaneously diagonalizable alternating pencils. No assertion of the complete Hilbert stratification of all pencils or of a general two-generator generic ideal is made. The numerical extremal statements concern parameters in a fixed finite field and do not classify all geometric orbits. Characteristic-two cohomology for one multiplier, canonical pencil normal forms, and standard finite-field alternating-form counts are prior knowledge. An equivalent specialization hidden in broader modular exterior-algebra literature remains a historical priority risk. The proof is self-contained, but independent mathematical review has not been performed.

## References

- G. Moreno-Socías and J. Snellman, *Some conjectures about the Hilbert series of generic ideals in the exterior algebra*, arXiv:math/0007089 (first submitted 2000-07-14); https://arxiv.org/abs/math/0007089.
- H. D. Nguyen, *Koszul hypersurfaces over the exterior algebras*, arXiv:1406.0489 (2014); https://arxiv.org/abs/1406.0489.
- N. S. Narasimha Sastry and P. Sin, *On the Doubly Transitive Permutation Representations of Sp(2n, F2)*, Proposition 5.1 and §5; https://people.clas.ufl.edu/sin/files/steiner.pdf.
- V. Crispin Quiñonez, S. Lundqvist and G. Nenashev, *On ideals generated by two generic quadratic forms in the exterior algebra*, arXiv:1803.08918 (2018); https://arxiv.org/abs/1803.08918.
