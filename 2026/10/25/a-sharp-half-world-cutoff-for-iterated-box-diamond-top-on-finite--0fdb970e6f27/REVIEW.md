# Scientific review: sharp half-world stabilization of iterated necessity–possibility

## Correctness

PASS. The key lemma establishes \(T_i\cap U_j=\varnothing\) for all stage pairs by induction on the sum of their indices, using the exact successor recurrences \(T_{i+1}=\operatorname{Pre}(U_i)\) and \(U_j=\{v:R(v)\subseteq T_j\}\). If the modal sequence changes at stage \(r+1\), the \(T\)-sequence has at least \(r+1\) distinct additions and the \(U\)-sequence at least \(r+1\), proving that the frame has at least \(2r+2\) worlds. Explicit directed paths attain the bound; the formula is interpreted under standard vacuous-box Kripke semantics. Exact small-frame experiments and a separate direct recursive evaluator corroborate, but do not replace, this proof.

## Originality

PASS within inspected sources. Alpay–Başaran (arXiv:2606.15437v1, Section 7) already proves the path upper witness for all indices and exact global minimality for indices 1, 2, and 3 using exhaustive and SAT checks; these are excluded from the novelty claim. Their Lemma 2 expressly says that the path family alone does not prove arbitrary-index minimality. No located published mathematical record or targeted older-literature search yielded the two-sided separation invariant, global half-world stabilization bound, or exact minimality **for every index**. The standard modal fixpoint finite-carrier bound of \(n\) changes is weaker. Residual risk remains from possible equivalent older attractor-game formulations that were not identified by the actual searches.

## Value

PASS. The motivating paper experimentally certified the first three minimal separating sizes but had no uniform optimality theorem. This finding closes the complete integer-index problem with a short invariant, halves the generic finite-carrier approximation bound, and identifies exact smallest model sizes for a natural infinite family of variable-free modal distinctions. It is a structural extremal fact relevant to modal-depth certification, not a mere reformulation of the known path upper witnesses.

## Scope and priority limitations

The theorem applies to a single iterated operator over arbitrary finite one-relation frames, not to arbitrary \(\mu\)-calculus operators or infinite structures. The existence of a published game-semantic reformulation of the invariant has not been excluded exhaustively. The source's path lemma and its 1–3 finite exact values are credited as known. The scientific review is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
