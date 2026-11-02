# Scientific review

## Correctness — PASS

The inverse-cycle action preserves cardinality, and the inverse merging letter only removes, preserves, or adds state zero. The monotonicity deletion argument proves that a shortest expanding inverse-action sequence cannot contain a non-growing first merger; its first merger must grow the current set and terminate the sequence. This gives a necessary and sufficient zero-to-one cyclic-boundary criterion and a **unique** shortest word. The all-length histogram follows from counting monotone binary prefixes, with a separate closing-boundary count. The stated mean follows by finite geometric summation. The replayable program independently checks shortest inverse subset-graph paths for every subset through \(n=13\), and direct forward word enumeration through \(n=8\), including uniqueness. Finite tests are corroborative, not replacements for the proof.

## Originality — PASS, qualified best-knowledge comparison

The strongest primary match is Miccinesi [1]: Example 1 settles exactly the two stuck subsets at \(n=3\), while Section 8.1 establishes existence of obstructions for arbitrary \(n\), but not a general exact classification, the full distribution or unique shortest words. The full revised Berlinkov–Ferens–Szykuła paper [2] and its MFCS precursor [3] define the same preimage problem and illustrate one four-state Černý example; their results are complexity and decision theorems, not this simultaneous histogram. Published work on \(k\)-avoiding subsets and initial image-rank compression does not imply the claim because its subset quantifiers, objectives, and transformations differ. Search comparisons were conducted against the exact cyclic-boundary rule, its equivalent histogram, and potential stronger uniform-extension results. Residual priority risk: an unindexed earlier cyclic-state computation or a source in a different notation could cover this short structural proof. No exhaustive universal priority guarantee is asserted.

## Value — PASS

Subset extension is a core quantitative object in the extension method for synchronizing automata, and the 2026 certificate theory explicitly leaves the Černý negative-certificate region and its stuck sets as a motivating limit. This result gives a complete **individual** solution across all \(2^n-2\) possible subsets, determines the unique shortest witness, counts every threshold and exactly classifies the exceptional \(n-1\) subsets. The exponentially small obstruction fraction and constant limiting mean give an interpretable contrast with this automaton family's quadratic extremal reset length. This exact structural benchmark is useful independently of obtaining a new general reset bound.

## Risks and boundaries

No theorem about arbitrary automata or reset-word length follows. The historical overlap comparison has finite coverage and leaves priority uncertainty, particularly for unindexed earlier notes about the Černý automaton. Independent mathematical review has not been undertaken.

Self-review: passed. Independent audit: not yet performed.

### Sources

[1] M. Miccinesi, *Certificates for short extending words in a finite automaton*, arXiv:2609.21603 (2026-09-18), §§3, 8.1, appendix. https://arxiv.org/abs/2609.21603

[2] M. V. Berlinkov, R. Ferens, M. Szykuła, *Preimage problems for deterministic finite automata*, arXiv:1704.08233v4, §§1–6. https://arxiv.org/html/1704.08233v4

[3] M. V. Berlinkov, R. Ferens, M. Szykuła, *Complexity of Preimage Problems for Deterministic Finite Automata*, MFCS 2018. https://doi.org/10.4230/LIPIcs.MFCS.2018.32
