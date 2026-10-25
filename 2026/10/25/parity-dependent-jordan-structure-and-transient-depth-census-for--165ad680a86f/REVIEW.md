# Scientific review

## Correctness — PASS

The calculation starts from a precisely specified directed update on admissible words. For each \(t<m\), its matrix rows are indicator vectors of nonempty, disjoint prefix cylinders indexed by length-\(m-t\) suffixes; this yields the exact rank \(q(q-1)^{m-t-1}\). Restriction to the last-letter subspace is precisely \(I+J\) over \(\mathbb F_2\). The identities \(J^2=qJ\), \(\operatorname{rank}J=1\), and the power-rank second differences prove all eventual cycles, exact entry-time populations, and Jordan blocks. All boundary cases \(q=2\), \(m=1\), and both alphabet parities were explicitly reconstructed. The independent finite-instance checker directly builds the adjacency matrix and confirms 149 rank equalities and 8,788 full state simulations; exhaustive finite checks supplement but cannot replace the infinite proof.

## Originality — PASS, historically qualified

The closest source inspected is Rosenfeld (2002), which gives the iterated-line-digraph characteristic polynomial; that statement does not determine the nilpotent Jordan block profile or preperiod populations in characteristic two. Dalfó and Fiol (2016) analyze iterated-line-digraph and cyclic-Kautz enumeration, without the same binary state-transition classification. Sutner (1988) and Giang (2010) give general additive/linear finite-state frameworks. The related Ganguly et al. (2008) work concerns cycle structures of additive cellular automata, but full text was not available, so a hidden equivalent cannot be excluded. No exact statement or stronger result covering this Kautz rank/entry-time census was found in the completed scientific comparisons. The novelty judgement is a bounded search conclusion, not proof of uniqueness.

## Value — PASS

Kautz digraphs have a natural iterated-line shift architecture, making them a motivated test family for finite-field dynamics. The characteristic-two parity transition is structurally meaningful: the same update becomes a projection in odd alphabet sizes and an involution in even sizes after the shift compression. Unlike a single rank evaluation, the theorem determines all nilpotent block sizes, sharp transient depth, exact counts at every depth, and recurrent orbit populations uniformly over two unbounded parameters.

## Main risks

Known characteristic-polynomial and line-digraph formulas are clearly separated from the new rank/Jordan/dynamical census. An inaccessible related 2008 paper and unindexed sources are residual originality risks. The numerical verifier is finite and no independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
