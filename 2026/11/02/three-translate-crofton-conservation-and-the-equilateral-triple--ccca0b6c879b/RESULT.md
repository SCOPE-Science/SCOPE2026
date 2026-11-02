# Three-translate Crofton conservation and the equilateral triple-transversal phase

## Finding

Let \(K\subset\mathbb R^2\) be a compact convex body with nonempty interior, and let \(p_1,p_2,p_3\in\mathbb R^2\) be three noncollinear translation vectors. Suppose the three translates \(K_i=K+p_i\) are **pairwise intersecting**; no common intersection of all three is required. For an unoriented affine line \(\ell\), let \(N(\ell)\in\{0,1,2,3\}\) count the labeled translates it meets. Write \(T=\operatorname{conv}\{p_1,p_2,p_3\}\) and \(P(B)\) for Euclidean perimeter.

With motion-invariant line measure \(d\mu=d\theta\,dt\), where \(\ell=\{x:x\cdot(\cos\theta,\sin\theta)=t\}\), \(0\le\theta<\pi\), the **three-translate conservation law** is
\[
\boxed{\mu(N=1)=\mu(N=2)=P(T),\qquad
       \mu(N=3)=P(K)-P(T).}
\]
Consequently, \(\mu(N\ge1)=P(K)+P(T)\), and, conditional on a line meeting at least one translate,
\[
\boxed{\Pr(N=1)=\Pr(N=2)=\frac{P(T)}{P(K)+P(T)},\qquad
\Pr(N=3)=\frac{P(K)-P(T)}{P(K)+P(T)}.}
\]
This is shape-independent in the first two incidence classes, including for non-centrally-symmetric convex bodies. More strongly, for **each fixed line normal**, the one-hit and two-hit sets of offsets have the same length, namely the width of the triangle of translations in that normal direction.

The same incidence question admits a **complete elementary phase law** even when the bodies are *not* pairwise intersecting, for three disks of common radius \(r>0\) with centers at the vertices of an equilateral triangle of side \(s>0\). Put \(q=2r/s\), \(h=\sqrt3/2\), and define
\[
 B(q)=\begin{cases}
 2\big(q\arcsin q+\sqrt{1-q^2}-1\big),&0<q\le1,\\
 \pi q-2,&q\ge1,
 \end{cases}
\]
\[
 H(q)=\begin{cases}
 0,&0<q\le h,\\
 6\big(q(\pi/6-\arccos q)+\sqrt{1-q^2}-1/2\big),&h<q\le1,\\
 \pi q-3,&q\ge1.
 \end{cases}
\]
Set \(D(q)=3\pi q-3B(q)+H(q)\). The complete line-incidence law, conditioned on meeting at least one disk, is
\[
\boxed{
\Pr(N=1)=\frac{3\pi q-6B(q)+3H(q)}{D(q)},\quad
\Pr(N=2)=\frac{3B(q)-3H(q)}{D(q)},\quad
\Pr(N=3)=\frac{H(q)}{D(q)}.}
\]
The triple-hit probability is zero for \(q\le h\), positive for \(q>h\), and obeys the **sharp quadratic onset**
\[
\boxed{
\Pr(N=3)=\frac{6}{3+\pi\sqrt3/2}\big(q-\sqrt3/2\big)^2
+O\big((q-\sqrt3/2)^3\big)
\quad(q\downarrow\sqrt3/2).}
\]
Thus it is continuously differentiable but not twice differentiable at the first triple-transversal threshold. For every \(q\ge1\), the law simplifies to
\[
\boxed{\Pr(N=1)=\Pr(N=2)=\frac3{\pi q+3},\qquad
\Pr(N=3)=\frac{\pi q-3}{\pi q+3}.}
\]
In unnormalized line measure, the one-hit and two-hit classes each have measure \(3s\), independent of radius in this overlapping regime. The existence threshold for an equilateral triple of disks is classical; the quantitative phase law and the conservation statements are the claims assessed here.

## Assumptions and scope

Each convex body is closed, compact, and has nonempty interior. Lines meeting a boundary tangentially are counted as meeting, but this convention changes neither the invariant line measures nor the probabilities. The three shifts in the general theorem are noncollinear, so \(T\) has ordinary polygonal perimeter. Pairwise intersections can be tangencies; there need not be a point common to all three bodies. All results use the motion-invariant measure \(d\theta\,dt\), not an unbounded uniform distribution over all affine lines. Probability statements condition on a line meeting the union and are therefore well-defined.

