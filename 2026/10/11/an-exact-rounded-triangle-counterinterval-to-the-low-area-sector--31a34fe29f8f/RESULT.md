# An exact rounded-triangle counterinterval to the low-area sector conjecture
## Finding
For every
\[
1\le \theta<\theta_*,
\qquad
\theta_*=\pi-2-\frac{(\pi-3)\sqrt{4-\pi}}{\sqrt{6-\pi-\sqrt3}}
=1.0179838247780255\ldots,
\]
and every prescribed perimeter \(P>0\), the circular sector of angle \(\theta\) is not a minimum-diameter convex body among bodies with that perimeter and the same area.

Let \(T\) be a unit-side equilateral triangle, let \(B\) be the Euclidean unit disk, and define the rounded-equilateral family
\[
K_t=tT+\frac{1-t}{2}B,\qquad 0\le t\le1.
\]
Each \(K_t\) has diameter \(1\). For every \(\theta\) in the stated interval there is a unique parameter \(t_\theta\) such that, after scaling \(K_{t_\theta}\) to perimeter \(P\), it has exactly the sector's area as well, while its diameter is strictly smaller than the sector's diameter.

For the normalization \(P=\pi\) used in the motivating problem, the counterinterval of sector areas is
\[
\frac{\pi^2}{18}\le A<
A_*,
\qquad
A_*=
\frac{\pi^2\theta_*}{2(2+\theta_*)^2}
=0.551539741814377\ldots.
\]
Thus a nontrivial interval inside the proposed low-area sector regime is ruled out analytically.

## Assumptions and scope
All bodies are compact convex subsets of the Euclidean plane with nonempty interior. Perimeter, area, and diameter are denoted by \(P(K)\), \(A(K)\), and \(D(K)\).

A circular sector of radius \(R\) and angle \(\theta\le\pi/3\) has diameter \(R\): the largest chord between its two radial endpoints is \(2R\sin(\theta/2)\le R\). Hence
\[
P_S=R(2+\theta),\qquad
A_S=\frac{R^2\theta}{2},\qquad
D_S=R.
\]

For scale comparison define
\[
q(K)=\frac{A(K)}{P(K)^2}.
\]
Two convex bodies can be rescaled to the same perimeter and area exactly when they have the same value of \(q\). If they have the same \(q\), then after rescaling to a common perimeter \(P\), the body with larger normalized ratio \(P(K)/D(K)\) has smaller diameter.

The claim concerns only the displayed sector-angle interval and the explicit rounded-equilateral comparison family. It does not identify the global diameter minimizer outside that interval.

## Proof
Normalize first by diameter.

For the sector, take \(R=1\). Then
\[
p_S(\theta)=2+\theta,\qquad
a_S(\theta)=\frac{\theta}{2},
\qquad
q_S(\theta)=\frac{\theta}{2(2+\theta)^2}.
\]

For \(K_t=tT+\frac{1-t}{2}B\), Minkowski addition with a disk enlarges every diameter by twice the disk radius, so
\[
D(K_t)=t+(1-t)=1.
\]
The planar parallel-body formulas give
\[
p(t)=\pi-(\pi-3)t
\]
and
\[
a(t)=\frac{\pi}{4}
+\frac{3-\pi}{2}\,t
+\frac{\pi+\sqrt3-6}{4}\,t^2.
\]
Thus
\[
q(t)=\frac{a(t)}{p(t)^2}.
\]
Direct differentiation simplifies completely:
\[
q'(t)=
\frac{t(\pi\sqrt3-9)}{2p(t)^3}<0
\qquad (0<t\le1),
\]
because \(\pi\sqrt3<9\). Hence \(q\) is strictly decreasing along the rounded-equilateral family.

Now compare the member whose normalized perimeter agrees with the sector. Put
\[
t_s(\theta)=\frac{\pi-2-\theta}{\pi-3},
\]
so that \(p(t_s)=2+\theta\). On \(1\le\theta\le\pi/3\), one has \(0<t_s\le1\). Define
\[
g(\theta)=a(t_s(\theta))-\frac{\theta}{2}.
\]
Its derivative is
\[
g'(\theta)=
\frac{(6-\pi-\sqrt3)(\pi-2-\theta)}
{2(\pi-3)^2}>0
\]
throughout this interval. Also
\[
g(1)=\frac{\sqrt3-2}{4}<0.
\]
Solving \(g(\theta)=0\) gives the unique zero in \([1,\pi/3]\),
\[
\theta_*=
\pi-2-\frac{(\pi-3)\sqrt{4-\pi}}
{\sqrt{6-\pi-\sqrt3}}.
\]
Therefore
\[
g(\theta)<0
\qquad\text{for}\qquad
1\le\theta<\theta_*.
\]
Because \(p(t_s)=p_S\), this inequality is exactly
\[
q(t_s)<q_S(\theta).
\]

