# Scientific review

## Correctness — PASS
The proof establishes an eventually periodic accepted-length law from every epsilon-free unary NFA by pumping a simple directed cycle through a common multiple of all productive simple-cycle lengths. The one-sided pumping implication is upgraded to eventual two-sided periodicity separately on each residue class. A primitive residue predicate of prime-power modulus then forces one productive simple cycle to have length divisible by the full modulus; bipartiteness forces it also to be even. The matching deterministic cycle is a bipartite cactus and recognizes exactly the claimed language. The count of genuinely multiresidue primitive predicates excludes both translation-invariant sets and the singleton/co-singleton boundary classes. These arguments cover every stated prime power and every nonempty finite alphabet.

The finite verifier checked 935 primitive masks and 55,567 witness length instances. It additionally exhaustively excluded all bipartite unary NFAs with at most four states for any nontrivial modulo-three predicate, across 214,660 candidate machine/final-set configurations. Those finite computations corroborate, but are not used as substitutes for, the infinite proof.

## Originality — PASS within examined evidence
Grobler, Koziel, and Siebertz, *Every Regular Language Has a Bipartite Cactus Automaton* (arXiv:2610.11717v1), prove the existence of representations but explicitly leave tight quantitative state overhead unresolved. Previously established results for a **single** accepted congruence class determine the cost of singleton-residue languages; these are excluded from the stated result, as are their complements. The new theorem simultaneously treats multiple accepted and rejected residues with full prime-power translation period, a setting not implied by the singleton calculation because nondeterministic automata do not generally preserve state complexity under union or complementation. This distinguishes it from a renaming of a known special case.

Czerwiński et al. (arXiv:2302.06435) study unary NFA/UFA complexity without the bipartite graph constraint. Kutrib, Malcher, and Schneider (doi:10.1007/s00236-021-00402-0) require same-label reverse transitions, a different and much more restrictive model. No statement covering the genuinely multiresidue prime-power classification was identified in the examined primary works or searches. Historical priority remains subject to uncatalogued and unindexed literature.

## Value — PASS
The motivating 2026 structural representation theorem leaves optimal state blow-up open. Here the exact graph-restricted cost is determined for \(2^{p^k}-2^{p^{k-1}}-2p^k\) naturally defined length predicates at each prime-power modulus \(p^k\ge4\). The result separates odd-primary and two-primary obstructions, shows that the weaker bipartite restriction and stronger cactus restriction have identical exact cost throughout this large family, and proves that nondeterminism cannot improve the optimum. It is a natural complete classification rather than an arbitrary finite numerical slice.

## Limits and risks
The result is not a bound for all regular languages or for arbitrary composite moduli. It does not assert that the underlying-graph notion is the same as symmetric-transition undirected automata. A possible equivalent statement in earlier inaccessible or unindexed graph-restricted automata literature is a residual originality risk. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
