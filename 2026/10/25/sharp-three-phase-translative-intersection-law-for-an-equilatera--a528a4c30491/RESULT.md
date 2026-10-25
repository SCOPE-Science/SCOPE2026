# Sharp three-phase translative intersection law for an equilateral triangle and a square

## Finding
Let \(T=\operatorname{conv}\{(1,0),(-1/2,\sqrt3/2),(-1/2,-\sqrt3/2)\}\) and \(Q_r=\{(x,y):|x|+|y|\le r\}\) for every \(r>0\). The relative orientations of this regular triangle and diamond-oriented square are fixed; their relative translations are arbitrary. Define
\[
M(r)=\max_{(t,u)\in\mathbb R^2}\operatorname{area}(T\cap(Q_r+(t,u))),\quad
r_- =\frac{3(\sqrt3-1)}4,\quad r_+=\frac{3+\sqrt3}4.
\]
Then the **complete sharp translative intersection profile** is
\[
M(r)=\begin{cases}2r^2,&0<r\le r_-,\\[2pt]
\frac{3\sqrt3}{4}-\sqrt3(r_+-r)^2,&r_-<r<r_+,\\[2pt]
\frac{3\sqrt3}{4},&r\ge r_+.
\end{cases}
\]
For \(r_-<r<r_+\), the **unique** optimal translation is \((t_*(r),0)\), with
\[t_*(r)=\frac{1+2r(1-\sqrt3)}4.\]
In the small-size regime exactly the translations placing the square entirely inside the triangle are optimal; in the large-size regime exactly the translations placing the triangle entirely inside the square are optimal. These two scale thresholds are sharp.

In particular, for equally sized circumradii \(r=1\), aligning the centroids is **strictly suboptimal**:
\[
\operatorname{area}(T\cap Q_1)=2\sqrt3-\frac94,
\qquad M(1)=\frac38+\frac{\sqrt3}{2},
\qquad \frac{\operatorname{area}(T\cap Q_1)}{M(1)}
=\frac{82-40\sqrt3}{13}<1.
\]
The gain in area from the optimal noncentral translation is exactly \(21/8-3\sqrt3/2>0\).

## Assumptions and scope
The triangle and square have fixed vertex directions in the Euclidean plane. The triangle circumradius is one, the square circumradius is \(r>0\), and there is **no optimization over rotations**. Intersection area is ordinary Euclidean planar area; its maximum is attained because the overlap vanishes outside a compact translation set. Equality cases in the two plateau regimes refer to positive-area full containment; boundary contact is allowed.

## Proof
For a horizontal coordinate \(x\), the triangle's vertical section (when \(-1/2\le x\le1\)) is the symmetric interval with half-width \(A(x)=(1-x)/\sqrt3\). The translated square has, for \(|x-t|\le r\), the vertical interval centered at \(u\) with half-width \(B(x)=r-|x-t|\). For two symmetric intervals, their intersection length cannot increase when one is displaced vertically. Integrating each horizontal section proves
\[
\operatorname{area}(T\cap(Q_r+(t,u)))\le I_r(t):=\operatorname{area}(T\cap(Q_r+(t,0))).
\]

The square can fit entirely inside the triangle if and only if \(r\le r_-\). Indeed, by the vertical centering inequality such a placement can be chosen with \(u=0\); the four diamond vertices require
\[
t-r\ge-\frac12,\qquad t+r\le1,\qquad r\le\frac{1-t}{\sqrt3}.\]
These inequalities have a solution exactly when \(r\le3(\sqrt3-1)/4\); one solution is \(t=\max\{0,r-1/2\}\). Hence \(M(r)=\operatorname{area}(Q_r)=2r^2\) in the first phase.

Conversely the triangle fits into a translated diamond exactly when \(r\ge r_+\). After vertical centering, the vertex constraints are \(r\ge |1-t|\) and \(r\ge |-1/2-t|+\sqrt3/2\). Their optimal balance occurs at \(t=(1-\sqrt3)/4\), giving the sharp threshold \(r_+=(3+\sqrt3)/4\). Thus the last phase equals the whole triangle area \(3\sqrt3/4\).

