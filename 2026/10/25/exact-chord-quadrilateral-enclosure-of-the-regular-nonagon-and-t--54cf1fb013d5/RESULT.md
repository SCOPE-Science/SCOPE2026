# Exact chord-quadrilateral enclosure of the regular nonagon and essential diagonal directions

## Finding
For the unit-circumradius regular nonagon \(P_9\), let \(\theta=\pi/9\), \(c=\cos\theta\), and denote by \(q_{\mathrm{ch}}(P_9)\) the smallest area of a containing polygon with at most four sides, each parallel to a chord between vertices of \(P_9\). Then
\[
q_{\mathrm{ch}}(P_9)=2\frac{c-\frac12(1+c^2)\cos(5\theta)}{\sin(5\theta)}+2c^2\tan(2\theta).
\]
The value divided by \(\operatorname{area}(P_9)=\frac92\sin(2\theta)\) is \(1.2868576376403533\ldots\). Exactly nine chord quadrilaterals attain equality, one orbit under nonagon rotations. Their successive outward normal indices, for normals \(n_k=(\cos(k\pi/9),\sin(k\pi/9))\), are the rotations \(\{0,5,9,13\}+2r\pmod {18}\), \(r=0,\ldots,8\). Consequently exactly one of their four supporting directions is not parallel to a polygon edge.

If the quadrilateral's sides must all be parallel to *edges* of \(P_9\), the sharp, strictly larger area is
\[
q_{\mathrm{edge}}(P_9)=c^2\bigl(3\tan(2\theta)+\tan(3\theta)\bigr),
\]
attained by exactly the nine rotations of \(\{1,5,9,13\}\). The edge-only to unrestricted-chord area gap is approximately \(0.0299775611734\) (circumradius one). Affine changes of coordinates preserve the ratio and carry both equality classifications to affine-regular nonagons.

## Assumptions and scope
A chord means any segment joining two polygon vertices, including polygon edges. Containing quadrilaterals may use every chord *direction*, but each supporting line can be translated independently. The polygon is strictly convex and regular with circumradius one. A minimal enclosure has four supporting sides: starting from any enclosure with fewer sides, an additional support in a nonagon-edge direction removes a positive-area portion unless the enclosure already equals the nonagon, impossible with fewer than nine sides.

## Proof
The vertices are \(v_j=(\cos(2j\theta),\sin(2j\theta))\) for \(j=0,\ldots,8\). A chord through \(v_i\) and \(v_j\) has undirected normal angle \((i+j)\theta\) modulo \(\pi\). Thus all possible directed chord normals are exactly \(n_0,\ldots,n_{17}\). The supporting half-plane with normal \(n_k\) is
\[
n_k\cdot x\le h_k,\qquad h_k=\begin{cases}1,&k\text{ even},\\c,&k\text{ odd}.\end{cases}
\]
This follows by maximizing the cosines of the nine vertex angle differences. Pushing any other parallel bounding line inward until contact cannot increase enclosure area.

For four cyclically ordered distinct indices \(k_0<k_1<k_2<k_3\), put \(k_4=k_0+18\) and \(d_i=k_{i+1}-k_i\) for \(i=0,\ldots,3\). The four half-planes have bounded intersection if and only if \(1\le d_i\le8\) for all four indices: equivalently the four outward normals positively span the plane. The chosen support lines are tangent to the nonagon. They bound a convex polygon whose consecutive vertices are obtained by intersecting consecutive lines; a zero-length intermediate side is permitted. The support-line formula for the enclosed area is
\[
A(k_0,k_1,k_2,k_3)=\sum_{i=0}^3\frac{h_{k_i}h_{k_{i+1}}-\frac12(h_{k_i}^2+h_{k_{i+1}}^2)\cos(d_i\theta)}{\sin(d_i\theta)},
\]
where the support height at \(k_4\) is that at \(k_0\). Indeed, the length of the supporting edge at normal \(k_i\) is the sum of its signed tangent-coordinate displacements to adjacent intersections, and the polygon area equals half the sum of each support height times its corresponding edge length. This derivation applies also when an intermediate contact edge has zero length.

