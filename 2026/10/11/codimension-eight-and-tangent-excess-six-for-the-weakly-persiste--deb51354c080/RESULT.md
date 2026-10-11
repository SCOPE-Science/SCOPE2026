# Codimension eight and tangent excess six for the weakly persistent isochronous cubic locus
## Finding
Let \(\mathcal I\subset\mathbb C^{14}\) be the coefficient locus of the normalized general complex cubic system
\[
\begin{aligned}
\dot z&=z+\varepsilon\left(a_{20}z^2+a_{11}zw+a_{02}w^2+a_{30}z^3+a_{21}z^2w+a_{12}zw^2+a_{03}w^3\right),\\
\dot w&=-w-\varepsilon\left(b_{20}w^2+b_{11}zw+b_{02}z^2+b_{30}w^3+b_{21}zw^2+b_{12}z^2w+b_{03}z^3\right),
\end{aligned}
\]
for which the origin is a weakly persistent isochronous center, in the sense of time-preserving analytic linearizability for every common perturbation parameter covered by the source definition. Let \(\overline{\mathcal I}^{\,Z}\) denote the Zariski closure in \(\mathbb C^{14}\). Then
\[
\dim_{\mathbb C}\overline{\mathcal I}^{\,Z}=6,
\qquad
\operatorname{codim}_{\mathbb C^{14}}\overline{\mathcal I}^{\,Z}=8.
\]
At the zero coefficient vector,
\[
T_0\overline{\mathcal I}^{\,Z}
=\left\{v\in\mathbb C^{14}:v_{a_{21}}=v_{b_{21}}=0}\right\},
\qquad
\dim_{\mathbb C}T_0\overline{\mathcal I}^{\,Z}=12.
\]
Thus the linear system is a singular point with tangent excess \(6\). In particular, six of the eight local codimensions are invisible to first-order parameter-space linearization at the origin.

## Assumptions and scope
The coefficient coordinates are
\[
(a_{20},a_{11},a_{02},a_{30},a_{21},a_{12},a_{03},
 b_{20},b_{11},b_{02},b_{30},b_{21},b_{12},b_{03})\in\mathbb C^{14}.
\]
The proof takes the complete if-and-only-if classification in Theorem 4.10 of arXiv:2609.39761v1 as a published premise and extracts the algebraic geometry of the resulting coefficient locus. Open conditions in families \(I_{19}\), \(I_{20}\), and \(I_{21}\) are handled by taking their Zariski closures. No statement is made about the real conjugacy slice, multiplicities of scheme-theoretic components, or a minimal generating set for the radical ideal of the full locus.

## Proof
Theorem 4.10 states that every point of \(\mathcal I\) satisfies
\[
a_{21}=b_{21}=0
\]
and belongs to one of twenty-one explicitly listed families \(I_{01},\ldots,I_{21}\), with every coefficient not displayed in a family left arbitrary.

For \(I_{01}\) through \(I_{17}\), the displayed conditions are independent linear equations after the common equations \(a_{21}=b_{21}=0\) are included. Their complex dimensions are
\[
\begin{array}{c|c}
\text{families}&\text{dimension}\\ \hline
I_{01},I_{02},I_{03},I_{04}&6\\
I_{06},I_{07}&5\\
I_{05}&4\\
I_{08},I_{09},I_{10},I_{11},I_{14},I_{15}&3\\
I_{12},I_{13},I_{16},I_{17}&2.
\end{array}
\]
For \(I_{18}\), the common equations together with its eight independent linear equations leave a four-dimensional linear slice. On that slice its remaining equation becomes a nonzero cubic hypersurface equation, so its closure has dimension \(3\). Families \(I_{19}\) and \(I_{20}\) are each rationally parameterized by the two nonzero coordinates \(a_{20}\) and \(b_{20}\), hence their closures have dimension \(2\). For \(I_{21}\), after the common, zero-coordinate, and linear relations are imposed, four coordinates remain; on the nonzero torus the two remaining binomial equations are finite over \((a_{30},b_{30})\), so its closure has dimension \(2\). Consequently every classified family has dimension at most \(6\), while \(I_{01}\) is a six-dimensional linear subspace. Hence \(\dim_{\mathbb C}\overline{\mathcal I}^{\,Z}=6\).

