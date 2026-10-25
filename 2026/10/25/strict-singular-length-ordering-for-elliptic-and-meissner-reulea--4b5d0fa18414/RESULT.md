# Strict singular-length ordering for elliptic and Meissner Reuleaux surgeries

## Finding

Fix a unit standard three-dimensional Reuleaux polyhedron \(R\). Its circular edges occur in finitely many dual pairs. For any pair having chord lengths \(0<a,b\le1\), write \(C_A,C_B\) for the lengths of the two original circular arcs, and \(E_A,E_B\) for the new elliptic arcs introduced by Mercado-Flores and Roldán-Pensado. Then

\[
\boxed{\max\{C_A,C_B\}<E_A+E_B<C_A+C_B.}
\]

The inequalities hold strictly for every such pair, without a symmetry or equal-chord hypothesis. Among the independent three-way surgery choices in Section 6.2 of [1], the one-dimensional Hausdorff measure of the nonsmooth boundary is uniquely **maximized** by performing the elliptic replacement in every dual pair. It is **minimized** by retaining an original circular edge of smaller arclength in each pair; exactly the local equal-length ties remain. The original (unmodified) Reuleaux edge skeleton has greater total arclength than the all-elliptic one, but it is not itself generally the boundary singular set of a constant-width body.

There is also a sharp degenerate-pair law. For fixed \(a\in(0,1]\),

\[
C_A-E_A=\kappa(a)b^2+O_a(b^4),\qquad
\kappa(a)=\frac{6-a^2}{4a^2}\arcsin\frac a2-\frac{3\sqrt{4-a^2}}{8a}>0.
\]

This law refers to the explicit local four-endpoint configuration even if its degeneration is not realized by a fixed global Reuleaux polyhedron.

## Assumptions and scope

A *unit standard Reuleaux polyhedron* means the finite intersection of closed Euclidean unit balls centered at exactly its vertices, with the standard incidence conditions of [1]. Each unordered dual-edge pair has four vertices \(A_{\pm},B_{\pm}\), with all four cross-distances one and \(a=|A_+-A_-|\), \(b=|B_+-B_-|\), where \(0<a,b\le1\). Its three allowed choices are to retain circular arc \(A\), to retain circular arc \(B\), or to retain both elliptic replacement arcs. Every choice gives a unit constant-width body [1, Section 6.2].

Define

\[
q=a^2+b^2,\quad c=\frac a{\sqrt q},\quad d=\frac b{\sqrt q},\quad
h=\sqrt{1-q/4},\quad t_0=\arcsin(\sqrt q/2).
\]

The replacement curves, in canonical orthogonal coordinates, are

\[
\gamma_A(t)=(c\sin t,0,c^2\cos t),\qquad
\gamma_B(t)=(0,d\sin t,-d^2\cos t),\quad |t|\le t_0.
\]

Thus their lengths, with the positive square root, are

\[
E_A=2c\int_0^{t_0}\sqrt{1-d^2\sin^2t}\,dt,\qquad
E_B=2d\int_0^{t_0}\sqrt{1-c^2\sin^2t}\,dt.
\]

The original arcs lie on circles of respective radii \(r_A=\sqrt{1-b^2/4}\) and \(r_B=\sqrt{1-a^2/4}\); their lengths are

\[
C_A=2r_A\arcsin\frac{a}{2r_A},\qquad
C_B=2r_B\arcsin\frac{b}{2r_B}.
\]

All lengths are ordinary Euclidean arclengths. The nonsmooth locus is the set of points of the boundary having more than one supporting plane. \(\mathcal H^1\) is one-dimensional Hausdorff measure. The extremum is restricted to mixed surgeries of *this fixed* \(R\); it makes no extremality claim among all bodies of constant width.

## Proof

**1. A strict local arclength comparison.** The source gives height graphs of the original circular and replacement elliptic arcs above \(-a/2\le x\le a/2\):

\[
Z_R(x)=-hd^2+\sqrt{r_A^2-x^2},\qquad
Z_E(x)=c\sqrt{c^2-x^2}.
\]

Their endpoint values agree. For \(0<x<a/2\), the positive magnitudes of the descending slopes are

\[
m_R(x)=\frac{x}{\sqrt{r_A^2-x^2}},\qquad
m_E(x)=\frac{cx}{\sqrt{c^2-x^2}}.
\]

Both denominators are strictly positive in the whole integration range. Squaring shows that \(m_R(x)>m_E(x)\) is equivalent to

\[
c^2(1-r_A^2)>x^2(1-c^2)
\quad\Longleftrightarrow\quad a^2/4>x^2.
\]

It is therefore strict throughout the interior. Since \(s\mapsto\sqrt{1+s^2}\) is strictly increasing for \(s>0\), integrating its two slope values proves \(0<E_A<C_A\). Interchanging \(a,b\) proves \(0<E_B<C_B\). Consequently \(E_A+E_B<C_A+C_B\).

**2. The opposite, two-to-one comparison.** The same length-integrand map is strictly 1-Lipschitz on \([0,\infty)\). Hence

\[
0<C_A-E_A<2\int_0^{a/2}(m_R-m_E)\,dx
=2\bigl(Z_R(0)-Z_E(0)\bigr).
\]

The last equality uses the common endpoint height. Direct algebra, with \(h=\sqrt{1-(a^2+b^2)/4}\), yields the **exact midpoint separation**

\[
Z_R(0)-Z_E(0)
=\frac{a^2b^2}{16(1+r_A)(r_A+h)(1+h)}.
\]

All three denominator factors exceed one; thus

\[
0<C_A-E_A
<\frac{a^2b^2}{8(1+r_A)(r_A+h)(1+h)}
<\frac{b}{8}.
\]

