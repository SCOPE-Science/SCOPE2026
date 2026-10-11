# Exact M-curvature of the regular decagon
## Finding
Let \(P_{10}\subset\mathbb R^2\) be a regular decagon centered at the origin. For a centrally symmetric convex domain \(C\), Dalla, Larman, Mani-Levitska, and Zong define the M-curvature by
\[
m(C)=
\min_{\substack{x,y\in\partial C\\ \lVert x-y\rVert_C=1}}
\left(
1-\frac{d(0,L(x,y))}{d(0,T(x,y))}
\right),
\]
where \(L(x,y)\) is the line through \(x,y\), and \(T(x,y)\) is the parallel support line on the same side of the origin.

For the regular decagon,
\[
m(P_{10})
=
\frac{7-3\sqrt5}{2}
=
0.145898033750315\ldots.
\]
Equivalently,
\[
\max
\frac{d(0,L(x,y))}{d(0,T(x,y))}
=
\frac{3\sqrt5-5}{2}.
\]

Normalize the circumradius to \(1\) and put
\[
v_j=
\left(
\cos\frac{j\pi}{5},
\sin\frac{j\pi}{5}
\right).
\]
Every Minkowski-unit difference vector is dihedrally equivalent to
\[
d(t)=(1-t)v_0+t v_1,
\qquad
0\le t\le\frac12.
\]
Set
\[
\tau=\frac{3-\sqrt5}{2}.
\]
The maximal normalized height for the fixed difference vector \(d(t)\) is
\[
r(t)=
\begin{cases}
\displaystyle
\frac{3\sqrt5-5}{2}
+\frac{11-5\sqrt5}{2}t
+(\sqrt5-2)t^2,
&0\le t\le\tau,\\[8pt]
\displaystyle
1-\frac{\sqrt5-1}{2}t(1-t),
&\tau\le t\le\frac12.
\end{cases}
\]
The maximum is
\[
\frac{3\sqrt5-5}{2}
\]
and occurs exactly at
\[
t=0
\quad\text{and}\quad
t=\tau
\]
on the chosen half-edge, together with their images under the dihedral symmetries of the decagon.

## Assumptions and scope
The Minkowski norm \(\lVert\cdot\rVert_{P_{10}}\) has \(P_{10}\) as unit ball. Hence
\[
\lVert x-y\rVert_{P_{10}}=1
\]
is equivalent to the difference vector
\[
d=y-x
\]
lying on \(\partial P_{10}\).

The M-curvature is invariant under nonsingular linear transformations, so the Euclidean regular decagon of circumradius \(1\) is a sufficient representative of its affine class.

The result computes the invariant of the regular decagon exactly. It does **not** prove the global conjecture that the regular decagon maximizes M-curvature among all centrally symmetric planar convex domains.

## Proof
Let
\[
u_j=
\left(
\cos\left(\frac{\pi}{10}+\frac{j\pi}{5}\right),
\sin\left(\frac{\pi}{10}+\frac{j\pi}{5}\right)
\right),
\qquad
c=\cos\frac{\pi}{10}.
\]
Then
\[
P_{10}
=
\{z\in\mathbb R^2:u_j\cdot z\le c,\ 0\le j\le9\}.
\]

Fix
\[
d\in\partial P_{10}.
\]
A chord with difference vector \(d\) has starting point
\[
x\in Q_d:=P_{10}\cap(P_{10}-d).
\]
Let
\[
n=(-d_2,d_1).
\]
The distance ratio in the M-curvature definition is unchanged if the Euclidean normalization of \(n\) is omitted. Therefore the largest possible ratio for this fixed \(d\) is
\[
r(d)
=
\frac{\max_{x\in Q_d}n\cdot x}
{h_{P_{10}}(n)}.
\]
A maximizing \(x\) gives the outermost chord parallel to \(d\), so its endpoints lie on \(\partial P_{10}\). Thus maximizing \(r(d)\) over \(d\in\partial P_{10}\) is exactly the maximization required in the M-curvature definition.

By dihedral symmetry, it is enough to put
\[
d(t)=(1-t)v_0+t v_1,
\qquad
0\le t\le\frac12.
\]
For this interval the support denominator is
\[
h_{P_{10}}(n(t))=n(t)\cdot v_3.
\]

The linear program over
\[
Q_t=P_{10}\cap(P_{10}-d(t))
\]
has one active-constraint switch. Define
\[
\tau=\frac{3-\sqrt5}{2}.
\]

