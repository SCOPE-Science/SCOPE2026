# NOT-Exp endpoint limits invalidate all four displayed hazard-shape examples
## Finding
For the NOT-Exp distribution, let
\[
\alpha>0,\qquad \gamma>0,\qquad \theta>0,
\]
and define
\[
v(y)=1-e^{-\theta y}.
\]
The source gives the CDF
\[
G(y)
=
\left[
\frac{(1+\alpha)v(y)}
{\alpha+v(y)}
\right]^\gamma,
\qquad y>0.
\]
Its density is
\[
g(y)
=
\frac{
\alpha\gamma\theta(1+\alpha)^\gamma
e^{-\theta y}
v(y)^{\gamma-1}
}{
\{\alpha+v(y)\}^{\gamma+1}
},
\]
and the hazard is
\[
h(y)=\frac{g(y)}{1-G(y)}.
\]

The hazard has exact endpoint asymptotics
\[
\boxed{
h(y)
\sim
\gamma
\left(
\frac{(1+\alpha)\theta}{\alpha}
\right)^\gamma
y^{\gamma-1}
\qquad
(y\downarrow0)
}
\]
and
\[
\boxed{
h(y)\longrightarrow\theta
\qquad
(y\to\infty).
}
\]

The small-time limit therefore has a sharp trichotomy:
\[
0<\gamma<1
\quad\Longrightarrow\quad
h(y)\to\infty,
\]
\[
\gamma=1
\quad\Longrightarrow\quad
h(y)\to
\frac{(1+\alpha)\theta}{\alpha},
\]
and
\[
\gamma>1
\quad\Longrightarrow\quad
h(y)\to0.
\]

These endpoint limits impose necessary global hazard-shape constraints.

If
\[
0<\gamma<1,
\]
a globally increasing hazard is impossible because the hazard begins at \(+\infty\) and ends at the finite value \(\theta\).

If
\[
\gamma=1,
\]
a globally increasing hazard is again impossible because
\[
\frac{(1+\alpha)\theta}{\alpha}>\theta.
\]

If
\[
\gamma>1,
\]
a globally decreasing hazard is impossible because the hazard begins at \(0\) and ends at the positive value \(\theta\).

The same endpoints rule out the initial directions required by the two standard nonmonotone shapes used in the source. A bathtub hazard is described there as initially declining and then increasing. Such an initial decline is impossible when
\[
\gamma>1,
\]
because a nonnegative hazard already starts at its minimum boundary value \(0\). An upside-down-bathtub hazard is initially increasing and then declining; this initial rise is impossible when
\[
0<\gamma<1,
\]
because the hazard starts at \(+\infty\).

Consequently all four Figure 1 parameter labels conflict with the model's endpoint mathematics:

\[
(\alpha,\gamma,\theta)=(0.1,0.1,0.1)
\]
is labeled increasing, but
\[
\gamma=0.1<1
\]
forces
\[
h(0+)=\infty
\quad\text{and}\quad
h(\infty)=0.1.
\]

\[
(\alpha,\gamma,\theta)=(2.8,4.5,1.5)
\]
is labeled decreasing, but
\[
\gamma=4.5>1
\]
forces
\[
h(0+)=0
\quad\text{and}\quad
h(\infty)=1.5.
\]

\[
(\alpha,\gamma,\theta)=(1.5,2.8,1.5)
\]
is described as bathtub-shaped with an initial decline, but
\[
\gamma=2.8>1
\]
forces the hazard to begin at \(0\).

Finally,
\[
(\alpha,\gamma,\theta)=(2.5,0.9,3.2)
\]
is labeled upside-down-bathtub, but
\[
\gamma=0.9<1
\]
forces the hazard to begin at \(+\infty\).

Thus the paper's plotted examples cannot realize the four global hazard shapes assigned to them under the standard meanings used in its own prose. The long-run failure rate is also universally
\[
\theta,
\]
independent of \(\alpha\) and \(\gamma\).

## Assumptions and scope
The parameter domain is the source's full positive domain
\[
\alpha,\gamma,\theta>0,
\]
with
\[
y>0.
\]

The finding is an endpoint theorem. It supplies necessary conditions for global monotonicity and for the initial direction of standard bathtub and upside-down-bathtub shapes. It does not give a complete finite-\(y\) phase diagram for every parameter triple.

The statements about the two nonmonotone shapes use the descriptions adopted in the source itself: bathtub means initial decline followed by increase, while upside-down bathtub means initial rise followed by decline.

The result does not challenge the CDF, PDF, likelihood, censoring mechanism, or inferential algorithms. It corrects the reliability interpretation of the model's advertised hazard flexibility.

