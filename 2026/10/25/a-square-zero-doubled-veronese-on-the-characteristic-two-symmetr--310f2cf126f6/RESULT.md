# A square-zero doubled Veronese on the characteristic-two symmetric determinantal cubic

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(X\subset\mathbb P^5_k\) be the cubic hypersurface whose defining equation is the determinant of the generic symmetric matrix
\[
M=\begin{pmatrix}a&b&d\\b&c&f\\d&f&e\end{pmatrix},\qquad
F=ace+af^2+cd^2+eb^2.
\]
Its intrinsic projective Jacobian singular scheme \(Y\) is the complete intersection of exactly three quadrics
\[
J_Y=(ac+b^2,\ ae+d^2,\ ce+f^2).
\]
Its reduction \(Z=Y_{\mathrm{red}}\) is the quadratic Veronese surface \(v_2(\mathbb P^2)\), but \(Y\) is a nonreduced, locally split, square-zero double structure. With \(i:Z\hookrightarrow Y\) and the canonical identification \(Z\cong\mathbb P^2\), its nilradical \(\mathcal N\) satisfies
\[
\mathcal N^2=0,\qquad \mathcal N\cong\mathcal O_{\mathbb P^2}(-3),\qquad
0\longrightarrow i_*\mathcal O_{\mathbb P^2}(-3)\longrightarrow\mathcal O_Y\longrightarrow i_*\mathcal O_Z\longrightarrow0.
\]
Here the last sequence is one of sheaves of abelian groups, with a square-zero ideal inclusion; no global splitting is asserted. The scheme \(Y\) is a projective complete intersection of degree \(8\), whereas its reduced support has degree \(4\). Its graded coordinate ring has Hilbert series
\[
H_{k[Y]}(t)=\frac{(1+t)^3}{(1-t)^3},
\]
and Hilbert polynomial \(P_Y(n)=4n^2+2\). The hypersurface \(X\) itself is integral and normal.

## Assumptions and scope
All schemes are over an algebraically closed field of characteristic exactly \(2\); the scheme structure of \(Y\) is the intrinsic Jacobian scheme \(\operatorname{Proj}(k[a,b,c,d,e,f]/(F,\partial_aF,\ldots,\partial_fF))\). Because \(F\) is homogeneous of degree \(3\), Euler's identity reduces the defining ideal to the three derivatives, as verified below. The usual identification between symmetric bilinear matrices and all ternary quadratic forms does **not** hold in characteristic \(2\); this is specifically a symmetric-matrix determinant cubic, not the universal ternary-conic discriminant.

## Proof
**The Jacobian ideal.** Differentiating \(F\) in the six independent symmetric-matrix coordinates yields \(\partial_a F=ce+f^2\), \(\partial_c F=ae+d^2\), \(\partial_e F=ac+b^2\), and \(\partial_bF=\partial_dF=\partial_fF=0\). Directly,
\[
F=a(ce+f^2)+c(ae+d^2)+e(ac+b^2),
\]
so the cubic belongs to its derivative ideal \(J\).

**Underlying reduced Veronese.** Denote by \(P\) the homogeneous prime ideal of all six \(2\)-by-\(2\) minors of \(M\): the three generators of \(J\), together with
\[
u=af+bd,\qquad v=cd+bf,\qquad w=eb+df.
\]
For any point of \(V(J)\), one of \(a,c,e\) must be nonzero, since their simultaneous vanishing forces \(b=d=f=0\). On the chart \(a\ne0\), put \(u_1=b/a\), \(u_2=d/a\), and \(\eta=(af+bd)/a^2\). The equations of \(J\) imply
\[
\frac ca=u_1^2,\qquad \frac ea=u_2^2,\qquad \frac fa=u_1u_2+\eta,\qquad \eta^2=0.
\]
Indeed the first two follow from the principal minors and the third is the definition of \(\eta\); the remaining minor is \(\eta^2=0\). Thus the exact affine chart ring is
\[
\mathcal O_Y(D_+(a))\cong k[u_1,u_2,\eta]/(\eta^2).
\]
The analogous descriptions hold on \(c\ne0\) and \(e\ne0\), and those three charts cover the projective scheme. Its reduced charts therefore glue to the rank-one locus \([s^2:st:t^2:sr:r^2:tr]\), with matrix entries ordered as above, i.e. the Veronese embedding of \(\mathbb P^2\). In particular \(\sqrt J=P\) after saturation, and there are no additional singular components.

