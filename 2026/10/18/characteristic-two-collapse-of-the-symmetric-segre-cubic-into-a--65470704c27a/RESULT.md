# Characteristic-two collapse of the symmetric Segre cubic into a Hermitian cone

## Finding
Let \(\mathcal X\subset\mathbb P^5_{\mathbb Z}\) be the coefficientwise integral projective scheme
\[
\mathcal X=V\!\left(\sum_{i=0}^5 Z_i,\;\sum_{i=0}^5 Z_i^3\right).
\]
For an algebraically closed field \(k\) of characteristic \(p\), let \(X_p=\mathcal X\times_{\mathbb Z}k\). The following is a complete geometric description of this **specified symmetric-coordinate model**, not of every integral model of the six-point moduli space.

1. If \(p=0\) or \(p\ge5\), \(X_p\) is a normal cubic threefold with exactly ten ordinary double points, indexed by the unordered partitions of six indices into two triples.
2. If \(p=2\), \(X_2\) is the projective cone with vertex \(v=[1:1:1:1:1:1]\) over a smooth nondegenerate Hermitian cubic surface \(S\subset\mathbb P^3_{\mathbb F_4}\). Its **entire scheme-theoretic projective singular locus** is supported at \(v\), with affine local algebra
   \[
   \mathcal O_{\operatorname{Sing}(X_2),v}\simeq k[y_1,y_2,y_3,y_4]/(y_1^2,y_2^2,y_3^2,y_4^2).
   \]
   It has length \(16\), Hilbert function \((1,4,6,4,1)\), and the hypersurface has multiplicity \(3\) at \(v\). The threefold contains **exactly 27 projective planes**, all defined over \(\mathbb F_4\), and all containing \(v\). Exactly \(135\) of their \(351\) unordered pairs meet along a projective line; the other \(216\) pairs meet only at \(v\). The distinct pairwise intersection lines correspond to the \(45\) points of \(S(\mathbb F_4)\), with exactly three planes passing through each such line.
3. If \(p=3\), the scheme \(X_3\) is \(\mathbb P_k^4\), since the cubic equation vanishes identically on the hyperplane. In particular, \(\mathcal X\to\operatorname{Spec}\mathbb Z\) is not flat at three, but its restriction over \(\mathbb Z[1/3]\) is flat.

## Assumptions and scope
The coordinates are the **literal six integral coordinates** of the displayed power-sum model, with no characteristic-dependent renormalization. All statements about singularities concern geometric fibers over an algebraically closed field. The phrase “singular scheme” means the projective Jacobian/Tjurina scheme of the relative cubic hypersurface inside its hyperplane \(H_k\simeq\mathbb P_k^4\). A projective plane is a linearly embedded \(\mathbb P_k^2\subset X_2\), counted geometrically. The Hermitian surface is the nonsingular degree-three surface given by a nondegenerate Frobenius-Hermitian form on a four-dimensional \(\mathbb F_4\)-vector space. No assertion identifies the special fibers with a characteristic-independent graphical or GIT quotient presentation.

## Proof
**Ordinary characteristic.** When \(p\ne3\), the linear equation defines \(H_k\cong\mathbb P^4_k\) and the restricted cubic is not identically zero. A point of \(X_p\) is singular if and only if the six partial derivatives of \(F=\sum Z_i^3\) agree modulo the conormal to \(H_k\), i.e., the six squares \(Z_i^2\) agree (because \(3\) is invertible). If their common value were zero, all projective coordinates would vanish. Over an algebraically closed field of characteristic different from two, each coordinate is therefore \(\varepsilon_i a\), with \(a\ne0\) and \(\varepsilon_i\in\{1,-1\}\). The condition \(\sum Z_i=0\) says \(2r-6=0\) in \(k\), where \(r\) is the number of plus signs. For \(p=0\) or \(p\ge5\), only \(r=3\) is possible. Overall sign identifies the complementary triples, leaving \(\binom63/2=10\) points. Euler's identity shows that the cubic equation is automatic at these critical points. The affine tangent quadratic form is the restriction of \(3\sum_i Z_i (\delta Z_i)^2\), whose polar form is \(6\operatorname{diag}(Z_i)\). On the five-dimensional linear tangent hyperplane \(\sum_i\delta Z_i=0\), its radical is exactly the radial direction \(\langle Z\rangle\), because \(\operatorname{diag}(Z_i)^{-1}(1,\dots,1)\) is proportional to \(Z\). It induces a nondegenerate quadratic form on the four-dimensional projective tangent space. Each point is thus an ordinary quadratic double point with reduced Jacobian local algebra. Since the singular locus has codimension three, the cubic hypersurface is normal by Serre's criterion.

