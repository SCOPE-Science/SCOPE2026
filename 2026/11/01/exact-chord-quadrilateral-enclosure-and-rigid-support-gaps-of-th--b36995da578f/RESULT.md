# Exact chord-quadrilateral enclosure and rigid support gaps of the regular heptagon

## Finding

Let \(P_7\subset\mathbb R^2\) be a regular heptagon of circumradius one. Among convex polygons with at most four sides that contain \(P_7\) and whose side directions are parallel to chords (segments connecting two heptagon vertices), the least area is
\[
q_{\mathrm{ch}}(P_7)=\cos^2\!\left(\frac\pi7\right)\left(\tan\frac\pi7+3\tan\frac{2\pi}7\right).
\]
Its ratio to the heptagon area is
\[
\boxed{\frac{q_{\mathrm{ch}}(P_7)}{|P_7|}=\frac47+\frac{3}{7\cos(2\pi/7)}=1.258803773547\ldots.}
\]
The ratio is the unique real root greater than one of \(49r^3-84r+8=0\).

There are exactly **seven** different minimizing chord quadrilaterals, forming one orbit under the heptagon's cyclic rotations. All four of their sides contain heptagon edges. With the fourteen outward support-normal angles indexed by \(j\pi/7\) (\(j=0,\ldots,13\)), chosen so that odd indices are heptagon-edge normals, the seven minimizing index sets are cyclic translates of \(\{1,3,7,11\}\) modulo fourteen.

Every other bounded four-support chord quadrilateral has area larger than the minimum by **strictly more than** \(1/40\) for circumradius one. This is a certified, conveniently rational separation; it is not claimed to be the exact runner-up gap.

## Assumptions and scope

A chord joins two *vertices* of the heptagon. A chord quadrilateral has at most four sides and contains the entire closed heptagon. Its side directions, not necessarily its supporting points, must be chord-parallel. Translation of each side toward the heptagon yields a supported enclosure of no greater area. The optimum necessarily has four sides: a triangle containing a genuine heptagon has a corner outside the heptagon, and adding a separating heptagon-edge support cuts that corner and strictly reduces area without exceeding four sides. In a minimum four-sided enclosure, all sides can consequently be taken to be supporting lines.

Every heptagon vertex-to-vertex chord direction has a normal direction indexed by one of \(j\pi/7\), for \(j\in\mathbb Z/14\mathbb Z\); the corresponding support numbers are
\[
h_j=\begin{cases}1,&j\text{ even},\\ \cos(\pi/7),&j\text{ odd}.\end{cases}
\]
Thus the available support lines are exactly fourteen. Four distinct outward normals in cyclic order bound a nondegenerate containing quadrilateral precisely when every successive angular gap is strictly less than \(\pi\). Collinear or unbounded cases cannot improve a bounded minimizer.

## Proof

**Finite reduction.** Let \(j_1,j_2,j_3,j_4\) be four distinct cyclically ordered indices, and put \(\delta_i=(j_{i+1}-j_i)\pi/7\in(0,\pi)\), with indices cyclic modulo fourteen. Split the supporting quadrilateral into the four triangles subtended at the origin by successive intersections of its supporting lines. The resulting exact area identity is
\[
A(j_1,j_2,j_3,j_4)=\sum_{i=1}^4
\frac{h_{j_i}h_{j_{i+1}}-\tfrac12(h_{j_i}^2+h_{j_{i+1}}^2)\cos\delta_i}{\sin\delta_i}.
\tag{1}
\]
Here the origin is interior because all support numbers are positive. The allowable normal angles form one 14-element cyclic set. Enumerating four-element subsets subject to every consecutive index gap below seven leaves exactly 511 bounded supported quadrilaterals.

**Candidate and algebraic form.** The normal index set \(\{1,3,7,11\}\) has all four supports equal to \(c=\cos(\pi/7)\) and angular gaps \(2\pi/7,4\pi/7,4\pi/7,4\pi/7\). Equation (1) gives
\[
A_*=c^2\left(\tan\frac\pi7+3\tan\frac{2\pi}7\right).
\]
The heptagon area is \(|P_7|=7\sin(\pi/7)\cos(\pi/7)\). Elementary trigonometric simplification gives
\[
\frac{A_*}{|P_7|}=\frac47+\frac{3}{7\cos(2\pi/7)}.
\]
Writing \(z=2\cos(2\pi/7)\), the seventh-root-of-unity identity yields \(z^3+z^2-2z-1=0\). Substitution \(z=6/(7r-4)\) gives \(49r^3-84r+8=0\). Of its three real roots, the displayed ratio is the only one greater than one.

