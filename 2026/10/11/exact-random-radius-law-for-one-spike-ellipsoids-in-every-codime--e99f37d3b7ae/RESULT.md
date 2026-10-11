# Exact random-radius law for one-spike ellipsoids in every codimension

## Finding

Let
\[
E_{a,b}^{N}
=
\left\{
x\in\mathbb R^N:
\frac{x_1^2}{a^2}+
\sum_{j=2}^{N}\frac{x_j^2}{b^2}
\le1
\right\},
\qquad
a>b>0,
\]
and let \(E_n\) be a Haar-uniform random subspace of codimension \(n\), where
\[
N\ge2,
\qquad
1\le n<N.
\]
Write
\[
R_n
=
\operatorname{rad}(E_{a,b}^{N}\cap E_n).
\]

If
\[
T\sim\operatorname{Beta}\!\left(\frac n2,\frac{N-n}{2}\right),
\]
then the random section radius has the exact distributional representation
\[
\boxed{
R_n
\overset{d}=
\left(
a^{-2}+(b^{-2}-a^{-2})T
\right)^{-1/2}.
}
\]

Thus, for \(b\le r\le a\),
\[
\boxed{
\mathbb P(R_n\le r)
=
1-I_{\tau(r)}\!\left(\frac n2,\frac{N-n}{2}\right),
\qquad
\tau(r)
=
\frac{r^{-2}-a^{-2}}{b^{-2}-a^{-2}},
}
\]
where \(I_x(\alpha,\beta)\) denotes the regularized incomplete beta function.

Writing
\[
\kappa=\frac ab>1,
\]
all positive moments are
\[
\boxed{
\mathbb E R_n^q
=
a^q\,{}_2F_1\!\left(
\frac q2,\frac n2;\frac N2;-(\kappa^2-1)
\right),
\qquad q>0.
}
\]

The smallest radius among all codimension-\(n\) sections is exactly \(b\). Hence the exact probability that random information is within a factor \(C\) of optimal information is, for \(1\le C\le\kappa\),
\[
\boxed{
\mathbb P(R_n\le Cb)
=
1-I_{\theta_C}\!\left(\frac n2,\frac{N-n}{2}\right),
\qquad
\theta_C
=
\frac{\kappa^2/C^2-1}{\kappa^2-1}.
}
\]
It is \(0\) for \(C<1\) and \(1\) for \(C\ge\kappa\).

In the high-anisotropy limit,
\[
\boxed{
\frac{R_n}{b}
\Longrightarrow
T^{-1/2}
\qquad(\kappa\to\infty).
}
\]
Consequently, if \(N\to\infty\), \(n/N\to\lambda\in(0,1)\), and \(\kappa\to\infty\), then
\[
\boxed{
\frac{R_n}{b}
\longrightarrow
\lambda^{-1/2}
}
\]
in probability. Thus the familiar \(\sqrt{N/n}\) degradation of random versus optimal information is attained exactly, asymptotically, by the one-spike ellipsoid.

## Assumptions and scope

The ellipsoid is Euclidean, centered, and has exactly two distinct semiaxis lengths: one long semiaxis \(a\) and \(N-1\) equal short semiaxes \(b\). The random subspace is distributed according to normalized Haar measure on the Grassmannian.

The theorem gives the complete one-dimensional law of the random radius for every finite \(N\) and every codimension \(n\). It does not give the complete spectrum or volume of the random section ellipsoid.

The probability formula concerns Euclidean worst-case recovery error, which is the radius of the kernel section in the Hilbert ellipsoid model used in the random-information literature.

## Proof

Let
\[
Q
=
\operatorname{diag}(a^{-2},b^{-2},\ldots,b^{-2}).
\]
Then
\[
E_{a,b}^{N}
=
\{x:\langle Qx,x\rangle\le1\}.
\]
For a fixed subspace \(E\), the squared reciprocal of the section radius is the smallest eigenvalue of the quadratic form restricted to \(E\):
\[
\operatorname{rad}(E_{a,b}^{N}\cap E)^{-2}
=
\lambda_{\min}(Q|_E).
\]

Write
\[
\alpha=a^{-2},
\qquad
\beta=b^{-2},
\qquad
\gamma=\beta-\alpha>0.
\]
Then
\[
Q
=
\beta I-\gamma e_1e_1^{\mathsf T}.
\]
Compressing this rank-one perturbation to \(E\) gives
\[
Q|_E
=
\beta I_E
-
\gamma(P_Ee_1)(P_Ee_1)^{\mathsf T}.
\]
If
\[
S=\|P_Ee_1\|^2,
\]
then the eigenvalues of \(Q|_E\) are
\[
\beta-\gamma S
\]
once, and \(\beta\) with multiplicity \(N-n-1\). Hence
\[
\operatorname{rad}(E_{a,b}^{N}\cap E)
=
\left(\beta-\gamma S\right)^{-1/2}.
\]

