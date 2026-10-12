# The EBR log-concavity theorem fails in its claimed parameter region
## Finding
For the exponentiated Bell Rayleigh (EBR) density of Al-Essa, Imran, and Jamal, let
\[
\alpha>0,\qquad \beta>0,\qquad \lambda>0,
\]
and put
\[
x=\frac{t}{\alpha},
\qquad
G(x)=1-e^{-x^2/2},
\qquad
H(x)=G(x)^\beta .
\]
After removing constants independent of \(t\), the exact log-density from the published PDF is
\[
\boxed{
\ell(t)
=
C+\log x-\frac{x^2}{2}
+(\beta-1)\log G(x)
-\lambda H(x)
-e^\lambda\{1-e^{-\lambda H(x)}\}.
}
\]

The paper's Theorem 2.1 claims that the EBR density is log-concave whenever
\[
\beta>\frac14.
\]
That statement is false in two independent ways.

First, the origin phase is controlled by
\[
\boxed{\beta=\frac12,}
\]
not by \(1/4\). For every fixed \(\alpha,\lambda>0\) and every \(\beta\ne1/2\),
\[
\boxed{
\ell''(t)
=
-\frac{2\beta-1}{t^2}
+
o(t^{-2})
\qquad(t\downarrow0).
}
\]
Consequently,
\[
0<\beta<\frac12
\quad\Longrightarrow\quad
\ell''(t)>0
\]
for all sufficiently small \(t>0\), whereas
\[
\beta>\frac12
\quad\Longrightarrow\quad
\ell''(t)<0
\]
for all sufficiently small \(t>0\).

In particular, every parameter choice with
\[
\frac14<\beta<\frac12
\]
is locally log-convex near the origin. This directly contradicts Theorem 2.1. It also contradicts Figure 5, which includes the case \(\beta=0.3\) among its purported log-concave examples.

At the boundary \(\beta=1/2\), the singular \(t^{-2}\) term cancels and the finite limiting curvature is
\[
\boxed{
\lim_{t\downarrow0}\ell''(t)
=
\frac1{\alpha^2}
\left(
\frac{\lambda^2e^\lambda}{2}-\frac34
\right).
}
\]
Thus even local log-concavity at the boundary depends on \(\lambda\). There is a unique number
\[
\boxed{
\lambda_0
=
0.8148840354416833337\ldots
}
\]
satisfying
\[
\lambda_0^2e^{\lambda_0}=\frac32.
\]
The boundary density is locally log-concave when \(0<\lambda<\lambda_0\) and locally log-convex when \(\lambda>\lambda_0\).

Second, no correction based only on replacing \(1/4\) by a larger threshold in \(\beta\) can make the published global theorem true. On the simple slice
\[
\beta=1,
\]
one obtains exactly, at \(t=\alpha\),
\[
\boxed{
\ell''(\alpha)
=
\frac1{\alpha^2}
\left[
\lambda^2e^{-1+\lambda e^{-1/2}}-2
\right].
}
\]
The bracket is strictly increasing after crossing zero and has a unique positive root
\[
\boxed{
\lambda_1
=
1.4858293101896016707\ldots .
}
\]
Therefore every
\[
\lambda>\lambda_1
\]
gives a density that is not globally log-concave even though \(\beta=1\).

A concrete counterexample is
\[
(\alpha,\beta,\lambda,t)=(1,1,2,1),
\]
for which
\[
\boxed{
\ell''(1)
=
4e^{-1+2e^{-1/2}}-2
=
2.9498421171424967310\ldots>0.
}
\]

Hence the paper's asserted \(\beta>1/4\) log-concavity region is not a valid region of global log-concavity, and the source's proof does not establish such a theorem.

## Assumptions and scope
The finding uses exactly the EBR CDF and density printed as Eqs. (2.4) and (2.5) in the primary source.

The scale parameter \(\alpha\) only rescales curvature:
\[
\frac{d^2}{dt^2}\log w(t)
=
\frac1{\alpha^2}
\frac{d^2}{dx^2}\log w(\alpha x).
\]
Therefore all curvature signs are independent of the numerical choice of \(\alpha\) after expressing location through \(x=t/\alpha\).

The result does not classify the full global log-concavity region in the \((\beta,\lambda)\) plane. It proves that the published region is false, gives the exact local origin phase away from and at \(\beta=1/2\), and gives an explicit global obstruction on the slice \(\beta=1\).

No claim is made that log-concavity is necessary for the model's validity as a probability distribution.

## Proof
Write
\[
s=\frac{x^2}{2},
\qquad
G(x)=1-e^{-s},
\qquad
H(x)=G(x)^\beta.
\]
The published density is, up to a positive parameter-only constant,
\[
w(t)
\propto
t\,e^{-s}
G(x)^{\beta-1}
e^{-\lambda H(x)}
\exp\!\left[-e^\lambda\{1-e^{-\lambda H(x)}\}\right].
\]
Taking logarithms gives
\[
\ell(t)
=
C+\log x-s
+(\beta-1)\log G(x)
-\lambda H(x)
-e^\lambda\{1-e^{-\lambda H(x)}\}.
\]

