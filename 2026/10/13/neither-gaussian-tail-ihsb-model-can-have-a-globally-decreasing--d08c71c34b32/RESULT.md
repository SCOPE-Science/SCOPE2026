# Neither Gaussian-tail IHSB model can have a globally decreasing hazard
## Finding
The 2026 inverse-hazard size-biased construction introduces two new lifetime families based on half-normal and Maxwell baselines. For either family, let
\[
\alpha>0,\qquad \beta>0,
\]
let \(R_0(x)\) denote the corresponding baseline survival function, and define
\[
m_\alpha(x)
=
\int_x^\infty t^{\alpha-1}R_0(t)\,dt.
\]
The hazard of the transformed model is
\[
h_\alpha(x)
=
\frac{x^{\alpha-1}R_0(x)}{m_\alpha(x)},
\qquad x>0.
\]

For both the IHSB half-normal and IHSB Maxwell models,
\[
\boxed{
h_\alpha(x)\sim \frac{x}{\beta^2}
\qquad(x\to\infty).
}
\]
In particular,
\[
h_\alpha(x)\to\infty.
\]

At the lower endpoint,
\[
R_0(x)\to1
\]
and
\[
m_\alpha(0)
=
\frac{\operatorname{E}(X_0^\alpha)}{\alpha},
\]
where \(X_0\) is the baseline lifetime. Therefore
\[
\boxed{
h_\alpha(x)
\sim
\frac{\alpha x^{\alpha-1}}
{\operatorname{E}(X_0^\alpha)}
\qquad(x\downarrow0).
}
\]

Consequently,
\[
\boxed{
\text{neither IHSBHN nor IHSBM has a globally decreasing hazard for any }
\alpha,\beta>0.
}
\]

There is an additional structural consequence when
\[
0<\alpha<1.
\]
Then
\[
h_\alpha(x)\to\infty
\]
at both endpoints. Since the hazard is finite and continuous for every \(x>0\), it attains at least one finite interior global minimum. Thus every such parameter pair has a genuine down-then-up hazard turn, although this result does not claim that the minimum is unique.

For the scale used in the source's hazard figures,
\[
\beta=1,
\]
the small-shape curves illustrate the effect. At
\[
\alpha=0.1,
\]
numerical evaluation gives for IHSBHN
\[
h(0.1)=4.7047987461\ldots,
\]
an interior minimum near
\[
x=0.79251185
\]
with
\[
h(x)=2.49722593\ldots,
\]
and then
\[
h(10)=10.28272635\ldots.
\]
For IHSBM,
\[
h(0.1)=3.2541919120\ldots,
\]
the minimum is near
\[
x=0.65565005
\]
with
\[
h(x)=1.66888622\ldots,
\]
and
\[
h(10)=10.09015329\ldots.
\]

The source describes the hazards of both newly introduced families as including decreasing, increasing, and bathtub-shaped behavior. The endpoint theorem above rules out the globally decreasing class.

## Assumptions and scope
The parameter domain is
\[
\alpha,\beta>0,
\]
and the lifetime support is
\[
x>0.
\]

For IHSBHN,
\[
R_0(x)
=
2\left[1-\Phi(x/\beta)\right].
\]
For IHSBM,
\[
R_0(x)
=
\frac{2}{\sqrt{\pi}}
\Gamma\!\left(
\frac32,\frac{x^2}{2\beta^2}
\right).
\]

The conclusion concerns a hazard that is decreasing over its entire support. It does not rule out a finite interval on which the hazard decreases.

For \(0<\alpha<1\), existence of an interior minimum is proved. No assertion of uniqueness is made.

## Proof
For the half-normal survival, Mills' ratio gives
\[
R_0(x)
=
\sqrt{\frac{2}{\pi}}
\frac{\beta}{x}
\exp\!\left(
-\frac{x^2}{2\beta^2}
\right)
\left[
1+O(x^{-2})
\right].
\]
For the Maxwell survival, the standard large-argument expansion of the upper incomplete gamma function gives
\[
R_0(x)
=
\sqrt{\frac{2}{\pi}}
\frac{x}{\beta}
\exp\!\left(
-\frac{x^2}{2\beta^2}
\right)
\left[
1+O(x^{-2})
\right].
\]

Thus in either case,
\[
R_0(x)
=
C x^\nu
\exp\!\left(
-\frac{x^2}{2\beta^2}
\right)
\left[
1+O(x^{-2})
\right]
\]
for a positive constant \(C\) and an exponent \(\nu\in\{-1,1\}\).

