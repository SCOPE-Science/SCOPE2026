# Cohomological contraction and a Floquet edge in the trigonometric Nosé–Hoover flow

## Source setting

Szumiński and Llibre introduce the smooth flow on \(\mathbb T^3\)
\[
\dot x=\sin y,\qquad
\dot y=-\sin x-a\sin y\sin z,\qquad
\dot z=b(1-2\cos y),
\]
and record the reversing involution
\[
S(x,y,z)=(x,-y,-z)
\]
as well as the divergence
\[
\operatorname{div}v=-a\cos y\sin z.
\]
They also exhibit the exact periodic orbit
\[
\Gamma_0:\quad (x,y,z)=(0,0,z_0-bt)\pmod{2\pi}
\]
for \(b\ne0\), and use its normal variational equation in their differential-Galois analysis. For \(b=1/2\), their numerical bifurcation diagram reports that the regular branch around this central orbit persists to about \(a\simeq1.6\) and then changes rapidly to chaotic motion.

This note gives two source-specific refinements: an exact cohomological reduction of phase-space contraction, and an exact Hill/Floquet reduction of the central periodic orbit whose first observed stability edge lies at the reported transition scale.

## 1. Exact contraction cohomology

Assume \(b\ne0\). From the thermostat equation,
\[
\cos y=\frac12\left(1-\frac{\dot z}{b}\right).
\]
Substitution into the divergence gives the pointwise identity along every trajectory
\[
\boxed{
\operatorname{div}v
=-\frac a2\sin z-\frac{a}{2b}\frac{d}{dt}(\cos z).
}
\]
Equivalently, if \(X\) denotes the vector field,
\[
\operatorname{div}v=-\frac a2\sin z-\frac{a}{2b}X(\cos z).
\]
Thus the two-variable contraction observable \(-a\cos y\sin z\) is cohomologous to the one-variable observable \(-\tfrac a2\sin z\).

Integrating and using Liouville's formula yields the exact finite-time Jacobian identity
\[
\boxed{
\log\det D\Phi^T(x_0)
=-\frac a2\int_0^T\sin z(t)\,dt
-\frac{a}{2b}\bigl(\cos z(T)-\cos z(0)\bigr).
}
\]
Hence, for every invariant probability measure \(\mu\),
\[
\boxed{
\int\operatorname{div}v\,d\mu=-\frac a2\int\sin z\,d\mu.
}
\]
Whenever the Lyapunov sum exists for an ergodic invariant measure,
\[
\boxed{
\lambda_1+\lambda_2+\lambda_3=-\frac a2\langle\sin z\rangle_\mu.
}
\]
The bounded coboundary contributes nothing to the asymptotic contraction rate.

### Reversibility consequence

Because \(\sin z\circ S=-\sin z\), every invariant measure that is also \(S\)-invariant has
\[
\int\sin z\,d\mu=0,
\qquad
\sum_i\lambda_i=0.
\]
Moreover, if \(\mu\) is any invariant measure, then \(S_*\mu\) is invariant and has the opposite contraction average. Thus a contracting invariant state and its reversed image have equal and opposite Lyapunov sums. This is the source-specific realization of the familiar attractor/repeller pairing in reversible dissipative dynamics; the general phenomenon itself is prior art.

For an \(S\)-symmetric periodic orbit, the integrated divergence over one period vanishes. Since a three-dimensional autonomous periodic orbit has the trivial multiplier \(1\), the product of its two transverse Floquet multipliers is exactly \(1\). Consequently, an \(S\)-symmetric periodic orbit cannot be asymptotically attracting or asymptotically repelling.

## 2. Central orbit as an exact Whittaker–Hill problem

Along \(\Gamma_0\), the source paper derives
\[
\ddot X+a\sin(z_0-bt)\dot X+X=0.
\]
Set \(\theta=z_0-bt\) and make the periodic Liouville substitution
\[
X(t)=\exp\!\left[-\frac{a}{2b}\cos\theta\right]W(t).
\]
Then the first derivative disappears and one obtains the Hill equation
\[
\boxed{
W''+\left[1+\frac{ab}{2}\cos\theta-\frac{a^2}{4}\sin^2\theta\right]W=0,
}
\]
or equivalently
\[
\boxed{
W''+\left[1-\frac{a^2}{8}+\frac{ab}{2}\cos\theta+\frac{a^2}{8}\cos2\theta\right]W=0.
}
\]
This is a two-harmonic Whittaker–Hill equation. The gauge factor is periodic with the orbit period \(T=2\pi/|b|\), so it preserves the Floquet multipliers.

