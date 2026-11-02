# Scientific review: exact cyclic spectrum fibers

## Correctness — PASS
The proof first recovers counts of `01`, `10`, and each symbol from the length-\(k\) spectrum. It uses the presence or absence of a bounded sandwich factor \(\bar x x^s\bar x\) and of \(x^{k-1}\) to force each run either to its prescribed short length or to length at least \(k-1\). The converse keeps all mixed windows invariant and determines monochromatic counts from the total surplus. A two-vector cyclic Burnside count proves the formula, while explicit non-equivalent excess allocations show sharpness of the threshold. Exhaustive direct window checks through length 16 and 26,160 longer constructed-word trials agree with all statements. The theorem is restricted to exact cyclic multiplicity-preserving observations, \(k\ge2\), and \(t\ge2\).

## Originality — PASS (qualified)
Primary comparison: Gabrys–Milenkovic (arXiv:1804.04548) address linear substring reconstruction codes and repeat-replacement, not the stated exact periodic cyclic fibers. Ota–Manada (DOI:10.1587/transfun.2023TAP0015) address circular substring-frequency uniqueness but impose primitivity of the source, excluding the repeated necklaces here, and do not enumerate the fiber. Related fixed-length three- and four-gram classifications may imply isolated special cases, not an all-length theorem by themselves. Relevant semantic searches found no statement or strictly stronger result with this all-parameter run allocation classification. There remains genuine priority risk from implicit Eulerian-cycle enumeration and less-visible special-purpose literature; the search does not prove novelty.

## Value — PASS
The inverse fiber of a natural, highly repetitive circular sequencing target is determined for every read length, not merely by a rough bound or a single collision. The result gives a sharp sequencing threshold, an exact ambiguity count at every shorter length, and a complete constructive description of all confusable circular sources. These directly quantify ambiguity caused by homopolymer-run redistribution in complete-read assembly.

## Limits and evidence
The proof handles an infinite parameter family, whereas the standalone checker tests finite cases only. It concerns necklaces without reverse-complement equivalence and without read noise. The investigated primary materials and actual comparisons are documented in the structured review record. Equivalence to an unlocated prior Euler-tour formula remains possible.

Self-review: passed. Independent audit: not yet performed.
