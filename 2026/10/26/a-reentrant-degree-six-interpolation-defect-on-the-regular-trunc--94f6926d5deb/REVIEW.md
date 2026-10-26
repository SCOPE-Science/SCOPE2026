# Scientific review

## Correctness (PASS)

The exact object is the twelve-point tetrahedral orbit of normalized signed permutations of \((3,1,1)\), with sign product positive. The addition theorem equates the exact-degree evaluation rank to the rank of the rational Legendre Gram matrix. The finite-field certificate for degrees \(0\)–\(324\) proves nonzero rational minors; the three independent rational degree-six null vectors provide the matching rank-nine upper bound. A self-contained integral estimate plus rational trigonometric bounds proves strict diagonal dominance for all degrees \(\ell\ge325\). The nearby-deformation assertion follows because the degree-six determinant is a nonzero rational function of the deformation parameter. The complete `verify.py` file was executed successfully. Computational checking is finite, and the infinite-range conclusion explicitly uses an analytic inequality.

## Originality (PASS, with bounded-literature risk)

The primary source by Krčmár–Gendiar–Nishino (arXiv:1512.09059, Section II and Table I) describes precisely twelve truncated-tetrahedral spin directions, but its claims concern thermodynamic phase diagrams, not the rank of Legendre evaluation matrices. The full text was examined for harmonic or interpolation results. Zhou–Chen (arXiv:1502.03562) addresses spherical design accuracy and polynomial approximation, and Misner (arXiv:gr-qc/9910044) addresses harmonic extraction on cubic grids; neither supplies this all-degree rank sequence. An–Chen–Sloan–Womersley (DOI:10.1137/100795140) concerns well-conditioned spherical designs of degree-at-most spaces; only abstract-level text was accessible in this comparison, so hidden overlap cannot be excluded. Targeted mathematical-record searches for the truncated tetrahedron, degree-six rank-nine deficiency, exact-degree interpolation and equivalent Legendre Gram formulations found no stronger covering statement. Previously accessible research claims on the truncated octahedron, dodecahedron, icosahedron and related root sets concern different point configurations; their results do not imply this twelve-node classification. The search cannot prove universal priority.

## Mathematical value (PASS)

The regular truncated tetrahedron is a canonical Archimedean configuration and a standard twelve-direction symmetric spin discretization. Exact harmonic degree, rather than cumulative polynomial degree, determines whether angular data can be freely prescribed in a single-frequency representation. The complete infinite rank law includes a reentrant fall from rank \(11\) at degree \(5\) to rank \(9\) at degree \(6\), then persistent full rank at degree \(7\); three explicit obstructions and local disappearance under nonuniform truncation reveal a geometric resonance rather than a generic dimension count. This is a natural complete classification with an intrinsic sampling interpretation. No broad approximation or numerical stability theorem is claimed.

## Limits and closest literature

The closest exact geometric source is Krčmár–Gendiar–Nishino, arXiv:1512.09059 (2015). The most relevant methodological source is An–Chen–Sloan–Womersley, DOI:10.1137/100795140 (2010). These sources do not yield the precise stated fixed-degree rank sequence in the inspected material, but the second was available only at abstract level. Possible independent derivations through finite-group representation theory or unindexed appendices remain the main novelty risk. The proof is fully reproducible but has not been independently checked.

Self-review: passed. Independent audit: not yet performed.
