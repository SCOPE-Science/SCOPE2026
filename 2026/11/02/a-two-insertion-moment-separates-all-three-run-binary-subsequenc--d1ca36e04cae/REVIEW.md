# Scientific review of the three-run strong-Wilf separation theorem

## Correctness

PASS. The claim quantifies over every binary pair in which the first pattern has at most three runs. The known one-insertion run-multiset lemma reduces possible alternatives to permutations of those run lengths. For three runs the ordered-pair-of-embeddings expansion separates equal, once-overlapping, and disjoint omitted pairs, with exact weights 4, 2, and 1. A complete six-shape compatibility table yields a symmetric base minus the term \(2ac\mathbf1_{\{b\geq2\}}\). That term identifies the middle run, including singleton and repeated-length boundary cases. Full direct enumeration and separate omitted-hole calculations confirm the formula on 81 and 216 parameter triples respectively. Only the combinatorial proof, not the finite tests, covers all positive lengths.

## Originality

PASS subject to the stated residual priority risk. Menon--Singh, *Subsequence frequency in binary words* (arXiv:2306.07870v1), Lemma 3.6 and Conjecture 5.2, explicitly establishes the run-multiset invariant and leaves the all-pattern strong-equivalence classification conjectural. Its results for three-run patterns concern maximum multiplicities and internal zeros, not this identification by second moment. Bruda (arXiv:2607.02578) treats eventual polynomial occurrence-frequency counts for fixed \(k\), not equality of entire distributions or recovery of the ordered run composition. Targeted searches of relevant indexed published records, relevant primary literature, and accessible prior claims did not identify a stronger covering result. This is best-knowledge originality, not a proof of absence from all literature.

## Value

PASS. The problem is a clearly named conjecture in the foundational 2023 subsequence-frequency study. Establishing it for the entire natural three-run subclass is an infinite-domain structural classification, not a finite or arbitrary parameter census. The main new invariant shows that *one extra-host-letter moment*, in conjunction with the already known run multiset, is sufficient to identify the middle run without reconstructing every frequency distribution. The precise correction also isolates the singleton-middle exceptional mechanism.

## Closest work and limitations

The first source already proves the unordered-run invariant and verifies its larger conjecture computationally only through pattern length 13; this work extends a three-run subclass to all lengths. Bruda concerns different frequency-count asymptotics; Tian gives per-host counting algorithms; Janson--Szpankowski treat random-host limit laws rather than the two-insertion fingerprint. An unindexed equivalent derivation, including a two-deletion or word-reconstruction reinterpretation, is a residual priority risk. No assertion is made for patterns with four or more runs, or for alphabets larger than two. The finite verifier is auxiliary to the symbolic proof.

Self-review: passed. Independent audit: not yet performed.
