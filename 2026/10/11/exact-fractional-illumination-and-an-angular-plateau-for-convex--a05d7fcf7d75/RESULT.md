# Exact fractional illumination and an angular plateau for convex polygons

## Finding

For a full-dimensional convex polygon \(P\) with \(m\ge3\) genuine vertices, let \(I^*(P)\) be the infimum of the total mass of finitely supported nonnegative measures on the direction circle for which the directions entering the interior of \(P\) from every boundary point have mass at least one. Say that \(P\) is equiangular if its successive outward edge-normal angles differ by \(2\pi/m\). Then
\[
I^*(P)=\frac{m}{\lfloor(m-1)/2\rfloor}.
\]
This formula is independent of its side lengths and offsets: regularity is not assumed.

There is also an explicit open angular plateau for odd-sided polygons. If \(m=2q+1\ge3\), the outward normal arguments admit an increasing cyclic labeling \(\theta_0,\ldots,\theta_{m-1}\), and for some \(\phi\in\mathbb R\)
\[
\left|\theta_i-\phi-\frac{2\pi i}{m}\right|<\frac{\pi}{2m}
\quad(0\le i<m),
\]
with a consistent cyclic lift, then
\[
I^*(P)=\frac{m}{q}.
\]
Thus the odd-sided equiangular value persists under all sufficiently small independent perturbations of the edge normals, without assumptions of nearly equal side lengths.

## Assumptions and scope

A genuine \(m\)-gon has no collinear consecutive edges, so the exterior turning angle between successive outward normals is strictly between zero and \(\pi\). Its vertices are indexed so that vertex \(v_i\) is incident to edges whose outward normal arguments are \(\theta_{i-1}\) and \(\theta_i\); extend the angles by \(\theta_{i+m}=\theta_i+2\pi\). The small normal-displacement hypothesis in the second assertion is on one consistently rotated labeling of the normals, rather than on side lengths or on distances of vertices from a regular polygon. All illumination inequalities use strictly inward directions at boundary points.

## Proof

**Reduction to vertex arcs.** A direction with angular argument \(t\) enters the interior at \(v_i\) exactly when its scalar products with both adjacent outward normals are strictly negative. In a compatible real angular lift its admissible set is the open circular arc
\[
A_i=\left(\theta_i+\frac\pi2,\ \theta_{i-1}+\frac{3\pi}2\right)\pmod{2\pi}.
\]
Its length is \(\pi-(\theta_i-\theta_{i-1})\), strictly between zero and \(\pi\). Strict negativity follows from the two active halfspace inequalities defining the local tangent cone. Conversely, if a small step from \(v_i\) enters the polygon interior, both active inequalities must be strict. At a relative interior point of edge \(i\), illumination requires only a negative scalar product with its one active normal. Therefore any fractional measure illuminating all vertices also illuminates each open edge: its incident vertex's illuminated-direction set is a subset of the open edge's illuminated-direction set. The infinitely many boundary constraints reduce exactly to the \(m\) vertex-arc constraints.

**Equiangular lower bound.** Write \(\Delta=2\pi/m\), \(k=\lfloor(m-1)/2\rfloor\), and \(\theta_i=\phi+i\Delta\). The arcs \(A_i\) have equally spaced start points and equal length \(\ell=\pi-\Delta\). The elementary inequalities
\[
(k-1)\Delta<\ell\le k\Delta
\]
hold for both parities: for odd \(m=2q+1\) the length is \((q-\tfrac12)\Delta\), while for even \(m=2q\) it is \((q-1)\Delta\). No direction belongs to more than \(k\) arcs, since \(k+1\) equally spaced arc starts cannot fit in an open interval of length at most \(k\Delta\), including the strict-endpoint even case. For a feasible finitely supported measure \(\mu\), summing the \(m\) vertex illumination inequalities and exchanging the finite sum and integral yields
\[
m\le\sum_{i=0}^{m-1}\mu(A_i)\le k\mu(S^1),
\]
so \(I^*(P)\ge m/k\).

