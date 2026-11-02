# Scientific review

## Correctness

**PASS.** For every fixed integer \(n\geq3\), the strictly positive equilibrium equations imply one dominant negative successor-column entry per row after positive column scaling, with a strict margin \(a_i>0\). A continuous homotopy scales every other nonnegative entry and remains nonsingular by strict dominance after column permutation. At the pure cycle matrix, the determinant is negative for **every** cycle length, not merely for odd lengths. The exact identity \(\det(-J)=\det(BX)<0\) forces a strictly positive real root of the monic characteristic polynomial. The same sign establishes invertibility and hence uniqueness of a full positive equilibrium, if it exists. An explicit all-order feasible but unstable example prevents vacuous interpretation. The proof does not infer an infinite theorem from computational samples. A standalone exact-fraction program checks 84 rational examples and 13 uniform witnesses.

## Originality

**PASS, with bibliographic uncertainty.** The closest source is Meng et al., *Impossible ecologies* (arXiv:2309.16261v1): it proves the \(n=3\) obligate cyclic predator case and records numerical, not rigorous, status for its four- and five-species impossible topologies. It explicitly conjectures infinite families resembling predation cycles and reports no all-order proof. The new theorem is quantified over **all** \(n\geq3\), allows arbitrary nonnegative competitive chords and asymmetric magnitudes, and proves negative Jacobian index and a positive real unstable mode. Its extension theorem proves possible subecology \(\Rightarrow\) possible extension, not the reverse; here each proper induced subcommunity lacks a necessary positive benefactor somewhere. Hong–Pego's subcommunity D-stability exclusion results concern multiple stable communities and do not imply instability of every all-obligate cyclic equilibrium. Mooij et al. concern competing-species stability, with only abstract-level examination and no decisive covering comparison. Mathematical research-record searches using predator-cycle, one-benefactor, signed-determinant and obligate-community aliases found no equivalent statement. Residual risk: an equivalent theorem under a classical signed-matrix, food-web or index formulation may exist outside the inspected sources.

## Mathematical value

**PASS.** The 2023 ecology paper highlights an exact gap: numerical classifications and a conjecture about infinite impossible ecological families. This solves a structurally natural whole family uniformly in species count, rather than checking an arbitrary small graph. The signed determinant identifies why feasibility itself creates instability, with the unexpectedly strong conclusion that the unstable eigenvalue is real and positive, and verifies that positive equilibrium points can genuinely exist. It clarifies the distinction between positive abundance feasibility and stable coexistence in trophic loops.

## Scope and remaining risks

The theorem requires strictly negative intrinsic growth at every species and exactly one beneficial partner in a single directed cycle. It does not cover added mutualism, additional prey, a disconnected cycle cover, non-equilibrium coexistence, global extinction, or the probability of coexistence under random parameters. The standard determinant-dominance lemma is mathematical background, not claimed as original. Publication priority remains subject to broader expert bibliographic comparison.

Self-review: passed. Independent audit: not yet performed.
