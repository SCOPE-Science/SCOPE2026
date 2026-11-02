# Review of exact liquidity thresholds for two-size envy-free transfers

## Correctness

**PASS.** Pairwise envy-freeness under identical valuations and balanced internal transfers fixes the net payment to the difference between the average total value and the assigned bundle value. The budget caps thereby become integer packing capacities. Summing capacities and summing capacities for large goods gives the necessary tests; a large-first, then unit-good construction proves sufficiency. The common-budget threshold follows algebraically. The exact checker exhaustively tested 40,800 finite rational profiles and 5,069,616 item-allocation load vectors, while the proof is valid for all stated sizes and budgets.

## Originality

**PASS, with residual publication-priority risk.** The motivating work of Bredereck, Deltl, Inamdar, Jain and Pandey already supplies the individual-budget internal-transfer model and general algorithmic techniques. Publicly indexed workshop passages describe its one-good-type equal-budget case and more general algorithms. The claim here is not algorithmic solvability per se: it is the complete two-inequality characterization with heterogeneous budgets and an exact common-budget threshold. Searches for equivalent cash-allocation and two-size heterogeneous bin-packing formulations found no statement subsuming the result. Full motivating-paper text was not obtainable, so a stronger result in an unseen portion or prior packing literature is a remaining risk; search failure is not proof of uniqueness.

## Value

**PASS.** The result describes the entire liquidity-feasible region through two distinct natural obstructions, permitting quick assessment of arbitrary agent-specific payment limits and exact computation of the smallest shared liquidity endowment. The construction uses only counts, not expansion into individual item copies. This is a motivated natural complete classification, not an unrestricted complexity claim.

## Closest literature and limitations

The M-PREF 2025 workshop manuscript *Envy-free Allocations with Individual Payments* (arXiv:2610.09610) contains the source model, fixed-type general algorithms and a one-type equal-budget result. General discrete-size bin-packing literature supplies context. The result needs identical valuations and two integral positive denominations, one of which is the unit item. The primary workshop/full preprint remained inaccessible during this comparison; publication priority is consequently provisional. No independent scientific audit or formal proof-assistant validation was performed.

Self-review: passed. Independent audit: not yet performed.
