# Independent mathematical audit

## correctness

PASS

The literal GP(10,2) adjacency has 20 vertices, 30 edges, degree three. Exhaustive independent BFS/Euler acyclicity analysis tested all 2^20=1,048,576 vertex masks and obtained exact k=0..14 forest coefficients [1,20,190,1140,4845,15492,38580,76260,120540,151920,150480,113400,60620,19600,2520], with zero k≥15 and sum 755,608. Exactly 2520 forests have order14; 1860 are trees, 660 have component sizes (1,13):280,(2,12):180,(4,10):120,(6,8):60,(7,7):20. All inclusion-maximal induced forests have order 13 (1120) or 14 (2520). Independent adjacency-preserving bijection enumeration found exactly 120 automorphisms. The 25 literal CSV representatives generate disjoint orbits covering all 2520 optimum masks, orbit sizes 120×18+60×5+40+20. These computations exhaust the FINITE graph only.

## originality

PASS

The classical 14-vertex induced forest and decycling number six are already in literature and explicitly NOT claimed as new. Prior survey/planar/girth-five works and generalized Petersen decycling-number papers emphasize a single extremal size, not the full coefficient polynomial, inclusion-maximal profile, component partition or 25 orbit classes. Resultary returned dodecahedral independence/matching complex invariants but no same induced-forest polynomial. Full Gao and Wei–Li articles were inaccessible; residual priority risk retained.

## value

PASS

The dodecahedron is the canonical 20-vertex cubic girth-five graph and a sharpness case for induced-forest bounds; its complete induced-forest polynomial, exact optimum component distribution, minimal feedback set profile and automorphism orbit census form a natural, reusable extremal benchmark. Exhaustive independently verified enumeration is a legitimate finite classification, not merely recomputation of already-known α_f=14.

The dated certificate retains the supplied scientific assessment, sources and limitations.
