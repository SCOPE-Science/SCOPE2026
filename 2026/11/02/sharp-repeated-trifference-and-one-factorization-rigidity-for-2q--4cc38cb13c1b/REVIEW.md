# Review: sharp repeated trifference and one-factorization rigidity

## Correctness
PASS. The per-coordinate Maclaurin maximum is \(8\binom q3\), making the all-coordinate average separation exactly \(2q-4\). Equality forces balanced symbol-pairs and three nonseparations for every triple. The pair-multiplicity triangle sums plus degree sums yield \((2q-4)m_{uv}=2q-4\), so every edge occurs exactly once for \(q\ge3\). The round-robin factors supply all-parameter equality witnesses. The finite labeled-optimizer count follows from exhaustive enumeration of 3003 candidate five-factor families with precisely six factorizations, checked by standalone code.

## Originality
PASS with documented priority risk. Bishnoi and collaborators already found the cardinality \(T(5,2)=6\) in arXiv:2505.07706; only the equality-case rigidity and 7776 labeled optima, together with the all-\(q\) theorem, are claimed. Full motivating paper and targeted perfect-hashing/one-factorization comparisons do not reveal this classification. Legacy perfect-hash literature could contain an implicit equivalent theorem and is not fully exhausted.

## Value
PASS. The all-parameter equality case of a sharp repeated triple-hashing bound is a structural theorem. It identifies the exact combinatorial objects behind every optimizer and establishes a complete exact census at the first ternary two-fold instance, which is a natural extension of a published numerical maximum. No global bound on codebook size is claimed for arbitrary alphabet parameters.

## Closest literature and limitations
Bishnoi et al. (arXiv:2505.07706, Section V.A) record the size-six maximum but not its optimizer types. Kurz (2023) studies single-trifference, rather than the five-coordinate twice-separated optimizers. Related three-row perfect-hash and frequency-permutation-array indexed records have different objects and parameters. Exact finite enumeration is independently replayable, not a substitute for the general proof. Unexamined historical equivalents remain a priority risk.

Self-review: passed. Independent audit: not yet performed.
