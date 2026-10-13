# NMED is a shifted Gamma law, correcting its quantile and mean residual life
## Finding
For the neutrosophic moment exponential distribution (NMED) of Alomani et al., let
\[
I\in\mathbb R,
\qquad
\beta>0,
\]
and consider the published density on \(x>I\),
\[
f(x;\beta,I)
=
\frac{x-I}{\beta^2}
\exp\!\left[-\frac{x-I}{\beta}\right].
\]
This is exactly a translated gamma density:
\[
\boxed{X_N=I+Y,\qquad Y\sim\Gamma(2,\beta),}
\]
where the second gamma parameter is the scale.

This structural identity forces two corrections to the source.

First, for every \(0<p<1\), the exact quantile is
\[
\boxed{
Q(p)
=
I+\beta\left[-1-W_{-1}\!\left(-\frac{1-p}{e}\right)\right],
}
\]
where \(W_{-1}\) is the lower real branch of Lambert's \(W\) function on \((-1/e,0)\).

The source instead prints
\[
I+\beta\left[-W\!\left(\frac{1-p}{e}\right)-1\right].
\]
Its Lambert-\(W\) argument is positive. Since the principal real \(W\) is then positive, the bracket is less than \(-1\), so the printed expression lies below \(I\). It cannot be a quantile of a law supported on \((I,\infty)\).

Second, the correct mean residual life for \(t\ge I\) is
\[
\boxed{
m(t)
=
\beta\frac{t-I+2\beta}{t-I+\beta}
=
\beta+\frac{\beta^2}{t-I+\beta}.
}
\]
Hence
\[
m(I)=2\beta,
\qquad
m'(t)=-\frac{\beta^2}{(t-I+\beta)^2}<0,
\qquad
m(t)\downarrow\beta.
\]
The source's Theorem 3 instead states
\[
m(t)=\beta+(t-I),
\]
and interprets the mean residual life as linearly increasing. That theorem and its corresponding plot are incompatible with the published survival function.

## Assumptions and scope
The finding concerns the mathematical NMED density printed by the source, with fixed real shift \(I\) and \(\beta>0\). It does not require any interpretation of \(I\) beyond the source's own representation \(X_N=X+I\).

The corrected quantile is for \(0<p<1\). The endpoint values are obtained by limits: \(Q(0+)=I\) and \(Q(1-)=\infty\).

The mean residual life is defined for \(t\ge I\) by
\[
m(t)=\mathbb E[X_N-t\mid X_N>t]
=
\frac{\int_t^\infty S(x)\,dx}{S(t)}.
\]
No claim is made here about the paper's maximum-likelihood calculations or the empirical comparison on the mortality dataset.

## Proof
The density becomes, after \(y=x-I\),
\[
f_Y(y)=\frac{y}{\beta^2}e^{-y/\beta},
\qquad y>0,
\]
which is the \(\Gamma(2,\beta)\) density. Therefore
\[
F(x)=1-\left(1+\frac{x-I}{\beta}\right)
\exp\!\left[-\frac{x-I}{\beta}\right].
\]

For the quantile, put
\[
z=\frac{Q(p)-I}{\beta}\ge0,
\qquad
s=1-p\in(0,1).
\]
Then
\[
(1+z)e^{-z}=s.
\]
Writing \(v=1+z\ge1\),
\[
v e^{-v}=\frac{s}{e},
\]
so
\[
(-v)e^{-v}=-\frac{s}{e}.
\]
Because \(-v\le-1\), the required real Lambert branch is \(W_{-1}\), not \(W_0\). Thus
\[
v=-W_{-1}\!\left(-\frac{s}{e}\right),
\]
which yields the stated quantile.

For the mean residual life, let
\[
y=t-I\ge0.
\]
The published survival is
\[
S(t)=\left(1+\frac{y}{\beta}\right)e^{-y/\beta}.
\]
The numerator is
\[
\int_t^\infty S(x)\,dx
=
\int_y^\infty
\left(1+\frac{u}{\beta}\right)e^{-u/\beta}\,du
=
(y+2\beta)e^{-y/\beta}.
\]
Dividing by
\[
S(t)=\frac{y+\beta}{\beta}e^{-y/\beta}
\]
gives
\[
m(t)=\beta\frac{y+2\beta}{y+\beta}.
\]
Differentiation proves strict decrease.

## Verification
The bundled checker evaluates the source CDF and survival at representative values of \(I\), \(\beta\), and \(p\). It verifies that the corrected Lambert-\(W_{-1}\) quantile satisfies \(F(Q(p))=p\) to high precision and that the printed positive-argument expression lies below the support.

It also compares numerical integration of the survival function with the corrected closed-form mean residual life and checks the derivative sign. These are consistency checks; the proof above is exact.

## Relationship to prior work
The 2025 source explicitly defines \(X_N=X+I\) and prints the density of \(X_N\) as a location-shifted moment-exponential density. It correctly derives the MGF
\[
M_{X_N}(t)=\frac{e^{tI}}{(1-\beta t)^2},
\qquad t<1/\beta,
\]
which is already the MGF of \(I+\Gamma(2,\beta)\).

However, its quantile section prints a Lambert-\(W\) expression with the wrong sign/branch, and its Theorem 3 gives an increasing linear mean residual life. The source's own survival function is enough to disprove both formulas.

Focused searches using the exact DOI, NMED name, Lambert-\(W\) branch terminology, shifted-gamma equivalence, and mean-residual-life correction terminology did not locate a published corrigendum or another paper making these two NMED corrections.

## Limitations
The finding does not assess every formula in the source. It isolates two reliability/statistical formulas whose correction follows directly from the same shifted-gamma structure.

The parameter \(I\) is treated as fixed, exactly as in the source's displayed density and likelihood formulas. Broader philosophical interpretations of neutrosophic indeterminacy are outside the claim.

The corrected quantile uses the real branch \(W_{-1}\); numerical libraries that default to the principal branch must select branch \(-1\) explicitly.

## References
1. G. Alomani, R. Maya, M. R. Irshad, A. I. Al-Omari, and A. S. Aparna, “Neutrosophic moment exponential distribution: properties and modeling of child mortality rate data,” AIMS Mathematics 10 (2025), 27816–27836. DOI: 10.3934/math.20251222.
