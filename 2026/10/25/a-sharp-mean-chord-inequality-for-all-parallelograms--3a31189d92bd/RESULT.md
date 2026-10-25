# A sharp mean-chord inequality for all parallelograms

## Finding
For every nondegenerate Euclidean parallelogram \(K\) with perimeter \(p\), and any point \(P\in K\), the expected length of the chord of \(K\) through \(P\), using uniform unoriented line direction, satisfies
\[
M_K(P)\le\frac{p}{\pi}\operatorname{arsinh}(1)
=\frac{p}{\pi}\log(1+\sqrt2).
\]
Equality occurs exactly when \(K\) is a square and \(P\) is its center. This is also the sharp result among all nondegenerate centrally symmetric convex quadrilaterals.

## Assumptions and scope
The plane carries the Euclidean metric and Lebesgue area measure. A parallelogram is the compact convex hull of two independent edge vectors and their translates; nondegenerate means positive area. For each \(\theta\in[0,\pi)\), let \(L(P,\theta)\) be the full unoriented line through \(P\) of angle \(\theta\). Define
\[
M_K(P)=\frac1\pi\int_0^\pi\mathcal H^1(K\cap L(P,\theta))\,d\theta.
\]
The point \(P\) may lie in the interior or on the boundary. Tangent or exceptional directions do not affect the integral. This is not the average under motion-invariant random affine lines, where the sampling probabilities and normalization differ. The perimeter is the sum of the four side lengths, not the semiperimeter.

## Proof
**1. Angular mean equals an inverse-distance potential.** Because \(K\) is convex and \(P\in K\), its ray intersection from \(P\) has a radial length \(\rho_P(\theta)\ge0\), even on boundary rays. The length of the unoriented chord in direction \(\theta\) is \(\rho_P(\theta)+\rho_P(\theta+\pi)\). Consequently polar integration about \(P\) gives
\[
\pi M_K(P)=\int_0^{2\pi}\rho_P(\theta)\,d\theta
=\int_K\frac{dx}{|x-P|}=:V_K(P).
\]
The point singularity is integrable in two dimensions.

**2. A symmetric body's center uniquely maximizes this potential.** Translate coordinates so that \(K=-K\). For any \(r>0\), set \(E_r=K\cap(P+B_r)\), where \(B_r\) is the closed disk of radius \(r\) centered at the origin. Then \(-E_r=K\cap(-P+B_r)\), and convexity and symmetry imply
\[
\tfrac12(E_r+(-E_r))\subset K\cap B_r.
\]
The planar Brunn–Minkowski inequality therefore gives \(|K\cap(P+B_r)|\le |K\cap B_r|\). The layer-cake identity
\[
V_K(P)=\int_0^\infty |K\cap(P+B_r)|\,\frac{dr}{r^2}
\]
proves \(V_K(P)\le V_K(0)\). For strictness when \(P\ne0\), let \(R=\max_{x\in K}|x|\) and choose \(x\in K\) with \(|x|=R\). Since \(\max\{|x-P|,|-x-P|\}>R\), one of the opposite extreme points has distance greater than \(R\) from \(P\). Thus for an interval of radii just above \(R\), the disk centered at \(P\) omits a positive-area portion of \(K\), while the disk centered at zero contains \(K\). The layer-cake comparison is strict, so \(V_K(P)<V_K(0)\). This applies to boundary points as well.

**3. Straightening an arbitrary parallelogram improves the fixed-perimeter functional.** Rotate the centered parallelogram so that its independent edge vectors are \((a,0)\) and \((s,h)\), with \(a,h>0\) and \(s\in\mathbb R\). Its horizontal section at height \(y\in[-h/2,h/2]\) is
\[
[sy/h-a/2,\;sy/h+a/2].
\]
For fixed \(y\ne0\), the function \(x\mapsto(x^2+y^2)^{-1/2}\) is even and strictly decreasing with \(|x|\). The integral over a length-\(a\) interval is therefore maximal when that interval is centered at zero, strictly so unless its center vanishes. Integrating over \(y\) gives
\[
V_K(0)\le V_{R_{a,h}}(0),
\]
with equality exactly when \(s=0\), where \(R_{a,h}=[-a/2,a/2]\times[-h/2,h/2]\). Moreover,
\[
\operatorname{per}(K)=2(a+\sqrt{h^2+s^2})\ge2(a+h)=\operatorname{per}(R_{a,h}),
\]
again with equality exactly when \(s=0\). The potential \(V\) is homogeneous of degree one under uniform dilation; combining these inequalities reduces the fixed-perimeter maximum to rectangles, with equality in the reduction only for a genuine rectangle.

