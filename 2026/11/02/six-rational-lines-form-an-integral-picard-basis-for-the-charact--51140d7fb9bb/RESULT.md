# Six rational lines form an integral Picard basis for the characteristic-two Clebsch cubic

## Finding

Let \(S/\mathbb F_2\) be the smooth Clebsch diagonal cubic
\[
\sum_{i=0}^{4}X_i=\sum_{i=0}^{4}X_i^3=0\quad\text{in }\mathbb P^4.
\]
For distinct indices \(i,j,k,l,m\) exhausting \(\{0,1,2,3,4\}\), define its \(\mathbb F_2\)-line
\[
L_{ij|kl}=\mathbb P\bigl(\operatorname{span}_{\mathbb F_2}\{e_i+e_j,e_k+e_l\}\bigr),
\]
where \(e_i\) denotes the coordinate vector. The order within each pair and the order of the pairs do not matter. Define six lines
\[
(L_1,L_2,L_3,L_4,L_5,L_6)=
(L_{01|23},L_{01|24},L_{01|34},L_{02|13},L_{02|14},L_{03|14}).
\]
**The six divisor classes \([L_1],\ldots,[L_6]\) form a \(\mathbb Z\)-basis of \(\operatorname{Pic}(S)\), and hence of \(\operatorname{Pic}(S_{\overline{\mathbb F}_2})^{\mathrm{Frob}_2}\).** Their intersection matrix is
\[
G=\begin{pmatrix}
-1&1&1&1&0&0\\
1&-1&1&0&1&0\\
1&1&-1&0&0&1\\
1&0&0&-1&1&0\\
0&1&0&1&-1&1\\
0&0&1&0&1&-1
\end{pmatrix},\qquad \det G=-2.
\]
Thus the arithmetic Picard lattice has rank \(6\), signature \((1,5)\), and absolute discriminant \(2\). The full geometric Picard rank is \(7\); Frobenius acts on it as a single root reflection. These statements concern divisor classes, not just the number of rational lines.

## Assumptions and scope

All coordinates, line spans and Galois actions use the displayed \(\mathbb F_2\) model. By \(\operatorname{Pic}(S)\) we mean the integral group of line-bundle classes over \(\mathbb F_2\); finite-field Brauer vanishing identifies it with the invariant subgroup of the geometric Picard group. The theorem does not assert that every geometric line is rational over \(\mathbb F_2\): there are exactly \(15\) rational lines and six Frobenius-conjugate pairs of additional lines, all defined over \(\mathbb F_4\).

## Proof

**Smoothness and splitting field.** Let \(H\) be the four-dimensional \(\mathbb F_2\)-linear hyperplane in \(\mathbb F_2^5\) with coordinate sum zero. After extension to \(\mathbb F_4\), the cubic polynomial on \(H\) is the norm form \(h(v,v)=\sum_i v_i v_i^2\). Its associated Hermitian form is nondegenerate: the perpendicular space to \(H\) in the ambient five-dimensional standard Hermitian space is the line spanned by \((1,1,1,1,1)\), which does not belong to \(H\) because \(5\) is odd. Therefore \(S\) is a smooth cubic surface. The standard Hermitian-surface calculation with \(q=2\) gives \(45\) points and \(27\) generator lines over \(\mathbb F_4\). A smooth cubic surface over the algebraic closure has exactly \(27\) lines, so all geometric lines are already defined over \(\mathbb F_4\). Since line classes generate the geometric Picard group, the square of arithmetic Frobenius acts trivially on that rank-seven lattice.