Set
\[
q(x)
=
\beta^2x^{\alpha-2}R_0(x).
\]
Both \(q(x)\) and \(m_\alpha(x)\) tend to zero. Differentiating,
\[
m_\alpha'(x)
=
-x^{\alpha-1}R_0(x).
\]
Also,
\[
\frac{q'(x)}{m_\alpha'(x)}
=
\frac{\beta^2 h_0(x)}{x}
-
\frac{\beta^2(\alpha-2)}{x^2},
\]
where
\[
h_0(x)=-\frac{R_0'(x)}{R_0(x)}
\]
is the baseline hazard.

For both half-normal and Maxwell baselines,
\[
h_0(x)\sim\frac{x}{\beta^2}.
\]
Hence
\[
\frac{q'(x)}{m_\alpha'(x)}\to1.
\]
L'Hospital's rule yields
\[
m_\alpha(x)
\sim
\beta^2x^{\alpha-2}R_0(x).
\]
Substitution into the transformed hazard gives
\[
h_\alpha(x)
=
\frac{x^{\alpha-1}R_0(x)}{m_\alpha(x)}
\sim
\frac{x}{\beta^2}.
\]

At zero,
\[
R_0(x)\to1
\]
and, by the tail-integral moment identity,
\[
m_\alpha(0)
=
\int_0^\infty t^{\alpha-1}R_0(t)\,dt
=
\frac{\operatorname{E}(X_0^\alpha)}{\alpha}.
\]
Therefore
\[
h_\alpha(x)
\sim
\frac{\alpha x^{\alpha-1}}
{\operatorname{E}(X_0^\alpha)}.
\]

The upper-endpoint divergence alone excludes a globally decreasing positive hazard for every \(\alpha>0\): a positive decreasing function cannot diverge to \(+\infty\) at the right endpoint.

If \(0<\alpha<1\), the lower-endpoint asymptotic also diverges. Continuity then implies that the hazard attains an interior minimum: choose endpoint neighborhoods where the hazard exceeds some finite interior value, then minimize on the remaining compact interval.

## Verification
The included checker evaluates the hazard directly from the source's integral formula for both new models.

It verifies numerically that
\[
\frac{\beta^2h_\alpha(x)}{x}
\]
approaches one at large \(x\) for several values of \(\alpha\).

For the source's plotted scale \(\beta=1\), the checker reproduces the small-shape down-then-up behavior. In particular, at \(\alpha=0.1\) it finds an IHSBHN minimum near \(0.79251185\) and an IHSBM minimum near \(0.65565005\).

These finite computations are reproducibility aids. The exclusion of a globally decreasing hazard is proved by the endpoint asymptotics.

## Relationship to prior work
The primary article gives the exact hazard formulas for IHSBHN and IHSBM and then states that the two new models can exhibit decreasing, increasing, and bathtub-shaped hazards.

The endpoint calculation uses only those displayed formulas together with standard Gaussian-tail and incomplete-gamma asymptotics. It shows that both transformed hazards have the universal far-tail scale
\[
x/\beta^2,
\]
which excludes the decreasing class claimed in the qualitative discussion.

The source's figures are compatible with this correction: the small-\(\alpha\) curves shown there already turn upward within the displayed window. The new statement is the parameter-uniform exclusion of a globally decreasing hazard, not a reinterpretation of one plotted curve.

Focused searches using the exact article DOI, the IHSBHN and IHSBM names, inverse-hazard size bias, decreasing-hazard terminology, and Gaussian-tail asymptotics did not locate a published model-specific correction.

## Limitations
The result does not classify all possible interior critical points.

For \(0<\alpha<1\), it proves existence but not uniqueness of an interior minimum.

For \(\alpha\ge1\), it excludes global decrease but does not assert that the hazard is globally increasing.

A recent or unindexed author correction could exist outside the sources examined.

## References
1. A. M. Gemeay, Y. A. Iriarte, O. A. Alqasem, F. M. A. Zaghdoun, and M. SidAhmed Mustafa, “Families of weighted distributions with inverse-hazard size bias: theory and applications,” AIMS Mathematics 11 (2026), 11296–11321. DOI: 10.3934/math.2026464.
2. NIST Digital Library of Mathematical Functions, §8.11, “Asymptotic Approximations and Expansions” for incomplete gamma functions.
