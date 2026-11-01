# An exact two-cap width law and quadratic transition for the regular 24-cell

## Finding
Let \(C\subset\mathbb R^4\) be the regular 24-cell with vertex set
\[
V=\{\pm e_i:1\le i\le4\}\cup
\left\{\tfrac12(\varepsilon_1,\ldots,\varepsilon_4):\varepsilon_i\in\{-1,1\}\right\}.
\]
For a Haar-uniform direction \(U\in S^3\), let \(W=h_C(U)+h_C(-U)\) be the length of its orthogonal projection onto the line \(\mathbb R U\). Put
\[
s_* = \sqrt{2/3},\qquad s_0=\sqrt3/2,\qquad
P(s)=\pi^{-1}\bigl(\arccos s-s\sqrt{1-s^2}\bigr),
\]
and for \(s_*\le s\le s_0\) define
\[
y(s)=\frac{\sqrt3}{2}\sqrt{1-s^2}-\frac{s}{2},\qquad
Q(s)=\pi^{-1}\left(\arcsin y(s)-\frac{2s}{\sqrt3}y(s)\right).
\]
Set \(Q(s)=0\) when \(s_0<s\le1\). Then the **exact upper distribution** is
\[
\boxed{\Pr\{W\ge2s\}=24P(s)-96Q(s),\quad s_*\le s\le1.}
\]
Thus a one-cap formula is exact for \(\sqrt3\le w\le2\):
\[
\Pr\{W\ge w\}=\frac{24}{\pi}
\left(\arccos\frac w2-\frac w2\sqrt{1-\frac{w^2}{4}}\right).
\]
At the sharp first overlap threshold \(w_0=\sqrt3\), the difference between the true survival probability and the continuation of this one-cap expression has the **quadratic onset**
\[
\boxed{\Pr\{W\ge w\}-24P(w/2)
=-\frac{96}{\pi\sqrt3}(\sqrt3-w)^2
+O\bigl((\sqrt3-w)^3\bigr),\quad w\uparrow\sqrt3.}
\]
In particular, the survival function is continuously differentiable but not twice continuously differentiable at \(w_0\); the nonzero coefficient counts the 96 edges of the 24-cell. The exact formula covers a fraction
\[
24P(\sqrt{2/3})-96Q(\sqrt{2/3})
\approx0.936356818452
\]
of all Haar directions (the fraction with \(W\ge2\sqrt{2/3}\)).

## Assumptions and scope
All coordinates and widths are Euclidean. The listed vertices have norm one, and the 24-cell is centrally symmetric about the origin, so
\[
W=2\max_{v\in V}\langle U,v\rangle
=2\max\left(\lVert U\rVert_\infty,\frac12\sum_{i=1}^{4}|U_i|\right).
\]
The probability distribution on \(S^3\) is normalized rotation-invariant area measure, not uniform measure on a discrete set or on the cube. All thresholds are inclusive. The result determines exactly the upper part \(W\ge2\sqrt{2/3}\), not the whole lower tail of the width distribution. No equivalent assertion is made about three-dimensional hyperplane projections (brightness).

## Proof
**1. Exact cap incidence.** For \(s\in[0,1]\), let \(A_v(s)=\{u\in S^3:\langle u,v\rangle\ge s\}\). The width event is the union of these 24 spherical caps. Distinct 24-cell vertices have inner product in \(\{-1,-1/2,0,1/2\}\). Exactly 96 unordered pairs have inner product \(1/2\), each vertex being incident to eight of these pairs. One can check this directly: the 8 axis vertices contribute 64 positive pairs with the 16 half-sign vertices, and the half-sign vertices contribute 32 positive pairs among themselves (Hamming distance one). Every other distinct pair has inner product at most zero.

If \(u\in A_v(s)\cap A_z(s)\), then \(2s\le\langle u,v+z\rangle\le\|v+z\|_2=\sqrt{2+2\langle v,z\rangle}\). Thus for \(s\ge s_*=\sqrt{2/3}>1/\sqrt2\), intersecting caps must correspond to those 96 pairs of inner product \(1/2\). If three caps intersect, their three pairs must all be of that type, and
\[
3s\le\left\|v_1+v_2+v_3\right\|_2=\sqrt6,
\]
so \(s\le\sqrt{2/3}\). At equality there is at most one common direction per triple, hence zero spherical measure; for larger \(s\) the triple intersection is empty. This proves exact inclusion--exclusion with only single- and double-cap terms throughout \(s_*\le s\le1\), including the lower endpoint in measure:
\[
\Pr\{W\ge2s\}=24\,\sigma(A_v(s))-96\,\sigma(A_v(s)\cap A_z(s)),
\quad \langle v,z\rangle=1/2.
\]

**2. One-cap probability.** For Haar-uniform \(U\in S^3\) and fixed unit \(v\), the coordinate \(\langle U,v\rangle\) has density \(2\sqrt{1-t^2}/\pi\) on \((-1,1)\). Integrating this density from \(s\) to one gives
\[
\sigma(A_v(s))=\frac2\pi\int_s^1\sqrt{1-t^2}\,dt
=\frac1\pi\left(\arccos s-s\sqrt{1-s^2}\right)=P(s).
\]

