# Mathematical review

## Correctness — PASS

The argument determines the unique central socle \(C=\mathbf F_qE_{14}\) and proves every additive two-sided ideal either lies in \(C\) or contains \(C\); the quotient \(R/C\) has two-dimensional square-zero product image. Every quotient ideal is reconstructed as an additive graph over its projected subspace, with all two-sided closure constraints explicitly enumerated. Gaussian coefficients and graph-map counts give the all-prime-power polynomial. Two standalone checkers enumerate the actual ideals at prime-field orders \(2,3\) and at extension-field order \(4\), including direct closure tests and scalar-linearity comparison. Boundary cases \(m=1\), the zero ideal and whole ring are included. Finite checks alone would not prove the theorem; the argument does.

## Originality — PASS, with residual literature risk

The closely matching Marberg study (arXiv:1005.4150) classifies supernormal groups and obtains a counting formula when the field order is prime; hence its prime-field case is prior art. The new claimed invariant is the complete prime-subfield-additive ideal-size polynomial over arbitrary extension fields, not the known scalar-linear or prime-field enumeration. The 2018 skew-brace study (arXiv:1804.04106) defines and examines the appropriate ideal notion but does not present this polynomial in its inspected main text. Semantic result-index searches for aliases, ordinary/Lie versus associative ideals, nonprime field cases and exact finite counts found no dominating statement. An unindexed equivalent formula remains a residual risk; unavailability of universal literature coverage is not asserted as novelty proof.

## Value — PASS

The natural notion of ring/brace ideal requires additive rather than full field-linearity, and extension fields create many non-scalar subgroups. The polynomial measures the complete size distribution uniformly for all field characteristics and degrees. Its first extension-field instance identifies a substantial difference—\(3011\) additive ideals versus \(59\) scalar-linear ideals over \(\mathbf F_4\)—and gives explicit sizes, useful for ideal-lattice, radical-brace and supernormal-subgroup comparisons. This is a complete intrinsic invariant rather than an arbitrary finite census.

## Evidence and limitations

The explicit four-case matrix multiplication, Gaussian subspace counts and graph-map multiplicities are self-contained in `RESULT.md`. Standalone programs `verify_gf4.py` and `verify_prime.py` reproduce the finite cases. Theorem does not count all group normal subgroups and does not extend to larger matrix sizes. The exact primary-literature dates are the initial arXiv posting of arXiv:1804.04106 (2018-04-11), and Marberg's arXiv:1005.4150 (2010).

Self-review: passed. Independent audit: not yet performed.