**The characteristic-two cone.** Put \(v=(1,1,1,1,1,1)\). In characteristic two \(\sum_i v_i=0\). Both defining equations are invariant under \(Z\mapsto Z+t v\): for the cubic, the expansion is
\[
\sum_i(Z_i+t)^3=\sum_i Z_i^3+t\sum_i Z_i^2+t^2\sum_i Z_i+6t^3=\sum_i Z_i^3
\]
because \(\sum_iZ_i=0\) and \(\sum_i Z_i^2=(\sum_i Z_i)^2=0\). Thus projection from \(v\) makes \(X_2\) a cone. Choose its linear complement in \(H_k\) by setting \(Z_5=0\); write \(Z_0=y_1,\ldots,Z_3=y_4\) and \(Z_4=y_1+\cdots+y_4\). The cubic base equation becomes
\[
 f(y_1,\ldots,y_4)=\sum_{i=1}^4 y_i^3+\left(\sum_{i=1}^4 y_i\right)^3
 =\sum_{i\ne j}y_i^2y_j.
\]
With \(J\) the all-ones \(4\times4\) matrix over \(\mathbb F_2\), its partial derivatives satisfy
\[
 (\partial_1 f,\ldots,\partial_4 f)^T=(I+J)(y_1^2,\ldots,y_4^2)^T,
 \qquad (I+J)^2=I
\]
since \(J^2=4J=0\). Hence \(\nabla f=0\) only at \(y=0\); the base surface is smooth. Moreover \(f=\sum_i y_i\partial_i f\), by Euler's identity in characteristic two, so in the affine chart at the cone vertex the complete Tjurina ideal is exactly \((y_1^2,\ldots,y_4^2)\). This yields the asserted local algebra and Hilbert function, and also shows scheme-theoretically that there are no singular points away from the vertex. The initial equation has degree three, so the vertex multiplicity is three. Over \(\mathbb F_4\), the same polynomial is a Hermitian form \(y^{(2)T}(I+J)y\) with nonsingular coefficient matrix, establishing the claimed Hermitian structure. The threefold is normal because it is a hypersurface with an isolated singularity in dimension three.

**All planes and their intersections.** A smooth cubic surface over an algebraically closed field has exactly \(27\) lines (the classical \(27\)-line theorem, valid in characteristic two). An explicit exhaustive \(\mathbb F_4\)-linear calculation in the attached checker finds \(45\) points of \(S(\mathbb F_4)\), exactly \(27\) \(\mathbb F_4\)-lines fully contained in \(S\), and exactly three such lines through every rational point. Thus these are all geometric lines, with no others defined over a field extension. Any plane contained in the threefold cone projects from \(v\) into \(S\). If it did not contain \(v\), its projected image would be a plane in the smooth irreducible cubic surface, impossible; therefore each plane is the span of \(v\) and a unique line on \(S\). Two of these planes meet along the line from \(v\) to a point precisely if their base lines meet. Their base-line intersections are \(\mathbb F_4\)-rational. There are \(45\binom32=135\) such pairs, while \(\binom{27}2-135=216\) pairs have intersection exactly \(v\). This also accounts for all \(45\) distinct intersection lines.

