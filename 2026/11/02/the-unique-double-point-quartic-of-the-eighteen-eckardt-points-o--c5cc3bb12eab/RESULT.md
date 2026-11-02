# The unique double-point quartic of the eighteen Eckardt points on a diagonal cubic

## Finding

Let \(k\) be any field of characteristic different from \(2\) and \(3\), and let \(a_0,a_1,a_2,a_3\in k^\times\). For the smooth diagonal cubic surface \(S\subset\mathbb P^3_k\) defined by \(F=\sum_{i=0}^{3}a_i x_i^3\), let \(E\) be its reduced geometric Eckardt-point locus, and let \(I\subset R=k[x_0,x_1,x_2,x_3]\) be the homogeneous ideal of \(E\). Put \(Q=x_0x_1x_2x_3\) and \(J=(x_1x_2x_3,x_0x_2x_3,x_0x_1x_3,x_0x_1x_2)\).

The geometric locus \(E\) consists of exactly eighteen distinct points and \(I=(F,J)\). Its entire symbolic square is
\[
 I^{(2)}=I^2+(Q).
\]
Thus \(I^{(2)}/I^2\) is cyclic, generated in degree \(4\); \(Q\) is the **unique** quartic up to scalar having multiplicity at least two at every one of the eighteen Eckardt points. A minimal homogeneous generating set of \(I^{(2)}\) comprises \(Q\) and nine sextics \(F^2\), \(F x_0x_1x_2\), \(F x_0x_1x_3\), \(F x_0x_2x_3\), \(F x_1x_2x_3\), and the four squares of the displayed generators of \(J\).

The doubled point scheme \(2E\) has length \(72\), and its homogeneous coordinate ring has Hilbert series
\[
 H_{R/I^{(2)}}(t)=\frac{1+3t+6t^2+10t^3+14t^4+18t^5+13t^6+7t^7}{1-t}.
\]
In particular its Hilbert function in degrees \(0,1,\ldots,7\) is \((1,4,10,20,34,52,65,72)\), and remains \(72\) thereafter. The Castelnuovo--Mumford regularity of \(R/I^{(2)}\) is \(7\).

## Assumptions and scope

The characteristic restriction is needed to identify the *complete geometric Eckardt locus* with these eighteen points. The ideal identity itself is valid for every field in which the diagonal cubic intersects each coordinate line in three distinct geometric points. All assertions are scheme-theoretic over \(k\), and remain valid when those points split only after a field extension. The symbolic square of a reduced finite set of projective points is its saturated ordinary square and equals the ideal of its first infinitesimal neighborhoods.

## Proof

**Geometric identification.** A geometric Eckardt point of a smooth cubic surface is characterized by vanishing of the quadratic term on its tangent plane, equivalently a triple point of its tangent-plane cubic section. At a point \(P=(p_0:\cdots:p_3)\in S\), the linear and quadratic Taylor terms, up to nonzero scalar factors, are \(L=\sum a_i p_i^2u_i\) and \(B=\sum a_i p_i u_i^2\). If \(P\) has at least three nonzero coordinates, the restriction of \(B\) to each two-coordinate tangent direction would force \(a_ip_i^3+a_jp_j^3=0\) for each pair of nonzero coordinates. Three such pairwise conditions are contradictory in characteristic different from \(2\). A point with only one nonzero coordinate cannot lie on \(S\). Conversely, every point with exactly two nonzero coordinates satisfying \(F=0\) makes \(B|_{L=0}=0\). There are three distinct points on each of the six coordinate lines because the characteristic is not \(3\). These eighteen points miss all coordinate vertices.

The reduced union of the six coordinate lines has ideal \(J\): it is the Stanley--Reisner ideal of the rank-two uniform matroid on four elements. Since \(F\) is nonzero on every component, it is a nonzerodivisor modulo \(J\), and \(I=(J,F)\) is the saturated reduced ideal of the eighteen transverse intersections.

**Symbolic square on the six lines.** Set \(M=J^{(2)}=\bigcap_{0\le i<j\le3}(x_i,x_j)^2\). A monomial \(x_0^{b_0}\cdots x_3^{b_3}\) belongs to \(M\) precisely when \(b_i+b_j\ge2\) for all pairs. If all four exponents are positive the monomial is divisible by \(Q\); if one exponent is zero, all three remaining exponents are at least two, so the monomial is divisible by the square of a cubic generator of \(J\). Two zero exponents are impossible. Consequently
\[
 M=J^2+(Q)=(Q,(x_1x_2x_3)^2,(x_0x_2x_3)^2,(x_0x_1x_3)^2,(x_0x_1x_2)^2).
\]
The simplicial complex of \(J\) is the rank-two uniform matroid, so by the symbolic-power Cohen--Macaulay theorem (Varbaro, Theorem 2.1) \(R/M\) is Cohen--Macaulay of dimension two. The polynomial \(F\) avoids each of its six associated coordinate-line primes and is therefore regular on both \(R/M\) and \(R/J\).

