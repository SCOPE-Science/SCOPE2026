# Global orbit classification for the farthest-facet projection map on a regular simplex

## Finding
Let \(d\geq3\), and let \(S\subset\mathbb R^d\) be a nondegenerate regular simplex with vertices indexed by \(0,\ldots,d\). On its boundary, choose a supporting facet farthest from the current point, project orthogonally onto that facet, and leave the point fixed if two or more facets tie for largest distance. Denote this map by \(T\).

There are **exactly \(d!\) distinct nonconstant periodic orbits**, all of least period \(d+1\), and no other nonconstant periodic orbits. They are indexed by cyclic orders of the \(d+1\) vertex labels. At a periodic phase with increasing barycentric-coordinate order \((i_0,\ldots,i_d)\), the coordinates are exactly
\[
\lambda_{i_k}=\frac{2k}{d(d+1)},\qquad 0\leq k\leq d.
\]
The next step changes the increasing label order to \((i_d,i_0,\ldots,i_{d-1})\), and all \(d!\) periodic orbits are exponentially attracting in their strict-coordinate-order basins.

Every nonfixed point with any two equal barycentric coordinates reaches a fixed point after finitely many iterations, whereas every point with all barycentric coordinates distinct converges exponentially, phase by phase, to one of the \(d!\) cycles. The fixed points are exactly the points where the largest barycentric coordinate is attained at least twice. In particular, **every invariant Borel probability** has the form
\[
\mu=\eta+\sum_{C\in\mathcal C}w_C\,\nu_C,
\]
where \(\mathcal C\) is the set of \(d!\) cycles, \(\nu_C\) is uniform probability on cycle \(C\), \(w_C\geq0\), and \(\eta\) is any finite positive measure supported on the fixed set with \(\eta(S)+\sum_C w_C=1\). This decomposition is unique. For a uniformly surface-area-distributed starting point, the selected attracting cycle is uniformly distributed among the \(d!\) possibilities.

For a regular tetrahedron, there are precisely **six attracting four-cycles**; at every periodic phase, the two transverse multipliers of the four-step return are
\[
\rho_{\pm}=\frac{-7\pm4\sqrt2\,i}{81},\qquad |\rho_{\pm}|=\frac19.
\]

## Assumptions and scope
Barycentric coordinates \(\lambda_0,\ldots,\lambda_d\) are normalized by \(\lambda_i\geq0\) and \(\sum_{i=0}^{d}\lambda_i=1\). The boundary consists exactly of points with at least one zero coordinate. Every facet is the bounded closed \((d-1)\)-simplex \(F_j=\{\lambda_j=0\}\), and distances are ordinary Euclidean distances to these facets. Orthogonal projection from any point of \(S\) onto the affine hyperplane of \(F_j\) lies in \(F_j\), so using the bounded face or its full supporting hyperplane produces the same map. The tie convention is essential: tied *maximal* distances give a stationary point rather than an arbitrary choice. A cyclic order is a permutation modulo cyclic rotation. Exponential convergence means that along each residue class modulo \(d+1\) the distance to the corresponding phase of the limiting cycle is bounded by a constant times \(q_d^n\) after \(n\) full cycles, for some \(q_d<1\) depending only on the dimension.

## Proof
**1. Exact projection and the maximum-coordinate rule.** A regular simplex has one common altitude \(h>0\). The perpendicular distance of a point to \(F_j\) is \(h\lambda_j\). The perpendicular foot of vertex \(j\) on its opposite facet is that facet's centroid. Since orthogonal projection is affine, projecting a point with barycentric vector \(\lambda\) to \(F_j\) gives
\[
(P_j\lambda)_j=0,\qquad
(P_j\lambda)_i=\lambda_i+\frac{\lambda_j}{d}\quad(i\ne j).
\tag{1}
\]
All entries stay nonnegative and sum to one, proving that the foot belongs to the bounded facet. The dynamical choice is therefore \(T(\lambda)=P_j\lambda\) when \(\lambda_j\) is uniquely maximal; otherwise \(T(\lambda)=\lambda\).

