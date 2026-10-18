# Exact Haar polygon-type law for central sections of the regular truncated tetrahedron

## Finding

Let \(A_0=(1,1,1)\), \(A_1=(1,-1,-1)\), \(A_2=(-1,1,-1)\), and \(A_3=(-1,-1,1)\). Let \(T\subset\mathbb R^3\) be the regular truncated tetrahedron
\[
 T=\operatorname{conv}\{2A_i+A_j:0\le i,j\le3,\ i\ne j\}.
\]
Let \(U\) be uniform on \(\mathbb S^2\). For a generic \(U\), write \(N(U)\) for the number of vertices of the central polygon \(T\cap U^\perp\). For \(b\in\{1,5,7,9\}\) put \(\theta_b=\arccos(b/11)\).

**Theorem.** Almost surely \(N(U)\in\{4,5,6\}\), and the exact Haar probabilities are
\[
\begin{aligned}
\mathbb P(N=4)&=\frac{-12\pi+48\theta_1+24\theta_5-48\theta_7-24\theta_9}{4\pi},\\
\mathbb P(N=5)&=\frac{48\pi-96\theta_1-48\theta_5+24\theta_7+48\theta_9}{4\pi},\\
\mathbb P(N=6)&=\frac{-32\pi+48\theta_1+24\theta_5+24\theta_7-24\theta_9}{4\pi}.
\end{aligned}
\]
Numerically these probabilities are approximately \(0.215936085313\), \(0.520247465239\), and \(0.263816449448\), respectively. Every event has nonempty open orientation support. The underlying arrangement of section types partitions the oriented normal sphere into exactly \(134\) open spherical polygons of **six** area/section-type classes specified below. As an independent exact check, the mean is
\[
 \mathbb E N(U)=\frac{18}{\pi}\arccos\left(\frac7{11}\right).
\]

The six spherical chamber classes, shown by section vertex count, number of spherical polygon corners, multiplicity, and spherical area of **each** chamber, are:

| Section vertices | Normal-cell corners | Number of cells | Exact normal-cell area |
| --- | ---: | ---: | --- |
| \(4\) | \(4\) | \(24\) | \(-\pi+2\theta_1+\theta_5-\theta_7\) |
| \(4\) | \(8\) | \(6\) | \(2\pi-4\theta_7-4\theta_9\) |
| \(5\) | \(3\) | \(48\) | \(-\theta_1+\theta_7+\theta_9\) |
| \(5\) | \(5\) | \(24\) | \(2\pi-2\theta_1-2\theta_5-\theta_7\) |
| \(6\) | \(4\) | \(24\) | \(-\pi+2\theta_1+\theta_7-\theta_9\) |
| \(6\) | \(3\) | \(8\) | \(-\pi+3\theta_5\) |

## Assumptions and scope

The tetrahedron with vertices \(A_i\) is regular, centered at the origin. Truncating every vertex symmetrically one third of the way along each incident edge produces the twelve vertices \(V_{ij}=2A_i+A_j\), up to overall scaling; thus \(T\) is a regular truncated tetrahedron. The construction is full-dimensional, and the origin is interior because the twelve vertices have zero sum and span \(\mathbb R^3\). The choice of scale does not affect section combinatorics. All probabilities use normalized spherical area on \(\mathbb S^2\), not a nonuniform distribution of planes at arbitrary offsets. Normals at which a section passes through a vertex are excluded; they form twelve great circles of surface measure zero. The statement is therefore about generic *central* hyperplane sections only.

## Proof

**Step 1: edge crossings encode the section vertex count.** Each \(V_{ij}\) has squared Euclidean norm \(11\). An elementary check of the twelve triples shows that two distinct vertices are joined by a polytope edge exactly when their squared distance is \(8\); there are precisely \(18\) such edges. Equivalently, the edges comprise the \(12\) edges around the four original vertices and the \(6\) edges connecting the two oriented truncation points on each original tetrahedron edge. For any normal \(u\) with \(u\cdot V_{ij}\ne0\) at all twelve vertices, every intersection of the plane \(u^\perp\) with an edge in its relative interior contributes one distinct vertex of the section polygon, and all section vertices arise thus. Consequently,
\[
 N(u)=\#\{\{p,q\}\in E(T):(u\cdot p)(u\cdot q)<0\}.
\]

**Step 2: all normal chambers can be enumerated exactly.** The twelve great circles \(C_p=\{u\in\mathbb S^2:u\cdot p=0\}\), for \(p\in V(T)\), divide the sphere into cells on each of which all vertex signs, and hence \(N\), are constant. Direct integer determinants show that no three distinct vertex vectors are coplanar with the origin, and no two are proportional. Hence every pair of circles has two distinct crossing points and there are \(2\binom{12}{2}=132\) distinct spherical arrangement vertices. Each circle has \(22\) open arcs between consecutive crossings. The embedded arrangement therefore has \(264\) arcs. Euler's formula gives \(264-132+2=134\) cells.