For Haar-uniform \(E=E_n\), the squared projection of a fixed unit vector onto the orthogonal complement \(E_n^{\perp}\), which has dimension \(n\), is beta distributed:
\[
T
:=
\|P_{E_n^{\perp}}e_1\|^2
\sim
\operatorname{Beta}\!\left(\frac n2,\frac{N-n}{2}\right).
\]
Since \(S=1-T\),
\[
\beta-\gamma S
=
\alpha+(\beta-\alpha)T,
\]
which proves the distributional identity.

The cumulative distribution follows because the map
\[
t\longmapsto
\left(\alpha+(\beta-\alpha)t\right)^{-1/2}
\]
is strictly decreasing. For \(b\le r\le a\), the event \(R_n\le r\) is exactly
\[
T\ge
\frac{r^{-2}-a^{-2}}{b^{-2}-a^{-2}}.
\]
This gives the regularized-beta formula.

For the moments, factor out \(a^{-2}\):
\[
R_n^q
=
a^q
\left(1+(\kappa^2-1)T\right)^{-q/2}.
\]
Euler's beta integral for the Gauss hypergeometric function yields
\[
\mathbb E R_n^q
=
a^q\,{}_2F_1\!\left(
\frac q2,\frac n2;\frac N2;-(\kappa^2-1)
\right).
\]

Every codimension-\(n\) subspace has dimension \(N-n\) and therefore its section radius is at least \(b\): if the subspace has a nonzero component in the long-axis direction, the radius is larger, while a subspace contained in \(e_1^{\perp}\) has radius exactly \(b\). Hence \(b\) is the optimal-information radius. Substituting \(r=Cb\) into the CDF gives the factor-\(C\) probability.

Finally,
\[
\frac{R_n}{b}
=
\frac{\kappa}{\sqrt{1+(\kappa^2-1)T}}
=
\left(T+\frac{1-T}{\kappa^2}\right)^{-1/2}.
\]
For fixed \(N,n\), this converges almost surely to \(T^{-1/2}\) because \(T>0\) almost surely. If also \(n/N\to\lambda\in(0,1)\), then
\[
\mathbb ET=\frac nN,
\qquad
\operatorname{Var}(T)
=
\frac{2n(N-n)}{N^2(N+2)},
\]
so \(T\to\lambda\) in probability. The last assertion follows by continuity.

## Verification

The bundled checker independently verifies the rank-one compression formula on deterministic random Grassmannian samples, compares numerical beta integrals with the hypergeometric moment formula, checks the closed beta mean and variance, and confirms the factor-\(C\) threshold transformation.

These finite checks are supplementary. The all-dimensional theorem follows from the rank-one compression identity and the standard beta law for a fixed vector's squared projection onto a Haar random subspace.

The primary 2026 source was inspected through its definition of random radius, its comparison with optimal Gelfand information, and its ellipsoid applications. The earlier full ellipsoid paper was inspected through its problem formulation and theorem statements on high-probability and order estimates.

## Relationship to prior work

Guedon, Litvak, Tatarko, and Vritsiou study random radii of arbitrary convex bodies and apply their general bounds to \(p\)-ellipsoids, obtaining sharp estimates in many parameter regimes. They emphasize the comparison between random and optimal information and note that the factor \(\sqrt{N/n}\) may be unavoidable for small codimension.

Hinrichs, Krieg, Novak, Prochno, and Ullrich previously studied random sections of Hilbert ellipsoids. Their full formulation identifies the minimal codimension-\(n\) radius as the \((n+1)\)-st semiaxis and develops high-probability and expected-radius estimates for general semiaxis sequences.

Those results address broad semiaxis sequences by inequalities and asymptotic orders. The present theorem instead gives the complete finite-dimensional distribution, all positive moments, and the exact random-versus-optimal success curve for the canonical one-spike sequence
\[
(a,b,\ldots,b).
\]
Targeted searches under random-section, Gaussian-information, one-spike, axisymmetric-ellipsoid, beta-law, and exact-distribution terminology found no prior statement of this full law.

## Limitations

The exact beta reduction relies on the quadratic form being a scalar matrix plus a rank-one perturbation. It does not extend directly to ellipsoids with three or more distinct semiaxis levels, where a random compression has several nontrivial eigenvalues.

The theorem gives an exact benchmark for random information but does not improve the general high-probability inequalities for arbitrary convex bodies.

An equivalent one-spike computation may exist in older multivariate-statistics or random-matrix literature under different terminology. This remains the main bibliographic residual risk.

## References

1. O. Guedon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131v1, 21 September 2026.
2. A. Hinrichs, D. Krieg, E. Novak, J. Prochno, M. Ullrich, *Random sections of ellipsoids and the power of random information*, Transactions of the American Mathematical Society 374 (2021), 8691--8713; arXiv:1901.06639v2.
3. A. Hinrichs, J. Prochno, M. Sonnleitner, *Random sections of \(\ell_p\)-ellipsoids, optimal recovery and Gelfand numbers of diagonal operators*, Journal of Complexity 72 (2022), 101656; arXiv:2109.14504.