**Characteristic three and flatness.** In characteristic three, \(\sum_i Z_i^3=(\sum_iZ_i)^3\), hence \((L,F)=(L)\), and \(X_3\simeq\mathbb P^4_k\). For every characteristic other than three, the restriction \(F|_{H_k}\) is a nonzero cubic, so it defines a relative effective Cartier divisor inside the flat projective bundle \(\mathbb P^4_{\mathbb Z[1/3]}\); this proves flatness over that base. The special fiber at three has dimension four, so flatness fails there.

## Verification
The accompanying Python 3 checker is `verify_segre_reduction.py`. Execute `python verify_segre_reduction.py`. It uses exact finite-field arithmetic, enumerating all \(85\) points and \(357\) lines in \(\mathbb P^3(\mathbb F_4)\); it checks the \(45\)-point/\(27\)-line Hermitian incidence, its \(135\) intersecting and \(216\) skew pairs, the local Jacobian coefficient-matrix identity, and all singular projective points in characteristics five and seven. Expected final output is `VERIFY_OK`. These finite tests independently corroborate the proof; they do **not** prove the arbitrary-characteristic parts, for which the symbolic Jacobian and tangent-form arguments above are essential.

## Relationship to prior work
The power-sum equations and ten-node characteristic-zero geometry of the Segre cubic are classical. Howard–Millson–Snowden–Vakil describe the six-point moduli space and explicitly give these usual equations in Section 2.10 of their 2006 treatment; they observe that the usual power-sum presentation fails in characteristic three while their graphical presentation is integral. Their study of local rank-one matrix cones concerns the intrinsic moduli construction, not the coefficientwise reduction of the displayed power sums. In their 2007 companion paper, Section 2.4, the comparison between six-point invariants and the symmetric coordinates uses a factor \(1/2\); consequently, equality of integral models at the prime two cannot be inferred. The classical \(27\)-line theorem and Hermitian surface counts are used as established background. The proposed specific contribution is the *combined exceptional-prime degeneration, nonreduced vertex Jacobian scheme, and the complete \(27\)-plane incidence structure of the literal symmetric equation*, not those prior elementary or classical statements.

## Limitations
This result does not assert that the canonical GIT model of six ordered points has a single singular point in characteristic two: the theorem concerns only the coefficientwise power-sum integral model. The projective singular scheme in characteristic two is nonreduced, even though the underlying threefold is normal and reduced. The enumerative incidence certificate is over \(\mathbb F_4\), and the inference that it exhausts geometric lines invokes the classical smooth cubic-surface \(27\)-line theorem. No classification of deformations, resolutions, or canonical integral moduli models is claimed. An equivalent formulation in unindexed historical literature cannot be ruled out solely by a negative search.

## References
- B. Howard, J. Millson, A. Snowden, R. Vakil, *The projective invariants of ordered points on the line*, arXiv:math/0505096 (first posted 5 May 2005), https://arxiv.org/abs/math/0505096.
- B. Howard, J. Millson, A. Snowden, R. Vakil, *The moduli space of n points on the line is cut out by simple quadrics when n is not six*, arXiv:math/0607372 (first posted 16 July 2006), https://arxiv.org/abs/math/0607372. For the full treatment, *The equations for the moduli space of n points on the line*, Section 2.10, https://www.math.umd.edu/~millson/papers/hmsvfinalversion.pdf.
- B. Howard, J. Millson, A. Snowden, R. Vakil, *A description of the outer automorphism of S6, and the invariants of six points in projective space*, arXiv:0710.5916 (31 October 2007), Section 2.4, https://arxiv.org/abs/0710.5916.
- Classical smooth cubic-surface \(27\)-line theorem and nondegenerate finite Hermitian surface incidence; the exact finite-field incidence is checked in the standalone artifact.
