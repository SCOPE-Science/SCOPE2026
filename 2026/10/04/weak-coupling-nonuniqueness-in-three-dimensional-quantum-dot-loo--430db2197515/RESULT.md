# Weak-coupling nonuniqueness in three-dimensional quantum-dot loop optimization
## Finding
Let \(v\ge 0\) be a nonzero radial potential supported in \(B_\rho(0)\subset\mathbb R^3\), with radial profile in \(L^2(0,\rho)\). For a finite array \(Y=\{y_1,\dots,y_N\}\) whose translated support balls are pairwise disjoint, set
\[
W_Y(x)=\sum_{j=1}^N v(x-y_j),\qquad H_{\lambda,Y}=-\Delta-\lambda W_Y.
\]
Choose any Sobolev constant \(C_S\) for which
\[
\|u\|_6^2\le C_S\|\nabla u\|_2^2\qquad (u\in H^1(\mathbb R^3)).
\]
Then
\[
0<\lambda\le \frac1{C_S N^{2/3}\|v\|_{3/2}}
\]
implies
\[
H_{\lambda,Y}\ge0
\]
for every admissible geometry \(Y\). Since a finite compactly supported potential leaves the essential spectrum equal to \([0,\infty)\), it follows that
\[
\inf\sigma(H_{\lambda,Y})=0
\]
uniformly over the admissible array geometry.

Exner's Conjecture 5.3 formulates a unique-maximizer statement for the spectral bottom of arrays placed at equal arc-length positions on a loop of fixed length in dimensions two and three. In dimension three, the displayed weak-coupling interval gives a geometry-independent plateau at zero. Hence, whenever the admissible fixed-loop class contains at least two noncongruent configurations, the literal uniqueness statement cannot hold there. A hypothesis ensuring binding, or an equivalent restriction to configurations with negative spectral bottom, is necessary.

## Assumptions and scope
The potential is attractive and regular: \(v\ge0\), \(v\not\equiv0\), radial, supported in a ball of radius \(\rho\), and its radial profile belongs to \(L^2(0,\rho)\). The number of wells \(N\) is finite and their support balls do not overlap. The result is specific to three dimensions and gives a sufficient, not asserted sharp, weak-coupling interval.

The nonuniqueness conclusion concerns any fixed-length-loop optimization class containing more than one noncongruent admissible configuration. For example, once the length is large enough compared with \(N\rho\), a regular polygon and sufficiently small noncongruent smooth deformations of the loop can both retain pairwise support separation. No assertion is made about the optimal coupling threshold for binding.

## Proof
Because the radial profile lies in \(L^2(0,\rho)\), it also lies in \(L^{3/2}(0,\rho)\). With the radial volume element and bounded support,
\[
\int_{\mathbb R^3} |v(x)|^{3/2}\,dx
=4\pi\int_0^\rho |v(r)|^{3/2}r^2\,dr<\infty,
\]
so \(v\in L^{3/2}(\mathbb R^3)\).

Pairwise disjoint supports give the exact norm identity
\[
\|W_Y\|_{3/2}^{3/2}=N\|v\|_{3/2}^{3/2},
\qquad
\|W_Y\|_{3/2}=N^{2/3}\|v\|_{3/2}.
\]
For \(u\in H^1(\mathbb R^3)\), Hölder's inequality followed by Sobolev gives
\[
\int_{\mathbb R^3}W_Y|u|^2
\le \|W_Y\|_{3/2}\|u\|_6^2
\le C_S N^{2/3}\|v\|_{3/2}\|\nabla u\|_2^2.
\]
Therefore the quadratic form of \(H_{\lambda,Y}\) satisfies
\[
q_{\lambda,Y}[u]
\ge
\bigl(1-\lambda C_S N^{2/3}\|v\|_{3/2}\bigr)\|\nabla u\|_2^2.
\]
Under the stated coupling bound this is nonnegative, proving \(H_{\lambda,Y}\ge0\) uniformly in \(Y\).

The finite sum \(W_Y\) is compactly supported and belongs to the standard form class for which multiplication by the potential is relatively form-compact with respect to \(-\Delta\). Hence
\[
\sigma_{\mathrm{ess}}(H_{\lambda,Y})=[0,\infty).
\]
Combining this with nonnegativity yields \(\inf\sigma(H_{\lambda,Y})=0\). Thus all admissible geometries in the fixed-loop class have the same spectral bottom throughout the weak-coupling interval, which excludes uniqueness whenever the class contains two noncongruent members.

## Verification
The conclusion is analytic and does not rely on finite enumeration or numerical fitting. The critical steps are the exact disjoint-support identity for the \(L^{3/2}\) norm, Hölder's inequality, the three-dimensional Sobolev inequality, and preservation of the free essential spectrum under the finite compactly supported perturbation.

At the endpoint \(\lambda C_S N^{2/3}\|v\|_{3/2}=1\), the proof establishes nonnegativity but does not rule out a zero-energy resonance. This does not affect the spectral-bottom plateau. The coupling threshold is only sufficient and is not claimed optimal.

## Relationship to prior work
Exner's 2023 paper defines the finite regular-well model in dimensions two and three, explicitly introduces the coupling parameter \(\lambda\), and notes that in three dimensions a bound state requires a critical interaction strength. Its Conjecture 5.3 asks for a unique regular-polygon maximizer of the spectral bottom for equal arc-length placements on a loop of fixed length. The present observation combines those model assumptions with a uniform Sobolev bound to show that the literal three-dimensional statement has a nonbinding weak-coupling plateau.

The earlier point-interaction optimization paper proves equidistant optimization for singular interactions on a circle. That singular model does not imply the present regular-potential weak-coupling statement: point interactions bind according to a different renormalized coupling mechanism, whereas the present obstruction is precisely the absence of negative spectrum for sufficiently weak regular potentials in three dimensions.

## Limitations
The constant \(C_S N^{2/3}\|v\|_{3/2}\) is not asserted to give the sharp binding threshold. The argument establishes a sufficient interval of nonbinding, not the full phase diagram. It also does not address the two-dimensional part of the conjecture, where arbitrarily weak attractive regular wells have qualitatively different binding behavior.

There is a terminological caveat: if “principal eigenvalue” in the conjectural discussion is intended to restrict the optimization domain implicitly to configurations that already possess a negative eigenvalue, then the result identifies a necessary missing binding hypothesis rather than contradicting that restricted intended reading.

## References
1. P. Exner, *Geometry effects in quantum dot families*, arXiv:2305.12748, first version 22 May 2023.
2. P. Exner, *An optimization problem for finite point interaction families*, arXiv:1906.01229, first version 4 June 2019.
