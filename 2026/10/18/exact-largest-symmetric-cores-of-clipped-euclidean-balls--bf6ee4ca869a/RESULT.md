# Exact largest symmetric cores of clipped Euclidean balls

## Finding
For every integer \(n\ge 2\) and every \(-1\le a<1\), define the closed convex body
\[
K_{n,a}=\{(x,y)\in\mathbb R\times\mathbb R^{n-1}:x^2+\|y\|_2^2\le1,\ x\ge a\}.
\]
Put
\[
q_n=2^{-2/(n-1)},\qquad a_n^*=-\sqrt{1-q_n},\qquad
s_n(a)=\begin{cases}
0,&-1\le a\le a_n^*,\\[2pt]
\displaystyle\frac{2a+\sqrt{q_na^2+(4-q_n)(1-q_n)}}{4-q_n},&a_n^*<a<1.
\end{cases}
\]
Among **all centrally symmetric convex subsets** of \(K_{n,a}\), without restrictions on their shapes, the unique maximum-volume subset is
\[
C_{n,a}=K_{n,a}\cap\bigl(2s_n(a)e_1-K_{n,a}\bigr).
\]
Its unique center of symmetry is \(s_n(a)e_1\). With \(\kappa_j\) denoting the volume of the unit \(j\)-ball, its sharp volume and volume fraction are
\[
\boxed{V_n(a)=2\kappa_{n-1}\int_{s_n(a)}^{2s_n(a)-a}
(1-t^2)^{(n-1)/2}\,dt},
\]
\[
\boxed{\beta_n(a)=\frac{2\int_{s_n(a)}^{2s_n(a)-a}(1-t^2)^{(n-1)/2}\,dt}
{\int_a^1(1-t^2)^{(n-1)/2}\,dt}}.
\]
These integrals are ordinary proper integrals on subintervals of \([0,1]\). The optimizer has a sharp **center-locking transition**: for cuts \(a\le a_n^*\) its center remains at the original ball center, and for cuts \(a>a_n^*\) it moves strictly into the retained cap.

For a three-dimensional hemisphere, \(\beta_3(0)=2/\sqrt7\), and the maximizing center has height \(1/\sqrt7\). In every fixed dimension, the thin-cap asymptotic is
\[
\boxed{\lim_{a\uparrow1}\beta_n(a)=(2-q_n)^{-(n-1)/2}}.
\]
For \(n=3\), this limit is \(2/3\). The limiting constants converge to \(1/2\) as \(n\to\infty\).

## Assumptions and scope
The dimension is an integer \(n\ge2\), the cut parameter satisfies \(-1\le a<1\), and all volumes are Euclidean Lebesgue volumes. A centrally symmetric convex subset must be compact and have nonempty interior for positive volume. One may equivalently optimize over all measurable centrally symmetric subsets: at any prescribed center, the reflected intersection contains every such subset.

At \(a=-1\) the body is the whole unit ball and the optimizer is the ball itself. The degenerate endpoint \(a=1\) is excluded because the containing set has zero \(n\)-volume and cannot have a unique maximum-volume full-dimensional subset. No claim is made for general non-Euclidean norms or for intersections with multiple nonparallel halfspaces.

## Proof
**Reduction to reflected intersections.** Fix a center \(c\in K_{n,a}\). Every centrally symmetric set \(S\subseteq K_{n,a}\) with center \(c\) obeys \(S=2c-S\subseteq 2c-K_{n,a}\). Thus it is contained in the centrally symmetric convex set \(M(c)=K_{n,a}\cap(2c-K_{n,a})\). Maximizing \(\operatorname{vol}_n(M(c))\) over \(c\in K_{n,a}\) is exactly the unrestricted problem.

**No transverse displacement.** Write \(c=(s,z)\), with \(z\in\mathbb R^{n-1}\). At a fixed first coordinate \(x\), a section of \(M(c)\) is the intersection of two \((n-1)\)-balls centered at \(0\) and \(2z\), with respective radii
\[
R_1(x)=\sqrt{1-x^2},\qquad R_2(x)=\sqrt{1-(2s-x)^2},
\]
whenever both \(x\) and \(2s-x\) lie in \([a,1]\). The intersection volume is bounded above by \(\kappa_{n-1}\min(R_1,R_2)^{n-1}\), exactly the corresponding section of \(M((s,0))\). If \(z\ne0\) and \(M(c)\) has positive volume, the inequality is strict on a positive-measure neighborhood of \(x=s\): there the radii are positive and equal at the center, while two translated equal-radius balls have a strictly smaller intersection than a single ball. Hence every positive-volume maximizer has \(z=0\).

**Axial section formula.** Write \(c=se_1\), with \(a\le s\le1\), and set \(f_n(t)=(1-t^2)^{(n-1)/2}\) for \(0\le t\le1\). The allowed first coordinates are symmetric about \(s\), at distances \(u\) with
\[
0\le u\le w(s):=\min\{s-a,1-|s|\}.
\]
Both Euclidean-ball conditions together give a transverse radius \(\sqrt{1-(|s|+u)^2}\). Therefore
\[
\operatorname{vol}_n(M(se_1))
=2\kappa_{n-1}\int_0^{w(s)} f_n(|s|+u)\,du.
\tag{1}
\]
For negative \(s\), necessarily \(a<0\); then \(w(s)<-a\), and strict decrease of \(f_n\) away from zero shows that (1) is strictly smaller than its value at \(s=0\). Thus no negative center is optimal.

