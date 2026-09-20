# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**Verdict: PASS.**

The proof reduces the affine reflected-gradient recurrence to the quadratic characteristic equation
\[
(r^2-r)+\lambda(2r-1)\mu=0
\]
for each eigenvalue \(\mu\) of \(M\). This reduction does not require diagonalizability because the companion determinant is a matrix polynomial in \(M\). Strong monotonicity and the spectral norm bound imply the scaled spectral enclosure \(\operatorname{Re}(\mu/L)\ge\sigma/L\), \(|\mu/L|\le1\).

The unit-circle parameterization was checked symbolically. With \(r=e^{i\theta}\) and \(c=\cos\theta\), the real part and squared modulus of the mapped spectral value reduce to
\[
A(c)/\tau,\qquad B(c)/\tau^2,
\]
with the formulas stated in `RESULT.md`. Eliminating \(c\) using \(t^2=B(c)\) gives
\[
q=\frac{t(3t^2-1)}{2(1-2t^2)}
\]
and therefore the cubic
\[
3t^3+4qt^2-t-2q=0.
\]
The map is strictly increasing from 0 to 1 on \([1/\sqrt3,2/3]\), proving existence and uniqueness of the threshold. A compactness/continuity argument from small positive step size then excludes any earlier loss of Schur stability.

The sharpness witness is a normal two-dimensional rotation-dilation matrix. Its symmetric part and norm attain the assumed bounds exactly, and at the threshold its scaled eigenvalue is the unit-disk point with real part \(q\) used by the unit-circle construction. Thus the companion matrix has a unit-modulus multiplier. The endpoint \(q=1\) reduces to the scalar polynomial with boundary root \(r=-1\) at \(\lambda L=2/3\).

The symbolic verification artifact checks the elimination identities, monotonicity derivative, endpoints, a representative \(q=1/2\) boundary contact, and the numerical specialization \((\sigma,L)=(2,\sqrt5)\). No empirical computation is used as a substitute for the proof.

## Originality

**Verdict: PASS, to the best of our knowledge.**

The closest source is Shehu (arXiv:2609.18355v1, 2026). Its affine unconstrained theorem determines the sharp merely-monotone threshold \(\lambda L=1/\sqrt3\). The same paper separately proves an R-linear strong-monotonicity theorem with the conservative requirement \(\lambda\le\min\{1/(5L),1/(32\sigma)\}\), explicitly notes that the \(\lambda\sigma\le1/32\) ceiling is an artifact, and tests the planar family \(B=\sigma I+J\). It does not state the condition-ratio-dependent sharp affine threshold, the cubic interpolation, or the universal rotation-dilation extremizer proved here.

Malitsky (2015), Maing\'e--Gobinddass (2016), and Yang--Liu (2018) establish linear/R-linear convergence for reflected-gradient-type methods under strong monotonicity, but the located statements do not give this exact affine stability region.

Anagnostides--Panageas (arXiv:2109.04603, SOSA 2022) is a significant nearby result. Its OGD theorem assumes both strong monotonicity and \(1/\widehat L\)-cocoercivity and gives the sharp bound \(2/(3\widehat L)\) for that class. Those hypotheses are different: strong monotonicity plus \(L\)-Lipschitzness alone only yields cocoercivity coefficient \(\sigma/L^2\), so direct application gives \(2\sigma/(3L^2)\), not the threshold here. Their paper was inspected at the theorem and assumption statements.

Huang--Zhang (arXiv:2103.15270) studies strongly monotone Lipschitz VIs and an OGDA direction, but the displayed OGDA result uses separately chosen current-gradient and optimism coefficients rather than the pure reflected-gradient coefficients. Searches using reflected gradient, optimistic gradient, strong monotonicity, affine/linear operators, spectral stability, condition number, rotation, and the derived cubic did not locate an equivalent theorem.

Residual originality risk remains because the result is an elementary root-locus calculation and the control/OGD literature is broad. In particular, older one-step VI papers and general absolute-stability literature could contain an equivalent specialization under different notation. The full theorem texts of Maing\'e--Gobinddass (2016) and Yang--Liu (2018) were not inspected; their accessible abstracts report linear convergence under strong monotonicity but do not advertise an exact conditioning-dependent sharp boundary. This residual risk does not amount to evidence of coverage.

## Value

**Verdict: PASS.**

The result turns the source paper's condition-independent affine threshold into a sharp condition-dependent law for the important strongly monotone subclass. It interpolates continuously between the rotation-dominated \(1/\sqrt3\) barrier and the scalar/cocoercive \(2/3\) barrier, identifies the exact extremal two-dimensional operator, and quantifies how much strong monotonicity can safely enlarge the constant step. It also explains why the source paper's planar validation family is structurally extremal rather than merely illustrative.

## Limitations

The theorem is finite-dimensional, affine, unconstrained, deterministic, and constant-step. It does not extend the sharp range to nonlinear or projected variational inequalities, adaptive or filtered methods, or noisy computation. It characterizes stability, not the step that optimizes the worst-case contraction factor. The result assumes the constants \(\sigma\) and \(L\) are available for tuning.
