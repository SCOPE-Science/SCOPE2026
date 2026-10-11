# Scientific review

## Correctness
PASS. Connected incidence matrices have rank one less than the vertex count. For a cactus, edge-disjoint semi-balanced cycle dependencies form the entire affine kernel, so the root-polytope configuration is an affine join. Each balanced cycle factor is a free sum of two \((k-1)\)-simplices, each with uniquely centered asymmetry \(k-1\). A direct join barycentric-coordinate argument gives the global lower bound, explicit center, and uniqueness; the distinct-edge reflection identities give a constructive sharp upper bound. The exact-rational standard-library verifier passes 270 cases and 3,685 vertex reflection identities, without being mistaken for an infinite proof.

## Originality
PASS within the inspected evidence, subject to priority risk. The nearest published mathematics is Kálmán–Tóthmérész, arXiv:2105.00960, which proves the semi-balanced affine cycle structure and studies Jaeger dissections and Ehrhart data; Numata–Takahashi–Tamaki, arXiv:2203.14521, which studies face structure; and Kálmán–Tóthmérész, arXiv:2203.17127, which studies \(h^*\)-polynomials. A published oriented-cycle published-finding corpus finding gives Ehrhart formulas and is confined to cycles. Their inspected results supply ingredients, not a stronger Minkowski asymmetry formula, the cactus-wide center classification, or the exact reflection certificate. Earlier general convexity work on joins or signed edge polytopes could independently imply this classification; targeted searches did not resolve that global possibility.

## Value
PASS. The theorem classifies a classical affine invariant for a natural infinite class of graph polytopes. It distinguishes bridge and cycle edge contributions by a rigid two-to-one center weight ratio, identifies an orientation-insensitive exact asymmetry law across arbitrarily many disjoint cycles and bridges, proves center uniqueness, and gives constructive sharpness certificates. This is more than finite enumeration, a renaming, or an isolated small numerical improvement; the result does not assert a general graph theorem beyond the cactus class.

## Boundaries
Graphs with edge-overlapping cycles do not have the required direct-sum cycle kernel. Zero-dimensional one-edge cases are excluded. Searches do not prove global novelty. Independent publication-priority review and independent verification remain outstanding.

Same-model review: passed. Independent audit: not yet performed.