In the equilateral-disk corollary the disks need not be disjoint, and the formulas cover *every* \(q>0\). The regimes \(q<h\), \(h<q<1\), and \(q>1\) have different geometric behavior. At the endpoints the stated expressions agree by continuity.

## Proof

**1. Projection intervals and a pointwise conservation identity.** Fix \(u=(\cos\theta,\sin\theta)\). The offsets \(t\) for which the normal-\(u\) line meets \(K\) form a closed interval \([a(u),b(u)]\) of length \(w_K(u)=b(u)-a(u)\). For the three translates, the intervals are \([a(u)+p_i\cdot u,b(u)+p_i\cdot u]\).

Order \(x_i=p_i\cdot u\) so that \(x_1\le x_2\le x_3\), and let \(R=x_3-x_1\). Since each pair of translates intersects, their projected intervals intersect. In particular \(R\le w_K(u)\), and the three projected intervals have a common interval (one-dimensional Helly). Their occupancy, as \(t\) increases, is
\[
 1\text{ on }[a+x_1,a+x_2],\quad
 2\text{ on }[a+x_2,a+x_3],\quad
 3\text{ on }[a+x_3,b+x_1],
\]
\[
 2\text{ on }[b+x_1,b+x_2],\quad
 1\text{ on }[b+x_2,b+x_3],
\]
with intervals of zero length allowed. Thus the lengths of the sets of offsets meeting exactly one, two, and three translates are respectively
\[
 R,\qquad R,\qquad w_K(u)-R.
\]
By definition \(R=\max_i(p_i\cdot u)-\min_i(p_i\cdot u)=w_T(u)\), the support-width of the convex hull of the three centers. This proves the stronger fixed-direction claim.

**2. Invariant-line integration.** Cauchy's planar perimeter formula states for every compact convex body \(C\) that
\[
 \int_0^\pi w_C(\theta)\,d\theta=P(C).
\]
Integrating the three pointwise offset measures in \(\theta\) gives precisely the three asserted line measures. Their sum gives \(P(K)+P(T)\); division by this positive quantity gives the conditional probabilities. The proof requires no symmetry, differentiability, strict convexity, or triple physical intersection. In particular it proves the nontrivial necessary inequality \(P(T)\le P(K)\) under the pairwise-intersection assumption.

**3. Equilateral disks: inclusion–exclusion.** Let \(s=1\) temporarily; scale restores general \(s\) by multiplying invariant line measures by \(s\). For one disk, its projected interval has length \(q\) in every direction, so its line measure is \(\pi q\). For any fixed pair of disks, their centers are distance one apart, and the common projection-offset interval has length \((q-|\cos\theta|)_+\), up to a rotation of \(\theta\). Direct integration over \([0,\pi)\) yields \(B(q)\) as defined above.

For all three disks, their common projected interval has length \((q-w_T(\theta))_+\). By the six reflection sectors of the equilateral triangle, its width on a representative sector \(0\le\theta\le\pi/6\) is \(\cos(\pi/6-\theta)\), increasing from \(h\) to \(1\). Accordingly,
\[
 \int_0^\pi(q-w_T(\theta))_+\,d\theta
 =6\int_0^{\pi/6}(q-\cos(\pi/6-\theta))_+\,d\theta.
\]
For \(q\le h\) this vanishes. For \(h<q\le1\), only \(0<\theta<\pi/6-\arccos q\) contributes, and elementary integration gives the middle expression for \(H(q)\). For \(q\ge1\), every direction contributes and Cauchy's formula for the unit equilateral triangle gives \(H(q)=\pi q-3\).

Let \(m_j\) denote the measure of lines meeting exactly \(j\) disks, for \(j=1,2,3\). Summing all single-disk measures, all three pair-overlap measures, and the triple-overlap measure yields
\[
 m_1+2m_2+3m_3=3\pi q,\qquad
 m_2+3m_3=3B(q),\qquad
 m_3=H(q).
\]
Solving gives \(m_1=3\pi q-6B+3H\), \(m_2=3B-3H\), \(m_3=H\), and their total \(D(q)\). Dividing proves the piecewise probability formulas. At \(q\ge1\), \(B(q)=\pi q-2\) and \(H(q)=\pi q-3\) give \(m_1=m_2=3\), the special case of the general three-translate law. No probabilistic independence of the disk-hit events is assumed.