**Unique axial optimum.** Put \(b=(1+a)/2\) and restrict to \(s\in[\max\{0,a\},1]\). For \(s\le b\), equation (1) becomes
\[
F(s)=2\kappa_{n-1}\int_s^{2s-a} f_n(t)\,dt,
\qquad F'(s)=2\kappa_{n-1}\bigl(2f_n(2s-a)-f_n(s)\bigr).
\tag{2}
\]
For \(b\le s\le1\), it instead becomes \(F(s)=2\kappa_{n-1}\int_s^1 f_n(t)\,dt\), strictly decreasing on \([b,1)\).

On the first interval, \(2s-a\ge s\ge0\); the ratio \(f_n(2s-a)/f_n(s)\) is strictly decreasing in its interior because \(t\mapsto t/(1-t^2)\) strictly increases for \(0\le t<1\). More explicitly, its logarithmic derivative is
\[
(n-1)\left(\frac{s}{1-s^2}-\frac{2(2s-a)}{1-(2s-a)^2}\right)<0.
\]
At \(s=b\), the ratio is zero. If \(a\ge0\), its left-endpoint value (at \(s=a\)) is one; if \(a<0\), its value at \(s=0\) is \((1-a^2)^{(n-1)/2}\). It follows that the maximum is \(s=0\) precisely when \(a\le-\sqrt{1-q_n}\); otherwise the unique maximizer satisfies
\[
2f_n(2s-a)=f_n(s)
\quad\Longleftrightarrow\quad
(4-q_n)s^2-4as+a^2+q_n-1=0.
\]
The positive root is exactly \(s_n(a)\), and it belongs to the first interval strictly before \(b\). This proves uniqueness and the volume formula. Dividing by \(\operatorname{vol}_n(K_{n,a})=\kappa_{n-1}\int_a^1 f_n(t)\,dt\) gives \(\beta_n(a)\).

**Specialization and limiting ratio.** For \(n=3\), \(q_3=1/2\) and \(s_3(0)=1/\sqrt7\). Integrating \(f_3(t)=1-t^2\) gives \(V_3(0)=4\pi/(3\sqrt7)\), against hemisphere volume \(2\pi/3\), hence \(\beta_3(0)=2/\sqrt7\). For \(a=1-h\uparrow1\), the quadratic optimality equation yields
\[
s_n(1-h)=1-\frac{h}{2-q_n}+O(h^2),\qquad
2s_n(1-h)-(1-h)=1-\frac{q_nh}{2-q_n}+O(h^2).
\]
Using \(f_n(1-u)\sim(2u)^{(n-1)/2}\) in the two volume integrals gives \(\beta_n(a)\to2(1-q_n^{(n+1)/2})/(2-q_n)^{(n+1)/2}=(2-q_n)^{-(n-1)/2}\), since \(q_n^{(n-1)/2}=1/2\). Finally \((n-1)(1-q_n)\to2\log2\), so the thin-cap constant tends to \(1/2\) with dimension.

## Verification
The proof is analytic and covers all real \(-1\le a<1\) and all integer dimensions \(n\ge2\); no finite experiment is used to infer this continuum. The standalone standard-library program `verify.py` checks the quadratic identity, tests the predicted center against dense finite axial grids in multiple dimensions, and integrates planar off-axis sections for random centers. Running `python3 verify.py` prints `VERIFY_OK`. It provides numerical corroboration only. The special hemisphere identity and thin-cap limit are derived algebraically above.

## Relationship to prior work
The classical Kovner–Besicovitch volume measure asks for the largest centrally symmetric subset of a convex body. The reflected intersection \(M(c)\) is also called its Macbeath region at \(c\). These foundations are not new. Khovanova (2012) discusses this measure and the classical planar triangle bound. Meyer, Schütt, and Werner (2011) study a different family of affine-covariant symmetry measures, and Taschuk (2015) compares a harmonic-mean measure with other measures.

A published exact Kovner–Besicovitch computation for regular Reuleaux odd-gons reduces a dihedrally symmetric intersection of many disks to the body's central reflection, not a one-sidedly truncated Euclidean ball with a moving optimal center. A published sharp theorem for aligned parallel planks optimizes the volume of slabs intersected with a ball, not the volume of a ball intersected with its translated point reflection. Neither supplies the nonlinear center-shift condition or the threshold above.

## Limitations
The priority comparison is based on relevant accessible primary texts, targeted scientific searches, and published comparable exact results; it is not a proof of worldwide historical novelty. A full text of the 2015 harmonic-mean paper was not available for detailed inspection. Older unindexed computations of Macbeath regions or planar circular segments may contain special cases. The independent scientific audit has not yet occurred. The optimizer is characterized only for a single halfspace cut of a Euclidean ball.

## References
1. M. Meyer, C. Schütt, E. M. Werner, *New affine measures of symmetry for convex bodies*, Advances in Mathematics 228 (2011), 2920–2942, DOI: 10.1016/j.aim.2011.08.002. Author manuscript: https://case.edu/artsci/math/werner/publications/MSW-revision07-22-11.pdf.
2. T. Khovanova, *A Measure of Central Symmetry*, 2 September 2012, https://blog.tanyakhovanova.com/2012/09/a-measure-of-central-symmetry/.
3. S. Taschuk, *The harmonic mean measure of symmetry for convex bodies*, Advances in Geometry 15 (2015), 109–120, DOI: 10.1515/advgeom-2014-0021.
4. *Exact Kovner–Besicovitch area ratio of regular Reuleaux odd-gons*, published geometric result, identifier `71273748c58f`, consulted for implication comparison.
5. *Sharp ball-volume profile for every parallel plank family*, published geometric result, identifier `5a5385d2bdaf`, consulted for implication comparison.
