# Four exact partial-plank phases of the regular hexagon

## Finding

Let \(H\) be the regular planar hexagon of circumradius one, and let \(0<W<\sqrt3\). Among **all finite families** of Euclidean planks of total width at most \(W\), the greatest covered area is \((3\sqrt3/2)\Phi(W)\), where

\[
\Phi(W)=\begin{cases}
\dfrac{4W}{3\sqrt3}-\dfrac{W^2}{9},&0<W\le\dfrac{\sqrt3}{2},\\[3pt]
\dfrac{1+W^2}{3},&\dfrac{\sqrt3}{2}\le W\le1,\\[3pt]
1-\dfrac{(2-W)^2}{3},&1\le W\le\dfrac32,\\[3pt]
\dfrac23+\dfrac{W^2}{9},&\dfrac32\le W<\sqrt3.
\end{cases}
\]

An optimal family consists of a single *centered* plank of width \(W\). Its unoriented unit normal is classified uniquely modulo the dihedral symmetries of the hexagon. Fix a vertex-normal axis and denote by \(\theta\in[0,\pi/6]\) the smallest nonnegative angle of an optimal normal from that axis toward an adjacent edge-normal axis. Then

\[
\theta(W)=\begin{cases}
\pi/6,&0<W\le\sqrt3/2,\\
\arctan\!\left(\dfrac{\sqrt3(1-W^2)}{W^2+\sqrt{4W^2-3}}\right),&\sqrt3/2<W<1,\\
0,&1\le W\le3/2,\\
\arctan\!\left(\dfrac{\sqrt{4W^2-9}}3\right),&3/2<W<\sqrt3.
\end{cases}
\]

In particular, **strictly oblique** orientations are optimal on exactly two disjoint width intervals: \((\sqrt3/2,1)\) and \((3/2,\sqrt3)\). Both optimal normal orbits vary continuously at the three breakpoints. At the endpoints the adjacent descriptions agree. The theorem classifies optimal **single-plank normals**; it does not assert that every optimal collection of several planks must be a single plank.

## Assumptions and scope

A Euclidean plank of width \(w\ge0\) is a set \(\{x\in\mathbb R^2:|\langle x,n\rangle-b|\le w/2\}\), with \(n\) a Euclidean unit vector. Widths of planks in a finite family add; the quantity optimized is the ordinary planar area of the intersection of \(H\) with their union. Let

\[
H=\operatorname{conv}\{(\cos(k\pi/3),\sin(k\pi/3)):k=0,\ldots,5\}.
\]

Its area is \(3\sqrt3/2\) and its minimum width is \(\sqrt3\). In this range every optimum can be attained with the stated single plank by the planar partial-plank theorem of Bakaev and Polyanskii [1]. No global uniqueness claim is made about arbitrary multi-plank families. The normal is unoriented: \(n\) and \(-n\) describe the same plank.

## Proof

**1. Reduction to centered planks and one angular chamber.** Theorem 12 of [1] proves that for every planar convex body and total width strictly below its minimum width, there exists an optimal *single* plank of that full width. For any fixed normal \(n\), the lengths of slices \(H\cap\{\langle x,n\rangle=t\}\) form an even concave function of \(t\) on the projection interval (the two-dimensional Brunn--Minkowski/linear-slicing property). Thus a centered interval of a fixed length has maximal integral, so an optimum of this normal can be centered. By the dihedral symmetries, we need only minimize the area of the positive cap for \(\theta\in[0,\pi/6]\), with \(n=(\cos\theta,\sin\theta)\).

**2. Exact cap area.** Put \(s=W/2\) and

\[
A=\cos\theta,\qquad B=\cos(\pi/3-\theta),\qquad C=\cos(\pi/3+\theta).
\]

We have \(A=B+C\) and \(0\le C\le B\le A\). The six vertex projections are \(\pm A,\pm B,\pm C\). For \(E(\theta,s)=\operatorname{Area}\{x\in H:\langle x,n\rangle>s\}\), direct clipping of the six edges at the three ordered projected vertex levels yields the continuous piecewise formulas

