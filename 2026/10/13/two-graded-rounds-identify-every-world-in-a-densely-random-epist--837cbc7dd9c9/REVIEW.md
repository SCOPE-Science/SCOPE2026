# Scientific assessment: dense random-grid graded depth

## Correctness — PASS

The theorem is proved for every fixed density strictly between zero and one. The semantic base case gives depth-one graded types \((X_{ij},D_i,E_j)\); this is checked independently by the finite verifier. A deterministic sufficient criterion shows that pairwise uniqueness of all row and column marked-neighbor degree histograms forces depth-two singleton types. The key probability argument conditions on all columns with the two compared rows deleted; an exact cancellation identity reduces each histogram difference to an independent zero-sum test on a central bin. Fixed-density local binomial lower bounds supply \(\Theta(\sqrt n)\) occupied bins each containing \(\Theta(\sqrt n)\) columns; Fourier anti-concentration and a union bound then exclude all row and column collisions. Separate degree concentration excludes full depth-one separation, and the absence of monochromatic rows or columns gives an explicit two-class ordinary bisimulation. All quantifiers, the independence requirement, and the fixed-density boundary are explicit. Finite verification agrees with the deterministic intermediate signatures; it is supplementary rather than a substitute for the asymptotic proof.

Remaining limitations: the theorem says nothing uniform for changing densities; the finite verifier is finite and does not certify the analytic concentration bounds. Full external mathematical checking is not complete.

## Originality — PASS, subject to historical-priority risk

The fully inspected Ahvonen–Heiman–Kuusisto 2024 article introduces general graded multimodal types, message passing, and Weisfeiler–Leman correspondences, but not a Bernoulli row/column-equivalence-frame theorem, its exact depth-two threshold, or the independent-bin collision argument. Inspected portions of Nunn–Schwarzentruber 2023 concern graph-neural-network logical expressivity and decision problems, not a random-grid exact depth. The Babai–Erdős–Selkow 1980 random graph result is a canonical-labeling statement for ordinary random graphs and is not a direct claim about edge-colored complete bipartite incidence matrices reinterpreted as an \(n^2\)-world bimodal S5 model. Related prior mathematical work already gives maximal quotient ratios on explicit sparse grids and a Poisson limit for **ordinary** sparse random-grid definability; the asserted contribution is instead sharp two-round **graded** distinguishability at every fixed positive density.

Equivalence, broader coverage, exact-table, and implication searches found no statement proving this complete claim. Nonetheless, the classical random-bipartite color-refinement literature is dispersed, and an implicit stronger antecedent cannot be excluded without specialist review. A lack of search hits is not used as proof of priority.

## Mathematical value — PASS

This is a natural average-case expressivity question about the standard finite two-agent S5 product frame and one random propositional generator. The result simultaneously supplies a sharp constant depth, complete algebra generation, and maximal graded-versus-ordinary separation almost surely for all fixed nondegenerate densities. The new mechanism—many independent conditioned degree bins—is a reusable concentration argument for degree-profile refinement, rather than a low-dimensional case table. It contrasts substantively with both slow-depth structured examples and sparse isolated-row limits; it does not claim the already known abstract refinement correspondence or the extremal ratio itself as novel.

Self-review: passed. Independent audit: not yet performed.
