# Scientific review

**Correctness — PASS.** The proof first characterizes absent length-\(k+1\) subsequences for cuts after a one by partitioning into \(k\) arches. Cuts in a double-zero gap are handled through the alternating \((01)^k0\) subsequence and a greedy bound. Reversal supplies the corresponding cuts before ones. Counting terminal runs proves completeness, and the Fibonacci substitution plus coprime symbol counts proves the distinct-rotation specialization. The package's independent direct-enumeration and dynamic-programming verifier passes; finite checks supplement, not replace, the unrestricted proof.

**Originality — PASS against inspected evidence.** The general 2021 arch-factorization treatment and the 2022 near-universality study provide algorithmic tools to count missing scattered subsequences for *individual linear words*. Full text relevant to their descriptions and counting propositions was inspected. Neither describes a cyclic gap-run multiplicity histogram or its Fibonacci specialization. The 2013 Fibonacci balance paper concerns another invariant. Mathematical-record searches and available historical claim comparisons revealed no dominating or equivalent theorem; a possible unindexed earlier result remains a risk. Application of prior general algorithms to each word is acknowledged rather than misrepresented as novel.

**Value — PASS.** The result classifies all cuts of an unbounded natural family of binary necklaces by their exact near-universality defect. Its unexpected dependence on the gap-run length multiset, not the order, yields a structural quotient and a closed Fibonacci law for all substitution levels. It is more than a fixed-size data table.

**Scientific limitations.** The cyclic gap alphabet is restricted to one or two zeros and must include a long gap. The generic histogram counts indexed cuts even in periodic words; only the Fibonacci specialization counts distinct rotations. No full bibliographic uniqueness guarantee or independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
