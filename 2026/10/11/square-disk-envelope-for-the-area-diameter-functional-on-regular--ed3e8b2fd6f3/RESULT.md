# Square–disk envelope for the area–diameter functional on regular polygons
## Finding
For \(0\le\alpha\le1\), put
\[
F_\alpha(K)=
\frac{\alpha\,\operatorname{area}(K)
+(1-\alpha)\operatorname{diam}(K)^2}
{\operatorname{per}(K)\operatorname{diam}(K)}.
\]
For the family of all finite Euclidean regular polygons \(P_n\), \(n\ge3\),
\[
\sup_{n\ge3}F_\alpha(P_n)
=
\max\left\{
\frac{\sqrt2(2-\alpha)}8,\,
\frac{1-\alpha}{\pi}+\frac{\alpha}{4}
\right\}.
\]
The first expression is \(F_\alpha(P_4)\). The second is the value for a Euclidean disk and is the limit of \(F_\alpha(P_n)\) as \(n\to\infty\).

The two branches cross at
\[
\alpha_*=
\frac{2(\sqrt2\pi-4)}
{\pi(\sqrt2+2)-8}
=
0.324924321990671\ldots .
\]
Hence the square is the unique maximizing finite regular polygon for
\[
0\le\alpha\le\alpha_*.
\]
For
\[
\alpha_*<\alpha\le1,
\]
no finite regular polygon attains the supremum; it is approached by polygons with an increasing number of sides.

Equivalently, in normalized coordinates
\[
x(K)=\frac{\operatorname{diam}(K)}{\operatorname{per}(K)},
\qquad
y(K)=\frac{\operatorname{area}(K)}
{\operatorname{per}(K)\operatorname{diam}(K)},
\]
all regular polygons lie below the chord joining the square point
\[
\left(\frac1{2\sqrt2},\frac{\sqrt2}{8}\right)
\]
to the disk point
\[
\left(\frac1\pi,\frac14\right),
\]
with equality among finite regular polygons only at the square.

## Assumptions and scope
All polygons are nondegenerate Euclidean regular polygons. Area, diameter, and perimeter are the ordinary Euclidean quantities. The functional \(F_\alpha\) is scale invariant.

The source question asks, for each \(\alpha\in[0,1]\), for the smallest constant \(c(\alpha)\) such that
\[
\alpha\,\operatorname{area}(C)
+(1-\alpha)\operatorname{diam}(C)^2
\le
c(\alpha)\operatorname{per}(C)\operatorname{diam}(C)
\]
for every planar convex body \(C\). The present result solves only the complete regular-polygon subfamily and its disk limit. It does not determine the global constant \(c(\alpha)\).

## Proof
Write
\[
x=\frac{\operatorname{diam}}{\operatorname{per}},
\qquad
y=\frac{\operatorname{area}}
{\operatorname{per}\operatorname{diam}}.
\]
Then
\[
F_\alpha=(1-\alpha)x+\alpha y.
\]

First consider an even regular \(n\)-gon and set
\[
\theta=\frac{\pi}{n},
\qquad
0<\theta\le\frac{\pi}{4}.
\]
Normalize its circumradius to \(1\). Its diameter is \(2\), perimeter is
\[
2n\sin\theta,
\]
and area is
\[
n\sin\theta\cos\theta.
\]
Therefore its normalized point is
\[
x(\theta)=\frac{\theta}{\pi\sin\theta},
\qquad
y(\theta)=\frac{\cos\theta}{4}.
\]
As \(\theta\to0\), this tends to the disk point
\[
B=\left(\frac1\pi,\frac14\right),
\]
while at \(\theta=\pi/4\) it equals the square point
\[
Q=\left(\frac1{2\sqrt2},\frac{\sqrt2}{8}\right).
\]

We prove that this even-polygon curve is strictly convex as a graph \(y=y(x)\). Differentiation gives
\[
\frac{dx}{d\theta}
=
\frac{\sin\theta-\theta\cos\theta}
{\pi\sin^2\theta}>0
\]
and
\[
\frac{dy}{dx}
=
\frac{\pi\sin^3\theta}
{4(\theta\cos\theta-\sin\theta)}.
\]
A second differentiation with respect to \(\theta\) yields
\[
\frac{d}{d\theta}\left(\frac{dy}{dx}\right)
=
\frac{\pi\sin^2\theta}
{8(\theta\cos\theta-\sin\theta)^2}
\,g(\theta),
\]
where
\[
g(\theta)
=
2\theta\cos(2\theta)+4\theta-3\sin(2\theta).
\]
To determine its sign, put
\[
h(\theta)=1-\cos(2\theta)-\theta\sin(2\theta).
\]
Then
\[
g'(\theta)=4h(\theta),
\]
\[
h'(\theta)=\sin(2\theta)-2\theta\cos(2\theta),
\]
and
\[
h''(\theta)=4\theta\sin(2\theta)\ge0
\]
on \(0\le\theta\le\pi/4\). Since
\[
g(0)=h(0)=h'(0)=0,
\]
we obtain
\[
g(\theta)>0
\]
for every \(\theta\in(0,\pi/4]\). Thus
\[
\frac{d^2y}{dx^2}>0.
\]
The even-polygon curve therefore lies strictly below the open chord \(BQ\).