For the tangent space, all twenty-one families satisfy \(a_{21}=b_{21}=0\), so
\[
T_0\overline{\mathcal I}^{\,Z}\subseteq
W:=\left\{v:v_{a_{21}}=v_{b_{21}}=0}\right\}.
\]
The six free coordinates of \(I_{01}\) are
\[
a_{11},a_{02},a_{12},a_{03},b_{20},b_{30},
\]
whereas those of \(I_{02}\) are
\[
a_{20},a_{30},b_{11},b_{02},b_{12},b_{03}.
\]
These two coordinate sets are complementary inside \(W\). Since both six-planes pass through the origin and lie in \(\overline{\mathcal I}^{\,Z}\), their tangent spaces are contained in \(T_0\overline{\mathcal I}^{\,Z}\), and together they span all of \(W\). Therefore equality holds and the tangent dimension is \(12\). The local dimension at the origin is \(6\), because a six-dimensional branch passes through it and no branch has larger dimension. Thus the origin is singular with tangent excess \(6\).

## Verification
The standalone checker `artifacts/verify_isochronous_geometry.py` encodes the linear conditions in \(I_{01}\) through \(I_{17}\) over the rationals, recomputes their ranks, verifies the four-dimensional linear slices used for \(I_{18}\) and \(I_{21}\), checks an explicit rank-two Jacobian witness for the two residual equations of \(I_{21}\), and confirms that the free coordinate sets of \(I_{01}\) and \(I_{02}\) are complementary in the twelve-dimensional hyperplane \(a_{21}=b_{21}=0\). Its final output is `VERIFY_OK`.

The computation is only a replay of finite rank and Jacobian checks. The dimension claims for \(I_{18}\), \(I_{19}\), \(I_{20}\), and \(I_{21}\) are justified in the proof by hypersurface or finite-parameter arguments, not by sampling.

## Relationship to prior work
Theorem 4.10 of Li--Liu--Cao--Yu gives the complete twenty-one-family classification used here, but it does not state the dimension, codimension, or Zariski tangent dimension of the resulting full coefficient locus. The same paper emphasizes the algebraic decomposition problem in the fourteen-parameter cubic family. The earlier work of Mencinger--Ferčec--Fernandes--Oliveira introduced linearizable persistent and weakly persistent centers and used affine-variety methods, but its complete weakly persistent calculation is restricted to the semi-Kolmogorov subfamily rather than the general fourteen-parameter cubic family.

The present statement is therefore an algebraic-geometric consequence of the new complete classification: it quantifies how thin the full weakly persistent isochronous locus is and, simultaneously, how degenerate its first-order geometry is at the linear system.

## Limitations
The complete classification in arXiv:2609.39761v1 is used as a literature premise rather than re-derived from its full elimination calculation. The result concerns the reduced set and its Zariski closure; it does not determine the irreducible-component decomposition, tangent cone, multiplicities, local analytic type, or the geometry after imposing real conjugacy conditions. An equivalent dimension-and-tangent statement could exist under different linearizability-variety terminology in older literature not surfaced by the inspected searches.

## References
1. F. Li, H. Liu, C. Cao, and P. Yu, *Complete solution to the weak persistent center and isochronous center problems of cubic polynomial systems*, arXiv:2609.39761v1, 2026. Stable record: https://arxiv.org/abs/2609.39761v1
2. M. Mencinger, B. Ferčec, W. Fernandes, and R. Oliveira, *Linearizability problem of persistent centers*, Electronic Journal of Qualitative Theory of Differential Equations 2018, No. 37. DOI: https://doi.org/10.14232/ejqtde.2018.1.37