**Exact exhaustive comparison and uniqueness.** The included standalone program `verify_heptagon.py` uses no floating point or third-party dependencies. Machin's identity and alternating rational series rigorously enclose \(\pi\), while rational Taylor bounds enclose every required sine and cosine. Outward-rounded rational intervals with denominator \(10^{18}\) are then applied to equation (1), for **all 511** configurations. Exactly seven have four edge normals with cyclic gap multiset \(\{2,4,4,4\}\) in index steps. For these seven, direct interval evaluations contain the analytically exact value \(A_*\); their equality follows from their identical gap multiset and support numbers. For each of the other **504** configurations, the **lower** rational area bound exceeds the **upper** rational bound for \(A_*\) by more than \(1/40\). This exhausts the finite problem and establishes both strict optimality and classification.

## Verification

Run `python3 verify_heptagon.py` in the directory containing the supplied verification program. It reports 511 bounded configurations, seven optimal support sets, and 504 strict competitors. Its exact rational interval calculations certify a uniform competitor excess of more than \(1/40\). The closest competing index set encountered is \(\{0,3,7,11\}\); the minimum certified lower bound on its difference, multiplied by \(10^{18}\), is 25947319986048213.

The proof that *only* 511 candidates must be checked is geometric and given above; the interval program rigorously checks that finite collection. This is an exhaustive finite certificate, not an extrapolation from sampling.

## Relationship to prior work

Vígh introduced the chord-quadrilateral function, established the universal \(\sqrt2\) chord upper bound, and reported approximately \(1.2588\) for a regular heptagon in numerical experiments. This identifies the same natural benchmark, but the inspected article supplies neither the above exact closed form nor the complete minimizing support sets and certified gap.

The general convex-body estimate of Fodor and Grundbacher, and the exact pentagonal bound of Hong, Ismailescu, Kwak and Park, address different quantifiers and do not determine the heptagon's exact chord-constrained minimum. The published exact minimum-enclosing-parallelogram theorem for regular polygons constrains opposite side pairs to be parallel, while the optimal heptagon chord quadrilateral here has four distinct side directions. A published exact quadrilateral enclosure of a particular midpoint-truncated pentagon likewise concerns a different polygon and allows unrestricted side directions.

## Limitations

This is an exact benchmark and rigidity result for one seven-vertex affine-equivalence class, not a new universal upper bound for all polygons, nor a proof of Kuperberg's conjecture. The gap \(1/40\) is a rigorous simple lower bound, not the optimal gap. The result concerns chord-constrained enclosures, and a potentially smaller *unrestricted* minimum enclosing quadrilateral is not computed. The finite certificate can be rerun independently but has not received independent mathematical audit. Historical literature or unindexed computations may already contain an equivalent exact heptagon specialization; no uniqueness of historical priority is claimed.

## References

1. V. Vígh, *A note on Kuperberg's quadrilateral conjecture*, arXiv:2610.08168v1, publicly posted October 6, 2026, especially Definition 2.1 and the numerical experiments. https://arxiv.org/html/2610.08168v1
2. F. Fodor and F. Grundbacher, *On the minimal area of quadrangles circumscribed about planar convex bodies*, arXiv:2506.05185v1, June 5, 2025. https://arxiv.org/html/2506.05185
3. E. Hong, D. Ismailescu, A. Kwak and G. Y. Park, *On the smallest area (n−1)-gon containing a convex n-gon*, arXiv:2108.00326 (2021). https://arxiv.org/abs/2108.00326
4. *Exact minimum-area enclosing parallelograms for regular polygons*, published mathematical finding, October 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-minimum-area-enclosing-parallelograms-for-regular-polygons--827c68cd7bad
5. *Exact quadrilateral enclosure of the midpoint-truncated affine-regular pentagon*, published mathematical finding, October 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-quadrilateral-enclosure-of-the-midpoint-truncated-affine-r--8673c6028e36
