# Self-review

## Correctness — PASS

The fixed-carrier statement is quantified over every finite bounded lattice (including the trivial one) and every operation satisfying the five source axioms and Chen's two additional \(\mathsf T\)-conditions. A unique atom is shared by all nonzero elements, so semicomplementation forces negation of any positive element to be zero; conditional identity gives negation of zero equal to one. Conversely, two distinct atoms \(p,q\) produce the displayed operation. The proof checks (P1)-(P4) and separately splits all three logically possible (P5) cases, then exhibits \(\neg p=q\) and \(\neg q=0\). This validates the strict separation without assuming distributivity. The four-element Boolean census follows by determining every row from (P1)-(P4) plus identity and semicomplementation; all four operations pass (P5), and double negation keeps precisely two. The standalone executable checker directly tests source axioms, not just the statement of the criterion.

## Originality — PASS, with residual priority risk

Chen, *Fundamental Propositional Logic with Preconditional* (arXiv:2607.20221), defines the relevant conditional hierarchies and provides no finite-lattice atomic criterion in the inspected introduction, algebraic definitions, or key logical results. Holliday, *Preconditionals* (arXiv:2402.02296), develops the preconditional axioms and Sasaki-style construction but does not give the asserted criterion. A closely related published result, *Fixed-point normal form for finite-chain preconditionals*, proves \(\mathsf T=\mathsf F\) **only for chains**; its complete RESULT.md was inspected. A chain has one atom, so the present result implies that special case but the older result does not imply the all-finite-lattice converse or the two-atom witness. The finite-chain factorial census, existing representations, and definitional reductions are explicitly credited. published-finding corpus similarity searches, published mathematical claims and targeted literature queries did not identify covering treatment. An unlocated lattice-negation theorem could still subsume the result; failed searches cannot establish absolute novelty.

## Mathematical value — PASS

The axiom added between the two named logical systems is meaningful globally, but its status over a *fixed finite algebraic carrier* lacked a supplied structural criterion. The theorem replaces table-by-table checking with the simple order-theoretic invariant “number of atoms,” in the full nondistributive finite lattice class. It explains the earlier chain collapse, identifies every carrier on which it fails, constructs a uniform counterexample, and locates the sharp first failure with a complete minimal census. This is a natural structural classification rather than an arbitrary small table or a restated known identity. It does not imply a new general decidability bound.

## Closest literature and remaining limits

Relevant sources: Chen (2026), sections 2.4, 3.1–3.2; Holliday (2024), sections 2.1–2.4; Holliday–Massas (2026), sections 1–2; published finite-chain normal form (full RESULT.md). The main limitation is finite carriers; the converse is not proved for infinite atomless lattices. Historical priority remains incompletely settled, and no independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
