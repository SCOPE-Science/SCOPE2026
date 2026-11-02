# Scientific review

## Correctness — PASS

The finite exhaustive proof is reconstructable from the bundled C++ verifier and independently programmed Python crosscheck, both using integer arithmetic. Good relabeling fixes the first agent's true ranking without loss; all 120 second rankings, all 14,400 reported ranking pairs, and all eight adjacent swaps at each state are considered. Each allocation-changing adjacent swap is verified to exchange exactly one good, which reduces profit to a single true-rank comparison independently of cardinal spacing. Every resulting improvement digraph is checked acyclic, the longest directed paths are calculated exactly, and all steps of the 18- and 6-move witness paths are verified from recomputed allocations. Sharpness follows from those paths with positive rank-consistent additive utilities. Finite enumeration establishes only the five-good statement, not an infinite extrapolation.

## Originality — PASS, with residual risks

The closest source, Lucet et al. (2026), explicitly proves the two-agent adjacent-swap convergence statement for four goods (Appendix A.3) and leaves arbitrary item counts conjectural. Its all-size item-preserving-swap convergence addresses a more restrictive, distinct move set. Aziz, Goldberg, and Walsh (2017), Theorem 1, show cycling for *unrestricted* report improvements and do not establish adjacent-swap convergence. Direct comparison of the objects, permitted deviations, initial states, and claimed implications confirms that neither theorem supplies the exact five-good improvement graph acyclicity or the sharp path-length constants 18 and 6. Searches for adjacent-transposition report dynamics, five-good convergence, exact improvement-path lengths, and associated public mathematical-result records found no equal or stronger covering statement. Residual risks are unindexed equivalents and other unpublished computations. Absence of search hits alone is not an originality proof.

## Value — PASS

The exact five-good frontier is the **first number of goods beyond the motivating work's proved adjacent-swap regime**. It is therefore a motivated finite cutoff, not an arbitrary parameter slice. The findings show a stronger finite improvement property—acyclicity from arbitrary reports—and give tight worst-case termination horizons under both arbitrary and truthful starts. The two sharp constants distinguish the effect of initialization and provide reproducible benchmarks for any proposed general potential function or bound addressing the open two-agent arbitrary-item conjecture. The value is finite and does not rest on any claim to solve that conjecture.

## Closest literature and limitations

- M. Lucet, H. Surugue, N. Benabbou, A. Beynier, N. Maudet, A. Novaro (2026), *On the Convergence of Iterated Round Robin*, arXiv:2610.23040v1, especially Section 3 and Appendix A.3.
- H. Aziz, P. Goldberg, T. Walsh (2017), *Equilibria in Sequential Allocation*, arXiv:1705.09444v1, especially Section 3.

The claim applies only to two agents and five goods with strict, additive, positive true valuations, the specified alternating picking sequence, and strictly improving adjacent swaps of reports. Termination need not yield unrestricted Nash equilibrium; the six-step truthful-start lower bound is for improving moves, not necessarily cardinally optimal one-step replies. Independent scholarly review remains necessary before presenting the result as established literature.

Self-review: passed. Independent audit: not yet performed.
