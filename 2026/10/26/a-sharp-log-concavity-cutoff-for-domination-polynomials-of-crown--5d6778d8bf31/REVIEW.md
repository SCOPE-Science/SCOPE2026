# Independent mathematical audit

## correctness

PASS

Classify a dominating set by selected left/right counts: both >=2 contribute A_n(t)^2 with A_n=(1+t)^n−1−nt; a singleton on one side forces the corresponding missing-neighbor vertex on the other side, yielding two n t²(1+t)^(n−1) terms with n t² double-count overlap; exactly entire single side contributes two t^n. For n>=5, d2=n,d3=2n(n−1),d4=C(n,2)^2+2nC(n−1,2), giving d3²−d2d4=−n²(n−1)(n²−13n+8)/4<0 for all n>=13. The finite complementary orders n=2..12 are EXHAUSTIVELY checked by all integer coefficient minors, not extrapolated. Strict increase to middle uses upward-closed probability d_k/C(2n,k), and strict fall after n follows every (n+1)-set dominating, d_n=C(2n,n)−2n and central binomial gap. Total-dom polynomial A_n² is an earlier known identity, and log-concavity follows from convolution of nonnegative log-concave interval-supported sequences. Independently enumerated all labeled subsets for n=2..6 and checked integer minors up to n=60; finite testing is not the infinite sign proof.

## originality

PASS

Best-of-knowledge independent claim-versus-prior implication comparison: A total-count scalar does not imply coefficientwise log-concavity; a total-dom polynomial does not determine ordinary-dom polynomial. The candidate contributes full ordinary enumerator plus exact phase boundary, though the scalar count itself was published long before. Closest exact antecedents are explicitly credited and risks retained.

## value

PASS

The full ordinary domination coefficient sequence of a canonical regular bipartite graph family exhibits an exact and persistent log-concavity change at the natural order threshold 12/13, while staying strictly unimodal and contrasting with the already-known total-domination formula. This is a motivated graph-polynomial structural cutoff, not merely recomputation of OEIS A287063 total counts. The threshold is proved for the entire infinite family by a symbolic negative minor plus exhaustive finite positive interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
