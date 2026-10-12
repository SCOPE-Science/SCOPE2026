# Scientific review

## Correctness — PASS

The failure-set recurrence is derived directly from the two modal satisfaction clauses. Monotonicity makes failure layers nested. The critical rank-core lemma proves that no world which ever fails a finite iteration can have all its successors among finite-failure-rank worlds. Its minimal-rank contradiction is valid on arbitrary frames. Any new failure at stage \(k\) then forces \(k\) successively lower-ranked worlds and \(k\) distinct permanent-survivor witnesses, establishing the \(2k\) bound. The directed path of that length gives equality. The separate program checks the recurrence against a direct evaluation, the lemma, witness distinctness, and paths; its finite tests are supplementary, not a substitute for the general proof.

## Originality — PASS, with literature risk

The closest primary source is Alpay–Basaran, arXiv:2606.15437. Its Section 7, Proposition 5 and Table 3 establish minimality only at \(m=1,2,3\); Lemma 2 gives a path *upper bound* for every \(m\) and states that this alone does not prove minimality. The present theorem supplies the missing lower bound simultaneously for all \(m\). Searches for alternating box–diamond iteration, semantic mirages, minimal Kripke frame size, modal depth and predecessor fixed-point ranks did not identify an equivalent all-size lower bound. Generic filtration and finite-depth equivalence results do not imply the exact \(2m+2\) threshold. Residual risk: a classical alternating-reachability or modal-game result could express this invariant without the same modal wording.

## Value — PASS

The primary source explicitly distinguishes finite certified instances from arbitrary-depth optimality. The theorem converts this naturally posed size question into an exact formula for an unbounded, syntactically simple family, and the rank-core lemma explains the otherwise non-obvious factor of two. It determines where exhaustive countermodel search must first succeed at every iteration depth. It is not a claim about general modal-formula complexity or a blanket finite-model bound.

Self-review: passed. Independent audit: not yet performed.
