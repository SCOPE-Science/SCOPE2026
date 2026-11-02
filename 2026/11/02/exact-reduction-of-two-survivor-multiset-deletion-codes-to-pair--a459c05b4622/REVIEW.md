# Scientific review

## Correctness

**PASS.** For any two distinct codewords, a shared multiplicity-two symbol would violate the overlap-at-most-one condition. Choosing one repeated symbol per heavy codeword therefore injects heavy codewords into alphabet symbols. Replacing those words by corresponding constants preserves all allowed pairwise intersections; the remaining all-distinct words are an \(n\)-uniform pair packing. A construction using the \(q\) constants and any maximum packing attains the derived upper bound. Quantifiers include \(q,n\ge2\), with the conventions for \(n>q\). The triple-system formula follows from established minimum-leave classifications. The 16 independent finite optimization comparisons are corroborative, not a substitute for the proof.

## Originality

**PASS, with stated priority limitations.** The closest January 2026 primary paper introduces the same two-survivor multiset model and intersection condition. Its Section 3.4 proves small-alphabet cases and an incidence bound, but leaves the \(n\le q\) optimum open rather than deriving \(S_q(n,n-2)=q+P(q,n,2)\). The March 2026 companion studies different geometric and algebraic bounds. Classical maximum partial triple systems establish the numerical design table, not the reduction from arbitrary multiset codewords. A relevant published mathematical claim on three-survivor codes has a different intersection threshold, and another concerning cover-free triples solves a separate family-selection condition. The inspected sources and targeted searches revealed no statement implying the full normalization theorem; unknown unindexed work remains possible.

## Value

**PASS.** The problem asks for exact capacity in the most severe nontrivial multiset deletion channel. The result reduces *all* alphabet sizes and lengths to an established packing-design extremal parameter, supplies exact closed three-symbol-length capacities for all alphabets, and removes the formerly open distinction between repeated-symbol and all-distinct optimal constructions. Classical packings can now be transferred directly into capacity-achieving unordered deletion codes. No claim is made to newly solve the independent packing-design problem at all block sizes.

## Closest literature and limits

Primary comparisons: arXiv:2601.05636, Section 3.4; arXiv:2603.18322, Introduction and Sections 2, 4, 5; arXiv:1612.08837, Introduction and coding-bound sections; arXiv:1708.07646, Introduction. Priority beyond published indexed records is not certified. Only the all-parameter reduction and its provable corollaries are claimed; an efficient implementation and classification of every original optimum are not supplied.

Self-review: passed. Independent audit: not yet performed.
