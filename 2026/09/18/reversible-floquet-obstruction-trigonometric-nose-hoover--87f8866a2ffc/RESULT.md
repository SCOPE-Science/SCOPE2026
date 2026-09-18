# Reversible Floquet obstruction in the trigonometric Nosé–Hoover oscillator

## Statement

Consider the trigonometric Nosé–Hoover flow introduced by Szumiński and Llibre,
\[
\dot x=\sin y,\qquad
\dot y=-\sin x-a\sin y\sin z,\qquad
\dot z=b(1-2\cos y)
\]
on \(\mathbb T^3\), with \(b\ne0\). It is reversible under
\[
S(x,y,z)=(x,-y,-z)
\]
and has divergence
\[
\operatorname{div}v=-a\cos y\sin z.
\]

### Theorem 1 — symmetric periodic orbits cannot attract

Let \(\gamma\) be a periodic orbit that is invariant as a set under the reversing involution \(S\). Then
\[
\int_\gamma \operatorname{div}v\,dt=0.
\]
Consequently, if \(1,\mu_1,\mu_2\) are its Floquet multipliers, with \(1\) the trivial multiplier of the flow direction, then
\[
\boxed{\mu_1\mu_2=1.}
\]
Hence an \(S\)-symmetric periodic orbit is never asymptotically attracting and never asymptotically repelling. If it is hyperbolic, it is necessarily saddle-type.

### Corollary 1 — the entire explicit periodic family is non-attracting

The exact family
\[
\varphi_{k,s}(t)=
\left(k\pi,s\pi,z_0+b[1-2(-1)^s]t\right)\pmod{2\pi}
\]
is \(S\)-symmetric for every \(k,s\in\mathbb Z\). Therefore every member has reciprocal transverse multipliers and none can be an attracting or repelling periodic orbit, for any \(a\) and any \(b\ne0\).

For \(s\) even its primitive period is \(2\pi/|b|\); for \(s\) odd it is \(2\pi/(3|b|)\).

### Corollary 2 — exact classification at \(a=0\)

Along \(\varphi_{k,s}\), when \(a=0\), the normal variational equations reduce to
\[
\dot X=(-1)^sY,\qquad
\dot Y=-(-1)^kX.
\]
Writing \(T_s=2\pi/(|b|\,|1-2(-1)^s|)\), the two transverse multipliers are

\[
\begin{cases}
e^{\pm iT_s},&k+s\ \text{even},\\[2mm]
e^{\pm T_s},&k+s\ \text{odd}.
\end{cases}
\]

Thus the same-parity members are elliptic or parabolic at resonant periods, while opposite-parity members are hyperbolic saddles.

### Corollary 3 — all-parameter Hill reduction for the central orbit

For
\[
\varphi_{0,0}(t)=(0,0,z_0-bt),
\]
the source paper derives the normal variational equation
\[
X''+a\sin(z_0-bt)X'+X=0.
\]
With
\[
X(t)=u(t)\exp\!\left[-\frac{a}{2b}\cos(z_0-bt)\right],
\]
this becomes the Hill equation
\[
u''+
\left[
1+\frac{ab}{2}\cos(z_0-bt)-\frac{a^2}{4}\sin^2(z_0-bt)
\right]u=0.
\]
Equivalently, using \(z=z_0-bt\),
\[
u_{zz}+
\left[
\frac{1-a^2/8}{b^2}
+\frac{a}{2b}\cos z
+\frac{a^2}{8b^2}\cos2z
\right]u=0.
\]
Its monodromy has determinant one. If \(\Delta(a,b)\) denotes its Floquet discriminant, the central periodic orbit therefore has the exact trichotomy
\[
|\Delta|<2 \Rightarrow \text{elliptic},\qquad
|\Delta|>2 \Rightarrow \text{saddle},\qquad
|\Delta|=2 \Rightarrow \text{parabolic}.
\]
In particular, it has no focus-type attracting or repelling regime.

### Theorem 2 — attractor–repeller pairing

For any periodic orbit \(\gamma\), \(S\gamma\) is also periodic. If \(\gamma\) is not \(S\)-symmetric, then its partner is distinct and their nontrivial Floquet spectra are reciprocal. Therefore every asymptotically attracting periodic orbit has a distinct asymptotically repelling \(S\)-partner.

