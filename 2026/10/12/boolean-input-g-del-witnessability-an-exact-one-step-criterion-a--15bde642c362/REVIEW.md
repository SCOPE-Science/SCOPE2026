# Scientific review: Boolean-input Gödel witnessability

## Correctness — PASS

The equivalence is proved by a Boolean atom that selects an arbitrary nonempty set of positive outgoing edge grades; failure of a maximum makes its diamond supremum unattained. In reverse, every modal-free Gödel formula under Boolean atomic inputs is Boolean, so each box infimum is over zero-one contributions and each diamond supremum is over zero together with a subset of the positive row grades. The latter is attained precisely under the row-spectrum condition. In the explicitly defined countable tree, every nonempty positive row-grade set is a singleton, yet the outer box has positive terms decreasing to zero and thus no attaining world. Double negation supplies a concrete failure of the witness axiom. The script `verify.py` checks nine finite restrictions with exact rational arithmetic, including the finite witness axiom and increasing-grade stress tests. It does not replace the infinite argument.

## Originality — PASS

The inspected 2026 Ferrari–Fiorentini–Giardini–Rodriguez paper treats logics whose individual models are already witnessed; it gives semantic definitions and finite-model results but no all-Boolean-valuation criterion for arbitrary fuzzy frames. The 2025 crisp-frame treatment excludes the graded edges essential here. The 2022 paraconsistent finite-branching results use a distinct two-component semantics. Searches for equivalent grade-spectrum and one-step witnessability formulations did not find a dominating statement. In particular, model-level witnessability, logic finite-model properties, and a frame-level guarantee for all Boolean atomic valuations have different quantifiers. This is a provisional scientific originality assessment, not proof that the literature is exhaustively searched.

## Value — PASS

Frame-level witnessability under restricted valuation types is a mathematically natural condition for graded modal semantics. The result gives its exact depth-one structural boundary, with a single-variable diagnostic, while the countable example proves that satisfying this optimal local property does not suffice at depth two. The example retains one positive weight per row and a globally reverse-well-ordered set of grades, so branching and arbitrary row-level grade diversity alone do not explain the obstruction. The modal-depth threshold and concrete witness-axiom failure are the principal value; no general theorem about every modal depth is asserted.

## Closest literature and limitations

Ferrari, Fiorentini, Giardini, and Rodriguez, *A Gödel Modal Logic Over Witnessed Models* (2026), arXiv:2606.31906, DOI:10.4204/EPTCS.447.20; Ferrari, Fiorentini, and Rodriguez, *A Gödel Modal Logic over Witnessed Crisp Models* (2025), DOI:10.1007/978-3-032-06085-3_8; and Bílková, Frittella, and Kozhemiachenko, *Paraconsistent Gödel Modal Logic* (2022), DOI:10.1007/978-3-031-10769-6_26, were read at their semantic definitions and relevant main results. The theorem is for Boolean atomic inputs at depth one, not arbitrary fuzzy input assignments; the second claim is an existence counterexample at depth two, not a complete deeper characterization. A prior formulation using different terminology remains possible. Finite code checks cannot settle infinite attainment. Independent external review has not occurred.

Self-review: passed. Independent audit: not yet performed.