The formula reduces the global continuous enclosure problem to a finite comparison. There are \(\binom{18}{4}=3060\) index sets; exactly \(1548\) have every cyclic normal gap at most eight. Let \(x=2\cos\theta\), the unique root in \((1,2)\) of \(x^3-3x-1=0\), and let \(C_d=\cos(d\theta)\) and \(S_d=\sin(d\theta)/\sin\theta\). These obey the exact recurrences
\[
C_0=1,\ C_1=x/2,\ C_{d+1}=xC_d-C_{d-1};\qquad S_0=0,\ S_1=1,\ S_{d+1}=xS_d-S_{d-1}.
\]
Consequently each \(A\sin\theta\) is a rational function of \(x\). The accompanying standalone `nonagon_chord_checker.py` proves exact lower and upper bounds for every one of the \(1548\) eligible rational functions using outward rational interval arithmetic. Its isolating rational interval for \(x\) has endpoints \(18793852415/10^{10}\) and \(18793852417/10^{10}\); both are checked against the defining cubic. It certifies that **precisely nine** candidates minimize \(A\), namely the rotations \(\{0,5,9,13\}+2r\pmod{18}\), and that the scaled area \(A\sin\theta\) of every other candidate exceeds the winner by more than \(1/100\). This is a complete finite exact-arithmetic comparison, not a floating-point search.

For the winning set the four cyclic gaps are \((5,4,4,5)\), with support heights \((1,c,c,c)\). Substituting into the area formula gives the first displayed closed form. Restricting to odd indices, i.e. actual edge directions, leaves \(90\) bounded candidates; the same exact checker proves that **precisely nine** minimize, all rotations of \(\{1,5,9,13\}\), and that the scaled gap above the best edge-only candidate is more than \(1/10\) for every other edge-only configuration. Their gaps are a permutation of \((4,4,4,6)\), yielding the second displayed expression. The checker also proves the best edge-only scaled area is more than \(1/100\) above the unrestricted chord optimum, hence the diagonal-direction improvement is strict.

Finally, every invertible affine transformation bijectively maps chord-parallel enclosing quadrilaterals and actual-edge-parallel quadrilaterals to those of the image nonagon, multiplying all areas by the absolute determinant. This preserves ratios and optimizer counts.

## Verification
Run `python nonagon_chord_checker.py` with standard Python 3; no external dependencies are used. The script reconstructs the isolating interval, recursively computes rational intervals for all relevant trigonometric expressions, proves positive denominators, enumerates \(3060\) support-normal subsets, checks all \(1548\) bounded cases, and independently checks the \(90\) bounded edge-only cases and both optimizer orbits. The test output contains the exact-count and strict-margin certificates. The proof is valid for the fixed nine-gon because enumeration is exhaustive over its finite chord-normal set; no general all-polygons inequality is claimed.

## Relationship to prior work
Vígh's October 2026 note defines chord-quadrilateral enclosure, proves a general \(\sqrt2\) upper bound and recalls the sharp pentagon case. It reports numerical experiments at several polygon sizes and a numerical benchmark for a regular heptagon, but gives neither an exact regular-nonagon chord enclosure nor a nine-gon optimizer classification. The existing theorem of Hong, Ismailescu, Kwak and Park concerns pentagonal enclosures and does not imply this regular nine-gon calculation. Published work on minimum-area *parallelogram* enclosures of regular polygons concerns a strictly smaller set of allowed quadrilateral shapes and cannot determine the present strict diagonal-direction gap. The older regular-heptagon exact chord computation concerns a different polygon and does not imply the nine-gon value or its changed optimal tangency pattern.

## Limitations
This concerns chord-restricted enclosing quadrilaterals and the edge-only subproblem for affine-regular nonagons, not the unrestricted minimum-area quadrilateral, not all nine-gons, and not the universal Kuperberg/chord conjectures. The enumeration is a fully specified finite exact-arithmetic proof for the nonagon only. Independent external verification has not been performed. Possible overlap in unindexed prior literature is not excluded by the searches.

## References
1. V. Vígh, *A note on Kuperberg's quadrilateral conjecture*, arXiv:2610.08168v1, first posted 2026-10-06, https://arxiv.org/html/2610.08168v1.
2. S. Hong, D. Ismailescu, S. Kwak and J. Park, *On smallest area (n-1)-gon containing a convex n-gon*, arXiv:2108.00326v1, https://arxiv.org/abs/2108.00326.
