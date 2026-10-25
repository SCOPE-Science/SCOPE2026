# Exact midpoint law and a parity singularity for random polygon chords

## Finding

Let \(K\subset\mathbb R^2\) be a nondegenerate convex polygon with \(n\ge3\) positive-length edges \(E_1,\ldots,E_n\), no consecutive collinear edges, lengths \(\ell_i\), direction vectors \(e_i\), and perimeter \(P=\sum_i\ell_i\). Choose \(X,Y\) independently from normalized arclength on \(\partial K\), and set \(M=(X+Y)/2\). Then the *complete law* of \(M\) consists of an explicitly described planar absolutely continuous component and two kinds of one-dimensional singular components.

For each pair of **nonparallel** distinct edges, write \(Q_{ij}=(E_i+E_j)/2\), their midpoint parallelogram, and let \(\alpha_{ij}\in(0,\pi)\) be the unoriented angle between their supporting lines. The density of the absolutely continuous component is, for Lebesgue-almost every \(x\),

\[
 f_K(x)=\frac8{P^2}\sum_{i<j:\,e_i\not\parallel e_j}
 \frac{\mathbf 1_{Q_{ij}}(x)}{|\sin\alpha_{ij}|}.
\]

The total singular mass, and its canonical separation into boundary and interior singular mass, are

\[
\begin{aligned}
 s(K)&=\frac{\sum_i\ell_i^2+2\sum_{i<j:\,e_i\parallel e_j}\ell_i\ell_j}{P^2},\\
 s_{\partial}(K)&=\frac{\sum_i\ell_i^2}{P^2},\qquad
 s_{\mathrm{int}}(K)=\frac{2\sum_{i<j:\,e_i\parallel e_j}\ell_i\ell_j}{P^2}.
\end{aligned}
\]

The boundary singular part is distributed on each edge according to a triangular arclength density. The interior singular part lies *exactly* on midpoint segments of distinct parallel edges and has explicit triangular or trapezoidal arclength densities. In particular, \(s_{\mathrm{int}}(K)>0\) if and only if the polygon has a pair of parallel distinct edges.

For the regular \(n\)-gon, the singular probability has the exact parity law

\[
\boxed{s(K)=\begin{cases}1/n,&n\text{ odd},\\2/n,&n\text{ even}.
\end{cases}}
\]

For a centrally symmetric \(n=2m\)-gon, one furthermore has the sharp rigidity inequality

\[
\boxed{s(K)\ge\frac2n,}
\]

with equality **exactly when all side lengths are equal** (not necessarily when the polygon is regular). These statements hold for all permitted dimensions of the polygonal parameter space, without a generic-position restriction on nonadjacent parallel edges.

## Assumptions and scope

The sampling law is **two independent boundary-arclength samples**, not a motion-invariant random line, random chord midpoint, or two area-uniform interior samples. Vertices have zero sampling probability. The convex polygon has no redundant collinear consecutive edges, so each distinct supporting edge line touches the polygon in precisely that edge. The measure decomposition is with respect to planar Lebesgue measure and its singular complement; intersections of singular lines have probability zero. These distinctions are essential to the singular-mass classification.

To give the one-dimensional densities, use the unit-speed parameter \(z\in[0,1]\) on an edge \(E_i\). The boundary component there has density

\[
\frac{4\ell_i}{P^2}\min\{z,1-z\}
\]

with respect to Euclidean arclength. For a parallel pair \(E_i,E_j\), choose a common unit vector \(u\), let their projections onto \(u\) be intervals \([a_i,b_i]\), \([a_j,b_j]\) of lengths \(\ell_i,\ell_j\), and let \(t=\langle u,M\rangle\). On their midpoint line, the pair's arclength density is

\[
\frac4{P^2}\Big[\min\{b_i,2t-a_j\}-\max\{a_i,2t-b_j\}\Big]_+,
\]

where \([q]_+=\max\{q,0\}\). The line's orthogonal coordinate is the average of those of the two supporting lines. Summing densities accounts for coincident midpoint lines if they occur.

## Proof

**Edge-pair decomposition.** For a single edge \(E_i\), the arclength sampling probability is \(\ell_i/P\). Thus an unordered distinct pair \(\{i,j\}\) occurs with probability \(2\ell_i\ell_j/P^2\), and a same-edge pair with probability \(\ell_i^2/P^2\). Conditioned on the selected edges, two independent uniform arclength parameters \(u,v\in[0,1]\) determine the midpoint via the affine map

\[
F_{ij}(u,v)=\frac{v_i+v_j+ue_i+ve_j}{2},
\]

where \(v_i\) is one endpoint of \(E_i\) and \(e_i\) is the full directed edge vector.

**Nonparallel pairs.** If the edge directions are independent, the determinant of this map is \(|\det(e_i,e_j)|/4=\ell_i\ell_j|\sin\alpha_{ij}|/4\). Uniform parameter measure pushes forward to the uniform probability measure on \(Q_{ij}\), of planar density \(4/(\ell_i\ell_j|\sin\alpha_{ij}|)\). Multiplication by the unordered edge-pair probability gives \(8/(P^2|\sin\alpha_{ij}|)\). Summing over nonparallel pairs gives the claimed planar density. Each term integrates to its edge-pair probability because \(\operatorname{Area}(Q_{ij})=\ell_i\ell_j|\sin\alpha_{ij}|/4\).

