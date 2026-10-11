# Independent mathematical audit

## correctness

PASS

The package graph model matches the stated non-overlap conditions. There are exactly 216 self-non-overlapping candidates with counts 6,18,48,144 by lengths two through five. The coloring branch-and-bound is an exact clique algorithm: each color is an independent set and therefore gives a rigorous upper bound on every remaining clique branch. Independent reconstruction of the graph and algorithm reproduced clique number 17 and, after forcing each of all 72 short vertices, maximum 16; the supplied 17- and 16-word witnesses were directly rechecked.

## originality

PASS

Prior work gives the fixed-length ternary length-five maximum 17 and a general upper bound saying a variable-length code cannot exceed the corresponding fixed-length maximum, but it does not characterize equality or show that one shorter word forces a drop. The exact forced-short maximum 16 is therefore additional information, and it sharpens the general average-length bound to the exact value five at cardinality 17.

## value

PASS

The result resolves a natural equality case in the variable-length maximum/average-length problem at the first ternary length-five frontier. It is a complete exact finite cutoff tied directly to the general theory, not an arbitrary sample or a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
