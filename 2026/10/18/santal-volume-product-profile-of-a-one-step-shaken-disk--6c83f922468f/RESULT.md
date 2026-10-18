# Santaló volume-product profile of a one-step shaken disk

## Finding
For the vertical \(\lambda\)-Steiner operation, with \(0\le\lambda\le1/2\), applied once to the Euclidean unit disk, set \(\delta=1-2\lambda\). Write the resulting body as
\[
K_\delta=\left\{(x,y):-1\le x\le1,\; -(1-\delta)\sqrt{1-x^2}\le y\le(1+\delta)\sqrt{1-x^2}\right\},\qquad 0\le\delta\le1.
\]
The Santaló point is \((0,c_\delta)\), where \(c_0=0\), while \(0<c_\delta<1+\delta\) for every \(0<\delta\le1\). It is the *unique* minimizer of the explicit one-dimensional function
\[
I_\delta(c)=\tfrac12\bigl[J(1+\delta,c)+J(1-\delta,-c)\bigr],\qquad -(1-\delta)<c<1+\delta,
\]
with \(0<c<2\) for \(\delta=1\), where
\[
J(a,c)=\int_{-\infty}^{\infty}\frac{du}{(\sqrt{u^2+a^2}-c)^2},\quad a>0,\ c<a;
\qquad J(0,c)=-\frac{2}{c}\quad(c<0).
\]
Consequently, the *exact* Santaló volume product \(\mathcal M(\delta)=|K_\delta|\,|(K_\delta-(0,c_\delta))^\circ|\) is
\[
\boxed{\mathcal M(\delta)=\pi I_\delta(c_\delta).}
\]
The formula has a completely elementary evaluation: put
\[
G(a,c)=\begin{cases}
\dfrac{2\arccos(-c/a)}{\sqrt{a^2-c^2}},&-a<c<a,\\[4pt]
\dfrac{4\operatorname{artanh}\sqrt{(-a-c)/(a-c)}}{\sqrt{c^2-a^2}},&c<-a.
\end{cases}
\]
Then \(J(a,c)=(a^2G(a,c)+2c)/(a^2-c^2)\) for \(c\ne-a\), and \(J(a,-a)=4/(3a)\). The polar-area minimizer is characterized without any undetermined geometric data by the scalar equation \(\partial_c I_\delta(c_\delta)=0\).

The volume product is **strictly decreasing** on \(0\le\delta\le1\). Its exact second-order decrease at the disk is
\[
\boxed{\mathcal M(\delta)=\pi^2-\left(\frac{32}{3}-\pi^2\right)\delta^2+O(\delta^4),\qquad c_\delta=\frac{8}{3\pi}\delta+O(\delta^3).}
\]
In fact, the vertical coordinate of the centroid of \(K_\delta\) is exactly \(8\delta/(3\pi)\), whereas the Santaló center has the sharper expansion
\[
\boxed{c_\delta=\frac{8}{3\pi}\delta+\frac{32(88-9\pi^2)}{27\pi^3}\delta^3+O(\delta^5).}
\]
Because \(88-9\pi^2<0\), the Santaló point sits strictly below the centroid for all sufficiently small positive \(\delta\). The coefficient \(32/3-\pi^2>0\) is sharp in the sense of the actual leading expansion. At the shaking endpoint \(\delta=1\), \(c_1\approx0.7832818394699077\) and \(\mathcal M(1)\approx8.716345507152886\).

## Assumptions and scope
The disk is the closed Euclidean unit disk in \(\mathbb R^2\). All areas are ordinary Euclidean areas. \(C^\circ\) means the polar about the origin for a body containing the origin in its interior. The Santaló point is the unique interior translation minimizing polar area. The parameter \(\delta\) runs through the full closed interval \([0,1]\), including the flat-edged shaking endpoint. Statements about smooth expansions are local to \(\delta=0\). Only a *single operation on a disk* is considered, not an iterated random process.

## Proof
**1. Geometry and volume.** A vertical chord of the disk above horizontal coordinate \(x\) has length \(2\sqrt{1-x^2}\). Moving its center by \(\delta\sqrt{1-x^2}\) gives the displayed boundary equations, matching the definition of the \(\lambda\)-Steiner operation. Its area is independent of \(\delta\): integrating the chord lengths gives \(|K_\delta|=\pi\). Reflection \((x,y)\mapsto(-x,y)\) forces the unique Santaló point onto the vertical axis.

**2. Polar integral and minimizer.** For a unit normal direction \((\cos\theta,\sin\theta)\), the support function of \(K_\delta\) equals \(\sqrt{\cos^2\theta+(1+\delta)^2\sin^2\theta}\) when \(\sin\theta\ge0\), and the same expression with \(1-\delta\) when \(\sin\theta<0\). Translating by \((0,c)\) subtracts \(c\sin\theta\). Polar area is half the angular integral of the reciprocal support squared. On each semicircle the substitution \(u=\cot\theta\) converts this to \(J\), proving \(I_\delta(c)\), including the limiting \(a=0\) case. For all admissible centers, differentiating under the integral gives
\[
\frac{d^2}{dc^2}I_\delta(c)=3\int_{-\infty}^{\infty}\left[\frac1{(\sqrt{u^2+(1+\delta)^2}-c)^4}+\frac1{(\sqrt{u^2+(1-\delta)^2}+c)^4}\right]du>0.
\]
When \(\delta=1\) the second denominator is \(|u|+c\) and the admissible center has \(c>0\). The polar area tends to infinity as \(c\) approaches either end of the interior vertical interval; strict convexity therefore gives exactly one minimizing center. At \(\delta>0\), the derivative at \(c=0\), when admissible, is \(2[(1+\delta)^{-2}-(1-\delta)^{-2}]<0\), so \(c_\delta>0\). In the endpoint case \(c>0\) is necessary for interiority.