**Same-edge pairs.** The average of two independent unit uniforms has density \(4\min\{z,1-z\}\) on \([0,1]\). Multiplying by \(\ell_i^2/P^2\) and converting \(dz\) to physical arclength \(\ell_i dz\) gives the stated density and total mass \(\ell_i^2/P^2\). Every such midpoint lies on \(\partial K\).

**Parallel distinct pairs.** With the common tangent coordinate, the convolution of two uniform interval distributions at the sum coordinate \(2t\) has density equal to the overlap length

\[
 \big|[a_i,b_i]\cap[2t-b_j,2t-a_j]\big|/(\ell_i\ell_j).
\]

The coordinate change from sum to average multiplies it by \(2\); the unordered pair weight multiplies it by \(2\ell_i\ell_j/P^2\). This gives the displayed trapezoidal density \(4/P^2\) times the interval-overlap length, integrating to \(2\ell_i\ell_j/P^2\). The image is one dimensional. Because distinct supporting edges of a nondegenerate convex polygon have no common supporting line, the midpoint of interior points on distinct edges lies in \(\operatorname{int}K\); hence this entire one-dimensional component is interior singular, away from endpoints of measure zero.

**Exhaustion and parity.** All ordered edge choices belong to exactly one of the above three cases. Consequently the three masses sum to one and the Lebesgue decomposition is complete. In a regular odd \(n\)-gon no distinct edges are parallel, while in a regular even \(n\)-gon each edge has exactly one parallel opposite edge. With \(\ell_i/P=1/n\), same-edge mass is \(1/n\), and parallel-pair mass is respectively \(0\) or \((n/2)(2/n^2)=1/n\). This proves the parity law.

**Centrally symmetric sharpness.** Every centrally symmetric convex \(2m\)-gon has exactly \(m\) opposite parallel edge pairs of equal lengths \(L_1,\ldots,L_m\), with \(P=2\sum_k L_k\), and no other parallel distinct pairs. Its same-edge and interior-parallel masses are each \(2\sum_kL_k^2/P^2\), giving

\[
s(K)=\frac{\sum_{k=1}^mL_k^2}{(\sum_{k=1}^mL_k)^2}\ge\frac1m=\frac2n.
\]

Cauchy--Schwarz gives equality exactly when all \(L_k\) are equal, i.e. when the whole polygon is equilateral.

As another exact geometric consequence, for a triangle the medial triangle occupies precisely half of each nonparallel edge-pair midpoint parallelogram (and contains no positive mass from same-side pairs). Therefore

\[
\Pr\{M\in\operatorname{int}(\text{medial triangle})\}
=\frac12\left(1-\sum_{i=1}^3\frac{\ell_i^2}{P^2}\right)
\le\frac13,
\]

with equality exactly for equilateral triangles.

## Verification

The complete proof above is symbolic and does not require sampling. The standalone script `verify_polygon_midpoint.py` reproduces six independently sampled edge-type frequency checks, direct numerical integration of four parallel-pair line densities, exact normalization identities for the regular polygons with \(3\le n\le20\), and the medial-triangle event for a scalene triangle. Run `python3 verify_polygon_midpoint.py`; `CHECKS.txt` records the observed results. The relevant probability pieces are conditioned on **which edges** were sampled, an observable discrete variable, avoiding unstable detection of singular supports through numerical distance thresholds. For every nonparallel pair, the analytic Jacobian check independently verifies its planar density normalization. These finite experiments are corroboration, not an infinite-dimensional or all-polygon proof.

## Relationship to prior work

Bäsel (arXiv:1204.2707, first posted 2012-04-12) calculates invariant-line chord lengths for regular polygons and distances between independently sampled **interior-area** points. His full preprint develops the motion-invariant line parameterization and its length distribution, not the spatial midpoint measure of two **boundary-arclength** samples. Both settings concern polygonal geometric probability, but neither random variable determines this midpoint-law decomposition.

The 2007 paper *Evaluating the boundary and covering degree of planar Minkowski sums and other geometrical convolutions* studies geometry and preimage multiplicity of sums of plane curves. Its general Jacobian/covering perspective motivates the separation of rank-two and rank-one edge-pair maps; the weighted probability densities, sharp singular masses, and regular-polygon parity law are additional statements, not asserted in its displayed covering-degree analysis. Standard convolution and change-of-variables formulas are the essential background method. The result does not claim these methods to be new.

## Limitations

The endpoints must be sampled independently with **uniform perimeter arclength**, and the polygon must have genuine edges with positive lengths. The claim does not describe motion-invariant random-line chords, random interior pairs, smooth convex curves, or nonconvex polygonal curves. Near-parallel edge pairs produce large but finite planar densities and become truly singular only at exact parallelism; convergence in total variation under geometric approximation is not asserted. An equivalent general published convolution theorem, especially one explicitly treating polygonal boundary measures and their singular components, could supersede the present originality assessment; publication-level originality remains provisional pending independent review.

## References

1. Uwe Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first submitted 2012-04-12; subsequently *Acta Math. Univ. Comenianae* 83 (2014), 1--18. https://arxiv.org/abs/1204.2707
2. *Evaluating the boundary and covering degree of planar Minkowski sums and other geometrical convolutions*, *Journal of Computational and Applied Mathematics* 209 (2007), 246--266. DOI:10.1016/j.cam.2006.11.006.
3. L. A. Santaló, *Integral Geometry and Geometric Probability*, 1976. General geometric-probability background; no midpoint measure formula is attributed to this book.
