# Self-review

## Correctness — PASS

The greedy first-occurrence recurrence is an exact if-and-only-if for subsequence acceptance. Its four 32-symbol base evaluations give the stated languages, and a 32-step symbolic transfer on three boundary residual languages proves S(AU)=B S(U), preserving boundary hypotheses. The transfer checks all four literal blocks and remains valid for every residual length by translation-invariance of the length offsets. Induction covers arbitrarily many blocks. A direct odd-part argument verifies the dyadic paperfolding decomposition. checker.py replays all four base cases and four symbolic transfers and independently verifies every block product of length <=3 (84 cases), plus dyadic ranks 5--11; finite tests are corroboration, not the infinite proof.

The proof's assumptions are exact: binary alphabet, literal block strings, q>=1, and k>=5 for the dyadic specialization. The recursive function for shortest absent subsequences is justified by leftmost matching, and the symbolic step examines the complete four-choice 32-position transition rather than extrapolating finite data. The packaged checker actually passed all declared tests. Unproved limits: arbitrary paperfolding factors and other instruction sequences are not covered.

## Originality — PASS (qualified)

The precise full shortest-absent language B^q or B^q Sigma for the four-block family and the paperfolding corollary are not implied by the inspected full-text statements. Holub proves existence of contiguous Abelian powers in paperfolding words, not missing scattered words. Kosche et al. prove generic SAS characterizations and algorithms, not the explicit four-block formula. Published published-finding corpus records on general binary universality-index distribution and fixed-length SAS extrema solve distinct aggregate optimization/enumeration problems; inspected RESULT.md statements do not determine the exact paperfolding family. Previous own entries for a different Rudin--Shapiro block family, ordinary paperfolding attractors, and paperfolding prefix-normality do not entail the literal word-level identity. Priority remains a limited-research judgment, not a mathematical uniqueness assertion.

The closest inspected material is Holub 2012, Kosche et al. 2021/2023 and the two published published-finding corpus theorems on generic binary SAS extrema/distributions. The accessible prior research records also contains a Rudin–Shapiro result with a similar proof *method* but a different word family; it does not logically cover this language. Searches include the specific literal 32-block template, equivalent scattered-subword terminology and general universality results. Residual risk: not all historical full texts can be ruled out, and negative searches do not certify uniqueness.

## Value — PASS

The result identifies every shortest absent scattered subsequence, not just an algorithm or count, for an infinite natural paperfolding family, with exactly two independent free positions per 12-symbol absent block. The stronger theorem exposes a four-parameter block invariance for arbitrary concatenations, despite changes in their source strings. The explicit word-level language provides compressed description of 2^(2^(k-4)+1) absent words, gives a closed universality profile, and supplies a reusable symbolic finite-transfer phenomenon for subword-avoidance investigations. The natural paperfolding object and whole-length spectrum are motivated by classical word-combinatorics questions; the result is not a single unmotivated finite table.

The value comes from complete exact language structure in an infinite natural sequence and its stronger arbitrary-concatenation invariant, not from a bounded-rank table or a minor scalar gain.

## Verification and limitations

The full new proof, assumptions, standalone checker, finite transfer, relevant literature comparisons and access limitations are included. Independent mathematical assessment, universal historical priority and extensions beyond complete dyadic prefixes remain unproved.

Self-review: passed. Independent audit: not yet performed.
