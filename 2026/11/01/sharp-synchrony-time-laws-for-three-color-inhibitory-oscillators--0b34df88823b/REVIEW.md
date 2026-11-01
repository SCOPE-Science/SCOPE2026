# Scientific review

## Correctness — PASS
The actual three-color parallel transition rule is specified with open neighborhoods, its support-pair reduction is exact because vertices of the same color and same graph part evolve identically, and the 49 representative trajectories give an exhaustive first-synchronization table for **all** sizes. Formal inclusion-exclusion weights give the exact formulas; the exceptional mask is already period-three, so there are no hidden nonsynchronous transients. The independent vertex-level C++ test checks 923463 labelled states and reproduces the formulas. The 49-case table is finite but exhaustive **over support equivalence classes**, rather than a bound-dependent sample. Reproducibility details and sharpness follow from the attached scripts and proof.

## Originality — PASS (qualified)
The 2014 primary work introduces and analyzes the inhibitory update, while the 2016 full-text tree study gives synchronization criteria and general time bounds. Neither inspected article provides the complete-split support table or all-size first-synchronization distribution. The known star result is precisely the boundary case with a singleton clique, and the complete bipartite case has different inhibition between vertices in its first shore. A targeted search of published mathematical results returned related but non-dominating oscillator and graph-system findings; exact-overlap searches revealed no covering formula. Such searches cannot rule out unindexed equivalents. The exact structure-specific claim is therefore accepted on current evidence with a residual priority risk, not presented as independently established novelty.

## Mathematical value — PASS
The complete split graph is a natural two-parameter family interpolating between star-like and densely coupled oscillator networks. Determining the first time **every** labeled state synchronizes, rather than only existence of synchronous or asynchronous orbits, is a meaningful dynamical invariant. The universal finite classifier, the assertion that every non-synchronizing state is already recurrent, the exact six-step cutoff, and the uniform large-clique two-step concentration give structural information not supplied by the earlier star formula. This is neither a numerical table recomputation nor an arbitrary parameter slice.

## Sources and limits
Main contextual sources: Lyu, arXiv:1407.1103 (2014); Lyu, arXiv:1610.00837 (2016). Contextual alternative continuous-phase model: Vogell–Schilcher–Bettstetter (2020), DOI:10.1103/PhysRevE.102.062211. The claim covers only the stated deterministic three-color graph rule and its uniformly random initial-color corollaries; no independent external scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
