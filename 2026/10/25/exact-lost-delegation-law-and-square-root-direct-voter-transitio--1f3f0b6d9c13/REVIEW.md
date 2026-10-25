# Scientific review: bipartite transitive delegation and lost voting weight

## Correctness — PASS
The model fixes all quantifiers, directed edges, q in (0,1), unit weights, independently sampled local choices, and the cycle-loss convention. Sequential exposure gives the exact finite falling-factorial survival probabilities, with all revisits classified by parity of path length. The asymptotic collision exponent follows from logs of finite products on the \(\sqrt N\) scale, and the uniform Gaussian collision bound controls tails. At fixed positive q, first-revisit decomposition and dominated convergence give the stated finite loss constant. Independent of the proof, an exact rational full-profile enumerator checks sixteen small graph/parameter pairs, including the boundary at part size one. These checks support but do not replace the analytic proof.

## Originality — PASS, with limitations
Related theoretical foundations and methods are established: transitive delegations and cycle abstention, complete-network probabilistic delegation, birthday-collision exploration. Primary comparison with Colley–Delemazure–Gilbert (2023) identified their one-way bipartite proxy-voting theorem, which excludes delegation cycles, and their complete-digraph voter-criticality formula, which changes the network and observable. Berinsky et al. (2021) discuss stochastic delegate weights and graphical processes, not the present two-way bipartite lost-weight crossover in inspected sections. Utke–Schmidt-Kraepelin (2023) use alternative robust delegation semantics. Recorded semantic literature and research-database searches did not identify a theorem covering this exact finite law and both asymptotic regimes. Older random mapping theory might conceal an equivalent formula; no universal novelty proof is asserted. Comparison against related claims yielded no covering implication.

## Value — PASS
Delegation cycles invalidate original voting weight, yet conventional analyses often bound power concentration or study decision accuracy instead of predicting the fractional loss of representational weight. This theorem gives every bipartite size's expected loss, the exact square-root regime boundary between macroscopic participation and collapse, and the nonzero finite expected loss even when direct voting has fixed positive probability. The threshold is a structural scaling law for a natural two-community proxy network and not an arbitrary finite table.

## Limits and closest literature
The primary papers listed in RESULT.md are the closest inspected liquid-democracy literature. The theorem does not address full loss distributions, arbitrary graphs, heterogeneous behaviors, or election outcomes. General random-mapping absorption asymptotics may imply related statements; a broader exhaustive historical assessment was not possible.

Self-review: passed. Independent audit: not yet performed.
