# Strict finite-vertex area–perimeter incompatibility for noncircular ellipses

## Finding

Let \(a>b>0\), \(n\ge3\), and let \(E\) be the filled ellipse with semiaxes \(a,b\). Every maximum-area convex inscribed \(n\)-gon is the affine image of a regular \(n\)-gon, with vertices
\[
p_j(\phi)=(a\cos(\phi+2\pi j/n),b\sin(\phi+2\pi j/n)),\quad 0\le j<n.
\]
Consider stationarity of its ordinary Euclidean perimeter against **independent boundary motions** of the individual vertices (not merely rotation of the entire affine-regular family). The gradient vanishes at every vertex if and only if \(n=4\) and \(\phi\in(\pi/2)\mathbb Z\). In particular, **for every \(n\ne4\), no maximum-area inscribed \(n\)-gon can maximize perimeter**.

This separation is quantitatively uniform over the complete one-parameter family of maximum-area \(n\)-gons. Let \(P_n^*(E)\) denote the maximal Euclidean perimeter among convex \(n\)-gons inscribed in \(E\). For \(n\ne4\), put
\[
h=\pi/n,\quad N=n/\gcd(n,4),\quad
G=\frac{(a^2-b^2)b^2\sin^3(2h)}{8a^3\cos h}\cos\frac{\pi}{2N},\qquad
H=2a+\frac{a^2}{b\sin(h/2)}.
\]
Then \(N\ge2\), \(G>0\), and **for every phase** \(\phi\),
\[
\boxed{P_n^*(E)-\operatorname{Per}(p_0(\phi),\ldots,p_{n-1}(\phi))
\ge \frac G2\min\{h,G/H\}>0.}
\]
The constant is explicit but is not claimed sharp. The exceptional quadrilateral statement classifies only first-order stationarity, not the global perimeter maximizers at \(n=4\).

## Assumptions and scope

Here \(E=\{(x,y):(x/a)^2+(y/b)^2\le1\}\). Vertices lie on \(\partial E\) and are cyclically ordered, with distinct consecutive vertices. The perimeter is the sum of Euclidean chord lengths. Since \(E\) is strictly convex, an ordered polygon with distinct cyclic vertices is convex and remains so under small single-vertex motions preserving cyclic order. For each \(n\ge3\), the maximum-area family above exhausts all convex inscribed \(n\)-gons of maximum area and has area \(ab(n/2)\sin(2\pi/n)\). The circle \(a=b\) is excluded: its area-maximizing regular polygons also maximize perimeter, by concavity of sine.

## Proof

**1. All maximum-area polygons.** Under inverse diagonal scaling by \(\operatorname{diag}(1/a,1/b)\), the ellipse becomes the unit disk and areas acquire a common factor \(ab\). Among cyclically ordered unit-circle vertices the area is maximized by equally spaced points. One proof takes each consecutive central-angle gap \(\Delta_j>0\), summing to \(2\pi\): twice the signed polygon area is \(\sum_j\sin\Delta_j\). For any interior maximum, varying one vertex with fixed two neighbors gives a unique local maximum at the arc midpoint, since its two adjacent contributions sum to \(2\sin((\Delta_{j-1}+\Delta_j)/2)\cos((\Delta_{j-1}-\Delta_j)/2)\), with the total two-gap angle strictly between \(0\) and \(2\pi\). Thus adjacent gaps coincide, and all are \(2\pi/n\). Existence of a global regular maximizer and strict inequalities for polygons with coincident vertices complete the argument. Affine scaling preserves this entire family.

**2. Individual-vertex perimeter gradient.** Set \(t_j=\phi+2\pi j/n\), \(h=\pi/n\), \(A=\operatorname{diag}(a,b)\), and \(w(t)=(-\sin t,\cos t)\). For a fixed vertex \(j\), define
\[
u_j^-=Aw(t_j-h),\quad u_j^+=Aw(t_j+h),\quad
F_j^\pm=\|u_j^\pm\|,\quad B_j=\langle u_j^-,u_j^+\rangle.
\]
Varying only the boundary parameter of vertex \(j\) differentiates exactly the two incident chord lengths. The unit incident chord vectors are \(u_j^-/F_j^-\) and \(u_j^+/F_j^+\); the vertex's tangent vector is \(Aw(t_j)=(u_j^-+u_j^+)/(2\cos h)\). Therefore its perimeter derivative is
\[
D_j=\frac{(F_j^--F_j^+)}{2\cos h}
\left(1-\frac{B_j}{F_j^-F_j^+}\right).
\]
These two chord vectors are never parallel because their determinant has absolute value \(ab\sin(2h)>0\). Cauchy–Schwarz is thus strict, so the parenthesized factor is positive. Direct trigonometry gives
\[
(F_j^-)^2-(F_j^+)^2=-(a^2-b^2)\sin(2h)\sin(2t_j).
\]
As \(a>b\), \(D_j=0\) holds precisely for \(t_j\in(\pi/2)\mathbb Z\). All the \(n\) consecutive parameters are multiples of \(\pi/2\) modulo \(\pi\) only when \(2\pi/n\) is a multiple of \(\pi/2\), which for \(n\ge3\) gives \(n=4\). At \(n=4\) this occurs exactly for \(\phi\in(\pi/2)\mathbb Z\). Every other candidate has at least one nonzero independent first variation, hence cannot globally maximize perimeter.

