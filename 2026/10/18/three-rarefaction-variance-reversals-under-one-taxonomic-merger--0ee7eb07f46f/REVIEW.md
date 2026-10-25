# Independent mathematical audit

## correctness

PASS

For uniform size-m without-replacement rarefaction, I_i=1_{taxon i seen} gives absence q_i=C(N-a_i,m)/C(N,m) and joint absence q_ij=C(N-a_i-a_j,m)/C(N,m), so variance is Σq_i(1-q_i)+2Σ(q_ij−q_iq_j) exactly. Every possible positive abundance multiset N<=16 is one integer partition; every pair of taxa up to relabeling is one unordered value-pair. A standalone independent implementation using sympy integer partitions and Fraction was run, enumerating 3380 distinct merger types, verifying zero with >=3 strict adjacent flips for N<16 and exactly one at N=16. Its unique witness is eight singletons, 2,6 merged by (1,2), with 14 exact rational differences and flips m4→5,7→8,14→15 matching the source; 3380-row source CSV parsed and exact unique hit independently corroborated. The source verifier additionally constructs full richness generating distributions; source and certificate contents were inspected, not taken as proof by an exit-code alone. Complete finite enumeration is sufficient precisely because the theorem only asserts N<=16.

## originality

PASS

Best-of-knowledge statement-and-implication search and material inspection distinguish previously established premises and general frameworks from the additional exact theorem; remaining priority risks are explicit rather than treated as negative proof.

## value

PASS

Taxonomic pooling is a natural operation in community biodiversity measurement. Its expected richness decreases but the direction of sampling variance can reverse three times with sample depth; the exact minimal population size and unique witness classify the onset of this non-monotonic phenomenon. The 3380-case classification yields an independently useful exact fact for future analyses of taxonomic aggregation and uncertainty, not an arbitrary unmotivated finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
