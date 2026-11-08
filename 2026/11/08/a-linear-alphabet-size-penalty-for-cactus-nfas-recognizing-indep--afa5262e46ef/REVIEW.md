# Scientific assessment: cactus-NFA parity overhead

## Correctness (PASS)
The proved claim is a state-count lower bound, not an exact cactus minimum. Every trim state has a unique parity-vector label because accepting continuations can be spliced to arbitrary prefixes reaching the same state. Every edge of the \(k\)-cube forces an edge with a different pair of endpoint labels. All useful states are connected to the initial state, and the resulting graph is automatically bipartite. A connected bipartite cactus has at most \(4(N-1)/3\) simple edges. These inequalities give \(N\ge1+3k2^{k-3}\). The separate \(2^k\) unrestricted minimum follows from a deterministic parity automaton and a size-\(2^k\) fooling set. The package's standard-library checker passed the finite tests documented in `VERIFICATION.md`; finite tests are not used as proof for the universal claim.

## Originality (PASS, with explicitly unresolved priority risk)
The Oct 8, 2026 Grobler–Koziel–Siebertz existence result motivates a quantitative complexity comparison; its Theorem 1.1 states existence of epsilon-free bipartite cactus NFAs, while its Section 4 explicitly says tight state-complexity bounds are not established and remain open. The complete openly readable paper was inspected: its structural closure constructions do not give a cactus-state lower bound for independent parity languages. General fooling-set lower bounds (Gruber–Holzer) yield the unrestricted \(2^k\) count but not the extra \(\Omega(k)\) factor. The new proof combines group-phase uniqueness, lifted Cayley/hypercube edges, and bipartite-cactus edge sparsity. Searches for these implications and analogous graph-restricted automata did not identify stronger covering results. A broader earlier or unindexed result could still subsume the lower bound; retrieval absence is not a novelty proof.

## Mathematical value (PASS)
The language family is the canonical intersection of \(k\) independent parity conditions. The result proves a nonconstant representational cost, at least \(3k/8+2^{-k}\) relative to an optimal ordinary NFA, for imposing a cactus transition graph, despite existence of a cactus presentation. The phase/graph-density method also supplies a reusable lower-bound principle for languages recognized as kernels of finite group morphisms. The result does not purport to be an exact cactus-state classification or to achieve a fixed-alphabet separation.

## Closest literature and limitations
- Grobler, Koziel, Siebertz, *Every Regular Language Has a Bipartite Cactus Automaton*, arXiv:2610.11717 (2026). Complete openly readable primary full text, including the main theorem, proof, and conclusion, was inspected.
- Gruber and Holzer, *Finding Lower Bounds for Nondeterministic State Complexity is Hard*, ECCC TR06-027 (2006), describes conventional NFA lower-bound methods rather than cactus graph restrictions.

The quantitative bound may not be sharp. Earlier undiscovered graph-restricted language complexity bounds could subsume it. A general proof is provided, but no independent mathematical review has been performed.

Self-review: passed. Independent audit: not yet performed.
