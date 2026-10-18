# Research review: three-nonzero-digit reversal products

**Correctness (PASS).** The formal multiplication produces a symmetric seven-term coefficient pattern with central coefficient \(S=a^2+b^2+c^2\). Carry inversion at opposite ends proves that a \(2d+1\)-digit palindromic product is carry free, so the only possible exceptions have \(2d+2\) digits. For most gaps the leading/trailing two-digit obstruction is divisibility by \(11\); the remaining large-gap case has two explicit boundary candidates with unequal central digits; four short-gap patterns reduce to an exhaustive \(2916\)-case exact-integer check. The checker was run successfully. The proof does not infer infinite truth from testing arbitrary finite widths.

**Originality (PASS, with risk).** OEIS A062936 identifies a sufficient low-square-sum family, not an exhaustive three-sparse converse. Ezerman–Meyer–Solé establish the expected-length carry-free case but leave open possible longer palindromic products, and their broader Conjecture 11 includes that obstruction. The new exclusion of the one-digit-overflow case for every triple is not implied by the cited expected-length theorem. Specific exact-object and equivalent-formulation queries across the relevant mathematical search sources and earlier findings yielded no covering statement. Priority risk remains for an unindexed equivalent or later paper.

**Value (PASS).** This is a complete classification for a natural first nontrivial sparse-digit family, with arbitrary interior placement, within a separately stated classical reversal-product conjecture. It removes precisely the carry-length obstruction that existing theory does not settle in this subfamily; it is not merely another finite table or renaming of a known sufficient condition.

**Scope and limitations.** The proof uses an exhaustive small certificate and does not resolve the unrestricted conjecture, other bases, or higher digit sparsity. No independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
