# Exactly two smooth-net extensions of every conic pencil over \(\mathbf F_3\)

## Finding
Let \(V=\mathbf F_3[X,Y,Z]_2\), the six-dimensional vector space of homogeneous ternary quadratic forms. A *smooth pencil* means a two-dimensional vector subspace \(P\subset V\) for which all four one-dimensional subspaces of \(P\) define geometrically smooth conics. A *smooth net* means a three-dimensional vector subspace \(N\subset V\) for which all thirteen one-dimensional subspaces of \(N\) define geometrically smooth conics.

**Theorem.** Every smooth pencil \(P\) is contained in exactly two distinct smooth nets. The group \(\operatorname{PGL}_3(\mathbf F_3)\) is transitive on smooth pencils; the two containing nets belong to different projective orbits. There are exactly \(1872\) smooth pencils and \(288\) smooth nets. The nets form two projective orbits of \(144\) nets each. Every smooth net contains thirteen smooth pencils. Hence the pencil–net incidence graph has degree \(2\) on its \(1872\) pencil vertices and degree \(13\) on its \(288\) net vertices, with each pencil adjacent to one net from each net orbit.

In coefficient order \((X^2,Y^2,Z^2,XY,XZ,YZ)\), one pencil representative is spanned by
\[
F=X^2+YZ,\qquad G=Y^2+XZ+YZ.
\]
Its two smooth-net extensions are obtained by adjoining respectively
\[
H_1=Z^2+2XY+2XZ,\qquad H_2=Z^2+2XY+2XZ+2YZ.
\]
The coefficients \(2\) are elements of \(\mathbf F_3\). No uniqueness or existence assertion is made for larger fields.

## Assumptions and scope
All fields and linear spaces are defined over \(\mathbf F_3\). A conic is geometrically smooth if smooth after base extension to the algebraic closure. Subspaces are genuine vector subspaces, not lists of generators; scalar-equivalent forms define the same projective conic. Projective equivalence is induced by change of coordinates through \(\operatorname{PGL}_3(\mathbf F_3)\). The assertion concerns every smooth pencil, not merely pencils belonging to a designated projective orbit.

## Proof
Write a ternary quadratic as
\[
Q=aX^2+bY^2+cZ^2+dXY+eXZ+fYZ.
\]
As \(\operatorname{char}(\mathbf F_3)\ne2\), its homogeneous gradient is represented by the symmetric matrix
\[
M(Q)=\begin{pmatrix}2a&d&e\\d&2b&f\\e&f&2c\end{pmatrix}.
\]
Euler's identity \(2Q=XQ_X+YQ_Y+ZQ_Z\) shows a nonzero singular projective point occurs over the algebraic closure if and only if this matrix is singular. Consequently \(Q\) is geometrically smooth exactly when \(\det M(Q)\ne0\) in \(\mathbf F_3\). This criterion is exact over the algebraic closure; it is not a point-sampling test.

Represent each coefficient vector \((a,b,c,d,e,f)\) by the integer \(\sum_{i=0}^{5}a_i3^i\) in the range \(0\) through \(728\). The nonzero scalar classes comprise \((3^6-1)/(3-1)=364\) projective forms. Exact application of the determinant criterion identifies \(234\) smooth forms. Enumerate all \(k\)-dimensional subspaces by their unique reduced-row-echelon matrices, where \(k=2,3\). There are \({6\brack2}_3=11011\) pencils and \({6\brack3}_3=33880\) nets, where the brackets denote Gaussian binomial coefficients. Testing the \((3^k-1)/2\) projective form directions in each subspace gives exactly \(1872\) smooth pencils and \(288\) smooth nets. Both totals are reproducible in `verify_full_census.py` with only integral arithmetic.

For a structural completeness check independent of the full net enumeration, consider the displayed pencil \(P_0=\langle F,G\rangle\). Its projective span contains four smooth conics, checked by \(\det M\ne0\). Any three-dimensional extension of \(P_0\) corresponds to a one-dimensional subspace of the four-dimensional quotient \(V/P_0\), so exactly \((3^4-1)/(3-1)=40\) candidate nets exist. Enumerate these forty subspaces without repetitions, test all thirteen member conics, and obtain **exactly two** smooth extensions, represented by adjoining \(H_1\) and \(H_2\).

