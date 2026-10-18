# Exact chord-quadrilateral enclosure of the regular heptagon

## Finding

Let \(P_7\) be a Euclidean regular heptagon of circumradius one. A *chord quadrilateral* is a convex polygon with at most four sides containing \(P_7\), every side being parallel to a segment between two vertices of \(P_7\). Let \(q_{\mathrm{ch}}(P_7)\) denote the least area of such a polygon. Put \(c=\cos(\pi/7)\). Then
\[
q_{\mathrm{ch}}(P_7)
=c^2\left(\tan\frac\pi7+3\tan\frac{2\pi}7\right),
\qquad
\frac{q_{\mathrm{ch}}(P_7)}{|P_7|}
=\frac{1+3\tan(2\pi/7)/\tan(\pi/7)}7
=1.258803773547\ldots.
\]
Exactly seven minimizing quadrilaterals exist. Each is bounded by four supporting *edge* lines of the heptagon; their four cyclic gaps between chosen edge-normal directions, measured in units of \(2\pi/7\), are a permutation under cyclic order of \((1,2,2,2)\). They form one orbit under the dihedral symmetry group. The formula, ratio, and optimizer classification transfer under every invertible affine map of the heptagon.

For circumradius one, among all *support-saturated* four-direction chord enclosures other than these seven, the area exceeds the minimum by more than \(1/40\). This last discrete separation is not a stability bound against arbitrary small perturbations of non-supporting lines.

## Assumptions and scope

The heptagon is the convex hull of the seven points \((\cos(2\pi j/7),\sin(2\pi j/7))\) for integers \(0\le j<7\). A side of an enclosure may be parallel to any heptagon edge or diagonal, with outward normal chosen accordingly. The enclosed body has nonempty interior, and all areas use the Euclidean Lebesgue measure. Affine invariance refers to the area *ratio*, not to Euclidean circumradius normalization.

## Proof

**Finite support directions.** The direction of the segment joining heptagon vertices with indices \(i\ne j\), modulo \(\pi\), is \(\pi/2+\pi(i+j)/7\). Thus all permitted outward unit normals are
\[
u_k=(\cos(k\pi/7),\sin(k\pi/7)),\qquad 0\le k<14.
\]
The heptagon's support function at these normals is
\[
h_k=h_{P_7}(u_k)=\begin{cases}1&k\text{ even},\\ c&k\text{ odd} .\end{cases}
\]
Each side of a minimum-area enclosing quadrilateral must be a supporting line of the heptagon: otherwise it can be moved inward, reducing area, unless redundant, in which case the enclosure has at most three sides. Consequently a four-sided minimizer is the intersection of four distinct half-planes \(\langle x,u_k\rangle\le h_k\). It can be bounded only if the four cyclic index gaps \(g_i\) lie in \(\{1,\ldots,6\}\), since a gap of at least seven places all the normals in a closed semicircle.

**Area identity.** For any support-saturated genuine four-sided candidate with cyclic normal indices \(k_1,k_2,k_3,k_4\), put \(k_5=k_1+14\), \(g_i=k_{i+1}-k_i\), and \(\delta_i=\pi g_i/7\). The two adjacent support lines meet, and summing the four edge-length contributions to \(2\operatorname{area}(Q)=\sum_i h_{k_i}\operatorname{length}(e_i)\) gives
\[
\operatorname{area}(Q)=\sum_{i=1}^4
\frac{h_{k_i}h_{k_{i+1}}-	frac12(h_{k_i}^2+h_{k_{i+1}}^2)\cos\delta_i}{\sin\delta_i}.
\tag{1}
\]
Here indices for \(h\) are reduced modulo fourteen. Formula (1) is only invoked as the geometric area when all four lines are active. If one is redundant, the actual enclosure is a triangle and is handled separately.