The curved elliptic arc \(\gamma_B\) is strictly longer than its straight chord \(b\), because its curvature is nonzero throughout an interior interval. Consequently \(E_B>b>C_A-E_A\), and so \(E_A+E_B>C_A\). By symmetry it also exceeds \(C_B\). This establishes the boxed strict local ordering and, more precisely, a useful explicit upper bound on individual circular-to-elliptic shortening.

**3. Exact total singular length.** For each dual pair the selected generating set consists of either one original circular arc or two elliptic arcs [1, Section 6.2]. The interiors of arcs belonging to distinct dual pairs lie in mutually disjoint surgery regions; any intersections at vertices are finite [1, Proposition 3.1 and Section 6.2]. In each retained circular arc, the dual pair's two distinct opposite vertices are both supporting centers at every relative-interior point, so all such points are nonsmooth. For every elliptic arc, every interior point other than its midpoint has two different opposite elliptic-arc supporting centers [1, Lemma 2.2 and Proposition 5.2]; the same supporting-center argument holds for a mixed pattern because distinct surgery regions are disjoint. Conversely, the mixed-boundary regularity theorem in [1, Section 6.2] says the boundary is smooth outside the selected generating set. Thus the nonsmooth locus and the selected arcs differ at most by finitely many points, which have zero \(\mathcal H^1\)-measure. Additivity over their disjoint interiors gives the asserted finite sum.

For every pair, both circular choices have length below the two-elliptic choice, strictly, so any non-elliptic choice decreases total nonsmooth length. Therefore the all-elliptic pattern alone gives the maximum. The minimum is obtained independently in each pair by the shorter circular arc; if the two original circular lengths coincide, either circular choice gives the same minimum. No numerical optimization or symmetry assumption enters these conclusions.

**4. Sharp quadratic degeneracy.** Hold \(a\in(0,1]\) fixed and let \(b\downarrow0\). For \(0\le x\le a/2\), the slope magnitudes can be rewritten

\[
m_R(x)=\frac{x}{\sqrt{1-b^2/4-x^2}},\qquad
m_E(x)=\frac{x}{\sqrt{1-(1+b^2/a^2)x^2}}.
\]

Their denominators are uniformly bounded away from zero near \(b=0\), because \(a\le1\). Differentiating the length integrands analytically with respect to \(b^2\), then integrating, gives

\[
\lim_{b\downarrow0}\frac{C_A-E_A}{b^2}
=\frac14\int_0^{a/2}
\frac{x^2(1-4x^2/a^2)}{(1-x^2)^{3/2}}\,dx
=\frac{6-a^2}{4a^2}\arcsin\frac a2-
\frac{3\sqrt{4-a^2}}{8a}.
\]

The integral is strictly positive since its integrand is positive for \(0<x<a/2\). Analyticity in \(b^2\) gives the \(O_a(b^4)\) remainder. This completes the proof.

## Verification

The independent symbolic expression for the midpoint separation was reduced to zero with exact symbolic arithmetic; `check.py` also compares circular and elliptic lengths for a grid of 1,600 positive chord pairs \((a,b)\), using numerical quadrature, and checks the quadratic coefficient along a geometric sequence tending to zero. The checker provides evidence for the calculations but cannot establish universal quantifiers, which rely on the analytic proof above.

For the regular Reuleaux tetrahedron \(a=b=1\) in all three dual pairs: all-elliptic nonsmooth length is approximately \(6.348573008355379\), while each Meissner surgery has nonsmooth length approximately \(3.198126379334406\). These values come from the displayed integrals and do not assert a global minimum across all unit-width bodies.

## Relationship to prior work

Mercado-Flores and Roldán-Pensado [1] introduce the general elliptic replacement, prove the nonsmooth locus is its elliptic skeleton apart from finitely many arc midpoints, and explicitly allow independent mixed Meissner–elliptic surgeries. Their Lemma 2.3 compares the **positions** of the curves, not the arclength order, and their results do not state the strict three-choice singular-length ranking, the global extremizers of that one-dimensional measure, or the quadratic short-edge coefficient. The tetrahedral elliptic geometry had already appeared in [2], and earlier Meissner bodies in [3]; our comparison treats the new mixed class on every unit standard Reuleaux polyhedron. Literature checks are not a proof of absolute historical novelty; equivalent unpublished or unindexed work remains possible.

## Limitations

The optimization is only among independently available surgeries for a fixed starting polyhedron; it makes no claims about surface area, volume, curvature energy, or global extremal constant-width bodies. The exact numerical tetrahedral example is illustrative, not a separate classification. In the degenerate limit one chord tends to zero, and the limit may cease to be an edge pair of a fixed nondegenerate standard polyhedron. The prior-work conclusion is subject to normal indexing and historical-coverage uncertainty. Independent mathematical validation is not performed.

## References

[1] M. G. Mercado-Flores and E. Roldán-Pensado, *A new family of constant width bodies obtained from Reuleaux polyhedra*, arXiv:2610.16997v1 (first submitted 2026-10-12), Sections 2–6. https://arxiv.org/html/2610.16997v1

[2] M. G. Mercado-Flores, M. Raggi, and E. Roldán-Pensado, *A four-dimensional body of constant width*, arXiv:2510.16672 (first submitted 2025-10-19), particularly Sections 1 and 5. https://arxiv.org/html/2510.16672

[3] L. Montejano and E. Roldán-Pensado, *Meissner polyhedra*, Acta Math. Hungar. 151 (2017), 482–494. The relevant surgery properties are also reproduced and attributed in [1, Sections 3 and 6].