As \(x\downarrow0\),
\[
G(x)
=
\frac{x^2}{2}
\left(
1-\frac{x^2}{4}+O(x^4)
\right),
\]
so
\[
\log G(x)
=
2\log x-\log2-\frac{x^2}{4}+O(x^4)
\]
and
\[
H(x)
=
2^{-\beta}x^{2\beta}\{1+O(x^2)\}.
\]
Also,
\[
1-e^{-\lambda H}
=
\lambda H+O(H^2).
\]
Therefore
\[
\ell(t)
=
C_\beta
+
(2\beta-1)\log x
-
\lambda(1+e^\lambda)2^{-\beta}x^{2\beta}
+
O(x^2)
+
O(x^{4\beta}).
\]
Twice differentiating the explicit power expansion gives, for \(\beta\ne1/2\),
\[
\frac{d^2\ell}{dx^2}
=
-\frac{2\beta-1}{x^2}
+
o(x^{-2}).
\]
Because \(x=t/\alpha\), this is equivalent to
\[
\ell''(t)
=
-\frac{2\beta-1}{t^2}
+
o(t^{-2}).
\]

For \(\beta=1/2\), retain the quadratic terms:
\[
H(x)
=
\frac{x}{\sqrt2}
+O(x^3),
\]
and
\[
\ell(t)
=
C
-
\frac{\lambda(1+e^\lambda)}{\sqrt2}x
+
\left(
-\frac38+\frac{\lambda^2e^\lambda}{4}
\right)x^2
+
O(x^3).
\]
Thus
\[
\lim_{t\downarrow0}\ell''(t)
=
\frac1{\alpha^2}
\left(
-\frac34+\frac{\lambda^2e^\lambda}{2}
\right).
\]
The function \(\lambda^2e^\lambda\) is strictly increasing on \((0,\infty)\), so the boundary threshold \(\lambda_0\) is unique.

For \(\beta=1\), direct differentiation of the exact log-density at \(x=1\) simplifies to
\[
\frac{d^2\ell}{dx^2}(1)
=
\lambda^2e^{-1+\lambda e^{-1/2}}-2.
\]
The function
\[
\lambda\longmapsto
\lambda^2e^{-1+\lambda e^{-1/2}}
\]
is strictly increasing for \(\lambda>0\), starts at zero, and tends to infinity, so the crossing value \(\lambda_1\) is unique.

At \(\lambda=2\),
\[
\frac{d^2\ell}{dx^2}(1)
=
4e^{-1+2e^{-1/2}}-2
=
2.9498421171424967310\ldots>0.
\]
This single point already disproves global log-concavity for that admissible parameter triple.

## Verification
The included checker evaluates the exact published log-density with high precision.

It verifies:
\[
\frac{t^2\ell''(t)}{1-2\beta}\to1
\]
for a representative \(\beta=0.3\), confirming local convexity in the source's claimed log-concave region.

It verifies the finite boundary limit for \(\beta=1/2\), computes the unique root
\[
\lambda_0=0.8148840354416833337\ldots,
\]
and checks both curvature signs around it.

It also evaluates the exact \(\beta=1\) curvature formula at \(t=\alpha\), computes
\[
\lambda_1=1.4858293101896016707\ldots,
\]
and independently confirms
\[
\ell''(1)=2.9498421171424967310\ldots
\]
for \((\alpha,\beta,\lambda)=(1,1,2)\).

The numerical work is only a reproducibility check. The counterexamples and asymptotic phase statements are proved analytically above.

## Relationship to prior work
The primary paper states in Theorem 2.1 that the EBR density is log-concave whenever
\[
\beta>0.25.
\]
Its proof does not differentiate the actual log of Eq. (2.5): the displayed logarithm changes the sign of the Rayleigh exponential term and replaces the factor \(e^{\lambda-\lambda H(t)}\) by a logarithm involving \(1-e^{-\lambda H(t)}\). The proof then uses only an origin approximation and promotes that local calculation to a global statement.

The same source later states the correct density asymptotic
\[
w(t)\sim C_1t^{2\beta-1}
\qquad(t\downarrow0),
\]
which is already consistent with the corrected \(1/2\) origin transition and inconsistent with the claimed \(1/4\) transition.

Figure 5 explicitly includes
\[
\beta=0.3
\]
among the purported concave cases. The exact density instead has
\[
\ell''(t)>0
\]
for all sufficiently small \(t\) at every \(1/4<\beta<1/2\).

Focused searches using the exact DOI, EBR name, theorem number, log-concavity terminology, and the \(\beta=0.25\) boundary did not locate a published corrigendum or an independent source already making this correction. Searches of general Bell-G documentation located distribution software and earlier Bell-generated families but no theorem implying or repairing the disputed log-concavity claim.

## Limitations
The complete global log-concavity region in \((\beta,\lambda)\) is not determined here.

The result does not reassess the paper's quantile formula, moment formula, acceptance-sampling design, parameter estimates, or empirical fits.

The source also contains separate prose claims about heavy tails that are not part of this finding.

## References
1. L. A. Al-Essa, M. Imran, and F. Jamal, “Applications of the novel extended Rayleigh distribution in statistical quality, censored data with application for engineering materials,” AIMS Mathematics 11 (2026), 14025–17074. DOI: 10.3934/math.2026577.