## Proof
As
\[
y\downarrow0,
\]
one has
\[
v(y)
=
1-e^{-\theta y}
\sim
\theta y.
\]
Therefore
\[
\frac{(1+\alpha)v(y)}
{\alpha+v(y)}
\sim
\frac{1+\alpha}{\alpha}\theta y,
\]
and hence
\[
G(y)
\sim
\left(
\frac{(1+\alpha)\theta}{\alpha}
\right)^\gamma
y^\gamma.
\]
Writing
\[
C=
\left(
\frac{(1+\alpha)\theta}{\alpha}
\right)^\gamma,
\]
differentiation of the leading term gives
\[
g(y)
\sim
\gamma C y^{\gamma-1}.
\]
Since
\[
1-G(y)\to1,
\]
the small-time hazard asymptotic follows:
\[
h(y)
\sim
\gamma C y^{\gamma-1}.
\]

For the far tail, put
\[
\varepsilon=e^{-\theta y},
\qquad
\varepsilon\downarrow0.
\]
Then
\[
v(y)=1-\varepsilon,
\]
and
\[
\frac{(1+\alpha)v(y)}
{\alpha+v(y)}
=
\frac{1-\varepsilon}
{1-\varepsilon/(1+\alpha)}
=
1-\frac{\alpha}{1+\alpha}\varepsilon
+
O(\varepsilon^2).
\]
Therefore
\[
G(y)
=
1-
\frac{\gamma\alpha}{1+\alpha}
e^{-\theta y}
+
O(e^{-2\theta y}),
\]
so
\[
1-G(y)
\sim
\frac{\gamma\alpha}{1+\alpha}
e^{-\theta y}.
\]

The density formula gives
\[
g(y)
\sim
\frac{\gamma\alpha\theta}{1+\alpha}
e^{-\theta y}.
\]
Dividing yields
\[
h(y)
=
\frac{g(y)}{1-G(y)}
\longrightarrow
\theta.
\]

The shape exclusions are then immediate from nonnegativity and endpoint order. A globally increasing function cannot start above its finite terminal limit. A globally decreasing nonnegative function cannot start at \(0\) and end at a positive value. Likewise, a hazard that starts at its nonnegative boundary minimum \(0\) cannot initially decline, while a hazard that starts at \(+\infty\) cannot initially rise.

## Verification
The included checker evaluates the published CDF, density, and hazard at high precision.

It first differentiates the CDF numerically and confirms the published density formula.

For parameter values on both sides of
\[
\gamma=1,
\]
it checks the ratio
\[
\frac{
h(y)
}{
\gamma
\left(
\frac{(1+\alpha)\theta}{\alpha}
\right)^\gamma
y^{\gamma-1}
}
\to1
\]
as
\[
y\downarrow0.
\]

It also verifies
\[
h(y)/\theta\to1
\]
for large \(y\).

For the four Figure 1 parameter triples, the checker confirms the endpoint classifications:
the purported increasing example starts arbitrarily large and approaches \(0.1\);
the purported decreasing example starts arbitrarily close to \(0\) and approaches \(1.5\);
the purported bathtub example starts at \(0\);
and the purported upside-down-bathtub example starts arbitrarily large.

These computations are consistency checks. The endpoint statements and shape exclusions are proved analytically above.

## Relationship to prior work
Alotaibi and Elshahhat introduce the NOT-Exp model and advertise four reliability patterns: increasing, decreasing, bathtub, and upside-down-bathtub hazards. Their Figure 1 prose assigns one parameter triple to each pattern and describes the bathtub case as an initial decline followed by increasing risk.

The endpoint analysis above is obtained directly from the same CDF and density printed in the source. It shows that the four displayed parameter choices are incompatible with those labels before any numerical plotting issue is considered.

The result is stronger than checking the figure visually. It supplies a parameter-wide endpoint law:
\[
h(0+)
=
\begin{cases}
+\infty,&0<\gamma<1,\\
(1+\alpha)\theta/\alpha,&\gamma=1,\\
0,&\gamma>1,
\end{cases}
\]
and
\[
h(\infty)=\theta.
\]
Hence the source's shape claims must respect these constraints for every future use of the model.

Focused searches using the exact DOI, NOT-Exp name, hazard-shape terminology, Figure 1 parameter values, endpoint limits, and correction/erratum aliases did not locate a published corrigendum or a source already stating this endpoint correction.

## Limitations
The result gives necessary endpoint constraints, not a complete classification of all possible internal turning-point patterns.

It does not reconstruct the original Figure 1 plotting code. The contradiction follows from exact model formulas and does not depend on that code.

A very recent unindexed author correction could exist outside the records examined.

## References
1. R. Alotaibi and A. Elshahhat, “A New Exponential-Type Model Under Unified Progressive Hybrid Censoring: Computational Inference and Its Applications,” Mathematics 14 (2026), 1182. DOI: 10.3390/math14071182.