The system also has the ordinary symmetry
\[
R(x,y,z)=(-x,-y,z).
\]
Thus, unless additional setwise symmetries identify them, a nonsymmetric attracting orbit can occur together with an \(R\)-related attracting copy and the corresponding \(S\)- and \(RS\)-related repelling copies.

## Proof

Because \(\gamma\) is \(S\)-symmetric, after a phase shift there exists \(t_0\) such that
\[
S\gamma(t)=\gamma(t_0-t).
\]
The divergence is odd under the reverser:
\[
\operatorname{div}v(S(x,y,z))
=-\operatorname{div}v(x,y,z).
\]
Therefore, over one period \(T\),
\[
\begin{aligned}
I&=\int_0^T\operatorname{div}v(\gamma(t))\,dt\\
&=\int_0^T\operatorname{div}v(S\gamma(t_0-t))\,dt\\
&=-\int_0^T\operatorname{div}v(\gamma(t_0-t))\,dt=-I,
\end{aligned}
\]
so \(I=0\). Liouville's formula gives
\[
\det M(T)=e^I=1.
\]
An autonomous periodic orbit has a trivial multiplier \(1\), so the product of its two transverse multipliers is one. Both cannot have modulus below one or both above one.

Equivalently, differentiating the reversibility relation
\[
S\Phi^t=\Phi^{-t}S
\]
shows that the monodromy of \(S\gamma\) is conjugate to the inverse monodromy of \(\gamma\). If \(S\gamma=\gamma\), the spectrum is invariant under \(\mu\mapsto\mu^{-1}\). If \(S\gamma\ne\gamma\), this gives the attractor–repeller pairing.

For the explicit family, \(y=s\pi\equiv-s\pi\pmod{2\pi}\), and the \(z\)-motion winds around the full circle when \(b\ne0\), so \(S\) maps the orbit set to itself. Directly,
\[
\operatorname{div}v(\varphi_{k,s}(t))
=-a(-1)^s\sin\!\left(z_0+b[1-2(-1)^s]t\right),
\]
whose integral over a period is zero.

At \(a=0\), linearization along \(\varphi_{k,s}\) gives the two-dimensional system stated above; differentiating once yields
\[
X''=-(-1)^{k+s}X,
\]
which gives the exact multipliers. The Hill reduction follows from the standard removal of the first-derivative term in the source paper's normal variational equation.

## Consequences for the source paper

The source describes \(\varphi_{0,0}\) as a "stable periodic solution" in the small-\(a\) regime and separately reports a stable attracting periodic orbit in a regular window near \(a\simeq4.8\). The theorem above distinguishes these statements sharply:

- \(\varphi_{0,0}\) may be elliptic and Lyapunov-stable in an appropriate sense, but it cannot be asymptotically attracting.
- Any genuinely attracting periodic orbit must break the reversing symmetry and must have a distinct repelling time-reversed partner.
- A generic dissipative period-doubling cascade of an attracting orbit therefore cannot occur on the explicit \(S\)-symmetric family itself.

This does not contradict the reported attracting regular window; it constrains the symmetry and the unseen backward-time partner of the attracting orbit observed there.

## Limitations

The result does not determine the full stability diagram \(\Delta(a,b)\) of the Hill equation, prove nonlinear/KAM stability in elliptic regions, or establish the existence of the numerically reported attracting orbit. The statement concerns exact periodic-orbit Floquet structure in the unperturbed reversible model and does not survive arbitrary symmetry-breaking perturbations. The case \(b=0\) is excluded from the periodic-family statement because the displayed family then degenerates to equilibria.

The reciprocal-multiplier property of symmetric periodic orbits in reversible systems is classical and is not claimed as new. The contribution here is its exact application to the newly introduced trigonometric Nosé–Hoover model, the all-parameter obstruction for the explicit family, the \(a=0\) parity classification, the Hill-form stability trichotomy for \(\varphi_{0,0}\), and the resulting symmetry constraint on the reported attracting periodic windows.

## References

1. W. Szumiński and J. Llibre, *Trigonometric Nosé–Hoover oscillator: chaos, periodic orbits and integrability*, arXiv:2609.19958v1 (2026). https://arxiv.org/abs/2609.19958
2. J. S. W. Lamb and J. A. G. Roberts, *Time-reversal symmetry in dynamical systems: a survey*, Physica D 112 (1998), 1–39. https://doi.org/10.1016/S0167-2789(97)00199-1
