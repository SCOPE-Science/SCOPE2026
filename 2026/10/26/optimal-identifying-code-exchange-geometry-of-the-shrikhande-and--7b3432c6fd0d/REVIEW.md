# Scientific review of the identifying-code geometry comparison

## Correctness — PASS
For the Shrikhande graph, the bound \(2^4-1<16\) rules out codes of size four; the stated five-code has sixteen explicitly listed distinct nonempty closed-neighborhood signatures. Translation and linear Cayley symmetries produce the proposed \(96\) code templates. Two different exhaustive source programs verify that this family contains *every* five-code among exactly \(\binom{16}{5}=4368\) candidates. The parity-coset invariant gives a structural proof that each of the sixteen optimum exchange components is the line graph of a six-cycle. For the rook graph, both programs test the complete size-six universe, obtain \(2208\) minima, and compute every exchange edge and shortest-path eccentricity. Verification outputs were produced by executing the included source; the method does not infer infinite statements from sampling.

## Originality — PASS, residual risk noted
The strongest direct prior result is Gravier–Moncel–Semri (2008), which *already* gives the rook identifying-code minimum of six, but not the Shrikhande code classification or either exchange-graph structure. The relevant sections and original text of Gravier–Parreau–Rottey–Storme–Vandomme (2015) concern identifying codes in strongly regular and vertex-transitive graphs and quote the rook formula, without supplying the new classification. Published results for the same strongly regular pair about independence and Čech complexes have unrelated conclusions and cannot imply a census or exchange graph of identifying codes. Semantic searches of published mathematical records have not revealed a covering result. Unindexed or inaccessible equivalent computations remain possible; bibliographic priority is not independently certified.

## Mathematical value — PASS
The motivating invariant is the minimum number of sensors that give a distinct nonempty closed-neighborhood signature at every vertex, whose graph-specific determination is a standard coding-theoretic problem. The Shrikhande optimum meets the universal information bound with equality, in sharp contrast with the rook optimum despite identical strongly regular parameters. The full geometric classification and the disconnected-versus-connected minimum-code exchange graphs distinguish existence of optimum solutions from flexibility to replace them at fixed cost. This is an exact natural finite case, not an arbitrary unmotivated slice or an asserted infinite generalization.

## Limitations
The rook minimum size is known and is not claimed as a contribution. No conclusion is drawn for other strongly regular graphs or alternate reconfiguration operations. Exhaustive computations have been independently implemented in two source programs but not externally peer reviewed. Remaining risk of unnoticed equivalent literature is documented in the structured review.

Self-review: passed. Independent audit: not yet performed.
