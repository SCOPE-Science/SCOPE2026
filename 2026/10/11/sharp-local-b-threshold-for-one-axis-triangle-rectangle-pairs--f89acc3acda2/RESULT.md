# Sharp local \(B\)-threshold for one-axis triangle–rectangle pairs
## Finding
Let \(a,b,w,R,S,h>0\) with \(0<h<a\), \(R>w\), and \(S>b\). Set
\[
L=\operatorname{conv}\{(-w,-b),(0,a),(w,-b)\},\qquad K=[-R,R]\times[-S,h],
\]
and define \(f(t)=\operatorname{area}(e^tK\cap L)\), with dilation about the origin. Define
\[
h_* = \frac{a\sqrt{b(2a+b)}}{a+b+\sqrt{b(2a+b)}}.
\]
Then \(f\) is log-concave on some open neighborhood of \(0\) if and only if \(h>h_*\). For \(0<h<h_*\), one has \((\log f)''(0)>0\). At \(h=h_*\), the curvature vanishes at \(0\) but becomes positive immediately to the left, so no two-sided neighborhood of \(0\) is log-concave.

The displayed one-axis-symmetric counterexample of Livne Bar-On is recovered by \((a,b,w,R,S,h)=(3,2,5,6,3,1)\). Here \(h_*=4/3\), and the local area formula becomes
\[
f(t)=16+6e^t-e^{2t},
\]
so \((\log f)''(0)=26/441>0\).

## Assumptions and scope
The inequalities \(R>w\) and \(S>b\) ensure that, for all sufficiently small \(|t|\), the vertical sides and lower side of \(e^tK\) lie outside \(L\). The restriction \(0<h<a\) ensures that the upper side \(y=he^t\) cuts the two sloping sides of the triangle for all sufficiently small \(|t|\). Thus, locally, only one moving horizontal side controls the intersection.

The conclusion is deliberately local. It gives an exact phase boundary for log-concavity on a neighborhood of \(t=0\) inside this family. It does not claim global log-concavity for all \(t\), nor a classification of arbitrary pairs having only one reflection symmetry.

## Proof
For \(-b<y<a\), the horizontal cross-section of \(L\) has width
\[
\frac{2w(a-y)}{a+b}.
\]
Consequently, if \(x=he^t\) and \(|t|\) is small enough that the preceding active-side description holds, the triangular cap above \(y=x\) has area \(w(a-x)^2/(a+b)\). Since \(\operatorname{area}(L)=w(a+b)\),
\[
f(t)=\frac{w}{a+b}\left((a+b)^2-(a-x)^2\right)
     =\frac{w}{a+b}(x+b)(2a+b-x),\qquad x=he^t.
\]
The positive factor \(w/(a+b)\) does not affect logarithmic curvature. Write
\[
F(x)=(x+b)(2a+b-x).
\]
Because \(x'=x\), direct differentiation gives
\[
\frac{d}{dt}F(x)=2x(a-x),\qquad
\frac{d^2}{dt^2}F(x)=2x(a-2x).
\]
Hence
\[
F(x)\frac{d^2}{dt^2}F(x)-\left(\frac{d}{dt}F(x)\right)^2
=-2x\,G(x),
\]
where
\[
G(x)=ax^2+(4ab+2b^2)x-ab(2a+b).
\]
Since \(F(x)>0\) in the local regime,
\[
\operatorname{sgn}\bigl((\log f)''(t)\bigr)=-\operatorname{sgn}G(he^t).
\]
For \(x>0\),
\[
G'(x)=2ax+4ab+2b^2>0,
\]
while \(G(0)=-ab(2a+b)<0\). Thus \(G\) has exactly one positive zero. Solving the quadratic and rationalizing gives
\[
x=h_* = \frac{(a+b)\sqrt{b(2a+b)}-b(2a+b)}{a}
      = \frac{a\sqrt{b(2a+b)}}{a+b+\sqrt{b(2a+b)}},
\]
and \(0<h_*<a\).

If \(h>h_*\), continuity gives a sufficiently small two-sided neighborhood on which both the active-side formula remains valid and \(he^t>h_*\); therefore \((\log f)''(t)<0\) throughout that neighborhood. If \(h<h_*\), then \((\log f)''(0)>0\), so local log-concavity fails. If \(h=h_*\), then every sufficiently small negative \(t\) has \(he^t<h_*\), hence \((\log f)''(t)>0\); local log-concavity again fails. This proves the equivalence.

For the published example \((a,b,w,R,S,h)=(3,2,5,6,3,1)\), the threshold is \(h_*=4/3\). Substitution gives \(F(e^t)=16+6e^t-e^{2t}\), and at \(t=0\) the logarithmic-curvature numerator is \(21\cdot2-4^2=26\), yielding \((\log f)''(0)=26/441\).

## Verification
The factorization, the radical identity for \(h_*\), and the published numerical instance were replayed symbolically by `verify_threshold.py`. That checker is supplementary; the proof above is exact and does not depend on numerical experimentation.

Boundary cases were checked explicitly. The case \(h=h_*\) is not mislabeled as locally log-concave merely because the second derivative vanishes at \(0\): the exact sign formula shows positive logarithmic curvature on every sufficiently small left-hand interval. The hypotheses \(R>w\), \(S>b\), and \(0<h<a\) are used only to keep the same intersection combinatorics near \(0\).

## Relationship to prior work
Livne Bar-On proved the planar uniform-measure \(B\)-theorem for centrally symmetric convex shapes and observed that one common reflection axis does not suffice. The paper gives the explicit triangle–rectangle pair
\[
L=\operatorname{conv}\{(-5,-2),(0,3),(5,-2)\},\qquad K=[-6,6]\times[-3,1],
\]
and states that \(t\mapsto\operatorname{area}(e^tK\cap L)\) is not log-concave near \(0\). The result above turns that isolated example into a sharp local phase diagram for the full one-sided isosceles-triangle/rectangle family and analytically locates its transition.

Saroglou later proved the planar \(B\)-conjecture for even log-concave measures and symmetric convex bodies. Those hypotheses do not cover the present family: the triangle and the vertically off-center rectangle need not be centrally symmetric about the dilation center. Thus that broader positive theorem neither implies nor contradicts the threshold above.

Targeted searches for the exact radical threshold, the source coordinates, one-axis-symmetric triangle–rectangle dilations, and equivalent local-curvature formulations did not locate a prior statement of this phase boundary. This is evidence of noncoverage, not a proof that no unindexed occurrence exists.

## Limitations
The theorem is confined to the regime in which, near \(t=0\), exactly the upper horizontal side of the dilated rectangle cuts the triangle. It does not classify regimes in which a vertical or lower side is active, and it does not settle the general question of which nonsymmetric convex pairs satisfy the \(B\)-property. An elementary calculation of this kind could have appeared in an unindexed note or lecture text under different terminology; that remains the principal originality risk.

## References
1. A. Livne Bar-On, *The (B) conjecture for uniform measures in the plane*, arXiv:1311.6584v1, first public version 2013-11-26; later in *Geometric Aspects of Functional Analysis*, Lecture Notes in Mathematics 2116, Springer, DOI:10.1007/978-3-319-09477-9_22.
2. C. Saroglou, *More on logarithmic sums of convex bodies*, arXiv:1409.4346; *Mathematika* 62 (2016), 818–841, DOI:10.1112/S0025579316000061.
