# Review of the cocktail-party dimer-jamming theorem

## Correctness

**PASS.** Every transition of the exact \((p,s)\) recurrence is derived by counting eligible edges. The one-pair survival probability and its telescoping products yield two-sided first-moment bounds. Distinct tagged pairs give the uniform second-factorial-moment estimate. Conditioning at an intermediate size and choosing \(k=\lfloor n^{1/5}\rfloor\) proves the \(3/(4n)+O(n^{-6/5})\) claim, with explicit handling of states containing zero, one, or multiple intact deleted pairs. The accompanying script independently checks labeled-vertex dynamics and the claimed finite bounds. Finite checks are not substituted for the proof.

## Originality

**PASS, qualified by literature-access risk.** The same uniform-edge algorithm is discussed by Dyer–Frieze (1991); Pippenger (1989) studies RSA including edge occupancy. Neither accessible abstract establishes a sharp rare-jamming constant on this dense cocktail-party family. Gamarnik–Goldberg's 2008 arXiv paper was inspected beyond the abstract, specifically its definition of the greedy matching process and the hypotheses/statements of Theorem 5 and Corollary 5: its fixed-degree, large-girth results are not the growing-degree, girth-three regime, and its normalized mean-size limits cannot determine the \(1/n\)-scale failure probability. Prior work on the same graph's acyclic orientations is mathematically unrelated, as is prior binary crown-graph jamming. Restricted full-text access to the 1989 and 1991 primary papers remains a specific uncertainty; no comprehensive novelty certification is claimed.

## Value

**PASS.** Removing a perfect matching is a sparse structured perturbation of the complete adsorption substrate. The complete graph never jams short, yet this perturbation generates a nonzero probability of incomplete matching at the \(1/n\) scale, which is invisible in the limiting occupied fraction. The nontrivial constant \(3/4\), quantitative convergence bound, and exact finite-size recursion provide a natural finite-network jamming benchmark. It is not a mere renaming or arbitrary finite slice.

## Scope and residual risks

Only identically distributed continuous edge priorities are covered, not arbitrary greedy matching tie-breaking or vertex-first algorithms. An equivalent specialized older result may have escaped searches, particularly in the unavailable full texts of Dyer–Frieze (1991) or Pippenger (1989). The theorem's asymptotic error exponent is not asserted sharp.

Self-review: passed. Independent audit: not yet performed.
