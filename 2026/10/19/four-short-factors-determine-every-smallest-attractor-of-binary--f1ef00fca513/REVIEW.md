# Scientific review

## Correctness — PASS
The proof reconstructs the exact four-factor necessity condition, including the nonterminal \(10\) boundary and the distinct first/last positions for \(a,b\ge2\). It then proves every mixed factor is covered by a last-position pair: the first transition fixes a unique start residue, all occurrences form a contiguous arithmetic progression of period \(a+b\), and the proof splits into the cases where an occurrence reaches the next block boundary versus the short zero-start case. Reverse-and-complement transfers the proof to the first-position pairs. The two sets are disjoint and have exactly \(m(m-1)\) members each. The standalone exhaustive checker matches 70 finite instances, but no infinite assertion is inferred merely from these experiments.

## Originality — PASS within inspected evidence
The nearest full published result studies all minimum pairs for \((01)^n\) and the truncated word \(0(1100)^{n-1}1\). Neither is \((0^a1^b)^m\) with both run lengths at least two, and their pair formulas do not imply this theorem by simple normalization. The full recent paper on Fibonacci, period-doubling, and Thue–Morse minimum attractors supplies mathematical motivation rather than covering results. Research-record queries for exact claims and aliases, and comparisons with 69 accessible earlier claims, found no dominating statement. Absence from these searches cannot establish universal novelty; an unindexed, differently phrased older periodic-word classification remains a risk.

## Value — PASS
The result settles all optimum position sets and their multiplicity for a three-parameter family of strongly repetitive words, which is more informative than merely finding the optimum size. The exact four-factor certificate is a structural reduction from all factors of all lengths; the fact that both run lengths disappear from the multiplicity is mathematically explanatory. The sharp finite-word boundary restrictions are essential and not arbitrary numerical slices.

## Limitations
The result excludes run lengths one, one complete block, circular words, and attractor equivalence under rotation. Only self-review has been completed; independent audit and validation remain unperformed.

Self-review: passed. Independent audit: not yet performed.
