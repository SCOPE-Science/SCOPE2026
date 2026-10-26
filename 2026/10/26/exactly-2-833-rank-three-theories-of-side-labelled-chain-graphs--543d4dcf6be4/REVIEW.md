# Scientific review of the 2,833-class chain-graph theorem

## Correctness

PASS. The logical invariant is reconstructed from ordinary three-round atomic Hintikka types, including equality/repeated choices, both side predicates, and arbitrary adjacency patterns. The word representation lemma covers every finite side-labelled chain graph on exactly its original number of vertices. The two append operations preserve Ehrenfeucht–Fraïssé equivalence, so full transition closure gives an infinite-size theorem. `verify.py` replays 2,833 pairwise distinct rank-three profiles and all 5,666 transitions, proves shortest-path minimality in the finite transition graph, and reports two states at the sharp order 21. The generic independent-in-code atomic recursion corroborates sampled states. Numerical claims require replay of the provided actual files.

## Originality

PASS under the checked coverage, with residual risk. Search compared the theorem and its aliases against indexed findings and accessible research ledgers; no identified statement implies the exact 2,833-class count or 21-vertex bound for the same signature and class. The closest current literature supplies general logical methods (Pikhurko–Verbitsky 2010), nested chain-graph structure and optimization (Boyacı–Ekim–Shalom 2015), and the forbidden-subgraph/word-class context (Alecu et al. 2022). Distinct already recorded results cover uncoloured connected half-graphs at rank four or uncoloured threshold graphs at rank three, not this fully side-labelled chain-graph class. General finite-index results do not supply the exact enumerated state count without the missing classification. Unindexed literature remains a risk.

## Value

PASS. The exact bounded-rank logical spectrum and optimal induced-size representative threshold are natural invariants of the full hereditary class of two-sided chain graphs, not arbitrary sizes or selected examples. A compact complete finite-state model controls truth of *every* rank-three first-order sentence on *every* finite graph in the class; in particular, the 21-vertex bound produces a finite complete testing set and an optimal obstruction to smaller uniform kernels. The numerical complexity is nontrivial despite the class's two-letter construction. The result does not claim analogous consequences for uncoloured or richer logics.

## Related work and scientific limits

The closest inspected primary texts are Pikhurko–Verbitsky arXiv:1003.4865 (Section 3 and depth definitions), Boyacı–Ekim–Shalom arXiv:1504.03666v1 (full chain/co-chain discussion and optimization theorems), and Alecu–Atminas–Lozin–Malyshev DOI:10.1007/s00453-022-01019-6 (Sections 1–2 and later structure theorems). None states the exact same first-order rank-three classification. The proof requires exact finite certificate replay, and originality against all inaccessible or unindexed literature remains unproved. No external independent audit was carried out.

Self-review: passed. Independent audit: not yet performed.