Now let \(n\) be odd and set
\[
u=\frac{\pi}{2n}.
\]
With circumradius \(1\), the diameter is
\[
2\cos u.
\]
A direct substitution gives
\[
x(P_n)=\frac{1}{2n\sin u},
\qquad
y(P_n)=\frac{\cos(2u)}{4\cos u}.
\]
For the regular \(2n\)-gon,
\[
x(P_{2n})=\frac{1}{2n\sin u},
\qquad
y(P_{2n})=\frac{\cos u}{4}.
\]
Thus
\[
x(P_n)=x(P_{2n})
\]
and
\[
y(P_{2n})-y(P_n)
=
\frac{\sin^2u}{4\cos u}>0.
\]
Every odd regular polygon is therefore strictly below the corresponding even regular polygon at the same \(x\)-coordinate. Hence every finite regular polygon other than the square lies strictly below the open square–disk chord.

Because \(F_\alpha\) is a linear functional of \((x,y)\), its supremum over that chord is attained at an endpoint. The endpoint values are
\[
F_\alpha(Q)
=
\frac{\sqrt2(2-\alpha)}8
\]
and
\[
F_\alpha(B)
=
\frac{1-\alpha}{\pi}+\frac{\alpha}{4}.
\]
Solving their equality gives
\[
\alpha_*=
\frac{2(\sqrt2\pi-4)}
{\pi(\sqrt2+2)-8}.
\]

For \(0<\alpha\le\alpha_*\), strict chord separation makes the square the unique finite maximizer. At \(\alpha=0\), the same conclusion follows from the strict increase of \(x(\theta)\) on the even curve and the equality
\[
x(P_n)=x(P_{2n})
\]
for odd \(n\). For \(\alpha>\alpha_*\), the disk endpoint has the larger value and every finite regular polygon is strictly below it. This proves all assertions.

## Verification
The supplied `verify.py` symbolically reconstructs the even- and odd-polygon normalized coordinates, differentiates the even curve, verifies the identities for \(g\), \(h\), and their derivatives, checks the exact odd-to-even vertical gap, and verifies the crossover formula.

It also numerically evaluates every regular polygon with
\[
3\le n\le10000
\]
at a representative mesh of \(\alpha\)-values and confirms the proved envelope. This finite computation is only a regression check; the all-\(n\) statement follows from the symbolic convexity and odd-to-even domination arguments above.

## Relationship to prior work
Glazyrin and Morić asked for the sharp constant \(c(\alpha)\) in the general planar inequality
\[
\alpha\,\operatorname{area}(C)
+(1-\alpha)\operatorname{diam}(C)^2
\le
c(\alpha)\operatorname{per}(C)\operatorname{diam}(C).
\]
Their paper proves a particular perimeter--area--diameter estimate and explicitly notes that the behavior of \(c(\alpha)\) as a function of \(\alpha\) is unclear.

The present result does not solve that general question. Instead, it gives an exact structural elimination of the entire regular-polygon competitor family: as far as this functional is concerned, every finite regular polygon is dominated by the square--disk envelope, and only the square can be a finite regular-family maximizer.

Standard formulas for regular-polygon area and perimeter individually are classical. The new step is the joint normalized curve, its strict square--disk chord inequality, the exact odd-to-even domination, and the resulting all-\(\alpha\) envelope.

Searches using the source question, the normalized ratios, square--disk envelope language, regular-polygon variants, and the exact crossover value did not locate this statement or an implication that covers it.

## Limitations
The result is restricted to the regular-polygon family and its disk limit. Other convex bodies can lie above the square--disk chord, so no global formula for \(c(\alpha)\) is asserted.

The argument does not classify which nonregular convex bodies maximize the source functional for any \(\alpha\).

A residual originality risk remains because the regular-polygon formulas are classical and a similar envelope observation could occur in an unindexed exercise or discussion of area--perimeter--diameter diagrams.

## References
1. A. Glazyrin and F. Morić, *Upper bounds for the perimeter of plane convex bodies*, Acta Mathematica Hungarica 142 (2014), 366--383. DOI: 10.1007/s10474-013-0350-8. First published online 2013-09-18. Relevant material: Question 2 and the surrounding area--perimeter--diameter discussion.
2. G. D. Chakerian, *On some geometric inequalities*, Proceedings of the American Mathematical Society 15 (1964), 886--888.
3. T. Kubota, *Eine Ungleichheit für Eilinien*, Mathematische Zeitschrift 20 (1924), 264--266.