**The nilpotent line bundle.** The nilradical is \(P/J\), generated on \(D_+(a)\) by \(\eta_a=(af+bd)/a^2\), with \(\eta_a^2=0\). Likewise \(\eta_c=(cd+bf)/c^2\) and \(\eta_e=(eb+df)/e^2\). Their restrictions to overlaps are
\[
\eta_c=\eta_a/u_1^3,\qquad\eta_e=\eta_a/u_2^3.
\]
These are precisely the transition functions of \(\mathcal O_{\mathbb P^2}(-3)\) for the standard affine coordinates \(u_1=t/s\), \(u_2=r/s\). The local presentation has free rank-one nilradical on every chart, so this identifies it globally. It is square-zero locally and hence globally. The local scheme along each point of the reduced surface is a dual-number thickening; no embedded or isolated singular component occurs.

**Complete intersection and Hilbert data.** Each affine chart has dimension \(2\); hence \(J\) has homogeneous height \(3\) in the six-variable polynomial ring. Since it has exactly three homogeneous generators and the polynomial ring is Cohen–Macaulay, those quadrics form a regular sequence. A homogeneous complete intersection of codimension \(3\) is saturated, of degree \(2^3=8\), and has the stated Hilbert series. Its coefficients satisfy \(h_Y(0)=1\) and \(h_Y(n)=4n^2+2\) for every integer \(n\ge1\). The reduced Veronese coordinate ring has Hilbert function \(h_Z(n)=\binom{2n+2}{2}\); the difference agrees for \(n\ge1\) with the sections of \(\mathcal O_{\mathbb P^2}(2n-3)\). This also corroborates the nilpotent-bundle calculation.

**Normality of the cubic.** The polynomial \(F\), viewed as linear in \(e\), has coefficient \(ac+b^2\) and constant term \(af^2+cd^2\). These have no common irreducible factor, so \(F\) is irreducible. The cubic hypersurface is Cohen–Macaulay; its singular support has dimension \(2\), versus \(\dim X=4\), hence is codimension \(2\) in \(X\). Therefore \(X\) satisfies Serre's \(R_1\) and \(S_2\) conditions and is normal.

## Verification
Run `python3 CHECK.py` in the directory containing this document. The standard-library checker performs exact arithmetic in characteristic \(2\): it differentiates the determinant, tests its expression in the derivative ideal, verifies all fifteen Buchberger \(S\)-pairs for a stated Gröbner basis, reduces all six products of the three additional Veronese minors to zero, and compares the complete-intersection Hilbert coefficients against \(4n^2+2\) for degrees \(1\) through \(20\). The finite Hilbert test only corroborates the Hilbert-series proof from the complete-intersection resolution; it is not an infinite proof.

## Relationship to prior work
The symmetric determinant in characteristic \(2\) has a classical cancellation-of-paired-permutations formula. Grenet–Monteil–Thomassé [1, Proposition 2.1] prove this determinant identity in general and study polynomial determinantal representations, not the particular projective Jacobian double structure described here. Piontkowski [2] develops the geometry of linear symmetric determinantal hypersurfaces over \(\mathbb C\), including corank loci and singularities; those characteristic-zero statements do not supply the characteristic-two Jacobian scheme. The reduced Veronese rank-one locus is classical and is not claimed as new. The contribution assessed here is the full modular intrinsic singular **scheme**, including the square-zero line bundle and its Hilbert series. An equivalent presentation in older literature is possible and has not been excluded independently.

## Limitations
This is a self-reviewed algebraic calculation, not independent validation or publication. The theorem applies to one universal symmetric \(3\)-by-\(3\) determinant over algebraically closed fields of characteristic \(2\), not all matrices or the discriminant of quadratic forms. The exact sequence of sheaves need not split globally. Novelty has residual risk from unidentified historical geometry of nonreduced Veronese doublings. The symbolic checker is an aid to reproducibility; the infinite-dimensional consequences rely on the proof given above.

## References
[1] B. Grenet, T. Monteil, S. Thomassé, *Symmetric Determinantal Representations in Characteristic 2*, arXiv:1210.5879, first submitted 2012-10-22, https://arxiv.org/abs/1210.5879 .

[2] J. Piontkowski, *Linear Symmetric Determinantal Hypersurfaces*, Michigan Math. J. 54 (2006), 117–146, https://www.math.uni-duesseldorf.de/~piontkow/det.pdf .