**2. Rank rotation or finite stopping.** If the \(d+1\) coordinates are pairwise distinct, let their increasing label order be \((i_0,\ldots,i_d)\). Equation (1) sets the unique largest coordinate to zero and adds the same positive amount to all the others. The new coordinates are still pairwise distinct and have increasing label order \((i_d,i_0,\ldots,i_{d-1})\). Thus a full \(d+1\)-step itinerary visits each facet once and repeats its label order forever, without encountering a tie. If any two coordinates are equal and are not both maximal, they remain equal until one reaches the maximal rank, since neither is selected before then and they receive identical increments. Every unique maximum outside this equal pair moves to strict minimum; no label can stay ahead of the pair for more than \(d\) such removals. Hence the pair becomes tied for maximum within at most \(d\) moving steps, at which point the point is fixed. Initially tied maxima are already fixed. Conversely, (1) changes the unique maximal coordinate from a positive value to zero, so no point with a unique maximum is fixed. This identifies the fixed set and all finite stopping behavior.

**3. Construction and count of periodic orbits.** Define \(b_k=2k/[d(d+1)]\), for \(0\le k\le d\). These values are strictly increasing, nonnegative, and sum to one. A point with \(\lambda_{i_k}=b_k\) belongs to \(\partial S\). Here \(b_d/d=b_1\), so (1) sends the ordered vector \((b_0,b_1,\ldots,b_d)\) to \((0,b_1,b_2,\ldots,b_d)\) on the labels in the rotated order, because \(b_{k-1}+b_1=b_k\). Thus each cyclic ordering of labels defines a periodic orbit of least period \(d+1\). There are \((d+1)!/(d+1)=d!\) cyclic orders, and their orbits cannot intersect because each periodic phase has a unique strict ordering.

**4. Strict contraction and exhaustive attraction.** Fix an itinerary given by any cyclic order, and consider the composition of its \(d+1\) ordinary affine orthogonal projections onto the corresponding facet hyperplanes. The difference between outputs of two points is the product of the \(d+1\) *linear* orthogonal projections onto the respective parallel tangent hyperplanes. Each factor is nonexpansive in Euclidean norm. Equality of norms through every factor for a nonzero difference vector would require that vector to be tangent to every facet simultaneously. The facet normals of a nondegenerate simplex span \(\mathbb R^d\), so the intersection of their tangent subspaces is \(\{0\}\); equality is impossible. Compactness of the unit sphere therefore gives an operator norm \(q_d<1\). Symmetry permits the same constant for all facet permutations. By Step 2, a strict-order orbit forever follows this single repeated itinerary. Comparing it after each full itinerary with the explicitly constructed cycle phase gives \(\|T^{n(d+1)}x-z\|\le q_d^n\|x-z\|\); the intermediate projections are nonexpansive. Consequently every strict-order orbit converges phase by phase to the unique cycle of its cyclic label ordering. The same estimate rules out any other periodic points.

**5. Stationary probabilities.** A point outside the listed fixed points and periodic orbits is not recurrent. Indeed it either becomes a different fixed point after finitely many steps or approaches a finite periodic orbit from which its initial point is separated by a positive distance. Poincaré recurrence for an invariant Borel probability of a measurable self-map of the compact boundary implies that almost every point is recurrent. Hence every invariant probability is supported on the fixed set and the \(d!\) cycles. Its restriction to any cycle must have equal masses at all phases, since the map permutes those phases cyclically and no other recurrent state contributes to the measure. Its restriction to the fixed set is arbitrary. Conversely all the claimed measures are invariant, proving completeness and uniqueness of the decomposition.

**6. Surface-area basin weights.** On the relative interior of each facet, almost every point has pairwise distinct barycentric coordinates, and every ordering of the remaining \(d\) labels occupies equal facet area by symmetry. The full simplex symmetry group acts transitively on the \(d!\) cyclic-order basins and preserves \((d-1)\)-dimensional surface area. Their union has full boundary surface measure because the equality hyperplanes have zero facet-area measure. Thus every basin receives exactly \(1/d!\) of normalized boundary area.