For transitivity and net-orbit separation, use the four invertible coordinate matrices given explicitly in `verify_orbit_reduction.py`: a swap, an elementary shear, a nontrivial coordinate scaling, and a three-cycle. Matrix multiplication shows that these generate all \(11232\) elements of \(\operatorname{GL}_3(\mathbf F_3)\); quotienting by its two scalar matrices gives \(5616\) projective transformations. Applying the matrices by substitution to the four projective conics of \(P_0\) yields an orbit of exactly \(1872\) distinct pencils. The independently exhaustive enumeration above gives the same number of smooth pencils, hence this orbit is all of them. Each of the two extensions of \(P_0\) has a projective orbit of exactly \(144\) nets; the two orbits are disjoint. Since projective transformations preserve both extension and smoothness, every smooth pencil has exactly two extensions, one from each orbit. Finally there are \(288\) smooth nets in the complete enumeration, so the two net orbits exhaust all of them.

Every smooth net has \((3^3-1)/(3-1)=13\) two-dimensional subspaces; each is smooth because its members are among those of the net. The incidence count \(1872\cdot2=288\cdot13=3744\) agrees, and proves the stated degrees. The stabilizer of a smooth pencil has order \(5616/1872=3\), and each net stabilizer has order \(5616/144=39\).

## Verification
Run `python3 verify_full_census.py` and `python3 verify_orbit_reduction.py` with Python 3. Both files are self-contained and require no external packages. The first directly enumerates every reduced-row-echelon pencil and net, verifies the smooth member condition, builds complete pencil-to-net incidences, and constructs net and pencil orbits. The second independently tests precisely forty candidate extensions of a fixed smooth pencil, certifies the full coordinate group order by exhaustive matrix closure, computes its full pencil orbit and both disjoint net orbits. The two routines use distinct enumeration methods (complete subspace census versus quotient extension enumeration plus group transitivity), but share the elementary matrix determinant criterion explained above.

Checks performed: \(364\) projective quadratic forms, \(234\) smooth conics; \(11011\) pencils of which \(1872\) smooth; \(33880\) nets of which \(288\) smooth; every smooth pencil's extension multiplicity \(2\); two net orbits of size \(144\); one pencil orbit of size \(1872\); two disjoint net-extension orbits for \(P_0\). The accompanying expected-results files record the non-timing portions of actual execution output. This is an exhaustive finite computation, not a claim of formal proof-assistant certification.

## Relationship to prior work
Lavrauw, Popiel and Sheekey classified incidence invariants and stabilizers for **rank-one** nets of conics, i.e. nets containing a repeated-line conic (arXiv:2010.00177, first public 2020-10-01). Those nets cannot be all-smooth: a repeated line is singular. Their work and earlier classifications of pencils and nets provide important surrounding orbit theory, but the published scope inspected there does not give the exact smooth-pencil-to-smooth-net extension theorem over \(\mathbf F_3\). Asgarli and Ghioca (arXiv:2203.07169) study all-smooth pencils of hypersurfaces over finite fields, including small-field examples; their inspected existence and construction statements do not determine this incidence multiplicity or its division into two net orbits. The present claim is the precise F3 smooth-net extension incidence, not the general existence of smooth pencils or a reclassification of rank-one nets.

## Limitations
The result is restricted to ternary quadratics over \(\mathbf F_3\). Projective linear equivalence is considered, not any broader notion of moduli equivalence. Exact arithmetic enumeration is finite and reproducible, but an independent human mathematical audit is not provided. A historical or unpublished complete odd-characteristic net census could implicitly contain these numbers or the extension assertion; that priority risk is not excluded by unsuccessful search. The source classification dates are dates of first public versions, not journal revisions.

## References
1. M. Lavrauw, T. Popiel and J. Sheekey, *Combinatorial invariants for nets of conics in PG(2,q)*, arXiv:2010.00177, first posted 2020-10-01; published in Designs, Codes and Cryptography. https://arxiv.org/abs/2010.00177
2. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first posted 2022-03-14; Bull. Aust. Math. Soc. https://arxiv.org/abs/2203.07169
3. The accompanying `verify_full_census.py` and `verify_orbit_reduction.py`, with explicit finite-field arithmetic and complete enumeration procedures.
