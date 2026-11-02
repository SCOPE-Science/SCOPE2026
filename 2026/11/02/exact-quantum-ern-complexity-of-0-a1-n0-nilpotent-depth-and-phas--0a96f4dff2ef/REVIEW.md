# Self-review

## Correctness (C): PASS

For every positive integer \(a,n\), the lower bound follows from two strictly shorter non-synchronizing words, forcing a strict rank drop between the images of the \((a-1)\)-st and \(a\)-th powers of the zero-letter linear map while its \(a\)-th power remains nonzero. Stabilization of image ranks then gives a difference-space dimension at least \(a+1\). The upper-bound matrices have a one-dimensional kernel for the zero letter and an invertible rotation for the one letter. Every zero product requires at least \(a+1\) zero letters and at least \(n\) one letters; the only possible zero product at their sum of lengths is exactly \(0^a1^n0\). A sufficiently small perturbation of the completely depolarizing channel realizes the matrices as completely positive trace-preserving maps in minimal dimension, and the chosen initial state's reachable differences span the entire matrix space used in the construction. All boundary cases \(a,n\ge1\) are covered; no finite experiment substitutes for the proof.

The packaged checker `verify.py` was run on all 40 pairs with \(1\le a\le8\), \(1\le n\le5\), exhaustively evaluating 126400 short matrix products. Its observed shortest-zero-word uniqueness and dimension-rounding tests passed. Floating-point enumeration is corroboration, not infinite certification.

## Originality (O): PASS, with residual risk

Lee, Lee, and Kjos-Hanssen, arXiv:2609.40154 (2026-09-30), were inspected through their definitions, linearization, general upper bound, constant-word theorem, rotation example, and open-problem discussion. Their result for \(01^n0\) is already known and is explicitly excluded from the novel portion. Their \(\lceil\sqrt{|w|+1}\rceil\) length bound does not give an upper bound independent of \(n\), and the constant-word theorem does not establish this two-parameter family. The inspected earlier qutrit work, arXiv:2603.00861 (2026-03-01), concerns a different synchronization construction and does not establish the asserted exact optimum. Searches for the word family, nilpotent-rotation realizations, matrix-mortality equivalents, and quantum Černý dimension bounds found no statement subsuming this theorem.

The dissertation *Finite-state quantum automatic complexity* attributed to Swarnalakshmi Lakshmanan in the primary paper could not be examined in full; it may contain relevant variants. Search non-detection is not proof of priority, and later or unindexed work could independently contain the same result. No known stronger coverage or decisive unresolved implication was found in the inspected sources.

## Mathematical value (V): PASS

The result solves the natural two-parameter complexity question \(\operatorname{qc}(0^a1^n0)\) exactly, and exhibits a sharp obstruction to qubit realizability at \(a=3\). Unlike a single computed example or a routine restatement of the general length bound, the proof reveals two independently controlled resources: the nilpotent-chain depth produces the exact square-root dimension requirement, while an arbitrarily long middle run is counted by a rotation without raising dimension. This adds a structural family to the open classification of words of quantum Černý complexity two.

## Limits and nearest literature

The theorem treats only positive \(a,n\), mixed-target synchronization and one initial reachable-state set; it does not address all-density-state synchronization, pure targets or general binary words. Nearest sources: https://arxiv.org/abs/2609.40154 and https://arxiv.org/abs/2603.00861. The earlier case \(a=1\) is acknowledged rather than presented as new. Independent priority and mathematical validation are not claimed.

Self-review: passed. Independent audit: not yet performed.