**Saturation and exact equality.** Put \(K=I^2+(Q)=M+FJ+(F^2)\). Since \(F\) is regular modulo \(M\), direct reduction gives \((K:F)=I\) and \((K,F)=(M,F)\). Multiplication by \(F\) therefore yields the exact sequence
\[
 0\longrightarrow (R/I)(-3)\xrightarrow{\cdot F}R/K\longrightarrow R/(M,F)\longrightarrow0.
\]
Both outer modules are one-dimensional Cohen--Macaulay rings: \(R/I\) because \(R/J\) is Cohen--Macaulay and \(F\) regular, and \(R/(M,F)\) by the preceding paragraph. Therefore \(R/K\) has depth one, so \(K\) is saturated. At every geometric point of \(E\), the ideal \(I\) localizes to its maximal ideal, while \(Q\), containing the two vanishing coordinate factors, belongs to its square. Thus \(K\) and \(I^2\) define the same length-four local scheme at each of the eighteen points. Saturation proves \(K=I^{(2)}\).

**Hilbert series and generators.** Direct monomial counting gives
\[
 H_{R/J}(t)=\frac{1+2t+3t^2}{(1-t)^2},\qquad
 H_{R/M}(t)=\frac{1+2t+3t^2+4t^3+4t^4+4t^5}{(1-t)^2}.
\]
Apply the regular cubic \(F\) and the exact sequence above. The Hilbert series simplifies to the one stated in the finding. Since \(I\) is generated by five cubics, \(I^2\) has no nonzero forms below degree six, whereas \(Q\) has degree four. Hence \(Q\notin I^2\), the minimum nonzero degree of \(I^{(2)}\) is four, and the degree-four space is \(kQ\). Among the fifteen pairwise products of the five cubic generators of \(I\), the six products involving two distinct generators of \(J\) are multiples of \(Q\). The other nine sextics have linearly independent residues modulo \((Q)\), as witnessed by their distinct monomial supports, so they are minimal. The displayed numerator ends in degree seven, giving regularity seven for this one-dimensional Cohen--Macaulay graded ring.

## Verification

The standalone program `verify.py` independently forms all eighteen projective points over each of \(\mathbb F_7\), \(\mathbb F_{13}\), and \(\mathbb F_{19}\). It compares two independently constructed vector spaces in degrees four through eight: first-order jet vanishing at every point and the graded span of \(I^2+(Q)\). In every case their dimensions agree and the Hilbert function is \((34,52,65,72,72)\) in these five degrees. In degree six it separately finds dimension fifteen for \(I^2\) and nineteen for \(I^{(2)}\). These finite checks corroborate the theorem; the arbitrary-field assertion rests on the preceding ideal-theoretic proof.

## Relationship to prior work

Classical work on cubic surfaces identifies Eckardt points and the extremal eighteen-point configuration. Dardanelli--van Geemen analyze Eckardt geometry and Hessian K3 surfaces, not the symbolic square of the point ideal. Varbaro proves the general Cohen--Macaulay theorem for symbolic powers of matroid Stanley--Reisner ideals; it supplies one essential lemma, but not the hypersurface-cut Eckardt ideal or the quartic defect. Nagel--Seceleanu study **planar** Fermat point ideals in three variables, whose point set is different. Mantero treats full star configurations from all specified intersections; the present eighteen-point set is the cubic cut of the six coordinate lines, not the full star configuration of four coordinate hyperplanes plus the cubic (which additionally contains four coordinate vertices). Thus the precise doubled-Eckardt interpolation computation requires the separate identification and saturation argument above.

## Limitations

This describes the reduced geometric Eckardt-point scheme of diagonal cubic surfaces only; it does not classify the corresponding scheme for arbitrary cubic surfaces, nor triple or higher symbolic powers. The source comparisons do not prove worldwide historical priority. Characteristics two and three are excluded because the geometric Eckardt locus or transversality changes. The finite verifier samples three splitting fields and is not a proof in arbitrary characteristic.

## References

Dardanelli--van Geemen, *Hessians and the moduli space of cubic surfaces* (2004), arXiv:math/0409322, Section 2.
Varbaro, *Symbolic powers and matroids* (2010), arXiv:1003.2912, Theorem 2.1.
Nagel--Seceleanu, *Ordinary and symbolic Rees algebras for ideals of Fermat point configurations* (2015), arXiv:1509.04977, Sections 1--4.
Mantero, *The structure and free resolutions of the symbolic powers of star configurations of hypersurfaces* (2019), arXiv:1907.08172, Sections 1--2.
