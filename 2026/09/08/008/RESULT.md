# Exact illumination numbers of the five Fedorov parallelohedra

## Context

The Hadwiger–Levi–Boltyanski illumination conjecture in $\mathbb{R}^3$
asserts every convex body can be illuminated by at most $8$ directions; the
best known general bound is $H_3 \le 16$ (Papadoperakis, via Prymak–Shepelska).
The five Fedorov types are the complete finite classification of
3-dimensional parallelohedra (space-tiling centrally symmetric polytopes),
all realizable as zonotopes. Exact illumination numbers for these types give
concrete data points calibrating the $H_3 \le 16$ vs conjectured-$8$
boundary. No prior source gives exact real illumination numbers for any
non-cube Fedorov type.

## Definitions

Illumination is in the Boltyanski sense: a direction $d \ne 0$ illuminates a
boundary point $x$ of a convex body $P$ if $x+td$ lies in the interior of $P$
for all sufficiently small $t>0$. The illumination number $\mathrm{ill}(P)$
is the least number of directions illuminating every boundary point.
For a polytope it suffices to illuminate all vertices: a vertex $v$ with
incident facet outward normals $n_1,\dots,n_k$ is illuminated by $d$ iff
$\langle d,n_i\rangle < 0$ strictly for every $i$.
Illumination numbers are invariant under invertible affine maps.
Two vertices conflict if no single direction illuminates both, i.e. $0$ lies
in the closed convex hull of the union of their incident-normal sets
(Gordan alternative). A pairwise-conflicting $k$-set forces
$\mathrm{ill} \ge k$.

## Result

With the explicit integer-coordinate representatives below, the exact
illumination numbers of the five Fedorov 3-dimensional parallelohedra are:

| type | representative | $V$ | $E$ | $F$ | $\mathrm{ill}$ |
|---|---|---|---|---|---|
| parallelepiped (cube) | zonotope $\langle(1,0,0),(0,1,0),(0,0,1)\rangle$ | 8 | 12 | 6 | **8** |
| hexagonal prism | zonotope $\langle(1,0,0),(0,1,0),(1,1,0),(0,0,1)\rangle$ | 12 | 18 | 8 | **6** |
| rhombic dodecahedron | zonotope $\langle(1,0,0),(0,1,0),(0,0,1),(1,1,1)\rangle$ | 14 | 24 | 12 | **6** |
| elongated rhombic dodecahedron | zonotope $\langle(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,1,1)\rangle$ | 18 | 28 | 12 | **5** |
| truncated octahedron | $\mathrm{conv}$ of signed permutations of $(0,1,2)$ | 24 | 36 | 14 | **4** |

Facet shapes: cube 6 quadrilaterals; hexagonal prism 6 quadrilaterals +
2 hexagons; rhombic dodecahedron 12 rhombi (quadrilaterals); elongated
rhombic dodecahedron 8 quadrilaterals + 4 hexagons; truncated octahedron
6 squares + 8 hexagons. All $(V,E,F)$ satisfy Euler's formula.

Explicit attaining integer direction sets:

- Cube, 8: all $(\pm1,\pm1,\pm1)$.
- Hexagonal prism, 6: $(1,2,1)$, $(1,2,-1)$, $(1,-1,1)$, $(1,-1,-1)$,
  $(-2,-1,1)$, $(-2,-1,-1)$.
- Rhombic dodecahedron, 6: $(1,2,2)$, $(1,1,0)$, $(1,-2,2)$,
  $(1,-1,-2)$, $(-2,1,-1)$, $(-2,-2,-1)$.
- Elongated rhombic dodecahedron, 5: $(1,2,2)$, $(1,2,-3)$, $(1,-3,2)$,
  $(1,-3,-3)$, $(-3,-2,-1)$.
- Truncated octahedron, 4: $(1,1,-1)$, $(1,-3,3)$, $(-3,1,3)$,
  $(-3,-3,-2)$.

## Proof / Evidence

Upper bounds: for each type, every vertex cone satisfies
$\langle d,n\rangle<0$ strictly (integers) for at least one claimed
direction $d$; replayed by exact integer-dot checks in the artifact.

Lower bounds (two independent certificates, both verified):

1. Pairwise-conflict cliques of sizes $8,6,6,5,4$ respectively (maximum
   over the conflict graph), each pair verified exact by a
   $0$-in-closed-convex-hull test.
2. Complete optimum over ALL real directions: enumerate all $2^F$ strict
   sign vectors over facet normals; feasible cells (Gordan: $0 \notin$
   closed convex hull of signed rows) give every realizable illuminated
   vertex set (8, 12, 24, 24, 32 feasible cells respectively); exact
   set-cover optima are $8,6,6,5,4$. Hence no direction outside any sampled
   pool can improve the bound.

The auditor re-ran the verifier (`ALL FIVE TYPES VERIFIED`), independently
replayed all strict-dot upper bounds, recomputed the facet-polygon census,
and recomputed all optima and maximum cliques with a corrected exact
$0$-in-convex-hull predicate (exact $4\times 4$ rational simplex solve);
all claimed values were confirmed unchanged.

## Limitations

- Proved for the stated integer representatives; values attach to Fedorov
  types by affine invariance. No wider uniformity (e.g. over all affine
  images or all 3-zonotopes) is claimed.
- Type identification rests on the stated constructions plus verified
  $(V,E,F)$ and facet-polygon census, not a full face-lattice isomorphism
  certificate against external references.
- Lower-bound completeness rests on exact rational computation
  ($2^F$ Gordan enumeration plus set cover), replayable via the artifact,
  rather than a human-readable inequality chain.
- No claim about Hadwiger's conjecture in general; these are five exact
  data points.

## Reproducibility

Run `python3 artifacts/verify_illumination.py` (stdlib only, seconds).
It rebuilds the polytopes, rechecks Euler data, replays every strict-dot
witness, re-verifies every clique pair, and recomputes the complete cell
optima. Expected output ends with `ALL FIVE TYPES VERIFIED`.

## References

- A. Prymak, V. Shepelska, On the Hadwiger covering problem in low
  dimensions, arXiv:1811.08962. General bound $H_3\le 16$; no per-type
  exact values.
- K. Bezdek, M. A. Khan, The geometry of homothetic covering and
  illumination, arXiv:1602.06040. Survey; no five-type table.
- W. R. Sun, B.-H. Vritsiou, Illuminating 1-unconditional convex bodies in
  $\mathbb{R}^3$ and $\mathbb{R}^4$, arXiv:2407.11331. Disjoint
  coordinate-sign-invariant family; no Fedorov exact values.
- L. Rotem, A. Schejter, B. A. Slomka, The Complex Illumination Problem,
  arXiv:2410.12021. Complex ($C^n$) setting; nothing about real Fedorov
  numbers.
- R. T. Zivaljevic, Illumination complexes, $\Delta$-zonotopes, and the
  polyhedral curtain theorem, arXiv:1307.5138. Fair-division use of
  $\Delta$-zonotopes; no real illumination numbers.
