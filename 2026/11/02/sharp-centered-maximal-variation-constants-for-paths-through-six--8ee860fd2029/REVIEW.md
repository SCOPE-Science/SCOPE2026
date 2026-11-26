# Independent mathematical audit

## correctness

PASS

Passing to absolute input values cannot increase input variation. On nonnegative data use increments and translate the auxiliary vector of partial sums: adding a constant to all entries adds the same constant to every linear ball average and its maximum, and every real increment vector has a nonnegative representative. In each orthant on the l1=1 section, the equalities between ball forms, and coordinate hyperplanes, subdivide the simplex into compact polytopes. The maximizing form at each vertex of the path is fixed on each cell, so output variation is convex on that cell and bounded by its values at the cell vertices. A cell vertex requires n-2 independent active homogeneous equations in addition to the section equation; each is therefore the normalization of one of the two orientations of a rank-(n-2) intersection line. Ties and boundary supports are included. Independently replayed with own standard-library code at /workspace/path_variation_replay.py (python3 /workspace/path_variation_replay.py 5 6), deriving clipped balls from intervals, computing null lines by integer elimination, and evaluating each orientation with prefix sums and exact inequalities, with no frozen scripts executed. For n=5: 27 normals, 2829 full-rank triples, 1448 distinct oriented rays, 2 distinct equality orientations, max 4/5. For n=6: 46 normals, 151429 full-rank quadruples, 43756 distinct oriented rays, 2 distinct equality orientations, max 5/6. The distinct-ray counts do not count repeated intersections, unlike the frozen counters. The endpoint impulse attains exactly 1-1/n since its maximal profile increases from 1/n to 1. The C++ file named in RESULT.md is absent from the supplied support; the inspected Python support and the independently generated exhaustive replay leave no reliance on the claimed C++ execution.

## originality

PASS

The values were conjectured; the primary source explicitly distinguishes numerical evidence from a guaranteed global maximum, and the closest earlier proofs apply only to restricted input shapes or different graphs or objectives. The claim credited here is the exact upper bound for arbitrary data on the two specified paths, not the conjecture, impulse lower bound, or a claim for n>=7.

## value

PASS

These are the first two orders beyond the published exact small-path cases, where the conjecture allowed arbitrary oscillatory inputs and numerical optimization did not certify completeness. An exact all-input finite proof answers a motivated gap at those orders, and distinguishes the conjectured coefficient from an observed numerical value. No claim about larger orders or every extremizer is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
