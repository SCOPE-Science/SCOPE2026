# Independent mathematical audit

## correctness

PASS

The cyclic host excludes 0^r, but its targets are all linearly admissible length-(r+1) words. Exactly three windows are removed from the full overlap graph. Removing them makes u=10^(r-1) short one outgoing edge and v=0^(r-1) short one incoming edge; because r≥2 they are distinct, and one extra traversal must be the unique edge e_r from u to v. In a full de Bruijn tour the unique entrance to 0^r from another vertex, the loop, and the unique exit are consecutive in that order, as the loop must be used and the vertex cannot be revisited from outside. Replacing that passage by e_r achieves the bound. Conversely, expanding either occurrence of e_r restores the full tour, and these are the only choices. A shortest necklace is primitive because other factors occur once, so rotation cannot identify its two distinct marked occurrences; the expansions are genuinely different necklaces. The ordinary necklace count at order r+1 is 2^(2^r-r-1), exactly twice the claimed count. The four given examples follow by substitution.

## originality

PASS

For the repaired finding: the known covering theorems already account for the optimal length and factor profile. The inspected statements and constructions do not establish the explicit two-to-one contraction onto unmarked optimal necklaces, or its inverse distinguished-occurrence interpretation. This is a claim of distinct mathematical content relative to the comparisons, not a priority guarantee.

## value

PASS

The explicit map relates ordinary cycles to all optimal run-limited cycles at the first width where repeats are forced. It gives a concrete reconstruction from either marked occurrence, an exact count and equal multiplicity of preimages, so in particular it transfers uniform sampling without reweighting. These are structural properties of the family of optimizers, not just an alternate derivation of the known minimum length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
