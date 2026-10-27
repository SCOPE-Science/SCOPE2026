# Primitive arithmetic Picard lattices of the two quadratic Fermat-sextic double planes over \(\mathbb F_5\)

## Finding
Let \(X_1\) and \(X_2\) be the smooth projective double planes over \(\mathbb F_5\) defined in \(\mathbb P(3,1,1,1)\) by
\[
X_d:\quad d w^2=x^6+y^6+z^6,\qquad d\in\{1,2\}.
\]
These are the two quadratic twists of the indicated Fermat double plane, since \(2\) is a nonsquare in \(\mathbb F_5\). Their geometric Picard lattices are isomorphic, of rank \(22\) and discriminant \(-25\), but their primitive arithmetic Picard lattices have different intersection forms. Specifically,
\[
\begin{array}{c|c|c|c}
d&\operatorname{rank}\operatorname{Pic}(X_d)&\det\left(\operatorname{Pic}(X_d)\right)&\operatorname{Pic}(X_d)^\vee/\operatorname{Pic}(X_d)\\\hline
1&12&-5120&(\mathbb Z/2\mathbb Z)^9\oplus\mathbb Z/10\mathbb Z\\
2&11&10240&(\mathbb Z/2\mathbb Z)^{10}\oplus\mathbb Z/10\mathbb Z
\end{array}
\]
The corresponding Frobenius characteristic polynomials on \(H^2_{\mathrm{\acute et}}\) are \((t-5)^{12}(t+5)^{10}\) and \((t-5)^{11}(t+5)^{11}\). Thus, for every positive integer \(n\),
\[
\#X_1(\mathbb F_{5^n})=1+5^{2n}+5^n(12+10(-1)^n),
\qquad
\#X_2(\mathbb F_{5^n})=1+5^{2n}+5^n(11+11(-1)^n).
\]
The algebraic rank and discriminant-group conclusions concern the primitive integral Picard lattices, not merely their rationalizations. Invariant factors of the discriminant group are nine \(2\)'s followed by \(10\) for \(X_1\), and ten \(2\)'s followed by \(10\) for \(X_2\).

## Assumptions and scope
The characteristic is exactly \(5\); \(2\) is a nonsquare and \(\sqrt2\in\mathbb F_{25}\). The double-plane branch is the smooth degree-six Fermat curve. The characteristic-five K3 surface is supersingular of Artin invariant one. The statement compares only the two quadratic twists obtained by rescaling the covering coordinate, not every diagonal twist of the three base coordinates.

## Proof
Partial derivatives of \(x^6+y^6+z^6\) in characteristic \(5\) are \(x^5,y^5,z^5\), which have no common zero in projective space. Hence the branch sextic and the double plane are smooth, and the canonical double-cover formula identifies each as a K3 surface. Over \(\mathbb F_{25}\), the map \(w\mapsto\sqrt2\,w\) identifies the twists.

Shimada [1, Section 2] establishes an integral basis of \(22\) rational-curve classes over \(\mathbb F_{25}\) for the geometric Néron–Severi lattice, with intersection determinant \(-25\). Katsura–Kondō–Shimada [2, Section 4 and supplemental data [3]] give the full integral Gram matrix \(G\) and matrices \(F\) and \(J\) in the same basis for arithmetic \(5\)-Frobenius and the deck involution. Classes are row vectors. The matrices satisfy
\[
F^2=J^2=I,\qquad FJ=JF,\qquad FGF^{\mathsf T}=G,\qquad JGJ^{\mathsf T}=G,\qquad\det G=-25.
\]
For \(X_1\), the arithmetic fixed group is \(\ker_{\mathbb Z}(F^{\mathsf T}-I)\). For \(X_2\), the defining descent cocycle multiplies Frobenius by the deck involution, and its arithmetic fixed group is \(\ker_{\mathbb Z}((FJ)^{\mathsf T}-I)\). The finite-field Brauer group vanishes, so these primitive integral fixed sublattices are the actual Picard groups over \(\mathbb F_5\).

