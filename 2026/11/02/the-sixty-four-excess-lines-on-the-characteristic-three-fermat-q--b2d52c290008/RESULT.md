# The sixty-four excess lines on the characteristic-three Fermat quartic form a rank-twenty-one lattice

## Finding

Let \(k=\overline{\mathbb F}_3\), and consider the smooth K3 surface
\[
X:\ x_0^4+x_1^4+x_2^4+x_3^4=0\subset\mathbb P^3_k.
\]
The known set \(\mathcal L\) of \(112\) geometric lines admits a canonical partition relative to the fixed diagonal integral model: \(\mathcal C\), its \(48\) classical lines from characteristic zero, and \(\mathcal E=\mathcal L\setminus\mathcal C\), the \(64\) excess lines in characteristic three. When two lines are adjacent precisely if they meet, each classical line meets \(14\) other classical lines and \(16\) excess lines; each excess line meets \(12\) classical lines and \(18\) other excess lines. Hence the equitable adjacency quotient is
\[
\begin{pmatrix}14&16\\12&18\end{pmatrix}.
\]
The induced meeting graph on \(\mathcal E\) has characteristic polynomial
\[
\det(TI-A_{\mathcal E})=(T-18)(T-2)^{43}(T+2)^6(T+6)^{12}(T+10)^2.
\]
Its intersection Gram matrix \(G_{\mathcal E}=A_{\mathcal E}-2I\) has rank \(21\), with inertia \((1,20,43)\) (positive, negative, zero eigenvalues). With \(H\) the hyperplane class, the sum of the \(64\) excess line classes equals \(16H\) in \(\operatorname{NS}(X)\). Those classes span a rank-\(21\) rational subspace; adjoining **any one** of the \(48\) classical line classes yields the entire rank-\(22\) rational Picard space. The integral index is not determined.

## Assumptions and scope

All geometric statements are over the algebraic closure of \(\mathbb F_3\). The Fermat quartic is smooth: its four partial derivatives are nonzero scalar multiples of the coordinate cubes, so they never vanish simultaneously in projective space. For each of the three unordered pairings of the four coordinate positions, and each of the \(4^2\) choices of scalars satisfying \(a^4=b^4=-1\), the equations \(x_i=a x_j\), \(x_r=b x_s\) describe a line on \(X\). These \(48\) lines are exactly the classical characteristic-zero Fermat lines; the remaining \(64\) are excess relative to this fixed diagonal model. The distinction does **not** assert that an excess line cannot deform within a different family.

## Proof

**1. Exhaustive geometric line construction.** Work over \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\), with conjugation \(z\mapsto z^3\). The quartic equation is Hermitian: \(\sum x_i x_i^3=0\). A projective \(\mathbb F_9\)-line is contained in \(X\) exactly when its spanning two-dimensional vector space is totally isotropic for
\[
h(v,w)=\sum_{i=0}^3 v_i^3w_i.
\]
Indeed, the Hermitian polarization vanishes identically on the span exactly when both spanning vectors are isotropic and orthogonal. Enumerate normalized projective vectors in \(\mathbb F_9^4\), obtaining exactly \(280\) isotropic points. For each orthogonal unordered pair of distinct isotropic points, form the ten projective points on its line and deduplicate. The resulting collection has \(112\) distinct generator lines. The established sharp theorem that the Fermat quartic in characteristic three has exactly \(112\) geometric lines makes this finite enumeration *geometrically exhaustive*, not merely exhaustive over the finite field. Filtering by the \(48\) explicit coordinate-pair equations identifies \(48\) classical and \(64\) excess lines.

**2. Exact incidence and spectrum.** Distinct projective lines intersect in at most one point; every geometric intersection between two \(\mathbb F_9\)-rational lines is already rational over \(\mathbb F_9\). Therefore comparing their two ten-element projective point sets detects meeting exactly. Counting separately inside and across the partition yields \(14,16\) for a classical line and \(12,18\) for an excess line. An exact integer characteristic-polynomial calculation on the \(64\times64\) excess adjacency matrix yields the polynomial in the finding, in particular the \(18\)-regularity and eigenvalue \(2\) of multiplicity \(43\). On a smooth quartic K3, a line has self-intersection \(-2\), while two different lines intersect once if they meet and zero otherwise. Thus \(G_{\mathcal E}=A_{\mathcal E}-2I\), with eigenvalues \(16\) once, \(0\) forty-three times, \(-4\) six times, \(-8\) twelve times, and \(-12\) twice. Hence rank \(21\) and inertia \((1,20,43)\).

