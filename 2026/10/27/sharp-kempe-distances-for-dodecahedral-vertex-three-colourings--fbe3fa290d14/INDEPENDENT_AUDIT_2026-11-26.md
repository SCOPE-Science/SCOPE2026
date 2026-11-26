# Independent mathematical audit

## correctness

PASS

Independently enumerated the proper labelled assignments by taking the Cartesian product of colourings of the outer 10-cycle and two inner 5-cycles and filtering the spoke conflicts. This decomposition accounts for every edge and exhausts all assignments. Inner odd cycles force all colours, making the quotient projection exactly six-to-one. A bit-set connected-component closure enumerated all swaps for each colour pair; projecting every labelled edge gives the quotient, dropping loops and duplications. Both adjacencies were checked for symmetry, and all-source unweighted shortest-path distances independently gave the frozen exact numbers. In labelled and quotient order the state/edge counts are (7200,36120) and (1200,5360), radii 7 and 6, diameters 8 and 7, respectively. Degree counts are {10:6960,11:240} and {8:140,9:1020,10:20,11:20}; eccentricity counts are {7:5280,8:1920} and {6:460,7:740}. Finite distances from every source establish connectedness. The quotient is by colour names alone, not by automorphisms of the underlying polyhedron.

## originality

PASS

Prior work covers connectivity, shortest-sequence methods for other graph families, and different exact Kempe graphs. The supported distinct claim is the matched pair of sharp distance profiles and associated adjacency censuses for dodecahedral vertex colourings, not connectivity or mere evaluation of a colouring count. Bounded searches cannot rule out unpublished calculations.

## value

PASS

The dodecahedron is a canonical cubic planar graph, and shortest single-component Kempe sequences are a standard metric problem independent of this computation. The sharp worst-case lengths and complete eccentricity counts are usable benchmarks for shortest-sequence methods; a researcher can also quantify exactly how permitting arbitrary palettes at the endpoints changes the metric. This goes beyond both known connectivity and a lone chromatic count. No generalization from one graph is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