For completeness, a transparent exhaustive *integer* enumeration is possible without angular sampling. Given any distinct vertex vectors \(p,q\), put \(c=p\cdot q\), \(w=p\times q\). Since \(\|p\|^2=\|q\|^2=11\), one has \(|c|\in\{1,5,7,9\}\). For both signs \(\varepsilon\in\{\pm1\}\) and every local sign pair \((s_p,s_q)\in\{\pm1\}^2\), define
\[
 d=s_p(11p-cq)+s_q(11q-cp),\qquad u=10000\varepsilon w+d.
\]
Here \(p\cdot d=s_p(121-c^2)\) and \(q\cdot d=s_q(121-c^2)\). For every other vertex \(v\), the integer computation verifies \(\operatorname{sgn}(v\cdot u)=\operatorname{sgn}(\varepsilon v\cdot w)\). Thus \(u\) represents precisely one of the four open chambers adjacent to the crossing \(\varepsilon w/\|w\|\). Performing this for all \(66\) pairs, both antipodal crossing points, and all four adjacent quadrants gives \(528\) witnesses with exactly \(134\) distinct sign vectors. Because each open cell is a geodesically convex intersection of hemispheres and every spherical cell has boundary crossings, these are all \(134\) cells. Every integer operation and assertion is implemented in the accompanying checker, whose output includes the six-class table.

**Step 3: calculate each chamber area.** Fix a cell with vertex signs \(s_p\in\{\pm1\}\); it is the intersection of hemispheres \(s_p(u\cdot p)>0\). Its corners are exactly those \(\pm(p\times q)/\|p\times q\|\) lying in all twelve corresponding closed hemispheres. A corner arising from the constraints for \(p,q\) has interior spherical angle
\[
 \alpha_{p,q}=\pi-\arccos\left(\frac{s_p s_q(p\cdot q)}{11}\right).
\]
If the cell has \(m\) corners, the spherical excess formula gives
\[
 \operatorname{area}(\text{cell})=\sum_{\text{corners}}\alpha_{p,q}-(m-2)\pi.
\]
All scalar products and sign comparisons are integers; the only nonrational constants that remain are \(\pi\) and \(\theta_1,\theta_5,\theta_7,\theta_9\). Counting intersected edges and corners for each of the \(134\) sign cells gives exactly the six types in the table. Their multiplicities sum to \(134\). The areas in the table, multiplied by their multiplicities and summed across all six types, simplify **exactly** to \(4\pi\); the three totals, grouped by section count, are the probability numerators displayed in the theorem. Each of the six areas is positive, proving every claimed section type has an open set of orientations.

**Step 4: independently evaluate the mean.** Every edge \(\{p,q\}\) has \(p\cdot q=7\), because both endpoints have squared norm \(11\) and their squared distance is \(8\). For two vectors meeting at angle \(\theta\), the probability that a uniform normal has opposite-sign scalar products with them is exactly \(\theta/\pi\), by the area of the associated two spherical lunes. The edge-crossing count of Step 1 and linearity of expectation therefore yield
\[
 \mathbb E N=18\theta_7/\pi.
\]
It also follows from multiplying the three exact distribution probabilities by \(4,5,6\), respectively. This independent check detects a nontrivial cancellation of the other three angular constants.

## Verification

Run the standalone Python 3 checker `check_truncated_tetra_sections.py` (standard library only) from the directory containing this report:

```sh
python3 check_truncated_tetra_sections.py
```

It verifies all twelve integer vertices, all eighteen edges, nonconcurrence of the twelve great circles, every one of the \(528\) local crossing-quadrant sign witnesses, all \(134\) distinct spherical cells, the six cell types and exact integer coefficient tuples, exact total spherical area \(4\pi\), and the independent edge-crossing first-moment identity. Its final line is `EXACT_CHAMBERS_OK 134_cells 18_edges 3_support_values`. All area expressions are determined by exact integers multiplying \(\pi\) and \(\arccos(b/11)\); floating-point values only illustrate the distribution. The exhaustive finite integer enumeration and the spherical excess theorem jointly prove the general distribution; there is no sampling-based inference or unproved extrapolation.

## Relationship to prior work

Birkemeyer, Brose, Brandenburg and Prün (2026) study whether face-vector information of central sections determines the original polytope's combinatorial type, and formulate combinatorial slicing questions. Their results do not supply a Haar-distribution calculation for a truncated tetrahedron. De Loera, Lopez-Campos and Torres (2024) address attainable section-vertex counts and bounds for general polytopes and special cubes; their results do not determine the spherical measures of the three section types here. Counting intersected polytope edges and spherical excess are classical techniques and are not claimed as new. The specific combined exact probability law and six-class spherical arrangement census are the contribution under evaluation.

## Limitations

The result is for one natural three-dimensional Archimedean solid and *central* planes. It does not classify off-center sections, and it does not imply a general formula for other solids or for arbitrary affine deformations when the normal distribution remains Euclidean Haar measure. The exact finite checker establishes a complete computation for the explicitly specified twelve-vector configuration; it does not independently certify historical priority. Earlier unindexed stereological tables or older computational geometry literature may contain an equivalent distribution,; historical priority remains a separate, unresolved question.

## References

1. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, and N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195, first public version September 14, 2026. https://arxiv.org/abs/2609.16195
2. J. A. De Loera, G. Lopez-Campos, and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419, first public version December 17, 2024. https://arxiv.org/abs/2412.12419