At the disk endpoint,
\[
q(0)=\frac1{4\pi}>q_S(\theta)
\qquad(0<\theta\le\pi/3).
\]
Indeed this is equivalent to
\[
(2+\theta)^2>2\pi\theta,
\]
whose left-minus-right quadratic has discriminant \(4\pi(\pi-4)<0\). Since \(q(t)\) is continuous and strictly decreasing, for every \(1\le\theta<\theta_*\) there is a unique
\[
0<t_\theta<t_s(\theta)
\]
such that
\[
q(t_\theta)=q_S(\theta).
\]
Because \(p(t)\) is strictly decreasing,
\[
p(t_\theta)>p(t_s)=2+\theta.
\]

Finally fix an arbitrary common perimeter \(P>0\). Scale the unit-radius sector by \(P/(2+\theta)\), and scale \(K_{t_\theta}\) by \(P/p(t_\theta)\). Equality of the \(q\)-values gives equality of the scaled areas. Their diameters are
\[
D_S=\frac{P}{2+\theta},
\qquad
D_K=\frac{P}{p(t_\theta)}.
\]
The strict perimeter inequality above yields
\[
D_K<D_S.
\]
Hence the sector is not diameter-minimizing.

For \(P=\pi\), substituting the sector formula
\[
A=\frac{\pi^2\theta}{2(2+\theta)^2}
\]
at \(\theta=1\) and at the limiting \(\theta_*\) gives the stated area interval.

## Verification
The accompanying `verify.py` recomputes the closed formulas using ordinary double-precision arithmetic as a consistency check. It verifies the location of \(\theta_*\), the identity \(g(\theta_*)=0\), the sign of the derivative constants, and representative bisection solutions for \(t_\theta\) at several interior angles. It then rescales both bodies to a common perimeter and checks equal area and strict diameter improvement numerically.

The script is not the proof of the interval. The proof is the exact monotonicity and intermediate-value argument above.

## Relationship to prior work
Nandakumar's 2013 question asks for the minimum and maximum diameter of a convex planar region with prescribed area and perimeter. For the normalization \(P=\pi\), it proposes that below a critical area of about \(0.57\) the minimum-diameter body is probably a circular sector, with the sector angle decreasing below \(\pi/3\) as the area decreases. The present theorem gives a rigorous interval inside that proposed regime on which sectors are not minimizers.

The modern Blaschke--Santaló-diagram literature is important for the overlap comparison. Ftouhi's 2025 survey and numerical study records the classical Kubota description of the lower \((P,A)\)-boundary for diameter \(1\) only through the normalized-perimeter range \(2<P\le3\). It then describes the continuation from the equilateral triangle toward the Reuleaux triangle, where \(P>3\), as an analytically missing boundary treated numerically. The present comparison enters exactly that region: for every strict interior angle \(\theta>1\), the defeating rounded-equilateral body satisfies \(p(t_\theta)>2+\theta>3\). The threshold and the rounded-equilateral comparison are not stated there.

Pan, Sun, and Wang give the sharp upper-area branch for prescribed perimeter and diameter and list primary classification \(52A38\); that theorem concerns a different boundary of the same diagram and does not imply the counterinterval here.

## Limitations
The theorem does not determine the true minimum-diameter body for the affected \((P,A)\)-pairs. It only proves that the circular sector is not the minimizer and supplies one explicit better competitor. It also does not claim optimality of the rounded-equilateral family or that \(\theta_*\) is the largest possible angle at which the sector fails globally.

The exact interval ends at equality within this comparison family: at \(\theta=\theta_*\), the perimeter-matched rounded equilateral and the sector have the same normalized area, so the strict diameter improvement proved here disappears at that endpoint.

A residual literature risk remains that an older unindexed source contains the same explicit parallel-body comparison. The inspected modern diagram survey, however, treats the relevant \(P/D>3\) lower boundary as analytically unresolved and does not state this threshold.

## References
1. R. Nandakumar, *A Set of Questions in Combinatorial and Metric Geometry*, arXiv:1307.3472v1, first public version 2013-07-02.
2. I. Ftouhi, *Improved Description of Blaschke--Santaló Diagrams via Numerical Shape Optimization*, Applied Mathematics & Optimization 91 (2025), DOI:10.1007/s00245-025-10250-w.
3. S. Pan, X. Sun, and Y. Wang, *A variant of the isoperimetric problem, Part I*, Science in China Series A: Mathematics 51 (2008), DOI:10.1007/s11425-008-0043-x.