\[
E(\theta,s)=\begin{cases}
\dfrac{3\sqrt3}{4}-\dfrac{\sqrt3 s}{A},&0\le s\le C,\\[3pt]
\dfrac{\sqrt3}{4}\left(\dfrac{(A+B-s)^2}{AB}-1\right),&C\le s\le B,\\[3pt]
\dfrac{\sqrt3}{4}\dfrac{(A-s)^2}{BC},&B\le s<A.
\end{cases}\tag{1}
\]

At a boundary at which a displayed denominator vanishes, use the adjoining formula or its continuous limit. For completeness, the last branch is the triangle cut off near vertex \((1,0)\): the adjacent unit-hexagon triangle has area \(\sqrt3/4\), and the two edge ratios are \((A-s)/(A-B)=(A-s)/C\) and \((A-s)/(A-C)=(A-s)/B\). In the middle branch the cap is a quadrilateral. Its boundary comprises the two vertices \((1,0)\), \((1/2,\sqrt3/2)\) and the intersections with the edges leading respectively toward \((1/2,-\sqrt3/2)\) and \((-1/2,\sqrt3/2)\). If \(t=(A-s)/B\) and \(v=(B-s)/A\), these intersection points are \((1-t/2,-\sqrt3t/2)\) and \((1/2-v,\sqrt3/2)\). The shoelace formula splits this quadrilateral into two triangles and gives \(E=(\sqrt3/4)(t+v+tv)\), equal to the middle expression in (1). Once the opposite pair of vertices at levels \(\pm C\) is passed, the central chord length is constant \(\sqrt3/A\); integrating it from \(s=0\), where the cap has half the full area, gives the first expression. The branches agree at \(C\) and \(B\). The captured fraction is \(1-4E/(3\sqrt3)\).

**3. A rational angular parameter.** Define

\[
u=\sqrt3\tan\theta\in[0,1],\qquad Q(u)=\sqrt{1+u^2/3},\qquad q=sQ(u).
\]

Then \(A=1/Q\), \(B=(1+u)/(2Q)\), and \(C=(1-u)/(2Q)\). Equation (1) becomes

\[
E(u,s)=\begin{cases}
3\sqrt3/4-\sqrt3\,sQ,&q\le(1-u)/2,\\[2pt]
\dfrac{\sqrt3}{4}\left[\dfrac{((3+u)/2-sQ)^2}{(1+u)/2}-1\right],&(1-u)/2\le q\le(1+u)/2,\\[3pt]
\dfrac{\sqrt3(1-sQ)^2}{1-u^2},&q\ge(1+u)/2.
\end{cases}\tag{2}
\]

Call these, respectively, the central, quadrilateral and triangular regimes. Each term is evaluated only within its stated valid regime. The central-regime derivative is strictly negative for \(u>0\). The sign of the quadrilateral-regime derivative, for \(u<1\), is the sign of

\[
s-T(u),\qquad T(u)=\frac{3Q(u)}{2(3+u)}.
\]

Indeed, differentiate the middle expression: after removing positive factors, the derivative is \((1-u)(s-T(u))\). Moreover, \(T\) is strictly decreasing on \([0,1]\), because