**3. Uniform lower bound for a gradient coordinate.** The distinct values of \(2t_j\) modulo \(\pi\) form a uniform \(N=n/\gcd(n,4)\)-point grid, implying
\[
\max_j|\sin(2t_j)|\ge\cos(\pi/(2N)).
\]
By \(F_j^-+F_j^+\le2a\), the squared-norm difference above gives
\[
|F_j^--F_j^+|\ge\frac{(a^2-b^2)\sin(2h)}{2a}|\sin(2t_j)|.
\]
The determinant identity and \(1-\cos\vartheta\ge\sin^2\vartheta/2\), with \(F_j^\pm\le a\), give
\[
1-\frac{B_j}{F_j^-F_j^+}
\ge\frac{|\det(u_j^-,u_j^+)|^2}{2(F_j^-F_j^+)^2}
\ge\frac{b^2\sin^2(2h)}{2a^2}.
\]
Consequently \(\max_j|D_j|\ge G>0\), with \(G\) as stated.

**4. Turning first variation into a quantitative gap.** Choose \(j\) with \(|D_j|\ge G\), and move only its boundary angle by \(s\operatorname{sign}(D_j)\), \(0\le s\le h\). Both adjacent angular gaps initially equal \(2h\), hence remain at least \(h\). Their Euclidean chord lengths remain at least \(2b\sin(h/2)\). For any nonzero differentiable vector \(z(s)\),
\[
\left|\frac{d^2}{ds^2}\|z(s)\|\right|\le\|z''(s)\|+\frac{\|z'(s)\|^2}{\|z(s)\|}.
\]
Since a moving vertex has \(\|p_j'\|,\|p_j''\|\le a\), the second derivative of the sum of its two incident chord lengths is bounded in absolute value by \(H=2a+a^2/(b\sin(h/2))\). Thus, for \(\delta=\min(h,G/H)\), Taylor's integral remainder yields an admissible polygon with
\[
P(\delta)-P(0)\ge G\delta-\frac12H\delta^2\ge\frac12G\delta.
\]
The global supremum of perimeter is attained by compactness of cyclic vertex configurations; the right-hand side is positive and uniform in \(\phi\). This proves the stated bound.

## Verification

The standalone script `verify.py` uses only the Python 3 standard library and a fixed random seed. Run `python3 verify.py` next to these documents. It checks analytic individual-vertex derivatives against centered finite differences, the uniform-gradient lower bound, the predicted positive perimeter improvement for admissible single-vertex perturbations, and the exceptional quadrilateral phases. The script reports `VERIFY_OK 2320` for 2,320 finite assertions. These checks corroborate formulas, but the theorem for all ellipses and all \(n\) rests on the proof above.

## Relationship to prior work

Hoehner [1] characterizes the Euclidean ball through asymptotically optimal random-polytope approximation densities for two intrinsic-volume functionals, a motivation for considering two incompatible geometric objectives. The present claim is a deterministic, fixed-vertex-count statement specifically for ellipses, not an implication of those asymptotics.

The standard description of area-maximizing inscribed ellipse polygons is given explicitly by Pamfilos [2]. The published record [3] proves a distinct orientation-selection theorem for the Euclidean perimeter **restricted to the one-parameter maximum-area family**. That restricts all vertex motions to a common phase and does not imply perimeter stationarity under independent vertex variations, nor the quantified difference from the unrestricted perimeter optimum. This exact distinction is central to the contribution.

The long-standing maximum-perimeter-inscribed-polygon question [4] records the reflection-law/billiard necessary conditions. We exploit and evaluate this condition for the affine-regular family in order to settle simultaneous optimality for all \(n\ne4\). Earlier work on maximal inscribed rectangles and parallelograms already treats aspects of the four-vertex exception; no global quadrilateral maximality assertion is made here.

## Limitations

The uniform gap is explicitly positive but not claimed optimal. No exact formula for the unrestricted maximum perimeter is provided, nor is a full classification of its optimizing polygons. The sole exceptional case \(n=4\) is classified only for first-order stationarity among maximum-area inscribed quadrilaterals. The theorem does not address nonsmooth convex curves or ellipses degenerating to line segments. Historical priority of the first-variation obstruction remains provisional, as older billiard and affine-regular-polygon treatments may contain equivalent implicit statements.

## References

[1] S. Hoehner, *Simultaneous random polytope approximation characterizes the Euclidean ball*, arXiv:2602.18547, first posted 2026-02-20, https://arxiv.org/abs/2602.18547 (primary MSC2020 52A27).

[2] P. Pamfilos, *Maximal Polygon in Ellipse*, https://users.math.uoc.gr/~pamfilos/eGallery/problems/MaximalRegInEllipse.html (public posting date not established).

[3] *Exact perimeter selection among maximum-area polygons inscribed in ellipses*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-perimeter-selection-among-maximum-area-polygons-inscribed--9338777854e9, dated 2026-10-11.

[4] R. Nandakumar, *Inscribed n-gons of maximum perimeter for an ellipse*, MathOverflow, question posted 2021-10-27, https://mathoverflow.net/questions/407192/inscribed-n-gons-of-maximum-perimeter-for-an-ellipse.

[5] P. Gronchi, M. Longinetti, *Affinely Regular Polygons as Extremals of Area Functionals*, Discrete & Computational Geometry 39 (2008), 273–297, DOI:10.1007/s00454-007-9010-5; full text not inspected.