Here is the critical integer-lattice step. For each \(A\in\{F^{\mathsf T}-I,(FJ)^{\mathsf T}-I\}\), calculate a Smith decomposition \(UAV=D\), with integral unimodular \(U,V\). The last columns of \(V\), corresponding to zero columns of \(D\), give a **primitive \(\mathbb Z\)-basis** of \(\ker A\), since \(V\) is unimodular. Write that basis as the columns of \(K\); then compute the integral Gram matrix \(K^{\mathsf T}GK\), its determinant, and its Smith invariant factors. The source-included reproducible verifier carries out these exact operations without floating-point arithmetic. It returns rank \(12\), determinant \(-5120\), and nonunit Smith factors \(2\) repeated nine times followed by \(10\) for \(X_1\); and rank \(11\), determinant \(10240\), and nonunit Smith factors \(2\) repeated ten times followed by \(10\) for \(X_2\). In particular, the fixed lattices are saturated in the rank-\(22\) geometric lattice.

As independent consistency checks, the orthogonal anti-invariant lattice for \(F\) has rank \(10\) and absolute discriminant \(5120\), and its direct sum with the fixed lattice has index \(1024\) in the geometric lattice. For \(FJ\), both eigensublattices have rank \(11\), absolute discriminant \(10240\), and index \(2048\) in their sum inside the geometric lattice. Both obey \(|\det G_+\det G_-|=25[\operatorname{NS}:\operatorname{NS}^+\oplus\operatorname{NS}^-]^2\).

All \(22\) geometric divisor classes are defined over \(\mathbb F_{25}\), and the cycle-class map spans degree-two étale cohomology. Thus arithmetic Frobenius on \(H^2\) has eigenvalues only \(\pm5\), and the \(+5\)-multiplicity is the rational fixed rank just computed. The Lefschetz trace formula yields the displayed point-count identities and the two zeta functions
\[
Z(X_1/\mathbb F_5,T)=\frac1{(1-T)(1-25T)(1-5T)^{12}(1+5T)^{10}},
\]
\[
Z(X_2/\mathbb F_5,T)=\frac1{(1-T)(1-25T)(1-5T)^{11}(1+5T)^{11}}.
\]

## Verification
Run `python verify_lattice.py` using the accompanying `requirements.txt` for the exact integral matrices and Smith transformations. The code checks the geometric matrix determinant, the two involution identities and isometries, the commutation relation, the primitive fixed-kernel ranks, determinant and full discriminant-group invariant factors, and the orthogonal complement index identity. It contains the three published integral matrices in full; no internet download is needed. Run `python verify_points.py` for independent exhaustive point counts over \(\mathbb F_5\) and representative extension-field counts over \(\mathbb F_{25}\). The exact tests produced `CHECK_OK` and `VERIFY_OK` respectively.

## Relationship to prior work
The geometric surface, integral basis of \(22\) rational curves, geometric intersection matrix, arithmetic Frobenius matrix and deck-involution matrix were already available in [1–3] and are not new. In particular [2, Table 4.3] gives the complete Frobenius action; this is strong prior coverage and means the fixed-lattice invariants are **computationally implicit** in the published matrices. The present narrower statement extracts and proves the primitive arithmetic fixed-lattice discriminants and group structures of the two quadratic twists, rather than proposing any new geometric basis or Frobenius representation. Standard Jacobi-sum formulas also determine diagonal-surface zeta functions, so the zeta equations are consequences and consistency checks, not an independent originality claim. No specific published table identifying both primitive arithmetic fixed-lattice discriminant groups was located in the inspected primary texts or targeted comparisons.

## Limitations
This is a self-review, not independent scientific verification. The two arithmetic lattices are distinguished by their discriminant groups, but the full discriminant quadratic forms and ample cones are not classified. The given matrices come from previously published data, so mathematical priority may be limited to the explicit primitive integral saturation calculations; a published equivalent calculation under different terminology remains possible. The extension-field point counts independently check only selected finite fields and do not replace the cohomological proof for all \(n\).

## References
[1] I. Shimada, *Projective models of the supersingular K3 surface with Artin invariant 1 in characteristic 5*, arXiv:1201.4533 (first posted 2012-01-22), Section 2 and Table 2.1. https://arxiv.org/abs/1201.4533

[2] T. Katsura, S. Kondō, I. Shimada, *On the supersingular K3 surface in characteristic 5 with Artin invariant 1*, arXiv:1312.0687 (2013), Section 4, including the deck and Frobenius actions. https://arxiv.org/abs/1312.0687

[3] I. Shimada, publicly distributed accompanying exact computational data `compdataB.txt`, entries `GramSX`, `Frob`, and `Flip`: https://home.hiroshima-u.ac.jp/ichiro-shimada/preprints/KKSssK3char5/compdatassK3char5/compdataB.txt
