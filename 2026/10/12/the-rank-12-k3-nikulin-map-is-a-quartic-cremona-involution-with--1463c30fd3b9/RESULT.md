# The rank-12 K3 Nikulin map is a quartic Cremona involution with a five-line base locus
## Finding
Let \(Q\subset \mathbf P^3\) be a very general Picard-rank-12 generalized Inose quartic in the family of Clingher, Malmendier, and Poon. Write
\[
C(W,X)=c_2(2X,W),\qquad D(W,X)=d_4(2X,W),
\]
where \(C\) and \(D\) are homogeneous binary forms of degrees \(2\) and \(4\). On the open locus where \(C\) and \(D\) are squarefree and coprime, the rational map printed in their Remark 4.16,
\[
\Phi[W:X:Y:Z]=[C W Z:C X Z:-C Y Z:D],
\]
is a quartic Cremona involution of \(\mathbf P^3\) with multidegree \((1,4,4,1)\).

Its reduced base locus is exactly five concurrent lines,
\[
L_0=\{{W=X=0\}},\qquad L_i=\{{Z=d_i(2X,W)=0\}}\quad(1\le i\le4),
\]
where \(D=\prod_{i=1}^4 d_i(2X,W)\). All five pass through \([0:0:1:0]\). Moreover, the Jacobian determinant is
\[
\det J_\Phi=4Z^2C^3D.
\]
Consequently the exceptional locus has exactly seven planes: \(Z=0\), the two planes cut out by the two linear factors of \(C\), and the four planes cut out by the factors of \(D\). The first three contract to \([0:0:0:1]\), whereas each \(D\)-plane maps onto the corresponding line \(L_i\).

## Assumptions and scope
The statement is over \(\mathbb C\). It concerns the Picard-rank-12 family in which the source writes \(c_2\) and \(d_4\) as products of respectively two and four linear forms. We work on the very general open subset on which those six points of \(\mathbf P^1\) are distinct; equivalently, \(C\) and \(D\) are squarefree and coprime. Degenerations where roots collide are excluded because the reduced base and exceptional configurations can then merge.

The source proves that the restriction of \(\Phi\) to the generalized Inose quartic induces a Nikulin involution on the minimal resolution. The new claim concerns the ambient birational geometry of the displayed rational self-map.

## Proof
Put \(C=C(W,X)\) and \(D=D(W,X)\). After one application of \(\Phi\), the first two coordinates are \(W'=CWZ\) and \(X'=CXZ\). Homogeneity gives
\[
C(W',X')=C^3Z^2,\qquad D(W',X')=C^4Z^4D.
\]
Therefore a second application gives
\[
\Phi^2[W:X:Y:Z]
=[C^4DZ^3W:C^4DZ^3X:C^4DZ^3Y:C^4DZ^4],
\]
which is projectively \([W:X:Y:Z]\) wherever \(C D Z\ne0\). Thus \(\Phi\) is birational and self-inverse. Its coordinate forms have degree \(4\) and no common divisor, so its degree is exactly \(4\). Since the inverse is the same degree-
\(4\) map, the projective multidegree is \((1,4,4,1)\).

For the base locus, all four coordinate forms vanish only if \(D=0\). If \(W=X=0\), this gives the line \(L_0\). Otherwise \([W:X]\) is a root of \(D\). If \(Z\ne0\), vanishing of the first two coordinates forces \(C=0\), contradicting coprimality of \(C\) and \(D\). Hence \(Z=0\), and the four roots of \(D\) give exactly the four lines \(L_i\). Each line contains \([0:0:1:0]\), as does \(L_0\), proving the stated reduced base configuration.

Direct differentiation of the four defining quartics yields
\[
\det J_\Phi=4Z^2C^3D.
\]
Because \(C\) and \(D\) are squarefree, this has seven distinct plane components. On \(Z=0\), and on either plane \(C=0\), the image of a general point is \([0:0:0:1]\). On a plane \(d_i(2X,W)=0\), the last coordinate vanishes while the ratio \(W:X\) is fixed; varying \(Y\) gives precisely the corresponding line \(L_i\). The Jacobian factorization shows there are no further exceptional hypersurface components.

## Verification
The attached `verification.py` uses SymPy \(1.14.0\) to treat \(C\) and \(D\) as generic homogeneous binary forms with algebraically independent coefficients. It checks the two homogeneity identities, the complete composition identity for \(\Phi^2\), and the exact Jacobian factorization. A fresh replay returned `VERIFY_OK composition=involution degree=4 inverse_degree=4 multidegree=(1,4,4,1) reduced_base=5_concurrent_lines exceptional=3_planes_to_point+4_planes_to_lines`.

The reduced base-locus argument itself is symbolic and does not rely on finite sampling: after imposing \(D=0\), coprimality of \(C\) and \(D\) forces either \(W=X=0\) or \(Z=0\).

## Relationship to prior work
Clingher–Malmendier–Poon give the quartic family and the rational formula for \(\Phi\), and state that it induces a Nikulin involution on the minimal resolution. Their paper does not describe the ambient map as a Cremona involution, compute its multidegree, or determine its base and exceptional loci. Full-text checks found no occurrences of “Cremona” or “base locus” in that source.

The later Clingher–Malmendier–Roulleau paper develops projective and double-sextic models for K3 surfaces with automorphism group \((\mathbb Z/2\mathbb Z)^2\). Its inspected preprint likewise does not state this five-line base configuration or the seven-plane exceptional configuration. published-finding corpus searches for the exact map, five-line base locus, quartic Cremona involution, multidegree, and Nikulin/K3 aliases returned only different Cremona maps and unrelated K3 models.

## Limitations
The claim concerns the very general squarefree, coprime locus. It does not classify the degenerate base schemes when roots of \(c_2d_4\) collide, and it determines only the reduced base locus, not the full scheme structure or a minimal resolution of indeterminacy. The possibility that a classical Cremona classification contains an equivalent abstract transformation under different coordinates remains a residual literature risk; no such identification was found in the inspected sources.

## References
1. A. Clingher, A. Malmendier, F. Poon, *On two-elementary K3 surfaces with finite automorphism group*, arXiv:2206.00269v1, first public 2022-06-01. See Proposition 4.10, Equations (4.22), (4.27), and Remark 4.16.
2. A. Clingher, A. Malmendier, X. Roulleau, *On projective K3 surfaces \(\mathcal X\) with \(\operatorname{{Aut}}(\mathcal X)=(\mathbb Z/2\mathbb Z)^2\)*, arXiv:2305.08959v1, first public 2023-05-15.
