# Independent mathematical audit

## correctness

PASS

From published three-valued Nmatrix, atomic p∈{T,F}, negation T→F and F,U→{T,U}. Exact recurrence (t,u,f)→(u+f,u+f,t) with (1,0,1), so initial totals F_{n+3} and terminal distribution (F_{n+1},F_{n+1},F_n) for n≥1. The support rule requires each U position to be F in some row preserving every T of the candidate. Reconstructed the proof of first-round survivors: T-start forced alternating row, F-start all-U, F-start immediate T alternating, and F-start U^k T alternating rows; any U following a previous T is unsupported. At second pruning all mixed rows with k≥2 lose support at coordinate 1 when k even and 2 when k odd≥3; precisely k=1 survives. Hence n=0,1,≥2 sizes 2,3,4 and the four explicit A/B/C/D patterns for every n≥2; stabilization by two rounds. Independent literal generation and iterative support deletions matched all rows and first-pruning normal forms through n=13. The universal conclusion follows from the described normal-form induction, not the finite replay.

## originality

PASS

Leme–Coniglio–Lopes arXiv:2308.13664 gives exactly the semantics/support rule and coarse 2^{subformula count} initial bound, but its full HTML sections examined do not state the Fibonacci profile, two-round deletion or four-row normal form for the iterated-negation family. Resultary search for negation-tower support deletion / Fibonacci returned no relevant duplication. This is an exact new analysis of published semantics, not a new semantics/decision method. An equivalent observation in unindexed teaching/software notes is possible.

## value

PASS

Iterated unary negation is the most canonical depth-unbounded one-variable stress test for this Nmatrix. The theorem sharply distinguishes Fibonacci-sized initial generation from a constant four-row stabilized table. This quantifies a meaningful algorithmic phenomenon and provides a closed exact test family; it does not imply constant running time when materializing the initial rows or generalize to formulas containing implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
