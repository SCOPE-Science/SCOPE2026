# Review of sharp discrimination memory

## Correctness

**PASS.** The source Kraus family and the new Pauli comparator are CPTP. Their Bloch-transfer difference is rank one and square-zero on the doubly degenerate eigenspace. The exact \(n\)-step identity, all-ancilla trace-norm upper bound and matching pure-state lower bound are reconstructed in `RESULT.md`; neither a numerical matrix power nor a finite search establishes the diamond-norm result by itself. The adjacent-time ratio and exponential limit prove the optimizing time and \(2/e\) scaling. Exact-rational checks are reproducible with `verify.py`.

## Originality

**PASS, best knowledge.** Brandão's arXiv:2610.13622v1 provides the Jordan channel and full qubit preparation/measurement formula. The new statement instead compares it to a *physical diagonalizable Pauli channel with the identical spectrum* and computes the all-ancilla diamond norm, an attaining ancilla-free protocol and the optimized weak-noise repetition limit. Wong--Zeng--Li's experimental quantum-channel EP construction (arXiv:2507.16049), vom Ende's generic diagonalizability theorem (arXiv:2403.19643), and the broader diamond-norm literature do not state the particular comparison in the relevant inspected passages. The proof relies on known rank-one duality and Jordan identities; an equivalent unindexed benchmark remains a residual priority risk. See `AUDIT.json` for explicit equivalent-formulation, broader-coverage, database and prior-implication comparisons.

## Value

**PASS.** Identical eigenvalue multisets do not determine operational multi-step behavior. Here a spectrally matched, CPTP reference permits an exact quantitative comparison in a simple physically implementable qubit model, including a globally optimal preparation, measurement and repetition count. The \(2/e\) critical limit is a substantive long-time effect not described merely by reporting a nontrivial Jordan block. The result is limited to uninterrupted channel powers; it is not an adaptive multi-query theorem or a claim that the reference minimizes distance among all isospectral channels.

## Literature and limitations

Primary texts: Brandão (2026), arXiv:2610.13622v1, Sections III--VI; Wong, Zeng and Li (2026), *npj Quantum Information* 12:63, Results/Methods; vom Ende (2024), arXiv:2403.19643v1, Sections 1--5. The operational meaning of diamond norm is standard (Kliesch and Roth, *PRX Quantum* 2:010201). Searches do not certify global novelty. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