**Equiangular construction.** For every cyclic block of \(k\) consecutive arcs \(A_j,A_{j+1},\ldots,A_{j+k-1}\), their open intersection has length \(\ell-(k-1)\Delta>0\). Choose one direction \(t_j\) in this intersection. Give each of the \(m\) directions weight \(1/k\). Every vertex arc contains at least the \(k\) directions from the \(k\) cyclic blocks containing its index, hence has mass at least one. The total mass is \(m/k\). This proves the exact equiangular formula and attainment by finite support.

**Odd-sided angular plateau.** Let \(m=2q+1\), \(\Delta=2\pi/m\), and \(\eta=\max_i|\theta_i-(\phi+i\Delta)|<\Delta/4\). The corresponding regular-reference vertex arcs have length \((q-\tfrac12)\Delta\). Each actual arc is contained in its reference arc with both endpoints extended outward by \(\eta\). Each extended arc has length strictly less than
\[
(q-\tfrac12)\Delta+2(\Delta/4)=q\Delta.
\]
Since the reference start points are spaced by \(\Delta\), no direction belongs to \(q+1\) extended arcs and hence no actual direction illuminates more than \(q\) vertices. Summing the vertex constraints gives the lower bound \(I^*(P)\ge m/q\).

For the reverse bound, every intersection of \(q\) consecutive reference arcs has width \(\Delta/2\). Its midpoint has distance at least \(\Delta/4\) from every endpoint of any arc in that block. Because all actual endpoints move by at most \(\eta<\Delta/4\), this same midpoint illuminates the \(q\) corresponding vertices of the actual polygon. Place mass \(1/q\) at the \(m\) cyclic block-midpoints. Every vertex belongs to exactly \(q\) selected blocks, and hence receives at least unit mass. Thus \(I^*(P)\le m/q\), completing the proof.

## Verification

The supplied standalone `verify_fractional_polygon.py` uses exact rational fractions of a full angular turn. It constructs vertex arcs and cyclic-block directions for each \(3\le m\le27\), evaluates overlap counts at every arc endpoint and in every complementary interval, and repeats the checks on three deterministic perturbations for each odd \(m\). It verifies the complete incidence conditions rather than relying on approximate floating-point trigonometry. Replay with Python 3 using `python3 verify_fractional_polygon.py`; the expected result is `VERIFY_OK exact_fractional_polygon assertions=738`. These 738 assertions are illustrative finite consistency checks. The infinite statement, strict endpoint conventions, and angular plateau follow from the analytic arc-counting proof above.

## Relationship to prior work

Naszódi introduced fractional illumination and proved general upper bounds; his Proposition 5 supplies the lower bound \(I^*(P_5)\ge5/2\) for the regular pentagon. The present formula reproduces that bound as an equality in this known special case, but treats all equiangular polygons, gives the full parity-dependent sequence, and proves a quantitative open plateau for all odd side counts. Gorodzha's 2026 theorem gives \(I^*(K)\le2^d\), with equality only for parallelotopes, so in the plane it provides an upper bound of four but does not imply these exact polygonal values or their robustness. Distinct literature on polygonal **illumination bodies** deals with convex-hull area sublevel sets rather than weighted inward directions, and does not supply a competing value for \(I^*(P)\).

## Limitations

The sufficient angular radius \(\pi/(2m)\) is not claimed to be the largest possible plateau radius. No exact formula is asserted for arbitrary nonequiangular polygons or for higher dimensions. Finite checks do not prove general claims; the proof is analytic. The originality assessment has searched direct and equivalent terminology but cannot exclude an older derivation under an unindexed cyclic-arc formulation. No independent mathematical audit has been performed.

## References

M. Naszódi, “Fractional Illumination of Convex Bodies,” Contributions to Discrete Mathematics 4 (2009), no. 2, 83–88, especially Definition 1 and Proposition 5. https://cdm.ucalgary.ca/article/download/62022/46694/177154

Y. Gorodzha, “Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture,” arXiv:2609.23913, first publicly posted 2026-09-20. https://arxiv.org/abs/2609.23913