For
\[
0\le t\le\tau,
\]
the maximizing vertex is the intersection
\[
u_3\cdot x=c,
\qquad
u_1\cdot x=c-u_1\cdot d(t).
\]
The objective normal decomposes as a nonnegative combination
\[
n(t)=
\frac{(3-\sqrt5)t+\sqrt5-1}{2}\,u_3
+
\frac{(\sqrt5-1)(1-t)}{2}\,u_1.
\]
Hence this feasible intersection maximizes \(n(t)\cdot x\). Substitution in the remaining half-space inequalities shows feasibility throughout the stated interval. Solving the two active equations and dividing by \(n(t)\cdot v_3\) gives
\[
r_1(t)=
\frac{3\sqrt5-5}{2}
+\frac{11-5\sqrt5}{2}t
+(\sqrt5-2)t^2.
\]

For
\[
\tau\le t\le\frac12,
\]
the maximizing vertex is instead the intersection
\[
u_3\cdot x=c,
\qquad
u_2\cdot x=c-u_2\cdot d(t).
\]
Here the objective decomposition is especially simple:
\[
n(t)=t\,u_3+(1-t)\,u_2.
\]
Again all remaining half-space inequalities hold on the stated interval. Solving the active equations yields
\[
r_2(t)
=
1-\frac{\sqrt5-1}{2}t(1-t).
\]

Put
\[
r_0=\frac{3\sqrt5-5}{2}.
\]
On the first interval,
\[
r_1(0)=r_1(\tau)=r_0,
\]
and
\[
r_1''(t)=2(\sqrt5-2)>0.
\]
Hence the convex quadratic satisfies
\[
r_1(t)\le r_0
\]
with equality only at the two endpoints.

On the second interval,
\[
r_2(\tau)=r_0.
\]
Because
\[
t(1-t)
\]
is strictly increasing on
\[
[\tau,1/2],
\]
the function \(r_2\) is strictly decreasing there. Thus
\[
r_2(t)\le r_0
\]
with equality only at \(t=\tau\).

Consequently
\[
\max_{d\in\partial P_{10}}r(d)=r_0,
\]
and therefore
\[
m(P_{10})
=
1-r_0
=
\frac{7-3\sqrt5}{2}.
\]

## Verification
The supplied `verify.py` reconstructs the two active linear programs from the exact trigonometric half-space model of the regular decagon. It checks the active-normal decompositions, verifies all twenty half-space inequalities at both endpoints of each parameter interval, and uses their affine dependence on \(t\) to certify feasibility throughout each interval.

It then independently checks the two closed formulas for \(r(t)\) to high algebraic precision against the exact linear-system expressions and verifies the exact endpoint identities and monotonicity/convexity certificates.

No sampling is used to prove the continuum statement. The proof above reduces feasibility to affine inequalities on two compact intervals and reduces the final maximization to two explicit quadratic expressions.

## Relationship to prior work
The 2000 paper *The Blocking Numbers of Convex Bodies* introduced the M-curvature used here and posed the problem of determining its maximum over centrally symmetric convex domains. It explicitly conjectured that the regular decagon is the extremal figure.

A 2010 doctoral thesis on unrestricted blocking numbers revisited the same invariant. It reports that computer calculations identify the regular decagon as extremal among certain infinite families of regular even polygons, but the inspected discussion does not state an exact formula for \(m(P_{10})\), a piecewise height profile, or the two equality-direction families above.

Later blocking-number literature continues to use the Dalla--Larman--Mani-Levitska--Zong framework, but targeted searches for the exact algebraic value, M-curvature of a regular decagon, and the golden-ratio switch parameter did not locate a covering statement.

The present result is therefore a benchmark computation for the specific body singled out by the original conjecture; it does not claim to settle that conjecture.

## Limitations
The result is restricted to the regular decagon and its affine images.

It does not establish an upper bound for the M-curvature of arbitrary centrally symmetric convex domains.

The originality assessment retains a residual risk that the exact calculation appeared in an unindexed note or in unpublished computer work underlying the later thesis.

The primary 2000 article does not print an MSC line in the inspected copy. The classification \(52C17\) is used here because blocking-number work in the same research line is classified there and the problem is a packing-and-covering invariant in discrete geometry.

## References
1. L. Dalla, D. G. Larman, P. Mani-Levitska, and C. Zong, *The Blocking Numbers of Convex Bodies*, Discrete & Computational Geometry 24 (2000), 267--278. DOI: 10.1007/s004540010032. Online publication: 2000-05-03.
2. S. Sezgin, *The Unrestricted Blocking Number in Convex Geometry*, Ph.D. thesis, University College London, February 2010.
3. J. Wang and Y. Zhang, *On the blocking numbers of some special convex bodies*, Contributions to Discrete Mathematics 19 (2024), 209--221. DOI: 10.55016/ojs/cdm.v19i3.75983.
