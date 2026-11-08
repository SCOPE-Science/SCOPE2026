# Independent mathematical audit

## correctness

PASS

Every triangle is a coordinate line. Complementing the set converts the problem to a minimum-plus-one line-hitting set B of size 3^(n-1)+1. For each of n directions exactly one line is doubled and all others meet B in one point. Each two-coordinate face contains >=3 points and exactly one contains four, forcing all doubled lines through a common anchor v. Deleting v if v in B yields the unique exact transversal. If v is absent, each of its 2n distance-one points belongs to B, no distance-two point can belong, and in every coordinate 3-face four of eight distance-three corners must form one signed parity class. Any four-face then must have four weight-four members, while all four parity constraints force at most one signed corner, contradiction for n>=4. In n=2 and n=3 the remaining local hole patterns have exactly 9 and 54 nonextendible sets. Maximal exact-one-per-line sets over F3 are nonzero-coefficient affine hyperplanes because every order-three Latin square is affine. Count (3*2^(n-1))*(2*3^(n-1))=6^n completed cases; n=2,3 add the exceptional holes. Independently enumerated original line-hitting subsets n=2 and n=3 and maximal completion counts 45/36/9 and 270/216/54. Finite testing corroborates the dimension-free local-to-global parity proof, not vice versa.

## originality

PASS

Best-of-knowledge: actual Resultary semantic queries and primary published mathematical statements were compared by object, hypotheses and implications; no source inspected established this entire additional conclusion. The four explicit comparisons, source inspections and residual risks below qualify historical priority; inaccessible full texts alone do not count as disproof.

## value

PASS

A sharp stability/rigidity theorem immediately below a natural Hamming-graph triangle-free extremum, identifying a four-coordinate obstruction, unique completion at n>=4 and complete small-dimensional exceptions. Counting near-extremizers alone would not supply this structural dichotomy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
