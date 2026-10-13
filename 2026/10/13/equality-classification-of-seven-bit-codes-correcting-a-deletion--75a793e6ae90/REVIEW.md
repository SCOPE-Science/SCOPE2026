# Scientific assessment

## Correctness — PASS

The mixed-channel decoding condition is equivalent to disjoint one-deletion and at-most-one-adjacent-swap output sets for every distinct codeword pair; these outputs have different lengths. In a 128-vertex compatibility graph, clique enumeration with proper greedy-coloring upper bounds gives an exhaustive optimum of \(16\), exactly \(28\) maximum sets, and eight orbits of sizes \(4,4,4,4,4,4,2,2\) under reversal/complement. A distinct C++ implementation enumerates every deletion-only 16-clique (\(408\)) and finds no deletion-only 17-clique, then filters them by transposition outputs to recover precisely the same \(28\) sets. Actual programs have been executed after checking their supplied source paths. This is a finite exact result and relies on the full exhaustive procedures, not mere experimental examples.

## Originality — PASS with bibliographic limitations

The 2016 Gabrys–Yaakobi–Milenkovic preprint introduced this same alternative-error channel and asymptotic code constructions, and the 2021 Gabrys–Guruswami–Ribeiro–Wu preprint addresses nearly optimal asymptotic redundancy, including a warning about the earlier argument. Neither inspected primary full text contains the precise complete length-seven equality census or its eight symmetry classes. The 2019 No article establishes single-deletion bounds, not equality classification after adding transpositions. Direct comparisons to the mathematical research index and to previously recorded related code claims likewise revealed no implication of the new count or classification. A possibly unindexed older finite table remains a residual risk; search absence alone does not establish novelty.

## Value — PASS

The new census answers a natural first substantial finite case of the same deletion-or-transposition channel and quantifies the cost of requiring correction of adjacent swaps. There are \(408\) deletion-optimal codes but only \(28\) remain optimal for the mixed channel; notably all eight size-optimal VT residue classes fail despite existence of 28 alternatives at the same cardinality. Complete labeled and symmetry classifications are meaningful equality structure beyond the known numerical deletion-only upper bound. No broad asymptotic improvement is asserted.

## Scope and limitations

The claim is binary length seven only and uses the four-element reversal/complement symmetry group. The finite verifier assumes basic arithmetic and enumerates all code sets via independently implemented exact combinatorial algorithms; the result is not an independently audited theorem. Literature access and keyword/index coverage impose the remaining originality uncertainty.

Self-review: passed. Independent audit: not yet performed.
