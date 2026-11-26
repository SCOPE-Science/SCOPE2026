# Independent mathematical audit

## correctness

PASS

Reconstructed the interval and socle arguments for k≥3, e≥2k+1, 1≤j≤e−k−1. For j>k the offset sums [0,2j−2] and [j+k,e−1] leave no gap in the two-generator block. For j≤k the missing offsets are exactly [2j−1,j+k−1]; in the next block three small offsets cover [0,3j−3], while two large offsets start at 2(j+k)−e≤2j−1 and cover through j+k−1. This also works at j=1 (the first range ends at 0 and the second starts by 1). In either case an e-term consecutive run gives the conductor by addition of e. For the PF test, adding retained generators excludes the low offsets below j and the deleted offsets in both regimes. When j≤k, adding e+(e+j+k−1−x) to x∈[j+k,e−1] reaches F, and adding e+max(0,j−1−r) to e+j+r hits the third gap block. Every gap in that third block is PF; when j>k, exactly the surviving upper parts of the two low blocks are PF. Negative candidates in the integer definition are excluded by adding e, except −e, which is excluded by adding 2e−1. Counting gives the stated disjoint two type ranges, also when e=2k+1 leaves only the first branch. Substituting (g,F,t) gives the defect. Since t^e is regular, reduction modulo it preserves the minimal graded Betti ranks over the polynomial ring in the other generators; the last Koszul homology is the socle, with basis indexed by e+PF via the Apéry set. This is characteristic-free. The finite verifier was inspected but not rerun; VERIFICATION.md's 10,857-case output is recorded, not independent proof.

## originality

PASS

Pass the explicit pseudo-Frobenius classification and the resulting bijection of deletion positions with types for k≥3 on the bounded comparisons made. Prior same-family gap/genus/Frobenius and symmetry computations are credited, as is terminal Betti coverage in the symmetric case. The general type-to-Betti relation and the defect substitution are consequences, not separate new general theorems.

## value

PASS

A natural fixed-multiplicity, fixed-embedding-dimension deletion family realizes every type from 1 through ν−1 exactly once; the two PF interval formulas specify which gaps realize each type. This gives usable data about canonical invariants, terminal Betti numbers and distance from almost symmetry, not merely an enumeration at sampled multiplicities or a repetition of the known symmetric case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
