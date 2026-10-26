# Scientific review

**Correctness — PASS.** The 2026 root-shift theorem fixes precisely which root pairs represent \(i\)-conjugate elements. The tree-walk lemma gives the exact length \(2E-d\). Edge identity is reducible to free-group equality in deterministic logspace; first-occurrence enumeration computes \(E\), while crossing parity over each distinct edge computes distances using only logarithmic-sized counters. All root pairs are searched with reusable logarithmic workspace. The finite verifier checks 5,461 words independently but is not the reason for the infinite theorem.

**Originality — PASS, bounded.** The numeric extremum is an explicit consequence of Carvalho--Monteiro's Theorem 2.4 and Remark 3.4 and is not claimed as original. The mathematical contribution is its complete deterministic-logarithmic-space evaluation and resulting language decision. The inspected 2026 conjugacy-language paper proves grammar-class separations, the 2019 conjugacy study supplies decidability, the 2012 computational work treats word problems rather than conjugacy-geodesic languages, and the 2026 Green paper studies distinct equivalence relations. No inspected statement implies the space bound as a quoted theorem. Similar unindexed work remains a priority risk.

**Mathematical value — PASS.** The new bound locates a natural non-context-free and non-co-context-free language inside a sharply constrained space class. The procedure avoids building a Munn tree (which may have linearly many edges), by combining free-group equality with first-occurrence counting and parity. It supplies an exact output-sensitive invariant for conjugacy minimization, not only a membership test.

**Closest literature and limits.** Carvalho--Monteiro, arXiv:2608.10379, Theorems 2.4, 3.5--3.6 and Remark 3.4; Araújo--Kinyon--Konieczny, arXiv:1810.03208, §3; Diekert--Kausch--Lohrey, arXiv:1201.3174; Bodart--Carvalho--Monteiro, arXiv:2609.35251. The result is for a fixed rank and natural \(i\)-conjugacy; a specialized unpublished or unindexed prior algorithm cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