**Rational points and invariant rank.** Every element of \(\mathbb F_2\) satisfies \(u^3=u\). Thus every projective point of the hyperplane \(H(\mathbb F_2)\cong\mathbb P^3(\mathbb F_2)\) lies on \(S\), giving \(\#S(\mathbb F_2)=15\). The Lefschetz trace formula for smooth cubic surfaces reads
\[
\#S(\mathbb F_2)=1+2^2+2\operatorname{Tr}
\bigl(\mathrm{Frob}_2\mid\operatorname{Pic}(S_{\overline{\mathbb F}_2})\otimes\mathbb Q\bigr).
\]
Hence the trace is \(5\). The action is an involution on a seven-dimensional rational space, so its \(+1\) eigenspace has dimension \(6\) and its \(-1\) eigenspace dimension \(1\). Therefore the integral invariant Picard lattice has rank \(6\).

**The six lines and their determinant.** In characteristic two the restriction of the cubic to the projective line spanned by binary vectors \(a,b\in H\) is identically zero precisely when their ordinary dot product is zero: indeed the two mixed cubic coefficients both equal \(\sum_i a_i b_i\). The dot product on \(H\) is a nondegenerate alternating form, yielding exactly \(15\) rational totally isotropic two-planes, i.e. rational lines. The displayed six pair-of-pairs spans are among them. Distinct lines on a smooth cubic surface intersect in \(0\) or \(1\) point, and their self-intersection is \(-1\). Two of our binary linear spans meet geometrically if and only if they share a nonzero binary vector. Applying this rule gives precisely \(G\), and direct integer elimination yields \(\det G=-2\). In particular these six classes are linearly independent and form a full-rank sublattice \(L\) of the invariant lattice \(P\).

**Integral saturation.** If \(d=[P:L]\), the integral intersection pairing satisfies \(\lvert\operatorname{disc}L\rvert=d^2\lvert\operatorname{disc}P\rvert\). Both discriminants are nonzero integers because \(L\) and \(P\) have the same rational span and the geometric intersection form is nondegenerate. Since \(\lvert\operatorname{disc}L\rvert=2\), necessarily \(d=1\). Thus these six classes give an integral basis of the invariant lattice. The Hochschild--Serre exact sequence together with \(\operatorname{Br}(\mathbb F_2)=0\) yields \(\operatorname{Pic}(S)=P\), proving the theorem. The pairing signature is \((1,5)\) by the Hodge index theorem for surfaces (valid in characteristic two).

**Frobenius reflection.** The geometric Picard lattice of a smooth cubic surface is unimodular of signature \((1,6)\). The primitive orthogonal complement of the invariant lattice has rank one and, by the discriminant-duality property of primitive orthogonal complements in unimodular lattices, square \(-2\). Frobenius fixes its orthogonal complement and negates its generator \(r\); thus it is the root reflection \(v\mapsto v+(v\cdot r)r\). This corollary does not require choosing a nonrational line explicitly.

## Verification

A standalone pure-Python program `verify.py` constructs \(\mathbb F_4\) by \(t^2+t+1\), exhausts all \(357\) projective lines in \(\mathbb P^3(\mathbb F_4)\), and finds \(27\) contained in the cubic and \(45\) cubic rational points. Coordinate Frobenius fixes \(15\) of the lines and pairs the others into \(6\) orbits. The same code independently enumerates all \(15\) binary isotropic lines, identifies the chosen six, reconstructs their Gram matrix, and calculates its determinant \(-2\) by exact integer Bareiss elimination. Run with `python3 verify.py`; the corresponding execution output is in `verification_output.txt`. The finite enumeration checks the finite-field inputs and determinant; the assertion about the entire Picard group follows from the preceding geometric and cohomological proof, not an extrapolation from an enumeration.

## Relationship to prior work

The characteristic-zero Clebsch surface, its classical \(27\)-line configuration, and the geometry of smooth cubic surfaces are classical; Baez's 2016 exposition provides the five-coordinate equation and two families of lines. The characteristic-two arithmetic \(15\)-line and \(27\)-line configurations, as well as the conjugacy class \(A_1\) of the Galois action, are already treated in finite-field cubic-surface and finite-geometry literature (notably Vikulova, McKean, and Alazemi--Betten). Those results are not claimed here. The particular **six explicit rational divisor classes forming an integral basis** and the squarefree intersection determinant giving integral saturation, rather than mere rational spanning or rational line counts, form the precise assessed contribution.

## Limitations

This is one explicitly marked cubic surface over \(\mathbb F_2\), not a classification of all characteristic-two cubic surfaces. The reflection corollary follows from standard Picard-lattice theory; the only new calculation needed for the integral generator theorem is the six-line intersection determinant. The historical-priority claim remains provisional, particularly regarding unindexed tables and earlier arithmetic Picard calculations. No independent scientific audit is asserted.

## References

- John Baez, *27 Lines on a Cubic Surface*, AMS Visual Insight, February 15, 2016: https://blogs.ams.org/visualinsight/2016/02/15/27-lines-on-a-cubic-surface/.
- Stephen McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217 (original preprint January 20, 2021): https://arxiv.org/abs/2101.08217.
- Z. Kadyrsizova et al., *Cubic surfaces of characteristic two*, arXiv:2007.12018 (original preprint July 23, 2020): https://arxiv.org/abs/2007.12018.
- A. V. Vikulova, *The most symmetric smooth cubic surface over a finite field of characteristic 2*, arXiv:2312.17032, especially Lemma 5.3: https://arxiv.org/abs/2312.17032.
- A. Alazemi and A. Betten, *On Triangle-Free \(v_3\) Configurations*, *Mathematics* 13 (2025), 3938, Section 3: https://doi.org/10.3390/math13243938.