It remains to prove the middle phase. Set \(s=\sqrt3\) and \(t_*(r)=[1+2r(1-s)]/4\). For every \(r_-<r<r_+\), elementary substitutions yield the strict ordering
\[
 t_*-r<-\frac12<x_L<t_*<x_R<t_*+r<1,
\]
where
\[
 x_L=\frac{1-s(r-t_*)}{1+s},\qquad
 x_R=\frac{s(r+t_*)-1}{s-1}.
\]
For \(t\) sufficiently close to \(t_*\) the same ordering persists. The smaller half-width switches from the diamond's left flank to the triangle, then to the diamond's right flank. Consequently
\[
I_r(t)=2\left[\int_{-1/2}^{x_L(t)}(r-t+x)\,dx+
\int_{x_L(t)}^{x_R(t)}\frac{1-x}{s}\,dx+
\int_{x_R(t)}^{t+r}(r+t-x)\,dx\right],
\]
with \(x_L(t)=[1-s(r-t)]/(1+s)\) and \(x_R(t)=[s(r+t)-1]/(s-1)\). Direct antiderivatives give the **exact local identity**
\[
I_r(t)=\frac{3s}{4}-s(r_+-r)^2-2(t-t_*(r))^2.
\]
In particular \(t_*\) is a strict local maximum and its value is the claimed middle formula. To prove global optimality, let \(K_t=T\cap(Q_r+(t,0))\). Convexity gives \((1-\lambda)K_{t_1}+\lambda K_{t_2}\subseteq K_{(1-\lambda)t_1+\lambda t_2}\). The planar Brunn--Minkowski inequality therefore makes \(\sqrt{I_r(t)}\) concave wherever the intersection has positive area. An interior stationary point of this concave function is a global maximum. A second maximum would force an interval of maximizers, contradicting the displayed strict local quadratic. Thus \(t_*\) is the unique maximizing horizontal shift.

At the two crossing points \(x_L,x_R\), both section half-widths agree and are positive; on a small neighboring interval the vertical overlap is strictly reduced by any nonzero vertical displacement \(u\). Consequently the unique middle-phase maximizing planar translation has \(u=0\).

Finally, direct section integration at \(r=1,t=0,u=0\) yields \(2\sqrt3-9/4\), whereas the middle formula gives \(3/8+\sqrt3/2\). Subtraction and rationalization establish the stated strict centroid-alignment gap and ratio.

## Verification
The accompanying standalone `verify_overlap.py` computes all intersection areas independently by Sutherland--Hodgman half-plane clipping of the seven input polygon edges, rather than by the half-width antiderivative used above. It checks eleven radii across all three phases (including both thresholds), 1,980 random planar translations, sixteen strict-local quadratic predictions, and the exact center-alignment comparison. Executed result: `TRIANGLE_DIAMOND_PROFILE_OK radii=11 translations=1980 strict_local=16`. The calculations corroborate, but do not replace, the proof for all real radii.

## Relationship to prior work
Feldman's 2026 centroid-alignment theorem gives a universal sharp efficiency bound for intersections of translated convex bodies; it does not give the present fixed-orientation triangle--square phase diagram or its unique intermediate translation. The earlier geometric optimization literature, including de Berg et al. (1998) and Chan--Hair (2025), establishes exact algorithms for finding maximum overlap of arbitrary convex polygons, not this explicit continuous-parameter law. Brunn--Minkowski concavity of overlap is a known tool, and is used here without claiming it as new. The contribution is the exact three-phase closed form, both sharp transitions, the unique partial-overlap optimizer, and the quantified failure of centroid alignment for this elementary pair.

## Limitations
No claim is made about rotating the square, general triangles or squares, universal optimal centroid efficiency, or the novelty of the general overlap-optimization algorithm. Historical equivalence in older specialized intersection literature is a residual priority risk. Independent scientific validation has not been performed.

## References
1. David Victor Feldman, *Arranging convex bodies for maximum intersection volume: the sharp efficiency of centroid alignment*, arXiv:2608.04516, first public 2026-08-05, https://arxiv.org/abs/2608.04516.
2. Timothy M. Chan and Isaac M. Hair, *A Linear Time Algorithm for the Maximum Overlap of Two Convex Polygons Under Translation*, SoCG 2025, DOI:10.4230/LIPIcs.SoCG.2025.31; https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.31.
3. Mark de Berg, Otfried Cheong, Olivier Devillers, Marc J. van Kreveld, and Monique Teillaud, *Computing the maximum overlap of two convex polygons under translations*, Theory Comput. Syst. **31** (1998), 613--628, DOI:10.1007/PL00005845.
