# Scientific assessment

## Correctness — PASS
For positive run lengths the factor dichotomy is exhaustive: a factor either contains the uniquely occurring \(10\), or avoids it and is unary or of the form \(0^i1^j\). Unary occurrence counts give the pure powers. Each mixed factor has occurrences at no more than two \(01\) boundaries, and requiring both shorter adjacent factors to repeat leaves exactly the two run-gap cases. The pair series and its square then follow by disjoint choices of the two run-length pairs. An actual packaged verifier checks 2,401 positive quadruples and 95 length/count coefficient positions. Finite tests are not used as an infinite proof.

## Originality — PASS, with residual risk
The closest primary source, Mieno–Inenaga–Bannai–Takeda (MFCS 2016), proves the general \(2r-1\) upper bound on minimal unique substrings of an \(r\)-run string and provides run-length-index algorithms. Its pure-run lemma accounts for two of our candidate families, but the general bound seven at four runs does not imply the sharp binary upper bound five, the complete run-gap classification, the attaining-length boundary, or the two-variable generating function. The full accessible 2019 preprint and the 2021 full open article concern general sliding-window algorithms and do not state those formulas. The generic algorithm could of course compute each specified instance. Published-database and literature searches uncovered no equivalent general-length formula, but absence from the searchable corpus is not proof of novelty. The remaining plausible risk is an unpublished or unindexed exact specialization.

## Mathematical value — PASS
Minimal unique substrings are building blocks for unique-substring queries, and the four-run binary class is the first alternating-run family containing a repeated \(01\) transition and a single opposite transition. The result is a complete parameter classification, with a sharp five-versus-seven improvement over the general RLE bound, an exact finite-length distribution of every possible minimal-unique-factor count, and a precise asymptotic typical count. This is a natural structural test family for repeated-context detection rather than an arbitrarily selected numerical case. No broad algorithmic complexity improvement is claimed.

## Literature and limitations
Relevant sources: MFCS 2016, DOI:10.4230/LIPIcs.MFCS.2016.69 (generic run bound and unary case); arXiv:1909.02804 (2019; guiding source for sliding-window MUSs); Algorithmica DOI:10.1007/s00453-021-00864-1 (2021 online full text); arXiv:1905.12854 (space-efficient generic algorithms); arXiv:2004.01493 (compressed enumeration). The conclusion is confined to positive four-run binary words. Equivalent specializations may exist outside the inspected sources, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