**3. A divisor identity.** Let \(D=\sum_{L\in\mathcal E}[L]\). Every excess line meets \(18\) other excess lines, hence
\[
D^2=64(-2+18)=1024,\qquad H\cdot D=64,\qquad H^2=4.
\]
Consequently \((D-16H)\cdot H=0\) and \((D-16H)^2=0\). The Hodge index theorem makes the orthogonal complement of the ample class \(H\) negative definite on numerical Néron–Severi classes. Therefore \(D=16H\) numerically. The Néron–Severi group of a K3 surface is torsion-free, and numerical and algebraic equivalence agree there, giving the stated equality of divisor classes. In particular \(H\) belongs to the rational span of the excess lines.

**4. Completing the Picard span.** The exact Gram rank \(21\) equals the dimension of the rational span of the excess classes because that span contains the ample class \(H\), and the intersection form restricts nondegenerately on any subspace containing a positive vector in the signature-\((1,\rho-1)\) Néron–Severi space. Augmenting the \(64\)-line Gram matrix by the intersection row and self-intersection \(-2\) of one classical line increases the rank to \(22\), verified by exact rational elimination. Coordinate permutations and diagonal scalings by fourth roots of unity act transitively on the \(48\) classical lines, preserve the excess set, and hence transport this assertion to any classical line. The Fermat quartic in characteristic three is known to be supersingular with Picard rank \(22\); therefore the resulting rational span is all of \(\operatorname{NS}(X)\otimes\mathbb Q\).

## Verification

Run `python verify.py` using Python 3 and SymPy as stated in `requirements.txt`. The standalone program explicitly constructs \(\mathbb F_9\), all \(280\) isotropic projective points and \(112\) isotropic generator lines, the \(48/64\) partition, the entire meeting graph, the exact induced characteristic polynomial, and the two asserted Gram ranks. All conclusions tested in the program are assertions, and the included `verify_output.txt` is the actual successful execution output. The theoretical Hermitian-line completeness theorem and K3 intersection/Hodge-index facts are the independent mathematical bridge from finite computations to the geometric statements.

## Relationship to prior work

Schütt–Shioda–van Luijk provide the classical Fermat-line formula and reduction/Picard-lattice methods. Rams–Schütt prove the \(112\)-line bound in characteristic three and show that the Fermat model attains it. Degtyarev describes the full \(112\)-line generalized quadrangle and the rank-\(22\) Picard lattice; Veniani proves uniqueness of the \(112\)-line quartic. These results supply foundational geometric inputs, **not** the induced spectrum, the equitable cross-partition, or the rank-\(21\) specialization complement claimed here. In particular the \(64\) excess lines are not the distinct classical Schur quartic's \(64\) lines: that characteristic-zero configuration has a different adjacency spectrum. The specified decomposition is intrinsic to the chosen diagonal equation and its characteristic-zero model, not invariant under every abstract automorphism of the special fiber.

## Limitations

The conclusion concerns embedded geometric lines, their meeting graph and rational divisor spans. No integral saturation, index, elementary divisors, or complete stable deformation functor is claimed. The proof assumes the published \(112\)-line geometric completeness and Picard-rank theorem; the finite-field verifier alone cannot establish either. A full historical-priority determination may require unpublished or unindexed line-lattice coordinate tables associated with earlier full-configuration classifications.

## References

1. M. Schütt, T. Shioda, R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377, initially public 2008-12-12, https://arxiv.org/abs/0812.2377.
2. S. Rams, M. Schütt, *112 lines on smooth quartic surfaces (characteristic 3)*, arXiv:1409.7485, 2014, https://arxiv.org/abs/1409.7485.
3. A. Degtyarev, *Lines in supersingular quartics*, arXiv:1604.05836, 2016, https://arxiv.org/abs/1604.05836.
4. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, arXiv:1608.04209, 2016, https://arxiv.org/abs/1608.04209.
