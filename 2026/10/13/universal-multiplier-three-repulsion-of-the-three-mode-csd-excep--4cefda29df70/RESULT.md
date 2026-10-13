# Universal multiplier-three repulsion of the three-mode CSD exceptional orbit
## Finding

Consider cyclic steepest descent (CSD) with cycle length
\[
j=2
\]
on a strictly convex quadratic with exactly three active eigenvalues in arithmetic progression,
\[
\lambda_1=m-h,\qquad
\lambda_2=m,\qquad
\lambda_3=m+h,
\qquad
m>h>0.
\]
At a cycle boundary let
\[
p_i=\frac{\|P_i g\|^2}{\|g\|^2},
\qquad
p_i>0,
\qquad
p_1+p_2+p_3=1,
\]
where \(P_i\) is the spectral projector for \(\lambda_i\). Let \(T\) be the projective spectral-weight map after one CSD cycle, that is, after two updates using the same exact steepest-descent step.

The full-support reversal orbit is
\[
p_-=
\left(
\frac38+\frac{\sqrt2}{4},
\frac14,
\frac38-\frac{\sqrt2}{4}
\right),
\]
\[
p_+=
\left(
\frac38-\frac{\sqrt2}{4},
\frac14,
\frac38+\frac{\sqrt2}{4}
\right),
\]
with
\[
T(p_-)=p_+,
\qquad
T(p_+)=p_-.
\]

Its local projective dynamics is universal. In intrinsic simplex coordinates \((p_1,p_2)\),
\[
D(T^2)(p_-)=D(T^2)(p_+)=-3I_2.
\]
Consequently both points of the projective two-cycle are hyperbolic repellers for the two-cycle return map. For every tangent perturbation \(\delta\),
\[
T^2(p_\pm+\delta)-p_\pm
=
-3\delta+O(\|\delta\|^2).
\]
Thus sufficiently small nonzero spectral-weight perturbations expand by a factor tending to \(3\) every two CSD cycles, even though the exact exceptional orbit itself contracts radially.

The multiplier \(3\) is independent of the spectral center \(m\), spacing \(h\), and condition number.

## Assumptions and scope

The objective is a finite-dimensional strictly convex quadratic. Exactly three distinct eigenvalues are active at the cycle boundaries, and all three spectral weights are positive.

The CSD cycle length is exactly \(j=2\): the exact steepest-descent step computed at a cycle boundary is reused for two consecutive gradient updates.

Only projective spectral-weight stability is classified. The radial contraction along the exceptional orbit is a separate quantity and remains strictly smaller than one.

The statement is local. It does not classify the global basin structure of the nonlinear weight map, all exceptional CSD trajectories, or all possible periodic orbits.

## Proof

Affine normalization of the three eigenvalues removes \(m\) and \(h\) from the projective dynamics. Write
\[
z_1=-1,\qquad z_2=0,\qquad z_3=1
\]
so that
\[
\lambda_i=m+h z_i.
\]
For a spectral-weight vector \(p\), define
\[
\mu=\sum_{i=1}^3 z_i p_i.
\]
The exact steepest-descent step at the cycle boundary is
\[
\alpha=\frac{1}{m+h\mu}.
\]
After reusing this step for two gradient updates, the \(i\)-th squared spectral component is multiplied by
\[
(1-\alpha\lambda_i)^4.
\]
The common denominator and the common factor \(h^4\) disappear after projective normalization. Therefore
\[
T_i(p)
=
\frac{p_i(\mu-z_i)^4}
{\sum_{\ell=1}^3p_\ell(\mu-z_\ell)^4}.
\]
This formula is independent of \(m\) and \(h\).

Use intrinsic coordinates
\[
x=p_1,\qquad y=p_2,\qquad p_3=1-x-y.
\]
Then
\[
\mu=1-2x-y.
\]
Put
\[
A=\frac38+\frac{\sqrt2}{4},
\qquad
B=\frac38-\frac{\sqrt2}{4}.
\]
The two orbit points are
\[
p_-=(A,1/4,B),
\qquad
p_+=(B,1/4,A).
\]
Direct substitution into the displayed formula for \(T\) gives
\[
T(p_-)=p_+,\qquad T(p_+)=p_-.
\]

Differentiate the two-coordinate map. At the two orbit points the Jacobians are
\[
DT(p_-)
=
\begin{pmatrix}
5-\frac{7\sqrt2}{2} & \frac{\sqrt2}{4}\\
7\sqrt2 & 5+\frac{7\sqrt2}{2}
\end{pmatrix},
\]
and
\[
DT(p_+)
=
\begin{pmatrix}
5+\frac{7\sqrt2}{2} & -\frac{\sqrt2}{4}\\
-7\sqrt2 & 5-\frac{7\sqrt2}{2}
\end{pmatrix}.
\]
Multiplying in either return order gives
\[
DT(p_+)DT(p_-)
=
DT(p_-)DT(p_+)
=
-3I_2.
\]
By the chain rule,
\[
D(T^2)(p_-)=D(T^2)(p_+)=-3I_2.
\]

Because \(T^2\) is smooth on the interior of the simplex,
\[
T^2(p_\pm+\delta)-p_\pm
=
-3\delta+O(\|\delta\|^2).
\]
Hence, for all sufficiently small nonzero \(\delta\), the norm of the projective displacement increases after one return. The two-cycle is therefore hyperbolically repelling.

## Verification

The standalone script `artifacts/verify_csd_repeller.py` reconstructs the normalized projective map symbolically, verifies the exact reversal orbit, differentiates the map, and checks
\[
D(T^2)(p_\pm)=-3I_2
\]
with exact symbolic arithmetic.

The script verifies algebraic identities only. The local-instability conclusion follows analytically from the derivative and the smooth Taylor expansion.

## Relationship to prior work

Li and Wang construct exact counterexamples to R-superlinear convergence of CSD and give the full-support three-dimensional example with spectrum
\[
(1,2,3),
\]
cycle length \(j=2\), and an exact projective period-two orbit. Their full preprint gives the orbit and its radial contraction, but targeted full-text searches do not state a Jacobian, local stability classification, or projective multiplier for that orbit.

The same normalized projective map applies to every affine image of the spectrum \((-1,0,1)\), so the local multiplier computed here is independent of condition number. The result therefore complements the exact counterexample: the orbit is radially contracting but projectively repelling.

Recent work on generic CSD convergence studies behavior away from exceptional sets. The multiplier-three law supplies a local dynamical explanation for why a concrete full-support exceptional orbit need not be robust under perturbation of its spectral weights.

Targeted semantic searches for CSD projective-orbit stability, Jacobian multipliers, repelling period-two behavior, and the numerical multiplier \(3\) did not locate an implication-equivalent published statement.

## Limitations

The result is local and applies only to the stated three-mode arithmetic-spectrum orbit with cycle length \(j=2\).

A hyperbolic repeller does not by itself determine where perturbed trajectories go globally or prove a quantitative measure estimate for the exceptional set.

The projective multiplier does not equal the radial convergence factor. The exact orbit still contracts in the original error and gradient variables.

The argument does not address spectra with four or more active eigenvalues, other cycle lengths, or nonquadratic objectives.

## References

1. Y. Li, Q. Wang, *Exact counterexamples to R-superlinear convergence of cyclic steepest descent*, Zenodo record 22209278, version 3.0, first public 31 August 2026, DOI: 10.5281/zenodo.22209278; later arXiv:2610.00939v1.
2. R. Gu, *Doubly exponential convergence of the cyclic steepest descent method for strictly convex quadratics in arbitrary dimensions*, arXiv:2609.25800v1.