Abel's identity applied directly to the source normal variational equation gives
\[
\det M
=\exp\left[-a\int_0^T\sin(z_0-bt)\,dt\right]
=1
\]
for its transverse monodromy matrix \(M\). Therefore stability is controlled by the single discriminant
\[
\Delta(a,b)=\operatorname{tr}M:
\]
\(|\Delta|<2\) is elliptic, \(|\Delta|>2\) is hyperbolic, and \(\Delta=\pm2\) is a band edge.

## 3. The hidden \(-1\) Floquet collision at the reported \(a\simeq1.6\) transition

For the parameter value used in the source bifurcation diagram, \(b=1/2\), direct high-accuracy integration of the exact normal variational equation gives a band edge in
\[
1.58<a<1.60,
\]
with
\[
\boxed{
a_*\approx1.590316803014779,
\qquad
\Delta(a_*,1/2)=-2,
\qquad
\det M=1.
}
\]
At this value the computed monodromy is, to displayed precision,
\[
M\approx
\begin{pmatrix}
-1&-0.915963428\\
0&-1
\end{pmatrix},
\]
so the transverse multipliers collide at \(-1\). At \(a=1.58\), \(\Delta\approx-1.9304464\), whereas at \(a=1.60\), \(\Delta\approx-2.0645532\); the exact central orbit changes from elliptic to hyperbolic across this edge.

The source paper reports that, for the same \(b=1/2\) and an initial point very close to \(\Gamma_0\), the regular branch persists only to approximately \(a\simeq1.6\), after which the observed motion changes rapidly to chaos. The Floquet calculation therefore identifies a precise local instability mechanism at essentially the same parameter value: the central periodic orbit itself loses transverse ellipticity through a \(-1\) collision. This does **not** prove that the global chaotic transition is a nonlinear period-doubling bifurcation, nor that the local edge alone creates the chaotic attractor; it sharpens the local stability boundary underlying the observed transition.

The numerical value above is a high-accuracy floating-point computation, not an interval-certified enclosure. The exact statements are the cohomological contraction identity, the unit transverse determinant, and the Hill reduction.

## Verification

`artifacts/verify_floquet_contraction.py` independently checks:

- the contraction cohomology identity symbolically;
- the Liouville transformation to the Hill equation symbolically;
- the \(b=1/2\) trace crossing by direct integration of the source normal variational equation;
- the same trace from the transformed Hill equation;
- invariance of the monodromy trace under phase shifts \(z_0\);
- the exact finite-time contraction identity along a representative trajectory.

The recorded run in `artifacts/verification.txt` ends with `all_checks_passed=True`.

## Originality boundary

General Floquet theory, removal of a periodic first-derivative term, reciprocal multiplier structure for reversible/symmetric dynamics, and attractor/repeller pairing in time-reversible dissipative systems are established prior art. In particular, Posch and Hoover (1997) and Sprott (2015) discuss time-reversible dissipative attractors and symmetry breaking in broader classes of flows.

The novelty claim here is deliberately narrower: for the newly introduced trigonometric Nosé–Hoover system of arXiv:2609.19958v1, the explicit contraction cohomology, its exact invariant-measure consequence, the Whittaker–Hill stability reduction of the paper's central orbit, and the source-specific \(-1\) Floquet edge at \(a\approx1.590316803\) were not found in the source paper or in the literature search described in `REVIEW.md`.

## Limitations

- The cohomological identity requires \(b\ne0\); \(b=0\) is a different invariant-torus regime already treated separately in the source paper.
- The Floquet calculation concerns the exact central orbit \(\Gamma_0\), not all periodic branches or the full chaotic invariant set.
- The numerical band-edge value is not formally interval-verified.
- The local \(-1\) collision does not by itself prove a nonlinear flip bifurcation or a global route to chaos.
- No broad novelty is claimed for reversible attractor/repeller theory or periodic-damping Hill equations.

## References

1. W. Szumiński and J. Llibre, *Trigonometric Nosé–Hoover oscillator: chaos, periodic orbits and integrability*, arXiv:2609.19958v1 (2026). https://arxiv.org/abs/2609.19958
2. H. A. Posch and W. G. Hoover, *Time-reversible dissipative attractors in three and four phase-space dimensions*, Phys. Rev. E 55, 6803 (1997). https://doi.org/10.1103/PhysRevE.55.6803
3. J. C. Sprott, *Symmetric Time-Reversible Flows with a Strange Attractor*, Int. J. Bifurcation Chaos 25, 1550078 (2015). https://doi.org/10.1142/S0218127415500789
