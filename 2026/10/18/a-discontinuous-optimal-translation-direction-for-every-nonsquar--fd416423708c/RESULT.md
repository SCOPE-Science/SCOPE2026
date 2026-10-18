# A discontinuous optimal-translation direction for every nonsquare rectangle

## Finding

Let \(K=[-a/2,a/2]\times[-b/2,b/2]\), with \(a>b>0\), and let \(g_K(h)=\operatorname{area}(K\cap(K+h))\) be its covariogram. At a prescribed Euclidean translation distance \(t\), define \(M(t)=\max_{\|h\|_2=t}g_K(h)\). The optimizing direction has precisely one discontinuous transition for \(0<t<\sqrt{a^2+b^2}\).

Specifically, put \(r=a/b>1\), and let \(z_*\) be the unique root in \((0,\sqrt2-1)\) of
\[
z^4-4z^2+4rz-1=0.
\]
Define
\[
\theta_0=2\arctan z_*,\qquad
 t_0=\frac{(a-bz_*)(1+z_*^2)}{1-z_*^2},\qquad
 D=\sqrt{a^2+b^2},\qquad \theta_D=\arctan(b/a).
\]
Then \(0<t_0<a<D\) and \(0<\theta_0<\theta_D<\pi/4\). Up to independent sign changes of the two translation coordinates, all maximizing shifts have the following exhaustive classification:

1. For \(0<t<t_0\), precisely the long-side-axis shift \((t,0)\) maximizes overlap, and \(M(t)=b(a-t)\).
2. For \(t=t_0\), there are precisely two absolute-coordinate maximizing orientations: \(\theta=0\) and \(\theta=\theta_0\), both giving \(M(t_0)=b(a-t_0)\).
3. For \(t_0<t<D\), precisely one absolute-coordinate orientation \(\theta_*(t)\in(\theta_0,\theta_D)\) maximizes overlap. It is the unique solution on the increasing branch of
\[
t=\frac{a\cos\theta-b\sin\theta}{\cos(2\theta)},
\]
and \(M(t)=(a-t\cos\theta_*)(b-t\sin\theta_*)\). This direction increases strictly with \(t\) and tends to \(\theta_D\) as \(t\uparrow D\).

The optimal orientation therefore jumps from \(0\) to \(\theta_0>0\) at \(t_0\), while the maximal-overlap profile is continuous but has the strictly positive slope jump
\[
M'_+(t_0)-M'_-(t_0)=t_0\sin\theta_0\cos\theta_0.
\]
At \(t=0\) all directions give full overlap, and at \(t\ge D\) every direction gives zero overlap.

## Assumptions and scope

The rectangle is fixed and translated without rotation. Length \(t\) is measured in the ordinary ambient Euclidean metric, not in the rectangle's Minkowski gauge. The side inequality \(a>b>0\) is strict: the known square case is excluded from the contribution. The exact zero-overlap endpoint is \(D\), the rectangle's diagonal length. The classification counts orientations modulo coordinate sign, and specifies all their reflected copies. The theorem concerns an optimization of the covariogram on each Euclidean circle, not recovery of the rectangle from its whole covariogram.

## Proof

**Step 1: Product formula and angular reduction.** For \(h=(h_1,h_2)\), independent interval overlaps give
\[
g_K(h)=(a-|h_1|)_+(b-|h_2|)_+.
\]
It suffices by coordinate sign symmetry to consider \(h=t(\cos\theta,\sin\theta)\) with \(0\le\theta\le\pi/2\). For \(0\le\theta\le\pi/4\), swapping the coordinates reduces, or leaves unchanged, the overlap: if both products are positive their difference is \(t(a-b)(\cos\theta-\sin\theta)\ge0\), and if the reflected product vanishes the claim is immediate. The inequality is strict away from \(\theta=\pi/4\) whenever the reflected overlap is positive. Thus a maximizer can be chosen in \([0,\pi/4]\), and one in \((\pi/4,\pi/2)\) cannot be globally optimal when it has positive overlap. Since \(t<D\), choosing \(\theta_D=\arctan(b/a)\) yields strictly positive overlap \(ab(1-t/D)^2\), so every maximizer has positive overlap.

**Step 2: The global axis-versus-oblique threshold.** Initially suppose \(0<t<a\), so the axial candidate gives \(b(a-t)>0\). For every interior feasible angle \(0<\theta\le\pi/4\), a direct subtraction and half-angle identity yield
\[
g_K(t\cos\theta,t\sin\theta)-b(a-t)
=t\sin\theta\cos\theta\bigl(t-f(\theta)\bigr),
\quad f(\theta)=\frac{a-b\tan(\theta/2)}{\cos\theta}.
\]
Writing \(z=\tan(\theta/2)\), the admissible range is \(0\le z\le\sqrt2-1\) and
\[
f(z)=\frac{(a-bz)(1+z^2)}{1-z^2},\qquad
f'(z)=\frac{b\,[z^4-4z^2+4rz-1]}{(1-z^2)^2}.
\]
The quartic \(q(z)=z^4-4z^2+4rz-1\) is strictly increasing on this interval, because \(q'(z)=4z^3-8z+4r>0\) for \(r>1\) and \(0\le z\le\sqrt2-1\). It is negative at zero and positive at \(\sqrt2-1\). Therefore it has exactly one root \(z_*\), furnishing the unique strict global minimum \(t_0=f(z_*)\). Since \(f'(0)=-b<0\) and \(f(0)=a\), we have \(0<t_0<a\). For \(t<t_0\) the axis strictly dominates every other feasible angle; at \(t=t_0\) its only nonaxial competitor is \(\theta_0=2\arctan z_*\). The competitor is feasible because the root equation implies
\[
\frac ab\sin\theta_0=\frac{1+4z_*^2-z_*^4}{2(1+z_*^2)}<1,
\]
and \(t_0<a\). At \(t_0<t<a\), the same feasible \(\theta_0\) strictly improves upon the axis. For \(a\le t<D\), the axis has zero overlap while the diagonal-proportional orientation \(\theta_D\) has positive overlap, so it is likewise suboptimal.

