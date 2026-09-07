# Exact general-position rectilinear crossing number of K(5,7) is 36

## Context
Topological crossing numbers cr(K(5,n)) are settled by Kleitman at the Zarankiewicz number Z(5,n), so cr(K(5,7))=36 is textbook. General-position rectilinear (straight-line) numbers bar-cr(K(5,n)) remain uncertified table entries citable for graph-drawing and VLSI benchmarks. K(5,7) has 12 vertices, 35 edges, 595 edge pairs, with order-type search feasible, while larger strata are harder. Closing K(5,7) bridges Kuratowski planarity and Zarankiewicz-type bounds with a concrete millisecond-recheckable drawing.

## Definitions
Let K(m,n) have parts A,B with |A|=m, |B|=n and all A-B edges. A rectilinear general-position drawing is a choice of |V| distinct points in R^2, no three collinear, each edge drawn as the open straight segment between endpoints. Its rectilinear crossing number is the number of unordered disjoint edge pairs whose open segments meet; pairs sharing an endpoint are not counted. Let bar-cr be the minimum over such drawings; let cr be the topological minimum over curved drawings. Then bar-cr >= cr. Zarankiewicz number Z(m,n)=floor(m/2)*floor((m-1)/2)*floor(n/2)*floor((n-1)/2). For (5,7), Z=2*2*3*3=36.

## Result
Theorem. bar-cr(K(5,7)) = 36.

## Proof / Evidence
Lower bound (cited). Kleitman proves cr(K(5,n))=Z(5,n). For n=7, Z=36. Since every rectilinear drawing is a topological drawing, bar-cr(K(5,7)) >= 36. This audit verifies the citation metadata (Crossref title The crossing number of K5,n, 139 citations, doi:10.1016/S0021-9800(70)80087-4) and the arithmetic Z=36; it does not re-prove Kleitman.

Upper-bound witness (new, computed, independently verified). Points (integers, bounding box [0,40]^2):
A (5): (9,24), (16,9), (22,8), (1,40), (29,6)
B (7): (13,19), (39,3), (4,7), (9,17), (26,7), (20,11), (0,0)
Stored in coords_K57_rect.json. All 12 points distinct; all C(12,3)=220 orientation determinants orient(p,q,r)=(q_x-p_x)*(r_y-p_y)-(q_y-p_y)*(r_x-p_x) are nonzero by exact integer arithmetic, so no three collinear and no vertex lies on a non-incident edge.

Edges: 35. Total pairs C(35,2)=595. Disjoint pairs (no shared endpoint): 420=C(5,2)*C(7,2)*2. Underlying 2+2 quads: 210, each with at most one crossing. Proper crossing for disjoint (a,b),(c,d) by strict orientation signs: (o(a,b,c)>0)!=(o(a,b,d)>0) and (o(c,d,a)>0)!=(o(c,d,b)>0); in general position no orientation is zero. The witness has exactly 36 crossing disjoint pairs (36 quads with one crossing), listed in crossing_list.csv. Quad-type audit: 36 convex non-alternating (exactly the crossing quads), 42 convex alternating (none cross), 132 non-convex (none cross).

Two independent exact counts agree: verify_rect.py (orientation-sign method) and verify_rect_second.py (rational parametric solve a+t(b-a)=c+s(d-c) over Fraction, check 0<t,s<1), both 36. verify_planarity.py recomputes rotation by polar angle, recounts 36, matches stored crossing set, and checks over Fraction that the 36 intersections are pairwise distinct (no triple concurrency).

Topological control. The same straight-line drawing viewed topologically has 36=Z(5,7) crossings, so it is also a topological optimum witness. rotation_K57_36.json stores its rotation system (neighbors in atan2 order). verify_planarity.py checks rotation consistency and enumerates all C(5,3)*C(7,3)=350 induced K(3,3)s, each 6 vertices / 9 edges violating bipartite planarity e<=2v-4=8, hence K(5,7) nonplanar. Full cr>=36 is not proved by this script; it is cited from Kleitman. This control guards against miscounting.

How found (computed evidence, not proof). Uniform random 12-sets on [0,30]^2 filtered by general position with exact orientation count; best of 20k was 40; single-point annealing reached 38 then 36 within ~600 steps. Search code was ephemeral and is not part of the certificate; the certificate is coordinates plus verifiers.

## Limitations
- Lower bound relies on external Kleitman theorem; no new rectilinear branch-and-bound was needed because the topological bound is tight; deviation from rotation/B&B route is intentional.
- Upper bound is a single integer witness; minimality among rectilinear drawings follows only via cited lower bound; no enumeration of order types claimed.
- No claim of uniqueness or minimal coordinates; no claim beyond independent machine-checkable 36-witness (if a 36-witness appeared elsewhere, this is a reproduction).
- Observed (uncertified) annealing also attains Z for (5,5),(5,6),(5,8); conjecture bar-cr(K(5,n))=Z(5,n) for this band, but only (5,7) is proved here.
- General position means vertices only; edge-triple concurrency happens to be absent here (checked), so no counting ambiguity.

## Reproducibility
Stdlib Python 3.12.3 only, seconds:
bash output/artifacts/rerun.sh
- verify_rect.py -> 0 collinear, 595 total, 420 disjoint, 36 cross, Z=36, PASS
- verify_rect_second.py -> 36, PASS
- verify_planarity.py -> rotation PASS, 36 crossings, 350 K3,3, 36 distinct points, PASS
Hashes (sha256): coords_K57_rect.json d1edb9b7f1cd0727d37d8344541950cf4b1361ec45805c59ae9c4dc0ef54bccf; rotation_K57_36.json 0e8a03ac3627e6dc40be0d3d73948ddbcd7a5a435af7d007844b518444635156; crossing_list.csv befabd4f6017f3b36eb245e9d47a87ef82881aff69fa60957ffb8ade0f54dbbd; verify_rect.py 1c1c08c4cda2ef3136b220aaaea36382d6e9b403a9b810adc8a3618f858d67cc; verify_rect_second.py 2ffa6f839d6db114f024f3d06b0727afb90151f6ebef3126ad7e1d7af3b149f9; verify_planarity.py a307922e6911358b7d661e491760244f417ff24d624c9bea68a92cfb7ab2ed8c.

## References
[1] D. J. Kleitman, The crossing number of K(5,n), J. Combin. Theory 9 (1970), 315-323. https://doi.org/10.1016/S0021-9800(70)80087-4 - gives cr(K(5,n))=Z(5,n), hence 36 for n=7.
[2] M. Nafar, Rectilinear crossing number of the double circular complete bipartite graph, arXiv:2310.15882 (2023) - restricted to two concentric circles, different counting/optimization; no general-position K(5,7) coordinates. https://arxiv.org/abs/2310.15882
[3] O. Abrego et al., The bipartite-cylindrical crossing number, Graphs Combin. - cylindrical, not straight-line plane. https://doi.org/10.1007/s00373-019-02076-5
[4] E. Feder, D. Garber, On the Orchard crossing number of K(n,n), arXiv:1008.2638 - different line-separation definition, K(n,n) only. https://arxiv.org/abs/1008.2638
[5] R. Fabila-Monroy, J. Lopez, Computational search of small point sets with small rectilinear crossing number, J. Graph Algorithms Appl. 18 (2014), 393-399. https://doi.org/10.7155/jgaa.00328 - searches Kn point sets, not bipartite 5+7 stratum.
