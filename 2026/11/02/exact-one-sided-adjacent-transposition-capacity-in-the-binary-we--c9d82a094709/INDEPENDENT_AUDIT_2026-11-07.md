# Independent mathematical audit

## correctness

PASS

An output for a weight-two (i,j) is the same pair, or (i-1,j) if i>0, or (i,j-1) if j>i+1. Intersection of balls iff the coordinate difference is one of six nearest-neighbor displacements of the triangular grid. The residue i+2j mod3 is an independent coloring; color 2 has floor(n(n+1)/6) vertices. Each three-top-row strip S_m admits exactly m triangles and edge+singleton cliques, bounding an independent set by m+2, and induction using n-3 closes the upper bound; n=2,3,4 bases checked. Independent exhaustive maximum independent set search verified n=2..9.

## originality

PASS

Best-of-knowledge new stated claim after primary statement/implication comparisons and a Resultary search: An optimum for a bidirectional channel does not imply the one-sided optimum: error balls shrink and feasible packings enlarge. Generic asymptotic redundancy bounds neither imply the exact floor(n(n+1)/6) equality nor its all-size sharp strip construction.

## value

PASS

Determines the exact finite-blocklength unique-decoding capacity of an asymmetric one-step timing-error channel in a natural constant-weight layer, with a simple explicit optimal code and bounded-work decoder for every n. Different behavior from the much-studied two-direction shift makes the sharp answer genuinely informative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