**Step 3: A unique oblique maximizing branch.** On any positive-overlap angular interval \((0,\pi/4)\), differentiation gives
\[
\frac{\partial}{\partial\theta}g_K(t\cos\theta,t\sin\theta)
=t\cos(2\theta)\,[t-T(\theta)],\qquad
T(\theta)=\frac{a\cos\theta-b\sin\theta}{\cos(2\theta)}.
\]
With \(w=\tan\theta\in(0,1)\), the derivative of \(T=(a-bw)\sqrt{1+w^2}/(1-w^2)\) has the sign of
\[
H(w)=aw^3-3bw^2+3aw-b.
\]
Now \(H'(w)=3a[(w-b/a)^2+1-(b/a)^2]>0\), \(H(0)=-b<0\), and \(H(1)=4(a-b)>0\). Consequently \(T\) decreases strictly to one minimum and then increases strictly to infinity. Any lower-branch solution of \(T(\theta)=t\) is a local minimum of the angular overlap; the upper-branch solution is its only possible interior local maximum. Since \(\theta_0\) is a strict interior maximum at \(t=t_0\), it lies on the upper branch. Moreover \(T(\theta_D)=D\), and \(H(b/a)=2b[1-(b/a)^2]>0\). For \(t_0<t<D\), the upper-branch inverse \(\theta_*(t)\) therefore exists uniquely between \(\theta_0\) and \(\theta_D\), is strictly increasing, and has positive overlap: the two interval factors remain positive because \(\tan\theta_*<b/a\). The angular endpoint \(\theta=\pi/4\) cannot be a positive-overlap maximizer, as its derivative is negative there; zero-overlap endpoints are dominated. Together with Step 2, the upper-branch point is the unique global maximizer in \((0,\pi/4]\).

**Step 4: Jump and derivative.** The two maximizing angles \(0\) and \(\theta_0\) at \(t_0\) are distinct. The envelope theorem for the smooth upper branch gives the right derivative \(-b\cos\theta_0-a\sin\theta_0+2t_0\sin\theta_0\cos\theta_0\), while the left derivative is \(-b\). The stationary-angle equation and equality with the axis simplify their difference exactly to \(t_0\sin\theta_0\cos\theta_0>0\). Continuity of \(M\) follows from maximizing the continuous covariogram over the compact circle. The endpoint cases follow from the product formula and Cauchy–Schwarz. This proves the classification.

## Verification

The theorem is proved by the analytic derivative and constrained-overlap arguments above. The standalone standard-library script `verify.py` recomputes the critical quartic root, independently maximizes the explicit rectangle-intersection product over dense direction grids and sampled lengths, and compares the predicted orientation and positive derivative jump across several aspect ratios. Execute `python3 verify.py`. Its finite numerical tests cannot establish the all-parameter result, which depends on the proof.

## Relationship to prior work

Meyer–Reisner–Schmuckenschläger (arXiv:math/9204212v1, 1992) investigate volumes of intersections with translates, including geometric rigidity when such volumes depend only on a body's own gauge. Averkov–Bianchi (2009) prove planar covariogram determination, and Bianchi–Gardner–Kiderlen (2010) analyze covariogram-based reconstruction. These concern full-covariogram and recovery/rigidity questions, not this anisotropic fixed-Euclidean-distance extremizer.

A previously published exact hypercube fixed-distance phase diagram (published-finding corpus record `2026/10/11/SCOPE-a-complete-translation-distance-phase-diagram-for-hypercube-cova--5fadf7c81348`) establishes the square case and all higher-dimensional cubes. Its theorem expressly does not cover unequal rectangles. This result does not claim that square case and instead classifies the nontrivial aspect-ratio-dependent, nonsquare orientation jump, its quartic threshold, and the unique oblique branch. No inference of definitive historical priority is made from the searches.

## Limitations

No corresponding claim is made for arbitrary parallelograms under Euclidean distance, rotated overlapping rectangles, higher-dimensional nonsquare boxes, or minima of the covariogram. The generalization of an elementary product optimization might appear in older optimization literature without covariogram terminology; further priority checks remain warranted. No independent mathematical audit has been performed.

## References

1. M. Meyer, S. Reisner and M. Schmuckenschläger, *The Volume of the Intersection of a Convex Body with its Translates*, arXiv:math/9204212v1, first submitted 1992-04-14; https://arxiv.org/abs/math/9204212.
2. G. Averkov and G. Bianchi, *Confirmation of Matheron's conjecture on the covariogram of a planar convex body*, Journal of the European Mathematical Society 11 (2009), 1187–1202; https://doi.org/10.4171/JEMS/179.
3. G. Bianchi, R. J. Gardner and M. Kiderlen, *Phase retrieval for characteristic functions of convex bodies and reconstruction from covariograms*, arXiv:1003.4486v1, first submitted 2010-03-23; https://arxiv.org/abs/1003.4486.
4. *A complete translation-distance phase diagram for hypercube covariograms*, published-finding corpus, 2026-10-11; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-complete-translation-distance-phase-diagram-for-hypercube-cova--5fadf7c81348.
