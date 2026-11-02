# Mathematical review

## Correctness

**PASS.** Each admissible marked circular word is a closed walk in one of 256 edge-orientation graphs. The independent-of-length, finite 256-case strongly connected component lemma proves coverage by six explicit digraphs; their fifteen pairwise intersections have only constant-word cycles. Exact integer characteristic-polynomial identities for the six eight-state transfer matrices imply four copies of the \(1-z-z^7\) trace law and two copies of \(1-z-z^3\), with a precise four-count correction for duplicated constant words. A stand-alone standard-library checker recomputes every critical finite assertion, then checks finite source instances independently. The asymptotic follows from Perron-Frobenius theory for the primitive recurrent graphs. The finite word tests corroborate the theorem, but are not substituted for proof of arbitrary lengths.

## Originality

**PASS, with residual risk.** The full accessible text of Currie et al., *Complement Avoidance in Binary Words* (arXiv:2209.09598), including its Sections 2 and 5, treats repetition and growth phenomena for infinite and finite words, rather than the six-family exact count for marked circular words at length four. Munarini and Zagaglia Salvi's *Circular Binary Strings without Zigzags* treats joint avoidance of \(010\) and \(101\), not pairwise exclusion of complementary length-four factors. Hadjicostas and Zhang's accessible abstract describes a one-pattern cyclic count and a general conditional theory for multiple patterns, but its full text was not established accessible and cannot be certified as noncovering. A finite-state graph formula hidden in that or other indexed/unindexed literature could already imply this count. No exact matching claim was found in the compared mathematical literature and public sequence references; search absence alone is not proof of novelty.

## Value

**PASS.** Complement avoidance is an established, natural binary-factor constraint. The result gives an exact count for every circular length rather than only growth thresholds; identifies six renewal graph classes and the precise constant-word overlap; and pinpoints the length-seven onset and count of words exhibiting both homopolymer doublets. The exact finite-length formula and fixed-graph certificate can be used as benchmarks for complement-avoidance automata and cyclic sequence generation. The finding is more than an arbitrary parameter substitution or a tabulated finite slice.

## Literature, reproducibility and risks

The primary complement-avoidance preprint was read through its relevant body sections, the 2003 circular zigzag article was read as author-uploaded full text, and the 2018 cyclic pattern paper was compared from its full repository abstract only. A separate independent scientific audit has not been performed. The only nontrivial machine-dependent proof component is a self-contained exhaustive verification of a fixed finite collection of graphs, executed with Python's standard library. The publication-priority risk concerns unindexed finite-state interpretations of complement avoidance and the inaccessible full 2018 multiple-pattern discussion.

Self-review: passed. Independent audit: not yet performed.