**3. Elementary primitive.** Substitute \(u=a\sinh t\) and integrate the elementary rational function in \(\tanh(t/2)\). This yields \(G(a,c)=\int_{-\infty}^{\infty}(a\cosh t-c)^{-1}dt\) in the two stated arccos/artanh branches. Differentiating \(cG\) (or integrating the identity for \(a\cosh t\)) gives \(J=G+c\partial_cG=(a^2G+2c)/(a^2-c^2)\). Direct integration at \(c=-a\) yields \(4/(3a)\).

**4. Strict monotonicity.** The family \(K_\delta\), extended to \(-1\le\delta\le1\) by vertical reflection, is a volume-preserving shadow system obtained by vertical displacement of each original disk point with speed \(\sqrt{1-x^2}\). Meyer–Reisner's polar-shadow convexity theorem implies that \(\delta\mapsto1/|(K_\delta-s(K_\delta))^\circ|\) is convex. Vertical reflection makes it even, hence nondecreasing on nonnegative \(\delta\). If it took the same value at two distinct nonnegative parameters, convexity would force a constant interval centered at zero. The affine-rigidity clause of that theorem would force every \(K_\delta\) in that interval to be an affine image of the disk, hence an ellipse. For every \(\delta>0\), however, its upper and lower boundary arcs lie on distinct ellipses of respective vertical semiaxes \(1+\delta\) and \(1-\delta\), and together cannot lie on one nondegenerate conic. Thus there is no nontrivial plateau, and the volume product decreases strictly.

**5. Sharp quadratic coefficient.** Uniform Taylor expansion of the polar integral near \((a,c)=(1,0)\) gives
\[
J(a,c)=\frac\pi a+\frac{4c}{a^2}+\frac{3\pi c^2}{2a^3}+O(c^3).
\]
Substitution of \(a=1\pm\delta\) gives
\[
I_\delta(c)=\pi+\pi\delta^2-8c\delta+\frac{3\pi}{2}c^2+O((|c|+|\delta|)^3).
\]
The implicit-function theorem at \((\delta,c)=(0,0)\) and even/odd reflection symmetry yield \(c_\delta=8\delta/(3\pi)+O(\delta^3)\) and \(\mathcal M(\delta)=\pi^2-(32/3-\pi^2)\delta^2+O(\delta^4)\). The further expansion follows from the absolutely convergent series, valid for \(|c|<a\),
\[
J(a,c)=\frac{\pi}{a}+\frac{4c}{a^2}+\frac{3\pi c^2}{2a^3}+\frac{16c^3}{3a^4}+\frac{15\pi c^4}{8a^5}+O(c^5).
\]
Solving the critical equation through cubic order gives the stated coefficient \(32(88-9\pi^2)/(27\pi^3)\). The centroid is calculated directly from the first vertical moment \(\frac12\int_{-1}^1[(1+\delta)^2-(1-\delta)^2](1-x^2)\,dx\) divided by area \(\pi\). Since \(32/3>\pi^2\), the Mahler deficit coefficient is strictly positive.

## Verification
The standalone `checker.py` evaluates \(J\) by both its elementary closed form and independent improper quadrature; reconstructs Santaló centers from a derivative root; tests several parameters, including the shaking endpoint; and checks the quadratic coefficient. Execute `python3 checker.py` with Python and `mpmath` installed. The numerical tests are finite spot checks; the exact formulas, uniqueness, strict monotonicity, and asymptotic coefficient rest on the preceding mathematical proof and the cited shadow-system theorem.

## Relationship to prior work
Kipp and Sagmeister (2026) define the \(\lambda\)-Steiner operation and investigate convergence of repeated random operations, supplying the natural interpolation here. Their work does not assert a Santaló polar-area formula or this sharp second variation. Meyer and Reisner (2006, restated in their 2018/2019 paper) already establish the convexity and affine rigidity of reciprocal Santaló polar volume along shadow systems; the monotonicity mechanism used above is **their theorem**, not a new general principle. The new, narrower result is the complete explicit scalar Santaló-product law for the canonical one-step disk deformation, its moving minimizing center, the nontrivial quadratic constant, and the exact shaking endpoint. No claim of novelty is made for the classical Blaschke–Santaló inequality or for convexity of reciprocal polar volume.

## Limitations
An elementary one-dimensional root is required for the Santaló center; the root is unique but is not expressed as an elementary closed radical. This theorem is restricted to one-step images of disks and cannot be read as a formula for arbitrary convex bodies or random iterates. The matching of all earlier bibliographic appearances of this special scalar profile is not exhaustive, and independent mathematical validation has not been conducted.

## References
1. C. Kipp and Á. Sagmeister, *Random convergence of generalized Steiner processes*, arXiv:2610.05113v1, first public 2026-10-04, especially Definition 1.1; https://arxiv.org/html/2610.05113v1.
2. M. Meyer and S. Reisner, *Shadow Systems and Volumes of Polar Convex Bodies*, *Mathematika* **53** (2006), 129–148, Theorem 1 and Proposition 7, lawful full preprint https://arxiv.org/pdf/math/0606305 and https://doi.org/10.1112/S0025579300000061.
3. M. Meyer and S. Reisner, *Ellipsoids are the only local maximizers of the volume product*, arXiv:1812.11607v1 (2018), especially Theorem 1, https://arxiv.org/pdf/1812.11607.
