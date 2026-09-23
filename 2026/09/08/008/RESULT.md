# Exact illumination numbers of five canonical parallelohedron representatives

## Context

The Hadwiger–Levi–Boltyanski illumination conjecture in `R^3` asks whether every convex body can be illuminated by at most 8 directions; the best known general bound is larger. The five Fedorov classes are the five combinatorial types of three-dimensional parallelohedra. A Fedorov combinatorial type contains non-affinely-equivalent realizations, so affine invariance alone does **not** make illumination number a type invariant. This record therefore makes the exact claim only for the five explicit representatives below (and, automatically, their affine images).

## Definitions

A direction `d != 0` illuminates a boundary point `x` of a convex body `P` if `x+t d` lies in the interior of `P` for all sufficiently small `t>0`. For a polytope it suffices to illuminate every vertex: if the outward normals of facets incident to vertex `v` are `n_1,...,n_k`, then `d` illuminates `v` exactly when `<d,n_i><0` for every incident facet. The illumination number `ill(P)` is the minimum number of directions covering all vertices. It is invariant under invertible affine maps.

Two vertices conflict if no single direction illuminates both. A pairwise-conflicting `k`-set forces `ill(P)>=k`. Equivalently, feasibility of a common illuminating direction can be decided exactly by the Gordan alternative.

## Result

For the following **displayed representatives**, the exact illumination numbers are:

| representative / Fedorov combinatorial type | construction | V | E | F | ill |
|---|---|---:|---:|---:|---:|
| cube / parallelepiped | zonotope `<(1,0,0),(0,1,0),(0,0,1)>` | 8 | 12 | 6 | **8** |
| hexagonal-prism representative | zonotope `<(1,0,0),(0,1,0),(1,1,0),(0,0,1)>` | 12 | 18 | 8 | **6** |
| rhombic-dodecahedron representative | zonotope `<(1,0,0),(0,1,0),(0,0,1),(1,1,1)>` | 14 | 24 | 12 | **6** |
| elongated-rhombic-dodecahedron representative | zonotope `<(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,1,1)>` | 18 | 28 | 12 | **5** |
| truncated-octahedron representative | convex hull of signed permutations of `(0,1,2)` | 24 | 36 | 14 | **4** |

Their facet-shape censuses are respectively: 6 quadrilaterals; 6 quadrilaterals plus 2 hexagons; 12 quadrilaterals; 8 quadrilaterals plus 4 hexagons; 6 quadrilaterals plus 8 hexagons.

Explicit attaining integer direction sets are:

- cube: all `(±1,±1,±1)`;
- hexagonal-prism representative: `(1,2,1),(1,2,-1),(1,-1,1),(1,-1,-1),(-2,-1,1),(-2,-1,-1)`;
- rhombic-dodecahedron representative: `(1,2,2),(1,1,0),(1,-2,2),(1,-1,-2),(-2,1,-1),(-2,-2,-1)`;
- elongated-rhombic-dodecahedron representative: `(1,2,2),(1,2,-3),(1,-3,2),(1,-3,-3),(-3,-2,-1)`;
- truncated-octahedron representative: `(1,1,-1),(1,-3,3),(-3,1,3),(-3,-3,-2)`.

## Proof / evidence

For each representative, exact integer dot products verify that every vertex is illuminated by at least one direction in the displayed set, giving the upper bound.

Two independent lower certificates agree. First, the vertex-conflict graph has a clique of size `8,6,6,5,4` respectively, with each pair checked by an exact `0`-in-convex-hull test. Second, all strict sign patterns over the facet normals are enumerated: realizable sign cells give every possible set of vertices that any real direction can illuminate. The numbers of feasible cells are `8,12,24,24,32`, and exact set cover on these cells has optima `8,6,6,5,4`. Thus the lower bounds range over **all real directions**, not merely a sampled direction pool.

An independent audit rebuilt the five coordinate polytopes, recomputed the facet censuses and complete sign-cell set-cover optima, and obtained the same values. It also identified and removed the earlier unsupported inference from these representatives to every realization of their Fedorov combinatorial types.

## Limitations

- The theorem is for the five stated representatives and their affine images. Fedorov type is combinatorial, and non-cube types have non-affinely-equivalent realizations; no constancy of illumination number across an entire type is proved here.
- Type identification rests on the stated constructions together with the verified vertex/edge/facet and facet-polygon counts, rather than a separate full face-lattice certificate.
- Lower-bound completeness is computational, though exact and replayable.
- No claim about the general Hadwiger illumination conjecture is made.

## Reproducibility

Run `python3 artifacts/verify_illumination.py`. The stdlib-only verifier rebuilds the representatives, checks their Euler/facet data, replays every strict-dot witness, checks conflict cliques, enumerates feasible sign cells, and recomputes the exact set-cover optima. Expected output ends with `ALL FIVE TYPES VERIFIED`; that historical message refers to the five displayed representatives and should not be read as a proof of type-wide invariance.

## References

- A. Prymak, V. Shepelska, *On the Hadwiger covering problem in low dimensions*, arXiv:1811.08962.
- K. Bezdek, M. A. Khan, *The geometry of homothetic covering and illumination*, arXiv:1602.06040.
- W. R. Sun, B.-H. Vritsiou, *Illuminating 1-unconditional convex bodies in R^3 and R^4*, arXiv:2407.11331.
- L. Rotem, A. Schejter, B. A. Slomka, *The Complex Illumination Problem*, arXiv:2410.12021.
- R. T. Zivaljevic, *Illumination complexes, Delta-zonotopes, and the polyhedral curtain theorem*, arXiv:1307.5138.
