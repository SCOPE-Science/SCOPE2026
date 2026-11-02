# Independent mathematical audit

## correctness

PASS

The exact 24-vertex 36-edge (12,7,-7) LCF graph and independent-set recursion were inspected. Fresh exhaustive independent-set generation gave size vector (1,24,240,1304,4212,8328,10024,7072,2668,424,8), proving alpha=10. All legal moves on the 424 nine-sets and eight ten-sets were reconstructed from symmetric differences and checked with all-pairs BFS: TJ_9 has 1428 edges, one 424-component and eccentricity counts 9:32,10:368,11:24; TS_9 has 1068 edges, components 416+2+2+2+2; at ten both move models have two four-cycles and eight edges. The enumeration domain and adjacency definition are exhaustive, not sampled.

## originality

PASS

Bonsma–Kamiński–Wrochna (2014), Proposition 1, proves the general identity TJ_alpha(G)=TS_alpha(G), which is acknowledged. The Resultary 2026 McGee independence-complex result already gives all independent-set counts, including 424 and eight; these counts are also acknowledged. Neither supplies the exact reconfiguration edges, 9-layer connectivity transition, or diameters. Published exact graph-specific reconfiguration tables may exist outside the inspected corpus.

## value

PASS

At the natural maximum independent-set boundary, an exact change in connectedness between sliding and jumping and two nontrivial frozen components of maximum configurations reveal structure absent from independence polynomials or alpha alone. Complete radii/diameters and component classes are independently useful finite graph-reconfiguration invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
