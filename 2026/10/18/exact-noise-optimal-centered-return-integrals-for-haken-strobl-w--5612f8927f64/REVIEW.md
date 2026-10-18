# Self-review

## Correctness — PASS

The stated Lindbladian has unique maximally mixed equilibrium and all traceless modes decay exponentially. The invariant orbit reduction and integrated master equations reconstruct the exact signed return integral. The coefficients of \(\gamma\) and \(1/\gamma\) are strictly positive for \(n\ge3\); the only degenerate case is \(K_{1,1}\). The optimizer and fixed-part/proportionate scaling laws follow by explicit algebra. The packaged verifier checks exact-rational integrated-coordinate identities and the full complex density-matrix Liouvillian for many finite sizes/rates; these numerical tests do not substitute for the proof. Principal risk: errors in unit or dephasing normalization if transplanting the formula into a different physical convention; both are explicitly fixed here.

## Originality — PASS

The foundational Haken–Strobl equation and the generic finite-dimensional resolvent method are prior knowledge, not originality claims. A material read of Adithya L J et al. (arXiv:2507.17880) and Bressanini et al. (arXiv:2204.01836) found graph-Laplacian Haken–Strobl and dynamical-distance/coherence results, not this adjacency-biclique zero-frequency integral or its optimization. Razzoli et al. (doi:10.3390/e23010085) use coherent trap absorption; Novo et al. (arXiv:2012.00448) engineer an effective coherent complete-bipartite adjacency Hamiltonian. Neither addresses the present site-dephasing autocorrelation functional. Exact comparison matters: a graph Laplacian differs nontrivially from adjacency on unbalanced complete bipartite graphs, and on balanced graphs the studies use different observables. Published-mathematics searches using noise, autocorrelation, graph, and resolvent aliases found no equivalent implication, only unrelated graph results; their absence is not proof of novelty. Residual risk: unindexed/implicit older derivation or undiscovered table. Independent publication-priority certification has not occurred.

## Value — PASS

The biclique family isolates a meaningful dependence of return relaxation on the centrality class of the initial vertex. The exact global noise optimum makes it possible to distinguish \(J\sqrt b\) scaling with a fixed initial part from \(Jn\) scaling for two proportionately growing parts; these are structurally different experimental regimes. The signed integrated return is precisely the normalized stationary connected occupation autocorrelation, hence a natural zero-frequency response diagnostic; no unproved claim about mixing time or transport efficiency is made. The two-vertex exception is a sharp boundary, not an arbitrary small-case optimization.

## Closest literature and scientific limitations

See arXiv:2507.17880 (2025), arXiv:2204.01836 (2022), doi:10.3390/e23010085 (2021), and arXiv:2012.00448 (2020). They motivate the problem but do not state an equivalent all-size adjacency-biclique formula in the materially read portions. The precise sign, site-dephasing normalization, Hamiltonian, and return observable matter. The result does not cover nonuniform noise, finite measurement windows, or graph-Laplacian Hamiltonians with unequal degrees. Priority remains provisional pending further human literature assessment.

Self-review: passed. Independent audit: not yet performed.