\[
\frac{T'(u)}{T(u)}=\frac{u}{3+u^2}-\frac1{3+u}
=\frac{3(u-1)}{(3+u^2)(3+u)};
\]

it goes from \(1/2\) to \(\sqrt3/4\). The triangular-regime derivative has the sign of \(3Q(u)-4s\): more explicitly, it equals

\[
\frac{2\sqrt3\,u(1-sQ(u))}{(1-u^2)^2}
\left(1-\frac{4s}{3Q(u)}\right).\tag{3}
\]

Since \(0<W<\sqrt3\), every used branch has \(1-sQ>0\) when triangular.

**4. The four global minima.** If \(s<1/2\), then \(q<(1+u)/2\) throughout \([0,1]\): the ratio \(2sQ(u)/(1+u)\) is strictly decreasing, and its value at zero is \(2s<1\). The central regime, when present, decreases with \(u\); after it the quadrilateral regime applies. For \(s\le\sqrt3/4\), \(s\le T(u)\) everywhere and the cap is minimized at \(u=1\). For \(\sqrt3/4<s<1/2\), there is exactly one quadrilateral stationary point \(u_*\in(0,1)\), satisfying \(s=T(u_*)\). It really belongs to the quadrilateral regime: substituting \(s=T(u_*)\) gives \(q=(3+u_*^2)/(2(3+u_*))\), strictly between \((1-u_*)/2\) and \((1+u_*)/2\). The derivative changes from negative to positive there, so this is the unique global minimizer. With \(W=2s\), this stationary equation gives

\[
u_* =\frac{3(1-W^2)}{W^2+\sqrt{4W^2-3}}.
\]

Substitution into (2) yields the first two branches of \(\Phi\) and the corresponding angles.

If \(s\ge1/2\), the central regime is absent. The ratio \(2sQ/(1+u)\) is strictly decreasing from at least one at \(u=0\) to less than one at \(u=1\), so the triangular and quadrilateral regimes meet once. The quadrilateral cap is strictly increasing after that meeting point, because \(s\ge1/2\ge T(u)\). For \(1/2\le s\le3/4\), equation (3) shows that the triangular cap is nondecreasing, with unique minimum at \(u=0\). For \(3/4<s<\sqrt3/2\), the triangular cap decreases then increases, with its unique stationary minimum at

\[
u_\dagger=\sqrt{16s^2/3-3}=\frac{\sqrt{4W^2-9}}{\sqrt3}.
\]

This stationary point lies in the triangular regime: writing \(z=W^2\in(9/4,3)\), the required inequality is \(2z/3\ge1+\sqrt{4z-9}/\sqrt3\), which reduces, after squaring two nonnegative sides, to \(4(z-3)^2\ge0\). (The left side here is twice \(q\) at the stationary point, and the right side is \(1+u_\dagger\).) It follows that this point is the unique global cap minimizer. Substitution into (2) gives the last two branches of \(\Phi\) and their angles.

Each angular chamber has a unique minimizer; reflecting and rotating generates precisely the asserted dihedral orbit. Continuity at the three transition widths follows by direct substitution. This completes the proof.

## Verification

The included standalone `verify_hexagon.py` is runnable with Python 3 and its standard library. It constructs the six vertices independently, clips them by both plank halfplanes, computes area by the shoelace formula and compares that geometric area against the three cap formulas and the four claimed optimum formulas. With a fixed random seed it checks 1,205 positive widths (including every transition and both extreme regions) and 12,050 competitor directions. It passed these tests. The proof above, not these finite samples, establishes the statement for all real \(W\) in the specified open interval.

## Relationship to prior work

Bakaev and Polyanskii [1, Theorem 12] establish that a single plank suffices for every planar convex body and [1, Section 5] discuss certain simplices. Their theorem supplies the reduction to a single plank but does not specify the maximizing orientation or covered-area profile of a regular hexagon. The result here resolves that remaining geometry for the regular hexagon with two disjoint oblique phases. Computations for square and nonsquare rectangular sections concern different vertex-projection structures and do not imply (1) or its two internal angular bifurcations. Results on translative hull ratios and enclosing parallelograms of hexagons involve distinct optimization functionals and do not imply optimal area of a *strip intersection*. Ahn et al. [3] represent an affine-regular hexagon as an intersection of three containing strips in a minimum-area **enclosure** problem; their direction-rotation argument optimizes the enclosing hexagon, not the captured area of a width-constrained plank inside a fixed hexagon.

## Limitations

This is an exact theorem for the one-parameter regular hexagon, with circumradius normalized to one. It neither classifies maximizing single-plank orientations for arbitrary centrally symmetric hexagons nor characterizes all possibly tied multi-plank families. The finding has undergone a single nonindependent mathematical review; independent audit or verification has not been performed. A targeted literature search found no stronger covering formula, but an unindexed older polygon-strip calculation could overlap with the result.

## References

[1] E. Bakaev and A. Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483 (first public version July 29, 2026), in particular Theorem 12 and Section 5. https://arxiv.org/abs/2607.27483

[2] *Sharp translative convex-hull ratio for centrally symmetric hexagons*, public mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-translative-convex-hull-ratio-for-centrally-symmetric-hexa--ec2d6d717a26 (compared for object overlap only; its objective is different).

[3] H.-K. Ahn, S. W. Bae, O. Cheong, J. Gudmundsson, T. Tokuyama, and A. Vigneron, *A Generalization of the Convex Kakeya Problem*, arXiv:1209.2171v1 (2012), Section 5. https://arxiv.org/abs/1209.2171
