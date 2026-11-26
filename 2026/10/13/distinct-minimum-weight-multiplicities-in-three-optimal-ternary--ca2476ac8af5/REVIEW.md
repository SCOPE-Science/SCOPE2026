# Independent mathematical audit

## correctness

PASS

An independent field implementation verified the primitive power cycle and rank 10 for the two-zero parity checks on 242 coordinates. Matching oriented pairs of signed two-position syndromes with inverse syndromes on disjoint supports gave 145200, 203280, 261360 ordered matches. Every weight-four word has exactly three unordered two-plus-two partitions and two orders of the parts, hence the exact counts are 24200, 33880, 43560. As a second calculation, enumerating each 3^10-word dual and independently evaluating the ternary MacWilliams coefficients for weights 0 through 4 gave (1,0,0,0,24200), (1,0,0,0,33880), (1,0,0,0,43560), respectively. This also confirms minimum distance four without inferring it from the pair-bucket calculation alone. If two codewords of weight four on a common support were independent, a linear combination would cancel a nonzero position and give a nonzero word of weight at most three. Thus each support has exactly two scalar representatives, giving the three asserted support counts. Monomial maps preserve weight multiplicities, so the distinct counts establish pairwise inequivalence among the three codes.

## originality

PASS

Pass for the comparative claim, with explicit partial prior coverage: the e=2 multiplicity is already implied by an earlier full dual spectrum for the monomially equivalent exponent v=182, not merely by a coincident number. The weight-four counts for e=16 and e=20 and the resulting three-way distinction are not supplied or implied by the inspected construction theorems, tables, and spectrum examples. Their independent computation adds nonredundant facts; this is not a novelty pass for all three coefficients separately.

## value

PASS

The choice is a comparison of canonical distance-four construction families at a common small nondegenerate admissible extension degree, not a search for an arbitrary anomalous length. At equal length, dimension and minimum distance, the exact leading weight coefficient tracks the multiplicity of minimum words and supports, and here separates three codes up to monomial equivalence by a concrete invariant. The previously covered e=2 value serves only as a baseline. The two residual exact coefficients and their inequivalence consequences are useful for identifying and comparing optimal constructions even without a general weight-distribution theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
