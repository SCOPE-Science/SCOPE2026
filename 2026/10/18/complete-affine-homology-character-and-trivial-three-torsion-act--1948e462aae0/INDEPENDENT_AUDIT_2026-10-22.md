# Independent mathematical audit

## correctness

PASS

Inspected source RESULT.md and complete verify_paley17.py. Rebuilt all faces of open-neighborhood complex from Q quadratic residues mod17: f=(17,136,612,1122,952,476,136,17), 3468 nonempty. Source program deterministically constructs 1711 Morse pairs, topologically sorts full 15300-incidence graph, leaves one vertex, 5 critical 2-cells, 40 critical 3-cells; exact signed 5x40 Morse matrix has minor det -3 on specified columns, a 4x4 unit det -1, mod3 rank4 and mod2 rank5, hence integral Smith (1,1,1,1,3) and H2=Z/3, H3=Z^35. Read code for independent mod3 cycle/cocycle detection and scalar verification on every 136 affine map: induced torsion scalar +1. Independently enumerated signed fixed-face traces for all 136 affine maps; character values/counts (35:1, 1:16, 3:17, -1:102). Algebraic character is 2 W+E, E inflated C4 augmentation. Important limitation: independent replay did not separately recompute the 5x40 Smith and 136 torsion cocycle action, but algorithm/code was inspected and is finite/exhaustive for the specified graph.

## originality

PASS

Exact prior Paley17 neighborhood homotopy and torsion rank fully credited, but complete Resultary prior text does not determine affine rational character nor torsion action. Jones studies affine maps, Matsushita fundamental groups. Exact same-graph/module searches uncovered no stronger homology-action theorem; equivalent unpublished calculations risk remains.

## value

PASS

The full automorphism action on the 35 rational cycles plus the order-three integral torsion of a canonical strongly regular Paley graph is a natural equivariant refinement of a torsion-containing neighborhood-complex classification; these exact symmetry data are mathematically meaningful for equivariant topology, not arbitrary finite arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