**Exact exhaustive inequality.** The number of four-element subsets of \(\{0,\ldots,13\}\) with all cyclic gaps at most six is exactly \(511\). The standalone file `certify_heptagon.py` performs the following finite proof in pure rational arithmetic. It encloses \(\pi\) by Machin's arctangent identity and alternating rational series; it encloses every necessary sine and cosine by rational Taylor polynomials with explicit remainder bounds. For each of the \(511\) subsets it evaluates interval bounds of the right-hand side of (1). Exactly seven subsets have all odd indices and cyclic gaps \((2,4,4,4)\), up to placement of the shorter gap. For each of the other \(504\), its expression in (1) is strictly greater than the common value for those seven by \(1/40\). Since all interval endpoints and comparisons are rational, this is a finite proof, not a floating-point sampling experiment. The checker also certifies \(1.2588<q_{\mathrm{ch}}(P_7)/|P_7|<1.2589\).

For the seven special subsets every supporting line is tangent to the inball of radius \(c\), and its angular gaps are \((2\pi/7,4\pi/7,4\pi/7,4\pi/7)\). Therefore all four lines are active and the area is exactly
\[
c^2\left(\tan\frac\pi7+3\tan\frac{2\pi}7\right),
\]
using the standard formula for a tangential polygon, \(\operatorname{area}=c^2\sum_i\tan(\delta_i/2)\). No remaining four-sided candidate can match or improve that value by the exact exhaustive inequality.

If a candidate has at most three sides, it contains the heptagon's inball of radius \(c\); the planar circumscribed-triangle inequality gives area at least \(3\sqrt3\,c^2>4.05\), whereas the winning quadrilateral has area less than \(3.5\). Thus degenerate or redundant candidates cannot minimize. Finally \(|P_7|=7c^2\tan(\pi/7)\), proving the area ratio. Any non-support-saturated feasible enclosure can be tightened, so the seven selected support quadruples exhaust the equality cases. An invertible affine image preserves parallelism, inclusion, and area ratios.

## Verification

Run `python3 certify_heptagon.py` from the same directory. The certificate uses only the Python standard library and exact `fractions.Fraction` operations; it does not rely on external numerical libraries. It verifies a rational \(\pi\)-enclosure, bounds all trigonometric evaluations, checks all \(511\) bounded four-normal configurations, identifies exactly seven winners, and establishes the strict \(1/40\) exclusion gap for the other \(504\). The finite enumeration is exhaustive because the normal-direction classification is proved above; it does not certify arbitrary convex-body conjectures beyond this regular-heptagon class.

## Relationship to prior work

Vígh's 2026 note introduces the chord-quadrilateral restriction, proves a universal \(\sqrt2\) bound and reports the approximate value \(1.2588\ldots\) for an affine-regular heptagon in numerical investigations. This result supplies the exact algebraic-trigonometric value, an exhaustive proof of optimality, and all seven equality quadrilaterals. Hong, Ismailescu, Kwak and Park establish a sharp result for enclosing pentagons by quadrilaterals and discuss enclosing a regular heptagon by a *hexagon*, a distinct approximation problem. Fodor and Grundbacher prove a universal bound on unrestricted enclosing quadrilaterals, which does not determine the exact chord-constrained heptagon value. The same-area enclosure question for arbitrary heptagons is not resolved here.

## Limitations

This is a complete answer for affine images of the regular heptagon under the chord-direction restriction. It does not establish the unrestricted minimum quadrilateral area, the global chord conjecture, or a bound for arbitrary seven-vertex polygons. The strict \(1/40\) gap concerns the finite, support-saturated direction classes and does not imply continuous shape stability. Bibliographic novelty is subject to possible uncatalogued equivalent classical computations.

## References

1. V. Vígh, *A note on Kuperberg's quadrilateral conjecture*, arXiv:2610.08168v1 (first posted 2026-10-06), especially Sections 2, 4, 5.
2. D. E. Hong, D. Ismailescu, A. Kwak and G. Y. Park, *On the smallest area \((n-1)\)-gon containing a convex \(n\)-gon*, arXiv:2108.00326v1 (2021), Sections 2–3.
3. F. Fodor and F. Grundbacher, *On the minimal area of quadrangles circumscribed about planar convex bodies*, arXiv:2506.05185v1 (2025), Sections 1–2.