**3. An exactly integrable two-cap section.** Suppose \(v\cdot z=1/2\). Let
\[
m=(v+z)/\sqrt3,\quad n=v-z.
\]
These are orthonormal vectors, and
\(v=(\sqrt3/2)m+n/2\), \(z=(\sqrt3/2)m-n/2\).
For Haar \(U\in S^3\), the pair \((X,Y)=(\langle U,m\rangle,\langle U,n\rangle)\) is uniform in the Euclidean unit disk: its density is \(1/\pi\). Consequently the two-cap event is
\[
\frac{\sqrt3}{2}X-\frac12|Y|\ge s,
\qquad X^2+Y^2\le1.
\]
For \(0\le s\le s_0\), the positive upper intersection with the unit circle occurs at
\[
y(s)=\frac{\sqrt3\sqrt{1-s^2}-s}{2}\ge0,
\]
by solving \(\sqrt{1-y^2}=\frac2{\sqrt3}(s+y/2)\). The disk area is therefore
\[
\begin{aligned}
\sigma(A_v(s)\cap A_z(s))
&=\frac2\pi\int_0^{y(s)}\left(\sqrt{1-t^2}-\frac{2s+t}{\sqrt3}\right)dt\\
&=\frac1\pi\left(\arcsin y(s)-\frac{2s}{\sqrt3}y(s)\right)=Q(s).
\end{aligned}
\]
For \(s\ge s_0\), the caps have zero-measure intersection: their centers are separated by angle \(\pi/3\), so their cap radii are at most \(\pi/6\). Substitution into the exact cap inclusion--exclusion proves the claimed probability formula.

**4. First overlap singularity.** Write \(s=s_0-\delta\) with \(\delta\downarrow0\). Direct Taylor expansion of the elementary expressions gives
\[
y(s_0-\delta)=2\delta+O(\delta^2),
\qquad Q(s_0-\delta)=\frac4{\pi\sqrt3}\delta^2+O(\delta^3).
\]
These expansions follow also by rescaling \(t=\delta x\) in the disk integral: the integrand becomes \((2-x)\delta/\sqrt3+O(\delta^2)\) uniformly for \(0\le x\le2+O(\delta)\). Multiplying \(Q\) by 96 and substituting \(\delta=(\sqrt3-w)/2\) gives the stated coefficient. Since \(P\) is smooth at \(s_0\), while \(Q\) is zero above \(s_0\) and has this nonzero left quadratic term, the true survival law is \(C^1\) but not \(C^2\) across \(w_0\). The first overlap threshold is sharp because the 96 adjacent cap pairs acquire positive area immediately below \(s_0\).

## Verification
The accompanying standalone `verify.py` reconstructs all 24 vertices with exact rational coordinates; enumerates the 276 vertex pairs, their four Gram values and the 96 adjacent pairs; checks all 2,024 vertex triples against the positive-incidence condition; independently integrates the two-cap disk segment by Simpson quadrature; checks the first-onset coefficient; and compares the formula at nine thresholds against a fixed-seed 180,000-direction Haar simulation of the 24-vertex support maximum. Running `python3 verify.py` prints `VERIFY_OK` and the calculated upper-regime probability. Finite enumeration certifies this *particular* vertex Gram profile; the full continuous distribution follows instead from the analytic sphere/disk integration and inclusion--exclusion proof.

## Relationship to prior work
Novaga and Song's 2026 four-dimensional parallelohedron theorem makes the regular 24-cell a current canonical convex-geometric object; their Lemma 2.3 fixes the 24-vertex Euclidean realization. Their result optimizes the four-dimensional surface-area quotient, not the random directional width distribution. Abas's 2026 random-width and brightness theory gives exact densities for three-dimensional polytopes (including a regular tetrahedron and truncated octahedron), rather than this four-dimensional 24-cell law. A previous geometric note on the 24-cell's projection brightness computes the extrema of its **three-dimensional hyperplane-shadow volume**; neither those extrema nor the associated normal-facet formula imply the present **one-dimensional line-projection length** law. Previously established cubical spherical-cap formulas concern the cube's vertices and have different Gram incidences. The two-cap integral uses standard Haar-spherical marginal densities and elementary planar integration, not an unclaimed new method. The new feature is the exact 24-vertex/96-edge cap-incidence integration, its sharp overlap range, and the quadratic singularity coefficient.

## Limitations
The lower \(6.36\%\) of the width distribution is not classified. No assertion is made for arbitrary four-polytopes, affine deformations, other dimensions or orientation distributions. No corresponding full mean/variance law is proved. Existing general normal-fan/spherical-cap tools may yield equivalent expressions for this special case when specialized, and older unindexed results remain an originality risk. Abas's full 2026 manuscript could not be obtained from the accessible public endpoints; its available abstract specifies a three-dimensional forward density theory. The finite simulation is a diagnostic, not proof of a continuum statement. Independent external scientific validation has not been performed.

## References
1. M. Novaga and L. Song, *The isoperimetric problem for four-dimensional parallelohedra*, arXiv:2610.01653v1, first posted October 1, 2026; Lemma 2.3 and Theorem 1.1. https://arxiv.org/html/2610.01653v1
2. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1, first posted August 10, 2026 (abstract available; full text not inspected). https://arxiv.org/abs/2609.26202
3. *The regular 24-cell has exactly 24 least-bright and 192 most-bright projection directions*, online mathematical note, October 2026. Its invariant is three-dimensional brightness, not the directional width considered here.
4. *Exact directional width law of the cube and its first spherical-cap transition*, online mathematical note, October 2026. Its vertex-incidence structure is the hypercube's, not that of the 24-cell.