**7. Explicit tetrahedral multipliers.** For \(d=3\), at the periodic phase \(\lambda=(0,1/6,1/3,1/2)\), the next four target facets are \(3,2,1,0\). The derivative of (1) is the linear map \(M_j\) whose \(j\)-th column is zero in row \(j\) and \(1/3\) elsewhere, with all other columns unchanged from the identity. Multiplying \(M_0M_1M_2M_3\) and restricting to the tangent plane \(\lambda_0=0\), \(\sum_i\delta\lambda_i=0\), in basis \((e_1-e_3,e_2-e_3)\) yields
\[
D(T^4)=\frac1{81}\begin{pmatrix}-7&-4\\8&-7\end{pmatrix}.
\]
Its characteristic polynomial is \(t^2+(14/81)t+1/81\), with roots stated above. Every other tetrahedral cycle is a symmetry image and has the same pair of multipliers.

## Verification
Run `python3 verify.py` using Python 3 and the standard library. It enumerates the \((d+1)!\) labeled orbit phases for each \(d=3,4,5,6\), checks the exact barycentric return identities and strictly rotating facet itinerary using rational arithmetic, exercises nonperiodic rational strict-order points and ties, and recomputes the tetrahedral return matrix, trace, and determinant exactly. Its expected final output is `CHECK_OK`. Exact finite tests validate the formulas but do not establish the all-dimensions theorem; Steps 1–7 provide the proof.

## Relationship to prior work
Everett, *A Piecewise Contractive Map on Triangles* (online January 7, 2021), defines a farthest-perpendicular-projection rule on three complete triangle supporting lines, proves qualitative eventual periodic behavior in the plane, and explicitly asks about the dynamics of higher-dimensional polytopes under farthest-face projection in its closing discussion. The present result addresses that proposed direction for **all regular simplices of dimension at least three**, with an exact factorial orbit classification, explicit coordinates, complete invariant-probability description, and tetrahedral multipliers. It does not claim the general nonregular-polytope problem.

Bédaride and Rao, *Regular simplices and periodic billiard orbits* (arXiv:1112.2370), construct regular-simplex billiard trajectories meeting every facet once, but billiard reflection is not nearest-foot or farthest-foot orthogonal projection. Their face-hitting period can coincide, yet their barycentric formulas and equations of motion differ; in dimension three, their displayed first-type billiard phase has a coordinate tie while the present attracting four-cycle phase has four distinct coordinates. Consequently their theorem does not imply the projection dynamics or its invariant-measure classification. A separately published analysis titled *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map* determines planar three-cycles for three complete supporting lines; those statements likewise neither cover the simplex dimension \(d\ge3\) nor imply the all-dimensional factorial count or stationary-measure classification. Searches for equivalent maximum-coordinate redistribution and cyclic-barycentric formulations did not identify a covering theorem, but an undetected equivalent result remains possible.

## Limitations
The assumption of a **regular** simplex is essential to the equal-altitude/equal-increment rule; no extension to arbitrary simplices or general convex polytopes is proved. If the tie convention is changed, the classification at equality boundaries need not hold. The invariant probabilities described need not be physical limits for a single specified initial point on a tied rank hyperplane. The exponent \(q_d<1\) is certified to exist but not optimized for general dimensions. The result establishes no independent priority or external audit, and it does not classify variable face-weight projections or stochastic facet choices.

## References
1. Samuel Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* **18**(2), 183–192, DOI `10.1080/1726037X.2020.1847765`; publisher online-publication date January 7, 2021. Lawful author preprint arXiv `2408.16019v1` (August 26, 2024), specifically Definition 2.1 and closing discussion.
2. Nicolas Bédaride and Michael Rao, *Regular simplices and periodic billiard orbits*, arXiv `1112.2370v1` (December 11, 2011), especially Sections 3–4.
3. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, mathematical research record `2944d54e59d8` (October 11, 2026). The record's theorem concerns three complete supporting lines in the plane, not the higher-dimensional regular-simplex boundary.
