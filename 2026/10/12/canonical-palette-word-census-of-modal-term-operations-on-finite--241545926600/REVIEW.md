# Scientific review: canonical palette-word census

## Correctness

**PASS.** The proof supplies a color-preserving bounded morphism for every adjacent subset deletion, an explicit family of modal formulas separating the surviving levels, and a cross-model quotient-isomorphism argument establishing uniqueness of reduced pointed types. A separate capacity-subsequence realization proves that precisely the listed palette words occur. The finite disjoint union of all valuations and finite-model modal separation then give the exact term-operation exponent, without extrapolating from computation. The zero-generator boundary and the last-cluster index constraint are stated and checked. The executable verifier independently compares actual bisimulation refinement, realizable palettes, and direct Boolean modal term closure in finite cases.

## Originality

**PASS with residual historical risk.** The inspected 2023 linear-frame paper of Kurucz, Wolter and Zakharyaschev studies bisimulation, finite generation and interpolation over cluster chains, not the all-valuations r-ary term-clone census. The 2022/2023 paper by ten Cate and Koudijs proves general results on finite characterisations and local tabularity, not this explicit ordered-capacity invariant. Direct searches for S4.3 term-clone counts, palette-word normal forms and equivalent stuttering classifications produced no decisive dominating theorem. The use of standard bounded morphisms, modal distinguishability and finite bisimulation minimization is acknowledged. Prior results on fixed generating tuples do not directly count all r-ary term functions. Older, possibly differently named normal-form literature remains a substantive originality risk; a negative search is not a novelty proof.

## Mathematical value

**PASS.** For an arbitrary ordered vector of positive cluster capacities, the result replaces enumeration of syntactic modal terms by a finite, exact language of subset-noninclusion words, yielding the full arity-wise term-operation cardinality. Its meaning is intrinsic to the Boolean modal algebra, and the formula detects directional distinctions ignored by total cardinality: the same three-world total preorders with capacity orders \((2,1)\) and \((1,2)\) have respectively \(256\) and \(64\) unary term functions. The explicit \(4^h\) unary law for a reflexive chain gives a sharp all-length specialization. The classification is a natural algebraic and logical invariant relevant to finite expressive power, rather than a chosen small numerical slice.

## Closest literature and limitations

The primary comparisons are Balder ten Cate and Raoul Koudijs, *Characterising Modal Formulas with Examples* (arXiv:2206.06049 and arXiv:2304.06646), and Agi Kurucz, Frank Wolter and Michael Zakharyaschev, *A Non-Uniform View of Craig Interpolation in Modal Logics with Linear Frames* (arXiv:2312.05929). The former addresses formula characterisation and local tabularity; the latter analyzes interpolation and bisimilar linear-frame models. Neither inspected relevant treatment gives the capacity-indexed clone count claimed here. There remains a risk of equivalent statements in older modal algebra, finite-word, or coalgebraic normal-form sources.

The proof is for finite reflexive total preorders with the ordinary unimodal Boolean signature. No formula-length optimum, computational-complexity optimum, or result for graded/converse modalities is asserted. Finite tests corroborate but do not certify an infinite theorem. No independent review has occurred.

Self-review: passed. Independent audit: not yet performed.
