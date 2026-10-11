# The affine-regular decagon uniquely minimizes the James constant in a decagonal Radon family
## Finding
Mizuguchi introduced a one-parameter family \(X_\beta\), \(1/2\le\beta\le1\), of real Radon planes whose unit spheres are decagons. Put
\[
k_\beta=\frac{1-\beta}{\beta}.
\]
The norm is obtained by gluing an absolute normalized norm in the same-sign quadrants to the reflected dual norm in the opposite-sign quadrants. Explicitly, for \(ab\ge0\),
\[
\|(a,b)\|_\beta=
\begin{cases}
|a|,& |b|\le k_\beta|a|,\\
\beta(|a|+|b|),&k_\beta|a|\le |b|\le k_\beta^{-1}|a|,\\
|b|,&|a|\le k_\beta|b|,
\end{cases}
\]
with the natural endpoint convention, while for \(ab\le0\),
\[
\|(a,b)\|_\beta=
\begin{cases}
k_\beta|a|+|b|,&|a|\le|b|,\\
|a|+k_\beta|b|,&|b|\le|a|.
\end{cases}
\]
Then the James constant has a unique global minimum at
\[
\beta_*=\frac{\sqrt5-1}{2},
\]
and
\[
J(X_{\beta_*})=\frac{3\sqrt5-1}{4}.
\]
Moreover, \(X_{\beta_*}\) has an affine-regular decagonal unit sphere.

## Assumptions and scope
All spaces and scalars are real. The James constant is
\[
J(X)=\sup\{\min(\|x+y\|,\|x-y\|):x,y\in S_X\}.
\]
The input used from Mizuguchi's published theorem is the exact profile
\[
J(X_\beta)=
\begin{cases}
\dfrac{1+2\beta^2}{2\beta},&\dfrac12\le\beta<\dfrac{\sqrt5-1}{2},\\[6pt]
\dfrac{3\beta-2\beta^2}{1-\beta+\beta^2},&\dfrac{\sqrt5-1}{2}\le\beta<\dfrac23,\\[6pt]
\dfrac{-2+4\beta+\beta^2}{-1+2\beta+\beta^2},&\dfrac23\le\beta\le1.
\end{cases}
\]
The new claim is the global optimization and rigidity of this profile, together with the identification of the unique minimizing decagon as affine-regular.

## Proof
Write
\[
r=\frac{\sqrt5-1}{2},
\qquad r^2+r=1.
\]
On the first branch,
\[
F_1(\beta)=\beta+\frac1{2\beta},
\qquad
F_1'(\beta)=\frac{2\beta^2-1}{2\beta^2}.
\]
Because \(r<1/\sqrt2\), \(F_1'\) is strictly negative on \([1/2,r]\). Thus \(F_1\) decreases strictly to its endpoint value
\[
F_1(r)=\frac{3\sqrt5-1}{4}.
\]

On the second branch,
\[
F_2'(\beta)=-\frac{\beta^2+4\beta-3}{(\beta^2-\beta+1)^2}.
\]
The polynomial \(q(\beta)=\beta^2+4\beta-3\) is strictly increasing for positive \(\beta\). One has \(q(r)<0\) and \(q(2/3)=1/9>0\). Hence \(F_2\) first increases and then decreases, so its minimum on \([r,2/3]\) is at an endpoint. The endpoint values are
\[
F_2(r)=\frac{3\sqrt5-1}{4},
\qquad
F_2(2/3)=\frac{10}{7}.
\]
They are strictly ordered because
\[
\frac{10}{7}-\frac{3\sqrt5-1}{4}
=
\frac{47-21\sqrt5}{28}>0,
\]
the last inequality following from \(47^2>5\cdot21^2\).

On the third branch,
\[
F_3'(\beta)=-\frac{2\beta(\beta-1)}{(\beta^2+2\beta-1)^2}>0
\]
for \(2/3\le\beta<1\). Thus \(F_3\) is strictly increasing from
\[
F_3(2/3)=\frac{10}{7}.
\]
Combining the three branches proves that \(r\) is the unique global minimizer and gives the stated minimum.

It remains to identify its geometry. At \(\beta=r\), the relation \(r^2+r=1\) gives \(k_\beta=r\). Five consecutive vertices of the unit sphere are
\[
v_0=(1,0),\quad v_1=(1,r),\quad v_2=(r,1),\quad v_3=(0,1),\quad v_4=(-r,r),
\]
followed by \(v_5=(-1,0)\) and their central opposites. Put \(\varphi=1/r=1+r\). Direct calculation gives
\[
v_{j+1}=\varphi v_j-v_{j-1}
\]
for the consecutive vertices. This is exactly the second-order recurrence satisfied by the vertices of a Euclidean regular decagon, since \(\varphi=2\cos(\pi/5)\). Therefore a linear map carrying two consecutive Euclidean regular-decagon vertices to \(v_0,v_1\) carries the entire regular decagon to this unit sphere. Hence the minimizing decagon is affine-regular.

## Verification
The bundled `verify.py` checks the algebraic endpoint values, derivative-sign reductions, strict comparison of the competing endpoint values, and the affine-regular vertex recurrence exactly in \(\mathbb Q(\sqrt5)\). The published James-profile formula is cited as the theorem being optimized; the checker does not pretend to re-prove that published 17-page calculation.

## Relationship to prior work
Mizuguchi's paper proves the full piecewise formula for \(J(X_\beta)\) and states that the calculation covers Radon planes with decagonal unit spheres. The inspected article finishes with that exact profile but does not state the global minimizer or identify a unique least-James member of the family.

A separate public research record gives
\[
\delta_{\mathrm{BM}}(P_4,P_{10})=\frac{3\sqrt5-1}{4}
\]
for the Banach--Mazur distance from the parallelogram to the affine-regular decagon. Thus the newly identified minimum of the James profile has the same exact number. This is recorded only as a numerical cross-invariant coincidence: no general theorem equating these two invariants is asserted or used in the proof.

## Limitations
The uniqueness statement is only within Mizuguchi's displayed one-parameter decagonal Radon family; it is not a classification of all Radon planes or all decagonal normed planes. The Banach--Mazur comparison is statement-level because only the public scientific summary of that separate record was available here; the equality of the displayed numbers is exact, but no stronger implication comparison is claimed. Bibliographic and research-index searches cannot prove absolute novelty.

## References
1. H. Mizuguchi, “The James constant in Radon planes,” Aequationes Mathematicae 94 (2020), 201–217, doi:10.1007/s00010-020-00698-2. Mathematics Subject Classification: 46B20, 51B20, 52A21.
2. Mathematical Society of Japan, 2019 Annual Meeting program, talk 06-01-0023, “On the James constant in Radon planes,” public program dated 11 December 2018.
3. “Banach–Mazur distance from the parallelogram to the regular decagon,” public research record dated 4 October 2026, identifier `2026/10/4/SCOPE-banach-mazur-distance-from-the-parallelogram-to-the-regular-deca--762b51c74443`.