**4. Critical exponent and its coefficient.** For \(h<q<1\), write \(\delta=q-h\) and \(\alpha(q)=\pi/6-\arccos q\). The middle branch \(H(q)\) has derivatives
\[
 H'(q)=6\alpha(q),\qquad H''(q)=\frac6{\sqrt{1-q^2}}.
\]
Thus \(H(h)=H'(h)=0\), \(H''(h)=12\), and \(H(h+\delta)=6\delta^2+O(\delta^3)\). At the threshold,
\[
 B(h)=\frac{\pi\sqrt3}3-1,\qquad
 D(h)=3+\frac{\pi\sqrt3}2.
\]
Since \(D\) is continuously differentiable and positive there, the claimed conditional expansion follows. For \(q\le h\), \(H=0\) exactly, so the one-sided second derivative jumps from zero to \(12/D(h)>0\). The onset is a second-order transition, not simply an existence statement.

## Verification

The accompanying executable `checker.py` uses only the Python standard library. It independently enumerates line-offset occupancy intervals rather than using the proof's occupancy formulas. For three different planar shapes (an asymmetric triangle, a rectangle, and a 160-gon ellipse approximation), it checks the pointwise one/two/three identities at 9,000 directions and integrates all three classes against their Cauchy-perimeter values. It separately computes the disk-hit distribution from the actual three interval endpoints at 16,000 directions for each of eight size ratios spanning all three phases. On execution all checks pass, with the greatest integral discrepancy for the arbitrary-shape examples below \(6\times10^{-8}\) and all disk-formula discrepancies below \(4\times10^{-9}\) for these test cases. High-precision arithmetic independently confirms convergence of the normalized quadratic onset coefficient. These checks corroborate but do not replace the continuous-domain proof.

Run with `python3 checker.py` from this directory. No external packages are needed for the embedded verifier.

## Relationship to prior work

The classical theory of geometric line transversals asks when a line meeting several translates exists. Kaiser's 2002 paper establishes a Helly-type bound for disjoint unit disks (DOI 10.1007/s00454-002-2821-5), and Heppes' paper, publicly available online on 14 September 2010, studies critical separation factors and existence of common transversals for translates of convex ovals (DOI 10.1007/s00454-010-9292-x). Direct inspection of these texts did not find the present invariant-line *incidence measures* or a fixed-direction one-hit/two-hit equality. The classical equilateral three-circle tangency threshold is independently explained in the public exposition "Lines through Circles at Vertices of Equilateral Triangle" (Cut-the-Knot); its existence assertion is **not** claimed as new.

Cauchy's perimeter formula and the inclusion–exclusion identity are standard inputs. The proposed contribution is the combined shape-independent line-incidence conservation theorem for pairwise intersecting triples of convex translates and the complete equilateral-disk incidence phase distribution with its sharp quadratic activation constant. There is a residual historical-priority risk from specialized integral-geometric literature on multiple translated convex sets; negative searches do not prove universal novelty.

## Limitations

This concerns **unoriented planar affine lines** and translation families of *one* convex body, not independent rotated copies or nonconvex shapes. The pointwise equality need not hold for three arbitrarily shaped or unequal-width projection intervals. The arbitrary-triangle theorem requires pairwise intersection of the actual planar translates; the equilateral disk formulas extend beyond that assumption using a separate computation. There is no claim of a full classification of every non-equilateral disk arrangement or of other line-sampling conventions. Exact mathematical correctness rests on the interval calculation, elementary integration, and Cauchy's formula; no external independent audit has been performed, and historical priority remains subject to further bibliographic review.

## References

1. T. Kaiser, "Line Transversals to Unit Disks," *Discrete & Computational Geometry* **28** (2002), 379–387, DOI: 10.1007/s00454-002-2821-5. Full text: https://scispace.com/pdf/line-transversals-to-unit-disks-2din83moua.pdf.
2. A. Heppes, "Transversals in Superdisjoint \(T(3)\)-families of Translates," *Discrete & Computational Geometry* **45** (2011), 321–328; published online 14 September 2010, DOI: 10.1007/s00454-010-9292-x. Full text: https://link.springer.com/content/pdf/10.1007/s00454-010-9292-x.pdf.
3. "Lines through Circles at Vertices of Equilateral Triangle," Cut-the-Knot, https://www.cut-the-knot.org/m/Geometry/CirclesAtVertices.shtml (public exposition, precise initial publication day unverified).
4. Cauchy's classical perimeter formula for planar convex bodies (standard integral-geometric identity; no claim of new proof or priority).
