# Scientific review: sharp period-two onset in weighted bipartite sine networks

## Correctness — PASS

The theorem has a specified finite graph, positive weights, a phase-quotient state space, and a uniform statement for every such graph. The largest Laplacian eigenvalue is simple by the irreducible nonnegative signless-Laplacian conjugate. The quartic coefficient is strictly positive by connectedness. Strict Lyapunov descent persists at the sharp spectral endpoint because no nonzero gradient direction can maintain the saturating edge-cosine value throughout a moving step. Analytic Lyapunov–Schmidt reduction gives the nonzero period-two branch with the stated amplitude. The symmetric Jacobian at the two points has a critical multiplier \(-1+2\mu+O(\mu^2)\), while all other quotient eigenvalues remain in \((-1,1)\). The supplied numerical program checks seven weighted bipartite graphs and 3,689 conditions; it is corroboration, not the proof of any universal assertion.

## Originality — PASS, with explicit scope of known implications

The inspected source *Morse–Smale dynamics in discrete Huygens networks* (arXiv:2610.10993v1, Sections 2, 3, and 5) gives this graph model and the strict Lyapunov interval \(0<h<2/\lambda\). For trees it proves loss of fixed-point sink stability for \(h>2/\lambda\), but does not derive a stable period-two birth, a graph-dependent amplitude, or endpoint strict descent. Litman's *The Origin of Edge of Stability* (arXiv:2604.20446v1, Theorem 2.3 and Corollary 2.5) **already provides general local gradient-descent period-two branching theory**; the existence of a generic square-root branch is not original. The reviewed claim adds the unconditional graph-spectral and quartic sign assertions for every connected positive-weight bipartite graph, proves full quotient attraction and its critical Floquet coefficient, and identifies the exact global onset boundary by strict endpoint descent. General local theory alone does not assert all these graph-specific conclusions. The residual possibility of an earlier equivalent specialization remains genuine.

## Mathematical value — PASS

The 2026 network study makes \(2/\lambda_{\max}(L)\) a natural sharp loss-of-descent bound and notes that the antiphase equilibrium ceases to be a sink beyond it, leaving the ensuing dynamics unresolved. This theorem establishes a structural, topology-independent answer: the first nontrivial recurrent orbit is born immediately and attracts on the quotient for **every** connected weighted bipartite topology, even with cycles and irregular weights. The explicit eigenvector quartic gives a quantitative amplitude and a model-specific Floquet rate. The endpoint strictness establishes absence of all nonfixed periodic orbits at the transition itself. These statements are stronger than a textbook multiplier computation at the fixed point; they do not claim a global classification for large steps or resolve Morse–Smale transversality problems.

## Primary comparisons and limitations

Buescu–D'Aniello–Oliveira (arXiv:2610.10993v1) supplies the model and prethreshold descent, not the postthreshold cycle. Litman (arXiv:2604.20446v1) supplies generic local branching, not the graph-family sign and attraction theorem or endpoint exclusion. Hofmann (arXiv:2607.04993v1) treats polynomial gradient-descent models rather than this sine-network family; only its abstract was accessible. An earlier equivalent special case, including an unpublished or unindexed one, cannot be excluded. The attracting statement is local in the supercritical parameter and modulo common-phase rotation; the full map has a neutral circle direction. Numerical checks do not certify the unrestricted theorem.

Self-review: passed. Independent audit: not yet performed.