**4. The square is uniquely optimal among rectangles.** Direct integration over the four quarters yields
\[
V_{R_{a,h}}(0)=2\left[a\operatorname{arsinh}(h/a)
+h\operatorname{arsinh}(a/h)\right].
\]
For example, the primitive identity follows by differentiating \(\int_0^A\int_0^B(x^2+y^2)^{-1/2}\,dy\,dx=A\operatorname{arsinh}(B/A)+B\operatorname{arsinh}(A/B)\) with respect to \(A\) and checking its zero boundary value. The function \(f(t)=\operatorname{arsinh}(t)\) has strictly negative second derivative \(f''(t)=-t(1+t^2)^{-3/2}\) for \(t>0\). Weighted Jensen with weights \(a/(a+h)\), \(h/(a+h)\) and arguments \(h/a\), \(a/h\) gives
\[
\begin{aligned}
\frac{a f(h/a)+h f(a/h)}{a+h}
&\le f\!\left(\frac{a(h/a)+h(a/h)}{a+h}\right)\\
&=f(1).
\end{aligned}
\]
Strict concavity forces equality precisely when \(a=h\). Hence \(V_{R_{a,h}}(0)\le2(a+h)\operatorname{arsinh}(1)=\operatorname{per}(R_{a,h})\operatorname{arsinh}(1)\). Together with the preceding steps this yields \(V_K(P)\le p\operatorname{arsinh}(1)\), and equality requires first \(P=0\), then \(s=0\), then \(a=h\). Conversely a centered square satisfies equality in each step. Division by \(\pi\) proves the stated mean-chord inequality.

## Verification
All steps above are analytic and apply to all real positive side dimensions, all shear parameters, and every allowable point. The layer-cake formula is valid because \(|x-P|^{-1}\) is locally integrable in the plane; positivity permits Tonelli's theorem. The rectangle integral was checked by differentiation and by direct numerical quadrature for several non-square and sheared cases in the accompanying optional `check_parallelogram.py`. Finite numerical tests are illustrative and are not used for the universal theorem or its equality classification.

## Relationship to prior work
Rabinowitz's 2026 paper proves a sharp fixed-perimeter angular mean-chord inequality for **triangles**, with the equilateral triangle and its center uniquely extremal; the present theorem resolves the next natural centrally symmetric four-vertex family and supplies its distinct sharp constant. The centered-potential step is a standard symmetric-unimodal convolution principle, closely related to Anderson's 1955 inequality; only its elementary specialization is needed here. Other published studies of random chords of parallelograms concern independently sampled endpoint or interior-point ensembles, and studies of regular polygon central chords concern a fixed regular shape. Neither statement gives the fixed-perimeter comparison for every parallelogram and arbitrary chord base point. The proof is elementary and priority over all unindexed classical literature is not asserted.

## Limitations
No inequality is claimed for arbitrary non-centrally symmetric quadrilaterals or all convex bodies. The result has a fixed-perimeter, fixed-point angle-uniform sampling model; it is distinct from translation-invariant random-line averages. The result does not claim that its four inequalities constitute a new technique. The possible existence of an earlier equivalent statement in unindexed literature remains a residual priority risk; independent mathematical review has not been performed.

## References
1. S. Rabinowitz, *Average Chord Lengths in a Triangle* (2026), arXiv:2609.11370v1, first public 2026-09-10, https://arxiv.org/abs/2609.11370.
2. T. W. Anderson, *The integral of a symmetric unimodal function over a symmetric convex set and some probability inequalities*, Proceedings of the American Mathematical Society **6** (1955), 170–176.
3. *Fourth chord moment amplification and angular phase transition for parallelograms* (2026), public research record https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-fourth-chord-moment-amplification-and-angular-phase-transition-f--45b0568cfb6e (different chord sampling law; search-index evidence only).
