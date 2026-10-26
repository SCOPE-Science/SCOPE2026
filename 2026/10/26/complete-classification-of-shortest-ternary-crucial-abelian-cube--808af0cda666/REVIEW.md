# Scientific review

## Correctness — PASS

A self-contained necessity proof shows that three appended letters have distinct possible cube-block lengths in \(\{1,2,3,4\}\), excludes every three-element choice containing \(3\), and forces the profile \(\{1,2,4\}\). Normalizing labels then produces exactly 48 candidates. A direct factor argument proves that precisely four contain an Abelian cube, giving 44 representatives and 264 labeled words. A separate exhaustive implementation inspected all 177,147 ternary words of length 11 and every shorter length and reproduced these counts. Assumptions, right-extension direction, distinction between cube length and constituent-block length, and relabeling conventions are explicit in `RESULT.md`. The known minimum length eleven is credited to Glen–Halldórsson–Kitaev.

## Originality — PASS

The closest results are Glen–Halldórsson–Kitaev's minimal-length theorem and explicit ternary examples in the 2008 preprint and 2010 full journal article. Those results fix the shortest length but do not state the exact number of shortest crucial words, enumerate all representatives, or force the three witness lengths. Aberkane–Currie–Rampersad's published 50,520-word enumeration counts *all* cube-free words, not the crucial subset. Searches for aliases (right-maximal Abelian-cube-free words, crucial words, minimal crucial words), exact counts 264/44, source-relevant tables, and stronger covering statements found no equivalent result in the checked sources. Residual risk: a separate unindexed enumeration or a differently described classification could predate this work; search nonappearance does not prove absolute novelty.

## Value — PASS

The 2008 minimal-length theorem leaves an intrinsic finite extremal question: how many shortest witnesses exist, and are they all instances of one forced structural mechanism? The complete 44-representative classification answers both, with an explicit parsimonious construction, three forced right-extension witness lengths, and exact sixfold relabeling symmetry. This is a natural complete extremal classification rather than an arbitrary slice or an incremental bound. Its significance is specifically about shortest ternary crucial Abelian cubes; claims about higher alphabet sizes or longer words are not made.

## Scope of inspection and limitations

Relevant construction and ternary-length sections of the publicly accessible 2008 preprint and the complete 2010 primary article were read; the 2004 paper was inspected at its definition, growth result, and finite-count table. Checked computational comparisons independently match the 50,520 count published in 2004. Priority against unpublished or unindexed classifications is unresolved. The mathematical assessment is a self-review only; no independent audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
